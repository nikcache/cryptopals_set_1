import sys
import binascii
import base64
import re

def hexToB64(st):
    b2 = hexToB2(st)
    return B2ToB64(b2)

def hexToB2(st):
    b2 = ""
    if st == "":
        return None
    for i in st:
        if i == '0':
            b2 += "0000"
        elif i == '1':
            b2 += "0001"
        elif i == '2':
            b2 += "0010"
        elif i == '3':
            b2 += "0011"
        elif i == '4':
            b2 += "0100"
        elif i == '5':
            b2 += "0101"
        elif i == '6':
            b2 += "0110"
        elif i == '7':
            b2 += "0111"
        elif i == '8':
            b2 += "1000"
        elif i == '9':
            b2 += "1001"
        elif i.lower() == 'a':
            b2 += "1010"
        elif i.lower() == 'b':
            b2 += "1011"
        elif i.lower() == 'c':
            b2 += "1100"
        elif i.lower() == 'd':
            b2 += "1101"
        elif i.lower() == 'e':
            b2 += "1110"
        elif i.lower() == 'f':
            b2 += "1111"
        else:
            return "Nonvalid input"
    return b2

def B2ToHex(st):
    hex_str = ""
    if st == "":
        return None
    for i in range(0, len(st), 4):
        if st[i:i+4] == '0000':
            hex_str += "0"
        elif st[i:i+4] == '0001':
            hex_str += "1"
        elif st[i:i+4] == '0010':
            hex_str += "2"
        elif st[i:i+4] == '0011':
            hex_str += "3"
        elif st[i:i+4] == '0100':
            hex_str += "4"
        elif st[i:i+4] == '0101':
            hex_str += "5"
        elif st[i:i+4] == '0110':
            hex_str += "6"
        elif st[i:i+4] == '0111':
            hex_str += "7"
        elif st[i:i+4] == '1000':
            hex_str += "8"
        elif st[i:i+4] == '1001':
            hex_str += "9"
        elif st[i:i+4] == '1010':
            hex_str += "a"
        elif st[i:i+4]== '1011':
            hex_str += "b"
        elif st[i:i+4] == '1100':
            hex_str += "c"
        elif st[i:i+4] == '1101':
            hex_str += "d"
        elif st[i:i+4] == '1110':
            hex_str += "e"
        elif st[i:i+4] == '1111':
            hex_str += "f"
        else:
            return "Nonvalid input"
    return hex_str

def b_xor(st1, st2):
    
    st1, st2 = hexToB2(st1), hexToB2(st2)

    if len(st1) != len(st2):
        return 'Input lengths not equal'

    ret_str = ''

    for x in range(len(st1)):
        if st1[x] == st2[x]:
            ret_str += '0'
        else:
            ret_str += '1'

    ret_str = B2ToHex(ret_str)
    return ret_str

def reverse_b_xor(xord, st2):
    
    st2, xord = hexToB2(st2), hexToB2(xord)

    if len(st2) != len(xord):
        return 'Input lengths not equal'

    st1 = ''
    
    for x in range(len(st2)):
        if st2[x] == '1' and xord[x] == '1':
            st1 += '0'
        elif st2[x] == '1' and xord[x] == '0':
            st1 += '1'
        elif st2[x] == '0' and xord[x] == '1':
            st1 += '1'
        elif st2[x] == '0' and xord[x] == '0':
            st1 += '0'
        else:
            return 'Invalid inputs'
    return B2ToHex(st1)

