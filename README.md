# GV Downloader

Quickly download large amounts of katha and keertan from GurmatVeechaar.com and other websites with one click

## Supported Websites

- [gurmatveechar.com](http://www.gurmatveechar.com/)
- [sgpc.net](http://sgpc.net/)
- [sikhvibes.com](http://www.sikhvibes.com/)
- [gurbaniupdesh.org](http://www.gurbaniupdesh.org/)
- [sikhsoul.com](http://sikhsoul.com/)
- [japtapsamagams.com](https://www.japtapsamagams.com/)
- [gurunanakacademy.com](http://gurunanakacademy.com)
- [rajkaregakhalsa.net](https://www.rajkaregakhalsa.net/)

Support for websites that use direct download links will be added in the future

## About

The script works with any m3u playlist file and allows batch downloading of all the files in the playlist, as well as pausing and resuming. No programming knowledge is necessary to use the script.

The provided sample `playlist.m3u` file contains the complete [Larivaar Siri Guru Granth Sahib Ji Katha by Sant Giani Gurbachan Singh Ji Bhindranwale](http://www.gurmatveechar.com/audio.php?q=f&f=%2FKatha%2F01_Puratan_Katha%2FSant_Gurbachan_Singh_%28Bhindran_wale%29%2FGuru_Granth_Sahib_Larivaar_Katha)

# How To Use

## Setup

### Mac

No setup required. Skip to *Using the Script* instructions below

### Windows 10

1. Install WSL or Windows Subsystem for Linux:

Go to Settings > Update & Security > For Developers. Check the Developer Mode radio button. And search for “Windows Features”, choose “Turn Windows features on or off”.

2. Scroll to find WSL, check the box, and then install it. Once done, one has to reboot to finish installing the requested changes. Press Restart now.  BASH will be available in the Command Prompt and PowerShell.

### Windows 8 and older

1. Download and install [Cygwin](https://www.cygwin.com/)

## Using the Script

1. Download the `playlist.m3u` file for the playlist or folder that you want to download. Playlist files can usually be found on most katha/keertan websites: go to the folder or playlist that you want to download and look for a green 'play button' icon near the top of the folder.

2. Download the script using the link above (Download ZIP), unzip the folder and replace the provided `playlist.m3u` file with the file that you just downloaded.

3. Open `Terminal.app` (from the /Applications/Utilities folder or search for it using Spotlight) and drag-and-drop the `download.sh` file into the Terminal window to open it. 

**WINDOWS 10 USERS: Use Command Prompt instead of Terminal**

**OTHER WINDOWS USERS: Use Cygwin instead of Terminal**

4. Press the `Enter` key once. Then follow the on-screen instructions and begin downloading. You can quit the program at any time by pressing `CTR+C` (`^+C`) on your keyboard (on Windows, just close the Cygwin window).

When you restart, the program will automatically begin with the file that you left off at (and remove the already downloaded files from `playlist.m3u`) (Mac and Windows 10 users only)

Enjoy!


**If the script isn't running, you *may* need to change the file's permissions to run the script. To do this, copy/paste the following line into Terminal 
`cd "$(dirname "$0")" chmod a+x download.sh` and press enter.
