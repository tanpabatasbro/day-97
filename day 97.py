menu = {
    "kopihitam" : 8_500,
    "kopi susu" : 10_000,
    "es kopi susu" : 11_500,
    "cappucino" : 12_000,
    "coklat canas" : 13_000,
    "es coklat" : 15_000,
    "ice americano" : 14_000
}

print("""
      <===>>> -> KC COFFE <- <<<===>
      <======= DAFTAR MENU ========>
      """)

for i in menu:
    print(f"menu : {i}\tHarga : {menu[i]}")

print("""
      <<-============<>==================->>
        Pembelian Lebih Dari 4 Diskon 5%
        pembelian Lebih Dari 7 Diskon 10% 
      <<-============<>==================->>
      """)
beli = input("Pilih Menu  :  ")
jumlah = int(input("Jumlah Pesanan : "))
bayar = jumlah * menu [beli]

if jumlah >= 7:
    diskon = bayar * 10/100
    total = bayar - diskon
    
elif jumlah >=4:
    diskon = bayar * 5/100
    total = bayar - diskon
else :
    total = bayar
    
print(f"""
      <===>>> Detail Pembayaran <<<===>
      Menu : {beli}
      Jumlah : {jumlah}
      Total Harga : {bayar}
      Total Yang Harus dibayar : {total}      
      """)