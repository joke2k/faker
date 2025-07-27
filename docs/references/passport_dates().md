# **PASSPORT_DATES** function

Returns a tuple of formatted date strings for birth, passport issue, and expiration dates, adhering to U.S. standards of 5 and 10-year validity periods.

```py
from faker import Faker

fake = Faker()

print(fake.passport_dates())

# result : ('27 Jul 2025', '27 Jul 2025', '27 Jul 2030')
```
