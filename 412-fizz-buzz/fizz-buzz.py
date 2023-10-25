class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        array_n = []
        for i in range(n):
            i = i+1
            digit = ''
            if( i % 15 == 0):
                digit = "FizzBuzz"
            elif( i % 3 == 0):
                digit = "Fizz"
            elif(i % 5 == 0):
                digit = "Buzz"
            else:
                digit = str(i)
            array_n.append(digit)
        return array_n
