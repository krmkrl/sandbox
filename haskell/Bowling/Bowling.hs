module Bowling(roll, score, Frame) where

type Frame = (Int, Int, Int) --second field is -1 on strike, third field present in last frame (if spare or strike)

roll :: [Frame] -> Int -> [Frame]
roll [] n = [(n, -1, -1)]
roll frames n = reverse $ rollReversed (reverse frames)
        where rollReversed rframes
                | length rframes == 10 = let (x,y,z) = head rframes in if y == -1 then (x,n,-1):(tail rframes) else if x + y >= 10 then (x,y,n):(tail rframes) else rframes
                | ((10,-1,-1):fs) <- rframes = (n,-1,-1):rframes
                | ((x,-1,-1):fs) <- rframes = (x,n,-1):fs
                | ((x,y,-1):fs) <- rframes = (n,-1,-1):rframes

score :: [Frame] -> Int
score [] = 0
score [(x,-1,-1)] = x
score [(x,y,-1)] = x + y
score [(x,y,z)] = x + y + z
score ((10,-1,-1):(10,-1,-1):rest@((x3,y3,z3):xs)) = 10 + 10 + x3 + (score $ (10,-1,-1):rest)
score ((10,-1,-1):rest@((x2,y2,z2):xs)) = 10 + x2 + y2 + (score rest)
score ((x,y,-1):rest@((x2,y2,z2):xs)) = if x + y == 10 then 10 + x2 + (score rest) else x + y + (score rest)

