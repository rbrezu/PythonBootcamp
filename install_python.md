### Installing Python on Windows

Python is not usually included by default on Windows, however we can check if any version exists on the system. Open the command line–a text-only view of your computer–via PowerShell which is a built-in program.

Go to Start Menu and type “PowerShell” to open it.

Type the following command and hit the Enter/Return key:

```shell
$ python --version
Python 3.7.0
```

If you see output like this, Python is already installed. But most likely it is not. So…let’s install Python.

Go to the [downloads](https://www.python.org/downloads/) section of the official *Python* website. 
Download the installer and make sure to click the box on the bottom of the page for the Add Python 3.7 to `PATH` option, 
which will let use use python directly from terminal. 
Otherwise we’d have to enter our system’s full path and modify 
our environment variables manually. 
 
### Install jupyter notebook and ipython

```shell
$ pip install ipython jupyter
```
 