
pip show --files snowday

IF %ERRORLEVEL% NEQ 0 (
    echo "I am going to try and install the game now."
    pip install .
)

echo "running the game..."
python snowday\main.py
