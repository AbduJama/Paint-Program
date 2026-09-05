import pygame
import Startscreen
import Images
import BasicTools
import  Files
from getName import *


# Note: In python, all variable names in Python are said to be references to the values.
# Python keeps an internal counter to see how many references an object has and
# the garbage collector deletes objects once this reference counter goes to zero
pygame.init()

screen = pygame.display.set_mode((1200,800))
pygame.display.set_caption("Paint Program")

# Lists are mutable in python, so it is preferred to use them over
# tuple since changing their value will change the same object where as
# changing a immutable object like tuple will generate a new object

mouseep = [0,0]

firstscreen = Images.BlankCanvas_img
undolist = [firstscreen]
current_index = 0
negative_index = -1

undo_done = False


color = (0,0,0)  # Default colour for all tools that can change colour
size = 5
startangle = 0
endangle = 180
pointlist = []
connect = False
clock = pygame.time.Clock()
font.init()

Startscreen.startscreen(screen)
Startscreen.programscreen(screen)
Startscreen.ToolBox(screen)

canvas = pygame.Rect((300,80),(880,700))
pygame.draw.rect(screen,(255,255,255),canvas)

running = True
while running:
    textclick = False
    keys = pygame.key.get_pressed()
    mousepos = pygame.mouse.get_pos()
    screen.set_clip(None)  # This means that changes can occur anywhere on the screen (so buttons can be clicked)
    for occur in pygame.event.get():
        # print(event.event_name(occur.type))
        mospos = pygame.mouse.get_pos()
        if occur.type == pygame.QUIT:
            running = False
        if occur.type == pygame.MOUSEBUTTONDOWN:
            if occur.button == 1:
                ActionScreen = screen.copy()
                textclick = True
                comicFont = font.SysFont("Comic Sans MS", size)
                mouseep_tuple = pygame.mouse.get_pos()
                mouseep = list(mouseep_tuple)
                mp = occur.pos
            elif occur.button == 4 and size <= 50:
                size += 1
            elif occur.button == 5 and size >= 3: # scroll down to
                size -= 1

        if keys[pygame.K_UP] and size <= 50:
            size += 1
        elif keys[pygame.K_DOWN] and size <= 3:
            size -= 1

# -------------------------------------------------------------------------------------
#  ----- Controls for multiline tool where "ESC-key" starts a new multi-line
#  ----- and "L-key" connects the next points to the starting point -----

        if keys[pygame.K_ESCAPE]:
            connect = False
            pointlist.clear()
        if keys[pygame.K_l]:
            connect = True

# -------------------------------------------------------------------------------------
# --- Changes length of arc using startangle and changes orientation using endangle ---

        if keys[pygame.K_j] and startangle > 0:
            startangle -= 5
        if keys[pygame.K_n] and endangle > 5:
            endangle -= 5
        if keys[pygame.K_k] and startangle < 360:
            startangle += 5
        if keys[pygame.K_m] and endangle < 355:
            endangle += 5
