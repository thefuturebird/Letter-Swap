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
  def __sub__(self, other): 
    return letter_difference(self,other)
  def __rsub__(self,other):
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
    
    find_path(current_neighbors,current_word,min_distance+1)
  except StopIteration:
      print("We found the word. Stop the recursion.")
  
  
  print(word_path)
    
    
    
word_path = ['house', 'touse', 'torse', 'terse', 'tease', 'tense', 'cense', 'dense', 'lense', 'mense', 'terce', 'terne', 'perse', 'cease', 'chase', 'fease', 'lease', 'feaze', 'fesse', 'pease', 'leave', 'lyase', 'leash', 'manse', 'sense', 'kerne', 'torte', 'forte', 'porte', 'bouse', 'douse', 'louse', 'mouse', 'rouse', 'souse', 'corse', 'carse', 'copse', 'curse', 'gorse', 'horse', 'goose', 'gorge', 'worse', 'hoise', 'horde', 'horst', 'torsi', 'tarsi', 'torii', 'torsk', 'torso', 'parse', 'parle', 'marse', 'paise', 'parge', 'parve', 'passe', 'pause', 'peace', 'peage', 'peise', 'phase', 'poise', 'prise', 'purse', 'burse', 'nurse', 'pulse', 'puree', 'purge', 'force', 'farce', 'forge', 'forme', 'forth', 'firth', 'forts', 'forty', 'north', 'farts', 'torts', 'borts', 'fonts', 'foots', 'forbs', 'fords', 'fores', 'forks', 'forms', 'morts', 'ports', 'sorts', 'boule', 'bogle', 'joule', 'bowse', 'dowse', 'douce', 'druse', 'loose', 'louie', 'loupe', 'lowse', 'youse', 'moose', 'reuse', 'roose', 'rouge', 'route', 'deuce', 'dolce', 'dowie', 'cruse', 'noise', 'looie', 'noose', 'coupe', 'gouge', 'routh', 'carle', 'cable', 'table']




    

direct_list=[word_path[0]]

w2=word("table")



def next_best(last_word):
  
  jump=word_list(word_path)-word(last_word)
  best=0
  for j in range(len(jump)):
    if jump[j]==1:
      best=j

  if word(direct_list[len(direct_list)-1])-word_path[best]==1:
    direct_list.append(word_path[best])
    word_path.pop(best)
  return word_path[best]

current=word_path[1]

while word(current)-w2>1:
  current=next_best(current)
  print(direct_list)

print(direct_list)
  






