https://pythex.org/
```
\d digits 0-9
\w letter, digit, or underscore
\s whitespace character
\D not a digit
\W not a word character
\S not a whitespace character
. any character except line break
```

quantifers
```
+ one or more   e.g., s\w+
{3} exactly x times   e.g., \w{9}
{3,5} 3-5 times  
{4,} four or more times   e.g., \w{9}
*  zero or more times   e.g., ab*c
? Once or more (optional)
```


```
^ start of string or line
$ end of string or line
\b word boundary  
```


```
import re
pattern = re.compile(r'^(Mr\.|Mrs\.|Ms\.|Mdme\.) (?P<first>[A-Za-z]+) (?P<last>[A-Za-z]+)$')
pattern.search(input).group('first')
```
