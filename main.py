from word_operations import letter_difference,load, last_line

# library to make formated strings in to lists
import ast

dictionary = load('words.txt')
neighbors_list = load('neighbors.txt')

class word:
  def __init__(self,as_string="",id=-1):    
    if id==-1:
      self.as_string = as_string
      self.id = dictionary.index(self.as_string)
    if as_string=="":
      self.id = id
      self.as_string = dictionary[self.id]
      
  def __str__(self):
    return dictionary[self.id]
  def __len__(self):
    return len(dictionary[self.id])
  def __sub__(self, other): # w1- w2 gives the letter difference between words
    return letter_difference(self,other)
  def __rsub__(self,other): # w1 - word gives letter difference between words and strings
    return letter_difference(self,other)
    
  def list_neighbors_fast(self):
    for nearby_word_list in neighbors_list:
    #make a python list object of the needed line
      indexed_list=ast.literal_eval(nearby_word_list)
      if self==indexed_list[0]:
        return indexed_list
    if indexed_list not in locals():
      return []      
  def list_neighbors(self,distance=1):
    neighbors=[]    
    for v in dictionary:
      if self-v==distance:
        neighbors.append(v)      
    return neighbors



class word_list:
  def __init__(self,list=[]):
    
    self.list=list.copy()
  def __str__(self):
    return str(self.list)
  def __len__(self):
    return len(self.list)
  def __add__(self,other):
    temp=[*self.list]
    for i in other.list:
      if i not in temp:
        temp.append(i)
    return temp
  def __rsub__(self,other):
    temp=[]
    for z in self.list:
      temp.append(other-z)
    return temp
  def __sub__(self,other):
    temp=[]
    for z in self.list:
      temp.append(other-z)
    return temp
  


  def first_minimum_index(self,w):
    if len(self.list)>1:
      index_list=self-w
      min_ele = int(index_list[0])
      response = self.list[0]
      for i in range(len(index_list)):
        
        if int(index_list[i]) < min_ele:
          min_ele = int(index_list[i])
          
          response=self.list[i]
      return response
    else:
      return -1

      
def create_neighbors_list(file_name):
  if len(last_line(file_name))>1:
    last = ast.literal_eval(last_line(file_name))
  else:
    last=['']
       
  start =0 
  for w in dictionary:  
  
    if start==1 or last[0]=="":  
      k=word(w) 
      n=k.list_neighbors()
      n.insert(0,w)
      if len(n)>1:
        line =str(n)+"\n"
        print(line)
        with open(file_name, 'a') as file:
          file.write(line) 
  
    if w==last[0]:
      start=1 
      print(last)
      
#create_neighbors_list('neighbors.txt')


word_one=""
while type(word_one)!=str or word_one not in dictionary:
  word_one = input("Enter first word:")
  if word_one not in dictionary:
    print("Please type a real English word, all lowercase.")

word_two=""

while type(word_two)!=str or len(word_two)!=len(word_one) or word_two==word_one or word_two not in dictionary:
  word_two = input("Enter second distinct\nword that is the same length as your first word:")
  if word_two not in dictionary:
    print("Please type a real English word, all lowercase.")

w1=word(word_one)
w2=word(word_two)
min_distance=w1-w2

print("It will take at least "+ str(min_distance) + " steps\nto transform "+ str(w1) +" to "+ str(w2))

#find both words in neighbor index
for nearby_word_list in neighbors_list:
  #make a python list object of the needed line
  indexed_list=ast.literal_eval(nearby_word_list)
  if word_one==indexed_list[0]:
    print("neighbors of "+ str(w1)+": "+ str(indexed_list))
    w1_neighbors=word_list(indexed_list)    
  
  if word_two==indexed_list[0]:
    w2_neighbors=word_list(indexed_list)

if "w1_neighbors" and "w2_neighbors" in locals():  # only if the words have one-letter neighbors

  remaing_distance = min_distance
  current_word=w1
  current_neighbors=current_word.list_neighbors()
  word_path=[str(w1)]
  print(w1)
  

  def find_path(current_n,current_word,d):
    
      while w2-current_word>1 and len(current_n)>1:
        current_word=word_list(current_n).first_minimum_index(w2)
        current_n.pop(current_n.index(current_word))
        next_neighbors=word(current_word).list_neighbors()
        if current_word not in word_path:
          
          word_path.append(current_word)
          print(current_word)
          if w2-current_word<=1:
            
            word_path.append(str(w2))
            print(w2)
            raise StopIteration
            
  
        if d>0 and w2-current_word>1:
          find_path(next_neighbors,current_word,d-1)
                    
    
    
  try:
    
    find_path(current_neighbors,current_word,min_distance+3)
  except StopIteration:
      print("We found the word. Stop the recursion.")
  
  
  print(word_path)
    
    

path=[str(w1)]
remain=word_path[1:].copy()

def last_in(list):
  if len(list)>0:
    return(list[len(list)-1])
  else:
    ""
def navigate(path,remain):
  f=False
  for i in range(len(remain)):  
    if word(remain[i])-word(last_in(path))==1:
      path.append(remain[i])
      remain.pop(i)
      f=True
      break
  
  if not f:
    path.pop(len(path)-1)

  if word(last_in(path))-last_in(remain)>1:    
    navigate(path,remain)    
 
navigate(path,remain)
path.append(str(w2))
print(path)


snips=[]
for i in range(len(path)):
  t=0
  for j in range(len(path)):
    if word(path[i])-path[j]==1 and j-i>1:
      t=j
  if t>0:
    print(str(i)+ " " +path[i])
    print(str(t)+ " " +path[t])
    snips.append([i,t])



print(snips)  

def sort_shorts(snips):
  if len(snips[1:])>1: 
    best=1
    bestid=0
    for i in range(len(snips)):
      if snips[i][1]-snips[i][0]>best:
        best=snips[i][1]-snips[i][0]
        bestid=i
    
    
    snips.insert(0,snips.pop(bestid))
    
    snips=snips[0]+sort_shorts(snips[1:])
    return snips
  else:
    return []
    
print(snips)  
  


    
cut_list=[]

for snip in snips:
  i=snip[0]
  
  j=snip[1]
  
  print(path[i] + " " + path[j])
  for k in range(i+1,j):
    print(path[k])
    if path[k] not in cut_list and path[i] not in cut_list:
      cut_list.append(path[k])


for w in cut_list:

  path.remove(w)
  
print(path)

  






