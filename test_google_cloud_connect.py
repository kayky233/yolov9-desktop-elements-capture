import os
from google.cloud import vision

# 设置 Google Cloud 认证环境变量
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'D:\code_HW\yolov9\yolov9-desktop-elements-capture\fit-aleph-411206-f11a71fdce69.json'

# 确认环境变量是否正确设置
print("GOOGLE_APPLICATION_CREDENTIALS:", os.environ.get('GOOGLE_APPLICATION_CREDENTIALS'))

# 设置代理环境变量
os.environ['http_proxy'] = 'http://127.0.0.1:7899'
os.environ['https_proxy'] = 'http://127.0.0.1:7899'
os.environ['ALL_PROXY'] = 'socks5://127.0.0.1:7898'

def test_vision_api():
    client = vision.ImageAnnotatorClient()
    response = client.label_detection({
        'source': {'image_uri': 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/24/Blue_Tang.jpg/1200px-Blue_Tang.jpg'}
    })
    print(response)

if __name__ == "__main__":
    test_vision_api()
