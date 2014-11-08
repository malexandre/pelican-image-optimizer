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
