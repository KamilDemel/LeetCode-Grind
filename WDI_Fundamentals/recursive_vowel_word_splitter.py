def count_vowel_partitions(word):
    vowels = ["a", "e", "i", "o", "u"]
    total_ways = 0

    for i in range(1, len(word)):
        prefix = word[0:i]

        prefix_has_vowel = False
        for char in prefix:
            if char.lower() in vowels:
                prefix_has_vowel = True
                break

        if prefix_has_vowel:
            suffix = word[i:]
            suffix_has_vowel = False
            for char in suffix:
                if char.lower() in vowels:
                    suffix_has_vowel = True
                    break

            if suffix_has_vowel:
                total_ways += 1
                total_ways += count_vowel_partitions(suffix)

    return total_ways
