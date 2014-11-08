# -*- coding: utf-8 -*-

"""
Optimized images (gif, jpeg & png)
Assumes that Gifsicle, ImageMagick's convert and pngquant are isntalled on path.
http://www.lcdf.org/gifsicle/
http://www.imagemagick.org/
http://pngquant.org/
Copyright (c) 2014 Marc Alexandre (http://www.malexandre.fr)
"""

import os
import shutil
from subprocess import call

from pelican import signals

# The commands list per file type
JPEG = 'convert -strip -interlace Plane -gaussian-blur 0.05 ' +\
       '-quality 85% "{filename}" "{filename}."'
COMMANDS = {
    '.jpg': JPEG,
    '.jpeg': JPEG,
    '.png': 'pngquant -o "{filename}." "{filename}"',
    '.gif': 'gifsicle --no-warnings -O "{filename}" -o "{filename}."'
}


def pelican_image_optimizer(pelican):
    """
    Optimized gif, jpg and png images

    @param pelican: The Pelican instance
    """
    for dirpath, _, filenames in os.walk(pelican.settings['OUTPUT_PATH']):
        for name in filenames:
            if os.path.splitext(name)[1] in COMMANDS.keys():
                optimize(dirpath, name)

def optimize(dirpath, filename):
    """
    Optimize the image.

    @param dirpath: Path of folder containing the file to optimze
    @param filename: File name to optimize
    """
    filepath = os.path.join(dirpath, filename)

    ext = os.path.splitext(filename)[1]
    command = COMMANDS[ext].format(filename=filepath)
    call(command, shell=True)
    originsize = os.path.getsize(filepath)
    newsize = os.path.getsize(filepath + '.')

    if newsize < originsize:
        shutil.move(filepath + '.', filepath)
    else:
        os.remove(filepath + '.')


def register():
    """
    Register the plugin in Pelican.
    """
    signals.finalized.connect(pelican_image_optimizer)

