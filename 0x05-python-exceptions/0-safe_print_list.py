#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
	no = 0
	for i in range(x):
		try:
			print(my_list[i], end='')
			no += 1
		except IndexError:
			break
	print('')
	return no
'''def safe_print_list(my_list=[], x=0):
	try:
		count = 0
		for i in range(x):
			print(my_list[i], end='')
			count += 1
	except IndexError:
		pass
	print("\n")
	return count'''
