import ctypes
import hashlib
from ctypes import *

import base58
import pkg_resources
from ecdsa import SigningKey, SECP256k1

from eosiopy.exception import CantFindRecId
from eosiopy.exception import IllegalKey




def get_private_ket_by_wif(wif):
    eos_byte_array = bytearray(base58.b58decode(wif))
    if eos_byte_array[0] != 0x80:
        raise IllegalKey()
    hex_bytea_array = eos_byte_array[1:33]
    return hex_bytea_array


def sign(wfi, trx):
    pri = get_private_ket_by_wif(wfi)

    pri = bytes(pri)

    bin = bytearray()
    binlen = 65 + 4

    sk = SigningKey.from_string(pri, curve=SECP256k1, hashfunc=hashlib.sha256)
    g = trx
    print(g)
    signature = sk.sign(data=g, hashfunc=hashlib.sha256)
    print(len(bytearray(signature)))
    print(signature)

    recId = (ord(bytearray(signature)[0]) - 27) & 3

    c = bytearray(signature)[0] - 27
    c = c & 4
    if c:
        recId += 4
    recId += 27

    headerBytes = recId
    bin.append(headerBytes)
    bin.extend(bytearray(signature))
    temp = bytearray()
    temp.extend(bin[0:65])
    temp.append(75)
    temp.append(49)


    rmd160 = hashlib.new("rmd160")
    rmd160.update(temp)
    bin.extend(rmd160.digest())

    sig = str(base58.b58encode(bytes(bin)))[2:-1]
    sig = "SIG_K1_" + sig
    return sig
