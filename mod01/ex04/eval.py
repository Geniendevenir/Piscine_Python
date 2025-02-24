class Evaluator:
    def check_values(coefs, words):
        if (not isinstance(coefs, list) or not isinstance(words, list)):
            print("Coefs and Words should be lists")
            return -1
        elif (len(coefs) <= 0 or len(words) <= 0 or len(coefs) != len(words)):
            print("Coefs and Words should be lists of floats of the same lenght")
            return -1
        for number in coefs:
            if (not isinstance(number, float)):
                print("Coefs list should contains only floats values")
                return -1
        for char in words:
            if (not isinstance(char, str)):
                print("words list should contains only floats values")
                return -1
    
    def zip_evaluate(coefs, words):
        if (Evaluator.check_values(coefs, words) == -1):
            return -1
        return sum(nbr * len(word) for nbr, word in zip(coefs, words))

    def enumerate_evaluate(coefs, words):
        if (Evaluator.check_values(coefs, words) == -1):
            return -1
        total = 0.
        for i, word in enumerate(words):
            total += coefs[i] * len(word)
        return total
    

words = ["Le", "Lorem", "Ipsum", "n’", "est", "pas", "simple"]
coefs = [0.0, -1.0, 1.0, -12.0, 0.0, 42.42]
print(Evaluator.enumerate_evaluate(coefs, words))

words = ["Le", "Lorem", "Ipsum", "est", "simple"]
coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
print(Evaluator.zip_evaluate(coefs, words))