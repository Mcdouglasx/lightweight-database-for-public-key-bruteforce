#@mcdouglasx
import secp256k1 as ice
import random
from bitstring import BitArray



print("Scanning Binary Sequence")


#range
start= 3090000000        
end=   3093472814



X= 1024 #number of sequential pubkeys for each target

while True:

    pk= random.randint(start, end)
    
    target = ice.scalar_multiplication(pk)

    num = 64 # collision margin.

    subtract= 1 #amount to subtract each time.

    subtract_pub= ice.scalar_multiplication(subtract)

    res= ice.point_loop_subtraction(num, target, subtract_pub)
    
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

    b = BitArray(bin=my_str)

    c = bytes(b)

    file = open("multi-data-base.bin", "rb")
    dat= BitArray(file.read())
    
    

    if b  in dat:
        
        s = c
        f = dat
        inx = f.find(s)
        inx_1=str(inx).replace(",", "")
        inx_0=str(inx_1).replace("(", "")
        inx_2=str(inx_0).replace(")", "")
        
        Pk = (int(pk) + ((int(inx_2) % X)*subtract))
        cpub=ice.to_cpub(ice.scalar_multiplication(Pk).hex())
        with open("rand_subtract.txt", 'r') as Mk:

            lines= Mk.readlines()
            for line in lines:
                
                mk_0= str(line.strip())
                mk= int(mk_0[68:])
                mk2= mk_0[ :66]
                if mk2 in cpub:
                    print("found")
                    cpub2=ice.to_cpub(ice.scalar_multiplication(Pk+mk).hex())
                    data = open("win.txt","a")
                    data.write("Pk:"+" "+str(Pk+mk)+"\n")
                    data.write("cpub:"+" "+str(cpub2)+"\n")
                    data.close()
                    break
        break
