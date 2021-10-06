hex_string="49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

def hexStrToBits(hexstring):
    # Convert string of hexadecimal digits to a byte array
    hex_bytes=bytearray.fromhex(hex_string)
    digits=[]
    for byte in hex_bytes:
        # Create a string representation of the 1's and 0's of the
        # Binary octet of the byte
        binary_string = format(byte, '08b')
        # Break the binary octet string into component 1's and 0's
        # And append to a list
        for digit in binary_string:
            digits.append(digit)
    return digits

def bitsToInt(sextet):
    out=0
    for bit in sextet:
        # Shift the least significant bit to the left
        # Flip the new least significant bit to the bit in the sextet
        out = (out << 1) | bit
    return out

def bitsToBase64(bits):
    lookup = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
            'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b',
            'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3',
            '4', '5', '6', '7', '8', '9', '+', '/']
    base64string = ""
    sextet = []
    # Create a list containing a sextet, e.g. 6 bits
    for count, digit in enumerate(bits):
        sextet.append(int(digit))
        # If we don't have a remainder, we are on to the next sextet
        if (count+1) % 6 == 0:
            # So lookup the character representation in the Base64 character
            # lookup table, appending the character to the output string
            base64string += lookup[bitsToInt(sextet)]
            # And clear out the sextet list for the next iteration
            sextet=[]
        # If we run out of bits and the sextet wasn't flushed
        if (count+1) == len(bits) and len(sextet) != 0:
            # Pad the sextet list with zeros
            while len(sextet) <= 6:
                sextet.append(0)
            # And lookup the character representation in the Base64 character
            # lookup table, appending the character to the output string
            base64string += lookup[bitsToInt(sextet)]

            # Output string must be a multiple of 4 so if its not...
            if len(base64string) % 4 != 0:
                # And we have 2 dangling characters, we pad with two =
                # To make a multiple of 4
                if len(base64string) % 4 == 2:
                    base64string += "=="
                else:
                    # If we have 3 dangling characters, we pad with one =
                    # There isn't a condition with a single dangling character
                    # because a single character of input would equal 2 encoded
                    # bytes of output
                    base64string += "="

    return base64string

base64output = bitsToBase64(hexStrToBits(hex_string))
print(base64output)
