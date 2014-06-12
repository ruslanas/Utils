# simple command line image viewer
from Tkinter import *
import ImageTk
import sys

def main(name):
    master = Tk()
    master.title(name)
    photo = ImageTk.PhotoImage(file=name)

    canvas = Canvas(master, width=photo.width(), height=photo.height())
    canvas.pack()
    canvas.create_image(photo.width() / 2, photo.height() / 2, image=photo)
    master.mainloop()

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: imshow.py <file>')
        sys.exit(0)
        
    name = sys.argv[1]
    main(name)