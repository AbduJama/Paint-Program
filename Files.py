
''' This python file is for using the open and save file as png image features
    other image types can be saved by changing the extention in the string
    below to a file format supported by pygame '''

from getName import*
from pygame import*

def SaveFile(screen,canvas,textclick):
    if textclick:
        txt = getName(screen,False)
        image.save(screen.subsurface(canvas),"Saved Images/"+txt+".png")


def OpenFile(screen,canvas,textclick):
    if textclick:
        try:
            txt = getName(screen,False)
            loadcanvas_img = image.load("Saved Images/"+txt+".png")  #need to enter the filename with filename extention
            screen.blit(loadcanvas_img,(canvas))
        except IOError:
            print("File could not be opened")

def crop(screen, colour, mp, ):
    #draw.rect(screen,colour,)
    return None
