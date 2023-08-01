from Crypto.PublicKey import RSA
import gmpy2

with open('raw/public.key', 'r') as f:
    key = RSA.importKey(f.read())

N = key.n
e = key.e
p = 4738700273445489960492041313631971343000359635005034483771
q = 4988586550946572698837659323141005331783499412890195822279
d = int(gmpy2.invert(e,(p - 1) * (q - 1)))
rsa_private_key = RSA.construct((N, e, d))

with open('raw/private.key', 'wb') as f:
    f.write(rsa_private_key.exportKey('PEM'))