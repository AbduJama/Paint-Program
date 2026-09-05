from pygame import image
from pygame import Rect

""" --------- This module is used only to load the Images and generate Rectangles -----------
    The Images below are listed with comments giving each of their dimensions in the form (width,height) 
    The Rectangles will be used to host the Tools and Colour Palette"""

#-------------------------------------------------------------------------------------
import os
import sys
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
#-------------------------------------------------------------------------------------

# *------------------------ Start Screen and Program Screen -----------------------------*

Background_img = image.load(resource_path("Images/Other/greyback.jpg")) # (1200,800)
StartTitle_img = image.load(resource_path("Images/Other/starttitle.png")) # (500,200)
StartIcon_img = image.load(resource_path("Images/Other/starticon.png"))  # (200,200)
Period1_img = image.load(resource_path("Images/Other/period.png")) # (50,50)
Period2_img = image.load(resource_path("Images/Other/period.png")) # (50,50)
Period3_img = image.load(resource_path("Images/Other/period.png")) # (50,50)
Period4_img = image.load(resource_path("Images/Other/period.png")) # (50,50)
Period5_img = image.load(resource_path("Images/Other/period.png")) # (50,50)

Toolbox_img = image.load(resource_path("Images/Other/Toolbox.png"))  # (180,400)
ColourWheel_img = image.load(resource_path("Images/Other/colour palette.png"))  # (250,280)
ToolTips_img = image.load(resource_path("Images/Other/Tool Tips.png")) # (500,75)
ToolTipsClear_img = image.load(resource_path("Images/Other/ToolTips Clear.jpg")) # (500,75)
BrownMouse_img = image.load(resource_path("Images/Other/mouse.png")) # (16,16)

ProgramTitle_img = image.load(resource_path("Images/Other/programtitle.png")) # (250,50)
ProgramIcon_img = image.load(resource_path("Images/Other/programicon.png"))  # (50,50)
BlankCanvas_img = image.load(resource_path("Images/Other/blank.jpg"))  # (880,700)

# *--------------------------------------------------------------------------------------*

# *-------------------------------- Unselected Tools -------------------------------------*

arrow_up_img = image.load(resource_path("Images/Other/uparrow.jpg"))
brush_us_img = image.load(resource_path("Images/Unselected Tools/brush_unselected.jpg"))
circle_us_img = image.load(resource_path("Images/Unselected Tools/circle_unselected.jpg"))
copy_us_img = image.load(resource_path("Images/Unselected Tools/copy_unselected.jpg"))
crop_us_img = image.load(resource_path("Images/Unselected Tools/crop_unselected.jpg"))
curve_us_img = image.load(resource_path("Images/Unselected Tools/curve_unselected.jpg"))
ellipse_us_img = image.load(resource_path("Images/Unselected Tools/ellipse_unselected.jpg"))
eraser_us_img = image.load(resource_path("Images/Unselected Tools/eraser_unselected.jpg"))
fill_us_img = image.load(resource_path("Images/Unselected Tools/fill_unselected.jpg"))
line_us_img = image.load(resource_path("Images/Unselected Tools/line_unselected.jpg"))
lines_us_img = image.load(resource_path("Images/Unselected Tools/lines_unselected.jpg"))
multiline_us_img = image.load(resource_path("Images/Unselected Tools/multi-line_unselected.jpg"))
open_us_img = image.load(resource_path("Images/Unselected Tools/open_unselected.jpg"))
paste_us_img = image.load(resource_path("Images/Unselected Tools/paste_unselected.jpg"))
pencil_us_img = image.load(resource_path("Images/Unselected Tools/pencil_unselected.jpg"))
rectangle_us_img = image.load(resource_path("Images/Unselected Tools/rectangle_unselected.jpg"))
redo_us_img = image.load(resource_path("Images/Unselected Tools/redo_unselected.jpg"))
save_us_img = image.load(resource_path("Images/Unselected Tools/save_unselected.jpg"))
selector_us_img = image.load(resource_path("Images/Unselected Tools/selector_unselected.jpg"))
shapes_us_img = image.load(resource_path("Images/Unselected Tools/shapes_unselected.jpg"))
spray_us_img = image.load(resource_path("Images/Unselected Tools/spray_unselected.jpg"))
square_us_img = image.load(resource_path("Images/Unselected Tools/square_unselected.jpg"))
text_us_img = image.load(resource_path("Images/Unselected Tools/text_unselected.jpg"))
undo_us_img = image.load(resource_path("Images/Unselected Tools/undo_unselected.jpg"))

