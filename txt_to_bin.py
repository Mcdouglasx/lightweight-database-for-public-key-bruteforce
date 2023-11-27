
from bitstring import BitArray


data = open('Dat-Bin.txt',"r")

buffer = data.read()

my_str = buffer
binary_file = open('data-base.bin', 'wb')
b = BitArray(bin=my_str)
b.tofile(binary_file)
binary_file.close()