# ------------------------------------------------------------------------------------

        if Images.ColourWheel_rect.collidepoint(mouseep[0], mouseep[1]):
            screen.blit(Images.ColourWheel_img,(30,500))
            color = screen.get_at(mouseep)
            screen.blit(Images.BrownMouse_img, (mouseep))

        if occur.type == pygame.MOUSEBUTTONUP and canvas.collidepoint(mospos[0],mospos[1]) and not Images.Tool_States[12] and not Images.Tool_States[13]:
            screen_capture = screen.copy().subsurface(canvas)
            #print("screen captured")
            if undo_done:
                del undolist[current_index+1:len(undolist)]
                current_index = 0
                negative_index = -1
                undo_done = False
            undolist.append(screen_capture)
            #print(len(undolist))




        if Images.pencil_rect.collidepoint(mouseep[0],mouseep[1]) and not Images.Tool_States[0]:
            for i0 in Images.Tool_States:
                if i0:      # i0 in the for loop represents the "element in the list" not an "index"
                    Images.Tool_States[Images.Tool_States.index(i0)] = False
            Images.Tool_States[0] = True
            Startscreen.resetToolBox(screen)
            screen.blit(Images.pencil_s_img, Images.pencil_rect)
            mouseep = [0,0]
            #print(Images.Tool_States)
        elif Images.pencil_rect.collidepoint(mouseep[0],mouseep[1]) and Images.Tool_States[0]:
            screen.blit(Images.pencil_us_img,Images.pencil_rect)
            Images.Tool_States[0] = False
            mouseep = [0,0]


        if Images.eraser_rect.collidepoint(mouseep[0],mouseep[1]) and not Images.Tool_States[1]:
            for i1 in Images.Tool_States:
                if i1:      # i1 in the for loop represents the "element in the list" not an "index"
                    Images.Tool_States[Images.Tool_States.index(i1)] = False
            Images.Tool_States[1] = True
            Startscreen.resetToolBox(screen)
            screen.blit(Images.eraser_s_img, Images.eraser_rect)
            mouseep = [0,0]
            #print(Images.Tool_States)
        elif Images.eraser_rect.collidepoint(mouseep[0],mouseep[1]) and Images.Tool_States[1]:
            screen.blit(Images.eraser_us_img,Images.eraser_rect)
            Images.Tool_States[1] = False
            mouseep = [0,0]


        if Images.brush_rect.collidepoint(mouseep[0],mouseep[1]) and not Images.Tool_States[2]:
            for i2 in Images.Tool_States:
                if i2:      # i2 in the for loop represents the "element in the list" not an "index"
                    Images.Tool_States[Images.Tool_States.index(i2)] = False
            Images.Tool_States[2] = True
            Startscreen.resetToolBox(screen)
            screen.blit(Images.brush_s_img, Images.brush_rect)
            mouseep = [0,0]
            #print(Images.Tool_States)
        elif Images.brush_rect.collidepoint(mouseep[0],mouseep[1]) and Images.Tool_States[2]:
            screen.blit(Images.brush_us_img,Images.brush_rect)
            Images.Tool_States[2] = False
            mouseep = [0,0]


        if Images.spray_rect.collidepoint(mouseep[0],mouseep[1]) and not Images.Tool_States[3]:
            for i3 in Images.Tool_States:
                if i3:      # i3 in the for loop represents the "element in the list" not an "index"
                    Images.Tool_States[Images.Tool_States.index(i3)] = False
            Images.Tool_States[3] = True
            Startscreen.resetToolBox(screen)
            screen.blit(Images.spray_s_img,Images.spray_rect)
            mouseep = [0,0]
            #print(Images.Tool_States)
        elif Images.spray_rect.collidepoint(mouseep[0],mouseep[1]) and Images.Tool_States[3]:
            screen.blit(Images.spray_us_img,Images.spray_rect)
            Images.Tool_States[3] = False
            mouseep = [0,0]

