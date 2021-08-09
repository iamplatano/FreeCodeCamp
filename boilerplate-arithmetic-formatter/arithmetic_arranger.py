def arithmetic_arranger(problems,answers=False):
  arranged_problems = ""
  
  if(len(problems) >5):
    return "Error: Too many problems."
  for problem in problems:
    temp = problem.split()
    num1 = temp[0]
    num2 = temp[2]
    if len(num1) >= 5 or len(num2) >= 5:
      return "Error: Numbers cannot be more than four digits."
    elif (not num1.isnumeric() or not num2.isnumeric()):
      return "Error: Numbers must only contain digits."
    elif(len(num2) > len(num1)):
      arranged_problems += '{:>{length}s}'.format(temp[0],length = 2+len(num2))
    elif(len(num2) <= len(num1)):
      arranged_problems += '{:>{length}s}'.format(temp[0],length = 2+len(num1))
    if problem != problems[len(problems)-1]:
      arranged_problems += '    '
  
  arranged_problems += '\n'

  for problem in problems:
    temp = problem.split()
    num1 = temp[0]
    num2 = temp[2]
    sign = temp[1]
    if len(num1) >= 5 or len(num2) >= 5:
      return "Error: Numbers cannot be more than four digits."
    elif sign != '+' and sign != '-':
      return "Error: Operator must be '+' or '-'."
    elif(len(num2) > len(num1)):
      arranged_problems += '{sign} '.format(sign=temp[1])
      arranged_problems += '{:>{length}s}'.format(num2,length = len(num2))
    elif(len(num2) <= len(num1)) :
      arranged_problems += '{sign} '.format(sign=temp[1])
      arranged_problems += '{:>{length}s}'.format(num2,length = len(num1))
    if problem != problems[len(problems)-1]:
      arranged_problems += '    '
  arranged_problems += '\n'

  for problem in problems:
    temp = problem.split()
    arranged_problems += '{0:->{length}s}'.format("",length= 2+ max(len(temp[0]),len(temp[2])))
    if problem != problems[len(problems)-1]:
      arranged_problems += '    '

  if answers == True:
    arranged_problems += '\n'
    for problem in problems:
      temp = problem.split()
      if temp[1] == '+':
        answer = int(temp[0]) + int(temp[2])
        arranged_problems += '{:>{length}d}'.format(answer,length= 2+ max(len(temp[0]),len(temp[2])))
      elif temp[1] == '-':
        answer = int(temp[0]) - int(temp[2])
        arranged_problems += '{:>{length}d}'.format(answer,length= 2+ max(len(temp[0]),len(temp[2])))
      if problem != problems[len(problems)-1]:
        arranged_problems += '    '
  return arranged_problems