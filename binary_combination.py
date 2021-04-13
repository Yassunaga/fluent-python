bin_numbers = '0 1'.split()
bits = [
    str(bit_one + bit_two + bit_three)
    for bit_one in bin_numbers
    for bit_two in bin_numbers
    for bit_three in bin_numbers
]
print(bits)
