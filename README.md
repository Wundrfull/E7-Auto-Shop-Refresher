# E7-Auto-Shop-Refresher

**Use at your own risk.**

This macro automates shop rerolling by automatically shop refreshing and buying all Covenant/Mystic bookmarks. RNG is added to avoid third-party software detection.

This code references dengpris's [E7-Secret-Shop-Auto-Refresher](https://github.com/dengpris/E7-Secret-Shop-Auto-Refresher). 

Updated to handle Google Play Emulator and different resolutions (with some picture setup).

![](https://media.giphy.com/media/NSAX9N2SyPUVrih2E0/giphy-downsized-large.gif)

## How to Run:
1. Make sure you have [Python](https://www.python.org/downloads/) and the correct dependencies installed (see below).
2. Open Epic 7 in google play emulator and maximize.
3. Default resolution settings set to work with 2560x1440. 
    > Any resolution outside of the default, requires a one time photo setup. There are folders for your resolution under /imgs/{your_resolution}. You need to replicate all photos in "QHD" folder, in your own resolution folder. Photo names must match exactly. If you don't see your resolution folder to add your pictures to, add one for your resolution.
    > If you had to add a custom folder, you need to add your new resolution under the  "Resolution Settings" in AutoShopRefresher.py. There are comments to guide you on where to add custom ones.
4. Enter Secret Shop
5. Run the Python script __Make sure that refresh button is visible__
6. To exit the script, hold 'q' until the macro stops working completely

## Dependencies to Install
Use the package manager [pip](https://pip.pypa.io/en/stable/installation/) to install the following dependencies:
```
pip install pyautogui
pip install datetime
pip install keyboard
pip install time
pip install random
pip install win32api
pip install win32con
pip install sys
pip install ImageDraw
```

## DEBUGGER
I've added a debugger tool to help you test image identification. Debugger tool will take an image_path for the image you're testing and draw a yellow box around the image it finds.
> DrawDebugger.py
