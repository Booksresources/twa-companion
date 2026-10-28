# Listing 2.1: Creating and activating a virtual environment
python -m venv twa-env

# Activate it (choose the line for your system)
twa-env\Scripts\activate          # Windows
source twa-env/bin/activate        # macOS and Linux

# Install the core libraries
pip install pandas numpy matplotlib seaborn scikit-learn jupyterlab
