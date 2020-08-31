"Vaheguru Jee Kaa Khalsa Vaheguru Jee Kee Fateh!"
"This is now downloading all files in the playlist.m3u file in the same directory."

Get-Content playlist.m3u | ForEach-Object {Invoke-WebRequest $_ -OutFile $(Split-Path $_ -Leaf)}