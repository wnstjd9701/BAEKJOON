# command = input()
# print(command.startswith('push_back'))
# print(command)
# print(command.split())

s = 'abcdefg'
s.endswith('c') # False
s.endswith('g') # True
s.endswith('c', 0, 10) # False
print(s.endswith('c', 0, 3)) # True

