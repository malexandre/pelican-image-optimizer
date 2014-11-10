pelican-image-optimizer
=======================

This [pelican](http://blog.getpelican.com/) plugin uses ImageMagick, PNGQuant &amp; Gifsicle to optimize images for web. Using these tools give a fast and efficient result.

## Requirements

[ImageMagick](http://www.imagemagick.org/), [Gifsicle](http://www.lcdf.org/gifsicle/) & [pngquant](http://pngquant.org/) are required.

On Ubuntu:
```bash
sudo apt-get install gifsicle imagemagick pngquant
```

On Fedora:
```bash
sudo yum install -y gifsicle ImageMagick pngquant
```

## Installation

See the [pelican documentation](http://docs.getpelican.com/en/latest/plugins.html).

## Usage

All the GIF, PNG & JPEG images of your blog will be optimized during the build.
Adding `IMAGE_OPTIMIZATION_ONCE_AND_FOR_ALL = True` to you `pelicanconf.py` will optimize the images in the content folder directly. The files will be renamed `_optimized`, but once in the output folder, they will be renamed without the `_optimized`.
The markdown files need to use the name without `_optimized`.

Example:
1. I write the article `test` with an image `content/img/test.png` linked in the template and saved in my content folder.
2. On pelican generation, the file is optimized in my content folder and renamed `test_optimized.png`. In my output folder, the file is `test.png`, so my markdown link still works.
3. On the next pelican generation, the file won't be optimized, reducing the time for the generation.
