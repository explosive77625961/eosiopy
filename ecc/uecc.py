if __name__ == '__main__':
    from .src.ecdsa import SigningKey

    sk = SigningKey.generate()  # uses NIST192p
    vk = sk.get_verifying_key()
    signature = sk.sign("message")
    assert vk.verify(signature, "message")