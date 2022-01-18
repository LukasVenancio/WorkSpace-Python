studentName = input('What is the name of the student?')
firstNote = float(input('What is the first note of {}?' .format(studentName)))
secondNote = float(input('What is the second note?'))
average = (firstNote + secondNote) / 2

print('The average of the notes of the student {} is: {} ' .format(studentName, average))
