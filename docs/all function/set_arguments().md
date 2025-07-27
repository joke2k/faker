# **SET_ARGUMENTS** function

Defines an argument group with a single argument or a dictionary of arguments for token application in the parse method.

```py
from faker import Faker

fake = Faker()

print(fake.set_arguments())

# result : [Erreur lors de l'exécution : Generator.set_arguments() missing 2 required positional arguments: 'group' and 'argument']
```
