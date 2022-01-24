"""Weekly coding challenge"""
def customStringEncrypt(s):
    """encrypts string.
	step 1. reverse string
	step 2. replace vowels with new value
	step 3. add 'aca' to end of string
	"""
    s = s[::-1].replace('a', str(0)).replace('e', str(1)).replace('i', str(2)).replace('o', str(2)).replace('u', str(3))
    s = s + 'aca'
    return s