
# Variabel adalah tempat menyimpan data

# menaruh / assignment nilai
a = 10
c = 20
panjang = 1000

#Pemanggilan pertama

print("Nilai a = ", a)
print("Nilai c = ", c)
print("Nilai panjang = ", panjang)

# penamaan

nilai_y = 18 # dengan menggunakan underscore
juta10 = 10000000 # ini boleh
nilaiZ = 18.5 # ini boleh

# pemanggilan kedua

print("Nilai a = ", a)
a = 8
print("Nilai b = ", a)

# assignment indirect

b = a
print("Nilai b = ",b)

# assignment indirect
b = a
print("Nilai b = ",b)

a=int(input("masukkan nilai a:"))
b=int(input("masukkan nilai b:"))
print("variable a=",a)
print("variable b=",b)
print("hasil penggabungan {1}&{0}=%d".format(a,b) %(a+b))

#konversi nilai variable
a=int(a)
b=int(b)
print("hasil pejumlahan {1}+{0}=%d".format(a,b) %(a+b))
print("hasil pembagian {1}/{0}=%d".format(a,b) %(a/b))