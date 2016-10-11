module Bowling_Test where

import Bowling
import Control.Monad
import Data.Either
import Test.HUnit

rollList :: [Frame] -> [Int] -> [Frame]
rollList frames = toFrames . foldM roll frames

toFrames :: Either String [Frame] -> [Frame]
toFrames = either (\_ -> [(-1,-1,-1)]) id

--roll tests
roll_first = TestCase $ assertEqual "roll a 1, first roll" [(1, -1, -1)] $ rollList [] [1]
roll_two = TestCase $ assertEqual "roll a 1, then a 2" [(1, 2, -1)] $ rollList [] [1,2]
roll_strike = TestCase $ assertEqual "roll a strike, then a 2" [(10, -1, -1),(2, -1, -1)] $ rollList [] [10,2]
roll_all_zeroes = TestCase $ assertEqual "roll 20 zeroes" (replicate 10 (0,0,-1)) $ rollList [] $ replicate 20 0
roll_all_ones = TestCase $ assertEqual "roll 20 ones" (replicate 10 (1,1,-1)) $ rollList [] $ replicate 20 1
roll_all_strike = TestCase $ assertEqual "roll 12 tens" ((replicate 9 (10,-1,-1)) ++ [(10,10,10)]) $ rollList [] $ replicate 12 10
roll_bonus_strike = TestCase $ assertEqual "bonus roll after strike" ((replicate 9 (10,-1,-1)) ++ [(10,3,2)]) $ rollList [] $ (replicate 9 10) ++ [10,3,2]
roll_bonus_spare = TestCase $ assertEqual "bonus roll after spare" ((replicate 9 (10,-1,-1)) ++ [(9,1,2)]) $ rollList [] $ (replicate 9 10) ++ [9,1,2]
roll_no_bonus = TestCase $ assertEqual "last roll no bonus" (Left "game done") $ foldM roll [] $ replicate 21 1

--score tests
score_no_rolls = TestCase $ assertEqual "score should be 0 after no rolls" 0 $ score []
score_one_roll = TestCase $ assertEqual "score should be 2 after one roll of 2" 2 $ score $ rollList [] [2]
score_all_zeroes = TestCase $ assertEqual "score should be 0 after 20 zero rolls" 0 $ score $ rollList [] $ replicate 20 0
score_all_ones = TestCase $ assertEqual "score should be 20 after 20 one rolls" 20 $ score $ rollList [] $ replicate 20 1
score_all_spare = TestCase $ assertEqual "score should be 150 after 21 five rolls" 150 $ score $ rollList [] $ replicate 21 5
score_all_strike = TestCase $ assertEqual "score should be 300 after 12 ten rolls" 300 $ score $ rollList [] $ replicate 12 10
score_custom = TestCase $ assertEqual "score should be 133 after custom series" 133 $ score $ rollList [] [1,4,4,5,6,4,5,5,10,0,1,7,3,6,4,10,2,8,6]

rollTests = TestList [roll_first, roll_two, roll_strike, roll_all_zeroes, roll_all_ones, roll_all_strike, roll_bonus_strike, roll_bonus_spare, roll_no_bonus]
scoreTests = TestList [score_no_rolls, score_one_roll, score_all_zeroes, score_all_ones, score_all_spare, score_all_strike, score_custom]

main = runTestTT $ TestList [rollTests, scoreTests]
