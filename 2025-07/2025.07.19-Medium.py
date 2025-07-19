"""
1233. Remove Sub-Folders from the Filesystem

Given a list of folders folder, return the folders after removing all sub-folders in those folders. You may return the answer in any order.

If a folder[i] is located within another folder[j], it is called a sub-folder of it. A sub-folder of folder[j] must start with folder[j], followed by a "/". For example, "/a/b" is a sub-folder of "/a", but "/b" is not a sub-folder of "/a/b/c".

The format of a path is one or more concatenated strings of the form: '/' followed by one or more lowercase English letters.

For example, "/leetcode" and "/leetcode/problems" are valid paths while an empty string and "/" are not.

Example 1:
Input: folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
Output: ["/a","/c/d","/c/f"]
Explanation: Folders "/a/b" is a subfolder of "/a" and "/c/d/e" is inside of folder "/c/d" in our filesystem.

Example 2:
Input: folder = ["/a","/a/b/c","/a/b/d"]
Output: ["/a"]
Explanation: Folders "/a/b/c" and "/a/b/d" will be removed because they are subfolders of "/a".

Example 3:
Input: folder = ["/a/b/c","/a/b/ca","/a/b/d"]
Output: ["/a/b/c","/a/b/ca","/a/b/d"]
 
Constraints:
1 <= folder.length <= 4 * 10^4
2 <= folder[i].length <= 100
folder[i] contains only lowercase letters and '/'.
folder[i] always starts with the character '/'.
Each folder name is unique.
"""
from typing import List
from collections import defaultdict

class Solution:
	def removeSubfolders(self, folder: List[str]) -> List[str]:
		book = defaultdict(int)
		for fol in folder:
			book[fol] = 1

		result = []

		for fol in folder:
			result.append(fol)
			slashCount = fol.count("/")
			start = 1
			for i in range(1, slashCount):
				index = fol.find("/", start)
				start = index + 1
				if fol[:index] in book:
					result.pop()
					break

		return result
    
def main():
	solution = Solution()
	assert solution.removeSubfolders(["/a","/a/b","/c/d","/c/d/e","/c/f"]) == ["/a","/c/d","/c/f"]
	assert solution.removeSubfolders(["/a","/a/b/c","/a/b/d"]) == ["/a"]
	assert solution.removeSubfolders(["/a/b/c","/a/b/ca","/a/b/d"]) == ["/a/b/c","/a/b/ca","/a/b/d"]
	assert solution.removeSubfolders(["/a/b/c","/abc/d"]) == ["/a/b/c","/abc/d"]
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
