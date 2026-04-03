class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        # I will traverse the input numbers from right to left,
        # however I will populate the result left to right.
        # so that I can easily pop the extra zero(s)
        # after that I can reverse, make it str and return.

        # special case. if aone o fthe number is 0
        if num1[0] == "0" or num2[0] == "0":
            return("0")

        result = [0] * (len(num1) + len(num2))

        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                k = len(num1) + len(num2) - ( i + j) - 2
                print(i, j, k)
                res = int(num1[i]) * int(num2[j]) + result[k]
                val = res % 10
                carry = res // 10
                result[k] = val
                while carry:
                    k += 1
                    val = (result[k] + carry) % 10
                    carry = (result[k] + carry) // 10
                    result[k] = val
        
        while (result[-1] == 0):
            result.pop()
        result.reverse()
        result = [str(x) for x in result]
        return("".join(result))

                 