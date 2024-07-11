# mascot.ai

## Table of Content

* [Step 1 - Run the Program](#step-1---run-the-program)
    * [Download the Pre-buit Binary](#download-the-pre-buit-binary)
    * [Run the Python File Directly](#run-the-python-file-directly)
* [Step 2 - Feed audio to, e.g. VTube Studio](#step-2---feed-audio-to-eg-vtube-studio)
* [Building an Executable Yourself](#building-an-executable-yourself)

# Step 1 - Run the Program

## Download the Pre-buit Binary

- You can download and simply run the pre-buit binary for the Windows from the [releases](https://github.com/CheapNightbot/mascot.ai/releases/latest) page or please refer to the [building the binary](#building-an-executable-yourself) section down below.

- If you chose to download the pre-buit binary, you can skip to the [Step 2](#step-2---feed-audio-to-eg-vtube-studio).

## Run the Python File Directly

- Make sure [git](https://git-scm.com/) is already installed and then clone this repository to your local machine:

    - `git clone https://github.com/CheapNightbot/mascot.ai.git`

    - `cd` into the "mascot.ai" directory.

- [OPTIONAL] Create a Python [Virtual Environment](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/):

    - `python -m venv env`

    - Now, activate the virtual environment by running `source env/Scritps/activate`. Make sure to run this inside the "Git Bash" terminal as "Powershell" does not allow you to directly run such commands without changing the "execution policy".

- Install required packages:

    - `pip install -r requirements.txt`

- Run it:

    - If you are in the parent directory: `python src/mascot_ai.py`
    - Or change directory inside "src": `cd src/` and then `python mascot_ai.py`

- It will now prompt for the "Video ID" of a Live Stream, which is just a 11 characters long string. It will be like this "**cpKdPfyJRdk**" after the `=` sign in the URL bar: "**https://www.youtube.com/watch?v=**".

    - Just copy and paste this ID of your or any live stream and hit return/enter key.

- If everything goes well, the terminal should print the live chat with the author name, time and actual message sent in the chat. And you will be able to hear the message being read aloud.

- Remember: `ctrl` + `c` is your friend. :D

# Step 2 - Feed Audio to, e.g. VTube Studio

- TODO!

- I got lazy.. (_　_)。゜zｚＺ

# Building an Executable Yourself

- This project uses the `pyinstaller` to create binary executables.

    - Make sure to install it by running: `pip install -r optional_requirements.txt`

- So, there are really 3 important files when it comes to building a binary using *pyinstaller*:

    - `file_version_info.txt`, `mascot.ai.spec` and `build.py`.

    - The `file_version_info.txt` file is "Version resource file" and is responsible to add/show information when you right click > go to properties tab of the application.

    - The `mascot.ai.spec`, I have no idea.

    - The `build.py`, as you can see, is calling `pyinstaller` command from within a python file. It's equivalent to running `pyinstaller main.py...` in a terminal or command prompt.

- Make sure to change `file_version_info.txt` accordingly. Feel free to update or remove any additional options in `build.py`.

    - And then simply run `python build.py`.

- Please refer to [Pyinstaller Docs](https://pyinstaller.org/en/stable/index.html) for more information.
