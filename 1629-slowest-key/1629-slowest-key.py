class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        
        t = releaseTimes[0]
        k = keysPressed[0]
        
        for i in range(1, len(releaseTimes)):
            time = releaseTimes[i] - releaseTimes[i - 1]
            key = keysPressed[i]
            
            if time > t:
                t = time
                k = key
            
            elif (time == t) & (ord(key) > ord(k)):
                t = time
                k = key
        
        return k