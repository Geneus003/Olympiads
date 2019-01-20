a = int(input())

def main_f():
  a, b, c = input().split(" ")
  a = int(a)

  if len(b) > len(c):
    max_st = b
    min_st = c
  else:
    max_st = c
    min_st = b
  
  if max_st.find(min_st) == 0:
    a -= len(max_st) - len(min_st)
    if a >= 0 and a % 2 == 0 :
      return "Yes"
    return "No"

  t = 0

  for i in range(len(min_st)):
    if min_st[i] != max_st[i]:
      t = i
      break
  
  a -= len(b) - t
  a -= len(c) - t

  if a >= 0 and (a % 2 == 0 or a == 0):
    return "Yes"
  return "No"
  

for i in range(a):
  print(main_f())
