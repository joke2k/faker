# **PROFILE** function

Returns a comprehensive dictionary containing personal and professional profile information, optionally filtered by specified fields.

```py
from faker import Faker

fake = Faker()

print(fake.profile())

# result : {'job': 'Tax adviser', 'company': 'Hutchinson Group', 'ssn': '641-96-1011', 'residence': '8324 Holt Islands\nPort Jamie, VT 22732', 'current_location': (Decimal('-53.014267'), Decimal('75.752081')), 'blood_group': 'AB+', 'website': ['http://www.valdez.com/'], 'username': 'mark27', 'name': 'Henry Reyes', 'sex': 'M', 'address': '114 Wright Knoll Suite 917\nJeremystad, WA 67735', 'mail': 'sarah38@gmail.com', 'birthdate': datetime.date(1990, 7, 17)}
```
