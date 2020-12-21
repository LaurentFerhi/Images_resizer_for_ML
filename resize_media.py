### Script to resize images and videos
# By Laurent Ferhi

import PIL
from PIL import Image
import os
import moviepy.editor as mp

initial_path = os.path.abspath(os.getcwd())

# Create new folder for resized images
if 'resized_images' not in os.listdir():
	os.mkdir('resized_images')
	os.chdir(initial_path) # return to initial path

# Create new folder for resized images
if 'resized_videos' not in os.listdir():
	os.mkdir('resized_videos')
	os.chdir(initial_path) # return to initial path

# base width for resized image and height for resized video in pixels
basewidth = int(input('Images - Nombre de pixels en base (reco: 900) ?'))
height = int(input('Videos - Nombre de pixels en hauteur (reco: 240) ?'))

# for all files in directory with image extension
supported_files_img = ['jpg','JPG']
for name in [file for file in os.listdir() if file[-3:] in supported_files_img]:
	# load image
	img = Image.open(name)
	# New dimensions
	wpercent = (basewidth / float(img.size[0]))
	hsize = int((float(img.size[1]) * float(wpercent)))
	# Antialiasing to avoid grain effect
	img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
	print(name+' redimensionnée avec succès')
	img.save('resized_images\\resized_'+name)

# for all files in directory with video extension
supported_files_vid = ['mp4','MP4','avi','AVI']
for name in [file for file in os.listdir() if file[-3:] in supported_files_vid]:
	clip = mp.VideoFileClip(name)
	clip_resized = clip.resize(height=height)
	clip_resized.write_videofile('resized_videos\\resized_'+name[:-4]+'.mp4')

# Print size of new img folder
os.chdir('resized_images')
folder_img_size = sum(os.path.getsize(f) for f in os.listdir() if os.path.isfile(f))
print('\nTaille du dossier resized_images: {} Mo'.format(round(folder_img_size/1E6,2)))
os.chdir(initial_path)

# Print size of new vid folder
os.chdir('resized_videos')
folder_vid_size = sum(os.path.getsize(f) for f in os.listdir() if os.path.isfile(f))
print('\nTaille du dossier resized_images: {} Mo'.format(round(folder_vid_size/1E6,2)))