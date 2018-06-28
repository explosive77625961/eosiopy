# -*- coding: utf-8 -*-
# @Time    : 2018/6/26 17:01
# @Author  : Aries
# @Site    : 
# @File    : s.py
# @Software: PyCharm

# from distutils.core import setup, Extension
#
# module1 = Extension('rmd160',
#                     sources = ['rmd160.c'])
#
# setup(name = 'rmd160',
#     version = '1.0',
#     description = 'This is a Math package',
#     ext_modules= [module1])

# import ecc
from ecc.ecdsa import sign, keypair

if __name__ == '__main__':
    a = bytearray.fromhex('abbf4f282f57faf2d9817993bf5dfb7aae8805c6a9ed23f598a0c10905010a0b')
    b = bytearray.fromhex('8164be491093d7904de0b62b1cb2724d8546f7be19ac749a5a18785ee77641b7')
    c = '506896f7f6043316cb1d0b7795081dbfdbebbebe9fef1050247028f5914243a0019bd87033fea6f8ffadaea6985bb09127977a7b56f31d5dcfd74d7f6579c1d3'

    # print(keypair('8164be491093d7904de0b62b1cb2724d8546f7be19ac749a5a18785ee77641b7'))
    dk = (256, 95164591246607201828665211148860865940778311286669259514084724528599702368381L)
    d = 0xb2fdafb377e63a3dcaea66645e772949324101d1074e1fd3256265d02a6da429

    f = sign(d, dk)[1]
    print(f)
    j = hex(f)
    print(j)
    h = bytearray('1d2b92b3f17be1f4de5d68ad501a3402fe0278c167847dbc2567444639aea1a4')
    print(list(h))