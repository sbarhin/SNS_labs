import caesar
import time

t1 = time.time()
for key in range(1, 96):
	decode = caesar.encode_decode("zfmmpxcmvfhsffo", "decode", key)
	print(decode, key)
t2 = time.time()
print(t2-t1)
