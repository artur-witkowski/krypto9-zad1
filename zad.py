import os
import time
from stegano import lsb, lsbset
from stegano.lsbset import generators
import random
import string


def getRandomString(N):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))

# LSB method


def testLSB(chars, folder):
    print('=====')
    print(f'LSB - {chars} znakow - rozmiar ~{folder}')
    start = time.time()
    secret = lsb.hide(f'./{folder}/source.png', getRandomString(chars))
    end = time.time()
    print(f'Czas szyfrowania: {str(round(end - start, 2))}s')
    start = time.time()
    secret.save(f'./{folder}/lsb-{chars}chars.png')
    end = time.time()
    print(f'Czas odszyfrowania: {str(round(end - start, 2))}s')
    file_name = f'./{folder}/source.png'
    file_stats = os.stat(file_name)
    print(
        f'Rozmiar przed: {str(round(file_stats.st_size / (1024 * 1024), 2))}MB')
    file_name = f'./{folder}/lsb-{chars}chars.png'
    file_stats = os.stat(file_name)
    print(f'Rozmiar po: {str(round(file_stats.st_size / (1024 * 1024), 2))}MB')

# LSB method with sets


def testLSBwithSets(chars, folder, generator, genName):
    print('=====')
    print(f'LSB with sets - {chars} znakow - rozmiar ~{folder}')
    print(f'Using "{genName}" generator')
    start = time.time()
    secret_image = lsbset.hide(f'./{folder}/source.png',
                               getRandomString(chars),
                               generator)
    end = time.time()
    print(f'Czas szyfrowania: {str(round(end - start, 2))}s')
    start = time.time()
    secret_image.save(f'./{folder}/lsbset-{chars}chars.png')
    end = time.time()
    print(f'Czas odszyfrowania: {str(round(end - start, 2))}s')
    file_name = f'./{folder}/source.png'
    file_stats = os.stat(file_name)
    print(
        f'Rozmiar przed: {str(round(file_stats.st_size / (1024 * 1024), 2))}MB')
    file_name = f'./{folder}/lsbset-{chars}chars.png'
    file_stats = os.stat(file_name)
    print(f'Rozmiar po: {str(round(file_stats.st_size / (1024 * 1024), 2))}MB')


testLSB(100, '500KB')
testLSB(1000, '500KB')
testLSB(10000, '500KB')
testLSB(100000, '500KB')
testLSB(200000, '500KB')

testLSB(100, '5MB')
testLSB(1000, '5MB')
testLSB(10000, '5MB')
testLSB(100000, '5MB')
testLSB(200000, '5MB')

testLSB(100, '17MB')
testLSB(1000, '17MB')
testLSB(10000, '17MB')
testLSB(100000, '17MB')
testLSB(200000, '17MB')

testLSBwithSets(100, '500KB', generators.eratosthenes(), 'eratosthenes')
testLSBwithSets(100, '500KB', generators.eratosthenes(), 'eratosthenes')
testLSBwithSets(1000, '500KB', generators.eratosthenes(), 'eratosthenes')
testLSBwithSets(10000, '500KB', generators.eratosthenes(), 'eratosthenes')
testLSBwithSets(100000, '500KB', generators.eratosthenes(), 'eratosthenes')
testLSBwithSets(200000, '500KB', generators.eratosthenes(), 'eratosthenes')

testLSBwithSets(100, '5MB', generators.eratosthenes(), 'eratosthenes')
testLSBwithSets(1000, '5MB', generators.eratosthenes(), 'eratosthenes')
testLSBwithSets(10000, '5MB', generators.eratosthenes(), 'eratosthenes')
testLSBwithSets(100000, '5MB', generators.eratosthenes(), 'eratosthenes')
testLSBwithSets(200000, '5MB', generators.eratosthenes(), 'eratosthenes')

testLSBwithSets(100, '17MB', generators.eratosthenes(), 'eratosthenes')
testLSBwithSets(1000, '17MB', generators.eratosthenes(), 'eratosthenes')
testLSBwithSets(10000, '17MB', generators.eratosthenes(), 'eratosthenes')
testLSBwithSets(100000, '17MB', generators.eratosthenes(), 'eratosthenes')
testLSBwithSets(200000, '17MB', generators.eratosthenes(), 'eratosthenes')