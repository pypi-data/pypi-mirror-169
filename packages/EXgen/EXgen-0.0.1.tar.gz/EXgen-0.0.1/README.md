# EXgen : 

Python library for automatically generating Exercise or Exam sheets from configuration files. 

## Install : 
Make sure that you have a working installation of Latex. Then you can proceede with the python install. Install the requirements by running : 
```bash
python -m pip install -r requirements.txt
```

Then you can install the library by running 
```bash
python -m pip install .
```
in the root directory of the library where the `setup.py` file is located.


## Example : 
Switch to the examples folder and under *GETUE-1* you will find the files needed to generate an exercise sheet for 4 groups. After changing the directory to *GETUE-1* just run : 
```bash
generate-ex UE1_config.yaml
```

Where `UE1_config.yaml` is the name of the main configuration file which is used to set up the exercise or exam. Further files which are used are the `schematic.net` files which contain netlists for the used networks. Then last but not least one needs to define their task latex structure and this is done in the `tasks.tex` file. These files can have arbitrary names, it is important to name them correctly in the config file. 