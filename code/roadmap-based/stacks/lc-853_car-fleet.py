from typing import List
from collections import defaultdict


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # we can iterate forward for position
        # then if more than 1 car meets, we then need to change their speed
        # to the smallest, and we also know then this is a fleet
        # we do so until we reach the target
        fleet_count = 0
        n = len(position)
        fleets = defaultdict(list)
        for i, p in enumerate(position):
            fleets[p].append(i)
        fleet_speeds = {position[idx]: s for idx, s in enumerate(speed)}

        while n > 0:
            for p, car_list in fleets.items():
                if not car_list:
                    continue
                
                new_position = p + fleet_speeds[p]
                if new_position >= target:
                    fleet_count += 1
                    fleets[p] = []
                    n -= len(car_list)
                    continue
                else:
                    # but now we have to think about how to not immediately repeat
                    # the same cars when we loop through the fleets dict in the same
                    # round
                    fleets[new_position].extend(car_list)
        return fleet_count
