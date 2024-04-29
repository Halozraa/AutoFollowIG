import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui
from libs import shoutdown
import os
import cv2

def main():
    title = "Auto Follow Instagram Version 1.3"
    text = "Masukan Username IG kalian"
    display = str(pyautogui.prompt(text, title))
    
    username = ['dewajigan','mayasenpai24','lestinaserina','lerilasa54','tarpigwe','apehadue']
    password =['kaumlangit', 'kaumlangit', 'kaumlangit', 'kaumlangit', 'kaumlangit', 'kaumlangit']
    
    auto(username, password, display)
def automation(username, password,display):
    # Inisialisasi WebDriver
    driver = webdriver.Chrome()

    print("Akan Memulai Program")

    # Buka halaman Instagram
    ig = "https://www.instagram.com/"
    follow = f"https://www.instagram.com/{display}"
    driver.get(ig)
    driver.implicitly_wait(30)
    
    time.sleep(2)

    # Memasukan username
    print("Memasukan Username...")
    username_element = driver.find_element(By.NAME, 'username')
    username_element.send_keys(username) 
    print("Username sudah dimasukan...")
    time.sleep(2)

    # Memasukan password
    print("Mencoba memasukan password...")
    PW_element = driver.find_element(By.NAME, 'password')
    PW_element.send_keys(password) 
    print("Password berhasil dimasukan...")
    time.sleep(2)

    # Mencoba login
    print("Mencoba login...")
    masuk = driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]/button/div')
    masuk.click()
    print("Sudah login...")
    time.sleep(3)

    # Mencoba searching akun
    print("Mencoba searching akun...")
    driver.get(follow)
    time.sleep(2)
    print("Berhasil searching...")

    # Mencoba Follow 
    time.sleep(2)
    print("Mencoba follow...")
    time.sleep(3)

    # Mencoba Mencari gambar dan mengklik nya menggunakan pyautogui
    Ffollow = os.path.join('AutoFollowIG','assets','follow.png') #Lokasi foto follow yg ada diassets
    Ffollow1 = os.path.join('AutoFollowIG','assets','follow1.png')
    nfollow = os.path.join('AutoFollowIG','assets','notfollow.png')
    nfollow1 = os.path.join('AutoFollowIG','assets','notfollow.png')
    ss = pyautogui.locateOnScreen(Ffollow,confidence=0.7)
    ss1 = pyautogui.locateOnScreen(Ffollow1,confidence=0.7)
    ssnot =pyautogui.locateOnScreen(nfollow,confidence=0.7)
    ssnot1 =pyautogui.locateOnScreen(nfollow1,confidence=0.7)
    if ss is not None :
        print("Lokasian Foto ditemukan")
        time.sleep(0.9)
        pyautogui.click(ss)
        print("Berhasil follow...")
    elif ss1 is not None:
        print("Lokasian Foto ditemukan")
        time.sleep(0.9)
        pyautogui.click(ss)
        print("Berhasil follow...")
    elif ssnot is not None :
        print("Akun sudah Difollow")
        print("Skip")
    elif ssnot1 is not None :
        print("Akun sudah Difollow")
        print("Skip")
    else:
        print("Foto tidak ditemukan")

    time.sleep(2)
    time.sleep(3)
    driver.quit()   # Keluar dari chrome

def auto(username,password,display):
    for i in range(len(username)):
        print(f"Menjalankan iterasi ke-{i+1}")
        automation(username[i], password[i], display)
    shoutdown()  # Dipanggil setelah loop selesai

if __name__ == '__main__':
    main()