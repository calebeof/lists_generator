begin = True
end = False
code = ''
string = 'abcdefghijklmnopqrstuvxyz'
for i in range (945, 970):
  string+=chr(i) #adding the greek alphabet 

while end==False:
  n = ''
  c = '0'
  char = input('Enter #Q for a question or #Q1 for a question with letters: ')
  if char == 'Q' or char =='#Q':
    while n in string:
      n = input('What is the question\'s number? ')
    if begin == True:
      code+='<en-note>'
    code +=('<div><en-todo checked="false"/>Questão {}<br/></div>'.format(int(n)))
  elif char == 'Q1' or char == '#Q1':
    while n in string:
      n = input('What is the question\'s number? ')
    while c not in string:
      c = input('What is the last letter in the question? ')
    if begin == True:
      code+='<en-note>'
    code+=('<div><ul><li><div>Questão {}</div></li></ul><div><br/></div></div>'.format(int(n)))
    flag = False
    i=0
    while flag == False:
      code+=('<div><en-todo checked="false"/>{})</div>'.format(string[i]))
      if string[i]==c:
        flag = True
      i+=1
  continuing = input('\nDo you want to continue? Write Y or N')
  
  if continuing == 'N':
    code+='</en-note>'
    end = True
  else:
    begin = False
    
print(code)
