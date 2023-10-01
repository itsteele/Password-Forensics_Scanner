# Isaac Steele | Password Forensics Scanner

# Potentially useful libraries : os, glob


# Function that searches the string 
def fileSearch(path, keyword):
	with open(path, 'r') as file:
		
		data = file.read()
	
		if keyword in data:
			print('unsecured password found!')
		else:
			print('no password vulnerabilities found')

fileSearch(r'/Users/isaacsteele/Desktop/PFS-Test/private.txt', 'passwords')