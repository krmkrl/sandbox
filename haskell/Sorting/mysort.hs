import System.Random

quicksort :: Ord a => [a] -> [a]
quicksort [] = []
quicksort [x] = [x]
quicksort (x:xs) = quicksort (filter (<=x) xs) ++ [x] ++ quicksort (filter (>x) xs)


mergesort :: Ord a => [a] -> [a]
mergesort [] = []
mergesort [x] = [x]
mergesort xs = merge (mergesort xs') (mergesort ys') where
	(xs', ys') = splitAt (floor $ fromIntegral(length(xs)) / 2) xs

merge :: Ord a => [a] -> [a] -> [a]
merge [] ys = ys
merge xs [] = xs
merge xl@(x:xs) yl@(y:ys)
	| x < y = x : merge xs yl
	| otherwise =  y : merge xl ys

main :: IO ()
main = do
  g <- getStdGen
  let rlist = take 100 (randomRs (1, 100) g)::[Int] in 
    do print rlist
       putStr "qs: "
       print $ quicksort rlist
       putStr "ms: "
       print $ mergesort rlist
