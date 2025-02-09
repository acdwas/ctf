
import ctypes
import time

libsystem = ctypes.CDLL('/lib/x86_64-linux-gnu/libc.so.6')

libsystem.srand.argtypes = [ctypes.c_uint]
libsystem.srand.restype = None

libsystem.rand.argtypes = []
libsystem.rand.restype = ctypes.c_int

def shuffle(a1):
    result = len(a1) - 1
    for i in range(result, -1, -1):
        v3 = libsystem.rand() % (i+1)
        v2 = a1[i]
        a1[i] = a1[v3]
        a1[v3] = v2

def un_shuffle(a1, l):
    for i in range(len(l)):
        v3 = l[i]
        v2 = a1[v3]
        a1[v3] = a1[i]
        a1[i] = v2

time_now = int(time.time())

# w_list_c = list('te s srrn dts  nsyi i ai n rtehdnd h fhyitea raem hve hsre ipos  eacieaxiiiarceoenro  apdtoands tot_ritxeg hlcliof slocnyesseeNesdhesgat htbf,iaisteesO gsat esrctceyoussciagsiul. oyventtmecni  lhri eyapeanlaonsdlselau tv n g eremy-ams sees eso l a at t pee hteratooten gax ssoeofed tm  madininheHftlv_ hen  ,Hecpneanpcns s s ts nt oourecaeeugsgsten  xgr o muishtnr_o g ,tvalel elvleeilatana,rtg th , e ri hpeuy_,eps hneiaA  lts t.Wo n dnebdlptia eapn2TnaerteeEeEWanygmta euliprnlndis.nssutshn ftfadinc.anlpteut h}iasa hoadxatc rhnechrhmr teotpseeeeo tntragaapuo _einewswiar etiah degs d ooeenhni  tee_unllmeee  rr  twoc tylrr re2{tu tfhea ienudmoat ycy mhele, y; rg hcrdtpid_hwm?di  dsaene a d i erte-mltacodoeahmaetss o dosterp')

w_list_p = list('Outer Wilds is an action-adventure video game set in a small planetary system in which the player character, an unnamed space explorer referred to as the Hatchling, explores and investigates its mysteries in a self-directed manner. Whenever the Hatchling dies, the game resets to the beginning; this happens regardless after 22 minutes of gameplay due to the sun going supernova. The player uses these repeated time loops to discover the secrets of the Nomai, an alien species that has left ruins scattered throughout the planetary system, including why the sun is exploding. A downloadable content expansion, Echoes of the Eye, adds additional locations and mysteries to the game. lactf{are_you_ready_to_learn_what_comes_next?}')

w_len = len(w_list_p)

libsystem.srand(1739137009)

for i in range(22):
    shuffle(w_list_p)

print(f'Shuffle\n')

print(''.join(w_list_p))

print(f'\nUn_shuffle\n')

w_list_c = w_list_p

while True:

    # libsystem.srand(time_now)
    libsystem.srand(1739137009)

    list_rand = []
    for j in range(22):
        for i in range(w_len - 1, -1 , -1):
            list_rand.append(libsystem.rand() % (i+1))

    cut_list_rand = []

    for i in range(22):
        cut_list_rand.append(list_rand[i * w_len : w_len + (w_len * i)])

    cut_list_rand = cut_list_rand[::-1]

    copy_w_list = w_list_c[::]
    for i in range(22):
        # shuffle(ww)
        un_shuffle(copy_w_list, cut_list_rand[i][::-1])

    if 'lactf{' in ''.join(copy_w_list):
        print(''.join(copy_w_list))
        print(f'Time srand: {time_now}')
        break

    time_now -= 1

# lactf{are_you_ready_to_learn_what_comes_next?}
