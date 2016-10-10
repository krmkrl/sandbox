module Bowling_Test where

import Bowling
import Test.HUnit

roll_list :: [Frame] -> [Int] -> [Frame]
roll_list frames = foldl roll frames

--roll tests
test_roll_first = TestCase $ assertEqual "roll a 1, first roll" [(1, -1, -1)] (roll [] 1)
test_roll_two = TestCase $ assertEqual "roll a 1, then a 2" [(1, 2, -1)] (roll_list [] [1,2])
test_roll_strike = TestCase $ assertEqual "roll a strike, then a 2" [(10, -1, -1), (2, -1, -1)] (roll_list [] [10,2])
test_roll_all_zeroes = TestCase $ assertEqual "roll 20 zeroes" (replicate 10 (0,0,-1)) (roll_list [] $ replicate 20 0)
test_roll_all_ones = TestCase $ assertEqual "roll 20 ones" (replicate 10 (1,1,-1)) (roll_list [] $ replicate 20 1)
test_roll_all_strike = TestCase $ assertEqual "roll 12 tens" ((replicate 9 (10,-1,-1)) ++ [(10,10,10)]) (roll_list [] $ replicate 12 10)

--TODO bonus roll tests (see python solution)

--score tests
test_score_no_rolls = TestCase $ assertEqual "score should be 0 after no rolls" 0 (score [])
test_score_one_roll = TestCase $ assertEqual "score should be 2 after one roll of 2" 2 (score $ roll [] 2)
test_score_all_zeroes = TestCase $ assertEqual "score should be 0 after 20 zero rolls" 0 (score $ roll_list [] $ replicate 20 0)
test_score_all_ones = TestCase $ assertEqual "score should be 20 after 20 one rolls" 20 (score $ roll_list [] $ replicate 20 1)
test_score_all_spare = TestCase $ assertEqual "score should be 150 after 21 five rolls" 150 (score $ roll_list [] $ replicate 21 5)
test_score_all_strike = TestCase $ assertEqual "score should be 300 after 12 ten rolls" 300 (score $ roll_list [] $ replicate 12 10)
test_score_custom = TestCase $ assertEqual "score should be 133 after custom series" 133 (score $ roll_list [] [1,4,4,5,6,4,5,5,10,0,1,7,3,6,4,10,2,8,6])

rollTests = TestList [test_roll_first, test_roll_two, test_roll_strike, test_roll_all_zeroes, test_roll_all_ones, test_roll_all_strike]
scoreTests = TestList [test_score_no_rolls, test_score_one_roll, test_score_all_zeroes, test_score_all_ones, test_score_all_spare, test_score_all_strike, test_score_custom]

main = runTestTT $ TestList [rollTests, scoreTests]
