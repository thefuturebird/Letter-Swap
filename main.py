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

   
  

    
    
    
word_path = ['house', 'touse', 'torse', 'terse', 'tease', 'tense', 'cense', 'dense', 'lense', 'mense', 'terce', 'terne', 'perse', 'cease', 'chase', 'fease', 'lease', 'feaze', 'fesse', 'pease', 'leave', 'lyase', 'leash', 'manse', 'sense', 'kerne', 'torte', 'forte', 'porte', 'bouse', 'douse', 'louse', 'mouse', 'rouse', 'souse', 'corse', 'carse', 'copse', 'curse', 'gorse', 'horse', 'goose', 'gorge', 'worse', 'hoise', 'horde', 'horst', 'torsi', 'tarsi', 'torii', 'torsk', 'torso', 'parse', 'parle', 'marse', 'paise', 'parge', 'parve', 'passe', 'pause', 'peace', 'peage', 'peise', 'phase', 'poise', 'prise', 'purse', 'burse', 'nurse', 'pulse', 'puree', 'purge', 'force', 'farce', 'forge', 'forme', 'forth', 'firth', 'forts', 'forty', 'north', 'farts', 'torts', 'borts', 'fonts', 'foots', 'forbs', 'fords', 'fores', 'forks', 'forms', 'morts', 'ports', 'sorts', 'boule', 'bogle', 'joule', 'bowse', 'dowse', 'douce', 'druse', 'loose', 'louie', 'loupe', 'lowse', 'youse', 'moose', 'reuse', 'roose', 'rouge', 'route', 'deuce', 'dolce', 'dowie', 'cruse', 'noise', 'looie', 'noose', 'coupe', 'gouge', 'routh', 'carle', 'cable', 'table']



print(word_path)
    
p=word_list(word_path)
for w in word_path:
  k=word(w)
  jump=p-w
  print(jump)






