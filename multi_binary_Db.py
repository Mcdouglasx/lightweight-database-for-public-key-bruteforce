import secp256k1 as ice
#@mcdouglasx
print("Making Binary Data-Base")

target__multi_public_keys = "example.txt"

with open(target__multi_public_keys, 'r') as f:

    lines= f.readlines()
    X = len(lines)
    
    for line in lines:
       
        mk= ice.pub2upub(str(line.strip()))

        num = 32000000//X # number of keys.
        
        sustract= 1 #amount to subtract each time.

        sustract_pub= ice.scalar_multiplication(sustract)

        res= ice.point_loop_subtraction(num, mk, sustract_pub)

        for t in range (num+1):
            h= (res[t*65:t*65+65]).hex()
            hc= int(h[2:], 16)
            
            
            if str(hc).endswith(('0','2','4','6','8')):
                A="0"
                data = open("Dat-Bint.txt","a")
                data.write(A)
                data.close()
                
            if str(hc).endswith(('1','3','5','7','9')):
                A="1"
                data = open("Dat-Bint.txt","a")
                data.write(A)
                data.close()

            

