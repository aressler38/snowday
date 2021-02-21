python -m pip check
IF %ERRORLEVEL% NEQ 0 (
    pip install .
)
echo "running the game..."
python snowday\main.py
