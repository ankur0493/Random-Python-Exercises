def length_three(number_in):
  letter = ''
  letter = length_one(((number_in-26)/676)-1)+length_two(((number_in-26)%676)+26)
  return letter

def length_two(number_in):
  letter = ''
  letter = length_one(number_in/26-1)+length_one(number_in%26)
  return letter

def length_one(number_in):
  letter = ''
  if number_in == 0:
    letter = 'A'
  if number_in == 1:
    letter = 'B'
  if number_in == 2:
    letter = 'C'
  if number_in == 3:
    letter = 'D'
  if number_in == 4:
    letter = 'E'
  if number_in == 5:
    letter = 'F'
  if number_in == 6:
    letter = 'G'
  if number_in == 7:
    letter = 'H'
  if number_in == 8:
    letter = 'I'
  if number_in == 9:
    letter = 'J'
  if number_in == 10:
    letter = 'K'
  if number_in == 11:
    letter = 'L'
  if number_in == 12:
    letter = 'M'
  if number_in == 13:
    letter = 'N'
  if number_in == 14:
    letter = 'O'
  if number_in == 15:
    letter = 'P'
  if number_in == 16:
    letter = 'Q'
  if number_in == 17:
    letter = 'R'
  if number_in == 18:
    letter = 'S'
  if number_in == 19:
    letter = 'T'
  if number_in == 20:
    letter = 'U'
  if number_in == 21:
    letter = 'V'
  if number_in == 22:
    letter = 'W'
  if number_in == 23:
    letter = 'X'
  if number_in == 24:
    letter = 'Y'
  if number_in == 25:
    letter = 'Z'  
  return letter

def main(number_in):
  number = int(number_in)
  letter = ''
  length = len(number_in)
  if number>701:
    print length_three(number)
  elif number>25:
    print length_two(number)
  else:
    print length_one(number)

if __name__ == '__main__':
  number_in = raw_input('Please enter the number: ')
  main(number_in)