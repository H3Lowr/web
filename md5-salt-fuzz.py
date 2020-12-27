#!/usr/bin/python3

import hashlib 

fuzz = [line.rstrip('\n') for line in open('grinch.txt')]

for i in fuzz:

	#{"target":"203.0.113.33","hash":"5f2940d65ca4140cc18d0878bc398955"}

	  target =  i + "203.0.113.33"

	  target_hash = "5f2940d65ca4140cc18d0878bc398955"

	  generate_hash = hashlib.md5(target.encode())

	  md5 = str(generate_hash.hexdigest())

	  if target_hash == md5:

	  	print("Here's valid salt: "+i)

	  	break




