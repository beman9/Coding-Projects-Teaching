import pickle

exit = False
hasOpened = False

with open('todoList.pickle', 'rb') as f:
  todoList = pickle.load(f)

# with open('todoList.pickle', 'wb') as f:
#  pickle.dump(todoList, f)

print(" To-Do List\n")

while exit is False:
  entry = input('What would you like to do?\n a) add\n d) delete\n e) edit\n r) read\n q) quit\n\n')

  if entry == 'a':
    #this will add an item to the list
    todoList.append(input('What would you like to add?\n'))
    with open('todoList.pickle', 'wb') as f:
      pickle.dump(todoList, f)

  elif entry == 'd':
    #this will delete an item from the list
    print()
    i = 0
    for row in todoList:
      print('{}: {}'.format(i, row))
      i = i + 1
    print()
    try:
      deleteNum = int(input('Which number would you like to delete?\n'))
      del todoList[deleteNum]
      with open('todoList.pickle', 'wb') as f:
        pickle.dump(todoList, f)
    except IndexError:
      print('Please try again with a valid number.\n')

  elif entry == 'e':
    #this will edit an item on the list
    print()
    i = 0
    for row in todoList:
      print('{}: {}'.format(i, row))
      i = i + 1
    print()
    try:
      deleteNum = int(input('Which number would you like to edit?\n'))
      del todoList[deleteNum]
      edit = input('What would you like to change it to?\n')
      todoList.insert(deleteNum, edit)
      with open('todoList.pickle', 'wb') as f:
        pickle.dump(todoList, f)
    except ValueError:
      print('Please try again with a valid number.\n')

  elif entry == 'r':
    #this will read the to-do list
    print()
    i = 0
    for row in todoList:
      print('{}: {}'.format(i, row))
      i = i + 1
    print()

  elif entry == 'q':
    break
  else:
    print('Please enter a valid value. ')



