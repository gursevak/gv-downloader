import os.path
from tqdm import tqdm
import urllib.request
from urllib.request import urlopen
import requests
import easygui



print ("Vaheguru Jee Kaa Khalsa Vaheguru Jee Kee Fateh")
print ("gv-downloader")

input("The downloader will now ask you to select the playlist.m3u file you have downloaded for which tracks you would like to download. Please press enter to continue...")

path = easygui.fileopenbox()
      
    
print ("Reading File")
file = open (path, "r")
contents = file.read()

    
split_lines = contents.split()

playlist_length = (len(split_lines))
if playlist_length > 1:
    file_plur = "files"
if playlist_length == 1:
    file_plur = "file" 
    
print("This playlist has " , playlist_length ,  file_plur)

subfolder_name = input ("What would you like to name the subfolder into which the " + (file_plur) + " will be saved into? ")
    
try:
    # Create target folder
    os.mkdir(subfolder_name)
    print("Directory " , subfolder_name ,  " Created ") 
except FileExistsError:
    print("Directory " , subfolder_name ,  " already exists")

    
for url in split_lines:
    site = urlopen(url)
    meta = site.info()
        
    file_size = int(site.getheader('Content-Length'))
    total_size = file_size
    block_size = 1024
    chunk_size = block_size
        
    file_name = url.split('/')[-1]
    name =  subfolder_name + "/" + file_name

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
    if total_size != 0 and t.n != total_size:
        print("ERROR, something went wrong")
            
            
        


    
    print ("File downloaded")
    

input("Press enter to exit ")

