from pytube import YouTube
 
yt = YouTube('https://www.youtube.com/watch?v=5pm3N3PYObo')
available_clips = yt.streams.filter(progressive=True, file_extension='mp4')
print(available_clips)
stream = available_clips.get_by_itag(22)
stream.download()
