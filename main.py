import os

from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['contact']
collection = db['contacs']\

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_menu():
    clear_screen()
    print("=== APLIKASI KONTAK ===")
    print("[1] Lihat Daftar Kotak")
    print("[2] Buat Kontak Baru")
    print("[3] Edit Kontak")
    print("[4] Hapus Kontak")
    print("[0] Exit")
    print("------------------------")
    selected_menu = input("Pilih menu> ")

    if (selected_menu == "1"):
        show_contact()
    elif (selected_menu == "2"):
        create_contact()
    elif (selected_menu == "3"):
        edit_contact()
    elif (selected_menu == "4"):
        delete_contact()
    elif (selected_menu == "0"):
        exit()
    else:
        print("Kamu memilih menu yang salah!")
        back_to_menu()


def back_to_menu():
    print("\n")
    input("Tekan Enter untuk kembali...")
    show_menu()

def show_contact():
    clear_screen()
    try:
        contacts = collection.find()

        # Tampilkan informasi kontak
        print("Daftar Kontak:")
        for cont in contacts:
            print(f"No: {cont['NO']}, Nama: {cont['NAMA']}, Telepon: {cont['TELEPON']}")

    except Exception as e:
        print(f"Error: {e}")
    back_to_menu()

def create_contact():
    clear_screen()
    no = input("No urut: ")
    nama = input("Nama lengkap: ")
    telepon = input("No. Telepon: ")

    temp={'NO': no, 'NAMA': nama, 'TELEPON': telepon}
    collection.insert_one(temp)
    print("Berhasil disimpan!")

    back_to_menu()

def edit_contact():
    clear_screen()
    name = input("Nama : ")
    find = collection.find_one({"NAMA": name})
    if find:
        print("found")
        new_DATA = {
        "NO" : input("No urut baru: "),
        "NAMA": input("Nama lengkap baru: "),
        "TELEPON" : input("No. Telepon baru : ")
        }

        collection.update_one(
            {"NAMA":name},
            {"$set":new_DATA}
        )
        print("update succes")
    else:
        print("not found")
        return edit_contact()
    back_to_menu()

def delete_contact():
    name = input("Nama : ")
    find = collection.find_one({"NAMA": name})
    if find:
        print("found")
        collection.delete_one(
            {"NAMA":name}
        )

        print("delete succes")
    else:
        print("not found")
        return delete_contact()
    back_to_menu()

if __name__ == "__main__":
    while True:
        show_menu()