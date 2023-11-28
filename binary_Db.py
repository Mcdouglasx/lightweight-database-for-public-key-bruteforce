#@mcdouglasx
import secp256k1 as ice
from bitstring import BitArray

print("Making Binary Data-Base")


target_public_key = "030d282cf2ff536d2c42f105d0b8588821a915dc3f9a05bd98bb23af67a2e92a5b"

target = ice.pub2upub(target_public_key)

num = 1000 # number of keys.

sustract= 1 #amount to subtract each time.

sustract_pub= ice.scalar_multiplication(sustract)

res= ice.point_loop_subtraction(num, target, sustract_pub)
binary = ''
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

    
