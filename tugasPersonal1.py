import csv
from csv import writer
from csv import reader

f = open('tugasPersonal1.csv')
data = list(csv.DictReader(f))

# Mendapatkan nilai pada kolom gaji
hitung = []

for col in data:
    hitung.append(col['gaji'])
    hitung = [int(i) for i in hitung]

# No. 1
jabatan = []

for isJabatan in hitung:
    if isJabatan >= 15000000:
        object = ("Manager")
        jabatan.append(object)
        continue
    elif isJabatan >= 12000000:
        object = ("Asisten Manager")
        jabatan.append(object)
        continue
    elif isJabatan >= 10000000:
        object = ("Supervisor")
        jabatan.append(object)
        continue
    elif isJabatan >= 8000000:
        object = ("Officer")
        jabatan.append(object)

# Fungsi untuk membuat file output
def add_column_in_csv(input_file, output_file, transform_row):
    with open(input_file, 'r') as read_obj, \
            open(output_file, 'w', newline='') as write_obj:
        csv_reader = reader(read_obj)
        csv_writer = writer(write_obj)
        for row in csv_reader:
            transform_row(row, csv_reader.line_num)
            csv_writer.writerow(row)

# File output dengan penambahan kolom baru (Jabatan)
header_of_new_col = 'Jabatan'
new_col = jabatan

add_column_in_csv('tugasPersonal1.csv', 'output_tugasPersonal1.csv',
                  lambda row, line_num: row.append(header_of_new_col) if line_num == 1 else row.append(
                      new_col[line_num - 12]))

# No. 2
# Fungsi untuk mencari gaji terbesar
def gaji_maksimal(gaji):
    gaji_terbesar = gaji[0]

    for nilai in gaji:
        if nilai > gaji_terbesar:
            gaji_terbesar = nilai

    return gaji_terbesar

# Funsi untuk mencari gaji terkecil
def gaji_minimal(gaji):
    gaji_minimal = gaji[0]

    for nilai in gaji:
        if nilai < gaji_minimal:
            gaji_minimal = nilai

    return gaji_minimal

print('Gaji Terbesar : ', gaji_maksimal(hitung))
print('Gaji Terkecil : ', gaji_minimal(hitung))

