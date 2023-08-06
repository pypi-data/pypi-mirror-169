import setuptools
import platform

if platform.system()=='Windows':
    setuptools.setup(
        name='VKML',
        version='1.2',
        description='VKML: Virtual Kinetics of Materials Laboratory',
        author='Surya Mitra, Edwin Garcia, Alex Bartol, Jarrod Lund',
        author_email='sayalaso@purdue.edu,redwing@purdue.edu',
        url="https://github.itap.purdue.edu/garciagroup/VKML",
        packages=['VKML','VKML.gui','VKML.gui.tk'],
        license = "GNU GPLv3"
    )
    
else:
    setuptools.setup(
        name='VKML',
        version='1.2',
        description='VKML: Virtual Kinetics of Materials Laboratory',
        author='Surya Mitra, Edwin Garcia, Alex Bartol, Jarrod Lund',
        author_email='sayalaso@purdue.edu,redwing@purdue.edu',
        url="https://github.itap.purdue.edu/garciagroup/VKML",
        packages=['VKML','VKML.gui','VKML.gui.tk'],
        license = "GNU GPLv3",
    )
