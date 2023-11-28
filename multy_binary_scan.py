#@mcdouglasx
import secp256k1 as ice
import random
from bitstring import BitArray



print("Scanning Binary Sequence")

#Pk: 1033162084
#cPub: 030d282cf2ff536d2c42f105d0b8588821a915dc3f9a05bd98bb23af67a2e92a5b

#range
start= 1033000000
end=   1034000000

#total number of keys in database.
Db_items= 160000

#number of targets.
Db_target=16
A_x= Db_items//Db_target 
X= A_x
print(X)

while True:

    pk= random.randint(start, end)

    target = ice.scalar_multiplication(pk)

    num = 64 # collision margin.

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
    
        
    my_str = binary

    b = bytes(BitArray(bin=my_str))

    file = open("data-base.bin", "rb")

    dat = bytes(file.read())
    
    if b  in dat:
        with open (r"data-base.bin", "rb") as file:
            s = b
            f = bytes(file.read())
            inx = (f.find(s) % X)
            inx_0= inx*sustract
            Pk = (int(pk) + int(inx_0))+int(inx_0)*7
            pub= ice.scalar_multiplication(Pk).hex()
            cpub= ice.to_cpub(pub)
        
            data = open("win.txt","a")
            data.write("Pk:"+" "+str(Pk)+"\n")
            data.write("cpub:"+" "+str(cpub)+"\n")
            data.close()
            break
