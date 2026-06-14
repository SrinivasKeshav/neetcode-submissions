class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p, s] for p, s in zip(position, speed)]
        fleet, curTime = 0, 0

        for p, s in sorted(pair, reverse=True):
            destTime = (target - p) / s
            if curTime < destTime:
                fleet += 1
                curTime = destTime
        return fleet