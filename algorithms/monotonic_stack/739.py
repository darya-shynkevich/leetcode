class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []
        answer = []

        for temp in temperatures:
            i = 0
            while stack and stack[-1] < temp:
                i += 1
                stack.pop()

            stack.append(temp)
            answer.append(i)

        print(answer)


if __name__ == '__main__':
    solution = Solution()
    solution.dailyTemperatures([73,74,75,71,69,72,76,73])