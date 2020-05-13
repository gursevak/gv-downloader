import os.path
from tqdm import tqdm
import urllib.request
from urllib.request import urlopen
import requests


print ("Vaheguru Jee Kaa Khalsa Vaheguru Jee Kee Fateh")
print ("gw-downloader")

#To make sure that the file is in the same folder so that the script can read it
yes_list = ["Y", "y", "yes", "Yes", "YES"]
input1 = input ("Is the playlist file in the same folder as this script? Y/N   ")
if input1 == "N":
    print ("Please save the playlist.m3u file in the same folder and come back")

no_list = ["N", "n", "no", "No", "NO"]
if input1 in no_list:
    print ("Please save the playlist.m3u file in the same folder and come back")    
    
elif input1 in yes_list:
    print ("Reading File")
    #Open the folder
    file = open ("playlist.m3u", "r")
    contents = file.read()
    
    split_lines = contents.split()
  
    subfolder_name = input ("What would you like to name the subfolder into which the files will be saved into? ")
    
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

        urllib.request.urlretrieve(url, name)      
    
        print ("File downloaded - " + (name))
    
else:
    print ("Invalid Entry")

input("Press enter to exit ")
