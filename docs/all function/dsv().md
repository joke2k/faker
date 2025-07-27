# **DSV** function

Generates a string of random delimiter-separated values based on specified header and data column formats, dialect, and additional formatting parameters.

```py
from faker import Faker

fake = Faker()

print(fake.dsv())

# result : "William Hunt","53038 Deborah Road Suite 918
East Roger, PW 14132"
"Robert Smith","2219 Frank Manor
South Chadville, PA 11475"
"Amanda Brewer","368 Tate Walk
New Kelseyhaven, MA 12895"
"Tim Boyer","11819 Michelle Track Apt. 077
Lisamouth, MP 57618"
"Timothy Williams","3737 Joshua Tunnel
South Christophermouth, AS 36082"
"Tanya Velez","79998 Long Centers
Robertsonmouth, VA 65233"
"Kathryn Humphrey","1615 Mary Court Apt. 426
New Lisaside, MH 19769"
"Cory Bowman","47169 Marc Glen
South Tina, VT 25714"
"Sheri Mcmillan","160 Martinez Crest
South Lisastad, MA 77952"
"Ashlee Davies","Unit 8341 Box 9122
DPO AE 01249"

```
