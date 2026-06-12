import depi056

def main():
    while True:
        print("\nMenu:")
        print("1. Buat Matriks")
        print("2. Penjumlahan Matriks")
        print("3. Pengurangan Matriks")
        print("4. Perkalian Matriks")
        print("5. Determinan Matriks")
        print("6. Transpose Matriks")
        print("7. Keluar")

        pilihan = int(input("Pilih opsi: "))
        if pilihan == 1:
            depi056.buat_matriks()
        elif pilihan == 2:
            depi056.penjumlahan()
        elif pilihan == 3:
            depi056.pengurangan()
        elif pilihan == 4:
            depi056.perkalian()
        elif pilihan == 5:
            depi056.determinan()
        elif pilihan == 6:
            depi056.transpose()
        elif pilihan == 7:
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":    
    main()