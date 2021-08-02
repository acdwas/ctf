
def generate():
    v1 = 1
    list_2495 = [2]
    v2 = 3
    while v1 <= 6000:
        v3 = 1
        for i in range(len(list_2495)):
            if v2 % list_2495[i] == 0:
                v3 = 0
        if v3:
            list_2495.append(v2)
        v2 += 2
        v1 += 1
    return list_2495

buf = generate()

l = list('azeupqd_ftq_cgqefuaz_omz_ymotuzqe_ftuzwu_bdabaeq_fa_o')

for i in range(1336, -1, -1):
    w = ''
    for j in range(len(l)):
        w += l[(j - buf[i]) % len(l)]
    
    v5 = len(l)
    j = 0
    while True:
        if j >= v5:
            break
        v3 = ord(w[j])
        if v3 != 95:
            v3 = (v3 - 97 - buf[i]) % 26 + 97
        w = list(w)
        w[j] = chr(v3)
        j += 1
    l = list(w)

print('Uncipher: ' + ''.join(w))

l = list('i_propose_to_consider_the_question_can_machines_think')

for i in range(1337):
   
    v5 = len(l)
    j = 0
    while True:
        if j >= v5:
            break
        v3 = ord(l[j])
        if v3 != 95:
            v3 = (v3 - 97 + buf[i]) % 26 + 97
        l[j] = chr(v3)
        j += 1

    w = ''
    for j in range(len(l)):
        w += l[(j + buf[i]) % len(l)]

    l = list(w)

print('Cipher:   ' + ''.join(w))

# uiuctf{i_propose_to_consider_the_question_can_machines_think}
