# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 12:09:02 2019

@author: Phalin Pancholi
"""

def encrypt(text,n):
    """Assumes text to be a string and n to be int
       returns string in encoded form taking every 2nd character first and
       then taking every non-2nd character, this happens for n time
    """
    if n <= 0:
        return text
    else:
        return encrypt(text[1::2] + text[0::2],n-1)
def decrypt(encrypted_text,n):
    """ Assumes encrypyed_text to be string that has passed through encrypt
        method and n number of times encrypted_text to be decrypted
        returns a string that when passed through encrypt method returns 
        encrypted_text
    """
    if n <= 0:
        return encrypted_text
    else:
        temp_list=[]
        for i in range(0,len(encrypted_text)//2):
            temp_list.append(encrypted_text[i + (len(encrypted_text)//2)])
            temp_list.append(encrypted_text[i])
        if len(encrypted_text) % 2 != 0:
            temp_list.append(encrypted_text[-1])
        encrypted_text = "".join(temp_list)
        return decrypt(encrypted_text,n-1)