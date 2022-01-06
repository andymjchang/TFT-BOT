![main](https://i.imgur.com/roX0N3C.png)

## NOTES:
- To ensure best results, make sure you are running this on a computer that has decent specs.
- 1920x1080 fullscreen is required in League, game must also be on main monitor.
- Make sure you dont have any overlays on.
- If the program crashes, make sure you create an issue with the traceback.
- Feel free to create a PR for whatever you want, I used this project to learn python and much of the code can be improved.
- My initial goal with this project was to create a bot capable of hitting gold in TFT. Unfortunately I do not have anymore time to spend on this.

## INSTALLATION:
1. Install Python 3.9.6 from https://www.python.org/downloads/windows/
   - Note that Python 3.9.6 cannot be used on Windows 7 or earlier.
3. Run pip install -r requirements.txt in Command Prompt
4. Install tesseract using windows installer available at: https://github.com/UB-Mannheim/tesseract/wiki
   - Note the tesseract path from the installation.
   - Set the tesseract path in the ocr.py file (it may already be correct)
5. Run the main.py file

## FEATURES:
- Read the board state (Round / Level / Gold / Shop / Items)
- Keeps track of champions on the board and bench
- Pick a random item/champ from the carousel
- Pickup items from the board after PVE rounds
- Place items onto champions
- Plays the user defined team comp
- Auto queue using the LCU api

## TODO:
- Change the functions that take multiple screenshots and change it to one screenshot and crop that image. This should increase performance.
- Implement tome of traits logic
- Add more logic to the gold spending function
- Change all pyautogui screenshot functions to PIL ImageGrab
- Revamp auto queue so it can never fail
- Multiple defined team comps and pick the best one in game
- General code imrpovements and optimization
- [?] Intelligent carousel item/champion choice
