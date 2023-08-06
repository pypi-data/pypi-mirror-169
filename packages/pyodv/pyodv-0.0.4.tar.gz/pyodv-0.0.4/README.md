# pyODV               [![Upload Python Package](https://github.com/vliz-be-opsci/pyodv/actions/workflows/python-publish.yml/badge.svg)](https://github.com/vliz-be-opsci/pyodv/actions/workflows/python-publish.yml) [![Checking Master Branch](https://github.com/vliz-be-opsci/pyodv/actions/workflows/build-master.yml/badge.svg)](https://github.com/vliz-be-opsci/pyodv/actions/workflows/build-master.yml)
 

Python package for reading ODV (Ocean Data Variables)  and Bio-ODV files. This tool is intended to assist with scripts that use ODV/BioODV files as an input. The files can be parsed, validated and exposed as python objects. 

The specifications for BioODV and ODV file formats are taken from [here](https://www.seadatanet.org/content/download/636/file/SDN2_D85_WP8_Datafile_formats.pdf) and [here](https://www.seadatanet.org/content/download/638/file/SDN2_D84b_WP8_ODV_biology_variant_format%20guidelines.pdf) respectively.

## Setup
The library is available [from PyPi](https://pypi.org/project/pyodv/) and can be installed with:

```
pip install pyodv
```
This does not install the dependancies that are required by pyodv. This can be done with:
```
pip install pandas>=1.3.4 xmltodict>=0.13.0 beautifulsoup4>=4.11.1
```
or by using the requirement.txt file in the github repository. 

## Usage 

This pyODV package reads ODV and BioODV files and seperates the semantic header, dataset attributes, data columns and data quality columns. It's makes these items available as pytohn dicts or pandas dataframes. 

Below is a quick example of reading one of the ODV files included in the test directory:

```python
import pyodv

test_file = './test_files/ODV_timeseries_chemical_data.txt' 
parsed_file = pyodv.ODV_Struct(test_file) 
```
The parsed_file object has several child objects and functions. Here are several of interest:
  
  - parsed_file.df_data: ODV metadata columns. These are strictly defined in the ODV and BioODV spec docs. 
  - parsed_file.df_var: Dataframe containing ODV variables.
  - parsed_file.df_qc: Dataframe containing ODV quality variables. There should be one QC cell per variable cell
  - parsed_file.cols: List of columns avialable in the ODV file
  - parsed_file.params: Semantic paramater header items, as a python dictionary.
  - parsed_file.refs: Links to external references listed in ODV header, as a python dictionary.
  
## Future Work
Currently the ODV/BioODV files used for development are limited to those available [here](https://www.seadatanet.org/Standards/Data-Transport-Formats). These example files seem to be output from the same tool-chain so any differences with ODV files "out in the wild" have not been considered. It would be worth while to expand source, creation tools, and style of the ODV files in the test directory. 

The ODV parsing tool can be improved with:
  
  - improve limited testing currently done on the data struct
  - handle several common use cases:
    - write to file,
    - push data to database,
    - convert to some other format (csv, DWCa, TTL, etc)
  - More comprehensive parsing of the semantic header:
    -  retrieve link URLs for vocab terms
    -  check URLs are valid, correctly formatted and available
    -  check the units used in the columns comply with those defined in semantic parameter header
  - Better data structure:
    - Multiple dataframes are not the best structure for complex slicing. XArray might be a better tool but also does not seem to treat data parameters well. 

## Testing 

There are several options available in the make file to build, test, setup, or document the project. Some examples are:


    $ make test                                                   # to run all tests
    $ PYTEST_LOGCONF=debug-logconf.yml python tests/test_demo.py  # to run a specific test with specific logging


Check the code-style and syntax (flake8)


    $ make check
