#@mcdouglasx
import secp256k1 as ice
import random

print("Making random sustract Data-Base")

target_public_key = "030d282cf2ff536d2c42f105d0b8588821a915dc3f9a05bd98bb23af67a2e92a5b"

target = ice.pub2upub(target_public_key)

targets_num= 16

start= 1
end=   100000

for i in range(1,targets_num+1):

    A0 = random.randint(start, end)
    A1 = ice.scalar_multiplication(A0)
    A2= ice.point_subtraction(target, A1).hex()
    A3 = ice.to_cpub(A2)
    data = open("rand_sustract.txt","a")
    data.write(str(A3)+"\n")
    data.close()
    data = open("rand_sustract+pk.txt","a")
    data.write(str(A3)+"\n")
    data.write(str(A0)+"\n")
    data.close()
