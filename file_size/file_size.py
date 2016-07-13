import sys

byte_size = 0
f = open(sys.argv[1], 'rb')
try:
    byte = f.read(1)
    while byte != b"":
        byte_size += 1
        byte = f.read(1)
finally:
    f.close()

print("%s" % str(byte_size))
