# lightweight database for public-key bruteforce puzzle 32
*creating the lightweight database, 32 million keys 3.80MB.*

**requirements:**

pip install bitstring

secp256k1

https://github.com/iceland2k14/secp256k1

Download and place the files in the same folder as the scripts


**for single pubkey.**

1-we generate a bin file with the publickeys represented in 1s and 0s.


0=even,
1=odd.

using **binary_database.py**

**You should use numbers like this:**


Code:
num = 10000000000000
Low_m= 10000

Code:
num = 20000000000000
Low_m= 2000

**Avoid doing this or you will find private keys with the last numbers changed**

Code:
num = 14678976447
Low_m= 23


**we did it!**

We have a huge database, with little disk space.

Because there is no sequence between even and odd pubkeys we can set a collision margin of 64, 128, 256....
By this I mean that as you increase the collision margin, the probability of finding an identical binary sequence decreases.


**What's the use of this?**

We just need to randomly generate binary sequences and check if they exist in the
Database.

**searching single pubkey**


using **Search_key.py**

----------------------------------------------------------------------------------------------------------------------------------------------------------------

**FOR multiple pubkeys**


- first we create the database by making random subtractions in a range specified by us, you can create your own list at your discretion.


- Using **rand_targets_db.py**


**Db multi-pubkeys**


-we create our database for multiple keys.

- Using **multi_binary_Db.py**


**scan multi-pubkey**

- Using **multy_binary_scan.py**

bitcointalk post
https://bitcointalk.org/index.php?topic=5475626.msg63227343#msg63227343




**Donate to:**
**btc: bc1qxs47ttydl8tmdv8vtygp7dy76lvayz3r6rdahu**


