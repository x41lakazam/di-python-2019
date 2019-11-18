import jwt
import time

encrypted_data = b'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJiYW5rX3B3ZCI6ImFvZWlyam9pamVvaXdqciIsImJhbmtfYWNjb3VudCI6MjM5NDgwMTIzLCJiYW5rX25hbWUiOiJsZXVtaSJ9.dtG3ptdP677ZtoZI_dkilubTjr0aliWUwp9-vsdXw_Q'

# I know that the password is 9 letters long.
# Start from 9 a
# start = 'aaaaaaaaa'
# alphabet = 'abcdefghijklnopqrstuvwxyz'
# 
# def possibilites():
#     poss  = []
#     for letter1 in alphabet:
#         for letter2 in alphabet:
#             for letter3 in alphabet:
#                 for letter4 in alphabet:
#                     for letter5 in alphabet:
#                         for letter6 in alphabet:
#                             word = letter1+letter2+letter3+letter4+letter5+letter6
#                             yield word
# 
# 
# for possibility in possibilites():
#     print("testing", possibility)
#     try:
#         jwt.decode(encrypted_data, possibility)
#     except jwt.exceptions.InvalidSignatureError:
#         pass
#     else:
#         good_password = possibility
#         break
#
# print('The good password is:', good_password)
# print('Here is the data:', jwt.decode(encrypted_data, good_password))

#
# Dictionnary attack
import urllib.request as req

dictionnary_url = 'https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt'

# Open the url
response = req.urlopen(dictionnary_url)
password_str = str(response.read())
print("Got passwords list !")
start_time = time.time()
possibility = ''
slash = False

for letter in password_str:
    if slash and letter == 'n':
        print("testing", possibility)
        slash = False
        try:
            jwt.decode(encrypted_data, possibility)
        except jwt.exceptions.InvalidSignatureError:
            continue
        else:
            good_password = possibility
            break
        finally:
            possibility = ""

    if letter != '\\':
        possibility += letter
    else:
        slash = True
        continue

end = time.time()
print('The good password is:', good_password)
print('Here is the data:', jwt.decode(encrypted_data, good_password))

print("Time to find the password:", end-start_time)





