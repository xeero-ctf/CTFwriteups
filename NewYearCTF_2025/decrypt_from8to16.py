def decrypt001(encrypted_flag):
    decrypted_flag = []
    
    for i in range(0, len(encrypted_flag), 1):
        val = ord(encrypted_flag[i])
        
        first_char = chr(val >> 8) 
        second_char = chr(val & 0xFF)  

        decrypted_flag.append(first_char)
        decrypted_flag.append(second_char)

    return ''.join(decrypted_flag)

print(decrypt001("杲潤湯筩湳瑥慤彯晟㡟扩瑳彭慫敟ㄶ形楴獽"))

#grodno{instead_of_8_bits_make_16_bits}