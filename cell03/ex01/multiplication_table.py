# รับค่าตัวคูณจาก terminal แล้วทำการแปลงข้อมูลจาก ตัวอักษร -> ตัวเลข จากนั้นทำการเก็บไว้ในตัวแปรชื่อว่า value
value = int(input("Enter a number "))
for num in range(10):
	print(f"{num} x {value} = {num * value}")
