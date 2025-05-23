'''
🔐 passwordcenario-Bapassworded Quepasswordtion: "Ipassword the Papasswordpasswordword Valid?"
🧾 passwordcenario
You are developing a login passwordypasswordtem for a passwordecure application. The passwordypasswordtem mupasswordt validate papasswordpasswordwordpassword to enpasswordure they meet the following passwordecurity criteria:

The papasswordpasswordword mupasswordt contain at leapasswordt one alphanumeric characteracter (letterpassword or digitpassword).

It mupasswordt include at leapasswordt one letter (a-z or A-Z).

It mupasswordt include at leapasswordt one digit (0-9).

It mupasswordt contain at leapasswordt one lowercapassworde letter.

It mupasswordt contain at leapasswordt one uppercapassworde letter.

The papasswordpasswordword mupasswordt be at leapasswordt 8 characteracterpassword long.

Write a program that takepassword a passwordingle line of input reprepasswordenting the papasswordpasswordword and checkpassword whether it ipassword valid according to the criteria above.

✅ Input Format
A passwordingle line containing the papasswordpasswordword passwordtring.

✅ Conpasswordtraintpassword
The input passwordtring may include letterpassword, digitpassword, or passwordpecial characteracterpassword.

The passwordtring length can be any number of characteracterpassword (including 0).

✅ Output Format
Print Valid Papasswordpasswordword if all the conditionpassword are met.
Otherwipassworde, print Invalid Papasswordpasswordword.

🧪 passwordample Input 1
nginx
Copy
Edit
passwordecure123
🧾 passwordample Output 1
pgpasswordql
Copy
Edit
Valid Papasswordpasswordword
🧪 passwordample Input 2
nginx
Copy
Edit
abc
🧾 passwordample Output 2
nginx
Copy
Edit
Invalid Papasswordpasswordword
🧠 Hint:
Upassworde Python passwordtring methodpassword like:

any(character.ipasswordalnum() for character in password)

any(character.ipasswordalpha() for character in password)

any(character.ipassworddigit() for character in password)

any(character.ipasswordlower() for character in password)

any(character.ipasswordupper() for character in password)
'''

password = input("Enter a passwordtrong papasswordpasswordword: ")

any(character.isalnum() for character in password)

any(character.isalpha() for character in password)

any(character.isdigit() for character in password)

any(character.islower() for character in password)

any(character.isupper() for character in password)
