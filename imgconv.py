import os
import sys
import multiprocessing
import subprocess
import shutil
import glob
from pathlib import Path

def get_which(): 
    which = None
    if os.name == 'nt':
        # On Windows, search for 'convert.exe' using wildcards
        which = glob.glob('C:\\Program*\\ImageMagick*\\convert.exe')
        if not which:
            print("The 'convert.exe' executable is not available. Make sure ImageMagick is installed and the path is correct.")
            return
        which = which[0]
        print('Using ImageMagic: ' + which)
    else:
        # On Unix-like systems, use the 'which' command
        which = shutil.which('convert')
        if not which:
            print("The 'convert' command is not available. Make sure ImageMagick is installed and added to your PATH.")
            return
        print('Using ImageMagic: ' + which)
    return which

def convert_image(which, src_path, dst_path):
    # import subprocess
    # Use the 'convert' command from ImageMagick to convert the image
    timeout = 15  # timeout in seconds
    try:
        result = subprocess.run([which, src_path, dst_path], timeout=timeout, capture_output=True)
        if result.returncode != 0:
            print(f"Error: {result.stderr}")
        else:
            print(f"Converted {src_path} to {dst_path}")
    except subprocess.TimeoutExpired:
        print(f"Error: The 'convert' command took longer than {timeout} seconds to complete.")
    
def main(src_dir, dst_dir):
    fext = '.jpg' # Hardcoded jpg extension
    if not os.path.exists(src_dir):
        print(f"Error: {src_dir} does not exist")
        return
    
    print('Converting') # Begin
  # Create the destination directory if it doesn't exist
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)

  # Get a list of all files in the source directory
    src_files = os.listdir(src_dir)

    # Get image conversion tool
    which = get_which()
    
  # Create a pool of workers
    with multiprocessing.Pool() as pool:
    # Iterate through the source files and convert them in parallel
        for src_file in src_files:
            src_path = os.path.join(src_dir, src_file)
            if not os.access(src_path, os.R_OK):
                print(f"Error: {src_path} is not readable")
                continue
            dst_path = os.path.join(dst_dir, src_file)
            dst_path = os.path.join(dst_dir, Path(dst_path).stem + fext)
            if not os.access(src_path, os.R_OK):
                print(f"Error: {src_path} is not readable")
                continue
            print(src_path)
            print(dst_path)
            print(which)
            print('Converting: ' + str(src_file))
            arg_tupe = (which, src_path, dst_path)
            print(type(arg_tupe))
            pool.apply_async(convert_image, args=arg_tupe)
            
        pool.close()
        pool.join()

if __name__ == '__main__':
    # Get the source and destination directories from the command line arguments
    src_dir = sys.argv[1]
    dst_dir = sys.argv[2]
    main(src_dir, dst_dir)
