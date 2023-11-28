#@mcdouglasx
import secp256k1 as ice
from bitstring import BitArray
import bitcoin


print("Making Binary Data-Base")


target_public_key = "030d282cf2ff536d2c42f105d0b8588821a915dc3f9a05bd98bb23af67a2e92a5b"

target = ice.pub2upub(target_public_key)


num = 2000 # number of keys.

sustract= 1 #amount to subtract each time.

Low_m= 5 

lm= num // Low_m
   

sustract_pub= ice.scalar_multiplication(sustract)

res= ice.point_loop_subtraction(lm, target, sustract_pub)
binary = ''
for t in range (lm):

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

for i in range (1,Low_m):
    
    mem= ice.to_cpub(ice.scalar_multiplication(lm).hex())
    
    Apk= bitcoin.multiply(mem, i)
    
    Apk_upu= ice.pub2upub(Apk)

    A1= ice.point_addition(target, Apk_upu)

    sustract_pub= ice.scalar_multiplication(sustract)

    res= ice.point_loop_subtraction(lm, A1, sustract_pub)
    
    binary = ''
    for t in range (lm):

        h= (res[t*65:t*65+65]).hex()
        hc= int(h[2:], 16)
            
            
        if str(hc).endswith(('0','2','4','6','8')):
            A="0"
            binary+= ''.join(str(A))
                
        if str(hc).endswith(('1','3','5','7','9')):
            A="1"
            binary+= ''.join(str(A))
            

    my_str = bytes(BitArray(bin=binary))

    binary_file = open('data-base.bin', 'ab')
    binary_file.write(my_str)
    binary_file.close()

