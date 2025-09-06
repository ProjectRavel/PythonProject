
def penjumlahan(a, b):
    return a + b

def pengurangan(a, b):
    return a - b

def perkalian(a, b):
    return a * b

def pembagian(a, b):
    if b == 0:
        raise ValueError("BRO INI PEMBAGIAN GABISA DI BAGI 0")
    return a / b

def perpangkatan(a, b):
    return pow(a, b)

def angka_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Input harus berupa angka")

history = []

def tampilkan_history():
    if not history:
        print("Histori Kosong")
    else:
        for i, h in enumerate(history, start=1):
            print(f"{i}: {h}")

def list_menu():
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Perpangkatan")
    print("6. Histori")
    print("7. Selesai")

operasi_dict = {
    1: ("penjumlahan", penjumlahan, "+"),
    2: ("pengurangan", pengurangan, "-"),
    3: ("perkalian", perkalian, "x"),
    4: ("pembagian", pembagian, ":"),
    5: ("perpangkatan", perpangkatan, "^"),
}

def main():
    while True:
        list_menu()
        playerChoose = angka_input("Masukkan Angka: ")
        
        if playerChoose not in range(1, 8):
            print("Pilihan tidak valid, silakan pilih 1-7")
            continue
        
        if playerChoose == 6:
            tampilkan_history()
            continue
        elif playerChoose == 7:
            print("terimakasih sudah menghitung")
            break
        
        angka_pertama = angka_input("Masukkan Angka Pertama: ")
        angka_kedua = angka_input("Masukkan Angka Kedua: ")
        
        if playerChoose in operasi_dict:
            nama, fungsi, operasi = operasi_dict[playerChoose]
            try:
                hasil = fungsi(angka_pertama, angka_kedua)
                history.append(f"{angka_pertama} {operasi} {angka_kedua} = {hasil}")
                print("hasil: ", hasil)
            except ValueError as e:
                print(e)

main()
