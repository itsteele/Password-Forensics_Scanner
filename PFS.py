# Isaac Steele | Password Forensics Scanner

import os
import re

def scan(directory):
	for root, dirs, files in os.walk(directory):
		for file in files:
			file_path = os.path.join(root, file)
			
			# check file extensions
			if re.search(r'\.(pwd|pw|pswd)$', file, re.IGNORECASE):
				print(f"Potential password vulnerability found in file: {file_path}")
			
			# check file names and content for keywords
			if re.search(r'password|pwd|private|personal|pass|passkey', file, re.IGNORECASE):
				print(f"Potential password-related vulnerability found: {file_path}")
			
			# read file contents for potential passwords
			with open(file_path, 'r') as f:
				content = f.read()
				if re.search(r'password|pwd|private|personal|pass|passkey', content, re.IGNORECASE):
					print(f"Potential password-related vulnerability found: {file_path}")

# run scanner
scan('~/Users/isaacsteele/Desktop')