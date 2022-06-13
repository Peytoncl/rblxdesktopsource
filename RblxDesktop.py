from flask import Flask, render_template, request
import PIL
import pyautogui
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test', methods=['POST', 'GET'])
def test():
    if request.method == 'GET':
        data = str(GetPixelColors())
        return data
    return render_template('index.html')

def GetPixelColors():
    colors = []
    screenshot = pyautogui.screenshot()
    
    img = screenshot.resize((96, 54))
    pixels = img.load()
    
    for y in range(54):
        for x in range(96):
            color = []
            color.insert(0, pixels[x, y][0])
            color.insert(1, pixels[x, y][1])
            color.insert(2, pixels[x, y][2])
            colors.insert(len(colors)-1, color)

    return colors

#print(GetPixelColors())
app.run(host='0.0.0.0',port='1111',debug=False)
