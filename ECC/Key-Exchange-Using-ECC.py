from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization

# Generate private key for Alice
alice_private_key = ec.generate_private_key(ec.SECP256R1())
alice_public_key = alice_private_key.public_key()

# Generate private key for Bob
bob_private_key = ec.generate_private_key(ec.SECP256R1())
bob_public_key = bob_private_key.public_key()

# Exchange public keys and compute shared secret
alice_shared_key = alice_private_key.exchange(ec.ECDH(), bob_public_key)
bob_shared_key = bob_private_key.exchange(ec.ECDH(), alice_public_key)

print("Shared keys match:", alice_shared_key == bob_shared_key)
