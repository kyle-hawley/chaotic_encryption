def atob(m):
  return "".join("{1:0{0}b}".format(8, ord(c)) for c in m)

def iterateLogMap(x_n, a):
  return a * x_n * (1 - x_n)

def createKeySeq(length, c=0.5):

  keySeq = ""
  oldX = x0

  # transient buffer
  for _ in range(10000):
    newX = iterateLogMap(oldX, 4)
    oldX = newX

  for _ in range(length):
    newX = iterateLogMap(oldX, 4)
    oldX = newX

    if oldX < c:
      newBit = "0"
    else:
      newBit = "1"

    keySeq += newBit

  return keySeq

def xor(x, y):
    return '{1:0{0}b}'.format(len(x), int(x, 2) ^ int(y, 2))

message = 'Hi'
x0 = 0.89

binary_message = atob(message)
print("binary", binary_message)

keySeq = createKeySeq(len(binary_message))
print("keySeq", keySeq)

binary_cipher = xor(binary_message, keySeq)
print("binCip", binary_cipher)