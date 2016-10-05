import unittest

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
    if not self.frames:
      self.frames.append((pins, None))
    else:
      if self.lastRoll is not None:
        raise GameEndError
      (roll1, roll2) = self.frames[-1]
      if len(self.frames) == Game.NumFrames: #last frame, check strike or spare
        if roll2 is None:
          self.frames[-1] = (roll1, pins)
        elif roll2 is not None and roll2 > 0 and roll1 + roll2 == Game.FrameMaxPoints:
          self.lastRoll = pins
        elif roll2 is not None and roll2 == Game.FrameMaxPoints:
          self.lastRoll = pins
        else:
          raise GameEndError
      else: #not last frame
        if roll1 == Game.FrameMaxPoints: #strike
          self.frames.append((pins, None))
        elif roll2 is None:
          self.frames[-1] = (roll1, pins)
        else:
          self.frames.append((pins, None))

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
      if roll1 is not None:
        scores[i] += roll1  
      if roll2 is not None:
        scores[i] += roll2
      #check for spare
      if roll1 is not None and roll2 is not None and roll1 + roll2 == Game.FrameMaxPoints:
        if i == len(self.frames) - 1: #last frame
          scores[i] += self.lastRoll
        elif i + 1 < len(self.frames):
          (nextRoll, nextNextRoll) = self.frames[i + 1]
          if nextRoll is not None:
            scores[i] += nextRoll
      #check for strike
      if roll1 is not None and roll1 == Game.FrameMaxPoints:
        if i == len(self.frames) - 1: #last frame
          if roll2 == Game.FrameMaxPoints:
            scores[i] += self.lastRoll
        if i + 1 < len(self.frames):
          (nextRoll, nextNextRoll) = self.frames[i + 1]
          if nextRoll is not None:
            scores[i] += nextRoll
          if nextNextRoll is not None:
            scores[i] += nextNextRoll
          else: #nextRoll could have been a strike
            if i + 2 < len(self.frames):
              (thirdNextRoll, fourthNextRoll) = self.frames[i + 2]
              if thirdNextRoll is not None:
                scores[i] += thirdNextRoll


    return scores[-1]

class GameTest(unittest.TestCase):
  """
  Test a game of bowling
  """

  def setUp(self):
    self.game = Game()
    pass

  def rollSameMany(self, numRolls, pins):
    for i in range(0, numRolls):
      self.game.roll(pins)

  def testMinScore(self): #0
    self.rollSameMany(Game.NumFrames * 2, 0)
    score = self.game.score()
    self.assertEquals(score, 0)

  def testAllOnes(self): #20
    self.rollSameMany(Game.NumFrames * 2, 1)
    score = self.game.score()
    self.assertEquals(score, 20)

  def testSpare(self):
    self.game.roll(5)
    self.game.roll(5) #spare
    self.game.roll(7)
    self.game.roll(1)
    score = self.game.score()
    self.assertEquals(score, 25)

  def testAllSpare(self):
    self.rollSameMany(Game.NumFrames * 2 + 1, 5) #21 rolls
    score = self.game.score()
    self.assertEquals(score, 150) 
    
  def testStrike(self):
    self.game.roll(10)
    self.game.roll(5)
    self.game.roll(2)
    score = self.game.score()
    self.assertEquals(score, 24)
  
  def testContinousStrikes(self):
    self.game.roll(10)
    self.game.roll(10)
    self.game.roll(2)
    self.game.roll(4)
    score = self.game.score()
    self.assertEquals(score, 44)
  
  def testTooManyRolls(self):
    with self.assertRaises(GameEndError):
      self.rollSameMany(Game.NumFrames * 2 + 2, 5) #22 rolls
  
  def testLastRollNotAllowed(self):
    self.rollSameMany(Game.NumFrames * 2, 4)
    with self.assertRaises(GameEndError):
      self.game.roll(2)
    
  def testMaxScore(self): #300
    self.rollSameMany(12, 10) #12 rolls if all strikes
    score = self.game.score()
    self.assertEquals(score, 300)

  def testCustomScore(self):
    self.game.roll(1)
    self.game.roll(4)
    self.game.roll(4)
    self.game.roll(5)
    self.game.roll(6)
    self.game.roll(4)
    self.game.roll(5)
    self.game.roll(5)
    self.game.roll(10)
    self.game.roll(0)
    self.game.roll(1)
    self.game.roll(7)
    self.game.roll(3)
    self.game.roll(6)
    self.game.roll(4)
    self.game.roll(10)
    self.game.roll(2)
    self.game.roll(8)
    self.game.roll(6)
    score = self.game.score()
    self.assertEquals(score, 133)

  def testNoScore(self):
    score = self.game.score()
    self.assertEquals(score, 0)

if __name__ == '__main__':
  unittest.main()
