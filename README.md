# tech-console
Technician console for project Helios LARP.

## Installation instructions
### Ubuntu >18.04
#### Prerequisites
* python >3.6.6
* python3 development headers
* gcc
* make
* git
* pipenv
* python3 pip

To install prerequisites on Ubuntu 18.04 run the following
```bash
sudo apt install -y python3 python3-dev gcc make git python3-pip
pip install pipenv
```

#### Installation
Clone the git repository
```bash
git clone git@github.com:gmyuval/tech-console.git
```
Run the setup script
```bash
cd tech-console
./setup.sh
```

### Windows
#### Prerequisites
* python >3.6.6
* git
* pip
* pipenv

To install prerequisites on Windows 10 perform the following
* Download and install python 3 from [https://www.python.org/ftp/python/3.7.1/python-3.7.1-amd64.exe](https://www.python.org/ftp/python/3.7.1/python-3.7.1-amd64.exe)
* Download and install git for windows

From commandline run:
```cmd
pip install pipenv
```

#### Installation
Clone the git repository
```cmd
git clone git@github.com:gmyuval/tech-console.git
```

Run the setup script
```cmd
cd tech-console
setup.bat
```

## Usage
To use tech-console, execute the enclosed run bash script as follows
### Linux
```bash
./run.sh
``` 
### Windows
```cmd
run.bat
```