name = input('What is your name? ')
print('Hello, ' + name +'!"')
    
name = input('What is your name? ')
print(('Hello, ' + name).upper())
print(('Your name has ' + str(len(name)) + ' letters in it! Awesome!').upper())

print("________'s favorite subject in school is ________.")
name = input('What is name?')
subject = input('What is subject?')
print("{0}'s favorit subject in school is {1}.".format(name, subject))

day = int(input('Day (0-6)? '))
dayOfWeek = ['Sunday', 'Monday', 'Tuesday','Wednesday', 'Thursday', 'Friday', 'Saturday']
print(dayOfWeek[day])

day = int(input('Day (0-6)? '))
if day == 0 or day == 6:
  print("Sleep in")
else:
  print("Go to work")