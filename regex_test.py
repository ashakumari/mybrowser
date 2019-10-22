import re

assert re.findall(r"[0-9]", "2+3=5") == ['2', '3', '5']
assert re.findall(r"[a-m]", "Asha Kumari") == ['h', 'a', 'm', 'a', 'i']
assert re.findall(r"[0-9][0-9]", "July 28 2018") == ['28', '20', '18']
assert re.findall(r"[0-9]+", "July 28 in 2018") == ['28', '2018']
assert re.findall(r"[a-z]+|[0-9]+", "Memory002 in 5th era") == ['emory', '002', 'in', '5', 'th', 'era']
assert re.findall(r"-?[0-9]+", "12-13 pages of 1345") == ['12', '-13', '1345']
assert re.findall(r"[a-z]*[0-9]+", "Memory002 in 5th era") == ['emory002', '5']
assert re.findall(r"[0-9]+[0-9]+", "21+3=24") == ['21', '24']
assert re.findall(r"[0-9]+\+[0-9]+", "21+3=24") == ['21+3']
assert re.findall(r"[0-9].[0-9]", "1a1 222 cc3") == ['1a1', '222']
assert re.findall(r"[0-9][^ab]", "1a1 222 cc3") == ['1 ', '22', '2 ']
assert re.findall(r"do+|re+|mi+", "mimi rere midore doo-wop") != ['mimi', 'rere']
assert re.findall(r"(?:do)+|(?:re)+|(?:mi)+", "mimi rere midore doo-wop") == ['mimi', 'rere', 'mi', 'do', 're', 'do']
assert re.findall(r"(?:do|re|mi)+", "mimi rere midore doo-wop") == ['mimi', 'rere', 'midore', 'do']

regexp = r"ab|[0-9]+"
assert re.findall(regexp,"ab") == ["ab"]
assert re.findall(regexp,"1") == ["1"]
assert re.findall(regexp,"123") == ["123"]
assert re.findall(regexp,"a") != ["a"]
assert re.findall(regexp,"abc") != ["abc"]
assert re.findall(regexp,"abc123") != ["abc123"]


regexp1 = r"[a-z]+-?[a-z]+"
assert re.findall(regexp1,"well-liked") == ["well-liked"]
assert re.findall(regexp1,"html") == ["html"]
assert re.findall(regexp1,"a-b-c") != ["a-b-c"]
assert re.findall(regexp1,"a--b") != ["a--b"]

regexp2 = r"[a-z]+\([ ]*[0-9]+[ ]*\)"
assert re.findall(regexp2,"cos(0)") == ["cos(0)"]
assert re.findall(regexp2,"sqrt(   2     )") == ["sqrt(   2     )"]
assert re.findall(regexp2,"cos     (0)") != ["cos     (0)"]
assert re.findall(regexp2,"sqrt(x)") != ["sqrt(x)"]

regexp3 = r'"(?:[^\\]|(?:\\.))*"'
assert re.findall(regexp3,'"I say, \\"hello.\\""') == ['"I say, \\"hello.\\""']
assert re.findall(regexp3,'"\\"') != ['"\\"']


regexp4 = r"[0-9](?:-?[0-9]+)*"
assert re.findall(regexp4, "5") == ["5"]
assert re.findall(regexp4, "-5") != ["-5"]
assert re.findall(regexp4, "584398") == ["584398"]
assert re.findall(regexp4, "584-398908") == ["584-398908"]
assert re.findall(regexp4, "584-398-908") == ["584-398-908"]
assert re.findall(regexp4, "58-48-39-80-908") == ["58-48-39-80-908"]
assert re.findall(regexp4,"0878888888") == ["0878888888"]
