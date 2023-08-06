# VKML -- Virtual Kinetics of Materials Laboratory

Authors: A. Surya Mitra, J. Lund, A. Bartol, D. R. Ely, R. Edwin García.

If you use this software in academic work, please cite the relevant references detailing its development as presented in the `LICENSE` file.

VKML provides user interface to develop, modify and execute applications. The developed interface provides a TKInter-based GUI, which enables the user to rapidly prototype flexible interfaces with sliders, menus, buttons and tooltips. The interface  supports editing parameters through commands which allows command scripting.  

Older versions can be found and run directly online (cloud computing) at [https://nanohub.org/resources/vkmllive]

[1] Bartol, A., Ely, D. R., Guyer, J., García, R. E. The Virtual Kinetics of Materials Laboratory. 2015.

## Installation

Installation is similar to other Python libraries

The executive summary of steps is:
```
tar -xzvf VKML.tar.gz
cd VKML
python setup.py install
```
## Prerequisites

The current version of VKML has been tested on Linux (Ubuntu 14.0.6), Mac OS X (Catalina and Big Sur), and Windows (10). The following are required libraries for installation:

- [Python v2 or v3](http://www.python.org) .
- Mac OS X users will need to install an [*X11 server*](http://xquartz.macosforge.org/).
- `tkinter` module is a built-in python installation, but the user should make sure that the admin did not optout (in which case he/she should install it). 

## Procedure

Download `VKML.tar.gz` to a suitable folder. 
### 1.Unpack

  Unpack the .tar.gz file.  Typically, just run `tar -xzvf` on the
  file you want to unpack.  This will create a subdirectory named
  "VKML" in the directory where you run tar command.

### 2. Install

Switch to the newly-created directory after unpacking 'VKML', 

```
cd VKML

```
To install VKML, run the command 

```
python setup.py install
```
This will install VKML in the standard location for Python
extensions on your system. 

VKML can be installed in a different location:

```
python setup.py install --prefix=<prefix>
```
<prefix> is the directory where you want to install. If <prefix> is not in your Unix command path, you'll need to add it to the PATH environment variable. 

## Using VKML

1. After installation, VKML should be imported into python  as `from VKML.gui.tk import Parameter, Parser, Menu` .  See `example/testVKML.py` for a detailed description on how to use the VKML library. 
2. A parser is created as `p=Parser(title='Title for GUI',help_text='path for the description file for the current GUI')`. By default `help_text=""` 
3. In the parser `p` menus can be created as ` menu1 = Menu(title='Title for this menu', parser=p)` and `menu2 = Menu(title='Title for this menu', parser=p)`.
4. Each of these menus has parameters defined as `parName1=Parameter(name='parName1',display_name='Display name of the parameter or description',variable=<type of the variable>, menu=<name of the menu where this parameter exist>, default=<default value of this parameter to display>,tooltip='A tooltip description of the parameter',show_par=<Flag to display-'True' or hide the parameter -'False'>)`.  By default `tooltip=''` and `show_par='True'`. 
5. Creating Parameters for Menus: different types of parameters are possible in a menu using different variable types. The type of variables available are `'label', str, tuple, 'file', 'function', bool, list, float or int`
    * A `'label'` variable type creates a label in the menu : `Parameter(name='Name of the label', menu=<menu variable name>, variable='label')`
    * To create a variable with a dropdown options use a variable type of `tuple`. 
    * To allow user input text or values, variable type of `str` is used. 
    * Variable type `'file'` is used to allow user to browse and choose files.
    * Variable type `bool` creates a check box to allow user to choose true or false.
    * `list` allows user to input list using GUI, the user will be prompted with `Modify` button to edit the list in a new window. In the new list window, click `Update` button to update the list with new values and close the window, while `Cancel` just closes the window without updating the values.
    * `float` or `int` creates a slider for user to adjust the required value among a specified range of values.
    * `'function'` is used to create a button which runs the specified function.
6. The python code can be run in both graphical user interface (GUI) as well as through command line (CLI). 
    * For example:  To run the VKML example  `example\testVKML.py` can be run in GUI mode as `python testVKML.py --gui`.
    * To run in CLI mode `python testVKML.py --<parameterName1>=<parameterValue1> --<parameterName2>=<parameterValue2>`

## Uninstalling

To uninstall VKML in the terminal use `pip uninstall VKML` command.

## Acknowledgements

This work was partially supported by the Toyota Reaseach Institute (TRI), from October 2019 to February, 2021. 

## How to cite this work
A. Surya Mitra, J. Lund, A. Bartol, D. R. Ely, R. Edwin García. "VKML: Virtual Kinetics of Materials Laboratory," https://github.itap.purdue.edu/garciagroup/VKML February 2021.
