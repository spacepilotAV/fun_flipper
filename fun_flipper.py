#!/usr/bin/python
import sys, random

if len(sys.argv) < (2 + 1):
	print("USAGE: " + sys.argv[0] + " IN_FILE OUT_FILE {#BITFLIPS default=1%}")
	sys.exit(-1)

in_file      = open(sys.argv[1], "r")
out_file     = open(sys.argv[2], "w")
print("opened files")
in_txt = in_file.read()
print("read files")
in_file.close()
txt_mod = list(in_txt)

if type(sys.argv[3]) == type("0"):
    bit_flips = int(sys.argv[3])
else:
    bit_flips = len(in_txt) / 100
print(bit_flips)

def do_bit_flip():
	txt_mod[random.randint(0,len(txt_mod)-1)] = chr(random.randint(0,255))

for i in range(bit_flips):
    print("doing bitflip" + str(i))
    do_bit_flip()

print("writing")
out_file.write("".join(txt_mod))
print("closing")
out_file.close()

print("done")