def B2ToB64(st):
    b64 = ""
    while len(st) % 6 != 0:
        st = "0" ++ st
    for i in range(0,len(st),6):
        if st[i:i+6] == "000000":
            b64 += "A"
        elif st[i:i+6] == "000001":
            b64 += "B"
        elif st[i:i+6] == "000010":
            b64 += "C"
        elif st[i:i+6] == "000011":
            b64 += "D"
        elif st[i:i+6] == "000100":
            b64 += "E"
        elif st[i:i+6] == "000101":
            b64 += "F"
        elif st[i:i+6] == "000110":
            b64 += "G"
        elif st[i:i+6] == "000111":
            b64 += "H"
        elif st[i:i+6] == "001000":
            b64 += "I"
        elif st[i:i+6] == "001001":
            b64 += "J"
        elif st[i:i+6] == "001010":
            b64 += "K"
        elif st[i:i+6] == "001011":
            b64 += "L"
        elif st[i:i+6] == "001100":
            b64 += "M"
        elif st[i:i+6] == "001101":
            b64 += "N"
        elif st[i:i+6] == "001110":
            b64 += "O"
        elif st[i:i+6] == "001111":
            b64 += "P"
        elif st[i:i+6] == "010000":
            b64 += "Q"
        elif st[i:i+6] == "010001":
            b64 += "R"
        elif st[i:i+6] == "010010":
            b64 += "S"
        elif st[i:i+6] == "010011":
            b64 += "T"
        elif st[i:i+6] == "010100":
            b64 += "U"
        elif st[i:i+6] == "010101":
            b64 += "V"
        elif st[i:i+6] == "010110":
            b64 += "W"
        elif st[i:i+6] == "010111":
            b64 += "X"
        elif st[i:i+6] == "011000":
            b64 += "Y"
        elif st[i:i+6] == "011001":
            b64 += "Z"
        elif st[i:i+6] == "011010":
            b64 += "a"
        elif st[i:i+6] == "011011":
            b64 += "b"
        elif st[i:i+6] == "011100":
            b64 += "c"
        elif st[i:i+6] == "011101":
            b64 += "d"
        elif st[i:i+6] == "011110":
            b64 += "e"
        elif st[i:i+6] == "011111":
            b64 += "f"
        elif st[i:i+6] == "100000":
            b64 += "g"
        elif st[i:i+6] == "100001":
            b64 += "h"
        elif st[i:i+6] == "100010":
            b64 += "i"
        elif st[i:i+6] == "100011":
            b64 += "j"
        elif st[i:i+6] == "100100":
            b64 += "k"
        elif st[i:i+6] == "100101":
            b64 += "l"
        elif st[i:i+6] == "100110":
            b64 += "m"
        elif st[i:i+6] == "100111":
            b64 += "n"
        elif st[i:i+6] == "101000":
            b64 += "o"
        elif st[i:i+6] == "101001":
            b64 += "p"
        elif st[i:i+6] == "101010":
            b64 += "q"
        elif st[i:i+6] == "101011":
            b64 += "r"
        elif st[i:i+6] == "101100":
            b64 += "s"
        elif st[i:i+6] == "101101":
            b64 += "t"
        elif st[i:i+6] == "101110":
            b64 += "u"
        elif st[i:i+6] == "101111":
            b64 += "v"
        elif st[i:i+6] == "110000":
            b64 += "w"
        elif st[i:i+6] == "110001":
            b64 += "x"
        elif st[i:i+6] == "110010":
            b64 += "y"
        elif st[i:i+6] == "110011":
            b64 += "z"
        elif st[i:i+6] == "110100":
            b64 += "0"
        elif st[i:i+6] == "110101":
            b64 += "1"
        elif st[i:i+6] == "110110":
            b64 += "2"
        elif st[i:i+6] == "110111":
            b64 += "3"
        elif st[i:i+6] == "111000":
            b64 += "4"
        elif st[i:i+6] == "111001":
            b64 += "5"
        elif st[i:i+6] == "111010":
            b64 += "6"
        elif st[i:i+6] == "111011":
            b64 += "7"
        elif st[i:i+6] == "111100":
            b64 += "8"
        elif st[i:i+6] == "111101":
            b64 += "9"
        elif st[i:i+6] == "111110":
            b64 += "+"
        elif st[i:i+6] == "111111":
            b64 += "/"
        else:
            return "Incorrect input."
    return b64

def allKeys(n):

    hex_lst = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    
    if n == 1:
        return hex_lst
    else:
        return allKeysr(n, n - 1, [], hex_lst, hex_lst)

def allKeysr(n, c, new_lst, old_lst, hex_lst):
    if c == 0:
        return old_lst
    else:
        for i in range(len(old_lst)):
            for j in range(len(hex_lst)):
                new_lst.append(old_lst[i] + hex_lst[j])
        return allKeysr(n, c-1, [], new_lst, hex_lst)

