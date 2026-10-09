# app/mcp/server.py
from fastmcp import FastMCP

# 1. สร้าง FastMCP instance พร้อมกำหนดชื่อ Server
mcp = FastMCP("CS-Student-Helper")


# 2. ใช้ Decorator @mcp.tool() เพื่อแปลง Python Function ให้เป็น Tools สำหรับ AI
@mcp.tool()
def calculate_gpa(grades_data: list[dict]) -> float:
  """คำนวณเกรดเฉลี่ยสะสม (GPA) สำหรับนักศึกษา CS

  Args:
      grades_data: รายรับข้อมูลหน่วยกิตและเกรด เช่น [{"credit": 3, "grade": 4.0},
        {"credit": 1, "grade": 3.5}]
  """
  total_points = 0.0
  total_credits = 0

  # วนลูปคำนวณแต้มสะสม (Quality Points = Credit * Grade)
  for item in grades_data:
    credit = item.get("credit", 0)
    grade = item.get("grade", 0.0)
    total_points += credit * grade
    total_credits += credit

  # ป้องกันการหารด้วยศูนย์
  if total_credits == 0:
    return 0.0

  # คืนค่าเกรดเฉลี่ยปัดเศษ 2 ตำแหน่ง
  return round(total_points / total_credits, 2)


if __name__ == "__main__":
  # 3. รัน Server ผ่าน Stdio Transport เพื่อสื่อสารกับ Claude Desktop Client
  mcp.run()