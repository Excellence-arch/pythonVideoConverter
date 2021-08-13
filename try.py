# from moviepy import *
from moviepy.editor import *

filePath = input("Please input the name of your video and the file format: ")
p = filePath.split(".")[0]
# print(p)
createdFile = p+".mp3"

try:
	videoClip = VideoFileClip(filePath)
	clip = videoClip.audio

	clip.write_audiofile(createdFile)

	clip.close()
	videoClip.close()
except:
	print("The file you entered cannot be found")