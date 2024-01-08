#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        return len(sentence), None
    return len(sentence), sentence[0]


'''Alternatively using list comprehension
    return (len(sentence), sentence[0] if len(sentence) > 0 else None)'''