# *--------------------------------------------------------------------------------------*

# *-------------------------------- Selected Tools ---------------------------------------*

arrow_down_img = image.load(resource_path("Images/Other/downarrow.jpg"))
brush_s_img = image.load(resource_path("Images/Selected Tools/brush_selected.jpg"))
circle_s_img = image.load(resource_path("Images/Selected Tools/circle_selected.jpg"))
copy_s_img = image.load(resource_path("Images/Selected Tools/copy_selected.jpg"))
crop_s_img = image.load(resource_path("Images/Selected Tools/crop_selected.jpg"))
curve_s_img = image.load(resource_path("Images/Selected Tools/curve_selected.jpg"))
ellipse_s_img = image.load(resource_path("Images/Selected Tools/ellipse_selected.jpg"))
eraser_s_img = image.load(resource_path("Images/Selected Tools/eraser_selected.jpg"))
fill_s_img = image.load(resource_path("Images/Selected Tools/fill_selected.jpg"))
line_s_img = image.load(resource_path("Images/Selected Tools/line_selected.jpg"))
lines_s_img = image.load(resource_path("Images/Selected Tools/lines_selected.jpg"))
multiline_s_img = image.load(resource_path("Images/Selected Tools/multi-line_selected.jpg"))
open_s_img = image.load(resource_path("Images/Selected Tools/open_selected.jpg"))
paste_s_img = image.load(resource_path("Images/Selected Tools/paste_selected.jpg"))
pencil_s_img = image.load(resource_path("Images/Selected Tools/pencil_selected.jpg"))
rectangle_s_img = image.load(resource_path("Images/Selected Tools/rectangle_selected.jpg"))
redo_s_img = image.load(resource_path("Images/Selected Tools/redo_selected.jpg"))
save_s_img = image.load(resource_path("Images/Selected Tools/save_selected.jpg"))
selector_s_img = image.load(resource_path("Images/Selected Tools/selector_selected.jpg"))
shapes_s_img = image.load(resource_path("Images/Selected Tools/shapes_selected.jpg"))
spray_s_img = image.load(resource_path("Images/Selected Tools/spray_selected.jpg"))
square_s_img = image.load(resource_path("Images/Selected Tools/square_selected.jpg"))
text_s_img = image.load(resource_path("Images/Selected Tools/text_selected.jpg"))
undo_s_img = image.load(resource_path("Images/Selected Tools/undo_selected.jpg"))

# *--------------------------------------------------------------------------------------*

# *------------------------------- Tools Rectangles --------------------------------------*

ColourWheel_rect = Rect((40,540),(235,235))
pencil_rect = Rect((85,80),(36,36))
eraser_rect = Rect((175,80),(36,36))
brush_rect = Rect((85,125),(36,36))
spray_rect = Rect((175,125),(36,36))

shapes_rect = Rect((85,170),(36,36))
shapesarrow_rect = Rect((121,170),(15,36))
circle_rect = Rect((85,206),(36,36))
ellipse_rect = Rect((121,206),(36,36))
rectangle_rect = Rect((157,206),(36,36))
square_rect = Rect((193,206),(36,36))

lines_rect = Rect((175,170),(36,36))
linesarrow_rect = Rect((211,170),(15,36))
line_rect = Rect((175,206),(36,36))
multiline_rect = Rect((139,206),(36,36))
curve_rect = Rect((103,206),(36,36))

text_rect = Rect((85,251),(36,36))
fill_rect = Rect((175,251),(36,36))
selector_rect = Rect((85,296),(36,36))
crop_rect = Rect((175,296),(36,36))
copy_rect = Rect((85,341),(36,36))
paste_rect = Rect((175,341),(36,36))
undo_rect = Rect((85,386),(36,36))
redo_rect = Rect((175,386),(36,36))
open_rect = Rect((85,431),(36,36))
save_rect = Rect((175,431),(36,36))

# *---------------------------------------------------------------------------------------*

# Tool_State = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
Tool_States = [False,False,False,False,
               False,False,False,False,
               False,False,False,False,
               False,False,False,False]

ExtraTool_States = [False,False,False,False,
                    False,False,False]


