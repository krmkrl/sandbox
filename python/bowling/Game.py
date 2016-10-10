import unittest
import itertools

"""
Requires python 2.7.9
"""

class GameEndError:
  pass

class Game:
  """
  A game of bowling
  """

  NumFrames = 10
  FrameMaxPoints = 10

  def __init__(self):
    self.frames = [] #one frame consist of num rolls, e.g [(1,4)]
    self.lastRoll = None

  def roll(self, pins):
    """
    called each time the player rolls a ball
    pins are the number of pins knocked down
    """
    if self.lastRoll is not None:
      raise GameEndError
    if not self.frames:
      self.frames.append((pins, None))
    else:
      (roll1, roll2) = self.frames[-1]
      if len(self.frames) == Game.NumFrames: #last frame
        if roll2 is None:
          self.frames[-1] = (roll1, pins)
        elif roll1 + roll2 >= Game.FrameMaxPoints: #spare or strike
          self.lastRoll = pins
        else: #trying to do bonus roll without spare or strike
          raise GameEndError
      else: #not last frame
        if roll1 == Game.FrameMaxPoints or roll2 is not None: #add new frame if strike or frame full
          self.frames.append((pins, None))
        else:
          self.frames[-1] = (roll1, pins)

  def score(self):
    """
    called at the very end of the game
    returns the total score for that game
    """
    scores = [] #score for each frame
    scores.append(0)
    for i in range(0, len(self.frames)):
      (roll1, roll2) = self.frames[i]
      if i > 0:
        scores.append(0)
        scores[i] += scores[i - 1]
      scores[i] += roll1  
      if roll2 is not None:
        scores[i] += roll2
      #check for spare
      if roll2 is not None and roll1 + roll2 == Game.FrameMaxPoints:
        if i == len(self.frames) - 1: #last frame
          scores[i] += self.lastRoll
        elif i + 1 < len(self.frames):
          (nextRoll, nextNextRoll) = self.frames[i + 1]
          scores[i] += nextRoll
      #check for strike
      if roll1 == Game.FrameMaxPoints:
        if i == len(self.frames) - 1: #last frame
          if roll2 == Game.FrameMaxPoints:
            scores[i] += self.lastRoll
        elif i + 1 < len(self.frames):
          (nextRoll, nextNextRoll) = self.frames[i + 1]
          scores[i] += nextRoll
          if nextNextRoll is not None:
            scores[i] += nextNextRoll
          else: #nextRoll could have been a strike
            if i + 2 < len(self.frames):
              (thirdNextRoll, fourthNextRoll) = self.frames[i + 2]
              scores[i] += thirdNextRoll
    return scores[-1]

class GameTest(unittest.TestCase):
  """
  Test a game of bowling
  """

  def setUp(self):
    self.game = Game()

  def roll_list(self, rolls):
    for r in rolls:
      self.game.roll(r)

  def testMinScore(self): #0
    rolls = list(itertools.repeat(0, Game.NumFrames * 2))
    self.roll_list(rolls)
    score = self.game.score()
    self.assertEquals(score, 0)

  def testAllOnes(self): #20
    rolls = list(itertools.repeat(1, Game.NumFrames * 2))
    self.roll_list(rolls)
    score = self.game.score()
    self.assertEquals(score, 20)

  def testSpare(self):
    rolls = [5,5,7,1]
    self.roll_list(rolls)
    score = self.game.score()
    self.assertEquals(score, 25)

  def testAllSpare(self):
    rolls = list(itertools.repeat(5,Game.NumFrames * 2 + 1)) #21 rolls
    self.roll_list(rolls)
    score = self.game.score()
    self.assertEquals(score, 150) 
    
  def testStrike(self):
    rolls = [10,5,2]
    self.roll_list(rolls)
    score = self.game.score()
    self.assertEquals(score, 24)
  
  def testContinousStrikes(self):
    rolls = [10,10,2,4]
    self.roll_list(rolls)
    score = self.game.score()
    self.assertEquals(score, 44)
  
  def testIncompleteFrame(self):
    rolls = [10,5,2,4]
    self.roll_list(rolls)
    score = self.game.score()
    self.assertEquals(score, 28)

  def testBonusRollStrike(self):
    rolls = list(itertools.repeat(1,18))
    rolls += [10,0,5]
    self.roll_list(rolls)
    score = self.game.score()
    self.assertEquals(score, 18 + 15)
  
  def testBonusRollSpare(self):
    rolls = list(itertools.repeat(1,18))
    rolls += [4,6,1]
    self.roll_list(rolls)
    score = self.game.score()
    self.assertEquals(score, 18 + 11)
  
  def testTooManyRolls(self):
    with self.assertRaises(GameEndError):
      rolls = list(itertools.repeat(5, Game.NumFrames * 2 + 2)) #22 rolls
      self.roll_list(rolls)
  
  def testLastRollNotAllowed(self):
    rolls = list(itertools.repeat(4, Game.NumFrames * 2))
    self.roll_list(rolls)
    with self.assertRaises(GameEndError):
      self.game.roll(2)
    
  def testMaxScore(self): #300
    rolls = list(itertools.repeat(10, 12)) #12 rolls if all strikes
    self.roll_list(rolls)
    score = self.game.score()
    self.assertEquals(score, 300)

  def testCustomScore(self):
    self.roll_list([1,4,4,5,6,4,5,5,10,0,1,7,3,6,4,10,2,8,6])
    score = self.game.score()
    self.assertEquals(score, 133)

  def testNoScore(self):
    score = self.game.score()
    self.assertEquals(score, 0)

if __name__ == '__main__':
  unittest.main()
