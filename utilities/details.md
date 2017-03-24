### myregex.py

#### Issue: you can't apply regular expressions, where there are double quoted strings, since those strings may spoil all the patterns because they can contain every special character without special purpose.

* To avoid this issue, I defined all these functions in my regex. In these functions, I sort of ignored the double quoted text.
