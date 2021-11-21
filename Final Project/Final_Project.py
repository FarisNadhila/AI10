'''
INDONESIA AI BASIC PYTHON BATCH 10
FINAL PROJECT
PROGRAM MENGIRIM E-MAIL OTOMATIS

NAMA : MUHAMMAD FARIS NADHILA
'''
# Import Modul
import smtplib
import getpass
import os

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

while True: 
    print("Selamat datang dalam program pengirim e-mail otomatis!")
    print("------------------------------------------------------")
    print("---Daftar Menu---\n")
    print("1. Daftar e-mail Penerima\n2. Tambah e-mail Penerima\n3. Kirim e-mail otomatis\n4. Keluar\n")
    menu = input("Masukan input menu: \n")

    if menu == '1':
        print("Daftar e-mail penerima")
        print("----------------------\n")
        with open ('receiver_list.txt', 'r') as filex: #membuka daftar email penerima di receiver_list.txt
            daftar_penerima = filex.read()
            print(daftar_penerima)

    elif menu == '2':
        email = input(str("Tambah e-mail penerima: "))
        with open ('receiver_list.txt', 'a') as filex: #membuka dan menambahkan email penerima di "receiver_list.txt"
            filex.write(email)
            filex.write('\n')
        print()        
        print('e-mail berhasil ditambahkan')
    
    elif menu == '3':
        # with open('receiver_list.txt', 'r') as file_x:
        #     receipentemail = file_x.read()
        #     penerima = receipentemail.split("\n")

        # SETUP Pengirim, penerima, judul dan isi email

        # sent_from = gmail_user
        # sent_to = penerima
        # #sent_to = input(str("Masukkan gmail penerima lalu akhiri dengan enter: "))
        # sent_subject = input(
        #     str("Masukkan  subjek atau judul lalu akhiri dengan enter: "))
        # sent_body = input(
        #     str("Masukkan pesan yang akan dikirim lalu akhiri dengan enter: "))

        # email_text = """\
        # From: %s
        # To: %s
        # Subject: %s

        # %s
        # """ % (sent_from, ", ".join(penerima), sent_subject, sent_body)
        print("Login terlebih dahulu")
        gmail_user = input(str("Masukan akun gmail: "))
        gmail_app_password = getpass.getpass()

        #isi email (https://www.pythonindo.com/cara-mengirim-email-menggunakan-python/)
        msg = MIMEMultipart()
        msg['From'] = gmail_user
        msg['Subject'] = input(str("Masukan subject e-mail : "))
        body = input(str("Masukan isi e-mail: "))

        while True: 
            lampiran = input("Apakah anda ingin memasukan lampiran? (y/n) ")
            if lampiran == 'y':

                #lampiran
                filename = input("Masukkan nama File beserta formatnya: ")
                path = input("Masukkan Path File: ")
                attachment = open(path, "rb") 
                
                part = MIMEBase('application', 'octet-stream')
                part.set_payload((attachment).read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
                msg.attach(part)

                # penerima e-mail (https://stackoverflow.com/questions/10147455/how-to-send-an-email-with-gmail-as-provider-using-python)
                with open('receiver_list.txt','r') as filex:
                    penerima = filex.readlines()

                for i in range(len(penerima)):
                    receiver = penerima[i]                    
                    msg['To'] = receiver
                    msg.attach(MIMEText(body, 'plain'))
        
                    try:          
                        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                        server.ehlo()
                        server.login(gmail_user, gmail_app_password)
                        text = msg.as_string()
                        server.sendmail(gmail_user, receiver, text)
                        server.quit()
                        print("e-mail terkirim!")
                    except Exception as exception:
                        print("Error: %s!\n\n" % exception)
    
                break

            elif lampiran == 'n':
                with open ('receiver_list.txt','r') as filex:
                    penerima = filex.readlines()

                for i in range(len(penerima)):
                    receiver = f"{penerima[i]}"
                    msg['To'] = receiver
                    msg.attach(MIMEText(body, 'plain'))
            
                    try:          
                        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                        server.ehlo()
                        server.login(gmail_user, gmail_app_password)
                        text = msg.as_string()
                        server.sendmail(gmail_user, receiver, text)
                        server.quit()
                        print("e-mail terkirim!")
                    except Exception as exception:
                        print("Error: %s!\n\n" % exception)

                break

            else :
                print("Mohon maaf input anda salah")
            

    elif menu == '4': 
        print("---------------------------------")
        print("Program selesai, have a nice day!")
        print("---------------------------------")
        break

    else : 
        print("Mohon maaf, menu tidak tersedia")
