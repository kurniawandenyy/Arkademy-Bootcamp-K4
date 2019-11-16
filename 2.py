import re

def username(username):
	regex_username = re.compile(r'^[A-Z]{7}$')
	res = regex_username.search(username)
	if res:
		print("Valid Username")
	else:
		print("Invalid Username")

def password(password):
	regex_name = re.compile(r'^(\d)\1\1[*][A-Za-z]{3}$')	
	res = regex_name.search(password)
	if res:
		print("Valid Password")
	else:
		print("Invalid Password")

username("ARKDEMY")
username("arkdemy")
password("111*sss")
password("123*try")

