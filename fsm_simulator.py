def fsmsim(string, current, edges, accepting):
	if string == "":
		return current in accepting
	else:
		letter = string[0]
		if (current, letter) in edges:
			destination = edges[(current, letter)]
			remaining_string = string[1:]
			return fsmsim(remaining_string, destination, edges, accepting)
		else:
			return False


# Corresponds to regular expression r"a+1+"
edges1 = {
	(1, 'a') : 2,
	(2, 'a') : 2,
	(2, '1') : 3,
	(3, '1') : 3,	
}
accepting1 = [3]
assert fsmsim("aa11", 1, edges1, accepting1) == True
assert fsmsim("a1", 1, edges1, accepting1) == True
assert fsmsim("aaa", 1, edges1, accepting1) == False
assert fsmsim("111", 1, edges1, accepting1) == False
assert fsmsim("", 1, edges1, accepting1) == False
assert fsmsim("a1a1a1", 1, edges1, accepting1) == False

# Corresponds to regular expression r"q*"
edges2 = {
	(1, '') : 1,
	(1, 'q') : 1,
}
accepting2 = [1]
assert fsmsim("q", 1, edges2, accepting2) == True
assert fsmsim("qqqqq", 1, edges2, accepting2) == True
assert fsmsim("", 1, edges2, accepting2) == True
assert fsmsim("qqqrr", 1, edges2, accepting2) == False
assert fsmsim("aacc", 1, edges2, accepting2) == False

# Corresponds to regular expression r"[a-b][c-d]?"
edges3 = {
	(1, 'a') : 2,
	(1, 'b') : 2,
	(2, 'c') : 3,
	(2, 'd') : 3,
}
accepting3 = [2, 3]
assert fsmsim("ac", 1, edges3, accepting3) == True
assert fsmsim("ad", 1, edges3, accepting3) == True
assert fsmsim("bd", 1, edges3, accepting3) == True
assert fsmsim("bc", 1, edges3, accepting3) == True
assert fsmsim("a", 1, edges3, accepting3) == True
assert fsmsim("b", 1, edges3, accepting3) == True
assert fsmsim("", 1, edges3, accepting3) == False
assert fsmsim("ab", 1, edges3, accepting3) == False
assert fsmsim("aa", 1, edges3, accepting3) == False
assert fsmsim("az", 1, edges3, accepting3) == False
assert fsmsim("c", 1, edges3, accepting3) == False
assert fsmsim("d", 1, edges3, accepting3) == False

