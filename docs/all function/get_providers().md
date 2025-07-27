# **GET_PROVIDERS** function

Retrieves a list of all available provider objects for generating synthetic data.

```py
from faker import Faker

fake = Faker()

print(fake.get_providers())

# result : [<faker.providers.user_agent.Provider object at 0x000001772002A270>, <faker.providers.ssn.en_US.Provider object at 0x000001772002A120>, <faker.providers.sbn.Provider object at 0x0000017720029FD0>, <faker.providers.python.Provider object at 0x0000017720029E80>, <faker.providers.profile.Provider object at 0x0000017720029D30>, <faker.providers.phone_number.en_US.Provider object at 0x0000017720029BE0>, <faker.providers.person.en_US.Provider object at 0x0000017720029A90>, <faker.providers.passport.en_US.Provider object at 0x0000017720029940>, <faker.providers.misc.en_US.Provider object at 0x00000177200296A0>, <faker.providers.lorem.en_US.Provider object at 0x0000017720029550>, <faker.providers.job.en_US.Provider object at 0x0000017720029400>, <faker.providers.isbn.en_US.Provider object at 0x00000177200292B0>, <faker.providers.internet.en_US.Provider object at 0x0000017720029160>, <faker.providers.geo.en_US.Provider object at 0x0000017720029010>, <faker.providers.file.Provider object at 0x0000017720028EC0>, <faker.providers.emoji.Provider object at 0x0000017720028D70>, <faker.providers.doi.Provider object at 0x0000017720028C20>, <faker.providers.date_time.en_US.Provider object at 0x0000017720028AD0>, <faker.providers.currency.en_US.Provider object at 0x0000017720028980>, <faker.providers.credit_card.en_US.Provider object at 0x0000017720028830>, <faker.providers.company.en_US.Provider object at 0x00000177200286E0>, <faker.providers.color.en_US.Provider object at 0x0000017720028590>, <faker.providers.barcode.en_US.Provider object at 0x0000017720028440>, <faker.providers.bank.en_GB.Provider object at 0x00000177200281A0>, <faker.providers.automotive.en_US.Provider object at 0x0000017720028050>, <faker.providers.address.en_US.Provider object at 0x000001771FF47E00>]
```
