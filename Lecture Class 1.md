# Command Line on Terminal  
**Lecture Class 1**

---

## 1. List – คำสั่งสำหรับแสดงแฟ้มข้อมูล
ใช้สำหรับแสดงรายชื่อ file และ folder ที่อยู่ในโฟลเดอร์ปัจจุบัน

```bash
ls
bash
Copy code
ls -l
แสดงรายละเอียดไฟล์ในรูปแบบ long format
(Permission / จำนวน user / ขนาดไฟล์ / วันเวลา / ชื่อไฟล์)

text
Copy code
rwxrwxrwx 1 ilysbeam ilysbeam 18683777 Jun 27 20:28 '(แบบร่าง) Glumii Slide.pdf'
ตัวเลข → จำนวน Users ที่เป็นเจ้าของไฟล์

วันที่และเวลา → วันและเวลาที่ไฟล์ถูกสร้างหรือแก้ไขล่าสุด

bash
Copy code
ls -lh
แสดงขนาดไฟล์แบบอ่านง่าย (human-readable)

text
Copy code
rwxrwxrwx 1 ilysbeam ilysbeam 18M Jun 27 20:28 '(แบบร่าง) Glumii Slide.pdf'
bash
Copy code
ls -ltr
เรียงไฟล์ตามเวลาที่แก้ไขล่าสุด

-t เรียงตามเวลา

-r กลับลำดับ
➡️ ไฟล์ล่าสุดจะแสดงอยู่ด้านล่างสุด

Permission
r → read

w → write

x → execute

2. Change Directory
bash
Copy code
cd
กลับไปยัง home directory (~)

bash
Copy code
cd ..
ย้อนกลับไปโฟลเดอร์ก่อนหน้า 1 ระดับ

bash
Copy code
cd ../..
ย้อนกลับ 2 ระดับ

bash
Copy code
cd <ชื่อโฟลเดอร์>/
กด Tab เพื่อช่วยเติมชื่อโฟลเดอร์อัตโนมัติ

bash
Copy code
pwd
แสดงตำแหน่งที่อยู่ปัจจุบัน (current directory)

3. File / Folder Management
สร้างโฟลเดอร์
bash
Copy code
mkdir <folder_name>
สร้างและแก้ไขไฟล์
bash
Copy code
vi <ชื่อไฟล์>
vi <ชื่อไฟล์.py>
ขั้นตอนการใช้งาน vi

กด i เพื่อเข้าสู่โหมดเขียน

กด Esc แล้วพิมพ์

:wq → บันทึกและออก

:q! → ออกโดยไม่บันทึก

ลบไฟล์
bash
Copy code
rm <ชื่อไฟล์>
ลบโฟลเดอร์ทั้งหมด
bash
Copy code
rm -r <ชื่อโฟลเดอร์>
เปิดดูเนื้อหาไฟล์
bash
Copy code
cat <ชื่อไฟล์>
4. Move File
วิธีที่ 1: ระบุ path ต้นทางและปลายทาง
bash
Copy code
mv <path ต้นทาง>/<ชื่อไฟล์> <path ปลายทาง>/.
วิธีที่ 2: อยู่ในโฟลเดอร์ปลายทาง
bash
Copy code
mv ../abc.txt .
. หมายถึงตำแหน่งปัจจุบัน

5. Copy File / Folder
Copy ไฟล์
bash
Copy code
cp <path ต้นทาง>/<ชื่อไฟล์> <path ปลายทาง>/.
Copy โฟลเดอร์
bash
Copy code
cp -r <folder_source> .
6. Manual Page
bash
Copy code
man ls
ใช้ดูคู่มือคำสั่ง (สามารถใช้กับทุก command)

7. Check System Preference
bash
Copy code
htop
ใช้ดูการใช้งาน RAM และ CPU
หมายเหตุ: ต้องติดตั้งก่อนใช้งาน

Notes เพิ่มเติม
drwxr-xr-x

d = directory

r = read

x = execute

ls -lh → แสดงขนาดไฟล์แบบอ่านง่าย

ls -ltr → ไฟล์ล่าสุดอยู่ด้านล่างสุด
