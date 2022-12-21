# Batch_Img_Convert using ImageMagick
Uses `multiprocessing`.
Takes any image format readable by ImageMagick.
For now, output image format is defaulted to JPG.
Tested with `ImageMagick-7.1.0` and Windows 11.
Untested with \*nix but might work.

To install ImageMagick, you can use a package manager such as apt-get (on Debian-based systems) or yum (on Red Hat-based systems). 
For example, to install ImageMagick on a Debian-based system, you can use the following command:

```sudo apt-get install imagemagick```

Alternatively, you can download and build ImageMagick from source. 
For more information, see the [ImageMagick documentation](https://www.imagemagick.org/script/index.php).

Once ImageMagick is installed, you can use the script by passing the source directory and destination directory as command line arguments:
```python imgconv.py /path/to/src/dir /path/to/dst/dir```

The script will create the destination directory if it doesn't exist, and then it will iterate through all the files in the source directory and convert them in parallel using the `multiprocessing` module.
