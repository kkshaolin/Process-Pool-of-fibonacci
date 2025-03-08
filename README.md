โปรแกรมนี้เป็นโปรแกรมหาค่า fibonacci โดยละรับจำนวน n มาเพื่อใช้ในการกำหนดว่าต้องการหากี่ต่ำแหน่ง และมี 
concurrency แบบ synchronous โดยในโปรแกรมมีการทำงานอยู่ 2 ฟังก์ชัน โดยมีรายละเอียดดั้งนี้

### 1.import time 
เพิ่อใช้ในการคำนวนเวลาการทำงานของโปรแกรม

### 2. function fibonacci 
มีพารามิเตอร์ n และจะเริ่มโดยสร้าง list เก็บค่า 0 ,1 แล้ว loop จาก 2 ถึ่ง n เพื่อเพิ่มค่าในตำแหน่งต่อๆไปโดยการเอาค่าตำแหน่งก่อนลำดับ 1 บวกกับก่อนหน้าลำดับ 2 แล้ว return จาก 0 ถึ่ง n

### 3. function synchronous 
มีพารามิเตอร์ n และจะสร้าง list num มา แล้ว loop เพื่อส่ง n ที่ละค่าไปคำนวนที่ function fibonacci แล้วเอามาเก็บที่ list num แล้ว return num ออกมา

### 4. if __name__ == "__main__" 
จะมี list n ที่จำนวนลำดับทีจะหา แล้วมีการเริ่มจับเวลาแล้วส่ง list n ไปที่ function synchronous แล้วหยุดจับเวลา
