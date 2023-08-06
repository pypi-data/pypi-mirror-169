import getopt
import shutil
import os
import sys
from pathlib import Path
from itertools import product
from random import randint
import math


def main():
    # console input process
    inputfile = ''
    inputsymbol = ''
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hi:s:", ["ifile=", "isymbol="])
    except getopt.GetoptError:
        print('main.py -i <inputfile> -s <inputsymbol')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('main.py -i <inputfile> -s <inputsymbol')
            print('space between each symbol')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg

        elif opt in ("-s", "--isymbol"):
            inputsymbol = arg

    with open('config.txt', 'w', encoding='utf-8') as f:
        f.write(inputsymbol)

    # 先處理src # 內容
    shutil.copyfile(inputfile, "temp.cpp")
    hashtag_predeal("temp.cpp", inputfile)
    # 取得正規化list
    normalized_src = normalize("temp.cpp")

    # check config if >=2
    adjust_size()

    # 生成符號 dic
    nsset = set(customsplit(normalized_src))
    emojilen = get_encode_slen(len(nsset), get_emoji_size())
    emojils = get_rand_emoji(emojilen)
    var_dict = generate_dic(nsset, emojils)

    map_src = customsplit(normalized_src)

    # define string
    definlines = []
    for i in var_dict:
        if var_dict[i] == '':
            continue
        definlines.append(f"#define {var_dict[i]} {i}")

    # writing HotE3coder.cpp
    ipfile_dic = str(Path(inputfile).parent.resolve())
    with open(ipfile_dic+'\Hot3nCoder.cpp', 'a', encoding='utf-8') as f:
        for line in definlines:
            f.write(line+'\n')

        linespsrc = normalized_src.splitlines()
        for line in linespsrc:
            stringsp = customsplit(line)
            for key in stringsp:
                f.write(var_dict[key]+' ')

            f.write('\n')

        f.write('\n/*Created by Jasoff*/')

    os.remove("temp.cpp")
    os.remove("config.txt")

    print("Done!")


def customsplit(txt):
    # split "context",'context',' ', '\n'

    result = []
    i = 0
    temp = ''
    while i < len(txt):
        if txt[i] == "\"":
            result.append(temp)
            temp = ''

            temp += txt[i]
            i += 1
            while txt[i] != "\"":
                temp += txt[i]
                i += 1
            temp += txt[i]

        elif txt[i] == "\'":
            result.append(temp)
            temp = ''

            temp += txt[i]
            i += 1
            while txt[i] != "\'":
                temp += txt[i]
                i += 1
            temp += txt[i]

        elif txt[i] == " ":
            result.append(temp)
            temp = ''

        elif txt[i] == "\n":
            result.append(temp)
            temp = ''

        else:
            temp += txt[i]

        i += 1

    return result


def hashtag_predeal(file, inputfile):
    hashls = []
    result = []
    with open(file, 'r') as src:
        lines = src.read().splitlines()
    for line in lines:
        if '#' in line:
            hashls.append(line)
        else:
            result.append(line)

    with open(file, 'w') as temp:
        for line in result:
            temp.write(line+'\n')

    ipfile_dic = str(Path(inputfile).parent.resolve())
    with open(ipfile_dic+'\Hot3nCoder.cpp', 'w', encoding='utf-8') as final:
        for line in hashls:
            final.write(line+'\n')


def normalize(file):
    keyword2ls = ['!=', '%=', '&&', '++', '--', '::', '<<', '<=', '==', '>=', '>>']
    keywordls = ['#', '%', '&', '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '[', ']', '{', '}']

    with open(file, 'r') as f:
        src = f.read()

    encodedsrc = []

    i = 0
    while i < len(src):
        temp = src[i:i+2]

        if src[i] == "\"":
            encodedsrc.append(src[i])
            i += 1
            while src[i] != "\"":
                encodedsrc.append(src[i])
                i += 1
            encodedsrc.append(src[i])
            i += 1
            continue

        if src[i] == "\'":
            encodedsrc.append(src[i])
            i += 1
            while src[i] != "\'":
                encodedsrc.append(src[i])
                i += 1
            encodedsrc.append(src[i])
            i += 1
            continue

        if temp in keyword2ls:
            encodedsrc.append(' ')
            encodedsrc.append(temp)
            encodedsrc.append(' ')
            i += 2
            continue

        if src[i] in keywordls:
            encodedsrc.append(' ')
            encodedsrc.append(src[i])
            encodedsrc.append(' ')
            i += 1
            continue

        encodedsrc.append(src[i])
        i += 1

    result = ''.join(encodedsrc)

    return result


def get_encode_slen(dicnum, emojinum):
    return math.ceil(math.log(dicnum, emojinum))


def generate_dic(var_set, emj_ls):
    var_dict = dict.fromkeys(var_set, '')
    count = 0
    for i in var_dict:
        if i == '':
            continue
        var_dict[i] = emj_ls[count]
        count += 1

    return var_dict


def adjust_size():
    with open('config.txt', 'r', encoding='utf-8') as f:
        s = set(f.read().split(' '))
        if '' in s:
            s.remove('')

    stuff = 65
    while len(s) < 3:
        s.add(chr(stuff))
        stuff += 1

    with open('config.txt', 'w', encoding='utf-8') as f:
        for i in s:
            f.write(i+' ')


def get_emoji_size():
    with open('config.txt', 'r', encoding='utf-8') as f:
        temp = set(f.read().split(' '))
        if '' in temp:
            temp.remove('')
    return len(temp)


def get_rand_emoji(length):
    eset = set()
    with open('config.txt', 'r', encoding='utf-8') as f:
        eset = set(f.read().split(' '))
        if '' in eset:
            eset.remove('')

    rest = eset.pop()

    stuff = 65
    while len(eset) < length:
        eset.add(chr(stuff))
        stuff += 1

    half_re = list(product(eset, repeat=length))
    result = []

    for i in half_re:
        word = ''.join(i)+randnum_rest(rest)
        result.append(word)

    return result


def randnum_rest(symbol):
    amount = randint(0, 3)
    s = ""
    for i in range(amount):
        s += symbol

    return s


if __name__ == "__main__":
    main()
