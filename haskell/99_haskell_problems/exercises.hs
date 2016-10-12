import Data.List
import Control.Applicative
import Control.Monad
import System.Random

-- 1

myLast :: [a] -> a
myLast [] = error "empty"
myLast [x] = x
myLast (_:xs) =  myLast xs

myLast' :: [a] -> a
myLast' = head . reverse

myLast'' :: [a] -> a
myLast'' = foldr1 (\x y -> y)

myLast''' :: [a] -> a
myLast''' = foldr1 (const id)

myLast'''' :: [a] -> a
myLast'''' xs = xs !! (length xs - 1)

-- 2

myButLast :: [a] -> a
myButLast xs = xs !! (length xs - 2)

myButLast' :: [a] -> a
myButLast' [] = error "empty"
myButLast' (x:_:[]) = x
myButLast' (_:xs) = myButLast xs 

myButLast'' [x,_]  = x
myButLast'' (_:xs) = myButLast'' xs

-- 3 

elementAt :: [a] -> Int -> a
elementAt [] _ = error "empty list"
elementAt xs n = xs !! (n - 1)

elementAt' :: [a] -> Int -> a
elementAt' xs n = elemNumRec xs n 1

elemNumRec :: [a] -> Int -> Int -> a
elemNumRec [] _ _ = error "empty list"
elemNumRec (x:xs) n i = if i == n then x else elemNumRec xs n (i+1)

elementAt'' :: [a] -> Int -> a
elementAt'' [] _ = error "empty list"
elementAt'' (x:_) 1 = x
elementAt'' (_:xs) n
	| n < 1 = error "index error"
	| otherwise = elementAt'' xs (n-1)


-- 4

myLength :: [a] -> Int
myLength = foldl (\acc e -> acc + 1) 0

myLength' :: [a] -> Int
myLength' = foldr (\e acc -> acc + 1) 0

myLength'' :: [a] -> Int
myLength'' [] = 0
myLength'' (_:xs) = 1 + myLength'' xs

-- 5

myReverse :: [a] -> [a]
myReverse = foldl (\acc e -> e:acc) []

myReverse' :: [a] -> [a]
myReverse' = foldr (\e acc -> acc ++ [e]) []

myReverse'' :: [a] -> [a]
myReverse'' [] = []
myReverse'' (x:xs) = myReverse'' xs ++ [x]

myReverse''' :: [a] -> [a]
myReverse''' = foldl (flip (:)) []

-- 6

isPalindrome :: Eq a => [a] -> Bool
isPalindrome xs = xs == reverse xs

isPalindrome' :: Eq a => [a] -> Bool
isPalindrome' xs = xs == reverse xs

-- 7

data NestedList a = Elem a | List [NestedList a]

flatten :: NestedList a -> [a]
flatten (Elem x) = [x]
flatten (List ns) = foldr (\x y -> (flatten x) ++ y) [] ns


-- 8

compress :: Eq a => [a] -> [a]
compress [] = []
compress [x] = [x]
compress (x:y:ys) = if x == y then compress (y:ys) else x : compress (y:ys)

compress' :: Eq a => [a] -> [a]
compress' [] = []
compress' xs = foldr (\x acc@(y:ys) -> if x == y then acc else x:acc) [last xs] xs


-- 9

pack :: Eq a => [a] -> [[a]]
pack = group

pack' :: Eq a => [a] -> [[a]]
pack' [] = []
pack' l@(x:xs) = (takeWhile (== x) l) : (pack' $ (dropWhile (== x) l))

-- 10

encode :: (Eq a, Num n) => [a] -> [(n,a)]
encode = map (\xs -> (fromIntegral $ length xs, head xs)) . pack

-- 11

data Mult a = Multiple Int a | Single a deriving (Show)

encodeModified :: (Eq a) => [a] -> [Mult a]
encodeModified = map encodeMul . encode
	where encodeMul (1,a) = Single a
	      encodeMul (n,a) = Multiple n a

-- 12

decodeModified :: (Eq a) => [Mult a] -> [a]
decodeModified = concatMap decodeMul
	where decodeMul (Single a) = [a]
	      decodeMul (Multiple n a) = replicate n a

-- 13

encodeDirect :: (Eq a) => [a] -> [Mult a]
encodeDirect [] = []
encodeDirect (x:xs) = reverse $ encodeTail (Single x) xs []
	where encodeTail m [] ms = m:ms
	      encodeTail (Single x) (y:ys) ms = if x == y then encodeTail (Multiple 2 x) ys ms else encodeTail (Single y) ys ((Single x):ms)
	      encodeTail (Multiple n x) (y:ys) ms = if x == y then encodeTail (Multiple (n+1) x) ys ms else encodeTail (Single y) ys ((Multiple n x):ms)

-- 14


