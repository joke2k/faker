# **LEXIFY** function

Replaces each question mark in a given string with a random character from a specified set of letters, defaulting to all ASCII letters.

```py
from faker import Faker

fake = Faker()

print(fake.lexify())

# result : qzDd
```
