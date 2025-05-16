@echo off
:: Loop through all arguments passed to the script
for %%L in (%*) do (
    echo Checking for %%L...
    python -c "import %%L" 2>nul || (
        echo %%L is not installed. Installing...
        pip install %%L
    )
)
echo All libraries are now installed.
