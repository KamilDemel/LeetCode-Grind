def combinationSum2(candidates, target):
    n = len(candidates)
    res = []
    candidates.sort()
    def reku(i=0,curr_sum=0,res_list = None):
        if res_list is None:
            res_list = []
        if curr_sum == target:
            res.append(res_list.copy())
            return
        if curr_sum > target:
            return
        for idx in range(i,n):
            if idx > i and candidates[idx] == candidates[idx-1]:
                continue
            res_list.append(candidates[idx])
            reku(idx+1,curr_sum+candidates[idx],res_list)
            res_list.pop()
    reku()
    return res
