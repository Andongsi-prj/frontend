import pymysql
from PIL import Image
import io
import os

# MySQL 연결 설정
conn = pymysql.connect(
    host="192.168.0.163",
    port=3306,
    user="root",
    password="andong1234",
    database="manufacture"
)

# 이미지 경로 설정
save_path = "C:/Users/Admin/Desktop/data/resized/학습"

try:
    with conn.cursor() as cursor:
        # 모든 하위 폴더 포함하여 이미지 처리
        for root, dirs, files in os.walk(save_path):
            for image_name in files:
                image_path = os.path.join(root, image_name)
                with open(image_path, "rb") as image_file:
                    binary_image = image_file.read()
                
                insert_query = """
                INSERT INTO plt_img (img)
                VALUES (%s)
                """
                cursor.execute(insert_query, (binary_image,))
                print(f"이미지 저장 완료: {image_name}")

        conn.commit()
        print("모든 이미지가 성공적으로 저장되었습니다.")

except Exception as e:
    print(f"오류 발생: {str(e)}")
finally:
    conn.close()

