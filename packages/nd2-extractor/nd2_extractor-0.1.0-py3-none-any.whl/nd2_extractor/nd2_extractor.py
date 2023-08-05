import pprint
from pims import ND2Reader_SDK
pp = pprint.PrettyPrinter(indent=0)
from tabulate import tabulate
from tqdm.auto import tqdm 
import cv2
import numpy as np
from cowpy import cow
from termcolor import colored
from joblib import Parallel, delayed, parallel_backend
import yaml
import argparse
import os

def greeting():
    cheese = cow.Turtle()
    msg = cheese.milk("BakshiLab FAST ND2 Extractor - By Georgeos Hardo")
    print(msg)

def predict_t(directory): 
    frames =  ND2Reader_SDK(directory)
    frames.default_coords["t"] = 0
    t = 0
    while True:
        try:
            frames[t]
            t = t+1
        except:
            break
    frames.close()
    return int(t)

def predict_FOVs(directory):
    frames =  ND2Reader_SDK(directory)
    i = 1
    frames.default_coords["m"] = 0
    x_um = [frames[0].metadata["x_um"]]
    y_um = [frames[0].metadata["y_um"]]
    frames.default_coords["m"] = i
    while (x_um[0] != frames[0].metadata["x_um"] or y_um[0] != frames[0].metadata["y_um"]):
        frames.default_coords["m"] = i
        x_um.append(frames[0].metadata["x_um"])
        y_um.append(frames[0].metadata["y_um"])
        i+=1
    frames.close()
    return int(len(x_um) - 1)


def save_image(frame, i, img_format,save_directory,FOV,IMG_CHANNELS,channel, fill_empty=False):
    if (np.sum(frame) == 0) and fill_empty: # Check if a frame is empty, as Nikon inserts empty frames when you have some channels being read ever n frames.
        pass
    else:
        if img_format.lower() in "tiff":
            cv2.imwrite(save_directory + 'xy{}_{}_T{}.tif'.format(str(FOV).zfill(3),IMG_CHANNELS[channel],str(i).zfill(4)), frame, [cv2.IMWRITE_TIFF_COMPRESSION, 1])
        elif img_format.lower() in "png":
            cv2.imwrite(save_directory + 'xy{}_{}_T{}.png'.format(str(FOV).zfill(3),IMG_CHANNELS[channel],str(i).zfill(4)), frame)
        else:
            raise Exception("Invalid format, please choose either TIFF or PNG")

def zarr_saver(frame, zarr_file, m, t, c):
    zarr_file[m,t,c] = frame

