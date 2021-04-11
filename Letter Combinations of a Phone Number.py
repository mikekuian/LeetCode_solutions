def letterCombinations(digits):

    digits_dict = {"2": ["a", "b", "c"], "3": ["d", "e", "f"],
                   "4": ["g", "h", "i"], "5": ["j", "k", "l"], "6": ["m", "n", "o"],
                   "7": ["p", "q", "r", "s"], "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]}

    global buf
    global answer
    answer = []
    buf = ""

    def backward(i):

        global buf
        global answer

        if i == len(digits):
            return

        for char in digits_dict[digits[i]]:

            buf += char

            if len(buf) == len(digits):
                answer.append(buf)

            backward(i + 1)
            buf = buf[:-1]

    backward(0)

    return answer

if __name__ == '__main__':
    digits = "23"
    print(letterCombinations(digits))