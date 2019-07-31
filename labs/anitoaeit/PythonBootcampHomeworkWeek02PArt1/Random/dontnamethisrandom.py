import random
import string


passwd_len = 10
n_chars = [1, 1, 1, 1] # number of lowercase, uppercase, special characters and digits in this order

rem_chars = passwd_len - 4
while rem_chars > 0:
    rand_int = random.randint(0, rem_chars)
    rand_index = random.randint(0, 3)
    rem_chars -= rand_int
    n_chars[rand_index] += rand_int

passwd = ''
for i in range(n_chars[0]): # pick n_chars[0] random lowercase letters
    rand_index = random.randint(0, len(string.ascii_lowercase) - 1)
    passwd += string.ascii_lowercase[rand_index]

for i in range(n_chars[1]): # pick n_chars[1] random uppercase letters
    rand_index = random.randint(0, len(string.ascii_uppercase) - 1)
    passwd += string.ascii_uppercase[rand_index]

for i in range(n_chars[2]): # pick n_chars[2] random special characters
    rand_index = random.randint(0, len(string.punctuation) - 1)
    passwd += string.punctuation[rand_index]

for i in range(n_chars[3]): # pick n_chars[3] random digits
    rand_index = random.randint(0, len(string.digits) - 1)
    passwd += string.digits[rand_index]

shuffled_passwd = ''
picked_indexes = set()

for i in range(passwd_len):
    rand_index = random.randint(0, passwd_len - 1)
    while rand_index in picked_indexes:
        rand_index = random.randint(0, passwd_len - 1)
    picked_indexes.add(rand_index)
    shuffled_passwd += passwd[rand_index]

print(shuffled_passwd)