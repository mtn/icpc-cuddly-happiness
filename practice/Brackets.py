
def isValid(string, nesting=0):

  # if the string is empty then it is valid
  if not string: return nesting == 0, ""

  if string[0] == ")": return nesting != 0, string

  if string[0] == "(":
    prevString = string
    valid, string = isValid(string[1:], nesting+1)
    if valid:
      string = string[1:]
    else:
      return False, prevString, string
  return isValid(string, nesting)

# This is too hard

print(isValid("((((()))))((()))"))
print(isValid("(()(())(()))(())"))
print(isValid("()))(()"))
