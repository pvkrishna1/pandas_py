def myfunc():
  x = 300
  print("in my func")
  def myinnerfunc():
    print(x)
    print("in inner func")
  myinnerfunc()

myfunc()
