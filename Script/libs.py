import time

def countdown(seconds):
    while seconds > 0:
        print(seconds)
        seconds -= 1
        time.sleep(1)
    print(f"Program berakhir")

def shoutdown():
    try:
        seconds = 10
        countdown(seconds)
    except ValueError:
        print("Masukan angka bukan huruf")
def main():
    shoutdown()

if __name__ == '__main__' :
    main()