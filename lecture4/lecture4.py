
# template for "Stopwatch: The Game"
import simplegui

# define global variables
hundredms = 0
position = [50, 50]
width = 500
height = 500
interval = 100
is_started = False
ok = 0
hit = 0

def tick():
    global hundredms
    if is_started:
        hundredms += 1
    print hundredms

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    m = int(t / 600)
    residual = t % 600
    ss = int(residual / 100)
    s = int((residual - ss * 100) / 10)
    d = residual % 10
    return str(m) + ":" + str(ss) + str(s) + "." + str(d)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global is_started
    is_started = True
    
def stop():
    global is_started
    global hit
    global ok
    global hundredms
    is_started = False
    hit += 1
    if hundredms % 10 == 0:
        ok += 1
    
def reset():
    global hundredms
    global hit
    global ok
    stop()
    hundredms = 0
    hit = 0
    ok = 0
    

# define event handler for timer with 0.1 sec interval
def draw(canvas):
    global hundredms
    global ok
    global hit
    canvas.draw_text(format(hundredms), position, 36, "White")
    canvas.draw_text(str(ok) + "." + str(hit), [10, 10], 10, "White")
    
# define draw handler
frame = simplegui.create_frame("Timer Game", width, height)
    
# create frame

# register event handlers
frame.set_draw_handler(draw)
frame.add_button("Start", start)
frame.add_button("Stop", stop)
frame.add_button("Reset", reset)
timer = simplegui.create_timer(interval, tick)

# start frame
frame.start()
timer.start()

# Please remember to review the grading rubric
