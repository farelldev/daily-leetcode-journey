class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        if digits[-1] == 9:
            i = -1

            while digits[i] == 9:
                if len(digits) == -i:
                    digits[i] = 1
                    digits.append(0)
                    return digits

                digits[i] = 0
                i -= 1

            digits[i] += 1
            return digits
            

        digits[-1] += 1
        return digits