def k_encrypt(hex_str, key_lst, n):

    str_len = int(len(hex_str)//n)
    ret_lst = []

    for i in key_lst:
        temp_key = ""
        for j in range(str_len):
            temp_key += i
        ret_lst.append(b_xor(hex_str, temp_key))

    return ret_lst

def k_decrypt(hex_str, key_lst, n):

    str_len = int(len(hex_str)//n)
    ret_lst = []

    for i in key_lst:
        temp_key = ""
        for j in range(str_len):
            temp_key += i
        ret_lst.append(reverse_b_xor(hex_str, temp_key))

    return ret_lst

def fltr(hex_str):
    temp = ""
    for i in hex_str:
        if i.lower() in "abcdefghijklmnopqrstuvwxyz !?,.;:_-'\"":
            temp += i
    return temp

def getBasicFit(st):
    score = 0
    for i in st:
        letter = i.lower()
        if letter in "zqxj":
            score += 0
        elif letter in 'kv':
            score += 1
        elif letter in 'bpygfwmuc':
            score += 2
        elif letter in 'ld':
            score += 3
        elif letter in 'rhsni':
            score += 4
        elif letter in 'oa':
            score += 5
        elif letter == 't':
            score += 6
        elif letter == 'e':
            score += 8
        else:
            score += 0
    return score

def getAdvFit(st):
    score = 0
    n_list = ['bx', 'cj', 'cv', 'cx', 'dx', 'fq', 'fx', 'gq', 'gx', 'hx', 'jc', 'jf', 'jg', 'jq', 'js', 'jv', 'jw', 'jx', 'jz', 'kq', 'kx', 'mx', 'px', 'pz', 'qb', 'qc', 'qd', 'qf', 'qg', 'qh', 'qj', 'qk', 'ql', 'qm', 'qn', 'qp', 'qs', 'qt', 'qv', 'qw', 'qx', 'qy', 'qz', 'sx', 'vb', 'vf', 'vh', 'vj', 'vm', 'vp', 'vq', 'vt', 'vw', 'vx', 'wx', 'xj', 'xx', 'zj', 'zq', 'zx']
    for i in range(len(st) - 1):
        lt1 = st[i]
        lt2 = st[i + 1]
        if lt1.lower() + lt2.lower() in n_list or lt2.lower() + lt1.lower() in n_list:
            score -= 100
    return score

def s_1_c_4():

    c4 = open('s_1_c_4.txt', 'r')
    c4 = c4.read()
    c4 = c4.split()
    ret_lst = []

    # for i in c4:
    #     ret_lst.append(i[:-1])

    return c4

def s_1_c_4_solution():

    ret_lst = []
    n = 2

    for i in s_1_c_4():
        # print(i)
        k_str = k_decrypt(i, allKeys(n), n)
        # print(k_str)
        for j in k_str:
            ret_lst.append(j)
    
    return ret_lst
        
def h_dist(str1, str2):
    if len(str1) == len(str2):
        ret_count = 0
        for k in range(len(str1)):
            if str1[k] == str2[k]:
                pass
            else:
                ret_count+= 1
        return ret_count
    else:
        return 'Input strings not the same length'        

def B642B2(iStr):
    iStr = binascii.a2b_base64(iStr)
    return bin(int.from_bytes(iStr, byteorder=sys.byteorder))[2:]

def plain2bin(iStr):
    byte_array = iStr.encode()

    binary_int = int.from_bytes(byte_array, "big")
    binary_string = bin(binary_int)

    return binary_string[2:]

def plain2hex(iStr):
    return iStr.encode("latin-1").hex()

def hex2plain(iStr):
    return bytes.fromhex(iStr).decode('latin-1')

# SOLUTION FOR S_!_C_4
def getKey(item):
    return item[0]

def main():

    # print(B642B2('l0=='))

    # tStr1 = plain2bin("this is a test")
    # tStr2 = plain2bin("wokka wokka!!!")
    # print(h_dist(tStr1, tStr2))

    # tStr = 'Nikesh'
    # print(plain2bin(tStr)[2:])


    #For Challenge 4
    txt = open('sample_solution_s_1_c_4_decoded.txt', 'w', encoding = 'latin-1')
    s_list = s_1_c_4_solution()
    f_list = []
    for i in s_list:
        # print(i)
        hex_string = bytes.fromhex(i).decode('latin-1')
        fltr_str = fltr(hex_string)
        f_list.append([getBasicFit(fltr_str) + getAdvFit(fltr_str), fltr_str])

    f_list = sorted(f_list, key = getKey)

    for i in f_list:
        txt.write(i[1] + '\n' + 'SCORE: ' + str(i[0]) +'\n\n')

    txt.close()

if __name__ == '__main__':
    main()

# sys.setdefaultencoding()

# for i in s_1_c_4_solution():
#     try:
#         bytes_object = bytes.fromhex(i)
#         try:
#             ascii_string = bytes_object.decode("ASCII")
#             txt.write(ascii_string + '\n')
#         except:
#             pass
#     except Exception as e:
#         print(ascii_string, e)
#     txt.write(ascii_string)
# txt.close()

# print(bytes.fromhex('f1c9b817a6d2caaeb5f7edbca7dac912c2198cbfa6ffe1c0aca319d8efcd').decode('latin-1'))

# str_test = k_encrypt('f1c9b817a6d2caaeb5f7edbca7dac912c2198cbfa6ffe1c0aca319d8efcd', ['a'], 1)
# print(str_test)
# str_test2 = k_decrypt('5b6312bd0c7860041f5d47160d7063b868b326150c554b6a0609b3724567', ['a'], 1)
# print(str_test2)

# # For s_1_c_1
# inStr = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
# if hexToB64(inStr) == 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t':
#     print('s_1_c_1 is correct!')
# else:
#     print('Uh-oh, s_1_c_1 is incorrect!')
#     print(hexToB64(inStr))


# # For s_1_c_2
# inSt1 = '1c0111001f010100061a024b53535009181c'
# inSt2 = '686974207468652062756c6c277320657965'
# # Asserting answer
# if b_xor(inSt1, inSt2) == '746865206b696420646f6e277420706c6179':
#     print('s_1_c_2 is correct!')
# else:
#     print('Uh-oh, s_1_c_2 is incorrect!')

# # For s_1_c_3
# inSt1 = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

# # Asserting answer
# n = 0
# for i in k_decrypt(inSt1, allKeys()):
#     if i == '436f6f6b696e67204d432773206c696b65206120706f756e64206f66206261636f6e':
#         print(i, allKeys()[n])
#     n+=1
#     #Answer for s_1_c_3 = '58'
# if b_xor(inSt1, inSt2) == '746865206b696420646f6e277420706c6179':
#     print('s_1_c_2 is correct!')
# else:
#     print('Uh-oh, s_1_c_2 is incorrect!')
# 436f6f6b696e67204d432773206c696b65206120706f756e64206f66206261636f6e

