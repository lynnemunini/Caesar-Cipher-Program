alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ["1","2","3","4","5","6","7","8","9"]
import art
print(art.logo)

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    
    if char in numbers:
      end_text += char
    elif char == "/":
      end_text += "/"
    elif char == " ":
      end_text += " "
    else:
      position = alphabet.index(char)
      new_position = position + shift_amount
      if new_position>len(alphabet):
       new_position=new_position%len(alphabet)
      end_text += alphabet[new_position]
  print(f"Here's the {cipher_direction}d result: {end_text}")

stop = False
while not stop:
  direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift%26
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
  start = input("\n\nDo you want to restart the cipher program? Type 'yes' if you want to go again. Otherwise type 'no':\n").lower()
  if start == "no":
    stop = True
    print("\nGoodbye👋")
    



