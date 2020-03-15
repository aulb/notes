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
You can kill off `n` so. Also need to ask, 64 or 32 bit system? Assume 32.
We need to examine the bit one by one.
Powerful tool is to
1) Shift (multiply or divide by 2)
2) Examine the first bit, `n & 1`
