with open('tests/utils/test_utils.py', 'r') as f:
    content = f.read()

# Find and update the expected_providers list
# Look for where 'faker.providers.person' appears and insert 'faker.providers.passport' before it
lines = content.split('\n')
for i, line in enumerate(lines):
    if "'faker.providers.person'" in line and "'faker.providers.passport'" not in lines[i-1]:
        # Insert passport before person
        lines.insert(i, "            'faker.providers.passport',")
        break

content = '\n'.join(lines)
with open('tests/utils/test_utils.py', 'w') as f:
    f.write(content)
    
print("Updated expected providers list")
