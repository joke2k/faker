# **LOCATION_ON_LAND** function

Returns a tuple with land coordinates and metadata, or coordinates only if `coords_only` is passed.

```py
from faker import Faker

fake = Faker()

print(fake.location_on_land())

# result : ('26.11527', '86.59509', 'Supaul', 'IN', 'Asia/Kolkata')
```
