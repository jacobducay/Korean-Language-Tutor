import subprocess
import pyautogui
import time

# Adjust the command based on your OS and Anki installation path
subprocess.Popen(["F:/Program Files/Anki/anki.exe"])

# Ensure Anki has time to open
time.sleep(10)  # Wait for Anki to load, adjust timing as necessary (increase time in case of syncing)

# Navigate the menu to export a deck
pyautogui.hotkey('alt', 'f')  # Open the File menu
time.sleep(1)
pyautogui.press('down', presses=2)  # Navigate to Export option
pyautogui.press('enter')  # Open Export dialog

#Exclude media
pyautogui.press('tab') # Navigate to 'Include media'
pyautogui.press('space') # Toggle checkbox
pyautogui.press('tab') #navigate to export button
pyautogui.press('enter') # Open Export dialog

# Save the file
time.sleep(1)
pyautogui.write('P:\Program Files\Python_programs\Study App\Anki Exports\export.colpkg')  # Enter path and file name
pyautogui.press('enter')  # Confirm save
time.sleep(1)
pyautogui.press('enter') # Confirm overwrite
time.sleep(4)
pyautogui.hotkey('alt', 'f4')

