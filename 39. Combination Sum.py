class Solution:

    def combinationSum(self,candidates: List[int], target: int) -> List[List[int]]:
        def dfs(nums: List[int], index: int):
            
            if sum(nums) > target:
                return
            
            elif sum(nums) == target:
                
                result.append(nums)
                return

            for i in range(index, len(candidates)):
                dfs(nums + [candidates[i]], i )

        result = []
        dfs([], 0)
        return result