# Python skeleton app

A very simple Python skeleton app for use with Python 3.

- Change the `CoolPackageName` folder to the name of your project/package.
- Change `cool_file_name.py` to a meaningful filename.
- Change `test_cool_file_name.py` to the filename chosen above. Be sure to let that file name start with `test_` though! That way, py.test can automagically detect and run the tests within.

Need some extra information? Check [Jean-Paul Calderone's](http://as.ynchrono.us/2007/12/filesystem-structure-of-python-project_21.html) well explained blog post for how to structure your Python projects.

## Requirements

- Python 3
- PyPI for Python 3 (`pip`)
- Possibly [Virtualenv](https://virtualenv.pypa.io/en/stable/userguide/) to avoid dependency collisions between projects

## Installation

### Windows / macOS / Linux

```shell
$ git clone $(this.repo)
$ cd $(this.repo)
$ pip install -r requirements.txt
$ pytest --cov=.
```

### Vagrant

Alternatively, you could create a virtual machine with the accompanying Vagrantfile:

```shell
$ git clone $(this.repo)
$ vagrant plugin install vagrant-vbguest
$ vagrant up
$ vagrant ssh
$ cd /code
$ pytest --cov=.
```

### Tesseract

First download and install the exe from the [Mannheim University Git](https://github.com/UB-Mannheim/tesseract/wiki).


Make sure you install it in drive, you going to run your programs on.

Later run this in your favorite CLI:

```
$ pip install pillow
$ pip install pytesseract
```



For further reading:


[www.pyimagesearch.com](https://www.pyimagesearch.com/2017/07/10/using-tesseract-ocr-python/)

[www.developer.ibm.com](https://developer.ibm.com/tutorials/document-scanner/)

