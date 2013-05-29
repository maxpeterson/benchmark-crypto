# Encryption benchmark

Quick and simple test case to benchmark different encryption / decryption methods.

Initial version compares pycrypto==2.6 and SimpleAES==1.0.

Run `python main.py`

## Results

             name | rank | runs |    mean |       sd | timesBaseline
------------------|------|------|---------|----------|--------------
     pycrypto aes |    1 |   10 | 0.02799 | 0.004236 |           1.0
pycrypto blowfish |    2 |   10 |  0.1362 |  0.01185 | 4.86693156086
        simpleaes |    3 |   10 |   6.488 |    0.228 | 231.818900462

Each of the above 30 runs were run in random, non-consecutive order by
`benchmark` v0.1.5 (http://jspi.es/benchmark) with Python 2.7.2
Darwin-12.3.0-x86_64 on 2013-05-29 09:47:26.
