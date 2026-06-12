def buat_matriks():
    baris = int(input("Masukkan jumlah baris: "))
    kolom = int(input("Masukkan jumlah kolom: "))
    ordo = f"{baris}x{kolom}"
    print(f"Ordo Matriks: {ordo}")

    matriks = []
    print("\nMasukkan elemen matriks:")
    for i in range(baris):
        baris_baru = []
        for j in range(kolom):
            elemen = int(input(f"Elemen [{i}][{j}]: "))
            baris_baru.append(elemen)
        matriks.append(baris_baru)

    print("\nHasil Matriks:")
    for baris_matriks in matriks:
        print(baris_matriks)

def penjumlahan():
    matriks1 = []
    baris1 = int(input("Masukkan jumlah baris matriks 1: "))
    kolom1 = int(input("Masukkan jumlah kolom matriks 1: "))
    ordo1 = f"{baris1}x{kolom1}"
    print(f"Ordo Matriks 1: {ordo1}")

    matriks2 = []
    baris2 = int(input("Masukkan jumlah baris matriks 2: "))
    kolom2 = int(input("Masukkan jumlah kolom matriks 2: "))
    ordo2 = f"{baris2}x{kolom2}"
    print(f"Ordo Matriks 2: {ordo2}")

    if baris1 != baris2 or kolom1 != kolom2:
        print(f"Matriks harus memiliki ukuran ordo yang sama untuk penjumlahan.")
        return
    
    matriks1 = []
    print("\nMasukkan elemen matriks 1:")
    for i in range(baris1):
        baris_baru = []
        for j in range(kolom1):
            elemen = int(input(f"Elemen [{i}][{j}]: "))
            baris_baru.append(elemen)
        matriks1.append(baris_baru)

    matriks2 = []
    print("\nMasukkan elemen matriks 2:")
    for i in range(baris2):
        baris_baru = []
        for j in range(kolom2):
            elemen = int(input(f"Elemen [{i}][{j}]: "))
            baris_baru.append(elemen)
        matriks2.append(baris_baru)

    matriks_hasil = []
    for i in range(baris1):
        baris_baru = []
        for j in range(kolom1):
            total = matriks1[i][j] + matriks2[i][j]
            baris_baru.append(total)
        matriks_hasil.append(baris_baru)

    print("\nHasil Matriks:")
    for baris_matriks in matriks_hasil:
        print(baris_matriks)

def pengurangan():
    matriks1 = []
    baris1 = int(input("Masukkan jumlah baris matriks 1: "))
    kolom1 = int(input("Masukkan jumlah kolom matriks 1: "))
    ordo1 = f"{baris1}x{kolom1}"
    print(f"Ordo Matriks 1: {ordo1}")

    matriks2 = []
    baris2 = int(input("Masukkan jumlah baris matriks 2: "))
    kolom2 = int(input("Masukkan jumlah kolom matriks 2: "))
    ordo2 = f"{baris2}x{kolom2}"
    print(f"Ordo Matriks 2: {ordo2}")

    if baris1 != baris2 or kolom1 != kolom2:
        print(f"Matriks harus memiliki ukuran ordo yang sama untuk pengurangan.")
        return
    
    matriks1 = []
    print("\nMasukkan elemen matriks 1:")
    for i in range(baris1):
        baris_baru = []
        for j in range(kolom1):
            elemen = int(input(f"Elemen [{i}][{j}]: "))
            baris_baru.append(elemen)
        matriks1.append(baris_baru)

    matriks2 = []
    print("\nMasukkan elemen matriks 2:")
    for i in range(baris2):
        baris_baru = []
        for j in range(kolom2):
            elemen = int(input(f"Elemen [{i}][{j}]: "))
            baris_baru.append(elemen)
        matriks2.append(baris_baru)

    matriks_hasil = []
    for i in range(baris1):
        baris_baru = []
        for j in range(kolom1):
            total = matriks1[i][j] - matriks2[i][j]
            baris_baru.append(total)
        matriks_hasil.append(baris_baru)

    print("\nHasil Matriks:")
    for baris_matriks in matriks_hasil:
        print(baris_matriks)
    
    
