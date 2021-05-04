class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates = sorted(candidates)
        self.dfs(candidates, target,[],res)

        return res

    def dfs(self,candidates, target, path, res):
        if target==0:
            res.append(path)
            return
        for i in range(len(candidates)):
            if candidates[i]>target:
                continue
            if i>=1 and candidates[i] == candidates[i-1]:
               continue
            self.dfs(candidates[i+1:],target-candidates[i],path+[candidates[i]],res)
