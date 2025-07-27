# **CSV** function

Generate a string of random comma-separated values based on specified data templates and parameters.

```py
from faker import Faker

fake = Faker()

print(fake.csv())

# result : "Courtney Benton","8324 Woods Isle
West Danielview, MD 28559"
"Matthew Walton","003 Elliott Village Suite 114
Gordonbury, VA 10282"
"Brandi Weeks","8179 Bailey Cliff Apt. 774
West Andrehaven, UT 89527"
"Joseph Wheeler","82303 Jonathan Run
Paulside, AL 58833"
"Darren Butler","78293 Smith Ville Apt. 877
East Sarah, MI 28696"
"Thomas Jones","8129 Christopher Spring Suite 586
Donaldbury, MN 95230"
"Christian Calhoun","368 Cantrell Forks Apt. 340
South Patricia, AL 46372"
"Jaime Ellis","2006 Jones Islands
Kennethberg, WA 90871"
"Richard Evans","PSC 0535, Box 2586
APO AE 25991"
"Joan Chase","39183 Martinez Radial
West Veronicaland, AS 66670"

```
