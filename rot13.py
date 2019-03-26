#https://www.codewars.com/kata/rot13-1/python

alphabet = [a-z, A-Z]

def rot13(message):
    message = message.split()
    for charachter in message:
        if charachter in alphabet:
            message.append()
        else:
            message.append(charachter)