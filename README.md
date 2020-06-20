# Gurmat Veechar Downloader

Quickly download large amounts of katha and keertan from GurmatVeechar.com and other websites with one click

[Original Project by Irvanjit Singh](https://github.com/irvanjitsingh/gv-downloader)

## Supported Websites

- [gurmatveechar.com](http://www.gurmatveechar.com/)
- [sgpc.net](http://sgpc.net/)
- [sikhvibes.com](http://www.sikhvibes.com/)
- [gurbaniupdesh.org](http://www.gurbaniupdesh.org/)
- [sikhsoul.com](http://sikhsoul.com/)
- [japtapsamagams.com](https://www.japtapsamagams.com/)
- [gurunanakacademy.com](http://gurunanakacademy.com)
- [rajkaregakhalsa.net](https://www.rajkaregakhalsa.net/)



## About

The script works with any m3u playlist file and allows batch downloading of all the files in the playlist.

The provided sample `playlist.m3u` file contains the complete [Larivaar Siri Guru Granth Sahib Ji Katha by Sant Giani Gurbachan Singh Ji Bhindranwale](http://www.gurmatveechar.com/audio.php?q=f&f=%2FKatha%2F01_Puratan_Katha%2FSant_Gurbachan_Singh_%28Bhindran_wale%29%2FGuru_Granth_Sahib_Larivaar_Katha)


## Windows Instructions

1. Download the `playlist.m3u` file for the playlist or folder that you want to download. Playlist files can usually be found on most katha/keertan websites: go to the folder or playlist that you want to download and look for a green 'play button' icon near the top of the folder.

2. Download the `GVDOWNLOADER1.2.1` release [click here](https://github.com/themanjotsingh/gv-downloader/releases/tag/1.2.1). Ignore warnings from your web browser or Windows Defender. It shows this because of the exe not being signed as well as not being a commonly downloaded file (generally speaking).

3. Run `GVDOWNLOADER1.2.1.exe`. Follow the on screen prompts.

4. When asked, locate the playlist.m3u file you downloaded earlier.

4. When asked, enter a name for the sub-directory that you would like to create to put this playlist's files in.

5. The downloader will begin downloading files into the directory you chose. It will also check if that file already exists before downloading again in case you need to stop downloading for whatever reason and need to resume later on therefore having to not redownload already downloaded files.


## Mac Instructions [Project by Irvanjit Singh](https://github.com/irvanjitsingh/gv-downloader)

***This program is easy to use. No coding knowledge necessary!

******These instructions are tested on Mac only. WINDOWS USERS: to use this version, download and install [Cygwin](https://www.cygwin.com/) first. Then, in Step 3, use Cygwin instead of 'Terminal.app'. Pause and resume won't work so make sure you give enough time for your download to finish.

1. Download the `playlist.m3u` file for the playlist or folder that you want to download. Playlist files can usually be found on most katha/keertan websites: go to the folder or playlist that you want to download and look for a green 'play button' icon near the top of the folder.

2. Download the script using the link above (Download ZIP), unzip the folder and replace the provided `playlist.m3u` file with the file that you just downloaded in the `Terminal` Folder.

3. Open `Terminal.app` (from the /Applications/Utilities folder or search for it using Spotlight) and drag-and-drop the `download.sh` file into the Terminal window to open it.

4. Press the `Enter` key once. Then follow the on-screen instructions and begin downloading. You can quit the program at any time by pressing `CTR+C` (`^+C`) on your keyboard (on Windows, just close the Cygwin window).

When you restart, the program will automatically begin with the file that you left off at (and remove the already downloaded files from `playlist.m3u`).

Enjoy!


## Python Version Instructions

Prerequisites
Python 3.5 or later

1. Download the `playlist.m3u` file for the playlist or folder that you want to download. Playlist files can usually be found on most katha/keertan websites: go to the folder or playlist that you want to download and look for a green 'play button' icon near the top of the folder.

2. Download the script using the link above (Download ZIP), unzip the folder and replace the provided `playlist.m3u` file with the file that you just downloaded in the `Python` Folder.

3. Run the `GV Downloader.py` file. Follow the on screen prompts. 

4. When asked, locate the playlist.m3u file you downloaded earlier.

5. When asked, select the folder that you would like to create to put this playlist's files in.

5. The downloader will begin downloading files into the directory you chose. It will also check if that file already exists before downloading again in case you need to stop downloading for whatever reason and need to resume later on therefore having to not redownload already downloaded files.


Enjoy

**If the script isn't running, you *may* need to change the file's permissions to run the script. Please also confirm that your playlist file is named exactly as `playlist.m3u`.



**If the script isn't running, you *may* need to change the file's permissions to run the script. To do this, copy/paste the following line into Terminal 
`cd "$(dirname "$0")" chmod a+x download.sh` and press enter.

## Windows Powershell Intructions

1. Download the `playlist.m3u` file for the playlist or folder that you want to download. Playlist files can usually be found on most katha/keertan websites: go to the folder or playlist that you want to download and look for a green 'play button' icon near the top of the folder.

2. Download the script using the link above (Download ZIP), unzip the folder and replace the provided `playlist.m3u` file with the file that you just downloaded in the `Powershell` Folder.

3. Right click on `Powershell.ps1` and then click on "Run with Powershell" in the Right Click Context Menu.

Enjoy


-----------------------
Windows executable made with [Auto PY to EXE](https://github.com/brentvollebregt/auto-py-to-exe)

Uses [tqdm](https://github.com/tqdm/tqdm) [easygui](https://easygui.readthedocs.io/en/master/) [requests](https://requests.readthedocs.io/en/master/)
