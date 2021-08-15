using System;

public class Program {
	public static int FindClosestValueInBst(BST tree, int target) {
		return FindClosestValueInBstRec(tree, target, Int32.MaxValue-1);
	}
	
	public static int FindClosestValueInBstRec(BST tree, int target, int closest) {
		Console.WriteLine(closest);
		Console.WriteLine(tree.value);
		if(Math.Abs(tree.value-target)<Math.Abs(closest-target)){
			closest = tree.value;
		}
		if(tree.left == null && tree.right == null || closest == target){ return closest;}
		if(tree.left == null && tree.right != null){
			return FindClosestValueInBstRec(tree.right,target,closest);
		}
		if(tree.right == null && tree.left != null){
			return FindClosestValueInBstRec(tree.left,target,closest);
		}
		int leftChoice = Math.Abs(target - tree.left.value);
		int rightChoice = Math.Abs(target - tree.right.value);
		if(target < tree.value){
			tree = tree.left;
		}
		else{
			tree = tree.right;
		}
		Console.WriteLine(closest);
		return FindClosestValueInBstRec(tree,target,closest);
	}

	public class BST {
		public int value;
		public BST left;
		public BST right;

		public BST(int value) {
			this.value = value;
		}
	}
}
