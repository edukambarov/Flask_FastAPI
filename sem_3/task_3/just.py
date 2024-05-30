def check_it(text):
    splitted = [ch for ch in text]
    print(splitted)
    for ch in splitted:
        if ch.isdigit():
            splitted.remove(ch)
            break
    for ch in splitted:
        if ch.isalpha():
            print('OK')
            break
    else:
        print('Password must consist at least 1 letter and 1 digit')


check_it('1234567s')