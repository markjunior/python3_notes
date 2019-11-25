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

```
s->                // Method with String parameter and boolean return-type
  s.matches("...") //  Check if the string matches the regex fully
                   //  (which implicitly adds a leading "^" and trailing "$")

M{0,3}             // No, 1, 2, or 3 adjacent "M"
(     |        )   // Followed by either:
 C[MD]             //  A "C" with an "M" or "D" after it
      |            // or:
       D?          //  An optional "D"
         C{0,3}    //  Followed by no, 1, 2, or 3 adjacent "C"
(     |        )   // Followed by either:
 X[CL]             //  An "X" with a "C" or "L" after it
      |            // or:
       L?          //  An optional "L"
         X{0,3}    //  Followed by no, 1, 2, or 3 adjacent "X"
(     |        )   // Followed by either:
 I[XV]             //  An "I" with an "X" or "V" after it
      |            // or:
       V?          //  An optional "V"
         I{0,3}    //  Followed by no, 1, 2, or 3 adjacent "I"
```
