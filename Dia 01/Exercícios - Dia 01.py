def maximo(n1, n2):
  if n1 > n2:
    return n1
  else:
    return n2

print(maximo(98, 8885))

#########################################

def maximo(n1, n2):
  if n1 % n2 == 0:
    return True

print(maximo(4, 2))

#########################################

def maximo(lado):
  return lado * lado

print(maximo(4))