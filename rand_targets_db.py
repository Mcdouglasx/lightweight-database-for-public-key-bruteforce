#@mcdouglasx
import secp256k1 as ice
import random

print("Making random sustract Data-Base")

target_public_key = "0209c58240e50e3ba3f833c82655e8725c037a2294e14cf5d73a5df8d56159de69"

target = ice.pub2upub(target_public_key)

targets_num= 1000 # subtract keys numbers

start= 0
end=   1000000

for i in range(targets_num):

    A0 = random.randint(start, end)
    A1 = ice.scalar_multiplication(A0)
    A2= ice.point_subtraction(target, A1).hex()
    A3 = ice.to_cpub(A2)
    data = open("rand_subtract.txt","a")
    data.write(str(A3)+" "+"#"+str(A0)+"\n")
    data.close()
   
