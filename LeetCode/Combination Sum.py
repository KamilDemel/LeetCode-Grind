def combinationSum(candidates, target):
    n = len(candidates)
    res = []
    def reku(i=0,curr_sum=0,res_list = None):
        if res_list is None:
            res_list = []
        if i == n:
            return
        curr = candidates[i]
        if curr_sum == target:
            res.append(res_list.copy())
            return
        if curr_sum < target:
            res_list.append(curr)
            reku(i,curr_sum+curr,res_list)
            res_list.pop()
        if curr_sum > target:
            return
        reku(i + 1, curr_sum, res_list)
    reku()
    return res
