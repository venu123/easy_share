#!/usr/bin/pythoni

###
# This script serves to upload the pictures from the specified directory to the specified album in picasa.
# Usage : python picasaUploader -l <source directory> 
###
import gdata.photos.service
import gdata.media
import gdata.geo
import sys
import re
#import globals




'''
Function takes in filename,title,username and password
    uploads the given photo to the account
    and returns the url of that photo
'''
def post_to_picasa(filename,photo_title=None,username=None,password=None):
    fp = open("picasa.log","w")
    
    gd_client = gdata.photos.service.PhotosService()
    #UI should be called and parameters passed!
    #if picasa_username is None or picasa_password is None:
        # call UI .. set the username and password
        # Store them in globals.youtube_*
        # just in case, its taken as func arguments now
    print "*"*15
    print filename
    print photo_title
    print username
    print password
    picasa_username = username#"sandeep080" #username
    picasa_password = password#"helloWorld" #password
    photo_title = str(photo_title)
    if type(photo_title) == str:
      print "working!"
    else:
      photo_title = "namskara"
    picasa_title =  "worst_le22"
    #"jinchak"
    #fp.write("uname\n" + username)
    #fp.write("passwd\n" + password)
    #fp.write("ptitle\n" + photo_title)
    print "*"*15
    print picasa_username
    print picasa_password
    print photo_title
    print "*"*15
    gd_client.email = picasa_username #type your username here
    gd_client.password = picasa_password # store your password in an environment variable called PASSWD
    gd_client.source = 'python uploader'
    try:
        gd_client.ProgrammaticLogin()
    except:
        raise NameError('Could not authenticate the user')
        return 0
    
    username=gd_client.email
    index = 0
    try:
	
        #album = gd_client.InsertAlbum(title=photo_title,summary='Uploaded from EasyShare')
        album = gd_client.InsertAlbum(title=photo_title,summary='Uploaded from EasyShare')
        #print album
    except:
        raise NameError('Could not create Album')
        return 0
    album_url = '/data/feed/api/user/%s/albumid/%s' %(username,album.gphoto_id.text)
    try:
        photo = gd_client.InsertPhotoSimple(album_url,photo_title,'Uploaded from EasyShare',filename,content_type='image/jpeg')
    except :
        raise NameError('Error uploading photo')
        return 0
    try:
        res = re.search("href=\"(.*?)\"",str(photo.GetHtmlLink()),0)
        if res.group(1) is not None:
            return res.group(1)
        else:
            raise 'Could not extract link'
            return 0
    except: 
        raise 'Error in reg ex'
        return 0

#print post_to_picasa(filename = '/home/pali/Pictures/ubu.jpg', photo_title='Ubuntu', username = 'kartalkhan', password = 'kartalkhanAjja')
#title=sys.argv[0]
#post_to_picasa('/home/subrahmanya/PICASA/super.jpg','pes','sunnymttl6@gmail.com','sunnymttl6pesit')
