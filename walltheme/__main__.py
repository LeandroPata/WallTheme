"""
WallTheme by Leandro Pata
"""

import argparse
import os
import sys
from pathlib import Path

from . import colors, jinja, utils


def get_args() -> argparse.Namespace:
	"""
	Gets the arguments passed to the program
	"""

	arg = argparse.ArgumentParser(
		prog='WallTheme',
		description="Generate themes from an image's dominant colors",
	)
	arg.add_argument('image', help='Path to image file')
	arg.add_argument(
		'-m',
		'--max-colors',
		type=int,
		default=5,
		required=False,
		help='Number of dominant colors',
	)
	return arg


def parse_args_exit(parser):
	"""
	Arguments restrictions that cause the program to exit
	"""

	args = parser.parse_args()

	if not args.image:
		parser.error('No image provided!')
		sys.exit(1)


def parse_args(parser):
	"""
	Parses the arguments and generates the theme
	"""

	args = parser.parse_args()

	if args.image:
		image = utils.get_image(args.image)
		d_colors = colors.get_dominant_colors(image, args.max_colors)
		theme = colors.gen_theme(image, d_colors)
	else:
		parser.error('No image provided!')
		sys.exit(1)

	return theme


def main():
	"""
	Main function
	"""

	templates_dir = Path(os.path.expanduser('~/.config/walltheme/templates'))
	output_dir = Path(os.path.expanduser('~/.cache/walltheme'))
	utils.create_dir(templates_dir)
	utils.create_dir(output_dir)

	parser = get_args()
	parse_args_exit(parser)
	theme = parse_args(parser)

	jinja.render_templates(templates_dir, output_dir, theme)
	print('Templates rendered to:', output_dir)


if __name__ == '__main__':
	main()
