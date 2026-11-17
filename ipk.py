def konversi_nilai(huruf):
    bobot = {
        'A': 4.0,
        'AB': 3.5,
        'B': 3.0,
        'BC': 2.5,
        'C': 2.0,
        'D': 1.0,
        'E': 0.0
    }
    return bobot.get(huruf.upper(), -1)

def hitung_ipk():
    print("=== KALKULATOR IPK MAHASISWA ===")
    jumlah_matkul = int(input("Masukkan jumlah mata kuliah: "))
    
    total_sks = 0
    total_bobot = 0

    for i in range(jumlah_matkul):
        print(f"\nMata Kuliah ke-{i+1}")
        nama = input("Nama Mata Kuliah : ")
        sks = int(input("Jumlah SKS       : "))
        nilai = input("Nilai Huruf (A/AB/B/BC/C/D/E): ")

        angka = konversi_nilai(nilai)
        if angka == -1:
            print("Nilai huruf tidak valid, dianggap 0.")
            angka = 0

        total_sks += sks
        total_bobot += (angka * sks)

    if total_sks > 0:
        ipk = total_bobot / total_sks
        print("\n================================")
        print(f"Total SKS Diambil : {total_sks}")
        print(f"IPK Akhir Anda    : {ipk:.2f}")
        print("================================")
    else:
        print("Total SKS tidak boleh 0.")

if __name__ == "__main__":
    hitung_ipk()
