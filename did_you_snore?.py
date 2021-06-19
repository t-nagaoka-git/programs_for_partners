from tkinter import messagebox

hate = 0
while True:
  result = messagebox.askyesno('confirm', 'Did you snore ?')
  if result == True:
    hate += 1

    if hate % 100 == 0:
      break

    continue

  print('I love you')