class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        rad = deque()
        div = deque()
        
        for i, senator in enumerate(senate):
            if senator == 'R':
                rad.append(i)
            else:
                div.append(i)
        n = len(senate)
        while rad and div:
            if rad[0] < div[0]:
                rad.append(n + 1)
            else:
                div.append(n + 1)
            n += 1
            rad.popleft()
            div.popleft()

        return 'Radiant' if rad else 'Dire'
                

        