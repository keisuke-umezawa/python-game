# Implementation of classic arcade game Pong

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

init_pos  = [WIDTH / 2.0, HEIGHT / 2.0]
init_vel = [-3, -3]
time = 10
init_pad_pos = HEIGHT / 2.0
paddle1_pos = init_pad_pos
paddle2_pos = init_pad_pos
paddle1_vel = 0.0
paddle2_vel = 0.0
ball_pos = init_pos
ball_vel = init_vel
velocity = 1

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    sign = 0.0
    if direction == RIGHT:
        sign = 1.0
    else:
        sign = -1.0
        
    horizontal_vel = sign * random.randrange(12, 24) / time
    vertical_vel = -random.randrange(6, 18) / time
    
    ball_pos = init_pos
    ball_vel = [horizontal_vel, vertical_vel]
    
def tick():
    global ball_pos, ball_vel, paddle1_pos, paddle2_pos
    ball_pos = map(lambda x, y: x + y, ball_pos, ball_vel)

    paddle1_pos = paddle1_pos + paddle1_vel
    paddle2_pos = paddle2_pos + paddle2_vel

    if 0 > paddle1_pos:
        paddle1_pos = 0
    if paddle1_pos > HEIGHT:
        paddle1_pos = HEIGHT
    if 0 > paddle2_pos:
        paddle2_pos = 0
    if paddle2_pos > HEIGHT:
        paddle2_pos = HEIGHT
    
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    paddle1_pos = init_pad_pos
    paddle2_pos = init_pad_pos
    paddle1_vel = 0.0
    paddle2_vel = 0.0
    spawn_ball(LEFT)

def draw(canvas):
    global time, score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    if ball_pos[1] < 0 or HEIGHT < ball_pos[1]:
        ball_vel[1] = -ball_vel[1]
            
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")
    
    # update paddle's vertical position, keep paddle on the screen
    
    # draw paddles
    canvas.draw_line( \
        [0, paddle1_pos + PAD_HEIGHT / 2.0], \
        [0, paddle1_pos - PAD_HEIGHT / 2.0], \
        PAD_WIDTH, "Red")
                     
    canvas.draw_line( \
        [WIDTH, paddle2_pos + PAD_HEIGHT / 2.0], \
        [WIDTH, paddle2_pos - PAD_HEIGHT / 2.0], \
        PAD_WIDTH, "Red")
    
    # determine whether paddle and ball collide
    if ball_pos[0] < 0:
        if paddle1_pos - PAD_HEIGHT / 2.0 < ball_pos[1] \
            and ball_pos[1] < paddle1_pos + PAD_HEIGHT / 2.0:
                ball_vel[0] = -ball_vel[0]
        else:
            spawn_ball(RIGHT)
    if ball_pos[0] > WIDTH:
        if paddle2_pos - PAD_HEIGHT / 2.0 < ball_pos[1] \
            and ball_pos[1] < paddle2_pos + PAD_HEIGHT / 2.0:
                ball_vel[0] = -ball_vel[0]
        else:
            spawn_ball(LEFT)
    
    # draw scores
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['down']:
        paddle2_vel = paddle2_vel + velocity
    elif key == simplegui.KEY_MAP['up']:
        paddle2_vel = paddle2_vel - velocity
    if key == simplegui.KEY_MAP['s']:
        paddle1_vel = paddle1_vel + velocity
    elif key == simplegui.KEY_MAP['w']:
        paddle1_vel = paddle1_vel - velocity
   
def keyup(key):
    global paddle1_vel, paddle2_vel


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

# create timer
timer = simplegui.create_timer(time, tick)


# start frame
new_game()
frame.start()
timer.start()
