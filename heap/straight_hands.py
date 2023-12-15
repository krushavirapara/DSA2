import heapq
from typing import List
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        

        if len(hand) % groupSize != 0:
            return False

        # Sort the hand list to make it easier to pop elements
        

        while hand:
            heapq.heapify(hand)
            current_min = heapq.heappop(hand)

            # Check the consecutive elements in the group
            for i in range(1, groupSize):
                next_element = current_min + i

                if next_element not in hand:
                    return False

                hand.remove(next_element)

        return True

sol = Solution()
hand = [1, 2, 3, 6, 2, 3, 4, 7, 8]
groupSize = 3
result = sol.isNStraightHand(hand, groupSize)
print(result)

