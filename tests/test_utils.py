"""
Tests for utility functions
"""

import os
import shutil
from pathlib import Path

from walltheme import utils


def test_create_dir():
	"""
	Testing creating a directory
	"""
	tmp_dir = 'tmp'
	utils.create_dir(tmp_dir)
	assert os.path.isdir(tmp_dir)
	os.rmdir(tmp_dir)


def test_dir_check():
	"""
	Testing if is a directory
	"""
	# Should be True
	is_dir = utils.is_dir('tests')
	# Should be True (reversed boolean value for easier understanding)
	is_not_dir = not utils.is_dir('tests/test_files/test')

	assert is_dir and is_not_dir


def test_empty_dir_check():
	"""
	Testing if a directory is empty
	"""
	is_empty = utils.is_dir_empty('tests')
	assert not is_empty

	tmp_dir = 'tmp'
	utils.create_dir(tmp_dir)
	is_empty = utils.is_dir_empty(tmp_dir)
	assert is_empty
	os.rmdir(tmp_dir)


def test_file_check():
	"""
	Testing if is a directory
	"""
	# Should be True
	is_file = utils.is_file('tests/test_files/test')
	# Should be True (reversed boolean value for easier understanding)
	is_not_file = not utils.is_file('tests')

	assert is_file and is_not_file


def test_is_valid_image():
	"""
	Testing if a file is a valid image
	"""
	img_formats = ['.png', '.jpg', '.jpeg', '.webp']

	test_file_dir = Path('tests/test_files')

	for file_path in test_file_dir.iterdir():
		extension = ''.join(file_path.suffixes).lower()
		if extension in img_formats:
			assert utils.is_valid_image(file_path)
		else:
			assert not utils.is_valid_image(file_path)


def test_init_templates():
	"""
	Testing initializing templates
	"""
	tmp_dir = 'tmp'
	utils.create_dir(tmp_dir)
	utils.init_templates(tmp_dir)
	is_empty = utils.is_dir_empty(tmp_dir)
	assert not is_empty
	shutil.rmtree(tmp_dir)
