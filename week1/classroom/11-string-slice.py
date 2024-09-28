text = 'Welcome to Golang Course at URBE'


'''
w 0
e 1
l 2
c 3
o 4
m 5
e 6
  7
t 8
o 9
  10
g 11
'''

print(text[2:5])

g_index = text.lower().index('g')
print(g_index)

print(text[g_index:])

#reverse
print(text[::-1])