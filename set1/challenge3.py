#!/usr/bin/python3

import functools
import sys


class XorAnalyzer:
    def __init__(self, subject):
        self.subject = subject
        self.results = []

    def analyze(self):

        def characterAnalysis(coll, byte):
            character_frequencies = {
                    'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253,
                    'e': .12702, 'f': .02228, 'g': .02015, 'h': .06094,
                    'i': .06094, 'j': .00153, 'k': .00772, 'l': .04025,
                    'm': .02406, 'n': .06749, 'o': .07507, 'p': .01929,
                    'q': .00095, 'r': .05987, 's': .06327, 't': .09056,
                    'u': .02758, 'v': .00978, 'w': .02360, 'x': .00150,
                    'y': .01974, 'z': .00074, ' ': .13000
                    }
            # If its a printable character, increment printable count
            #if byte > 0x41 and byte < 0x7a:
            #    coll += 1

            # If its a space, give it an extra point
            #if byte == 0x20:
            #    coll += 1
            coll += character_frequencies.get(chr(byte), 0)
            return coll

        # Try each possible byte as a possible XOR value
        for char in range(256):
            output=""
            output_bytes=[]

            # for each byte in the ciphertext
            for byte in self.subject.lower():
                # Convert the integer to the corresponding ascii character, and then its
                # hexidecimal byte representation
                guess = bytes(chr(char), 'utf-8')[0]
                # Now that we're have all values as bytes, perform the xor
                decoded = guess ^ byte
                # Adding the decoded value to an array of bytes
                output_bytes.append(decoded)
                # And the decoded value converted to a string character and appended to
                # an output string
                output += chr(decoded)

            # Perform an analysis on the xor'd bytes and calculate a score
            score = functools.reduce(characterAnalysis, output_bytes, 0)
            # Create a tuple containing the score, the guessed character as hex, and the
            # output string
            self.results.append([score, hex(guess), output])

        self.results.sort()


def main() -> int:
    encoded="1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    barr1=bytearray.fromhex(encoded)
    xa = XorAnalyzer(barr1)
    xa.analyze()
    i = len(xa.results)-1
    print(f'Score: {xa.results[i][0]} Character: {xa.results[i][1]} Decoded: {xa.results[i][2]}')

    return 0

if __name__ == '__main__':
    sys.exit(main())
