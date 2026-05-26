from statistics import mean

nilai = []

def display_menu():
    print("\n =Data Nilai Siswa= ")
    print("\nMenu:")
    print("1. Tambah Data Nilai")
    print("2. Lihat Data Nilai")
    print("3. Hitung Rata-Rata")
    print("4. Tentukan Grade")
    print("5. Keluar")
    
def tambah_data():
        nilai_baru = int(input("Masukkan nilai anda: "))
        nilai.append(nilai_baru)
        print("Nilaimu sekarang:", nilai_baru)
        return

def lihat_data():
    if nilai:
        print("\nLihat Data Nilai:")
        for nilai_item in nilai:
            print(f"Nilai anda: {nilai_item}")
    else:
        print("\nBelum ada data nilai.")
    
def hitung_rata_rata():
    if nilai:
        print("Rata-rata nilai:", mean(nilai))
    else:
        print("Belum ada data nilai untuk dihitung rata-ratanya.")


def tentukan_grade():
    if not nilai:
        print("Belum ada data nilai untuk menentukan grade.")
        return
    
    for nilai_baru in nilai:
        if 90 <= nilai_baru <= 100:
            grade = "A"
        elif 80 <= nilai_baru <= 89:
            grade = "B"
        elif 70 <= nilai_baru <= 79:
            grade = "C"
        elif 60 <= nilai_baru <= 69:
            grade = "D"
        else:
            grade = "F"
        print(f"Nilai anda adalah {nilai_baru} dan Grade anda saat ini adalah {grade}")
    

def main():
    while True:
        display_menu()
        print("\n =Selamat datang di Data Nilai= ")
        choice = input("Silakan Pilih menu (1-5): ")
        if choice == '1':
            tambah_data()
        elif choice == '2':
            lihat_data()
        elif choice == '3':
            hitung_rata_rata()
        elif choice == '4':
            tentukan_grade()
        elif choice == '5':
            print("Terima kasih!")
            break
        else:
            print("Pilihan Tidak Valid! Silahkan pilih lagi")

if __name__ == "__main__":
    main()
        
