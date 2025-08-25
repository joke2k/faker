from faker import Faker

# Igbo provider
fake_ig = Faker("ig_NG")
print("Igbo samples:")
for _ in range(5):
    print(fake_ig.name())

# Hausa provider
fake_ha = Faker("ha_NG")
print("\nHausa samples:")
for _ in range(5):
    print(fake_ha.name())

# English-Nigerian provider
fake_en_ng = Faker("en_NG")
print("\nEnglish-Nigerian samples:")
for _ in range(5):
    print(fake_en_ng.name())

# Yoruba provider (already exists, just for comparison)
fake_yo = Faker("yo_NG")
print("\nYoruba samples:")
for _ in range(5):
    print(fake_yo.name())
