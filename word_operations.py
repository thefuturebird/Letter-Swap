import sys

def load(file):
  """Open a text file & return a list of lowercase strings."""
  try:
    with open(file) as in_file:
      loaded_txt = in_file.read().strip().split('\n')
      loaded_txt = [x.lower() for x in loaded_txt if len(x) > 1]
      return loaded_txt
  except IOError as e:
    print("{}\nError opening {}. Terminating program.".format(e, file),
          file=sys.stderr)
    sys.exit(1)

def last_line(file_name):
  l=""
  with open(file_name) as f:
    for line in f:
        l=line
    return l

def letter_difference(word_one,word_two):
  if len(word_one) == len(word_two):
    count_diffs = 0
    for a, b in zip(str(word_one), str(word_two)): #zip words to letter arrays
      if a != b:
        count_diffs += 1
    return count_diffs
  else:
    return -1 #if they aren't the same length