# -------------------------------------------------------------------------------------------------------------
        ''' *------------------------ The SHAPE tools UI is handled here ------------------------* '''

        if Images.shapes_rect.collidepoint(mouseep[0],mouseep[1]) and not Images.Tool_States[4]:
            for i4 in Images.Tool_States:
                if i4:
                    Images.Tool_States[Images.Tool_States.index(i4)] = False
            Images.Tool_States[4] = True
            Startscreen.resetToolBox(screen)
            screen.blit(Images.shapes_s_img,Images.shapes_rect)
            Startscreen.shapeswindowopen(screen)
            mouseep = [0,0]
            #print(Images.Tool_States)
        elif Images.shapes_rect.collidepoint(mouseep[0],mouseep[1]) and Images.Tool_States[4]:
            Startscreen.resetToolBox(screen)
            Images.Tool_States[4] = False
            mouseep = [0,0]

        if Images.Tool_States[4]:
            if Images.circle_rect.collidepoint(mouseep[0],mouseep[1]) and not Images.ExtraTool_States[0]:
                for j0 in Images.ExtraTool_States:
                    if j0:
                        Images.ExtraTool_States[Images.ExtraTool_States.index(j0)] = False
                Images.ExtraTool_States[0] = True
                Startscreen.resetshapeswindow(screen)
                screen.blit(Images.circle_s_img,Images.circle_rect)
                mouseep = [0,0]
                #print(Images.ExtraTool_States)
            elif Images.circle_rect.collidepoint(mouseep[0],mouseep[1]) and Images.ExtraTool_States[0]:
                screen.blit(Images.circle_us_img,Images.circle_rect)
                Images.ExtraTool_States[0] = False
                mouseep = [0,0]

            if Images.ellipse_rect.collidepoint(mouseep[0],mouseep[1]) and not Images.ExtraTool_States[1]:
                for j1 in Images.ExtraTool_States:
                    if j1:
                        Images.ExtraTool_States[Images.ExtraTool_States.index(j1)] = False
                Images.ExtraTool_States[1] = True
                Startscreen.resetshapeswindow(screen)
                screen.blit(Images.ellipse_s_img,Images.ellipse_rect)
                mouseep = [0,0]
                #print(Images.ExtraTool_States)
            elif Images.ellipse_rect.collidepoint(mouseep[0],mouseep[1]) and Images.ExtraTool_States[1]:
                screen.blit(Images.ellipse_us_img,Images.ellipse_rect)
                Images.ExtraTool_States[1] = False
                mouseep = [0,0]

            if Images.rectangle_rect.collidepoint(mouseep[0],mouseep[1]) and not Images.ExtraTool_States[2]:
                for j2 in Images.ExtraTool_States:
                    if j2:
                        Images.ExtraTool_States[Images.ExtraTool_States.index(j2)] = False
                Images.ExtraTool_States[2] = True
                Startscreen.resetshapeswindow(screen)
                screen.blit(Images.rectangle_s_img,Images.rectangle_rect)
                mouseep = [0,0]
                #print(Images.ExtraTool_States)
            elif Images.rectangle_rect.collidepoint(mouseep[0],mouseep[1]) and Images.ExtraTool_States[2]:
                screen.blit(Images.rectangle_us_img,Images.rectangle_rect)
                Images.ExtraTool_States[2] = False
                mouseep = [0,0]

            if Images.square_rect.collidepoint(mouseep[0],mouseep[1]) and not Images.ExtraTool_States[3]:
                for j3 in Images.ExtraTool_States:
                    if j3:
                        Images.ExtraTool_States[Images.ExtraTool_States.index(j3)] = False
                Images.ExtraTool_States[3] = True
                Startscreen.resetshapeswindow(screen)
                screen.blit(Images.square_s_img,Images.square_rect)
                mouseep = [0,0]
                #print(Images.ExtraTool_States)
            elif Images.square_rect.collidepoint(mouseep[0],mouseep[1]) and Images.ExtraTool_States[3]:
                screen.blit(Images.square_us_img,Images.square_rect)
                Images.ExtraTool_States[3] = False
                mouseep = [0,0]

# -------------------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------------------
        ''' *------------------------ The LINE tools UI is handled here ------------------------* '''

        if Images.lines_rect.collidepoint(mouseep[0],mouseep[1]) and not Images.Tool_States[5]:
            for i5 in Images.Tool_States:
                if i5:
                    Images.Tool_States[Images.Tool_States.index(i5)] = False
            Images.Tool_States[5] = True
            Startscreen.resetToolBox(screen)
            screen.blit(Images.lines_s_img,Images.lines_rect)
            Startscreen.lineswindowopen(screen)
            mouseep = [0,0]
            #print(Images.Tool_States)
        elif Images.lines_rect.collidepoint(mouseep[0],mouseep[1]) and Images.Tool_States[5]:
            #screen.blit(Images.lines_us_img,Images.lines_rect)
            Startscreen.resetToolBox(screen)
            Images.Tool_States[5] = False
            mouseep = [0,0]

        if Images.Tool_States[5]:
            if Images.line_rect.collidepoint(mouseep[0],mouseep[1]) and not Images.ExtraTool_States[4]:
                for j4 in Images.ExtraTool_States:
                    if j4:
                        Images.ExtraTool_States[Images.ExtraTool_States.index(j4)] = False
                Images.ExtraTool_States[4] = True
                Startscreen.resetlineswindow(screen)
                screen.blit(Images.line_s_img,Images.line_rect)
                mouseep = [0,0]
                #print(Images.ExtraTool_States)
            elif Images.line_rect.collidepoint(mouseep[0],mouseep[1]) and Images.ExtraTool_States[4]:
                screen.blit(Images.line_us_img,Images.line_rect)
                Images.ExtraTool_States[4] = False
                mouseep = [0,0]

            if Images.multiline_rect.collidepoint(mouseep[0],mouseep[1]) and not Images.ExtraTool_States[5]:
                for j5 in Images.ExtraTool_States:
                    if j5:
                        Images.ExtraTool_States[Images.ExtraTool_States.index(j5)] = False
                Images.ExtraTool_States[5] = True
                Startscreen.resetlineswindow(screen)
                screen.blit(Images.multiline_s_img,Images.multiline_rect)
                mouseep = [0,0]
                #print(Images.ExtraTool_States)
            elif Images.multiline_rect.collidepoint(mouseep[0],mouseep[1]) and Images.ExtraTool_States[5]:
                screen.blit(Images.multiline_us_img,Images.multiline_rect)
                Images.ExtraTool_States[5] = False
                mouseep = [0,0]

            if Images.curve_rect.collidepoint(mouseep[0],mouseep[1]) and not Images.ExtraTool_States[6]:
                for j6 in Images.ExtraTool_States:
                    if j6:
                        Images.ExtraTool_States[Images.ExtraTool_States.index(j6)] = False
                Images.ExtraTool_States[6] = True
                Startscreen.resetlineswindow(screen)
                screen.blit(Images.curve_s_img,Images.curve_rect)
                mouseep = [0,0]
                #print(Images.ExtraTool_States)
            elif Images.curve_rect.collidepoint(mouseep[0],mouseep[1]) and Images.ExtraTool_States[6]:
                screen.blit(Images.curve_us_img,Images.curve_rect)
                Images.ExtraTool_States[6] = False
                mouseep = [0,0]

