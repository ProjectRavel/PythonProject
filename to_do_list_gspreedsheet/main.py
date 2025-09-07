import json
import gspread
import os

def main():
    
    tasks = []
    path_file = 'tasks.json'
    
    if not os.path.exists(path_file):
        with open(path_file, 'w') as f:
            json.dump([], f)
    else:
        with open(path_file, 'r') as f:
            tasks = json.load(f)

    def update_file():
        try:
            with open(path_file, 'w') as f:
                json.dump(tasks, f, indent=4)
        finally:
            print("Berhasil di simpan!")
        
    def export_spreedsheet():
        update_file()
        gc = gspread.service_account(filename='credentials.json')
        sh = gc.open('PythonData')
        worksheet = sh.sheet1
       
        with open('tasks.json', 'r') as f:
           tasks = json.load(f)
           
        if not tasks:
            print("tasks.json kosong, gak ada data buat diexport.")
            return
           
        worksheet.clear()
        headers = list(tasks[0].keys())
        worksheet.append_row(headers)
        
        for row in tasks:
            worksheet.append_row(list(row.values()))
        print("Data JSON berhasil di export ke Google spreedSheet")

    def list_question():
        print("1. Tambah List")
        print("2. Lihat List")
        print("3. Edit List")
        print("4. Hapus List")
        print("5. Tandai yang sudah selesai")
        print("6. Keluar")
        print("7. Simpan")
        print("8. Export Ke Google SpreedSheet")
        
    def tambah_list():
        while True:
            new_task = input_string("Task apa yang belum kelar? (Ketik 'selesai' untuk berhenti) ")
            
            if new_task.lower() == 'selesai':
                break
            
            buat_list(new_task)

    def buat_list(task):
        tasks.append({
            "judul": task,
            "status": "belum selesai"
        })

    def lihat_list():
        print('-'*30)
        for i, t in enumerate(tasks, start=1):
            print(f"{i}. Task: {t['judul']}, Status: {t['status']}")
        
    def edit_list():
        lihat_list()
        user_choose = input_angka("Anda ingin mengubah nomor berapa? ")
        
        ubah_list(user_choose, 'edit')

    def hapus_list():
        lihat_list()
        user_choose = input_angka("Anda ingin mengubah nomor berapa? ")
        
        ubah_list(user_choose, 'delete')

    def selesai_list():
        lihat_list()
        user_choose = input_angka("udah selesai? nomor berapa? ")
        
        ubah_list(user_choose, 'done')

    def ubah_list(index, status):
        
        if index < 1 or index > len(tasks):
            print("Nomor Tidak ada di dalam task")
            return
        
        if status == 'edit':
            new_change = input_string("Menjadi apa? ")
            
            try:
                tasks[index - 1]["judul"] = new_change
            except IndexError:
                print("nomor gaada di dalam task")
        
        if status == 'done':
            try:
                tasks[index - 1]["status"] = 'selesai'
            except IndexError:
                print('nomor gaada di dalam task')
        
        
        if status == 'delete':
            try:
                tasks.pop(index - 1)
                print("and berhasil menghapus")
                lihat_list()
            except IndexError:
                print("nomor gaada di dalam task")

    def end_program():
        print("terimakasih")

    def input_angka(format):
        while True:
            try:
                output = int(input(format))
                return output
            except ValueError:
                print("masukkan angka yg valid")
            
    def input_string(format):
        while True:
            try:
                output = str(input(format))
                return output
            except ValueError:
                print("Salah type input!")


    while True:
            list_question()
            print("-"*30)
            user_choose = input_angka("Apa yang anda ingin lakukan: ")
            
            if user_choose == 1:
                tambah_list()
            elif user_choose == 2:
                lihat_list()
            elif user_choose == 3:
                edit_list()
            elif user_choose == 4:
                hapus_list()
            elif user_choose == 5:
                selesai_list()
            elif user_choose == 6:
                end_program()
                break
            elif user_choose == 7:
                update_file()
                break
            elif user_choose == 8:
                export_spreedsheet()
                break
            
            print('-'*30)

main()