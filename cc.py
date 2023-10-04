import random
import time

def generate_credit_card_number():
    return ''.join(str(random.randint(0, 9)) for _ in range(16))

def generate_cvc():
    return str(random.randint(100, 999))

def generate_date(month, year):
    return f"{month}/{year}"

def generate_credit_card_info(count):
    for i in range(count):
        credit_card_number = generate_credit_card_number()
        cvc = generate_cvc()
        date = generate_date(random.randint(1, 12), random.randint(2022, 2030))
        bank = random.choice(["VISA", "MASTERCARD"])

        print(f"\033[91mKredi Kartı Numarası: \033[32m{credit_card_number}\033[0m")
        print(f"\033[91mCVC: \033[32m{cvc}\033[0m")
        print(f"\033[91mSon Kullanma Tarihi: \033[32m{date}\033[0m")
        print(f"\033[91mBanka: \033[32m{bank}\033[0m")
        print("\033[94m----------------PLOXERET BİR DÜNYA MARKASI XDD----------------\033[0m \033[32m✓\033[0m")
        time.sleep(1)

count = int(input("Kaç adet kredi kartı bilgisi üretmek istiyorsunuz?: "))
generate_credit_card_info(count)