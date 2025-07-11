from typing import List
from collections import defaultdict


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        Solution:
            Goal is to find out the time it takes to reach the target
            from position x. Then fleets will form if cars behind a car
            have a shorter time to reach than the other. Fleets will
            always be blocked by the slowest car
        """
        return None