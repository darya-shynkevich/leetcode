# Given an n x n binary matrix image, flip the image horizontally, then invert it, and return the resulting image.
#
# To flip an image horizontally means that each row of the image is reversed.
#
# For example, flipping [1,1,0] horizontally results in [0,1,1].
# To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.
#
# For example, inverting [0,1,1] results in [1,0,0].
#
# Constraints:
#
# n == image.length
# n == image[i].length
# 1 <= n <= 20
# images[i][j] is either 0 or 1.
from typing import List


class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        result = []

        for row in image:
            result.append(list(map(lambda x: int(not x), reversed(row))))

        return result


if __name__ == "__main__":
    solution = Solution()

    assert solution.flipAndInvertImage(
        image=[
            [1, 1, 0],
            [1, 0, 1],
            [0, 0, 0]
        ]
    ) == [
        [1, 0, 0],
        [0, 1, 0],
        [1, 1, 1]
    ]

    assert solution.flipAndInvertImage(
        image=[
            [1, 1, 0, 0],
            [1, 0, 0, 1],
            [0, 1, 1, 1],
            [1, 0, 1, 0]]
    ) == [
        [1, 1, 0, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 1],
        [1, 0, 1, 0]
    ]
