class Solution:
    def removeDigit(self, number: str, digit: str) -> str:

        result = []
        number_array = list(number)
        count = number_array.count(digit)


        for idx, number in enumerate(number_array):
            if number == digit:
                number_array[idx] = ''
                result.append("".join(number_array))
                number_array[idx] = number
                
        return max(result)