# -------------------------------------------------------------------------------------------------------------

        if Images.text_rect.collidepoint(mouseep[0],mouseep[1]) and not Images.Tool_States[6]:
            for i6 in Images.Tool_States:
                if i6:
                    Images.Tool_States[Images.Tool_States.index(i6)] = False
            Images.Tool_States[6] = True
            Startscreen.resetToolBox(screen)
            screen.blit(Images.text_s_img,Images.text_rect)
            mouseep = [0,0]
            #print(Images.Tool_States)
        elif Images.text_rect.collidepoint(mouseep[0],mouseep[1]) and Images.Tool_States[6]:
            screen.blit(Images.text_us_img,Images.text_rect)
            Images.Tool_States[6] = False
            mouseep = [0,0]

        if Images.fill_rect.collidepoint(mouseep[0],mouseep[1]) and not Images.Tool_States[7]:
            for i7 in Images.Tool_States:
                if i7:
                    Images.Tool_States[Images.Tool_States.index(i7)] = False
            Images.Tool_States[7] = True
            Startscreen.resetToolBox(screen)
            screen.blit(Images.fill_s_img,Images.fill_rect)
            mouseep = [0,0]
            #print(Images.Tool_States)
        elif Images.fill_rect.collidepoint(mouseep[0],mouseep[1]) and Images.Tool_States[7]:
            screen.blit(Images.fill_us_img,Images.fill_rect)
            Images.Tool_States[7] = False
            mouseep = [0,0]


        if Images.selector_rect.collidepoint(mouseep[0],mouseep[1]) and not Images.Tool_States[8]:
            for i8 in Images.Tool_States:
                if i8:
                    Images.Tool_States[Images.Tool_States.index(i8)] = False
            Images.Tool_States[8] = True
            Startscreen.resetToolBox(screen)
            screen.blit(Images.selector_s_img,Images.selector_rect)
            mouseep = [0,0]
            #print(Images.Tool_States)
        elif Images.selector_rect.collidepoint(mouseep[0],mouseep[1]) and Images.Tool_States[8]:
            screen.blit(Images.selector_us_img,Images.selector_rect)
            Images.Tool_States[8] = False
            mouseep = [0,0]


        if Images.crop_rect.collidepoint(mouseep[0],mouseep[1]) and not Images.Tool_States[9]:
            for i9 in Images.Tool_States:
                if i9:
                    Images.Tool_States[Images.Tool_States.index(i9)] = False
            Images.Tool_States[9] = True
            Startscreen.resetToolBox(screen)
            screen.blit(Images.crop_s_img,Images.crop_rect)
            mouseep = [0,0]
            #print(Images.Tool_States)
        elif Images.crop_rect.collidepoint(mouseep[0],mouseep[1]) and Images.Tool_States[9]:
            screen.blit(Images.crop_us_img,Images.crop_rect)
            Images.Tool_States[9] = False
            mouseep = [0,0]


        if Images.copy_rect.collidepoint(mouseep[0],mouseep[1]) and occur.type == pygame.MOUSEBUTTONDOWN:
            for i10 in Images.Tool_States:
                if i10:
                    Images.Tool_States[Images.Tool_States.index(i10)] = False
            Images.Tool_States[10] = True    # This will be set to false once the task is executed
            Startscreen.resetToolBox(screen)
            screen.blit(Images.copy_s_img, Images.copy_rect)
            #clock.tick(30)
            mouseep = [0,0]
        elif occur.type == pygame.MOUSEBUTTONUP:
            #clock.tick(3)
            screen.blit(Images.copy_us_img,Images.copy_rect)


        if Images.paste_rect.collidepoint(mouseep[0],mouseep[1]) and not Images.Tool_States[11]:
            for i11 in Images.Tool_States:
                if i11:
                    Images.Tool_States[Images.Tool_States.index(i11)] = False
            Images.Tool_States[11] = True
            Startscreen.resetToolBox(screen)
            screen.blit(Images.paste_s_img,Images.paste_rect)
            mouseep = [0,0]
            #print(Images.Tool_States)
        elif Images.paste_rect.collidepoint(mouseep[0],mouseep[1]) and Images.Tool_States[11]:
            screen.blit(Images.paste_us_img,Images.paste_rect)
            Images.Tool_States[11] = False
            mouseep = [0,0]

 # -------------------------------------------------------------------------------------------------------------
 # ***HERE FORWARD IT SHOULD BE SETUP TO JUST BLINK WHEN PRESSED AND THE ACTION SHOULD BE COMMITTED***

        if Images.undo_rect.collidepoint(mouseep[0],mouseep[1]) and occur.type == pygame.MOUSEBUTTONDOWN:
            for i12 in Images.Tool_States:
                if i12:
                    Images.Tool_States[Images.Tool_States.index(i12)] = False
            Images.Tool_States[12] = True
            Startscreen.resetToolBox(screen)
            screen.blit(Images.undo_s_img,Images.undo_rect)
            if undo_done:
                negative_index = current_index - len(undolist)
            #print("Undo DOWN Button")
            if len(undolist) > 1 and negative_index > -1*(len(undolist)):
                undo_done = True
                #print("Canvas undone and put on screen")
                screen.blit(undolist[negative_index-1],(300,80))
                current_index = undolist.index(undolist[negative_index-1])
                #print(str(current_index) + ", " + str(negative_index))
            #print(Images.Tool_States)
        elif Images.undo_rect.collidepoint(mouseep[0],mouseep[1]) and occur.type == pygame.MOUSEBUTTONUP:
            screen.blit(Images.undo_us_img,Images.undo_rect)
            #print("Undo UP Button")


        if Images.redo_rect.collidepoint(mouseep[0],mouseep[1]) and occur.type == pygame.MOUSEBUTTONDOWN:
            for i13 in Images.Tool_States:
                if i13:
                    Images.Tool_States[Images.Tool_States.index(i13)] = False
            Images.Tool_States[13] = True
            Startscreen.resetToolBox(screen)
            screen.blit(Images.redo_s_img,Images.redo_rect)
            if undo_done and undolist.index(undolist[current_index]) < len(undolist)-1:
                #print("Canvas redone and put on screen")
                screen.blit(undolist[current_index+1],(300,80))
                current_index = undolist.index(undolist[current_index+1])
            #mouseep = [0,0]
            #print(Images.Tool_States)
        elif Images.redo_rect.collidepoint(mouseep[0],mouseep[1]) and occur.type == pygame.MOUSEBUTTONUP:
            screen.blit(Images.redo_us_img,Images.redo_rect)
            #mouseep = [0,0]


        if Images.open_rect.collidepoint(mouseep[0],mouseep[1]) and occur.type == pygame.MOUSEBUTTONDOWN:
            for i14 in Images.Tool_States:
                if i14:
                    Images.Tool_States[Images.Tool_States.index(i14)] = False
            Startscreen.resetToolBox(screen)
            screen.blit(Images.open_s_img,Images.open_rect)
            Files.OpenFile(screen,canvas,textclick)
            #mouseep = [0,0]
            #print(Images.Tool_States)
        elif Images.open_rect.collidepoint(mouseep[0],mouseep[1]) and occur.type == pygame.MOUSEBUTTONUP:
            screen.blit(Images.open_us_img,Images.open_rect)
            #mouseep = [0,0]


        if Images.save_rect.collidepoint(mouseep[0],mouseep[1]) and occur.type == pygame.MOUSEBUTTONDOWN:
            for i15 in Images.Tool_States:
                if i15:
                    Images.Tool_States[Images.Tool_States.index(i15)] = False
            #Images.Tool_States[15] = True
            Startscreen.resetToolBox(screen)
            screen.blit(Images.save_s_img,Images.save_rect)
            Files.SaveFile(screen,canvas,textclick)
            #mouseep = [0,0]
            #print(Images.Tool_States)
        elif Images.save_rect.collidepoint(mouseep[0],mouseep[1]) and occur.type == pygame.MOUSEBUTTONUP:
            screen.blit(Images.save_us_img,Images.save_rect)
            #mouseep = [0,0]
