module BTree (Tree(..), singleton, treeInsert, treeElem, treeElem', inorder, inorder', treeDelete) where

import qualified Data.Foldable as F
import Data.Monoid

data Tree a = EmptyTree | Node a (Tree a) (Tree a) deriving (Show, Read, Eq)

instance Functor Tree where
	fmap = treeMap

instance F.Foldable Tree where
	foldMap f EmptyTree = mempty
	foldMap f (Node a left right) = F.foldMap f left `mappend`
					f a 	         `mappend`
					F.foldMap f right

treeMap :: (a -> b) -> Tree a -> Tree b
treeMap f EmptyTree = EmptyTree
treeMap f (Node a left right) = Node (f a) (treeMap f left) (treeMap f right)

singleton :: a -> Tree a
singleton x = Node x EmptyTree EmptyTree

treeInsert :: (Ord a) => a -> Tree a -> Tree a
treeInsert x EmptyTree = singleton x
treeInsert x (Node a left right)
	| x == a = Node x left right
	| x < a = Node a (treeInsert x left) right
	| x > a = Node a left (treeInsert x right)

treeElem :: (Ord a) => a -> Tree a -> Bool
treeElem x EmptyTree = False
treeElem x (Node a left right)
	| x == a = True
	| x < a = treeElem x left
	| x > a = treeElem x right

treeElem' :: (Eq a, F.Foldable t) => a -> t a -> Bool
treeElem' e t = getAny $ F.foldMap (\x -> Any $ x == e) t

inorder :: Tree a -> [a]
inorder EmptyTree = []
inorder (Node x EmptyTree EmptyTree) = [x]
inorder (Node x left right) = (inorder left) ++ [x] ++ (inorder right)

inorder' :: Tree a -> [a]
inorder' = F.foldMap (\a -> [a])

treeDelete :: (Ord a) => a -> Tree a -> Tree a
treeDelete x EmptyTree = EmptyTree
treeDelete x (Node a left right)
	| x == a = deleteNode left right
	| x < a = Node a (treeDelete x left) right
	| x > a = Node a left (treeDelete x right)

deleteNode :: (Ord a) => Tree a -> Tree a -> Tree a
deleteNode EmptyTree EmptyTree = EmptyTree
deleteNode left EmptyTree = left
deleteNode EmptyTree right = right
deleteNode left right = (Node (getSucc left)) (treeDelete (getSucc left) left) right

getSucc :: Tree a -> a
getSucc (Node a left EmptyTree) = a
getSucc (Node a left right) = getSucc right