def perkalian():
    matriks1 = []
    baris1 = int(input("Masukkan jumlah baris matriks 1: "))
    kolom1 = int(input("Masukkan jumlah kolom matriks 1: "))
        
    matriks2 = []
    baris2 = int(input("Masukkan jumlah baris matriks 2: "))
    kolom2 = int(input("Masukkan jumlah kolom matriks 2: "))

    if baris1 != kolom2:
        print("Matriks harus memiliki ukuran baris dan kolom yang sama untuk perkalian.")
        return
    
    matriks1 = []
    print("\nMasukkan elemen matriks 1:")
    for i in range(baris1):
        baris_baru = []
        for j in range(kolom1):
            elemen = int(input(f"Elemen [{i}][{j}]: "))
            baris_baru.append(elemen)
        matriks1.append(baris_baru)

    matriks2 = []
    print("\nMasukkan elemen matriks 2:")
    for i in range(baris2):
        baris_baru = []
        for j in range(kolom2):
            elemen = int(input(f"Elemen [{i}][{j}]: "))
            baris_baru.append(elemen)
        matriks2.append(baris_baru)

    matriks_hasil = []
    for i in range(baris1):
        baris_nol = []
    for j in range(kolom2):
        baris_nol.append(0)
        matriks_hasil.append(baris_nol)
        
    for i in range(baris1):          
        for j in range(kolom2):      
            for k in range(kolom1):
                matriks_hasil[i][j] += matriks1[i][k] * matriks2[k][j]

    print("\nHasil Perkalian Matriks:")
    for baris_matriks in matriks_hasil:
        print(baris_matriks)

def determinan():
    baris = int(input("Masukkan jumlah baris: "))
    kolom = int(input("Masukkan jumlah kolom: "))
    ordo = f"{baris}x{kolom}"
    print(f"Ordo Matriks: {ordo}")

    if baris != kolom:
        print(f"Matriks harus memiliki ukuran baris dan kolom yang sama (2x2 atau 3x3 dst.) untuk determinan.")
        return
    
    matriks = []
    print(f"\nMasukkan elemen matriks baris demi baris:")
    for i in range(baris):
        baris_baru = []
        for j in range(kolom):
            try:
                elemen = int(input(f"Elemen [{i}][{j}]: "))
                baris_baru.append(elemen)
            except ValueError:
                print("Gagal: Input elemen harus berupa angka!")
                return
        matriks.append(baris_baru)

    def hitung_det(m):
        ukuran = len(m)
        if ukuran == 1:
            return m[0][0]
        if ukuran == 2:
            return m[0][0] * m[1][1] - m[0][1] * m[1][0]
        
        det = 0
        for kolom_aktif in range(ukuran):
            # Membuat sub-matriks dengan menghapus baris ke-0 dan kolom_aktif
            sub_matriks = [baris[:kolom_aktif] + baris[kolom_aktif+1:] for baris in m[1:]]
            # Tanda bergantian positif dan negatif (+, -, +, dst.)
            tanda = (-1) ** kolom_aktif
            # Rekursi
            det += tanda * m[0][kolom_aktif] * hitung_det(sub_matriks)
        return det
    
    print("\nMatriks yang dimasukkan:")
    for baris in matriks:
        print(baris)

    hasil = hitung_det(matriks)
    print(f"\n> Determinan Matriks tersebut adalah: {hasil}")

def transpose():
    baris = int(input("Masukkan jumlah baris: "))
    kolom = int(input("Masukkan jumlah kolom: "))
    ordo = f"{baris}x{kolom}"
    print(f"Ordo Matriks: {ordo}")

    matriks = []
    print("\nMasukkan elemen matriks:")
    for i in range(baris):
        baris_baru = []
        for j in range(kolom):
            elemen = int(input(f"Elemen [{i}][{j}]: "))
            baris_baru.append(elemen)
        matriks.append(baris_baru)

    matriks_transpose = []
    for j in range(kolom):
        baris_transpose = []
        for i in range(baris):
            # Membalik indeks: elemen [i][j] dipindah ke posisi [j][i]
            baris_transpose.append(matriks[i][j])
        matriks_transpose.append(baris_transpose)
    
    print("\nMatriks Awal:")
    for baris in matriks:
        print(baris)

    print("\nHasil Transpose Matriks:")
    for baris in matriks_transpose:
        print(baris)