import pytube
import sys 

#default link
link = sys.argv[2]

youtube = pytube.YouTube(link)
video = youtube.streams.get_by_resolution(sys.argv[1])
video.download(output_path='/home/bahi_djo/Documents/Videos',filename=youtube.title)
print('done')

