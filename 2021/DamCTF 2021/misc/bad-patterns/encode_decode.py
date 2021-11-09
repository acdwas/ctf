
orginal = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

l = 'Lpthq jrvym!frpos"vmt!cpit-"fsntgfxeuwu$aeksmsdkqk fnlx,!uhh eq#iivupsd!vhqppt#mndkgmdvpw$uu"oebpth$eu"gslpth$mbiqe bnluub0#Yt!gqmm!cg$mjplq wgqman.#uuju#rotvuyd!g{irdkwetjqq$umndqcp"oebptlw okvm vv#eljsxmp!g{$eb"fsmnqgs dqqwerwdx.!Fxms!cxxe!kuyrf"gslpt#mn!thtrfjhrdftlx jp#zomwsxaug#zemkw$etuh$cjnoym!frposg#iu!hxkibv#rumnd$pbtletvt1$Eyehttfwu$sjpw$odedicbv#guqkgetbv#roo"svojfhrt-"vynu"lr dwota!sxm phimcjc#hetguynu"pslmkw$aokp$ie"hwt!ndfoswp2'

def decode(l):
    w = ''
    x = 0
    for i in range(len(l)):
        if x == 5:
            w += l[i]
            x = 1
            continue
        if l[i] in 'abcdefghijklmnopqrstuvwxyz':
            w += chr(ord(l[i]) - x)
            x += 1
        elif l[i] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            w += chr(ord(l[i]) - x)
            x += 1
        else:
            w += chr(ord(l[i]) - x)
            x += 1
    return w

def encode(l):
    w = ''
    x = 0
    for i in range(len(l)):
        if x == 5:
            w += l[i]
            x = 1
            continue
        if l[i] in 'abcdefghijklmnopqrstuvwxyz':
            w += chr(ord(l[i]) + x)
            x += 1
        elif l[i] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            w += chr(ord(l[i]) + x)
            x += 1
        else:
            w += chr(ord(l[i]) + x)
            x += 1

    return w


print(l == encode(orginal))
print("bagelarenotwholewheatsometimes" == decode(encode("bagelarenotwholewheatsometimes")))

