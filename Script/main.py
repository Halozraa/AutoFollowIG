import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui
from libs import shoutdown
import os
import cv2

# Daftar username dan password
usernames = ['username', 'username', 'username', 'username', 'username', 'username'] #change your user 
passwords =['password', 'password', 'password', 'password', 'password', 'password'] #chnage your password


def automation(username, password):
    fJpg = os.path.join('AutoFollowIG','assets','follow.png') #Lokasi foto follow yg ada diassets
    follow = 'https://www.instagram.com/jenadammaya/' #tujuan follow kalian url nya ya
    # Inisialisasi WebDriver
    driver = webdriver.Chrome()

    print("Akan Memulai Program")

    # Buka halaman Instagram
    driver.get("https://www.instagram.com/")
    driver.implicitly_wait(10)
    
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
    ss = pyautogui.locateOnScreen(fJpg,confidence=0.7)
    if ss is not None :
        print("Lokasian Foto ditemukan")
        time.sleep(0.8)
        pyautogui.click(ss)
    else:
        print("Foto tidak ditemukan")

    time.sleep(2)
    print("Berhasil follow...")
    time.sleep(3)
    driver.quit()   # Keluar dari chrome

if __name__ == '__main__':
    for i in range(len(usernames)):
        print(f"Menjalankan iterasi ke-{i+1}")
        automation(usernames[i], passwords[i])
        shoutdown()
