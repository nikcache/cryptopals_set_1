#Nik and Cam
#Base conversions

import base64
import codecs
import math

def bin2Hex(st):
    return hex(int(st, 2))[2:]

def bin2Base64(st):
    st = bin2Hex(st)
    return hex2Base64(st)

def bin2Plain(st):
    return eval(str(codecs.decode(bin2Hex(st), "hex"))[1:])

def hex2Bin(st):
    return bin(int(st, 16))[2:]

def hex2Base64(st):
    return codecs.encode(codecs.decode(st, 'hex'), 'base64').decode().replace("\n", "")

def hex2Plain(st):
    if len(st) % 2 != 0:
        st = '0' + st
    return eval(str(codecs.decode(st, "hex"))[1:])
        # print(st)

def base642Bin(st):
    hexSt = base642Hex(st)
    return hex2Bin(hexSt)

def base642Hex(st):
    return base64.b64decode(st).hex()

def base642Plain(st):
    hexSt = base642Hex(st)
    return hex2Plain(hexSt)

def plain2Bin(st):
    b = st.encode()
    return hex2Bin(codecs.encode(b, "hex"))

def plain2Hex(st):
    b = st.encode()
    return str(codecs.encode(b, "hex"))[2:-1]

def plain2Base64(st):
    hexSt = plain2Hex(st)
    return hex2Base64(hexSt)    

## ENCRYPT/DECRYPT
def k_decrypt(hex_str, key_lst):

    str_len = math.ceil(len(hex_str)/(len(key_lst[0])))
    # print(str_len)
    ret_lst = []

    for i in key_lst:
        temp_key = ""
        for j in range(str_len):
            temp_key += i
        # print(len(hex_str), len(temp_key))
        ret_lst.append([reverse_b_xor(hex_str, temp_key[:len(hex_str)]), i])

    return ret_lst

def reverse_b_xor(xord, st2):

    lengthst2 = len(st2)
    lengthxord = len(xord)

    # print(lengthst2, lengthxord)

    st2, xord = hex2Bin(st2), hex2Bin(xord)
    if len(st2) != 4*lengthst2:
        diff = 4*lengthst2 - len(st2)
        st2 = diff * '0' + st2
    if len(xord) != 4*lengthxord:
        diff = 4*lengthxord - len(xord)
        xord = diff * '0' + xord
    # print(len(xord), len(st2))
    # print()

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
    return bin2Hex(st1)

#Key Generator
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


def fltr(hex_str):
    # if hex_str == None:
    #     return
    temp = ""
    for i in hex_str:
        if i.lower() in "abcdefghijklmnopqrstuvwxyz !?,.;:_-'\"":
            temp += i
    return temp

def getBasicFit(st):
    # if st == None:
    #     return 
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
    # if st == None:
    #     return
    score = 0
    n_list = ['bx', 'cj', 'cv', 'cx', 'dx', 'fq', 'fx', 'gq', 'gx', 'hx', 'jc', 'jf', 'jg', 'jq', 'js', 'jv', 'jw', 'jx', 'jz', 'kq', 'kx', 'mx', 'px', 'pz', 'qb', 'qc', 'qd', 'qf', 'qg', 'qh', 'qj', 'qk', 'ql', 'qm', 'qn', 'qp', 'qs', 'qt', 'qv', 'qw', 'qx', 'qy', 'qz', 'sx', 'vb', 'vf', 'vh', 'vj', 'vm', 'vp', 'vq', 'vt', 'vw', 'vx', 'wx', 'xj', 'xx', 'zj', 'zq', 'zx']
    for i in range(len(st) - 1):
        lt1 = st[i]
        lt2 = st[i + 1]
        if lt1.lower() + lt2.lower() in n_list or lt2.lower() + lt1.lower() in n_list:
            score -= 100
    return score

def getKey(item):
    return item[0][0]

def test():
    
    binStr = '11010000110010101101100011011000110111100000001'
    hexStr = '001fd'
    base64Str = 'aGVsbG8B'
    plainStr = "hello\x01"
    
    #Test functions:
    # print('Binary to Test')
    # print(bin2Hex(binStr))
    # print(bin2Base64(binStr))
    # print(bin2Plain(binStr))
    # print()

    print('Hex to Test')
    # print(hex2Bin(hexStr))
    # print(hex2Base64(hexStr))
    print(hex2Plain(hexStr))
    # print()

    # print('Base64 to Test')
    # print(base642Bin(base64Str))
    # print(base642Hex(base64Str))
    # print(base642Plain(base64Str))
    # print()

    # print('Plain to Test')
    # print(plain2Bin(plainStr))
    # print(plain2Hex(plainStr))
    # print(plain2Base64(plainStr))

if __name__ == "__main__":
    test()