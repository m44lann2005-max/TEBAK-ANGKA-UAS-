import random

def tebak_angka():
    angka_rahasia = random.randint(1, 100)
    print("\n=== Permainan Tebak Angka ===")
    print("Saya sudah memilih angka antara 1 sampai 100.")
    print("Coba tebak! (Maksimal 15 percobaan)")

    percobaan = 0
    batas_percobaan = 15

    while percobaan < batas_percobaan:
        try:
            tebakan = int(input(f"Percobaan ke-{percobaan+1}: Masukkan tebakan Anda: "))
        except ValueError:
            print("Harap masukkan angka yang valid!")
            continue

        percobaan += 1

        if tebakan < angka_rahasia:
            print("Angka Anda lebih kecil.")
        elif tebakan > angka_rahasia:
            print("Angka Anda lebih besar.")
        else:
            print(f"Selamat! Tebakan Anda benar 🎉 dalam {percobaan} percobaan.")
            return True  # Menandakan tebakan berhasil

    print(f"Sayang sekali, Anda sudah mencapai {batas_percobaan} percobaan. Angka rahasia adalah {angka_rahasia}.")
    return False  # Menandakan tebakan gagal

def main():
    while True:
        tebak_angka()
        ulang = input("Apakah Anda ingin mengulang? (y/n): ").lower()
        if ulang != 'y':
            print("Terima kasih sudah bermain. Sampai jumpa!")
            break

# Jalankan program
main()