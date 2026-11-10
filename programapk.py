# =====================================
#       APLIKASI KASIR RESTORAN
# =====================================

print("=" * 45)
print("       SELAMAT DATANG DI RESTORAN")
print("          APLIKASI KASIR")
print("=" * 45)

# Daftar menu makanan
menu = {
    1: ("Nasi Goreng", 25000),
    2: ("Mie Ayam", 15000),
    3: ("Ayam Geprek", 20000),
    4: ("Sate Ayam", 30000),
    5: ("Bakso", 18000)
}

total = 0
pesanan = []

# Perulangan menu
while True:
    print("\n========== MENU MAKANAN ==========")
    for nomor, (nama, harga) in menu.items():
        print(f"{nomor}. {nama:<15} : Rp{harga:,}".replace(",", "."))
    
    print("0. Selesai Memilih")
    print("==================================")

    pilihan = input("Pilih menu (0-5): ")

    # Jika memilih selesai
    if pilihan == "0":
        break

    # Validasi pilihan menu
    if not pilihan.isdigit() or int(pilihan) not in menu:
        print("Pilihan tidak tersedia!")
        continue

    pilihan = int(pilihan)
    nama, harga = menu[pilihan]

    # Input jumlah pesanan
    jumlah = input("Masukkan jumlah pesanan: ")

    if not jumlah.isdigit() or int(jumlah) <= 0:
        print("Jumlah pesanan tidak valid!")
        continue

    jumlah = int(jumlah)

    # Menghitung subtotal
    subtotal = harga * jumlah
    total += subtotal

    pesanan.append((nama, harga, jumlah, subtotal))

    print(f"{nama} berhasil ditambahkan!")
    print(f"Subtotal: Rp{subtotal:,}".replace(",", "."))


# =====================================
#          PERHITUNGAN DISKON
# =====================================

print("\n========== PEMBAYARAN ==========")

diskon = 0

if total > 200000:
    diskon = total * 20 / 100
    print("Selamat! Anda mendapatkan diskon 20%")
else:
    print("Anda tidak mendapatkan diskon.")

potongan = int(diskon)
total_bayar = total - potongan


# =====================================
#          STRUK PEMBAYARAN
# =====================================

print("\n========================================")
print("             STRUK PEMBAYARAN")
print("========================================")

for nama, harga, jumlah, subtotal in pesanan:
    print(f"{nama}")
    print(f"  {jumlah} x Rp{harga:,} = Rp{subtotal:,}".replace(",", "."))

print("----------------------------------------")
print(f"Total Belanja : Rp{total:,}".replace(",", "."))
print(f"Diskon        : {20 if diskon > 0 else 0}%")
print(f"Potongan      : Rp{potongan:,}".replace(",", "."))
print("----------------------------------------")
print(f"TOTAL BAYAR   : Rp{total_bayar:,}".replace(",", "."))
print("========================================")
print("       TERIMA KASIH TELAH BERBELANJA")
print("========================================")