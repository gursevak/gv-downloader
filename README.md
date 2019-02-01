# GV Downloader

This is a really simple bash shell script that I made to quickly download large amounts katha from [gurmatveechar.com](https://www.gurmatveechar.com) and keertan from various websites that support playlists.

It can be used to download the contents of any m3u playlist file, and keeps track of the files that have completed in the playlist, allowing you to pause and continue your batch download as you wish.

The provided sample `playlist.m3u` file contains the complete [Larivaar Siri Guru Granth Sahib Ji Katha by Sant Gurbachan Singh Ji Bhindranwale](http://www.gurmatveechar.com/audio.php?q=f&f=%2FKatha%2F01_Puratan_Katha%2FSant_Gurbachan_Singh_%28Bhindran_wale%29%2FGuru_Granth_Sahib_Larivaar_Katha)

# Usage

1. Download or clone the repository and replace the provided `.m3u` file with the `playlist.m3u` file that has the tracks you want to download. Playlist files can usually be downloaded from katha/keertan websites: navigate to the folder or playlist that you want to download and look for the green 'play button' icon at the top of the folder.

2. Open the `download.sh` file using `Terminal.app` or your bash terminal of choice (right-click > Open As).

Alternatively (or if the above method isn't working), open `Terminal.app` and navigate to the downloaded directory:
`cd ~/Downloads/gv-downloader` (or wherever other location you cloned/downloaded the script to).

You may need to change the file's permissions to run the script:
`chmod a+x download.sh`

then run it using 
`./download.sh`

3. Follow the on-screen prompts and begin downloading. You can quit the program at any time by pressing `CTR+C` (^+C) on your keyboard. 

When you restart, the program will automatically begin with the file that you left off at (and remove downloaded files from `playlist.m3u`).

Enjoy!
