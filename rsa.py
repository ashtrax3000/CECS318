import modutil  # will need the function modinv() which returns the inverse of an integer

def blocksize(n):
    """returns the size of a block in an RSA encrypted string"""
    twofive = "25"
    while int(twofive) < n:
        twofive += "25"
    return len(twofive) - 2
    
def RSAletters2digits(letters):
    """converts a string of letters without spaces to a string of integers"""
    letter2digit = {"A" : "00", "B" : "01", "C" : "02", "D" : "03", "E" : "04", 
                  "F" : "05", "G" : "06", "H" : "07", "I" : "08", "J" : "09",
                  "K" : "10", "L" : "11", "M" : "12", "N" : "13", "O" : "14",  
                  "P" : "15", "Q" : "16", "R" : "17", "S" : "18", "T" : "19",
                  "U" : "20", "V" : "21", "W" : "22", "X" : "23", "Y" : "24", 
                  "Z" : "25"}
    
    letters_copy = letters.replace(" ", "")  # getting rid of spaces    
    
    digits = ""
    for c in letters_copy:
        digits += letter2digit[c.upper()]
        
    return digits
    
def RSAdigits2letters(digits):
    """converts a string of double digits without spaces in the range 00-25 to a string of letters A-Z"""
    letter2digit = {"A" : "00", "B" : "01", "C" : "02", "D" : "03", "E" : "04", 
                  "F" : "05", "G" : "06", "H" : "07", "I" : "08", "J" : "09",
                  "K" : "10", "L" : "11", "M" : "12", "N" : "13", "O" : "14",  
                  "P" : "15", "Q" : "16", "R" : "17", "S" : "18", "T" : "19",
                  "U" : "20", "V" : "21", "W" : "22", "X" : "23", "Y" : "24", 
                  "Z" : "25"}
        
    digit2letter = dict((v,k) for k,v in letter2digit.items())  #creating a dictionary with keys and values exchanged
        
    letters = ""
    start = 0  #initializing starting index of first digit
    for i in range(0, len(digits), 2):
        digit = digits[start : start + 2]  # accessing the double digit
        letters += digit2letter[digit]     # concatenating to the string of letters
        start += 2                         # updating the starting index for next digit
    
    return letters
  
## Decryption  
def decryptRSA(c, p, q, e):
  c_copy = c.replace(" ", "")
  m = (p - 1) * (q - 1)
  e_inv = modutil.modinv(e, m)
  n = p * q
  # 

  digits = ""
  k = blocksize(n)
  start = 0
  for i in range(0,len(c_copy), k):
      block = c_copy[start: start + k]  # accessing each block of digits
      digit = str(int(block) ** e_inv % n)  # decrypting the block
      if len(digit) % 2 != 0:  #padding the block before adding it to the string
          digits += "0" + digit
      else:
          digits += digit
      start += k  #updating starting index for next block
  return RSAdigits2letters(digits)  #converting digits to letters
    
## Encryption
def encryptRSA(s, a, b, e):
    s_copy = s.replace(" ", "")
    n = a * b
    
    #STEP 1 & 2: CONVERT TO STRING OF INTEGERS
    digits_string = RSAletters2digits(s_copy)
        
        
    # STEP 3 & 4: DIVIDE INTO BLOCKS OF 2N DIGITS ENCRYPT EACH BLOCK AND CONCATENATE
    # determining l = 2N 
    l = blocksize(n)
    
    # padding if necessary
    if len(digits_string) % l != 0:
        diff = l - len(digits_string) % l
        digits_string = digits_string + "23" * (diff//2) # Letter X = 23
  
    # encrypting and concatenating 
    encryption = ""
    for i in range(0, len(digits_string), l):
        start = i
        end = i + l
        base = int(digits_string[start: end])
        digit = str(base ** e % n)
        if len(digit) % 2 != 0:
            encryption = encryption + " " + "0" + digit
        else:
            encryption = encryption + " " + digit
    
    return encryption

encrypted1 = encryptRSA("STOP", 43, 59, 13)
decrypted1 = decryptRSA(encrypted1, 43, 59, 13)
print("Encrypted Message:", encrypted1)
print("Decrypted Message:", decrypted1)


encrypted2 = encryptRSA("HELP", 43, 59, 13)
decrypted2 = decryptRSA(encrypted2, 43, 59, 13)
print("Encrypted Message:", encrypted2)
print("Decrypted Message:", decrypted2)

encrypted1 = encryptRSA("STOPS", 43, 59, 13)
decrypted1 = decryptRSA(encrypted1, 43, 59, 13)
print("Encrypted Message:", encrypted1)
print("Decrypted Message:", decrypted1)