def main_loop(directory,save_directory, joblib_workers, save_type = None, t_stop=None, fill_empty=False):
    # Get parameters of the experiment
    frames =  ND2Reader_SDK(directory)
    metadata_dir = os.path.dirname(os.path.dirname(directory))
    with open(metadata_dir+'metadata.yml', 'w') as outfile:
        yaml.dump(frames.metadata, outfile, default_flow_style=False)

    IMG_HEIGHT = frames.metadata["tile_height"]
    IMG_WIDTH = frames.metadata["tile_width"]
    IMG_CHANNELS_COUNT = frames.metadata["plane_count"]
    SEQUENCES = frames.metadata["sequence_count"]
    IMG_CHANNELS = []
    for x in tqdm(range(IMG_CHANNELS_COUNT), desc = "Getting experiment info - please wait"):
        IMG_CHANNELS.append(frames.metadata["plane_{}".format(x)]["name"])
    frames.close() 
    num_FOVs = frames.sizes["m"]
    if t_stop:
        num_t = t_stop
    else:
        num_t = frames.sizes["t"]
    if not t_stop:
        assert int(SEQUENCES / num_FOVs) == num_t, "FOVs ({}) and timepoints ({}) do not match sequences ({}) in the experiment - check your inputs".format(num_FOVs,num_t,SEQUENCES)
    print(colored("Experiment parameters (please verify before proceeding with extraction".format(num_FOVs), 'blue', attrs=['bold']))
    print(tabulate([
        ['TIMEPOINTS', num_t],
        ['FOVs', num_FOVs],
        ['IMG_HEIGHT', IMG_HEIGHT], 
        ['IMG_WIDTH', IMG_WIDTH],
        ["IMG_CHANNELS_COUNT", IMG_CHANNELS_COUNT],
        ['IMG_CHANNELS', IMG_CHANNELS]], headers=['Parameter', 'Value'], tablefmt='orgtbl'))


    if save_type:
        img_format = save_type
    else:
        print(colored("Choose image format: (TIFF/PNG) ", 'red', attrs=['bold']))
        img_format = input()


    FOVs_list = list(range(num_FOVs))
    CHANNELS_list = list(range(IMG_CHANNELS_COUNT))
    

    if save_directory[-1] != "/":
        save_directory = save_directory + "/"
    if save_type == "zarr":
        try:
            save_directory = os.path.dirname(save_directory)+".zarr"
            os.mkdir(save_directory)
        except:
            pass
    else:
        try:
            os.mkdir(save_directory)
        except:
            pass



    if save_type == "zarr":
        import zarr
        from numcodecs import Blosc
        from bz2 import compress

        zarr_dim = (num_FOVs, num_t, IMG_CHANNELS_COUNT, IMG_HEIGHT, IMG_WIDTH)
        chunk_size = (1,1,1,IMG_HEIGHT, IMG_WIDTH)
        zarr_dtype = {
            16: np.uint16,
            8: np.uint8
        }

        compressor = Blosc(cname='zstd', clevel=6, shuffle=Blosc.BITSHUFFLE)
        zarr_file = zarr.open(save_directory, mode='w', shape=zarr_dim, chunks=chunk_size, dtype=zarr_dtype[frames.metadata["bitsize_memory"]], compressor = compressor)

    with ND2Reader_SDK(directory) as frames:
        for FOV in tqdm(FOVs_list, desc = "Overall (FOV) progress"):
            for channel in tqdm(CHANNELS_list, desc = "Channel progress in FOV {}".format(FOV), leave = False, position = 1):
                frames.iter_axes = 't'
                try:
                    frames.default_coords['c'] = channel
                except:
                    pass
                frames.default_coords['m'] = FOV
                if save_type == "zarr":
                    Parallel(prefer="threads", n_jobs = joblib_workers)(delayed(zarr_saver)(frames[t], zarr_file, FOV, t, channel) for t in tqdm(range(num_t), desc = "Frame progress in channel {}".format(IMG_CHANNELS[channel]), leave = False, position = 2) )
                else:
                    Parallel(prefer="threads", n_jobs = joblib_workers)(delayed(save_image)(frames[i], i, img_format,save_directory,FOV,IMG_CHANNELS,channel,fill_empty) for i in tqdm(range(num_t), desc = "Frame progress in channel {}".format(IMG_CHANNELS[channel]), leave = False, position = 2) )

 
def main():
    parser = argparse.ArgumentParser(description="Extract and ND2 file to TIFF or PNG (zarr coming soon).")
    parser.add_argument("--ND2_directory", type=str, nargs=1, help="The absolute directory of the ND2 file.", required=True)
    parser.add_argument("--save_directory", type=str, nargs=1, help="The absolute directory of the extraction folder.", required=True)
    parser.add_argument("--save_type", type=str, nargs=1, help="The file type to save as (PNG/TIFF/zarr).", required=True)
    parser.add_argument("--workers", type=int, default=50, nargs=1, help="The number of joblib workers to send to the extractor.")
    parser.add_argument("--t_stop", type=int, nargs=1, help="Extract up until this timepoint.")
    parser.add_argument("--fill_empty", action="store_const", const=True, default=False, help="If supplied, will fill empty frames with empty images, or skip saving them. Will be ignored if zarr chosen.")
    args = parser.parse_args()
    print(args)
    main_loop(  
        args.ND2_directory[0], 
        args.save_directory[0], 
        args.workers[0], 
        args.save_type[0], 
        args.t_stop[0], 
        args.fill_empty
        )


if __name__ == "__main__":
    main()