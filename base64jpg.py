import base64
import pyperclip
filepath = "lotus.jpg"
filepath = r"C:\Users\glenl\Downloads\PixelSkates\images\1.png"
binary_fc = open(filepath, 'rb').read()  # fc aka file_content
base64_utf8_str = base64.b64encode(binary_fc).decode('utf-8')

ext = filepath.split('.')[-1]
dataurl = f'data:image/{ext};base64,{base64_utf8_str}'
print(dataurl)
pyperclip.copy(dataurl)