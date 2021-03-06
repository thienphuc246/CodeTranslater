import string
import CodeTranslater

if __name__ == '__main__' :

    print("----------------------------------------------------------------------------------------------------------------")
    print("--------------------------------------------------Made by Phien-------------------------------------------------")
    print("Options: \n\n Encode Ceasar Code (1) \n\n Decode Ceasar Code (2) \n\n Encode VigenegeCode (3) \n\n Quit (9) \n\n")
    open = True
    while open :
        Option = int(input("Option: "))
        if Option == 9: 
            open = False
        if Option == 1:
            text = input("Text you want to encode: ")
            shift = int(input("Step to fall back: "))
            print("Encoded CeasarCode:", CodeTranslater.EncodeCeasarCode(text,shift,[string.ascii_uppercase, string.ascii_lowercase, string.punctuation]))
        if Option == 2:
            text = input("Code you want to decode: ")
            print("Decoded CeasarCode:", CodeTranslater.DecodeCeasarCode(text,[string.ascii_lowercase, string.ascii_uppercase, string.punctuation]))
        if Option == 3:
            code = input("Code you want to decode: ")
            key = input("Key: ")
            if len(code) != len(key):
                print("Error!!")
            else:
                print("Decoded Vigenege Code:", CodeTranslater.DecodeVigenege(code, key))
        

