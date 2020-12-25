# from cp_p_1 import * 
# from cp_s1_p1 import * 
from convert import *

def normed_ham(plain, key_size):
    str1 = plain[0:key_size]
    str2 = plain[key_size : 2*key_size]
    #print(str1, str2)
    str1, str2 = plain2Bin(str1), plain2Bin(str2)
    str1, str2 = sameSize(str1, str2)
    #print(str1, str2)
    ham = h_dist(str1, str2)
    #print(ham)
    return ham / key_size

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

def sameSize(str1, str2):
    diff = abs(len(str1) - len(str2))
    if len(str1) < len(str2):
        str1 = diff * '0' + str1
    elif len(str1) > len(str2):
        str2 = diff * '0' + str2
    return str1, str2

# def padder(iStr):
#     if len(iStr) % 4 == 0:
#         return iStr
#     else:
#         while len(iStr) % 4 != 0:
#             iStr += '='
#         return iStr
def Base642PlainAll(lines):
    count = 0
    chompLines = []
    for line in lines:
        chompLine = chomp(line)
        chompLines.append(chompLine)
    plainLines = []
    for chompLine in chompLines:
        count+= len(base642Plain(chompLine))
        plainLines.append(base642Plain(chompLine))
    print(count)
    return plainLines


def detectKeySize(lines, num_keys, maxKeySize):
    chompLines = []
    for line in lines:
        chompLine = chomp(line)
        chompLines.append(chompLine)
    plainLines = []
    for chompLine in chompLines:
        plainLines.append(base642Plain(chompLine))
    flat_lst = [item for sublist in plainLines for item in sublist]
    flat_in = ''.join(map(str, flat_lst))
    # print(flat_in)

    minNorm = normed_ham(flat_in, 2)
    # print(minNorm)
    bestSize = 2
    norm_key_list = [[minNorm, 2]]
    for i in range(3,maxKeySize + 1):
        ham = normed_ham(flat_in, i)
        minNorm = min(minNorm, ham)
        norm_key_list.append([ham, i])
        if minNorm == ham:
            # print('Lower found', minNorm)
            bestSize = i
    
    norm_key_list.sort(key = lambda x: x[0])
    # print(norm_key_list)

    ret_lst = []
    for i in range(num_keys):
        ret_lst.append(norm_key_list[i][1])
    

    return ret_lst

def block(lines, keySize):
    chompLines = []
    for line in lines:
        chompLine = chomp(line)
        chompLines.append(chompLine)
    plainLines = []
    for chompLine in chompLines:
        plainLines.append(base642Plain(chompLine))

    # print(plainLines)
    final_list = []
    for plain in plainLines:
        # print(len(plain))
        emp = ""
        count = 0
        for ch in range(len(plain)):
            emp = emp + plain[ch]
            count+=1
            if count % keySize == 0:
                final_list.append(emp)
                emp = ""

    return final_list

def transpose(lst, keySize):
    newList = []
    
    for i in range(keySize):
        acc = ''
        for j in range(len(lst)):
            acc = acc + lst[j][i]
        newList.append(acc)
    
    print(len(newList))

    return newList 

def chomp(x):
    if x.endswith("\r\n"): return x[:-2]
    if x.endswith("\n") or x.endswith("\r"): return x[:-1]
    return x
    
def find_best_key(lst):

    # txt = open('potential_end_of_the_IS.txt', 'w', encoding = 'latin-1')
    s_list = lst
    f_list = []
    for i in s_list:
        
        i_val = i[0]
        i_key = i[1]

        # print(i_val)
        plain_txt = hex2Plain(i_val)#bytes.fromhex(i).decode('latin-1')
        # print(plain_txt)
        fltr_str = fltr(plain_txt)
        basic_fit = getBasicFit(fltr_str)
        adv_fit =  getAdvFit(fltr_str)
        if basic_fit == None:
            pass
        else:
            f_list.append([[basic_fit + adv_fit, fltr_str], i_key])

    f_list = sorted(f_list, key = getKey)

    return f_list[-1][1]

    # for i in f_list:
    #     txt.write(i[1] + '\n' + 'SCORE: ' + str(i[0]) +'\n\n')

    # txt.close()

def test():
    
    file1 = open('cryptFile6.txt', 'r')
    lines = file1.readlines()
    
    keySize_lst = detectKeySize(lines, 3, 40)

    for keySize in keySize_lst:

        block_lst = block(lines, keySize)
        trans_block_lst = transpose(block_lst, keySize)

        re_xor = []
        keys = allKeys(2)
        final_key = ""

        for i in trans_block_lst:
            i = plain2Hex(i)
            r_xor = k_decrypt(i, keys)
            # print(r_xor[0])
            best_key = find_best_key(r_xor)
            final_key+=best_key
        
        print(final_key)

        plainText = Base642PlainAll(lines)
        final_str = ""
        for plain in plainText:
            final_str+=plain

       
        final_r_xor = k_decrypt(plain2Hex(final_str), [final_key])
        print(hex2Plain(final_r_xor[0][0]))

    print("That's all folks!")

if __name__ == '__main__':
    test()