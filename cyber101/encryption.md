## Encryption

IN this room went through the importance of improving encryption algorithms based on a history of improving them through time. Large numbers can be easily cracked with computers and the dhkeyexchange.py file show

## Hashing Basics

In this room we discussed the major hashing algorithms MD5, SHA-1, SHA-256 and the weaknesses of ones that have been around longer. Highlighted something called a rainbow table that is a look up table of hashes to plaintext that will allow hackers to look up common hashed password that could be in a database. Also talked about the concept of saltiing, which adds a random value to a password before it is hashed so that it's harder to crack with a hash cracker. We can use the following commands on Kali linux to be able to crack certain things:

hexdump
md5sum filename
sha1sum filename
sha256sum filename


Best practice is to select a secure password, add a unique salt, combine the two and calculate the hash with whatever hash algo you've chosen and store the hashed value and the unique salt.  

Also mentioned that encryption of passwords alone may not be ideal because if you do get the key managed to grant access, then all the credentials stored in the database are now exposed.

Next, we learned how to use ```hashcat -m <hash_type> -a <attack_mode> hashfile wordlist``` as a means to crack hashed passwords. in order to use this you'll need th use the hash type from the Hashcat site based on the format of the hash. Then the attack mode most commonly used is 0 so it checks every word in the password list you pass to. The hashfile is the file that contains the hash you want to crack.

Last we went throught he use ```base64 -d filename ``` for encoding. Encoding converts data from one form to another to make it compatible with a specific system. 

### Referenced Sites
 [CrackStation](https://crackstation.net/)
 [Hashes.com](https://hashes.com/en/decrypt/hash)
 [Hashcat](https://hashcat.net/wiki/doku.php?id=example_hashes)
