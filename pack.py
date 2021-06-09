from cx_Freeze import setup, Executable

setup(
    name="TimeSeriesForecaster",
    version="0.1",
    description="test",
    executables=[Executable("source/client/main.py")])
