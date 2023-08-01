import base64

with open("files/key_for_rsa_public.hash", "rb") as f:
    key = f.read()

decoded = base64.b64decode(key)

with open("files/key_for_rsa_public.dec", "w") as f:
    f.write(decoded.hex())