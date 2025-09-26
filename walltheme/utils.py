import logging
import os
import sys


def split_theme(theme: dict):
	"""
	Splits the various types of data to facilitate the creation of templates
	"""

	i = 0
	wallpaper = ''
	special = {}
	palette = {}
	for k, v in theme.items():
		if i <= 0:
			wallpaper = v
		elif 0 < i < 4:
			special[k] = v
		else:
			palette[k] = v

		i += 1

	return wallpaper, special, palette


def get_image(image):
	"""
	Checks if the image is valid and gets its absolute path if true
	"""

	if not os.path.isfile(image):
		logging.error('No valid image found!')
		sys.exit(1)

	image_path = os.path.abspath(image)
	return image_path


def create_dir(dir_path):
	"""
	Util function to create directories
	"""

	os.makedirs(dir_path, exist_ok=True)
