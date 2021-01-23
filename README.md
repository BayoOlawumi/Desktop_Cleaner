## How to use this Script

1. Download the Scripts
2. Customize the default path your want to monitor to work with your PC
    ![!](/imgs/customize.PNG)
    1. Go to line 9 and adjust the dumping folder name to be whatsoever folder you have created on your desktop
    2. Go to line 10 in desktop_cleaner.py, Customize `folder_to_monitor = '/Users/BayoOlawumi/Desktop'`
    3. Go to line 13 in desktop_cleaner.py, Change the code location to where you saved your scripts

3. Adjust the content of file_organizer.bat to point to the desktop_cleaner.py, this depends on where you put your scripts
4. Also, adjust file_organizer.vbs to point to the location of file_organizer.bat

##  To automate the process to start when you switch on your PC (Windows Users only)

 > **Click the search button and search for register, open registry editor**
 >
    >> navigate to - ***Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run***
        - Right click, create new string value
        - After creating, righ click to modify
        - Fill in the filepath of you file_organizer.vbs, in my case
           - `C:\Users\BayoOlawumi\Desktop\Masters\CamSec\CamSec_Scripts\file_organizer.vbs`

> Restart your PC