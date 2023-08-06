# virtialsmoke
We used empirical data to build a virtual smoke detector or a model to predict fire alarm from environmental variables
## Installation
Install the package as follows:
```
python3 -m pip install virtualsmoke
```
## Usage
### As a CLI
The package can be used as a commandline interface or in a script. For CLI the following options must be provided:
```
NAME
    smoke.py

SYNOPSIS
    smoke.py T H P

POSITIONAL ARGUMENTS
    T
    H
    P

NOTES
    You can also use flags syntax for POSITIONAL ARGUMENTS
```
### In the script
```
from virtualsmoke.smoke import signal
print(signal(T,H,P))
```
Where T is the surrounding or surface temperature in Kelvin, H is the relative humidity (%), and P is the barometric pressure in hectopascal (hPa).  
The model will calculate the mean free path of air, which is the main indicator for sensing fires.
