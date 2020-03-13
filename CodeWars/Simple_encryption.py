def decrypt(encrypted_text:str, n:int) -> str:
    """
    Returns the original String that is encrypted using encrypt
    """
    while n > 0:
        text_list = list(encrypted_text)
        second_element = text_list[:len(text_list)//2]
        print(second_element,end="\n")
        other_element = text_list[len(text_list)//2:]
        print(other_element,end="\n")
        final_string = ""
        for i in range(len(text_list)//2):
            final_string += (other_element[i] + second_element[i])
        if(i < len(other_element)):
            for e in other_element[i+1:]:
                final_string += e
        n -= 1
        encrypted_text = final_string
    return encrypted_text


def encrypt(text:str, n:int) -> str:
    """
    Every second word in text is concatinated with other words 
    and the process is repeated for n times
    """
    while n > 0:
        s = text[1::2] + text[::2]
        text = s
        n -= 1
    return text

print(decrypt("hsi  etTi sats!",1))
print(decrypt("s eT ashi tist!", 2))
print(decrypt("hskt svr neetn!Ti aai eyitrsig",1))
print(encrypt("This is a test!",2))