import pygetwindow as gw
import pyautogui
import keyboard
import time

# Nama window aplikasi Growtopia (sesuaikan dengan nama window yang sesuai)
nama_apk = "Growtopia"

def pdk(initial_position):
    # Fungsi untuk melakukan dua klik tunggal dengan jeda 0.5 detik
    pyautogui.click(clicks=2, interval=0.5)
    pyautogui.moveTo(initial_position[0], initial_position[1])
    
def lock_mouse():
    # Mencari window aplikasi Growtopia
    apk_window = gw.getWindowsWithTitle(nama_apk)

    if not apk_window:
        print(f"Aplikasi {nama_apk} tidak ditemukan.")
        return

    try:
        # Mengunci pointer mouse ke window aplikasi Growtopia
        apk_window[0].activate()

        # Menunggu tombol "l" ditekan untuk merekam posisi pointer
        keyboard.wait("l")
        initial_position = pyautogui.position()
        print(f"Posisi pointer direkam: {initial_position}")

        while True:
            # Memonitor tombol "n" untuk melakukan klik
            if keyboard.is_pressed("n"):
                pdk(initial_position)
                time.sleep(0.01)  # Agar tidak terdeteksi klik berulang akibat tombol "n" yang masih tertahan

            time.sleep(0.01)
    except KeyboardInterrupt:
        # Jika pengguna menekan Ctrl+C, keluar dari loop
        pass

if __name__ == "__main__":
    lock_mouse()
