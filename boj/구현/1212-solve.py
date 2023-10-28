octal_num = input()
bin_num = [] 

bin_digits = dict() 

for octal_digit in range(8):
    bin_digit = [] 
    cur_octal_digit = octal_digit 
    
    while cur_octal_digit > 0:
        div, mod = cur_octal_digit // 2, cur_octal_digit % 2
        bin_digit.append(str(mod))
        cur_octal_digit = div
    
    bin_digit = ''.join(bin_digit[::-1])
        
    while len(bin_digit) < 3:
        bin_digit = '0' + bin_digit
        
    bin_digits[str(octal_digit)] = bin_digit
    
for octal_digit in octal_num:
    bin_num.append(bin_digits[octal_digit])
    
bin_num = ''.join(bin_num)
while len(bin_num) > 1 and bin_num[0] == '0':
    bin_num = bin_num[1:]

print(bin_num)