# Setting up a Virtual Environment

## Creating a Virtual Environment

In BASH, run `py -m venv ./venv`

## Activating Virtual Environment

1. Navigate to the `venv/Scripts` directory. Run `. activate`. Your virtual environment is activated.

## Select an Interpreter

Go down to the bottom right of VSCode and find where it mentions Python. Click that and then navigate to your virtual environment's `python.exe` file, which should be in `venv/Scripts`.

## Installing Modules from a `requirements.txt` file
Simply run the following command:
- `pip install -r requirements.txt`