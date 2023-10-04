import random
import time

def generate_mastercard_number():
    prefix = str(random.randint(5100000000000000, 5599999999999999))
    suffix = str(random.randint(100000000, 9999999999))
    return prefix + suffix

def generate_cvc():
    return str(random.randint(100, 999))

def generate_date(month, year):
    return f"{month}/{year}"

def generate_mastercard_info(count):
    for i in range(count):
        mastercard_number = generate_mastercard_number()
        cvc = generate_cvc()
        date = generate_date(random.randint(1, 12), random.randint(2022, 2030))

        print(f"\033[91mKredi Kartı Numarası: \033[32m{mastercard_number}\033[0m")
        print(f"\033[91mCVC: \033[32m{cvc}\033[0m")
        print(f"\033[91mSon Kullanma Tarihi: \033[32m{date}\033[0m")
        print(f"\033[94m----------------PLOXERET BİR DÜNYA MARKASI XDD----------------\033[0m \033")
        time.sleep(1)

count = int(input("Kaç adet CivCiv üretmek istiyorsunuz?: "))
generate_mastercard_info(count)
