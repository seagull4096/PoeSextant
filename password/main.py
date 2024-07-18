def AtoN(char):
    return ord(char) - 65


def NtoA(char):
    return chr(char + 65)


class Location:
    def __init__(self, loc_x, loc_y):
        self.x = loc_x
        self.y = loc_y


password = 2024030120240329
password = list(str(password))
pwa = password[:8]
pwb = password[8:]
pwa = int(''.join(pwb)) - int(''.join(pwa))
pwa = list(format(pwa, "04"))
for i in range(len(pwa)):
    password.append(pwa[i])

print(password)
temp = []
for i in range(5):
    temp.append([int(password[i*4 + 0]), int(password[i*4 + 1]), int(password[i*4 + 2]), int(password[i*4 + 3])])

password = []
for i in range(20):
    password.append(temp[i%5][i//5])

print(password)

for i in range(len(password) // 2):
    password[i] = password[i] + password[19 - i]

for i in range(len(password)):
    if password[19 - i] + i % 2 == 0:
        password[i] = 25 - password[i]

for i in range(len(password)):
    password[i] = NtoA(password[i])

password = ''.join(password)
print(password)
print(temp)
