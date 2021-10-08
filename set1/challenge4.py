#!/usr/bin/python3

from challenge3 import XorAnalyzer

f = open("4.txt", "r")

best_results=[]
for line in f:
    barr=bytearray.fromhex(line)
    xa = XorAnalyzer(barr)
    xa.analyze()
    i = len(xa.results)-1
    best_results.append(xa.results[i])

best_results.sort(reverse=True)
print(best_results[0])
print(f'Score: {best_results[0][0]} Character: {best_results[0][1]} Decoded: {best_results[0][2]}')
f.close()
