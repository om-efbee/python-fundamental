#operasi aritmatika
a = 10
b = 3
#operasi tambah +
hasil = a + b
print(a,'+',b, '=',hasil)
#operasi pengurangan -
hasil = a - b
print(a,'+',b, '=',hasil)
#operasi perkalian  x
hasil = a * b
print(a,'x',b, '=',hasil)
#operasi pembagian  :
hasil = a / b
print(a,'/',b, '=',hasil)

#operasi exponen  (pangkat)
hasil = a ** b
print(a,'**',b, '=',hasil)

#operasi modulus  (sisa bagi)
hasil = a % b
print(a,'%',b, '=',hasil)

#operasi floor division
'''perioritas operasi
1. ()
2. exponen **
3. Perkalian & teman teman * / ** % //
4. pertambahan dan pengurangan
'''



hasil = a // b
print(a,'//',b, '=',hasil)

x = 3
y = 2
z = 4

hasil =  x ** y * (z + x) / y - y % z // x
print (x, '**',y,'*', '(',z,'+',x, ')','/',y,'-',y,'%',z,'//',x, '=', hasil)

hasil = x + y * z
print ('(',x, '+', y,'*', z,')','hasil =',hasil)

hasil = (x + y) * z
print ('(',x, '+', y,') *', z,') *',z, '=',hasil)