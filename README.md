# lightweight-database-for-public-key-bruteforce-
creating the lightweight database, 32 million keys.

binary_Db.py

1-we generate a text file with the publickeys represented in 1s and 0s.
0=even,
1=odd.

txt_to_bin.py
2. we convert to bitarray  and creating a .bin file



we have 32 mkeys in a 3.81MB file.

Because there is no sequence between even and odd pubkeys we can set a collision margin of 64, 128, 256....
By this I mean that as you increase the collision margin, the probability of finding an identical binary sequence decreases.


What's the use of this?
binary_scan.py
We just need to randomly generate binary sequences and check if they exist in the database.

btc: bc1qxs47ttydl8tmdv8vtygp7dy76lvayz3r6rdahu


