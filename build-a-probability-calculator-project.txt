** start of main.py **

import copy
import random

class Hat:
    def __init__(self,**kwargs):
        self.contents = [] #create empty list to append strings later

        for colour,qty in kwargs.items(): #unpack *args
            for i in range(qty): #each colour represents a single ball of that colour
                self.contents.append(colour)
    
    def draw(self,n): #n indicates number of balls to draw
        #if number of balls to draw exceeds available quantity, return all balls
        if n>len(self.contents): 
            #clear contents
            allBalls = self.contents
            self.contents = []
            return allBalls
        
        #loop that draws balls one at a time without replacement
        removedBalls = [] #empty list of balls that will be removed
        for i in range(n):
            toAdd = self.contents.pop(random.randint(0,len(self.contents)-1)) #chooses a random integer inclusive
            #pop removes the ball
            removedBalls.append(toAdd)
        return removedBalls

def experiment(hat, expected_balls:dict, num_balls_drawn, num_experiments):
    #expected_balls : dictionary
    N = num_experiments
    M = 0
    for i in range(N):
        add = True
        copyHat = copy.deepcopy(hat) #create independent copy
        balls = copyHat.draw(num_balls_drawn)

        #convert drawn balls to dictionary
        nBalls = {} 
        for color in balls:
            if color in nBalls:
                nBalls[color] += 1
            else:
                nBalls[color] = 1
        
        for colour,qty in expected_balls.items(): #get expected colours and quantities
            try: 
                if qty > nBalls[colour]: #check if the quota has not been met
                    add = False
            except: #event that no balls of that colour are drawn
                add = False
        if add: #positive experiment
            M+=1

    return M/N




hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={'red':2,'green':1},
                  num_balls_drawn=5,
                  num_experiments=2000)


** end of main.py **

