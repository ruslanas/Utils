# simple command line image viewer
from Tkinter import *
from PIL import Image
import ImageTk
import imagehash
import sys

def main(name):
    master = Tk()
    master.title(name)
    photo = ImageTk.PhotoImage(file=name)

    hsh = imagehash.average_hash(Image.open(name))

    canvas = Canvas(master, width=photo.width(), height=photo.height())
    canvas.create_image(photo.width() / 2, photo.height() / 2, image=photo)
    canvas.pack()

    msg = Message(master, text=str(hsh) + ' ' + name + ' (%d X %d)' % (photo.width(), photo.height()), width=photo.width())
    msg.pack()
    master.bind('<Escape>', lambda x: master.quit())
    master.mainloop()

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: imshow.py <file>')
        sys.exit(0)
        
    name = sys.argv[1]
    main(name)