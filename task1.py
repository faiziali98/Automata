import re

def stringMatch(str):
	m = re.match(r"(?:[A-Z]|[a-z]|[1-9]|-|_){6,10}$", str)
	if m:
		return True
	else:
		return False

print stringMatch("asasdasdasdsadas")