"""General Patron is faced with a problem , his intelligence has intercepted some secret messages from the enemy but they are all encrypted. Those messages are crucial to getting the jump on the enemy and winning the war. Luckily intelligence also captured an encoding device as well. However even the smartest programmers weren't able to crack it though. So the general is asking you , his most odd but brilliant programmer.

You can call the encoder like this.

encode("Hello World!")
Our cryptoanalysts kept poking at it and found some interesting patterns.

print(
encode("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
print(
encode("bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"))
print(encode("!@#$%^&*()_+-"))
a,b,c = "", "", ""
for w in "abcdefghijklmnopqrstuvwxyz":
    a += encode(  "" + w)[0]
    b += encode( "_" + w)[1]
    c += encode("__" + w)[2]
print(a)
print(b)
print(c)
We think if you keep on this trail you should be able to crack the code! You are expected to fill in the

decode
function. Good luck ! General Patron is counting on you!"""

SYMBOLS = "яabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,? "


def encode(s):
    result = ''
    for i in range(len(s)):
        if SYMBOLS.find(s[i]) != -1:
            result += SYMBOLS[((SYMBOLS.find(s[i])) * 2 ** (i + 1)) % len(SYMBOLS)]
        else:
            result += s[i]
    return result


def decode(s):
    result = ''
    for i in range(len(s)):
        multiply = 0
        if SYMBOLS.find(s[i]) != -1:
            index = SYMBOLS.find(s[i])
            if index % 2:
                multiply = 1
            if 2 ** (i + 1) / len(SYMBOLS) > 1:
                multiply += 2 ** (i + 1) // len(SYMBOLS) - ((2 ** (i + 1) // len(SYMBOLS)) % 2)
            while (index + len(SYMBOLS) * multiply) % 2 ** (i + 1):
                if 2 ** (i + 1) / len(SYMBOLS) > 1:
                    a = (2 ** (i + 1) - ((index + len(SYMBOLS) * multiply) % 2 ** (i + 1))) // len(SYMBOLS)
                    if a > 2:
                        multiply += a
                    else:
                        multiply += 2
                else:
                    multiply += 2
            result += SYMBOLS[int((index + len(SYMBOLS) * multiply) / 2 ** (i + 1))]
        else:
            result += s[i]
    return result


def cheatdecode(s):
    for x in range(65):
        s = encode(s)
    return s

def bestdecode(s):
    decrypted_message = ''
    i = 0
    key = "bdhpF,82QsLirJejtNmzZKgnB3SwTyXG ?.6YIcflxVC5WE94UA1OoD70MkvRuPqHa"

    for char in s:
        i += 1
        if char not in key:
            decrypted_message += char
            continue
            
        idx = (key.index(char) - i) % 66
        decrypted_message += key[idx]
        
    return decrypted_message


print(encode('Hello World!'))
print(decode('atC5kcOuKAr!'))
print(cheatdecode('atC5kcOuKAr!'))
print(bestdecode('atC5kcOuKAr!'))
