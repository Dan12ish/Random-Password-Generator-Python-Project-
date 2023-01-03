import random

#Numeric Password.

def n_p():
	x=int(input("Enter the length of the password:\n"))
	print('')
	print('Password:\n', random.randint(pow(10,x-1),int('9'*x)))



#Alphabet Password (Uppercase).

def ap_u():
	x=int(input("Enter the length of the password:\n"))
	
	password=''

	for i in range(x):
		password+=chr(random.randint(65,90))
	print('')
	print('Password:\n', password)


#Alphabet Password Lowercase().
def ap_l():
	x=int(input("Enter the length of the password:\n"))
	
	password=''

	for i in range(x):
		password+=chr(random.randint(97,122))
	print('')
	print('Password:\n', password)


#Alphanumeric Password.
def anp():
	x=int(input("Enter the length of the password:\n"))
	
	password=''

	for i in range(x):
		password+=chr(random.randint(33,122))
	print('')
	print('Password:\n', password)


#Alphanumeric Password V2.

def anp_v2():
	x=int(input("Enter the length of the password:\n"))
	
	password=''
	
	while len(password) != x:
	   	ch=chr(random.randint(33,122))
	   	
	   	if (ord(ch)==33):
	   		password +=ch
	   	
	   	elif (ord(ch)==35):
	   	   password +=ch
	   	
	   	elif (ord(ch)==38):
	   		password +=ch
	   	
	   	elif (ord(ch)>=48 and ord(ch)<=57):
	   		password +=ch
	   	
	   	elif(ord(ch)>=64 and ord(ch)<=95):
	   		password +=ch
	   	
	   	elif (ord(ch)>=97 and ord(ch)<=122):
	   		password +=ch
	
	print('')  
	print('Password:\n', password)


#Start of the Program
	   		
print("Welcome to the random password generator!")
print(' ') 
print("Please choose from the below types of passwords:\n(1) Numeric Password.\n(2) Uppercase Alphabetical Password.\n(3) Lowercase Alphabetical Password.\n(4) Alphanumeric Password with all special symbols.\n(5) Alphanumeric Password with valid special symbols only.")	   		
print(' ')
a=int(input("Enter which type of password are you looking forward to generate:\n"))
print(' ')

if (a==1):
	n_p()
elif (a==2):
	ap_u()
elif (a==3):
	ap_l()
elif(a==4):
	anp()
elif(a==5):
	anp_v2()
print('') 
print('Thank you!')
