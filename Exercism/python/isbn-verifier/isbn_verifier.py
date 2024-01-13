def is_valid(isbn):
    polynomialFactor = 10
    for char in isbn[:-1]:
        if char.isdigit():
            isbnVerifierPolynomial += (int(char) * polynomialFactor)
            polynomialFactor -= 1
