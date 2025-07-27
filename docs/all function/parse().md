# **PARSE** function

Replaces tokens in a string with the output from the corresponding token method call, using argument groups as needed.

```py
from faker import Faker

fake = Faker()

print(fake.parse())

# result : [Erreur lors de l'exécution : Generator.parse() missing 1 required positional argument: 'text']
```
