import os
import pdb

from PIL import Image

def thumbnail(infile, size=(128, 128)):

    outfile = os.path.splitext(infile)[0] + "_thumbnail.jpg"

    try:
        im = Image.open(infile)
        im.thumbnail(size)
        im.save(outfile, "JPEG")

    except IOError:
        print("cannot create thumbnail for", infile)

if __name__ == "__main__":
    
    thumbnail(r"C:\Users\kosmo\OneDrive - 봉림중학교\@3막\블로그\아이 부자_자녀.jpg")