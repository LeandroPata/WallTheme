import logging
import os
import sys

from PIL import Image


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


def is_valid_image(image):
	"""
	Checks if image is valid
	"""

	try:
		with Image.open(image) as img:
			img.verify()
			return True
	except (IOError, SyntaxError):
		return False


def get_image(image):
	"""
	Gets the image's absolute path if it is valid
	"""

	if not os.path.isfile(image) or not is_valid_image(image):
		logging.error('No valid image found!')
		sys.exit(1)

	image_path = os.path.abspath(image)
	return image_path


def create_dir(dir_path):
	"""
	Util function to create directories
	"""

	os.makedirs(dir_path, exist_ok=True)
