nama = str(input("NAMA = "))
nim = str(input("NIM = "))
print ("List Minuman")
print ("1.Capucino ")
print ("2.Teh")
print ("3.Exit")
pesan=str(input("Masukan Pilihan : "))
if pesan == "1":
    pilihan ="Memilih Capucino"
    harga = (5000)
    ppn = int (harga * 0.1)
    totalharga = int(harga+ppn)
elif pesan == "2":
    pilihan ="Memilih Teh"
    harga =(3000)
    ppn = int(harga *0.1)
    totalharga = int(harga+ppn)
else:
    pilihan=input("")

print("Minuman :",pilihan)
print("Masukan harga: ", harga)
print("Jumlah yang harus dibayar",totalharga)

