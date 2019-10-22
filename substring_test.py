
# Selecting Substrings : Writing a Python Procedure

# Let p and q each be strings containing two words separated by a space.

# Examples:
#    "bell hooks"
#    "grace hopper"
#    "alonzo church"

# Write a procedure called myfirst_yoursecond(p,q) that returns True if the
# first word in p equals the second word in q. Return False otherwise.

def myfirst_yoursecond(p,q):
    myfirst_end = p.find(" ")
    yoursecond_start = q.find(" ")
    myfirst = p[0:myfirst_end]
    yoursecond = q[yoursecond_start+1:]
    if myfirst == yoursecond: return True
    return False

def myfirst_yoursecond_better(p,q):
	p_parts = p.split()
	q_parts = q.split()
	if p_parts[0] == q_parts[1]: return True
	return False


assert myfirst_yoursecond("bell hooks", "grace hopper") == False
assert myfirst_yoursecond("bell hooks", "curer bell") == True
assert myfirst_yoursecond_better("bell hooks", "grace hopper") == False
assert myfirst_yoursecond_better("bell hooks", "curer bell") == True
