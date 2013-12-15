#!/usr/bin/python
# coding: UTF-8

#author : younger. shen
#email  : younger.x.shen@gmail.com

#purpose : to learn python and linux stuff
#usage   :
#      python songtasteHelper.py -u http://www.songtaste.com/song/3018833/ -d ~/.music (url and your dir)


import sys
import getopt
import urllib
import re

URL = ""
DIR = "./"
BASE_URL = "http://www.songtaste.com/playmusic.php?song_id="
reST_SONG_URL = r"http://\w+.songtaste.com/\d+/[\S]*.mp3"
reURL = re.compile(r"http://www.songtaste.com/song/\d+/")

def main():
    """docstring for main"""
    cmd_handler()
    get_html_content()
    get_song_url()
    dump_to_file()

def get_html_content():
    global URL
    st_song_id = re.findall(r"\d+", URL)
    if len(st_song_id) > 0:
        song_id = st_song_id[0]
        URL = BASE_URL + song_id
    else:
        print "not find any song, try again :)"
        sys.exit(0)

def get_song_url():
    """docstring for get_song_url"""

    content = urllib.urlopen(URL).read()
    global URL
    URL = re.findall(reST_SONG_URL, content)[0]
    
def dump_to_file():
    """docstring for dumo_to_file"""
    name_list = URL.split('/');
    file_name = name_list[len(name_list) - 1]
    print "writing file " + DIR + file_name 
    path = DIR + file_name
    print URL
    dump = urllib.urlopen(URL).read()
    file = open(DIR + file_name, 'wb')
    file.write(dump)
    file.flush()
    file.close()

def print_usage():
    """docstring for print_usage"""
    print " usage: "
    print "       python songtasteHelper.py -u http://www.songtaste.com/song/3018833/ -d ~/.music (url and your dir)"

def cmd_handler():
    """docstring for cmd_handler"""
    try:
        opts ,args = getopt.getopt(sys.argv[1:], "hu:d:")
        for io, value in opts:
            if io == "-u":
                #check the url match
                mat = reURL.match(value)
                if(mat):
                    global URL
                    URL = value
                else:
                    print_usage()
                    sys.exit(0)
            elif io == "-d":
                global DIR
                DIR = value
    
    except Exception, e:
        print_usage()
        sys.exit(0)

if __name__ == "__main__":
    main()
