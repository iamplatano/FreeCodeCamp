import copy
import random
# Consider using the modules imported above.

class Hat():

  def __init__(self,**args):
    self.contents = []
    for color in args:
      while args[color] > 0:
        self.contents.append(color)
        args[color] -= 1 
    
   
  def draw(self,number_drawn):
    if len(self.contents) < number_drawn:
      return self.contents
    else:
      drawn = []
      for count in range(number_drawn):
        color = random.choice(self.contents)
        drawn.append(color)
        self.contents.remove(color)
      
      return drawn
      
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  temp = hat.contents.copy()
  tries = 0
  successes = 0
  drawn = []
  expected = []
  successes = 0
  for color in expected_balls:
      while expected_balls[color] > 0:
        expected.append(color)
        expected_balls[color] -= 1 
  expected_copy = expected.copy()
  print("\nExpected balls",expected)

  while tries < num_experiments:
    drawn = hat.draw(num_balls_drawn)
    for ball in drawn:
      if ball in expected_copy:
        expected_copy.remove(ball)
    if len(expected_copy) == 0:
      successes += 1
    
    expected_copy = expected.copy()
    hat.contents = temp.copy()
    tries += 1

  return successes/num_experiments
  