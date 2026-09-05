
import time
from pygame import constants

import pygame
import Images

# def startscreen():
#     start = True
#     counter = move_period = count = 0
#     boolean = [False,False,False,False]
#     screen.blit(Images.Background_img, (0, 0))
#     screen.blit(Images.StartTitle_img, (350, 150))
#     screen.blit(Images.StartIcon_img, (500, 360))

def startscreen(screen):
    start = True
    counter = move_period = count = 0
    boolean = [False,False,False,False]
    screen.blit(Images.Background_img, (0, 0))
    screen.blit(Images.StartTitle_img, (350, 150))
    screen.blit(Images.StartIcon_img, (500, 360))

    while start:
        counter += 1
        if counter == 101:
            start = False
        elif counter % 20 == 0 and counter != 0:
            if count <= 3:
                boolean[count] = True
            count += 1
        for occur in pygame.event.get():
            counter += 1
            if counter == 101 or occur.type == pygame.QUIT:
                start = False
            elif counter % 20 == 0 and counter != 0:
                if count <= 3:
                    boolean[count] = True
                count += 1

        # Note: Because the Background of the start screen is blit() in the while loop, the dots are blit() in this way
        # However, blitting the images like this takes more time which results in a better loading screen :)

        time.sleep(0.02) # This slows the blit(...) of the next period in this while loop
        screen.blit(Images.Period1_img, (400, 580))
        if boolean[0]:
            screen.blit(Images.Period1_img, (400 + 80, 580))
        if boolean[1]:
            screen.blit(Images.Period1_img, (400 + 160, 580))
        if boolean[2]:
            screen.blit(Images.Period1_img, (400 + 240, 580))
        if boolean[3]:
            screen.blit(Images.Period1_img, (400 + 320, 580))
        pygame.display.flip()
    return None


def programscreen(screen):
    screen.blit(Images.Background_img, (0,0))
    screen.blit(Images.Toolbox_img,(65,45))
    screen.blit(Images.ColourWheel_img,(30,500))
    screen.blit(Images.BrownMouse_img,(150,650))
    screen.blit(Images.ProgramTitle_img,(345,10))
    screen.blit(Images.ProgramIcon_img,(605,10))
    return None

def ToolBox(screen):
    # *----------------- Putting tools on screen -----------------*
    screen.blit(Images.pencil_us_img,Images.pencil_rect)
    screen.blit(Images.eraser_us_img,Images.eraser_rect)
    screen.blit(Images.brush_us_img,Images.brush_rect)
    screen.blit(Images.spray_us_img,Images.spray_rect)
    screen.blit(Images.shapes_us_img,Images.shapes_rect)
    screen.blit(Images.arrow_up_img,Images.shapesarrow_rect)
    screen.blit(Images.lines_us_img,Images.lines_rect)
    screen.blit(Images.arrow_up_img,Images.linesarrow_rect)
    screen.blit(Images.text_us_img,Images.text_rect)
    screen.blit(Images.fill_us_img,Images.fill_rect)
    screen.blit(Images.selector_us_img,Images.selector_rect)
    screen.blit(Images.crop_us_img,Images.crop_rect)
    screen.blit(Images.copy_us_img,Images.copy_rect)
    screen.blit(Images.paste_us_img,Images.paste_rect)
    screen.blit(Images.undo_us_img,Images.undo_rect)
    screen.blit(Images.redo_us_img,Images.redo_rect)
    screen.blit(Images.open_us_img,Images.open_rect)
    screen.blit(Images.save_us_img,Images.save_rect)
    return None

# create a function to slide open the shapes window and a function to close the shapes window

def resetToolBox(screen):
    screen.blit(Images.Toolbox_img, (65, 45))
    ToolBox(screen)
    return None

def shapeswindowopen(screen):
    screen.blit(Images.arrow_down_img,Images.shapesarrow_rect)
    screen.blit(Images.circle_us_img,Images.circle_rect)
    screen.blit(Images.ellipse_us_img,Images.ellipse_rect)
    screen.blit(Images.rectangle_us_img,Images.rectangle_rect)
    screen.blit(Images.square_us_img,Images.square_rect)
    return None

def lineswindowopen(screen):
    screen.blit(Images.arrow_down_img,Images.linesarrow_rect)
    screen.blit(Images.line_us_img,Images.line_rect)
    screen.blit(Images.multiline_us_img,Images.multiline_rect)
    screen.blit(Images.curve_us_img,Images.curve_rect)
    return None

def resetshapeswindow(screen):
    screen.blit(Images.circle_us_img,Images.circle_rect)
    screen.blit(Images.ellipse_us_img,Images.ellipse_rect)
    screen.blit(Images.rectangle_us_img,Images.rectangle_rect)
    screen.blit(Images.square_us_img,Images.square_rect)
    return None

def resetlineswindow(screen):
    screen.blit(Images.line_us_img, Images.line_rect)
    screen.blit(Images.multiline_us_img, Images.multiline_rect)
    screen.blit(Images.curve_us_img, Images.curve_rect)
    return None