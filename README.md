# Python Auto-Update Bot 🤖


## What the project does

This repository contains the code of a Basic Cross-platform Utility Bot which automatically checks for Python version update every time the computer boots, and downloads if available. 
Sounds cool, right? 😎 Follow up the simple setup process to benefit this automation!


## Why the project is useful

Gets you rid of:
- Using the old Python interpreter even if the new version is out. ✅
- Or wasting time in checking if the update is available or not again and again from [python.org/downloads](https://www.python.org/downloads). ✅


## Sample Screenshots

1) On computer start, bot automatically checks for update, and if available, prompts the user for permission to download.
<img src="Sample%20Screenshots/1)%20Update%20Auto-Found.png">

2) Downloads the update.
<img src="Sample%20Screenshots/2)%20Downloading.png">


## How users can get started with the project

### Install the Dependencies (Python Packages 🐍)

After downloading this project to your PC, open the project folder, there, open your [command-line interpreter](https://en.wikipedia.org/wiki/List_of_command-line_interpreters#:~:text=In%20computing%2C%20a%20command-line%20interpreter%2C%20or%20command%20language%20interpreter%2C%20is%20a%20blanket%20term%20for%20a%20certain%20class%20of%20programs%20designed%20to%20read%20lines%20of%20text%20entered%20by%20a%20user%2C%20thus%20implementing%20a%20command-line%20interface.) (e.g. Command Prompt for Windows), and run the following:
```bash
pip install -r requirements.txt
```

### Steps to Set up Script Auto-Start

This is the most important part of the Bot Setup, once done, you'll be just ready to go! 👌

#### For Windows 🪟
1) If Python scripts on your system are NOT set to always open with your Python interpreter (`python.exe`), set by following the steps:
    1) Right-click on the downloaded `PyUpdateBot.py`, click `Open with` > `Choose another app`
    2) Tick `Always use this app to open .py files`
    3) Under `Other options`, scroll down and click `More apps ↓`, again scroll down and click `Look for another app for this PC`
    4) An `Open with...` file dialog will open up, there, navigate to your `python.exe` (e.g. `C:\Users\Samyak\AppData\Local\Programs\Python\Python310`)
    5) Click `python.exe` > `Open`
    6) Done! 👍
2) Copy `PyUpdateBot.py` to the Startup folder (`C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup`).
   [[Source: Stack Overflow]](https://stackoverflow.com/a/59113610)
3) That's it! 🥳 Now, every time you'll start your PC, this bot will check for Python update and notify you if available!

**NOTE: I have a Windows laptop only, if anyone has Linux or macOS, please confirm the following, write the steps and make a PR. Thank you in advance! ❤️**

#### For Linux 🐧
[Run Python script at startup in Ubuntu](https://stackoverflow.com/questions/24518522/run-python-script-at-startup-in-ubuntu)

#### For macOS 🍎
[Run Python Script at OS X Startup](https://stackoverflow.com/questions/29338066/run-python-script-at-os-x-startup)


## Contact

[📧](mailto:samyak65400@gmail.com?subject=Regarding%20py-update-bot)


## Ciao! 🙋
