###
###
import time
import argparse
from Crypto.Cipher import AES
from http.server import BaseHTTPRequestHandler
FLAG = [0x34]*8 

def decode_str(zz:str):
    dd = list()
    zz = bytes.fromhex(zz)
    p = "pwntools"
    for indx, c in enumerate(zz):
        dd.append(chr(c^ord(p[(indx % 8)])))
    return ''.join(dd).encode('utf-8')

def wekfgwef():
     global FLAG
     
     noise203642="061119973240928"

     noise203643="0611asd1132967"
     
     noise203644="061asdfaswe23401998"
     aelwfuhweiuweiuf = "041e03111b000e1c1f1007115d5f5e40"
     noise203647="aa808027ccd93003e7f73f87aa84600e"
     aelwfuhweiuweiuf=decode_str(aelwfuhweiuweiuf)
     #print(type(aelwfuhweiuweiuf), key)
     #aelwfuhweiuweiuf= b'timetoboogie2023'
     iv= b'abcdefghijklmnop'
     noise203645="0623403940-[dksfnsdf101976"
     noise203646="9eddbb37aa44ce45d6ff322fd3dc6db5"
     noise203648="060wefwef71986"
     
     ciphertext= bytes.fromhex('baa012f603755dfd5dc7970b50ebeafc')
     cipher = AES.new(aelwfuhweiuweiuf, AES.MODE_CBC , iv=iv)
     plain_text = cipher.decrypt(ciphertext).decode('utf-8')[:8]
     #print(len(plain_text),plain_text)
     FLAG= plain_text

def compare_input(usr_input:str, flag:list) -> None:
    result= 1
    if len(usr_input) != len(flag):
        print("Please ensure user input is 8 characters long and only printable numbers 0-9.")
        return 0
    for pos,char in enumerate(usr_input):
        result= ord(char) ^ flag[pos]
    return result

def compare_input1(usr_input:str, flag:str) -> None:
    if len(usr_input) != len(flag):
        print("Please ensure user input is 8 characters long and only printable numbers 0-9.")
        return -1
    for pos,char in enumerate(usr_input):
        if ord(char) != ord(flag[pos]):
        #    print(ord(char), ord(flag[pos]))
            return False
        else:
            time.sleep(0.15) 
    return True    

def set_up():
    parser = argparse.ArgumentParser(prog="Example",description="This Program compares user input and decrypts the secret flag. Example: python3.10 chall.pyc -i 00000000 -m 0", epilog="Python is an interpreted language and uses an intermediate language.")
    parser.add_argument('-i','--input', required=True, help="user input that is only printable numbers 0-9.")
    parser.add_argument('-m','--mode',required=True,type=int, help="Mode 0 returns the last value of the input. Mode 1 compares character by character when checking the user input")
    return parser


if __name__ == "__main__":
    parser = set_up()
    wekfgwef()
    all_flags = parser.parse_args()
    if all_flags.mode == 0:
        res=compare_input(all_flags.input, FLAG)
        print(res)
    else:
        res=compare_input1(all_flags.input, FLAG)        
        print(res)
