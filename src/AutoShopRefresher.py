"""
Created on 11-26-2023

@author: Wundrfull
Code is a modified version of Zalkyrie's Refresher
"""
import pyautogui
import datetime
import keyboard

import time
import random
import win32api
import win32con
import sys

from DrawDebugger import locate_image_and_draw_box
from enum import Enum

# -------------------------
# HELPER CLASSES 
# -------------------------
class StandardResolution(Enum):
    HD = (1280, 720)
    FHD = (1920, 1080)
    QHD = (2560, 1440)
    UHD_4K = (3840, 2160)

current_resolution = StandardResolution.QHD.value
reso_acronym = "QHD"

class BookmarkType(Enum):
    MYSTIC = 1
    COVENANT = 2

# -------------------------
# HELPER FUNCTIONS 
# -------------------------
def convert_coordinates(x, y, target_res_enum):
    target_res = target_res_enum.value
    
    scale_x = target_res[0] / current_resolution[0]
    scale_y = target_res[1] / current_resolution[1]

    new_x = x * scale_x
    new_y = y * scale_y

    return int(new_x), int(new_y)

def click(x, y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    sleep_short()
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    
def get_random_point_within_box(box, margin = 3):
    left, top, width, height = box
    right = left + width
    bottom = top + height
    
    # Adjust the box coordinates by the margin
    adjusted_left = left + margin
    adjusted_top = top + margin
    adjusted_right = right - margin
    adjusted_bottom = bottom - margin

    # Ensure the box dimensions are valid after adjusting with the margin
    if adjusted_right <= adjusted_left or adjusted_bottom <= adjusted_top:
        raise ValueError("Box is too small for the given margin.")

    # Generate random coordinates within the adjusted box
    x = random.randint(adjusted_left, adjusted_right)
    y = random.randint(adjusted_top, adjusted_bottom)

    return x, y

def random_click_within_box(box, margin = 3):
    x, y = get_random_point_within_box(box, margin)
    
    click(x, y)
    sleep_medium()
    
def set_resolution():
    global reso_acronym
    global current_resolution
    
    resolution = pyautogui.size()
    
    if (isinstance(resolution, StandardResolution.HD.value)):
        print('\nHD Resolution Detected\n')
        reso_acronym = "HD"
        current_resolution = StandardResolution.HD
    elif (isinstance(resolution, StandardResolution.FHD.value)):
        print('\nFHD Resolution Detected\n')
        reso_acronym = "FHD"
        current_resolution = StandardResolution.FHD
    elif (isinstance(resolution, StandardResolution.QHD.value)):
        print('\nQHD Resolution Detected\n')
        reso_acronym = "QHD"
        current_resolution = StandardResolution.QHD
    elif (isinstance(resolution, StandardResolution.UHD_4K.value)):
        print("\n4K Resolution Detected\n")
        reso_acronym = "UHD_4K"
        current_resolution = StandardResolution.UHD_4K
    else:
        # You have some whack resolution widescreeners
        print("Whack-ass resolution detected. Get some help.\n\n")
        sys.exit()
        
def buy_bookmark(bookmark_type: BookmarkType):
    buy_time = time.time()
    bookmark_position = None
    buy_button_position = None
    bought = False
    
    # Locate the bookmark & Start Buy Process with 1/1 Buy Button
    while((bookmark_position is None) and (time.time() < (buy_time + timeout_duration))):
        if (bookmark_type == BookmarkType.COVENANT):
            bookmark_position = locate_covenant_buy_button()
            buy_button_position = locate_generic_buy_button(bookmark_position)
            random_click_within_box(buy_button_position)
            random_click_within_box(buy_button_position)
            
        else:
            bookmark_position = locate_mystic_bookmark()
            buy_button_position = locate_generic_buy_button(bookmark_position)
            random_click_within_box(buy_button_position)
            random_click_within_box(buy_button_position)
            
    # Confirm purchase the bookmark
    timeout_start = time.time()
    buy_button_position = None
    while(time.time() < (timeout_start + timeout_duration)):
        buy_button_position = locate_buy_button(bookmark_type)
        
        if (buy_button_position is not None):
            random_click_within_box(buy_button_position)
            random_click_within_box(buy_button_position)
            
            bought = True
            break
    
    if (bought is False):
        global exit_flag
        exit_flag = 1
        
def locate_generic_buy_button(box):
    global reso_acronym
    return pyautogui.locateOnScreen(f'./imgs/{reso_acronym}/generic_buy_button.png', confidence=0.8, region=box)

def locate_covenant_buy_button():
    global reso_acronym
    return pyautogui.locateOnScreen(f'./imgs/${reso_acronym}/covenant_buy_button.png', confidence=0.95)

def locate_refresh_button():
    global reso_acronym
    refresh_button = pyautogui.locateOnScreen(f'./imgs/{reso_acronym}/refresh_button.png',confidence=0.8)
    if (refresh_button is None):
        print("Refresh Button Not Found. Closing Script.")
        sys.exit()
    return refresh_button
        
def locate_convenant_bookmark():
    global reso_acronym
    return pyautogui.locateOnScreen(f'./imgs/{reso_acronym}/covenant_icon.png', confidence=0.8) 

def locate_buy_button(bookmark_type: BookmarkType):
    global reso_acronym
    if (bookmark_type == BookmarkType.COVENANT):
        return pyautogui.locateOnScreen(f'./imgs/{reso_acronym}/covenant_184_buy_button.png', confidence=0.8)
    else:
        return pyautogui.locateOnScreen(f'./imgs/{reso_acronym}/mystic_280_buy_button.png', confidence=0.8)
        
def locate_mystic_bookmark():
    global reso_acronym
    return pyautogui.locateOnScreen(f'./imgs/{reso_acronym}/mystic_icon.png', confidence=0.8)

def locate_confirm_button():
    global reso_acronym
    return pyautogui.locateOnScreen(f'./imgs/{reso_acronym}/confirm_button.png', confidence=0.8)

def sleep_short():
    time.sleep(random.uniform(0.1, 0.25))    
    
def sleep_medium():
    time.sleep(random.uniform(0.25, 0.75))

def sleep_long():
    time.sleep(random.uniform(1.0, 1.5))
    
def scroll():
    global current_resolution
    
    scroll_start_x = random.randint(convert_coordinates(1325, 0, current_resolution)[0], convert_coordinates(2036, 0, current_resolution)[0])
    scroll_end_x = random.randint(convert_coordinates(1325, 0, current_resolution)[0], convert_coordinates(2036, 0, current_resolution)[0])
    scroll_start_y = random.randint(convert_coordinates(0, 800, current_resolution)[1], convert_coordinates(0,1000, current_resolution)[1])
    scroll_end_y = random.randint(convert_coordinates(0, 333, current_resolution)[1], convert_coordinates(0,542, current_resolution)[1])
    scroll_time = random.uniform(.11, .136)
    
    win32api.SetCursorPos((scroll_start_x, scroll_start_y))
    pyautogui.dragTo(scroll_end_x, scroll_end_y, scroll_time, button='left')
    time.sleep(random.uniform(0.15, 0.25))
    
        
# -------------------------
# Initialization Section
# -------------------------

# Script Section
debug_timer = 0.5
exit_flag = 0
start_datetime = datetime.datetime.now()
set_resolution()
timeout_duration = 5 #debug timeout
refresh_button_position = locate_refresh_button()


# E7 Section
mystic_count = 0
covenant_count = 0
refresh_count = 0

# -------------------------
# Run Section
# -------------------------

while (exit_flag == 0):
    sleep_short() 
    refresh_button_position = locate_refresh_button()
    
    # Check for mystic bookmarks
    if (locate_mystic_bookmark() is not None):
        sleep_short()
        buy_bookmark(BookmarkType.MYSTIC)
        mystic_count += 1
        
    # check for covenant bookmarks
    if (locate_convenant_bookmark() is not None):
        sleep_short()
        buy_bookmark(BookmarkType.COVENANT)
        covenant_count += 1
    
    #########################################
    sleep_short()
    
    # Scroll twice to ensure the next bookmark is visible
    scroll()
    scroll()
    
    sleep_short()
    
     # Check for mystic bookmarks
    if (locate_mystic_bookmark() is not None):
        sleep_short()
        buy_bookmark(BookmarkType.MYSTIC)
        mystic_count += 1
        
    # check for covenant bookmarks
    if (locate_convenant_bookmark() is not None):
        sleep_short()
        buy_bookmark(BookmarkType.COVENANT)
        covenant_count += 1
        
        # Allow user to exit (debug)
    debug_time_start = time.time()
    while (time.time() < debug_time_start + debug_timer):
        if (keyboard.is_pressed('q') is True):
            exit_flag = 1
            break
        
    if exit_flag == 1:
        break
    
    refresh_button_position = locate_refresh_button()
    random_click_within_box(refresh_button_position)
    random_click_within_box(refresh_button_position)
    
    timeout_start = time.time()
    while(time.time() < (timeout_start + timeout_duration)):
        confirm_button_position = locate_confirm_button()
        if (keyboard.is_pressed('q') is True):
            exit_flag = 1
            break
        if (confirm_button_position is not None):
            #Confirm refresh
            sleep_medium()
            random_click_within_box(confirm_button_position)
            random_click_within_box(confirm_button_position)
            refresh_count = refresh_count + 1
            print("Refreshed: ", refresh_count)
            break
    
    if exit_flag == 1:
        break
    
    sleep_long()


# -------------------------
# Exit Section
# -------------------------
if (exit_flag == 1):
    print("Macro has forcefull exited.\n\n")
else:
    print("Macro has finished running.\n\n")
    
time_ran = datetime.datetime.now() - start_datetime
time_ran_mins = round(time_ran.total_seconds()/60)

# Print out stats of session
print(f'Total time ran: {time_ran_mins} minutes and {time_ran.seconds % 60} seconds')
print(f'Total times refreshed: {refresh_count} \nSkystones used: {refresh_count * 3}')
print(f'Covenant medals bought: {covenant_count * 5} \nMystic medals bought: {mystic_count * 50}')
print(f'Total gold used: {covenant_count * 184000 + mystic_count * 280000}\n')