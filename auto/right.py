import tkinter as tk
from threading import Thread
import pyautogui
import time

class AutoKeyPresser:
    def __init__(self, root):
        self.root = root
        self.root.title("Auto Right Key Presser")

        self.running = False

        # UI elements
        self.label = tk.Label(root, text="Interval (วินาที):")
        self.label.pack(pady=5)

        self.interval_entry = tk.Entry(root)
        self.interval_entry.insert(0, "0.5")  # ค่าหน่วงเริ่มต้น
        self.interval_entry.pack(pady=5)

        self.start_button = tk.Button(root, text="เริ่ม", command=self.start)
        self.start_button.pack(pady=5)

        self.stop_button = tk.Button(root, text="หยุด", command=self.stop)
        self.stop_button.pack(pady=5)

        self.status_label = tk.Label(root, text="สถานะ: หยุดอยู่")
        self.status_label.pack(pady=10)

    def key_loop(self):
        try:
            interval = float(self.interval_entry.get())
        except ValueError:
            self.status_label.config(text="กรุณากรอกตัวเลขที่ถูกต้อง")
            self.running = False
            return

        time.sleep(3)  # หน่วงเวลาก่อนเริ่ม (ให้ผู้ใช้ย้ายโฟกัส)

        while self.running:
            pyautogui.press('right')
            time.sleep(interval)

    def start(self):
        if not self.running:
            self.running = True
            self.status_label.config(text="สถานะ: กำลังทำงาน...")
            Thread(target=self.key_loop, daemon=True).start()

    def stop(self):
        self.running = False
        self.status_label.config(text="สถานะ: หยุดอยู่")

# สร้างหน้าต่าง
root = tk.Tk()
app = AutoKeyPresser(root)
root.mainloop()
