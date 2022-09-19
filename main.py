# Format xxxx-xxxx
# not use regular expression find text pattern
def is_phone_number(text):
    if len(text) != 9:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[4] != '-':
        return False
    for i in range(5, 8):
        if not text[i].isdecimal():
            return False

    return True


phoneNumber = str(input('enter a string:'))
if is_phone_number(phoneNumber):
    print(phoneNumber + ' is a phone number.')
else:
    print(phoneNumber + ' is not a phone number.')

phoneNumber = str(input('enter a string:'))
if is_phone_number(phoneNumber):
    print(phoneNumber + ' is phone number.')
else:
    print(phoneNumber + ' is not a phone number.')
