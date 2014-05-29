'''
Created on Aug 1, 2012

@author: josecoelho
'''
import sys
from xml.etree import ElementTree as ET
from shutil import copyfile
import urllib2
import os

def itunes_playlist_to_dir(playlist,toDir,copyToFormat):
    '''
        copy files described on playlist from itunes to a dir

        default configuration of itunes is <artist>/<album>/<music>
        the default copyToFormat value is <artist>/<album>/<track_number> - <name>

        and the order that items will be copied will be the natural order (alphabetical) of the folders
         because the order used on the MP3 player is by modified date

    '''
    toCopy = []
    xml = ET.parse(playlist)

    if(not copyToFormat):
        copyToFormat = "<artist>/<album>/<track_number> - <name>"

    nextIsLocation = False
    nextIsArtist = False
    nextIsAlbum = False
    nextIsTrackNumber = False
    nextIsName = False
    for item in xml.getroot().find('dict').find('dict').findall('dict'):
        #loading items on toCopy
        metadata = {}
        for i in item.getiterator():
            if(nextIsArtist):
                metadata['artist'] = i.text
            if(nextIsAlbum):
                metadata['album'] = i.text
            if(nextIsTrackNumber):
                metadata['track_number'] = i.text
            if(nextIsName):
                metadata['name'] = i.text.replace("/","-")
            if(nextIsLocation):
                print metadata

                # if artist not found set as undefined
                if not 'artist' in metadata.keys():
                    metadata['artist'] = 'undefined'
                # if album not found set as undefined
                if not 'album' in metadata.keys():
                    metadata['album'] = 'undefined'
                if not 'name' in metadata.keys():
                    metadata['name'] = 'undefined'
                # if track_number not defined, then set as 0
                if not 'track_number' in metadata.keys():
                    metadata['track_number'] = '0'

                nextIsLocation = False

                fromF= urllib2.unquote( i.text )
                fromF = fromF.replace("file://localhost", '')

                extension = os.path.splitext(fromF)[1]

                toF = toDir+copyToFormat

                toF = toF.replace('<artist>',metadata['artist'])
                toF = toF.replace('<album>',metadata['album'])
                toF = toF.replace('<track_number>',metadata['track_number'])
                toF = toF.replace('<name>',metadata['name'])

                toF = toF+extension

                #ignore, if that path already exists on toDir
                if os.path.exists(toF):
                    continue

                toCopy.append({'fromF':fromF,'toF':toF})

            nextIsArtist = i.text == 'Artist'
            nextIsAlbum = i.text == 'Album'
            nextIsTrackNumber = i.text == 'Track Number'
            nextIsName = i.text == 'Name'
            nextIsLocation = i.text == 'Location'

    #organize list
    toCopy.sort()



    #copy files
    for cp in toCopy:
        fromF = cp['fromF']
        toF = cp['toF']

        dir = os.path.dirname(toF)
        if not os.path.exists(dir): #create dir on toDir if that not exists
            os.makedirs(dir)

        print "Copy {0} to {1}".format(fromF,toF)
        copyfile(fromF,toF)


if __name__ == '__main__':
    playlist = sys.argv[1]
    toDir = sys.argv[2]
    copyToFormat = ''
    if(3 < len(sys.argv)):
      copyToFormat = sys.argv[3]

    itunes_playlist_to_dir(playlist,toDir,copyToFormat)





