# Python PIP and Virtual Environments 🐍📦🔧

This document provides a guide on how to use essential tools and commands in Python for working with virtual environments and managing package dependencies efficiently.

## 1. Project description 👇
### _Creating and Activating Virtual Environments in Python 3._

To avoid conflicts between different versions of packages in different projects, it is recommended to isolate each project in its own virtual environment. This allows installing the correct version of each package in each project without affecting others.


When collaborating on Python projects that rely on specific versions of third-party packages, it is best practice to create a requirements.txt file listing all dependencies and their versions. The README should provide instructions for installing these dependencies using the following command:

```sh
pip install -r requirements.txt
```
_"The previous command is going to be mention further on-the-go"._

## **2. Minimal Functional Products ⚙️**

### 2.1. Game Project: Rock, Paper and Scissors

In order tu run the game, you must follow the instructions below, in the terminal:

```sh
cd game
python3 main.py
```
![rock, paper, scissors](https://preview.redd.it/do-you-want-the-rock-paper-scissor-to-make-a-return-in-v0-e2q6a423xtua1.gif?width=320&auto=webp&s=a932c4a85b1167f4d661daf330e47f9ef2ff05a1)
### Happy playing!

### 2.2. App Project: World Population

```sh
git clone
cd app
conda create --name app_env # Create environment
conda activate app_env
pip install -r requirements.txt
python3 main.py
```
![world population](https://i.pinimg.com/originals/a9/4b/6e/a94b6e53b4f5718cb3a537101f660104.gif)
### Happy research!

## **3. Technology stack 💻**

### Programming language:
- [Python](https://docs.python.org/3/)

### Python Libraries:
- [pandas](https://pandas.pydata.org/docs/reference/frame.html): For data manipulation and analysis.
- [numpy](https://numpy.org/doc/stable/): For mathematical operations and array manipulation.
- [matplotlib.pyplot](https://matplotlib.org/stable/contents.html): For data visualization.
- [requests](https://requests.readthedocs.io/en/latest/): For making HTTP requests in Python.
- [FastAPI](https://fastapi.tiangolo.com/advanced/custom-response/#html-response): For building APIs with Python based on standard Python type hints.

#### Distribution platform
- [Anaconda](https://www.anaconda.com/)

### Development tools: 
- [VSC](https://code.visualstudio.com/)

### Development environtments:
- [Windows Subsystem for Linux(WSL) - Ubuntu](https://learn.microsoft.com/en-us/windows/wsl/install)
- [Docker](https://docs.docker.com/)

## **4. Essential Commands in Anaconda PowerShell Prompt 📋**

### conda create --name [virtual environment]
This command creates a virtual environment at the specified path.

Working  with virtual environments in Python 3, is essential for isolating and encapsulating projects and their third-party packages, ensuring that **dependencies of one project do not interfere with those of another,** even when using the same Python version and operating system.

### pip (Preferred Installer Program)
The pip tool is used to install Python packages as dependencies in our projects. It simplifies the management of additional libraries and modules required for development.

### conda activate [virtual environment]
This command activates the virtual environment, allowing the use of dependencies installed within it.

### Managing Dependencies
Installing all packages from a requirements.txt file:

```sh
pip3 install -r requirements.txt
```
This command installs all packages listed in the requirements.txt file, along with their specific versions.

```sh
pip list > requirements.txt
```
Saving installed packages and their versions to a requirements.txt file.

This command saves the names and versions of all third-party packages installed in the current environment to the requirements.txt file.

**Note:** requirements.txt should be different for every specific project folder (if we think in Github Repo). This ensures that all team members install exactly the same versions of the required packages for every project.

### Installing Specific Packages
Installing a specific version of a package. **Example:**

```sh
pip install requests==2.27.1
```
This command installs version 2.27.1 of the requests package.

###  **Contact info📧**
For further information, reach me at andres.buelvas.diago.01@gmail.com
