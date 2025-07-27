# **SET_FORMATTER** function

Registers a custom provider method to the generator with specified name and formatter.

```py
from faker import Faker

fake = Faker()

print(fake.set_formatter())

# result : [Erreur lors de l'exécution : Generator.set_formatter() missing 2 required positional arguments: 'name' and 'formatter']
```
