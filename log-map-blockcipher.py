from math import sqrt
def atob(m):
  return "".join("{1:0{0}b}".format(8, ord(c)) for c in m)

def iterateLogMap(x_n, a):
  return a * x_n * (1 - x_n)

def inverseLogMap(x_n):
  """Only uses a=4, quick and dirty"""

  if x_n < 0.5:
    print("x < 0.5")
    return 0.5 * (1 + sqrt(1-x_n))
  else:
    print("x > 0.5")
    return 0.5 * (1 - sqrt(1-x_n))

def createKeySeq(length, c=0.5):

  keySeq = ""
  oldX = x0

  # transient buffer
  for _ in range(10000):
    newX = iterateLogMap(oldX, 2)
    oldX = newX

  for _ in range(length):
    newX = iterateLogMap(oldX, 2)
    oldX = newX

    if oldX < c:
      newBit = "0"
    else:
      newBit = "1"

    keySeq += newBit

  return keySeq

def xor(x, y):
    return '{1:0{0}b}'.format(len(x), int(x, 2) ^ int(y, 2))

message = "Hi"
n = 10000

bin_message = atob(message)

x0 = float("." + bin_message)

print(x0)

oldX = x0
for _ in range(n):
  newX = iterateLogMap(oldX, 4)
  oldX = newX
  # print(oldX)

ciphertext = oldX
print("cipher", ciphertext)

# I was not able to implement decryption in time for the presentation. 
# The precision of the decimals was throwing me off and I had trouble with the square roots.
# I promise it works in theory!

