
# Python Bootcamp

## Introduction

Python is a modern, robust, high level programming language. It is very easy to pick up even if you are completely new to programming. 

Python, similar to other languages like matlab or R, is interpreted hence runs slowly compared to C++, Fortran or Java. However writing programs in Python is very quick. Python has a very large collection of libraries for everything from scientific computing to web services. It caters for object oriented and functional programming with module system that allows large and complex applications to be developed in Python. 

These lectures are using jupyter notebooks which mix Python code with documentation. The python notebooks can be run on a webserver or stand-alone on a computer.

To give an indication of what Python code looks like, here is a simple bit of code that defines a set $N=\{1,3,4,5,7\}$ and calculates the sum of the squared elements of this set: $$\sum_{i\in N} i^2=100$$


```python
N={1,3,4,5,7}
print('The sum of ∑_i∈N i*i =',sum( i**2 for i in N ) )
```

    The sum of ∑_i∈N i*i = 100

## Installation

You will have a few prerequisites before starting this tutorial:

* Install [Git](install_git.md) 
* Install [Python](install_python.md)
* Login with your Git account on our [JupyterHub](https://jhub.whitesoftware.ro) for homework

## Contents

This course is broken up into a number of weeks (chapters).
You can view the files as html or can interact with them using jupyter notebook.

### 1. Basic Knowledge and Data Types

* **01** [html](html/01_week/01_numbers.html) [notebook](notebooks/01_week/01_numbers.ipynb) Basic data types and operations (numbers, strings) 
* **02** [html](html/01_week/02_strings.html) [notebook](notebooks/01_week/02_strings.ipynb) String manipulation 
* **03** [html](html/01_week/03_data1.html) [notebook](notebooks/01_week/03_data1.ipynb) Data structures: Lists and Tuples
* **04** [html](html/01_week/04_data2.html) [notebook](notebooks/01_week/04_data2.ipynb) Data structures (continued): dictionaries
* **05** [html](html/01_week/05_flow.html) [notebook](notebooks/01_week/05_flow.ipynb) Control statements: if, for, while, try statements
* **06** [html](html/01_week/06_functions.html) [notebook](notebooks/01_week/06_functions.ipynb) Functions
   


### Other materials and websites

For a quick reminder / summary of Python syntax the following [Quick Reference Card](http://www.cs.put.poznan.pl/csobaniec/software/python/py-qrc.html) may be useful. 

A longer and more detailed tutorial style introduction to python is available from the python site at: https://docs.python.org/3/tutorial/
