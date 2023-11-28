#@mcdouglasx
import secp256k1 as ice
from bitstring import BitArray
print("Making Binary Data-Base")

target__multi_public_keys = "rand_sustract.txt"

with open(target__multi_public_keys, 'r') as f:

    lines= f.readlines()
    X = len(lines)
    binary = ''
    for line in lines:
      
        mk= ice.pub2upub(str(line.strip()))

        num = 32000000//X # number of keys.
        
        sustract= 1 #amount to subtract each time.

        sustract_pub= ice.scalar_multiplication(sustract)

        res= ice.point_loop_subtraction(num, mk, sustract_pub)

        
        for t in range (num):

            h= (res[t*65:t*65+65]).hex()
            hc= int(h[2:], 16)
                
                
            if str(hc).endswith(('0','2','4','6','8')):
                A="0"
                binary+= ''.join(str(A))
                    
            if str(hc).endswith(('1','3','5','7','9')):
                A="1"
                binary+= ''.join(str(A))
                

my_str = bytes(BitArray(bin=binary))

binary_file = open('data-base.bin', 'wb')
binary_file.write(my_str)
binary_file.close()

