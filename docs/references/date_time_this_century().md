# **DATE_TIME_THIS_CENTURY** function

Returns a datetime object representing a random date and time within the current century, with options to include dates before or after the current date and to specify a timezone.

```py
from faker import Faker

fake = Faker()

print(fake.date_time_this_century())

# result : 2007-10-25 16:34:30
```
