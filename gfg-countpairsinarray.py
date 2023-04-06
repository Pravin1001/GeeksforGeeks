    def getPairsCount(self, arr, n, k):
        c = 0
        freq = {}
        for num in arr:
            if k - num in freq:
                c += freq[k - num]
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        return c
