# **JSON_BYTES** function

Returns a byte-encoded JSON array of randomly generated objects with name and residency fields.

```py
from faker import Faker

fake = Faker()

print(fake.json_bytes())

# result : b'[{"name": "Karen Rivers", "residency": "7118 Wright Roads Suite 154\\nDavisborough, ID 74556"}, {"name": "Jonathan Johnson", "residency": "92573 Brandon Hills Suite 912\\nNorth Mark, MP 99938"}, {"name": "Destiny Anthony", "residency": "60271 Thomas Crest Apt. 180\\nWest Juliaborough, RI 82560"}, {"name": "Andrea Smith", "residency": "37618 Wiggins Crossroad\\nNew Jaimetown, KS 71801"}, {"name": "Christopher Holland", "residency": "756 Hinton Freeway\\nSuttonside, IN 22870"}, {"name": "Rebecca Mills", "residency": "0009 Andrews Rapid\\nAllenbury, PR 35494"}, {"name": "Emily Morales", "residency": "4582 Amber Via Apt. 999\\nWest Sandra, PR 81883"}, {"name": "John Blackburn", "residency": "113 Morris Rapids\\nRobertland, NM 12053"}, {"name": "Kristen Meyer", "residency": "48417 Perry Heights\\nChristopherland, WI 75597"}, {"name": "Dustin Lawson", "residency": "3183 Donald Wells\\nNorth Shannonmouth, IN 62766"}]'
```
