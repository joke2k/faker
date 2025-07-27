# **TIME_SERIES** function

Generates a sequence of tuples containing datetime and corresponding values at specified intervals from start_date to end_date, using a given distribution function and timezone.

```py
from faker import Faker

fake = Faker()

print(fake.time_series())

# result : <generator object Provider.time_series at 0x00000177202EBD00>
```
