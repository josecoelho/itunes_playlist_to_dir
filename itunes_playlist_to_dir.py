'''
Created on Aug 1, 2012

@author: josecoelho
'''
import sys
from xml.etree import ElementTree as ET
from shutil import copyfile
import urllib2
import os

def itunes_playlist_to_dir(playlist,toDir):
    '''
        copy files described on playlist from itunes to a dir
        
        default configuration of itunes is <artist>/<album>/<music>
        the target will receive <artist>-<album>/<music>, 
        and the order that items will be copied will be the natural order (alphabetical) of the folders 
         because the order used on the MP3 player is by modified date

    '''
    toCopy = []
    xml = ET.parse(playlist)    
    
    nextIsLocation = False
    for item in xml.getroot().find('dict').find('dict').findall('dict'):
        #loading items on toCopy
        for i in item.getiterator():
            if(nextIsLocation):
                nextIsLocation = False
                
                fromF= urllib2.unquote( i.text[i.text.find('/Users'):] )
                toF= toDir+fromF[fromF.find('Media/')+5:]
                
                #changing from Artist/Album to Artist - Album. To do that, we need the penultimate '/' index from string
                toFArtistSeparatorIdx = toF.rfind('/',0,toF.rfind('/')-1)
                
                toTemp = list(toF)
                toTemp[toFArtistSeparatorIdx] = '-'
                
                toF = ''.join(toTemp)
                
                
                
                #ignore, if that path already exists on toDir
                if os.path.exists(toF):
                    continue
                
                
                toCopy.append({'fromF':fromF,'toF':toF})
            
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
    itunes_playlist_to_dir(sys.argv[1],sys.argv[2])



    

