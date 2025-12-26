with open('tests/utils/test_utils.py', 'r') as f:
    lines = f.readlines()

# Find where to insert 'faker.providers.passport'
for i, line in enumerate(lines):
    if "'faker.providers.person'" in line:
        # Insert passport before person (alphabetical order)
        lines.insert(i, "        'faker.providers.passport',\n")
        break

with open('tests/utils/test_utils.py', 'w') as f:
    f.writelines(lines)

print("Added passport to expected providers list")
