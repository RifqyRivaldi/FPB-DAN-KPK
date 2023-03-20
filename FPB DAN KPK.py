#!/usr/bin/env python
# coding: utf-8

# In[8]:


def hitung_fpb(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def hitung_kpk(a, b):
    if a == 0 or b == 0:
        return 0
    kpk = max(a, b)
    while True:
        if kpk % a == 0 and kpk % b == 0:
            return kpk
        kpk += max(a, b)

def tampilkan_menu():
    print("Pilihan menu:")
    print("1. Hitung FPB")
    print("2. Hitung KPK")
    print("3. Keluar")

def main():
    while True:
        tampilkan_menu()
        try:
            pilihan = int(input("Masukkan pilihan Anda: "))
        except ValueError:
            print("Input tidak valid, silakan masukkan bilangan bulat.")
            continue

        if pilihan == 1:
            try:
                a = int(input("Masukkan bilangan pertama: "))
                b = int(input("Masukkan bilangan kedua: "))
            except ValueError:
                print("Input tidak valid, silakan masukkan bilangan bulat.")
                continue
            fpb = hitung_fpb(a, b)
            print("FPB dari", a, "dan", b, "adalah", fpb)

        elif pilihan == 2:
            try:
                a = int(input("Masukkan bilangan pertama: "))
                b = int(input("Masukkan bilangan kedua: "))
            except ValueError:
                print("Input tidak valid, silakan masukkan bilangan bulat.")
                continue
            kpk = hitung_kpk(a, b)
            print("KPK dari", a, "dan", b, "adalah", kpk)

        elif pilihan == 3:
            print("Thank You!!!!")
            break

        else: 
            print("Pilihan tidak valid, silakan coba lagi!!!")

if __name__ == '__main__':
    main()






