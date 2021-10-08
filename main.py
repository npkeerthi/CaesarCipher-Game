# logo = """           
#  ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
# a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
# 8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
# "8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
#  `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
#             88             88                                 
#            ""             88                                 
#                           88                                 
#  ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
# a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
# 8b         88 88       d8 88       88 8PP""""""" 88          
# "8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
#  `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
#               88                                             
#               88           
# """

from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(text, shift):
  cip= ""
  for i in text:
    if i in alphabet:  #for special char to ignore
      f= alphabet.index(i)
      if direction=="decode":
        newf= f-shift
      # print(newf)
      else:
        newf=f+shift
      cip += alphabet[newf]
    else:
      cip += i
  print(f"\nThe {direction}d text is {cip}")

repeat=True
while repeat:
  direction = input("\nType 'encode' to encrypt \nType 'decode' to decrypt\n\nType Here :").lower()
  ttext = input(f"\nType your message to {direction} it:\n").lower()
  sshift = int(input("\nType the shift number:\n"))
  if sshift>26:
    sshift=sshift % 26

  caesar(text=ttext,shift=sshift)

  again=input("\nDo you want to restart the cipher program ?\nEither to encode or decode this again?\n        'yes' or 'no' :").lower()
  if again=="no":
    repeat=False
    print("Good Bye")

