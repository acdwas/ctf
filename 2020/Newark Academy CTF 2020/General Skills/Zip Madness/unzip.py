
from zipfile import ZipFile
import glob
import os

while True:
    l = glob.glob("*")
    if 'flag.txt' in l:
        with open('flag.txt') as f:
            print(f.read())
        break
    if 'direction.txt' in l:
        with open('direction.txt') as f:
            s = f.read()
        f.close()
    for i in range(len(l)):
        if s in l[i]:
            break

    with ZipFile(l[i], 'r') as zipObj:
        zipObj.extractall()
    zipObj.close()

    for i in l:
        if 'unzip.py' == i or 'direction.txt' == i:
            pass
        else:
            os.remove(i)

# nactf{1_h0pe_y0u_d1dnt_d0_th4t_by_h4nd_87ce45b0}
