from Crypto.Cipher import AES
from hashlib import sha256
from sage.all import *

x = -74337111560408261770627327061677963299443114676921962193623077431929781105956693046458392735870264364007813650987534298743547687856228598375660321312737669922256322002836807209358272704779543549572555337507638951640423224736617988565507790110400638507902597678361464029732843617458061469432050977431403357467
y = 80004460393622006505206154227738652408980554199718416840470313398850884843675954680175518476630032820510826586724696390191570583297462980502959681243903214031598679172479920755464717427554287271300097926852452366085494286842499533040579721141160507448286612025375713562688645031383081188938949474253051185921
ct = b'\x9e\xae\\|\x80\xe9\x0br\xa9\xc1o8\x08\xdcy\xbf\x94\x97\x85\xdc\xbf\x94\xe2\xd7\x82\x8f\x81>\xf2\x1fl@+\x85\xe6\xd2}N\xcb\x12Ak\xfb\xc1\xbf\x88\'i</"\xf5\x01+4\x1aF\xb6\xf6\xdce!L\x9a'

H = 2 ** 2048
M = matrix(ZZ,[
    [x,1,0],
    [y,0,1],
])
M[:,0] *= H

r = M.LLL()[0]
# r = (0, a, b)
a = r[1]
b = r[2]

aes = AES.new(sha256(f'{a}||{b}'.encode()).digest(), AES.MODE_CBC, iv=bytes(16))
ct = aes.decrypt(ct)
print(f'{ct = }')