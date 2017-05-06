n = int(input())

aaa = input()

bbb = input()


if n%2 == 0:
   if all( a==b  for a,b in zip(aaa,bbb)):
       print('Deletion succeeded')
   else:
      print('Deletion failed')
else:
   if all(a != b for a,b, in zip(aaa,bbb)):
     print('Deletion succeeded')
   else:
     print('Deletion failed')
