class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        result = []


        for length in range(1,10):
            for start_digit in range(1,10-length + 1):
                num =0

                for i in range(length):
                    num = num*10 +(start_digit + i)



                if low <= num <= high:
                    result.append(num)

                elif num > high:

                    break
        return result