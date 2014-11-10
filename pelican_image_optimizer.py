# -*- coding: utf-8 -*-

"""
Optimized images (gif, jpeg & png)
Assumes that Gifsicle, ImageMagick's convert and pngquant are isntalled on path
http://www.lcdf.org/gifsicle/
http://www.imagemagick.org/
http://pngquant.org/
Copyright (c) 2014 Marc Alexandre (http://www.malexandre.fr)
"""

import os
import re
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

OPTIMIZED = '_optimized'
FLAG = 'IMAGE_OPTIMIZATION_ONCE_AND_FOR_ALL'


def image_optimizer_initialized(pelican):
    """
    Optimized gif, jpg and png images.

    @param pelican: The Pelican instance
    """
    if not pelican.settings[FLAG]:
        return

    for dirpath, _, filenames in os.walk(pelican.settings['PATH']):
        for name in filenames:
            if os.path.splitext(name)[1] in COMMANDS.keys():
                if not re.search(OPTIMIZED + r'\.(png|jpg|jpeg|gif)', name):
                    optimize(pelican, dirpath, name)


def image_optimizer_finalized(pelican):
    """
    Optimized gif, jpg and png images. If the
    FLAG settings is set to True, just rename
    the file alread optimized.

    @param pelican: The Pelican instance
    """
    for dirpath, _, filenames in os.walk(pelican.settings['OUTPUT_PATH']):
        for name in filenames:
            if os.path.splitext(name)[1] in COMMANDS.keys():
                if pelican.settings[FLAG]:
                    if '_optimized' in name:
                        filepath = os.path.join(dirpath, name)
                        newname = re.sub(OPTIMIZED + r'\.(png|jpg|jpeg|gif)',
                                         r'.\1', name)
                        newfilepath = os.path.join(dirpath, newname)
                        shutil.move(filepath, newfilepath)
                else:
                    optimize(pelican, dirpath, name)


def optimize(pelican, dirpath, filename):
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

    if pelican.settings[FLAG]:
        new_name = re.sub(r'\.(png|jpg|jpeg|gif)',
                          OPTIMIZED + r'.\1', filename)
        shutil.move(filepath, os.path.join(dirpath, new_name))


def register():
    """
    Register the plugin in Pelican.
    """
    signals.initialized.connect(image_optimizer_initialized)
    signals.finalized.connect(image_optimizer_finalized)
