# Signals-And-Data-Autumn-2025
This repository contains the exercises for each week of the 02462 Signals and Data course at DTU for autumn 2025. 

Before beginning to use this environment, we recommend setting up a virtual environment using the below guide:

## Setup virtual environment using UV (recommended)

[UV](https://docs.astral.sh/uv/) is the cooler, newer sibling to Pip. Getting started with it is pretty straightforward, whether you already use conda or not.

1. **Install UV**:
   1. **If you have conda**, open a conda terminal and write `pipx install uv`. If this does not work, enter `pip install uv`. If this does not work, continue to step 2 to 3.
   2. **If don't have conda, and are on Windows**, open a powershell terminal and enter `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`
   3. **If you don't have conda and are on Linux/macOS**, open a terminal and enter `curl -LsSf https://astral.sh/uv/install.sh | sh`, if you do not have curl, enter `wget -qO- https://astral.sh/uv/install.sh | sh`
      1. **If you get an error with the MacOS operation above**, install with Homebrew instead. Firstly, install Homebrew using `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"` then run `brew install uv`
2. **Clone the git repository**:
   1.  **If you have git installed and are on windows**, enter *git bash* prompt and enter `git clone https://github.com/02462-Signals-and-Data/Signals-and-Data-Autumn-2025-student.git`
   2.  **If you have git installed and are on Linux/macOS**, enter a terminal and enter `git clone https://github.com/02462-Signals-and-Data/Signals-and-Data-Autumn-2025-student.git`
   3.  **If you do not have git installed**, follow [this guide](https://git-scm.com/downloads) to install git
   4.  **If you *for some reason*** don't want to use git, click "Code" and "Download ZIP" and unzip in the location you want to run it from
3.  **Sync UV environment**:
    1.  Enter the terminal you used to install UV (likely powershell if windows, regular terminal otherwise)
    2.  Navigate to the folder you copied the git repository to with `cd` followed by the path to the folder
    3.  Enter `uv sync` - this should install all necessary packages from the *uv.lock* file to a new folder called .venv
4.  **Open Jupyter notebooks:**
    1.  To use jupyter notebook directly:
        1.  Open a terminal with the copied git folder as the directory 
        2.  Write `uv run --with jupyter jupyter lab`
        3.  This should open up a jupyter notebook instance with all the packages installed by UV
        4.  Repeat this whenever you want to reopen jupyter notebook
    2.  To use notebooks in vscode:
        1.   Enter one of the week's exercises
        2.   Press ctrl+shift+p to open up the command window
        3.   Write "interpreter" and you should be able to see an option called "Python: Select Interpreter". Press enter.
        4.   Navigate to "Enter Interpreter Path" and press enter. 
        5.   It will prompt you for a path to the .venv folder. You can copy this by right-clicking the .venv folder and pressing "Copy Path".
        6.   Enter this copied path into the vs code prompt.
        7.   Following this, whenever you run a cell in a notebook for the first time, you should see your .venv folder as an option, select this.
        8.   If it does not prompt you automatically, enter the command window with ctrl+shift+p and write "Kernel". Select the option called "Notebook: Select Notebook Kernel".
        9.   Click "select other kernels"
        10.  Navigate to the interpreter that points to the .venv folder path
        11.  If done correctly, VSCode will now automatically suggest the same kernel for future use.

- If you feel any packages are missing, you always install them with `uv add package-name`, this will also add them to the *pyproject.toml* file present in the project. 
- Packages can be removed with `uv remove package-name` followed by `uv sync`. Running `uv lock`, reproduces the *uv.lock* file, and allows for you to export a 'snapshot' environment to potential collaborators.
- The reason we recommend uv as opposed to pip, is to avoid the typical problems of package mismanagement that comes with machine learning when dictated by pip. Usually this comes in the form of pip correctly installing a version of a package with depdencies, and then overwriting those dependecies when installing the next package. UV fixes this by having the *uv.lock* file define a specific 'tree' of dependency resolution, and not allowing subdependency mismatches between packages specified in the pyproject.toml file

## Setup virtual environment using pip (not recommended)

Here we require pip, so we assume you have conda or simliar program with access to pip installed

1. Follow step 2 above to clone the git repository

2. **Make a new conda environment** (not necessary, but HIGHLY recommended)
   1. Enter a conda prompt and write `conda create --name signals-and-data python=3.11 -y`
   2. Activate the new conda environment with `conda activate signals-and-data`
   3. Install the packages in the requirements.txt file with `pip install -r requirements.txt` (make sure you are in the same folder as the requirements.txt file!)
3. **Open Jupyter notebooks:**
   1. To use jupyter notebook directly:
      1. Open a conda terminal
      2. Ensure you have the correct virtual environment chosen by running `conda activate signals-and-data`
      3. Enter `jupyter notebook` to open a jupyter notebook
   2. To use notebooks in vscode:
      1. Open any of of the week's exercises
      2. Enter ctrl+shift+p to enter the command window
      3. Write 'Python', you should see an option called "Python: Select enterpreter", choose this
      4. Under conda environments, you should be able to see one called 'signals-and-data' choose this
      5. When running a jupyter notebook cell, you should be prompted to select a kernel
      6. Click "select another kernel"
      7. Click "python environments"
      8. Choose the aforementioned newly created Python environment "signals-and-data"
  
- We assume you can install and remove packages using pip yourselves
- A warning, pip doesn't have a very good dependency solver, and you may run into issues where it wants to install one package that depends on a specific version of subdependency A, while later installing another package which depends on another version of subdependency A, this will cause pip to overwrite the version of subdependency A based on whatever package that requires it was installed last. 

## *Not* setting up a new virtual environment and running it in a base Python environment

**Don't** do this. It's not just for funsies we setup virtual environments. Stuff *will* break so long as you have any other course than this.

Just setup the virtual environment

## Pulling updates

During the course, we will both upload new material durig the weeks, as well as occasionally update existing material. To access these new updates, simply navigate to your project repository, open a terminal and write:

```git pull --rebase --autostash```

This **should** automatically do the following:

1. Stash your saved changes to the exercises
2. Pull the remote changes while rebasing your version to be placed at the 'head' of the git history
3. Apply your stashed changes on top of these pulled changes.

**Warning:** This might cause problems if we have pushed changes to an exercise **after** you have made changes to it. In this case our new changes will either be overwritten by your local changes, or simply 'coexist' with your changes, meaning some code blocks might not make sense any longer. 

You are of course free to use your own methods of pulling and such, but using this method automatically stashes and reapplies your local changes. Meaning:

1. Git doesn't complain about you not having commited or stashed your changes
2. Git does not overwrite your precious changes to existing weeks (in case we change something in the previous weeks to fix and error, for example)
3. **HOWEVER** in the case of 2. it *might* lead to merge conflicts and the like, as your local changes are applied willy-nilly on the remote changes.

