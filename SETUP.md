# Setup Instructions

This document provides detailed instructions for setting up your development environment for the Genome Analysis ML project.

## Prerequisites

### Required Software
1. **Python 3.9 or later**
   - Download from [python.org](https://www.python.org/downloads/)
   - During installation on Windows, check "Add Python to PATH"
   - Verify installation:
     ```bash
     python --version
     ```

2. **Git**
   - Download from [git-scm.com](https://git-scm.com/downloads)
   - Verify installation:
     ```bash
     git --version
     ```

3. **VSCode** (Recommended IDE)
   - Download from [code.visualstudio.com](https://code.visualstudio.com/)
   - Recommended extensions:
     - Python
     - Jupyter
     - Git Graph

## Project Setup

### 1. Clone the Repository
```bash
git clone https://github.com/JerryMcDonald/genome-analysis-ml
cd genome-analysis-ml
```

### 2. Set Up Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
# Install required packages
pip install -r requirements.txt
```

## Development Environment

### Running Jupyter Notebooks
1. Ensure your virtual environment is activated (you should see `(venv)` in your terminal)
2. Start Jupyter:
   ```bash
   jupyter notebook
   ```
3. Navigate to the `notebooks` directory to access project notebooks

### VSCode Configuration
1. Select Python Interpreter:
   - Press `Ctrl+Shift+P` (Windows) or `Cmd+Shift+P` (Mac)
   - Type "Python: Select Interpreter"
   - Choose the interpreter from your virtual environment

2. Git Configuration in VSCode:
   - Open Source Control panel (Ctrl+Shift+G)
   - Sign in to GitHub if prompted

## Troubleshooting

source activate base
conda activate genome-env

## Going forward, when you need to add new packages:

Add them to environment.yml
Run conda env update -f environment.yml


### Common Issues

1. **Python not found in PATH**
   - Solution: Reinstall Python and ensure "Add Python to PATH" is checked

2. **Virtual environment not activating**
   - Windows Solution: Run PowerShell as administrator and execute:
     ```powershell
     Set-ExecutionPolicy RemoteSigned
     ```

3. **Package installation fails**
   - Ensure virtual environment is activated
   - Try updating pip:
     ```bash
     python -m pip install --upgrade pip
     ```

### Need Help?
If you encounter issues:
1. Verify Python installation and PATH
2. Check virtual environment activation
3. Contact project maintainers for support

## Next Steps
- Review the notebooks in the `notebooks` directory
- Check project tasks in Trello
- Join the project's Google Space for team communication