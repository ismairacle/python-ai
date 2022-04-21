print('')
print('--Hitung nilai mata kuliah Kecerdasan Buatan---')
print('')
uts = float(input('Masukan Nilai UTS : ')) * 0.3
uas = float(input('Masukan Nilai UAS : ')) * 0.4
tugas = float(input('Masukan Nilai Tugas : ')) * 0.2
hadir = float(input('Masukan Jumlah Hadir : ')) / 18

total = uts + uas + tugas + hadir
indeks = ''
if total >= 8.0:
    indeks = 'A'
elif total >= 6.0 and total < 8.0:
    indeks = 'B'
elif total >= 4.0 and total < 6.0:
    indeks = 'C'
elif total >= 2.0 and total < 4.0:
    indeks = 'D'
else:
    indeks = 'E'
print('')
print('Anda mendapatkan nilai : ' + indeks)
