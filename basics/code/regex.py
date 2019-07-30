import re
pattern = re.compile(r'\d{3}-\d{3}-\d{4}')
print(type(pattern))
res = pattern.search('call me at a312-231-1242df dfadf\n dsafa 123-123-2413.')
print(res)
print(res.group())
res = pattern.findall('call me at a312-231-1242df dfadf\n dsafa 123-123-2413.')
print(res)


def extract_phone(input):
    phone_regex = re.compile(r'\d{3}-\d{3}-\d{4}')
    match = phone_regex.search(input)
    if match:
        return match.group()
    return None


print(extract_phone('asfdasfasdf sdaf sdafasdf 023-231-4341'))
print(extract_phone('asfdasfasdf sdaf sdafasdf 023-231-4341 and 231-421-3412'))

print('--------------------------------------------')
import re
pattern = re.compile(r"""
	^([a-z0-9_\.-]+)  # name of the email
	@
	([0-9a-z\.-]+)
	\.
	([a-z\.]{2,6})$  #com, org, net, etc.
""", re.VERBOSE | re.I)

match = pattern.search("ThomaS123@Yahoo.com")
print(match.group())
print(match.groups())


print('--------------------------------------------')
import re
text = "Last night Mrs. Daisy and Mr. white murdered Ms. Chow"

pattern = re.compile(r'(Mr.|Mrs.|Ms.) ([a-z])[a-z]+', re.I)
result = pattern.sub("\g<1> \g<2>", text)
print(result)


print('--------------------------------------------')
import re

def titleize(ori_str):
    pattern = re.compile(r'\b(\w)(\w*)\b')
    res = pattern.sub('\g<1>\g<2>', ori_str)
    return res
print(titleize('this is awesome'))
