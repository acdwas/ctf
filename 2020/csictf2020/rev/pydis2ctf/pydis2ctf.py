
def C1cipher(text):
    ret_text = ''
    for i in list(text):
        counter = text.count(i)
        ret_text += chr(2*ord(i) - len(text))
    return ret_text

def C2cipher(inpString):
    xorKey = 'S'
    length = len(inpString)
    for i in range(length):
        inpString = inpString[:i] + chr(ord(inpString[i]) ^ ord(xorKey)) + inpString[i+1:]
    return inpString


def decode(text):
    ret_text = ''
    for i in list(text):
        ret_text += chr((ord(i)+len(text))//2)
    return ret_text

l = '¤Ä°¤ÆªÔ\x86$\xa04\x9cÌ`H\x9c¬>¼f\x9c¦@HH\xa0\x84¨\x9a\x9a¢vÐØ'

print(decode(l))
