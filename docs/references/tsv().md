# **TSV** function

Produces tab-separated values with randomly generated data based on specified data columns and number of rows.

```py
from faker import Faker

fake = Faker()

print(fake.tsv())

# result : "Nicole Smith"	"3651 Spence Terrace
# Harrisonmouth, ND 87969"

# "Olivia Walter"	"USS Oneal
# FPO AP 89611"

# "Daniel Ballard"	"18824 Samuel Brooks Suite 280
# Christophermouth, FL 34738"

# "Joshua Davis"	"032 Smith Stravenue Apt. 433
# West Pamela, NM 53300"

# "Russell Patton"	"USS Villegas
# FPO AP 69967"

# "Rebecca James"	"6966 Barnes Villages Apt. 835
# Lake Tammyport, DE 43519"

# "Alexandria Moore"	"93225 Phillip Prairie
# Michaelfurt, TN 58878"

# "Michelle Thompson"	"082 Kevin Parks Suite 006
# Phillipsfort, SC 02935"

# "Alexandra Gonzales"	"8710 Jonathan Mountains
# North Johnport, MT 09166"

# "Tara Zamora"	"667 Brett Parkway
# Port Harold, NH 96970"


```
