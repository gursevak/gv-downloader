import os.path
from tqdm import tqdm
import urllib.request
from urllib.request import urlopen
import requests
import easygui as g

yes_list = ["Y", "y", "yes", "Yes", "YES", "True"]
no_list = ["N", "n", "no", "No", "NO", "False"]

print ("Please follow the on screen prompts.")

g.msgbox ("Vaheguru Jee Kaa Khalsa Vaheguru Jee Kee Fateh \n"
          "Please make sure that you have already downloaded a playlist.m3u file for which tracks you would like to download. You will be prompted to select the file.", "GV Downloader")

path = g.fileopenbox()
      
file = open (path, "r")
contents = file.read()
print(" ")
print (("Reading file ") + (os.path.basename(file.name)))


if (os.path.basename(file.name)) != "playlist.m3u":
    oui_2 = g.ynbox(("You selected the file ")+ (os.path.basename(file.name)) + ("\n") +
    ("Are you sure this is the file you meant to select? If yes, the downloader will continue. If no, you will be prompted to select a file again."), "GV Downloader")
    
    if oui_2 == ("True"):
            pass
    elif oui_2 == ("False"):
            path = easygui.fileopenbox()

    file = open (path, "r")
    contents = file.read()

  
split_lines = contents.split()

playlist_length = (len(split_lines))
if playlist_length > 1:
    file_plur = "files"
if playlist_length == 1:
    file_plur = "file" 
    
print("This playlist has " , playlist_length ,  file_plur)

g.msgbox ("Please select the folder into which you would like the " + (file_plur) + " to be saved to.", "GV Downloader")

chosen_dir = g.diropenbox()
subfolder_name = chosen_dir

list_to_choose = []

for each in split_lines:
    list_to_choose.append(each)    
    
chooser_msg = "Please choose the tracks that you would like to download. Click on individual tracks to select/deselect."
chooser_title = "Kirtan Downloader"
chooser_choices = list_to_choose
chooser_chosen = g.multchoicebox(chooser_msg, chooser_title, chooser_choices)

playlist_length = (len(chooser_chosen))

if playlist_length > 1:
    file_plur = "files"
if playlist_length == 1:
    file_plur = "file" 

print(" ")    
print("Now downloading " , playlist_length ,  file_plur)    
print(" ")
    
for url in chooser_chosen:
    try:
        site = urlopen(url)
    except:
        if "https" in url:
            print("welp")
        else:
            url = url.replace("http://","https://")
    site = urlopen(url)
    meta = site.info()

    print(" ")
        
    file_size = int(site.getheader('Content-Length'))
    total_size = file_size
    block_size = 1024
    chunk_size = block_size
        
    file_name = url.split('/')[-1]
    name =  subfolder_name + "/" + file_name
    
    if (os.path.isfile(name)):
        already_size = os.path.getsize(name)

        if already_size == total_size:
            print("The file " + file_name + " already exists. Continuing with next file...")
            continue
        
        elif already_size != total_size:
            print("Wrong fize size detected for " + file_name + ". This is possibly from a previous download attempt and could be a corrupted file. Redownloading...")
            # Streaming, so we can iterate over the response.
            r = requests.get(url, stream=True)
            # Total size in bytes.
            total_size = int(r.headers.get('content-length', 0))
            block_size = 1024 #1 Kibibyte
            t=tqdm(total=total_size, unit='iB', unit_scale=True)
            with open (name, mode = 'wb') as f:
                for data in r.iter_content(block_size):
                    t.update(len(data))
                    f.write(data)
            t.close()
            print ("File downloaded: " + file_name)
        
        if total_size != 0 and t.n != total_size:
            print("ERROR, something went wrong")

    elif not (os.path.exists(name)):
        print("Downloading " + file_name)
        # Streaming, so we can iterate over the response.
        r = requests.get(url, stream=True)
        # Total size in bytes.
        total_size = int(r.headers.get('content-length', 0))
        block_size = 1024 #1 Kibibyte
        t=tqdm(total=total_size, unit='iB', unit_scale=True)
        with open (name, mode = 'wb') as f:
            for data in r.iter_content(block_size):
                t.update(len(data))
                f.write(data)
        t.close()

        print ("File downloaded: " + file_name)
        
        if total_size != 0 and t.n != total_size:
            print("ERROR, something went wrong")
            
print(" ")
print("Downloading finished.")
    
g.msgbox (("Downloads complete. Downloader will now close.") , "GV Downloader")

exit()