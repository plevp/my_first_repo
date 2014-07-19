 
# http://www.codeskulptor.org/#user30_wREBjkVf7h_12.py
# Implementation of classic arcade game Pong
# import simpleguitk as simplegui

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_pos = [0.0,0.0];
ball_vel  = [0.0,0.0]

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball():
    global ball_pos, ball_vel # these are vectors stored as lists

    ball_pos[0] = WIDTH/2; ball_pos[1] = HEIGHT/2;
    # ball_vel[0] = -2;   ball_vel[1] = 1;
    ball_vel[0] = random.randrange(60,181)/ 60.0 * random.randrange(-1,2,2);
    ball_vel[1] = random.randrange(60,121)/60.0 * random.randrange(-1,2,2);
    
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints

    paddle1_pos = HEIGHT/2; paddle2_pos = HEIGHT/2
    paddle1_vel = 0; paddle2_vel = 0
    
    spawn_ball()

def draw_paddle(canvas, x1, x2, y):
    y1 = y - HALF_PAD_HEIGHT; y2 = y + HALF_PAD_HEIGHT;
    canvas.draw_polygon([(x1, y1), (x1, y2), (x2, y2), (x2, y1)], 1, "Red", "Orange")

def calc_paddle_y(y):
    r = y
    if y < HALF_PAD_HEIGHT:
        r = HALF_PAD_HEIGHT
    elif (y > (HEIGHT - HALF_PAD_HEIGHT)):
        r = HEIGHT - HALF_PAD_HEIGHT
    return r;
    
def draw_paddles(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel

    p1_x1 = 0; p1_x2 = PAD_WIDTH-1; 
    p2_x1 = WIDTH - PAD_WIDTH; p2_x2 = WIDTH;
   
    draw_paddle(canvas, p1_x1, p1_x2, paddle1_pos)
    draw_paddle(canvas, p2_x1, p2_x2, paddle2_pos)

count = 1;
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    global count;
    
    if count % 5 == 0:
        count +=1;
        print "New Game";
        new_game()
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")

    # update ball
    ball_pos[0] = ball_pos[0] + ball_vel[0]
    ball_pos[1] = ball_pos[1] + ball_vel[1]
    
    if ball_pos[0] + BALL_RADIUS >= WIDTH-PAD_WIDTH:
        ball_vel[0] = - ball_vel[0]
        print "RIGHT", ball_pos[1], paddle2_pos
        count += 1;
        if abs(ball_pos[1] - paddle2_pos) > (HALF_PAD_HEIGHT + 8):
            print "RIGHT", "miss"
    elif ball_pos[0] -BALL_RADIUS <= PAD_WIDTH:
        ball_vel[0] = - ball_vel[0]
        print "LEFT", ball_pos[1], paddle1_pos
        count += 1
        if abs(ball_pos[1] - paddle1_pos) > (HALF_PAD_HEIGHT +8):
            print "LEFT", "miss"
            
    if ball_pos[1] + BALL_RADIUS >= HEIGHT:
        ball_vel[1] = - ball_vel[1]
    elif ball_pos[1] - BALL_RADIUS <= 0:
         ball_vel[1] = - ball_vel[1]
    
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Yellow")
    
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos	 = calc_paddle_y(paddle1_pos - paddle1_vel)
    paddle2_pos	 = calc_paddle_y(paddle2_pos - paddle2_vel)
    
    # draw paddles
    draw_paddles(canvas);
    
    # draw scores
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    
    if chr(key) == "q" or chr(key) == "Q":
        paddle1_vel = 1
        
    if chr(key) == "a" or chr(key) == "A":
        paddle1_vel = -1
        
    if chr(key) == "o" or chr(key) == "O":
        paddle2_vel = 1
        
    if chr(key) == "l" or chr(key) == "L":
        paddle2_vel = -1	
   
def keyup(key):
    global paddle1_vel, paddle2_vel

    if chr(key) == "q" or chr(key) == "Q":
        paddle1_vel = 0
        
    if chr(key) == "a" or chr(key) == "A":
        paddle1_vel = 0
        
    if chr(key) == "o" or chr(key) == "O":
        paddle2_vel = 0
        
    if chr(key) == "l" or chr(key) == "L":
        paddle2_vel =  0	
        

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)


# start frame
new_game()
frame.start()

 