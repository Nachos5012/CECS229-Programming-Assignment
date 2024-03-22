""" ---------------- PROBLEM 1 ----------------"""
def equiv_to(a, m, low, high):
    # k_low = (low - a) // m
    k_low = -(-(low - a)//m)
    k_high = (high - a) // m
    # k_high = (high - a) // m
    k_vals = list(range(k_low, k_high + 1))
    x_vals = [m * k + a for k in k_vals]
    return x_vals

""" ---------------- PROBLEM 2 ----------------"""
def b_expansion(n, b):
    digits = [] 
    q = n
    while q != 0:
        digit = q % b
        if b == 16 and digit > 9:
            hex_dict = {10: 'A', 11 : 'B', 12: 'C', 13: 'D', 14: 'E', 15 : 'F'}
            digit = hex_dict[digit]
        digits.append(str(digit))
        q = q // b
    return ''.join(digits[::-1])
  
""" ---------------- PROBLEM 3 ----------------"""

def binary_add(a, b): 
    a = a.replace(' ', '')
    b = b.replace(' ', '')
    
    if len(a) < len(b):
        diff = len(b) - len(a)
        a = "0" * diff + a
    elif len(a) > len(b):
        diff = len(a) - len(b)
        b = "0" * diff + b
    
    result = ""
    carry = 0
    for i in reversed(range(len(a))):
        a_i = int(a[i])
        b_i = int(b[i])
    
        result_digit = (a_i + b_i + carry) % 2
        carry = (a_i + b_i + carry) // 2
        
        result = str(result_digit) + result
    
    if carry == 1:
        result = '1' + result
        
    return result
""" ---------------- PROBLEM 4 ----------------"""

def binary_mul(a, b):
  #no more white space in the string
    a = a.replace(' ', '')
    b = b.replace(' ', '')

  #algorithm
    partial_products = []
    i = 0
  #index of the current binary bit of the string'a' begining at 0, right-to-left
    for bit in reversed(a):
        if bit == '1':
            partial_product = b + '0' * i
            partial_products.append(partial_product)
        i += 1 # append(a+bit)
    
    result = '0'
  #while len(partial_product)>0:
    for partial_product in partial_products:
        result = binary_add(result, partial_product)
        
    return result