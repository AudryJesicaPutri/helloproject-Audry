a = [0, 1]
num = input("masukkan angka : ")
num = int (num)
if num < 2:
   print("minimal 2 deret")
else:
   for i in range (num-2):
      a.append (a [-2] + a [-1])
      print(a)