# -------------------------------------------------------------------------------------------------------------
        ''' *-------------------------- Tool operations are here --------------------------* '''

# Pencil Tool
    if Images.Tool_States[0] and pygame.mouse.get_pressed()[0]:
        screen.set_clip(canvas)
        BasicTools.pencil(screen,color,omx,omy,mousepos)
        screen.set_clip(None)

# Eraser Tool
    elif Images.Tool_States[1] and pygame.mouse.get_pressed()[0]:
        screen.set_clip(canvas)
        BasicTools.eraser(screen,omx,omy,mousepos,size)
        screen.set_clip(None)

# Brush Tool
    elif Images.Tool_States[2] and pygame.mouse.get_pressed()[0]:
        screen.set_clip(canvas)
        BasicTools.brush(screen,color,omx,omy,mousepos,size)
        screen.set_clip(None)

# Spray Tool
    elif Images.Tool_States[3] and pygame.mouse.get_pressed()[0]:
        screen.set_clip(canvas)
        BasicTools.spray(screen, color, mospos, size)
        screen.set_clip(None)

    elif Images.Tool_States[4] and Images.ExtraTool_States[0] and pygame.mouse.get_pressed()[0]:
        screen.set_clip(canvas)
        BasicTools.circle(screen, ActionScreen, color, mp, mospos, size)
        screen.set_clip(None)

    elif Images.Tool_States[4] and Images.ExtraTool_States[1] and pygame.mouse.get_pressed()[0]:
        screen.set_clip(canvas)
        BasicTools.ellipse(screen, ActionScreen, color, mp, mospos, size)
        screen.set_clip(None)

    elif Images.Tool_States[4] and Images.ExtraTool_States[2] and pygame.mouse.get_pressed()[0]:
        screen.set_clip(canvas)
        BasicTools.rectangle(screen, ActionScreen, color, mp, mospos, size)
        screen.set_clip(None)

    elif Images.Tool_States[4] and Images.ExtraTool_States[3] and pygame.mouse.get_pressed()[0]:
        screen.set_clip(canvas)
        BasicTools.square(screen, ActionScreen, color, mp, mospos, size)
        screen.set_clip(None)

    elif Images.Tool_States[5] and Images.ExtraTool_States[4] and pygame.mouse.get_pressed()[0]:
        screen.set_clip(canvas)
        BasicTools.line(screen, ActionScreen, color, mp, mospos, size)
        screen.set_clip(None)

    elif Images.Tool_States[5] and Images.ExtraTool_States[5] and pygame.mouse.get_pressed()[0]:
        screen.set_clip(canvas)
        BasicTools.multilines(screen, ActionScreen, canvas, color, mp, pointlist, connect, size)
        screen.set_clip(None)

    elif Images.Tool_States[5] and Images.ExtraTool_States[6] and pygame.mouse.get_pressed()[0]:
        screen.set_clip(canvas)
        BasicTools.arc(screen, ActionScreen, color, startangle, endangle, mp, mospos, size)
        screen.set_clip(None)

    elif Images.Tool_States[6] and pygame.mouse.get_pressed()[0]:
        BasicTools.text(screen, canvas, textclick, comicFont, mp)

    elif Images.Tool_States[7] and canvas.collidepoint(mp):
        oldcolor = screen.get_at((mp))
        BasicTools.fill(screen,mp[0],mp[1],oldcolor,color)

    omx = mousepos[0]
    omy = mousepos[1]
    clock.tick(60)
    pygame.display.flip()

pygame.quit()
