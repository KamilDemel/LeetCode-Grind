def permutations(nums):
    res = []
    def reku_pomoc(sciezka=None):
        if not sciezka:
            sciezka = []
        if len(sciezka) == len(nums):
            res.append(sciezka[:])
            return
        for i in range(len(nums)):
            if nums[i] in sciezka:
                continue
            sciezka.append(nums[i])
            reku_pomoc(sciezka)
            sciezka.pop()
    reku_pomoc()
    return res
