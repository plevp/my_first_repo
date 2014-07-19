# Simple "screensaver" program.

# Import modules
import simpleguitk as simplegui

import random

# Global state
counter = 0
# message = "0:00:0"
position = [40, 60]
width = 200
height = 60
interval = 100
work = False;
try_count = 0;
success = 0;

def format():
    global counter;
    min = counter / 600;
    sec = ((counter) % 600 )/ 10
    msec = counter % 10
    return '%d:%02d.%d' % (min, sec, msec)

    #return str(min) + ":" + str(sec).rjust(2, '0') +"." + str(msec)


    
# Handler for timer
def tick():
    global counter;
    if work:
        counter += 1
        
def start():
    global work
    work = True;

def stop():
    global work, counter, success, try_count
    try_count += 1;
    if counter % 10 ==0 :
        success +=1;
    work = False;

def reset():
    global work, counter, success, try_count;
    
    work = False;
    counter = 0;
    success = 0;
    try_count = 0;


# Handler to draw on canvas
def draw(canvas):
    global work, counter, success, try_count;
    
    canvas.draw_text(format(), position, 18, "White")
    #canvas.draw_text(str(success) + "/" + str(try_count),  [160, 40], 12, "Orange")
    canvas.draw_text('%d/%d' % (success, try_count),  [160, 40], 12, "Orange")


# Create a frame 
frame = simplegui.create_frame("Home", width, height)

frame.add_button("Start", start);
frame.add_button("Stop",  stop);
frame.add_button("Reset", reset);

# Register event handlers
frame.set_draw_handler(draw)

timer = simplegui.create_timer(interval, tick)

# Start the frame animation
timer.start()
frame.start()   # should be last 
