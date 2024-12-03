class Contact:
    def  __init__(self,nama,nomor) -> None:
        self.nama= nama
        self.nomor = nomor

class ContactManager:
    def __init__(self) -> None:
        self.contacts = []

    def add_contact(self,nama,nomor):
        contact = Contact(nama,nomor)
        self.contacts.append(contact)
        print(f"Kontak {nama} Berhasil Di Daftarkan")

    def list_contact(self):
        if not self.contacts:
            print("Tidak Ada Kontak")
        else:
            for i,contact in enumerate(self.contacts, 1):
                print(f"{i}. Nama :{contact.nama} , Nomor: {contact.nomor}")

    def edit_contact(self):
        self.list_contact()
        if not self.contacts:
            return
        try:
            index= int(input("Masukkan Nomor Kontak Yang Ingin Di Edit : ")) - 1
            if 0 <= index < len(self.contacts):
                kontak = self.contacts[index]

                nama_baru= input("masukkan nama Baru (Kosongka Jika Ingin Tidak Di ubah) : ")
                nomor_baru= input("masukkan nomor Baru (Kosongka Jika Ingin Tidak Di ubah) : ")
                
                kontak.nama = nama_baru if nama_baru else kontak.nama
                kontak.nomor = nomor_baru if nomor_baru else kontak.nomor
                
                print("kontak berhasil Di Edit ")
            else:
                print("Nomor Kontak Tidak Valid")
        except ValueError:
            print("Input Harus Angka")

    def delete_contact(self):
        self.list_contact()
        if not self.contacts:
            return
        try:
            index= int(input("Masukkan Nomor Kontak Yang Ingin Di Edit : ")) - 1
            if 0 <= index < len(self.contacts):
                deleted_contact= self.contacts.pop(index)
                print(f"kontak{deleted_contact.nama} Berhail Di Hapus")
            else:
                print("Nomor Kontak Tidak valid")
        except ValueError :
            print("Input Harus Berupa Angka")

class Main:
    def run(self):
        manager= ContactManager()
        while True:
            print("\nMenu:")
            print("1.Tambahkan Kontak")
            print("2. Lihat kontak")
            print("3.Edit Kontak")
            print("4.Hapus kontak")
            print("5.Keluar")
            pilihan = input("Pilih Menu :")

            if pilihan == '1':
                nama= input("Masukkan Nama : ")
                nomor= input("Masukkan Nomor : ")
                manager.add_contact(nama,nomor)
            elif pilihan == '2':
                manager.list_contact()
            elif pilihan == '3':
                manager.edit_contact()
            elif pilihan == '4':
                manager.delete_contact()
            elif pilihan == '5':
                print("keluar Dari Program")
                break
            else:
                print("Pilihan Tidak Valid ")

if __name__=="__main__":
    Main().run()