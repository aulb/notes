# Sum of Two Integers
When we can't use operators, it is most likely a recursive question.

# Number of 1 Bits
Trick is: `n & (n - 1)`. Only the least significant bit of `n` is flipped to 0, so just count how many times.
*Hamming weight*

# Count Bits
Odd numbers always have one more bit than the previous number.
Even numbers always have the same number of bits as its halves. Multiplying by 2 shifts the bits to the left by one.
Multiplying by 2: `<< 1`

# Missing Number
`n * (n + 1) / 2`

# Reverse Bits
Will not do.
