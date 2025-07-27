# **JSON** function

Generates serialized JSON data based on a specified data structure and number of entries.

```py
from faker import Faker

fake = Faker()

print(fake.json())

# result : [{"name": "Christine Hays", "residency": "9521 Hernandez Tunnel\nWest Teresaburgh, NY 79102"}, {"name": "Anthony Willis", "residency": "446 Cameron Causeway Apt. 209\nPort Catherinehaven, OH 31730"}, {"name": "Joshua Ruiz", "residency": "323 Christina Plains\nNew Sherryburgh, KY 25707"}, {"name": "Tina Lopez", "residency": "83935 Jeffrey Squares\nWest Austin, RI 31735"}, {"name": "Mary Hughes", "residency": "154 Thomas Hollow\nNorth Tiffanyberg, TN 66881"}, {"name": "Ronnie Stein", "residency": "98821 Ferguson Turnpike\nButlerville, DE 09452"}, {"name": "Richard Williams", "residency": "40454 Jones Land Suite 290\nBenitezchester, TN 55284"}, {"name": "Brianna Goodman", "residency": "013 Julia Road Apt. 746\nNew Kevin, PA 20086"}, {"name": "Sandra Jimenez", "residency": "645 Turner Throughway Apt. 991\nGreenburgh, PA 06414"}, {"name": "Alice Perez", "residency": "002 Jason Valley Apt. 710\nEast Kenneth, GU 90418"}]
```
