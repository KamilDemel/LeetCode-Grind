nums = [-2,1,-3,4,-1,2,1,-5,4]
obecny_max = nums[0]
najlepszy_wynik = nums[0]
for i in range(1, len(nums)):
    opcja1 = nums[i]
    opcja2 = obecny_max + nums[i]
    obecny_max = max(opcja1, opcja2)
    if obecny_max > najlepszy_wynik:
        najlepszy_wynik = obecny_max
print(najlepszy_wynik)