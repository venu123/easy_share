import gdata.youtube
import gdata.geo
import gdata.youtube.service
import gdata.media
import re
#import globals

'''
    Function uploads a video pointed by filename to YouTube
    It returns the Url of the uploaded video
'''
def post_to_youtube(filename,video_title,username=None,password=None) :
    #fout=open("logdirect.txt","w")
    yt_service = gdata.youtube.service.YouTubeService()
    #fout.write(yt_service.text())
    yt_service.ssl = False
    if username is None or password is None:
        # call UI .. set the username and password
        # Store them in globals.youtube_*
        # just in case, its taken as func arguments now
        youtube_username = username
        youtube_password = password
    
    yt_service.email = username
    yt_service.password= password
    yt_service.source = 'youtube_uploader'
    yt_service.developer_key = 'AI39si5tP665MN8g-UXMJlvnGjKwrS36geG6pZWYHvBOXaeRAZ-DAhjMAWnqRGo5AOiJ_rgmjk8FCDgtqMFsM-YwQwmlK0Uh9w'
    yt_service.client_id = 'youtube_uploader'
    try :
      yt_service.ProgrammaticLogin()
    except :
      raise NameError('Could not authenticate user')
      return 0
    
    # prepare a media group object to hold our video's meta-data
    my_media_group = gdata.media.Group(
    title=gdata.media.Title(text=video_title),
    description=gdata.media.Description(description_type='plain',
                                      text='Uploaded from EasyShare'),
    keywords=gdata.media.Keywords(text='EasyShare'),
    category=[gdata.media.Category(
      text='Autos',
      scheme='http://gdata.youtube.com/schemas/2007/categories.cat',
      label='Autos')],
      player=None
    )
    #fout.write("/n"+my_media_group)
    try:    
        video_entry = gdata.youtube.YouTubeVideoEntry(media=my_media_group,geo=None)
        #fout.write("/n"+"video_entry"+video_entry)
        video_location = filename
        #fout.write("/n"+"video_location"+video_location)
        #fout.close()
        print("outer block succesful")
        try :
            new_entry = yt_service.InsertVideoEntry(video_entry, video_location)
        except :
            raise NameError('could not authenticate the user')
            return 0
        try :
            res = re.search("href=\"(.*?)\"",str(new_entry.GetHtmlLink()),0)
            if res.group(1) is not None:
                return res.group(1)
            else:
                return 0
        except : 
            raise NameError('Error in reg ex')
            return 0
    
    except:
        raise NameError("Error with uploading")
        return 0
        
#post_to_youtube('/home/subrahmanya/bike','one more vedio for youtube','sunnypes09','sunnymttl6pesit')
