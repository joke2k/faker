# **IMAGE** function

Generates an image with a random polygon using specified size, format, hue, and luminosity, requiring the Pillow library.

```py
from faker import Faker

fake = Faker()

print(fake.image())

# result : b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x01\x00\x00\x00\x01\x00...
```
