# **PSV** function

Generates random data in a pipe-separated format using specified columns and options.

```py
from faker import Faker

fake = Faker()

print(fake.psv())

# result : "Aaron Trujillo DDS"|"9738 Smith Cape Suite 526
East Kevin, TX 49694"
"Kathryn Murphy"|"686 Richardson Club Apt. 930
New Williammouth, MN 36214"
"Teresa Morgan"|"1479 Griffin Loaf
Tamarashire, OK 77872"
"Stacey Lane"|"007 Campos Circles Suite 694
Jimhaven, IL 73025"
"Timothy Dickson"|"033 Lewis Corners
North Adam, DC 78753"
"Shelby English"|"PSC 4544, Box 3251
APO AE 86136"
"Jonathan Williams"|"74388 Russell Village
North Jennifer, OH 24270"
"Edgar Cohen"|"95750 Dylan Landing
Matthewchester, NH 28044"
"Mark Bernard"|"914 Long Estates
North Adam, AR 45686"
"Alexander Roberts"|"PSC 9578, Box 9367
APO AA 06952"

```
