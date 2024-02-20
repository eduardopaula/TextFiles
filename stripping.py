filename = 'Jabberwocky.txt'
with open(filename) as poem:
    first = poem.readline().rstrip()

print(first)

chars = "' Twasebv"
# no_apostrophe = first.strip(chars)
# print(no_apostrophe)

print('*' * 80)
print(first)
print(chars)
for character in first:
    if character in chars:
        print(f'removing "{character}"')
    else:
        break

print('*' * 80)
print(first)
print(chars)
for character in first[::-1]:  # process backwards
    if character in chars:
        print(f'removing "{character}"')
    else:
        break
