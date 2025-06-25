"""
2115. Find All Possible Recipes from Given Supplies

You have information about n different recipes. You are given a string array recipes and a 2D string array ingredients. The ith recipe has the name recipes[i], and you can create it if you have all the needed ingredients from ingredients[i]. A recipe can also be an ingredient for other recipes, i.e., ingredients[i] may contain a string that is in recipes.

You are also given a string array supplies containing all the ingredients that you initially have, and you have an infinite supply of all of them.

Return a list of all the recipes that you can create. You may return the answer in any order.

Note that two recipes may contain each other in their ingredients.

Example 1:
Input: recipes = ["bread"], ingredients = [["yeast","flour"]], supplies = ["yeast","flour","corn"]
Output: ["bread"]
Explanation:
We can create "bread" since we have the ingredients "yeast" and "flour".

Example 2:
Input: recipes = ["bread","sandwich"], ingredients = [["yeast","flour"],["bread","meat"]], supplies = ["yeast","flour","meat"]
Output: ["bread","sandwich"]
Explanation:
We can create "bread" since we have the ingredients "yeast" and "flour".
We can create "sandwich" since we have the ingredient "meat" and can create the ingredient "bread".

Example 3:
Input: recipes = ["bread","sandwich","burger"], ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]], supplies = ["yeast","flour","meat"]
Output: ["bread","sandwich","burger"]
Explanation:
We can create "bread" since we have the ingredients "yeast" and "flour".
We can create "sandwich" since we have the ingredient "meat" and can create the ingredient "bread".
We can create "burger" since we have the ingredient "meat" and can create the ingredients "bread" and "sandwich".

Constraints:
n == recipes.length == ingredients.length
1 <= n <= 100
1 <= ingredients[i].length, supplies.length <= 100
1 <= recipes[i].length, ingredients[i][j].length, supplies[k].length <= 10
recipes[i], ingredients[i][j], and supplies[k] consist only of lowercase English letters.
All the values of recipes and supplies combined are unique.
Each ingredients[i] does not contain any duplicate values.
"""
from typing import List
from collections import defaultdict

class Solution:
	def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
		
		supplies_dict = defaultdict(int)
		for supply in supplies:
			supplies_dict[supply] = 1
		recipes_dict = defaultdict(list)
		for i in range(len(recipes)):
			recipes_dict[recipes[i]] = ingredients[i]

		memo = {}
		visiting = set()
		result = []

		def can_be_cooked(recipe) -> bool:
			if recipe in memo:
				return memo[recipe]
			if recipe in visiting:
				memo[recipe] = False
				return False
			
			visiting.add(recipe)
			for ingredient in recipes_dict[recipe]:
				if ingredient in recipes_dict:
					if not can_be_cooked(ingredient):
						memo[recipe] = False
						visiting.remove(recipe)
						return False
				elif ingredient not in supplies_dict:
					memo[recipe] = False
					visiting.remove(recipe)
					return False
				
			visiting.remove(recipe)
			memo[recipe] = True
			return True
		
		for recipe in recipes:
			if can_be_cooked(recipe):
				result.append(recipe)
		return result

def main():
	solution = Solution()
	assert solution.findAllRecipes(["bread"], [["yeast","flour"]], ["yeast","flour","corn"]) == ["bread"]
	assert solution.findAllRecipes(["bread","sandwich"], [["yeast","flour"],["bread","meat"]], ["yeast","flour","meat"]) == ["bread","sandwich"]
	assert solution.findAllRecipes(["bread","sandwich","burger"], [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]], ["yeast","flour","meat"]) == ["bread","sandwich","burger"]
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
