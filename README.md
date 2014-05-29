# Itunes Playlist to Dir

This is as simple python script to organize mp3 files from itunes on a folder. I use this to create CDs/pendrives of MP3 to be used on my car...

Its simple, quickly writed and the code is a good piace of junk...

## What it do?

* copy files described on playlist from itunes to a dir
* default configuration of itunes is <artist>/<album>/<music>
* the default copyToFormat value is <artist>/<album>/<track_number> - <name>
* and the order that items will be copied will be the natural order (alphabetical) of the folders because the order used on some MP3 players is by modified date




## How to use?

This is a command line tool tested on MacOS X...

You will need to:

* Export your favorite playslist from Itunes on xml format. Save on your home directory, eg: ~/playlist.xml
* Clone this project to your machine:

```
   git clone https://github.com/josecoelho/itunes_playlist_to_dir.git
   cd itunes_playlist_to_dir
```

* Execute the command on the root folder of project

```
  python <fullpath_to>/itunes_playlist_to_dir.py /home/<user>/playlist.xml <target_folder> "<optional: cotyToFormat>"
```

E.G.:
```
 python /Users/josecoelho/itunes_playlist_to_dir/itunes_playlist_to_dir.py Tarantino.xml ./ "<album>/<track_number> - <name>"
```