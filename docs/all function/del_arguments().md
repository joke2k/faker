# **DEL_ARGUMENTS** function

Removes a specified argument or entire argument group from the generator configuration.

```py
from faker import Faker

fake = Faker()

print(fake.del_arguments())

# result : [Erreur lors de l'exécution : Generator.del_arguments() missing 1 required positional argument: 'group']
```
