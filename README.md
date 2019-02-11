# GV Downloader

This is a really simple bash shell script to quickly download large amounts of katha from [gurmatveechar.com](https://www.gurmatveechar.com) and keertan from various websites that support playlist files.

***You don't need to know anything about programming in order to use this script.

It works with any m3u playlist file and allows batch downloading of all the files in the playlist, as well as pausing and resuming.

The provided sample `playlist.m3u` file contains the complete [Larivaar Siri Guru Granth Sahib Ji Katha by Sant Giani Gurbachan Singh Ji Bhindranwale](http://www.gurmatveechar.com/audio.php?q=f&f=%2FKatha%2F01_Puratan_Katha%2FSant_Gurbachan_Singh_%28Bhindran_wale%29%2FGuru_Granth_Sahib_Larivaar_Katha)

# Usage

**Instructions are for MacOS

1. Download or clone the repository and replace the provided `.m3u` file with the `playlist.m3u` file that has the tracks you want to download. Playlist files can usually be downloaded from katha/keertan websites: go to the folder or playlist that you want to download and look for the green 'play button' icon at the top of the folder.

2. Open the `download.sh` file using `Terminal.app` or your bash terminal of choice (right-click file > Open With; the Terminal app is hidden away in the Utilities folder, /Applications/Utilities).

Alternatively (or if the above method isn't working), open `Terminal.app` and navigate to the downloaded directory by typing
`cd ~/Downloads/gv-downloader`
(or wherever you saved the script to).

You may need to change the file's permissions to run the script. To do this, type 
`chmod a+x download.sh`

then run the script by typing 
`./download.sh`

3. Follow the on-screen prompts and begin downloading. You can quit the program at any time by pressing `CTR+C` (`^+C`) on your keyboard. 

When you restart, the program will automatically begin with the file that you left off at (and remove downloaded files from `playlist.m3u`).

Enjoy!
