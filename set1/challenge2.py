buffer1="1c0111001f010100061a024b53535009181c"
buffer2="686974207468652062756c6c277320657965"
barr1=bytearray.fromhex(buffer1)
barr2=bytearray.fromhex(buffer2)

# For Loop Version
#output=""
#for i, _ in enumerate(barr1):
#    output += format(barr1[i] ^ barr2[i], 'x')

# One liner
output = ''.join([format(barr1[i] ^ barr2[i], 'x') for i, _ in enumerate(barr1)])

print(output)
