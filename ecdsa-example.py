from ecdsa import SigningKey, SECP256k1

sk = SigningKey.generate(curve=SECP256k1)
vk = sk.verifying_key

print("Signing Key : ", sk)
print("Verifying Key : ", vk)

signature = sk.sign(b"Not your keys, not your coins!")

print("Signature : ", signature)

assert vk.verify(signature, b"Not your keys, not your coins!")

print("Message Verified!")
