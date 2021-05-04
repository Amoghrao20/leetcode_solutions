class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def combination_sum(cur_ans, cur_sum, cand_idx):
                if cur_sum >= target:
                    if cur_sum == target:
                        ans.append(cur_ans)
                    return
                for i in range(cand_idx, len(candidates)):
                    combination_sum(cur_ans + [candidates[i]], cur_sum + candidates[i], i)
        ans = []
        combination_sum([], 0, 0)
        return ans
