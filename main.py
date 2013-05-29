import os
import random
import string

import benchmark
from Crypto import Random
from Crypto.Cipher import AES, Blowfish
from SimpleAES import SimpleAES


key = os.urandom(16)

padchar = ' '

simpleAES = SimpleAES(key)


def _random_noise(N):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(N))


def _pad_text(plaintext, BS):
    return plaintext + (BS - len(plaintext) % BS) * padchar


def _unpad_text(plaintext):
    return plaintext.rstrip(padchar)


def encrypt_pycrypto_aes(plaintext):
    bs = 16
    iv = os.urandom(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded = _pad_text(plaintext, bs)
    return iv + cipher.encrypt(padded)


def decrypt_pycrypto_aes(encrypted):
    iv = encrypted[:16]
    encrypted = encrypted[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = cipher.decrypt(encrypted)
    plaintext = _unpad_text(decrypted)
    return plaintext


def encrypt_pycrypto_bf(plaintext):
    bs = Blowfish.block_size
    iv = Random.new().read(bs)
    cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)
    padded = _pad_text(plaintext, bs)
    return iv + cipher.encrypt(padded)


def decrypt_pycrypto_bf(encrypted):
    bs = Blowfish.block_size
    iv = encrypted[:bs]
    encrypted = encrypted[bs:]
    cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)
    decrypted = cipher.decrypt(encrypted)
    plaintext = _unpad_text(decrypted)
    return plaintext


class Benchmark_Crypt(benchmark.Benchmark):
    each = 10

    def setUp(self):
        self.input_text = []
        for input_len in xrange(5, 1040, 5):
            for times in xrange(3):
                plain_text = _random_noise(input_len)
                self.input_text.append(plain_text)

    def test_simpleaes(self):
        for text in self.input_text:
            encrypted = simpleAES.encrypt(text)
            decrypted = simpleAES.decrypt(encrypted)
            assert text == decrypted

    def test_pycrypto_aes(self):
        for text in self.input_text:
            encrypted = encrypt_pycrypto_aes(text)
            decrypted = decrypt_pycrypto_aes(encrypted)
            assert text == decrypted

    def test_pycrypto_blowfish(self):
        for text in self.input_text:
            encrypted = encrypt_pycrypto_bf(text)
            decrypted = decrypt_pycrypto_bf(encrypted)
            if text != decrypted:
                print 'plaintext >{0}< ({1})'.format(text, len(text))
                print 'decrypted >{0}< ({1})'.format(decrypted, len(decrypted))
            assert text == decrypted


    #def test_pycrypto_blowfish(self):
    #    for text in self.input_text:
    #        encrypted = cryptoBF.encrypt(_pad_text_aes(text, bs_bs))
    #        decrypted = cryptoBF.decrypt(encrypted)
    #        print '>{}<'.format(text)
    #        print '>{}<'.format(decrypted)
    #        #assert text == decrypted


if __name__ == '__main__':
    benchmark.main(format="markdown", numberFormat="%.4g")
    # could have written benchmark.main(each=50) if the
    # first class shouldn't have been run 100 times.
