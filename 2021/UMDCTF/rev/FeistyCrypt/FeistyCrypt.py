
from z3 import *

s = Solver()

a = [BitVec('a{}'.format(i), 8) for i in range(32)]

l = [0x23fd5e89, 0x5b2261af, 0x2fe1beff, 0x5639c8b3, 0x055db46f, 0x06c72ec1, 0x5c3075ca,
     0x292db8ab, 0x41198ff2, 0x64317860, 0x56b49da4, 0x4184f32c, 0x62007c3b, 0x43dadc7c,
     0x7522e0c0, 0x6d7f9573, 0x2a22ed32, 0x382e0d39, 0x71fc8b4f, 0x0261ce41, 0x136edd56,
     0x137a86ce, 0x407d887a, 0x2b90757d, 0x77b52f05, 0x676937cb, 0x26a3dc5e, 0x64b29390,
     0x78c00ddb, 0x28dfacc6, 0x691c3744, 0x1b86b44f, 0x68c94ada, 0x3ff7330d, 0x2086ad97,
     0x4883547d, 0x71f066e7, 0x7394a4d9, 0x1bfa3ccf, 0x67e98cb6, 0x140971f5, 0x779c6fee, 
     0x187d9e70, 0x6bfc76e9, 0x0db407b6, 0x59b1a815, 0x21543363, 0x1ac7824e, 0x6ead0fb1, 
     0x1653b8a9, 0x03dd45f6, 0x113e5eff, 0x6d89001b, 0x68abea02, 0x78b81fef, 0x666f2f50,
     0x57af0fc2, 0x6bfbec39, 0x0de762d8, 0x04f360c2, 0x2ad69155, 0x74326af5, 0x43723f1a, 
     0x5de93d42, 0x6d534483, 0x04cfacfa, 0x5ba32576, 0x0dbf4ac9, 0x505bd98d, 0x25e58465,
     0x450e55dd, 0x0eda33f4, 0x11ee20d8, 0x61340d9e, 0x1e72fd16, 0x29484e9b, 0x42a58fab,
     0x20941cb3, 0x680a4ca1, 0x2950ab13, 0x52d1a096, 0x3774533b, 0x3b9987fb, 0x74f739da,
     0x4625d2a5, 0x3cd379d0, 0x3d80b811, 0x7013c78b, 0x0a68ad9b, 0x74dfcb56, 0x56762842,
     0x12405e6a, 0x0477f8a6, 0x336c4fe0, 0x7a5a3b66, 0x3a0246bd, 0x765d0f54, 0x7b9af87d,
     0x7405cde8, 0x61beae87, 0x32223ff4, 0x43d86afd, 0x1304e42c, 0x4ca72e7e, 0x23c87d96,
     0x15e67802, 0x4d4740b2, 0x6b0af4b1, 0x21c5c4ba, 0x7ef7b118, 0x0c023fe5, 0x4df209ae,
     0x79bd474f, 0x0dab7f41, 0x70551b15, 0x68552e29, 0x4f4fac4e, 0x20b8b2bf, 0x60b97860,
     0x1c88e618, 0x1beba0b5, 0x393f26a7, 0x3fdc3997, 0x3ba169a1, 0x00c28fe7, 0x08a01788,
     0x027bbbeb, 0x1fed911c, 0x3a039c20, 0x366a6cba, 0x1c3d2083, 0x1557a297, 0x79225613,
     0x724264bb, 0x6dd81aeb, 0x251955a8, 0x09168c1f, 0x7b346b10, 0x0103442d, 0x39ba64c8,
     0x64ac5ba7, 0x02b46aaa, 0x7f3254c0, 0x7d9e3ec0, 0x3b3a9491, 0x3d76232c, 0x53ffb65f,
     0x27e611e8, 0x3abf8a2f, 0x58ef8f13, 0x2eb74a4a, 0x0c161ec1, 0x21d6041f, 0x7e1b1105,
     0x567efdeb, 0x7c35eecf, 0x65c94361, 0x38d7b0c4, 0x6d9b74b3, 0x0ce9d485, 0x7b332ea6,
     0x6ac6d4dd, 0x2db54bc0, 0x0a48240d, 0x33825e57, 0x16180294, 0x60155387, 0x4f71fc30,
     0x55766ca3, 0x4e7e45e8, 0x083a5b37, 0x453a20c9, 0x604054cc, 0x0dfa79a8, 0x6278c591,
     0x4d38eaa5, 0x1d1c1af9, 0x52709b38, 0x0d9891b5, 0x5deecdb1, 0x76c7abf0, 0x61b1c4e3,
     0x58a22c33, 0x40c7ff21, 0x134979d7, 0x580b9029, 0x428ae425, 0x06033889, 0x7fc31dc1,
     0x3ab7b92c, 0x129a917d, 0x0ee37fb2, 0x002e98eb, 0x528afd7b, 0x7c3c2714, 0x6f3857eb,
     0x40d48d39, 0x2dc13029, 0x2bd24d7d, 0x7553d9e9, 0x2d5e9a50, 0x2408d01d, 0x3c1238bc,
     0x332cb98b, 0x745ee111, 0x28ac04e4, 0x43f757b3, 0x2d34c20d, 0x2573fd2f, 0x60fd1290,
     0x21596a8f, 0x20dadc3e, 0x2117fe1e, 0x1273a3b4, 0x5c710dff, 0x7905c80e, 0x5dd5d44e,
     0x4fd665b0, 0x1942323b, 0x46f421ed, 0x60c5c3c4, 0x10d40898, 0x5fc642ab, 0x7c201248,
     0x61764c25, 0x6401497d, 0x1e85f88e, 0x64502c64, 0x090da24d, 0x0c718924, 0x0b2d579f,
     0x6a6d82ec, 0x72902f96, 0x05ef7679, 0x10d156e8, 0x36a89aee, 0x69f1a459, 0x662ce4f8,
     0x5d7a8d28, 0x3fe21e01, 0x4c95b18e, 0x327fc3f5, 0x5093ba58, 0x320cfd69, 0x7ca511fa,
     0x4e3e518b, 0x2b77f722, 0x63d49291, 0x57b42564, 0x64022fa5, 0x238fb5e9, 0x7725ec84,
     0x312bad71, 0x10b70c12, 0x430643a8, 0x5861d29e ]


pas = [ 0x570B750B, 0x0C583369, 
	0x6B663437, 0x7F6D4C33, 
	0x2B636571, 0x64695877, 
	0x782D7E79, 0x2A0B167F ]

for i in range(32):
	s.add(a[i] > 0x20, a[i] < 0x7f)

tab = []

for i in range(0,32,8):
	v3 = Concat(a[4+i], a[5+i], a[6+i], a[7+i])
	v2 = Concat(a[0+i], a[1+i], a[2+i], a[3+i])
	for i in range(0xFF+1):
		v5 = v2 ^ (l[i] & v3 ^ 0xBA5EBA11)
		if i == 255:
			v6 = v3
			v3 = v5
			v5 = v6
		v2 = v3
		v3 = v5
	tab.append((v2,v3))

xx = 0
for i in range(0,8,2):
	s.add(tab[xx][0] == pas[i])
	s.add(tab[xx][1] == pas[i+1])
	xx += 1

s.check()
m = s.model()

w = ''
for i in range(32):
	w += chr(m[a[i]].as_long())
print(w)

# UMDCTF-{h0r57_f31573l_wuz_h3r3.}