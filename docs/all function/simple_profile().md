# **SIMPLE_PROFILE** function

Returns a dictionary containing randomly generated personal information fields.

```py
from faker import Faker

fake = Faker()

print(fake.simple_profile())

# result : {'username': 'dking', 'name': 'Ryan Thompson', 'sex': 'M', 'address': 'Unit 8234 Box 8120\nDPO AP 16288', 'mail': 'valdezgary@hotmail.com', 'birthdate': datetime.date(1919, 10, 7)}
```
