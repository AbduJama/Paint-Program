from pygame import *
import random
from getName import*
import math


def pencil(canvas,color,omx,omy,mouseposition):
    draw.circle(canvas,color,mouseposition,1,0)
    draw.line(canvas,color,(omx,omy),mouseposition,3)
    return None

def eraser(canvas,omx,omy,mouseposition,size):
    draw.circle(canvas,(255,255,255),mouseposition,size,0)
    draw.line(canvas,(255,255,255),(omx,omy),mouseposition,size)
    return None

def brush(canvas,color,omx,omy,mouseposition,size):
    if size <= 8:
        size = 8
        draw.circle(canvas,color,mouseposition,size,0)
        draw.line(canvas,color,(omx,omy),mouseposition,2*size)
    else:
        draw.circle(canvas, color, mouseposition, size, 0)
        draw.line(canvas, color, (omx, omy), mouseposition, 2*size)
    return None

def spray(canvas,color,mouseposition,size):
    if size <= 10:
        size = 10
        draw.circle(canvas,color,
        (random.randint(mouseposition[0]-size,mouseposition[0]+size),random.randint(mouseposition[1]-size,mouseposition[1]+size)),1,0)
    else:
        draw.circle(canvas, color,
        (random.randint(mouseposition[0]-size,mouseposition[0]+size),random.randint(mouseposition[1]-size,mouseposition[1]+size)), 1, 0)
    return None

