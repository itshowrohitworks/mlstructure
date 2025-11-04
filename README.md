# ML Project Structure

# Getting Started
## PrerequisitesPython: 
Ensure you have Python 3.x installed.Virtual Environment: Highly recommended for dependency isolation.📦 InstallationTo set up the project locally for development:
1. Clone the RepositoryBashgit clone https://github.com/itshowrohitworks/mlstructure.git
cd mlstructure
2. Create and Activate a Virtual EnvironmentBash:
uv venv 
I used uv package to make the virtual env.

## Activate (Example for macOS/Linux)
source .venv/bin/activate

3. Install the ProjectInstall all dependencies and the package itself in editable mode for development.Bash# Installs dependencies listed in setup.py (which uses requirements.txt)

## The -e flag allows source code changes to be reflected instantly.
uv pip install -e .

# Project Architecture & File NotesThese notes explain the purpose of your key configuration files.
setup.py AnalysisThis file is the core configuration for installing your Python package.ComponentCode ReferencePurposeget_requirements functionget_requirements('requirements.txt')A custom function designed to read the required package names from your requirements.txt file and return them as a list for setup().hypen_e_dot handlingif hypen_e_dot in requirements: ...This logic intentionally checks for and removes the specific string -e . from your requirements list. This is necessary because -e . is a development-only flag that should not be passed to the install_requires argument when building the package for distribution.packagespackages=find_packages()Automatically finds all folders that contain an __init__.py (like your src/ folder) and registers them as installable modules.install_requiresinstall_requires = get_requirements(...)Passes the final list of dependency names (like numpy, pandas) to setuptools so they are automatically installed when a user runs uv pip install mlstructure.

# Key Files and Directories setup.py: Defines all package metadata and dependencies, making the project installable.

requirements.txt: A plaintext list of all third-party libraries needed (e.g., numpy, pandas).

src/: Contains the actual, clean source code for the mlstructure package.

.gitignore: Tells Git to ignore temporary files (like venv/ or compiled .pyc files).

# Git Reference NotesThese are the essential Git commands for maintaining the project on GitHub.
Initial Repository Setup (One-Time per Branch)This command sets your local branch (main) to track the remote branch (origin/main), so you don't need to specify them again.
git push -u origin main

## Regular Workflow CommandsCommandPurposegit statusShows which files have been modified, staged, or are untracked
.git add . -> Stages all current changes for the next commit.

git commit -m "Your descriptive message" -> Records the staged changes locally.

git push -> Pushes the local commits to the tracking remote branch (origin/main).

git pull -> Fetches and merges changes from the remote repository.