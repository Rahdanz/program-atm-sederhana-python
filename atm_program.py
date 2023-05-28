import random 
import datetime
from customer import customer
from customer import garis

eidi=input("Masukkan id:")

try:
    pin=int(input('Masukkan pin baru anda:'))
    uang=int(input('Masukkan uang tabungan awal anda:'))
except:
    print('Maaf harap input pin dengan angka')
    print('Harap restart Perangkat')
    exit()

atm=customer(eidi,pin,uang)
while True:
    trial=0
    id=int(input("Masukkan pin anda: "))
       
    while(id != int(atm.checkpin()) and trial <3):
        id=int(input("Pin anda salah Silahkan Masukkan Lagi:"))
        trial+=1
        if trial==3:
            a=id
            b=atm.checkpin()
            if a!=b:
                print('Error.Silahkan ambil kartu dan coba lagi..')
                exit()
    while True:
        print("Selamat datan di ATM Progate..")
        print("\n1-cek Saldo \t 2 - Debet  \t 3 - Simpan \t 4- Ganti Pin \t 5 - Keluar")
        selectmenu=int(input("\n Silahkan Pilih Menu :"))
        if selectmenu==1:
              print("Saldo anda Sekarang: Rp."+str(atm.checkbalance())+"\n")
        elif selectmenu==2:
              nominal= float(input("Masukkan nominal saldo:"))  
              verify_withdraw=input('Konfirmasi:Anda Akan melakukan debet dengan nominal berikut '+str(nominal)+' [y/n] ? : ' ) 
              if verify_withdraw == "y" or verify_withdraw=='Y':
                 print("Saldo awal anda adalah: Rp. " + str(atm.checkbalance()) + "")
              else:
                 break
              if nominal < atm.checkbalance():
                 atm.withdrawbalance(nominal)
                 print("Transaksi debet berhasil!")
                 print("Saldo sisa sekarang: Rp. " + str(atm.checkbalance()) + "\n")
                 break
              else:
                 print("Maaf. Saldo anda tidak cukup untuk melakukan debet!")
                 print("Silakan lakukan penambahan nominal saldo")
                 break
        elif selectmenu==3:
                nominal = float(input("Masukkan nominal saldo: "))
                verify_deposit = input('Konfirmasi: Anda akan melakukan penyimpanan dengan nominal berikut '+str(nominal)+' [y/n] ? : ')
                if verify_deposit == "y" or verify_deposit=='Y':
                    atm.depositbalance(nominal)
                    print("Saldo anda sekarang adalah: Rp." +str(atm.checkbalance()) + "\n" )
                    break
                else:
                    break
        elif selectmenu==4:
                verify_pin = int(input("masukkan pin anda: "))
                while verify_pin != int(atm.checkpin()):
                    print('pin anda salah')
                    verify_pin = int(input("Masukkan pin anda kembali:"))
                verify_newpin = int(input("Harap masukkan pin baru: "))
                updated_pin=int(input('Masukkan kembali pin baru anda:'))
                if verify_newpin == updated_pin:
                    atm.pin=updated_pin
                    print("pin baru anda sukses!")
                    break
                else:
                    print("maaf, pin anda salah! ")
                    break
        elif selectmenu==5:
                print("Resi tercetak otomatis saat anda keluar. Harap simpan tanda terima ini \n sebagai bukti transaksi anda")
                print("No. Rekord: ", random.randint(100000, 1000000))
                print("Tanggal: ", datetime.datetime.now())
                print("Saldo akhir: ", atm.checkbalance())
                print("Terima kasih telah menggunakan ATM Progate!")
                exit()
        else :
               print("Error. Maaf, menu tidak tersedia")
               exit()
               
            
