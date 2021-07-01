num=int(input("enter the any number"))
if num%3==0:
	print("navgurukul")
elif num%7==0:
  print("gurukul")
  if num%3==1 and num%7==0:
	  print("navgurukul")
else:
	print("gurukul")