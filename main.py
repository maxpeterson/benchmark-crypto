import os
import random

import benchmark
from Crypto.Cipher import AES
from SimpleAES import SimpleAES


SECRET_KEY = os.urandom(16)
IV = os.urandom(16)

simpleAES = SimpleAES(SECRET_KEY)
cryptoAES = AES.new(SECRET_KEY, AES.MODE_CBC, IV)
BLOCK_SIZE = 16
PADDING = '{'

def _random_noise(len):
    return ''.join(chr(random.randint(0, 0xFF)) for i in range(len))

def _pad_text(s, block_size, padding):
    return s + (block_size - len(s) % block_size) * padding


class Benchmark_Crypt(benchmark.Benchmark):

    each = 10 # allows for differing number of runs

    def setUp(self):
        self.input_text = []
        self.simple_aes_encrypted_text = []
        self.crypto_aes_encrypted_text = []
        for input_len in xrange(128):
            for times in xrange(3):
                plain_text = _random_noise(input_len)
                self.input_text.append(plain_text)
                self.simple_aes_encrypted_text.append(
                    simpleAES.encrypt(plain_text)
                )
                self.crypto_aes_encrypted_text.append(
                    cryptoAES.encrypt(_pad_text(plain_text, BLOCK_SIZE, PADDING))
                )

    def test_simple_aes_encrypt(self):
        for text in self.input_text:
            simpleAES.encrypt(text)

    def test_simple_aes_decrypt(self):
        for text in self.simple_aes_encrypted_text:
            simpleAES.decrypt(text)

    def test_simple_crypto_encrypt(self):
        for text in self.input_text:
            cryptoAES.encrypt(_pad_text(text, BLOCK_SIZE, PADDING))

    def test_simple_crypto_decrypt(self):
        for text in self.crypto_aes_encrypted_text:
            cryptoAES.decrypt(text).rstrip(PADDING)


if __name__ == '__main__':
    benchmark.main(format="markdown", numberFormat="%.4g")
    # could have written benchmark.main(each=50) if the
    # first class shouldn't have been run 100 times.
