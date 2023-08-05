# Setup

`pip install nd2-extractor`

For notebook use:

`jupyter nbextension enable --py widgetsnbextension`

# Usage

### From a notebook:

Then launch `nd2_extractor_interactive.ipynb` in a Jupyter notebook.

### From the command line

```
$ nd2_extractor --help
usage: nd2_extractor.py [-h] --ND2_directory ND2_DIRECTORY --save_directory SAVE_DIRECTORY --save_type SAVE_TYPE [--workers WORKERS] [--t_stop T_STOP] [--fill_empty]

Extract and ND2 file to TIFF or PNG (zarr coming soon).

optional arguments:
  -h, --help            show this help message and exit
  --ND2_directory ND2_DIRECTORY
                        The absolute directory of the ND2 file.
  --save_directory SAVE_DIRECTORY
                        The absolute directory of the extraction folder.
  --save_type SAVE_TYPE
                        The file type to save as (PNG/TIFF/zarr).
  --workers WORKERS     The number of joblib workers to send to the extractor.
  --t_stop T_STOP       Extract up until this timepoint.
  --fill_empty          If supplied, will fill empty frames with empty images, or skip saving them. Will be ignored if zarr chosen.
  ```