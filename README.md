# GV Downloader

This is a really simple shell script that I wrote to quickly download large amounts of katha and keertan from [gurmatveechar.com](https://www.gurmatveechar.com) and other websites.

***You don't need to know anything about programming in order to use this script.

It works with any m3u playlist file and allows batch downloading of all the files in the playlist, as well as pausing and resuming.

The provided sample `playlist.m3u` file contains the complete [Larivaar Siri Guru Granth Sahib Ji Katha by Sant Giani Gurbachan Singh Ji Bhindranwale](http://www.gurmatveechar.com/audio.php?q=f&f=%2FKatha%2F01_Puratan_Katha%2FSant_Gurbachan_Singh_%28Bhindran_wale%29%2FGuru_Granth_Sahib_Larivaar_Katha)

# Usage

**Instructions are for MacOS

1. Download the `playlist.m3u` file for the playlist or folder that you want to download. Playlist files can usually be found on most katha/keertan websites: go to the folder or playlist that you want to download and look for a green 'play button' icon near the top of the folder.

2. Download the script using the link above (Download ZIP), unzip the folder and replace the provided `playlist.m3u` file with the file that you just downloaded.

2. Open `Terminal.app` (from the /Applications/Utilities folder or search for it using Spotlight) and drag-and-drop the `download.sh` file into the Terminal window to open it.

3. Follow the on-screen instructions and begin downloading. You can quit the program at any time by pressing `CTR+C` (`^+C`) on your keyboard. 

When you restart, the program will automatically begin with the file that you left off at (and remove the already downloaded files from `playlist.m3u`).

Enjoy!


**You *may* need to change the file's permissions to run the script. To do this, copy/paste the following line into Terminal 
`cd "$(dirname "$0")" chmod a+x download.sh` and press enter.
