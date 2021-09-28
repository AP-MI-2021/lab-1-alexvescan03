import sys

n =int(sys.argv[1])

'''  
Returneaza true daca n este prim si false daca nu.
'''
def is_prime(n):
  # codul vostru aici
  i = 2
  ok = True
  while i <= n/2:
    if n%i ==0 :
      ok = False
    i = i + 1
  if ok:
    print("Numarul e prim")
  else:
    print("Numarul nu e prim")
  
'''
Returneaza produsul numerelor din lista lst.
'''
def get_product(lst):
  # codul vostru aici
  print ("Functioneaz")
  
'''
Returneaza CMMDC a doua numere x si y folosind primul algoritm.
'''
def get_cmmdc_v1(x, y):
  # codul vostru aici
  print ("Functioneaz")
  
'''
Returneaza CMMDC a doua numere x si y folosind al doilea algoritm.
'''
def get_cmmdc_v2(x, y):
  # codul vostru aici
  print ("Functioneaz")
  
def main():
  # interfata de tip consola aici
  
  is_prime(n)


if __name__ == '__main__':
  main()
  