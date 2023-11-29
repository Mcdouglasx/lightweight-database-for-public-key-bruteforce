# lightweight-database-for-public-key-bruteforce-
creating the lightweight database, 32 million keys.

for single pubkey.

binary_Db.py

single publickey (low memory)

low_memory_db.py

If you want to create a longer database than your memory supports
For example, 1000 million keys and your memory limit is 100 million, divide by 10 changing this variable:

Low_m= 10


for multiple pubkeys

rand_targets_db.py

We create our random subtraction database.

You will obtain 2 .txt files, one with the amount subtracted and its respective publickey and another with the public keys for the binary database.


multi_binary_Db.py
for multiple pubkeys, txt file with one compressed public key per line.

1-we generate a text file with the publickeys represented in 1s and 0s.
0=even,
1=odd.

txt_to_bin.py
2. we convert to bitarray  and creating a .bin file



we have 32 mkeys in a 3.81MB file.

Because there is no sequence between even and odd pubkeys we can set a collision margin of 64, 128, 256....
By this I mean that as you increase the collision margin, the probability of finding an identical binary sequence decreases.


What's the use of this?
We just need to randomly generate binary sequences and check if they exist in the database.

for single public key

binary_scan.py


for multi-publickeys

multi_binary_scan.py


To search for multiple keys, divide the number of keys you choose // the target pubkeys.
example:
If you create a database of 100 million keys and have 10 objectives, each objective will represent 10 million keys.

Importantly, change this part to your settings.

#total number of keys in database.


Db_items= 100000000

#number of targets.


Db_target=10




Donate to:
btc: bc1qxs47ttydl8tmdv8vtygp7dy76lvayz3r6rdahu


