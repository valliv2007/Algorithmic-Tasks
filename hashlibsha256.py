from hashlib import sha256
string = '64113889'+";"+"hayatbeauty"+";"+"e8b1eaa33b376b1150360182efdc6d06"
stringswa = "hayatbeauty"+';'+'50'+';'+'e8b1eaa33b376b1150360182efdc6d06'

print(sha256(stringswa.encode()).hexdigest())