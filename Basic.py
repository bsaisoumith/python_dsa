""" 
# Binary to Decimal 
num = 1010
dec_num = int(num,2)
print(dec_num)

def bin_2_dec(num):
    dec_num = 0
    pow = 0

    for i in reversed(num):
        if i == '1':
            dec_num += 2 ** pow
        pow += 1
    return dec_num

print(bin_2_dec(num))
"""


""" 
# Decimal to Binary
num = 10
bin_num = bin(num)[2:] # to remove 0b
print(bin_num)

def dec_2_bin(num):
    if num == 0:
        return "0"
    
    bin_digits = []
    
    while num > 0:
        rem = num % 2
        bin_digits.append(str(rem))
        num = num // 2
    
    bin_digits.reverse()

    return ''.join(bin_digits)

print(dec_2_bin(num))
"""



