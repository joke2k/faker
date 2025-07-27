# **INVALID_SSN** function

Generate a random United States Social Security Number (SSN) that is invalid and not an Individual Taxpayer Identification Number (ITIN).

```py
from faker import Faker

fake = Faker()

print(fake.invalid_ssn())

# result : 634-89-0000
```
