# Itunes Playlist to Dir


## What it do?

* copy files described on playlist from itunes to a dir
* default configuration of itunes is <artist>/<album>/<music>
* the target will receive <artist>-<album>/<music>,
* and the order that items will be copied will be the natural order (alphabetical) of the folders because the order used on some MP3 players is by modified date


## How to use?

This is a command line tool...

You will need to:

* Export your favorite playslist from Itunes on xml format. Save on your home directory, eg: ~/playlist.xml
* Clone this project to your machine:

```
   git clone https://github.com/josecoelho/itunes_playlist_to_dir.git
   cd itunes_playlist_to_dir
```

* Execute the command on the root folder of project

```
  python ./itunes_playlist_to_dir.py ~/playlist.xml <target_folder>
```