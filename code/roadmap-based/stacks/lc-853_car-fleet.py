from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        Solution:
            A jam happen, if a car in the back is taking less time to
            reach the destination than a car in the front

            So we start counting from the furthest car - we calculate
            the time it takes to reach the target, then put it in a
            stack

            Then the next furthest car, if the time to reach destination
            is less, than a jam happened and there's a fleet.

            Since this new car will be blocked by that car in the front,
            its speed will be limited by the car in the front

            So we just keep the leading jammed car in the stack (and
            only note down its time to reach destination, since the
            slower car's time determines when the fleet reaches the
            target)

            If the car won't be blocked, we can then add this car (its
            time) into the stack, since this means that this car won't
            be blocked by a fleet in front of it, but it itself could be
            a blocker for the cars behind

            Once we've iterated over all cars, then we just need to
            count the length of the stack to know how many fleets formed

        Time Complexity: O(n log(n))
            O(n log(n)) to sort by position. Then we incur another O(n)
            iterating over all cars

        Space Complexity: O(n)
            The stack could grow to O(n), and the combined speed and
            position array also takes up O(n)
        """
        array = [(p, s) for p, s in zip(position, speed)]
        array = sorted(array, key=lambda x: -x[0])
        stack = []

        for p, s in array:
            curr_time = (target - p) / s
            if stack:
                if stack[-1] >= curr_time:
                    continue
            stack.append(curr_time)

        return len(stack)
