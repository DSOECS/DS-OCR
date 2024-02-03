from PIL import Image, ImageDraw, ImageFont
import os

def create_images_for_characters():
    text = """
    ก ข ค ฆ     ง จ ฉ ช     ซ ฌ ญ ฎ
    ฏ ฐ ฑ ฒ     ณ ด ต ถ     ท ธ น บ
    ป ผ ฝ พ     ฟ ภ ม ย     ร ล ว ศ
    ษ ส ห ฬ     อ ฮ ะ ั     า ำ ิ ี
    ึ ื ุ ู     ฺ ฿ เ แ     โ ใ ไ ๅ
    ๆ ็ ่ ้     ๊ ๋ ์ ํ ๎     ๏ ๐ ๑ ๒
    ๓ ๔ ๕ ๖     ๗ ๘ ๙ ๚     ๛
    abcdefghijklmnopqrstuvwxyz
    ABCDEFGHIJKLMNOPQRSTUVWXYZ
    ! @ # $ % ^ & * ( ) _ + - = { } [ ] | \ : ; " ' < > , . / ? ` ~
    """

    # สร้างโฟลเดอร์ characters_images ถ้ายังไม่มี
    output_folder = "font17"
    os.makedirs(output_folder, exist_ok=True)

    # กำหนดรูปแบบตัวอักษร
    font_size = 20

    # ลองเปลี่ยนเป็น font ภาษาไทยที่คุณมี
    font_path = "./font/font_text2/TH Charmonman Bold.ttf"
    
    # ใช้ ImageFont.truetype เพื่อสร้าง object ของ font
    font = ImageFont.truetype(font_path, font_size)

    for char in text.replace('\n', '').replace(' ', ''):
        # สร้างรูปภาพขนาด 20x20 พิกเซล
        image = Image.new("RGB", (20, 20), "white")
        draw = ImageDraw.Draw(image)

        # คำนวณขนาดของตัวอักษร
        textsize = font.getsize(char)
        text_width, text_height = textsize

        # คำนวณตำแหน่งที่จะวาดตัวอักษรเพื่อให้ได้ตำแหน่งกลาง
        x = (20 - text_width) // 2
        y = (20 - text_height) // 2

        # วาดตัวอักษรลงในรูปภาพ
        draw.text((x, y), char, font=font, fill="black")

        # บันทึกรูปภาพ
        char_image_path = os.path.join(output_folder, f"{ord(char)}.png")
        image.save(char_image_path)

    print(f"Character images saved to: {output_folder}")

create_images_for_characters()
