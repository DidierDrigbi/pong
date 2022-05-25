from psychopy import visual, core
from psychopy.hardware import keyboard
from psychopy.constants import *

win = visual.Window(size=[800,600], color='black', units = 'pix')
line = visual.Line(win, start=[0,-300], end=[0,300], lineWidth=5, fillColor='white')
ball = visual.Rect(win, size=[20,20], fillColor='red')
left_paddle = visual.Rect(win, size=[20, 60], fillColor='white', pos=[-375, 0])
right_paddle = visual.Rect(win, size=[20, 60], fillColor='white', pos=[375, 0])
score1 = 0
score2 = 0
left_score = visual.TextStim(win, text=score1, color='white', height=60, pos=[-200, 250])
right_score = visual.TextStim(win, text=score2, color='white', height=60, pos=[200, 250])

introduction = visual.ImageStim(win, image='introduction.png')

kb = keyboard.Keyboard()

### Before the game begins

introduction.draw()
win.flip()
kb.waitKeys(keyList=['space'])

### The game begins

continueRoutine = True
while continueRoutine:
    
###Drawing the board
    if line.status == NOT_STARTED:
        line.setAutoDraw(True)
        left_score.setAutoDraw(True)
        right_score.setAutoDraw(True)
        ball.setAutoDraw(True)
        left_paddle.setAutoDraw(True)
        right_paddle.setAutoDraw(True)

###Start the game
        update = [-2, -2]
        
###Different angles based on postion of the ball
        
    if ball.overlaps(left_paddle):
        if left_paddle.pos[0] - ball.pos[0] >= -10 or left_paddle.pos[1] - ball.pos[1] <= 10:
            update = [2, 0]
            
        if left_paddle.pos[0] - ball.pos[0] >= -25:
            update = [2, 2.5]
            
        if left_paddle.pos[0] - ball.pos[0] <= 25:
            update = [2, -2.5]
            
        if left_paddle.pos[0] - ball.pos[0] >= -30:
            update = [2, 3.5]
            
        if left_paddle.pos[1] - ball.pos[1] >= 30:
            update = [2, -3.5]
            
    if ball.overlaps(right_paddle):
        if right_paddle.pos[0] - ball.pos[0] >= -10 or right_paddle.pos[1] - ball.pos[1] <= 10:
            update = [-2, 0]
            
        if right_paddle.pos[0] - ball.pos[0] >= -25:
            update = [-2, 2.5]
            
        if right_paddle.pos[0] - ball.pos[0] <= 25:
            update = [-2, -2.5]
            
        if right_paddle.pos[0] - ball.pos[0] >= -30:
            update = [-2, 3.5]
            
        if right_paddle.pos[1] - ball.pos[1] >= 30:
            update = [-2, -3.5]
            
###Bounces of the sides and score changes
              
    if ball.pos[1] >= 290:
        update = [update[0], -(update[1])]
        
    elif ball.pos[1] <= -290:
        update = [update[0], -(update[1])]
            
    if ball.pos[0] <= -390:
        update = [-(update[0]), update[1]]
        score2 = score2 + 1

    elif ball.pos[0] >= 390:
        update = [-(update[0]), update[1]]
        score1 = score1 + 1
        
    ball.pos += update
    
###Moving the paddles
            
    if left_paddle.status == STARTED:
        kb.status = STARTED
        
        update_left = [0, 0]
        
        if kb.status == STARTED:
            kb.clock.reset()
            keys = kb.getKeys(keyList=['w', 's'], waitRelease = False, clear = False)
            
            for i in keys:
                if i == 'w':
                    if left_paddle.pos[1] <= 270:
                        update_left = [update_left[0], 2]
                if i == 's':
                    if left_paddle.pos[1] >= -270:
                        update_left = [update_left[0], -2]                        
            left_paddle.pos += update_left
            
    if right_paddle.status == STARTED:
        kb.status = STARTED
        
        update_right = [0, 0]
        
        if kb.status == STARTED:
            kb.clock.reset()
            keys = kb.getKeys(keyList=['up', 'down'], waitRelease = False, clear = False)
            
            for i in keys:
                if i == 'up':
                    if right_paddle.pos[1] <= 270:
                        update_right = [update_left[0], 2]
                if i == 'down':
                    if right_paddle.pos[1] >= -270:
                        update_right = [update_left[0], -2]
            right_paddle.pos += update_right    
    
    win.flip()
    
###Showing the score
    
    left_score.text = score1
    right_score.text = score2
    
    win.flip()
    
###Exit the game using escape
    
    if 'escape' in kb.getKeys(keyList=['escape'], clear=False):
        continueRoutine = False
        

        

