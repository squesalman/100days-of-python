#%%
import os


with open('test_file.txt', 'a') as f:
  #read_date = f.read()
  # for line in f:
  #   print(line, end='')
  #print(read_date)
  f.writelines('\nThis is line 5')

with open('test_file.txt','r') as g:
  for line in g:
    print(line, end='')
f.closed
g.closed



# %%
import os

my_dir = os.open('C:\\Users\\mshafique.salman\\OneDrive - PETRONAS\\Documents\\Python\\100days-Exercise\\test_folder',os.O_RDONLY)

def opener(path,flags):
  return os.open(path,flags,dir_fd=my_dir)

with open('test_file_diff.txt','a',opener=opener) as f:
  print('This will be written to test_file_diff.txt',file=f)

os.close(my_dir)

# %%