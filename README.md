# Encryption benchmark

Quick and simple test case to benchmark different encryption / decryption methods.

Initial version compares pycrypto and simpleaes.

Run `python main.py`

## Results

             name | rank | runs |      mean |        sd | timesBaseline
------------------|------|------|-----------|-----------|--------------
 pycrypto decrypt |    1 |   10 | 0.0009424 | 0.0003011 |           1.0
 pycrypto encrypt |    2 |   10 |  0.001077 | 0.0003112 | 1.14230778961
simpleaes decrypt |    3 |   10 |     1.853 |   0.07136 | 1965.98666734
simpleaes encrypt |    4 |   10 |     1.927 |    0.1027 | 2044.99840615

Each of the above 40 runs were run in random, non-consecutive order by
`benchmark` v0.1.5 (http://jspi.es/benchmark) with Python 2.7.2
Darwin-12.3.0-x86_64 on 2013-05-28 20:31:46.
