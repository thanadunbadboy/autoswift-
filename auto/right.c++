
#include <windows.h>
#include <thread>

int main() {
    // หน่วงเวลาก่อนเริ่ม (5 วินาที)
    Sleep(5000);

    while (true) {
        // ส่ง key down (กดปุ่มลูกศรขวา)
        keybd_event(VK_RIGHT, 0, 0, 0);
        // หน่วงสั้น ๆ
        Sleep(50);
        // ส่ง key up (ปล่อยปุ่ม)
        keybd_event(VK_RIGHT, 0, KEYEVENTF_KEYUP, 0);
        
        // หน่วงระหว่างการกดแต่ละรอบ (0.5 วินาที)
        Sleep(500);
    }

    return 0;
}
