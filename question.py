
def recurse(c):
  try:
    while c>0:
      print(c)
      c-=1
      if c==2:
        raise StopIteration

    recurse(c-1)
                  
  except StopIteration:
    print("We found the word. Stop the recursion.")
  
  
recurse(20)