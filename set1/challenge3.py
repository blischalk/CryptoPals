import functools

encoded="1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
barr1=bytearray.fromhex(encoded)

def characterAnalysis(coll, byte):
    # If its a printable character, increment printable count
    if byte > 0x41 and byte < 0x7a:
        coll += 1

    # If its a space, give it an extra point
    if byte == 0x20:
        coll += 1

    return coll

results=[]

# Try each possible byte as a possible XOR value
char=0
while char <= 255:
    output=""
    output_bytes=[]

    # for each byte in the ciphertext
    for byte in barr1:
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
    results.append([score, hex(guess), output])

    char += 1

results.sort()

for result in results:
    print(f'Score: {result[0]} Character: {result[1]} Decoded: {result[2]}')