def rectangle(screen,ActionScreen,color,mp,mospos,size):
    screen.blit(ActionScreen, (0, 0))
    width = mospos[0] - mp[0]
    height = mospos[1] - mp[1]
    print(width)
    print(height)
    rected = ((mp), (width, height))
    draw.rect(screen,color,rected,size)
    draw.circle(screen,color,mp,size//2,0)
    draw.circle(screen,color,(mp[0]+width,mp[1]),size//2,0)
    draw.circle(screen,color,(mp[0],height+mp[1]),size//2,0)
    draw.circle(screen,color,mospos,size//2,0)
    return None

def square(screen,ActionScreen,color,mouseep,mospos,size):
    screen.blit(ActionScreen,(0,0))
    width = mospos[0]- mouseep[0]
    print (width)
    height = mospos[1]- mouseep[1]
    print(height)
    draw.circle(screen,color,mouseep,size//2,0)
    if width > 0 and height > 0:
        difference = abs(width - height)
        if width > height:
            rected = ((mouseep), (width, height + difference))
            pos1 = (mouseep[0],mouseep[1]+height+difference)
            pos2 = (mouseep[0]+width,mouseep[1])
            pos3 = (mouseep[0]+width,mouseep[1]+height+difference)
        elif height > width:
            rected = ((mouseep), (width + difference, height))
            pos1 = (mouseep[0],mouseep[1]+height)
            pos2 = (mouseep[0]+width+difference,mouseep[1])
            pos3 = (mouseep[0]+width+difference,mouseep[1]+height)
        else:
            rected = ((mouseep), (width, height))
            pos1 = (mouseep[0],mouseep[1]+height)
            pos2 = (mouseep[0]+width,mouseep[1])
            pos3 = (mouseep[0]+width,mouseep[1]+height)
        draw.rect(screen,color,rected,size)
        draw.circle(screen,color,pos1,size//2,0)
        draw.circle(screen,color,pos2,size//2,0)
        draw.circle(screen,color,pos3,size//2,0)
    elif width < 0 and height < 0:
        if width > height:
            difference = height - width
            rected = ((mouseep),(width+difference,height))
            pos1 = (mouseep[0],mouseep[1]+height)
            pos2 = (mouseep[0]+(width+difference),mouseep[1])
            pos3 = (mouseep[0]+(width+difference),mouseep[1]+height)
        elif height > width:
            difference = width - height
            rected = ((mouseep),(width,height+difference))
            pos1 = (mouseep[0], mouseep[1]+(height+difference))
            pos2 = (mouseep[0]+width,mouseep[1])
            pos3 = (mouseep[0]+width,mouseep[1]+(height+difference))
        else:
            rected = ((mouseep),(width,height))
            pos1 = (mouseep[0],mouseep[1]+height)
            pos2 = (mouseep[0]+height,mouseep[1])
            pos3 = (mouseep[0]+width,mouseep[1]+height)
        draw.rect(screen,color,rected,size)
        draw.circle(screen,color,pos1,size//2,0)
        draw.circle(screen,color,pos2,size//2,0)
        draw.circle(screen,color,pos3,size//2,0)
    elif width > 0 and height < 0:
        testheight = abs(height)
        if testheight > width:
            difference = testheight - width
            rected = ((mouseep),(width+difference,height))
            pos1 = (mouseep[0],mouseep[1]+height)
            pos2 = (mouseep[0]+(width+difference),mouseep[1])
            pos3 = (mouseep[0]+(width+difference),mouseep[1]+height)
        elif testheight < width:
            difference = width - testheight
            rected = ((mouseep),(width,height-difference))
            pos1 = (mouseep[0],mouseep[1]+(height-difference))
            pos2 = (mouseep[0]+width,mouseep[1])
            pos3 = (mouseep[0]+width,mouseep[1]+(height-difference))
        else:
            rected = ((mouseep),(width,height))
            pos1 = (mouseep[0],mouseep[1]+height)
            pos2 = (mouseep[0]+width,mouseep[1])
            pos3 = (mouseep[0]+width,mouseep[1]+height)
        draw.rect(screen,color,rected,size)
        draw.circle(screen,color,pos1,size//2,0)
        draw.circle(screen,color,pos2,size//2,0)
        draw.circle(screen,color,pos3,size//2,0)
    elif height > 0 and width < 0:
        testwidth = abs(width)
        if testwidth > height:
            difference = testwidth - height
            rected = ((mouseep),(width,height+difference))
            pos1 = (mouseep[0],mouseep[1]+(height+difference))
            pos2 = (mouseep[0]+width,mouseep[1])
            pos3 = (mouseep[0]+width,mouseep[1]+(height+difference))
        elif testwidth < height:
            difference = height - testwidth
            rected = ((mouseep),(width-difference,height))
            pos1 = (mouseep[0],mouseep[1]+height)
            pos2 = (mouseep[0]+(width-difference),mouseep[1])
            pos3 = (mouseep[0]+(width-difference),mouseep[1]+height)
        else:
            rected = ((mouseep),(width,height))
            pos1 = (mouseep[0],mouseep[1]+height)
            pos2 = (mouseep[0]+width,mouseep[1])
            pos3 = (mouseep[0]+width,mouseep[1]+height)
        draw.rect(screen,color,rected,size)
        draw.circle(screen,color,pos1,size//2,0)
        draw.circle(screen,color,pos2,size//2,0)
        draw.circle(screen,color,pos3,size//2,0)
    return None

def circle(screen,ActionScreen,color,mp,mospos,size):
    screen.blit(ActionScreen,(0,0))
    dist = int(math.sqrt((mospos[0] - mp[0]) ** 2 + (mospos[1] - mp[1]) ** 2))
    if dist > size:
        draw.circle(screen, color, (mp[0], mp[1]), dist, size)
        draw.circle(screen, color, (mp[0]+1,mp[1]+1), dist, size)
        draw.circle(screen, color, (mp[0]-1,mp[1]-1), dist, size)
    else:
        draw.circle(screen, color, (mp[0], mp[1]), dist, 0)
    return None

def ellipse(screen,ActionScreen,color,mp,mospos,size):
    screen.blit(ActionScreen,(0, 0))
    width = mospos[0] - mp[0]
    height = mospos[1] - mp[1]
    ellipse_rect = Rect((mp[0], mp[1]), (mospos[0] - mp[0], mospos[1] - mp[1]))  # each rect has slightly different centers to overlap and give cleaner shape
    ellipse_rect2 = Rect((mp[0]+1, mp[1]+1), (mospos[0] - mp[0], mospos[1] - mp[1]))
    ellipse_rect3 = Rect((mp[0]-1, mp[1]-1), (mospos[0] - mp[0], mospos[1] - mp[1]))
    #print(str(abs(mospos[0] - mp[0])) + ", " + str(abs(mospos[1] - mp[1])))
    ellipse_rect.normalize()
    ellipse_rect2.normalize()
    ellipse_rect3.normalize()
    #print(str(width) + ", " + str(height))
    if ellipse_rect.width <= size * 2 or ellipse_rect.height <= size * 2:
        draw.ellipse(screen, color, ellipse_rect)
    else:
        draw.ellipse(screen, color, ellipse_rect, size)  # By drawing more ellipses, the drawn shape is cleaner
        draw.ellipse(screen, color, ellipse_rect2, size)
        draw.ellipse(screen, color, ellipse_rect3, size)
    return None

def line(screen,ActionScreen,color,mp,mospos,size):
    screen.blit(ActionScreen,(0,0))
    draw.circle(screen, color, mp, size // 2, 0)
    draw.line(screen, color, mp, mospos, size)
    draw.circle(screen, color, mospos, size // 2, 0)
    return None

def multilines(screen,ActionScreen, canvas, color,mp,pointlist,connect,size):
    screen.blit(ActionScreen, (0, 0))
    if canvas.collidepoint(mp):
        pointlist.append(mp)
        draw.circle(screen, color, mp, size // 2, 0)
        if len(pointlist) >= 2:
            draw.lines(screen, color, connect, pointlist, size)
    return None

#------------------------------------------------------------------------------------
''' ---------------------------- Circular Arc Functions ----------------------------'''
def degreesToRadians(deg):
    return deg / 180.0 * math.pi

def drawCircleArc(screen, color, center, radius, startDeg, endDeg, thickness):
    (x, y) = center
    rect = (x - radius, y - radius, radius * 2, radius * 2)
    startRad = degreesToRadians(startDeg)
    endRad = degreesToRadians(endDeg)

    draw.arc(screen, color, rect, startRad, endRad, thickness)

def arc(screen,ActionScreen,color,startangle,endangle,mp,mospos,size):
    screen.blit(ActionScreen, (0, 0))
    dist = int(math.sqrt((mospos[0] - mp[0]) ** 2 + (mospos[1] - mp[1]) ** 2))
    if size >= dist:
        draw.circle(screen,color,mp,dist,0)
    if dist > size:
        drawCircleArc(screen, color, mp, dist, startangle, endangle, size)
    elif dist < 1 or dist < size:
        drawCircleArc(screen, color, mp, 1, startangle, endangle, 1)
    return None
#------------------------------------------------------------------------------------

def text(screen, canvas, textclick, comicFont, mp):
    if textclick and canvas.collidepoint(mp):
        txt = getName(screen, False)
        txtPic = comicFont.render(txt, True, (0, 0, 0))
        screen.blit(txtPic, mp)
    return None

def fill(screen, x, y, oldcolour, newcolour):
    floodfill_list = [(x,y)]  # This is the point originally clicked in the space to be flood filled
    if oldcolour == newcolour:
        #print(floodfill_list)
        return
    while len(floodfill_list) > 0:
        x, y = floodfill_list.pop()  # eventually the list will be emptied when all pixels are changed to the fill colour
        if screen.get_at((x,y)) == oldcolour:
            screen.set_at((x,y), newcolour)
            floodfill_list += [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]
            #print(floodfill_list)  #This shows the list of values before the next pixel point is popped of and checked