
def encode_decode(text, type="encode", key=1):
    assert type in ["encode", "decode"]
    assert key in range(1, 255)
    
    t = ""
    for char in text:
        a = ord(char)
        if type == "encode":
            a += key
        elif type == "decode":
            a -= key
        # a = a % 26
        # convert back to char
        b = chr(a)
        t += b    
    return t

if __name__ == "__main__":
	text = "yellowbluegreen"

	encode = encode_decode(text, "encode", 1)
	decode = encode_decode(encode, "decode", 1)
	print(encode)
