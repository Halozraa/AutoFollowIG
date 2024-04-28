import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui
from libs import shoutdown


def main():
            # Inisialisasi WebDriver
        driver = webdriver.Chrome()

        print("Akan Memulai Program")

        # Buka halaman Instagram
        driver.get("https://www.instagram.com/")
        time.sleep(5)
        driver.maximize_window()
        time.sleep(2)

        #Memasukan username
        print("Memasukan Username")
        username_element = driver.find_element(By.NAME, 'username')
        username_element.send_keys('username') #ganti dengan usernmae anda
        print("username sudah dimasukan")
        time.sleep(2)

        #memasukan password
        print("Mencoba memasukan password")
        PW_element = driver.find_element(By.NAME, 'password')
        PW_element.send_keys('password') #ganti dengan password anda
        print("Password berhasil dimasukan")
        time.sleep(2)


        #mencoba login
        print("Mencoba login")
        masuk = driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]/button/div')
        masuk.click()
        print("Sudah login")
        time.sleep(10)


        #mencoba searing akun Ayang
        print("Mencoba searcing akun")
        print("3")
        driver.get('https://www.instagram.com/kobokanaeru/')
        time.sleep(2)
        print("2")
        print("1")
        print("Berhasil serching Ayang kobo")

        #Mencoba Follow ayang
        time.sleep(3)
        print("Mencoba follow ayang")
        time.sleep(10)
        pyautogui.click(1150,180,2) # auto follow
        time.sleep(2)
        print("Berhasil follow ayang")
        time.sleep(10)
        driver.quit()   #Keluar dari chrome






if __name__ == '__main__':
        main()
        shoutdown()

