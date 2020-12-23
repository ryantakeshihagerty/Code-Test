# Code-Test
weather_difference.py takes a formatted .dat file of daily weather data, and outputs the day with the smallest temperature spread. If no filename is provided through the command-line, program will default to 'w_data.dat'.

goal_difference.py takes a formatted .dat file of soccer stats, and outputs the team with the smallest goal difference. Like weather_difference.py, the program will default to using 'soccer.dat' if no filename is provided.

# How to run
NOTE: For Windows 10 and Python 3.7.7
1. Make sure the appropriate .dat files and .py files are in the same directory
2. Go to that same directory in Command Prompt
3. In the command prompt, run
```sh
py -m pip install pandas
```
4. Run the app
```sh
py weather_spread.py (OPTIONAL_FILE_NAME.dat)
py goal_difference.py (OPTIONAL_FILE_NAME.dat)
```
