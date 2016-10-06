module Bowling_Test where

import Bowling
import Test.HUnit

test_add1 = TestCase $ assertEqual "add1 on 1 should be 2" 2 (add1 1)


addTests = TestList [test_add1]

main = runTestTT $ TestList [addTests]
