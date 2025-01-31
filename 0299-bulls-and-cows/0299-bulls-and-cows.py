class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        '''
        create a hash of secret and guess
        iterate over the guess:
            c in guess ? ame pos as is in secret?
                if yes: bulls += 1
            elif number in secret but index is inaccurate
                cows += 1

        edge case: secret and guess == 1
            there is one bull
            there are no bulls and cows because not equal
        '''

        # keep track of index to value for fast lookups O(1)
        s_d = {}
        g_d ={}

        n = len(guess)
        for i in range(n):
            s_d[i] = secret[i]
            g_d[i] = guess[i]
        
        bulls = 0
        cows = 0
        counter = collections.defaultdict(int)
        for i, c in enumerate(guess):
            if c in s_d.values() and s_d[i] == c:
                bulls += 1
                del s_d[i]
            else:
                counter[c] += 1
    
        cows = 0
        for i, c in s_d.items():
            print(counter)
            if c in counter and counter[c] > 0:
                counter[c] -= 1
                cows += 1
                

        return str(bulls) + 'A' + str(cows) + 'B'