dupli :: [a] -> [a]
dupli = foldr (\x acc -> x:x:acc) []

dupli' :: [a] -> [a]
dupli' xs = xs >>= (\x -> [x,x])

dupli'' :: [a] -> [a]
dupli'' xs = do x <- xs
		[x,x]


-- 15

repli :: [a] -> Int -> [a]
repli xs n = concat $ foldr (\x acc -> (replicate n x):acc) [] xs

repli' :: [a] -> Int -> [a]
repli' xs n = concatMap (replicate n) xs

repli'' :: [a] -> Int -> [a]
repli'' xs n = xs >>= (\x -> replicate n x)

rep :: Int -> a -> [a]
rep 0 _ = []
rep n x = x : (rep (n-1) x)

repli''' :: [a] -> Int -> [a]
repli''' xs n = concat $ (\x -> rep n x) <$> xs

-- 16

dropEvery :: [a] -> Int -> [a]
dropEvery [] _ = []
dropEvery xs 0 = xs
dropEvery xs n = (take (n-1) xs) ++ (dropEvery (drop n xs) n)

dropEvery' :: [a] -> Int -> [a]
dropEvery' xs n = foldr (\(m, x) acc -> if mod m n == 0 then acc else x:acc) [] $ zip [1..] xs

-- 17

split :: [a] -> Int -> ([a],[a])
split xs n
	| length xs < n = (xs,[])
	| otherwise = spun xs n ([],[])
	              where spun xs 0 (ys,_) = (reverse ys,xs)
		            spun (x:xs) n (ys,zs) = spun xs (n-1) (x:ys,zs)


-- 18

slice :: [a] -> Int -> Int -> [a]
slice xs first last = take (last - first + 1) (drop (first - 1) xs)


slice' :: [a] -> Int -> Int -> [a]
slice' xs first last = let zl = zip [1..] xs in
		       map snd $ filter (\(n,e) -> n >= first && n <= last) zl


-- 19

rotate :: [a] -> Int -> [a]
rotate xs n
	| n < 0 = rotate xs $ (length xs) + n
	| otherwise = let chopHead = take n xs 
	                  rest = drop n xs in
	              rest ++ chopHead


-- 20

removeAt :: Int -> [a] -> (a,[a])
removeAt n xs = (xs !! (n - 1), rest xs)
	where rest xs = take (n - 1) xs ++ drop n xs

-- 21

insertAt :: a -> [a] -> Int -> [a]
insertAt e xs n
	| n <= 0 || n > length xs = xs
insertAt e xs 1 = (e:xs)
insertAt e (x:xs) n = x : (insertAt e xs (n-1))

insertAt' :: a -> [a] -> Int -> [a]
insertAt' e xs n = let (ys,zs) = Main.split xs (n-1) in ys ++ e:zs


-- 22

range :: Int -> Int -> [Int]
range start end = drop (start - 1) $ take end [1..]


range' :: Int -> Int -> [Int]
range' start end
	| start <= end = start : range' (start + 1) end
	| otherwise = []

-- 23

rnd_select :: [a] -> Int -> IO [a]
rnd_select xs n = do 
	indicesList <- randomIndices xs n
	return $ foldr (\elem acc -> (xs !! elem) : acc) [] indicesList
	where randomIndices xs n = do 
			gen <- newStdGen
			return $ take n $ randomRs (0, (length xs) - 1) gen

rnd_select' :: [a] -> Int -> IO [a]
rnd_select' xs n = replicateM n rands
	where rands = do randIndex <- randomRIO (0, length xs - 1) 
			 return (xs !! randIndex)

-- 24

diff_select :: Int -> Int -> IO [Int]
diff_select n range = do gen <- newStdGen
                         let randStream = randomRs (1,range) gen in return $ take n $ nub randStream

diff_select' :: Int -> Int -> IO [Int]
diff_select' n range = take n . nub . randomRs (1,range) <$> newStdGen


-- 25

rnd_permu :: [a] -> IO [a]
rnd_permu xs = do rs <- diff_select (length xs) (length xs)
                  return $ foldr (\r acc -> (xs !! (r - 1)) : acc) [] rs

rnd_permu' :: [a] -> IO [a]
rnd_permu' xs = do rs <- take (length xs) . nub . randomRs (0,length xs - 1) <$> newStdGen
                   return $ foldr (\r acc -> (xs !! r) : acc) [] rs


-- 26

combinations :: Int -> [a] -> [[a]]
combinations 0 _  = [[]]
combinations k xs = [ z:ys | z:zs <- tails xs, ys <- combinations (k-1) zs]

combinations' 0 _ = [[]]
combinations' k xs = do (z:zs) <- tails xs
                        ys <- combinations (k-1) zs
                        return (z:ys)

combinations'' k xs = filter ((k==).length) (subsequences xs)

