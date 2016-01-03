def digit_seven(money_digit_seven):
  money_words = ''
  if digit_two(money_digit_seven[0:2]):
    money_words = digit_two(money_digit_seven[0:2])+'Lakh'
  if digit_five(money_digit_seven[2:]):
    if int(money_digit_seven[2:4]) != 00: #adds a comma if there is a thousands component in the number
  	  money_words = money_words+', '
    money_words = money_words+digit_five(money_digit_seven[2:])
  return money_words

def digit_six(money_digit_six):
  money_words = ''
  if digit_one(money_digit_six[0]):
    money_words = money_words+digit_one(money_digit_six[0])+'Lakh'
  if digit_five(money_digit_six[1:]):
  	if int(money_digit_six[1:3]) != 00:
  	  money_words = money_words+', ' #adds a comma if there is a thousands component in the number
  	money_words = money_words+digit_five(money_digit_six[1:])
  return money_words

def digit_five(money_digit_five):
  money_words = ''
  if digit_two(money_digit_five[0:2]):
    money_words = digit_two(money_digit_five[0:2])+'Thousand'
  if digit_three(money_digit_five[2:]):
    money_words = money_words+', '
    if int(money_digit_five[2])==0: #adds an and if there is no hundreds component in the number
      money_words = money_words+'and '
    money_words = money_words+digit_three(money_digit_five[2:])
  return money_words

def digit_four(money_digit_four):
  money_words = ''
  if digit_one(money_digit_four[0]):
  	money_words = digit_one(money_digit_four[0])+'Thousand'
  if digit_three(money_digit_four[1:]):
    money_words = money_words+', '
    if int(money_digit_four[1])==0: #adds an and if there is no hundreds component in the number
      money_words = money_words+'and '
    money_words = money_words+digit_three(money_digit_four[1:])
  return money_words

def digit_three(money_digit_three):
  money_words = ''
  if digit_one(money_digit_three[0]):
    money_words = digit_one(money_digit_three[0])+'Hundred'
  if digit_two(money_digit_three[1:]):
    if money_words:
      money_words = money_words+', and '
    money_words = money_words+digit_two(money_digit_three[1:])
  return money_words

def digit_two(money_digit_two):
  if int(money_digit_two[0]) == 1:
  	money_digit_two = int(money_digit_two)
  	if money_digit_two == 00:
  	  return ''
  	elif money_digit_two == 10:
  	  return 'Ten '
  	elif money_digit_two == 11:
  	  return 'Eleven '
  	elif money_digit_two == 12:
  	  return 'Twelve '
  	elif money_digit_two == 13:
  	  return 'Thirteen '
  	elif money_digit_two == 14:
  	  return 'Fourteen '
  	elif money_digit_two == 15:
  	  return 'Fifteen '
  	elif money_digit_two == 16:
  	  return 'Sixteen '
  	elif money_digit_two == 17:
  	  return 'Seventeen '
  	elif money_digit_two == 18:
  	  return 'Eighteen '
  	elif money_digit_two == 19:
  	  return 'Nineteen '
  elif int(money_digit_two[0]) == 2:
    return 'Twenty '+digit_one(money_digit_two[1])
  elif int(money_digit_two[0]) == 3:
    return 'Thirty '+digit_one(money_digit_two[1])
  elif int(money_digit_two[0]) == 4:
    return 'Fourty '+digit_one(money_digit_two[1])
  elif int(money_digit_two[0]) == 5:
    return 'Fifty '+digit_one(money_digit_two[1])
  elif int(money_digit_two[0]) == 6:
    return 'Sixty '+digit_one(money_digit_two[1])
  elif int(money_digit_two[0]) == 7:
    return 'Seventy '+digit_one(money_digit_two[1])
  elif int(money_digit_two[0]) == 8:
    return 'Eighty '+digit_one(money_digit_two[1])
  elif int(money_digit_two[0]) == 9:
    return 'Ninety '+digit_one(money_digit_two[1])
  elif int(money_digit_two[0]) == 0:
    return digit_one(money_digit_two[1])

def digit_one(money_digit_one):
  money_digit_one = int(money_digit_one)
  if money_digit_one == 1:
    return 'One '
  elif money_digit_one == 2:
    return 'Two '
  elif money_digit_one == 3:
    return 'Three '
  elif money_digit_one == 4:
    return 'Four '
  elif money_digit_one == 5:
    return 'Five '
  elif money_digit_one == 6:
    return 'Six '
  elif money_digit_one == 7:
    return 'Seven '
  elif money_digit_one == 8:
    return 'Eight '
  elif money_digit_one == 9:
    return 'Nine '
  elif money_digit_one == 0:
    return ''

def main(money_int):
  length = len(money_int)
  if length == 0 or length>7:
    print 'Please enter a valid amount between 1 to 9999999'
  elif length == 1:
  	print  digit_one(money_int)
  elif length == 2:
    print digit_two(money_int)
  elif length == 3:
    print digit_three(money_int)
  elif length == 4:
    print digit_four(money_int)
  elif length == 5:
    print digit_five(money_int)
  elif length == 6:
    print digit_six(money_int)
  elif length == 7:
    print digit_seven(money_int)

if __name__ == '__main__':
  money_int = raw_input('Please enter the amount: ')
  main(money_int)