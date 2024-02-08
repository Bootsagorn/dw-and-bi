Documentation Data Modeling 2
1.ทำการรัน pip install cqlsh ติดตั้งเครื่องมือ cqlsh ผ่าน pip เพื่อเชื่อมต่อการทำงานกับ Cassandra database
2. ทำการรัน docker compose up เพื่อเปิดการใช้งานแอพในไฟล์ docker-compose.yml
3.เปิดหน้า ports 9042 เพื่อดูการเชื่อมต่อบน browser 
4. เปิดหน้า terminal ใหม่ ทำการรัน python etl.py เพื่อดึงข้อมูลจากไฟล์
 	4.1 โดยจาก file etl.py มีการสร้าง table events  มีข้อมูลในตารางดังนี้ ประกอบด้วย 3 คอลัมน์
      	   1)  id  (PK)  --> เก็บข้อมูลเป็น  text 
   	       2)  type (PK) --> เก็บข้อมูลเป็น text // การเก็บข้อมูล type สามารถเอามาดูได้ว่าผู้ใช้ทำ events  type แบบใด 
     	   3)  public --> เก็บข้อมูลเป็น boolean // การเก็บข้อมูล public สามารถรู้ได้ว่า events นี้เปิดให้ดูเป็น public หรือไหม สามารถ query เรียกดูแค่ข้อมูล public = true ได้
           * ในการออกแบบให้ id , type เป็น primary key และ type เป็น clustering column เพื่อเรียงลำดับข้อมูลภายใน partition ของคอลัมน์ id
5. รัน $ cqlsh ทำการเชื่อมต่อกับ Cassandra database เพื่อ Test Cluster
6. รัน cqlsh> select * from github_events.events ; เพื่อดู insert_sample_data ที่ได้เพิ่มเข้าไป
7. เมื่อทดสอบเสร็จ cqlsh> exit 