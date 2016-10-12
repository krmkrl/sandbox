module TreeTest (main) where
import BTree
import qualified Data.Foldable as F

main :: IO ()
main = do
	let list = [7,2,9,3,0,4,5,1,2]
	print $ "input list: " ++ show(list)
	let tree = foldr treeInsert EmptyTree list
	print tree
	print $ "sorted list: " ++ show(inorder tree)
	print $ ".. and with foldMap: " ++ show(inorder' tree)
	print $ treeDelete 2 tree
	print $ fmap (*2) tree
	print $ "foldr with (+) (sum of elems in tree)"
	print $ F.foldr (+) 0 tree
	print $ F.foldr (-) 0 tree
	print $ F.foldl (-) 0 tree
	print tree
