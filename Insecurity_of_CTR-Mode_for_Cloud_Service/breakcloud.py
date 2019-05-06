from cloud import *

def bytes_xor(s1, s2):
    return ''.join(chr(ord(c1) ^ ord(c2)) for c1,c2 in zip(s1,s2))

def breakcloud(cloud):
    old_ct = ""
    aes_output = ""
    i = 0
    curr_byte = cloud.Write(i, '\x00')
    while curr_byte != None:
        old_ct += curr_byte
        aes_output += cloud.Read(i)
        i += 1
        curr_byte = cloud.Write(i, '\x00')
    xor = bytes_xor(old_ct, aes_output)
    with open("plain.txt", mode='wb+') as file:
        file.write(xor)