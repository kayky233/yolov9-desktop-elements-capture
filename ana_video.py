import numpy
import numpy as np
from PIL import ImageGrab
import cv2
import time
import win32gui, win32ui, win32con, win32api
import argparse
import os
import platform
import sys
from pathlib import Path
from time import sleep
import pyautogui
from PIL import ImageGrab, Image
import pyscreeze
import cv2
import torch
import openai
from google.cloud import vision
import io
from models.common import DetectMultiBackend
from utils.dataloaders import IMG_FORMATS, VID_FORMATS, LoadImages, LoadScreenshots, LoadStreams,LoadImagesDirectly
from utils.general import (LOGGER, Profile, check_file, check_img_size, check_imshow, check_requirements, colorstr, cv2,
                           increment_path, non_max_suppression, print_args, scale_boxes, strip_optimizer, xyxy2xywh)
from utils.plots import Annotator, colors, save_one_box
from utils.torch_utils import select_device, smart_inference_mode

# 从环境变量中读取API密钥
openai.api_key = os.getenv("OPENAI_API_KEY")
# 设置 Google Cloud 认证环境变量
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'D:\code_HW\yolov9\yolov9-desktop-elements-capture\fit-aleph-411206-f11a71fdce69.json'

# 确保环境变量已正确设置
if not openai.api_key:
    raise ValueError("API key not found. Please set the OPENAI_API_KEY environment variable.")

# 设置代理环境变量
os.environ['http_proxy'] = 'http://127.0.0.1:7899'
os.environ['https_proxy'] = 'http://127.0.0.1:7899'
os.environ['ALL_PROXY'] = 'socks5://127.0.0.1:7898'

FILE = Path(__file__).resolve()
ROOT = FILE.parents[0]  # YOLO root directory
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  # add ROOT to PATH
ROOT = Path(os.path.relpath(ROOT, Path.cwd()))  # relative

def grab_screen(region=None):
    hwin = win32gui.GetDesktopWindow()
    if region:
            left,top,x2,y2 = region
            width = x2 - left + 1
            height = y2 - top + 1
    else:
        width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
        height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
        left = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
        top = win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)
    hwindc = win32gui.GetWindowDC(hwin)
    srcdc = win32ui.CreateDCFromHandle(hwindc)
    memdc = srcdc.CreateCompatibleDC()
    bmp = win32ui.CreateBitmap()
    bmp.CreateCompatibleBitmap(srcdc, width, height)
    memdc.SelectObject(bmp)
    memdc.BitBlt((0, 0), (width, height), srcdc, (left, top), win32con.SRCCOPY)
    signedIntsArray = bmp.GetBitmapBits(True)
    img = np.fromstring(signedIntsArray, dtype='uint8')
    img.shape = (height,width,4)
    srcdc.DeleteDC()
    memdc.DeleteDC()
    win32gui.ReleaseDC(hwin, hwindc)
    win32gui.DeleteObject(bmp.GetHandle())
    return cv2.cvtColor(img, cv2.COLOR_BGRA2RGB)

def analyze_image(image_path):
    client = vision.ImageAnnotatorClient()
    with io.open(image_path, 'rb') as image_file:
        content = image_file.read()
    image = vision.Image(content=content)
    response = client.label_detection(image=image)
    labels = response.label_annotations
    descriptions = [label.description for label in labels]
    return ', '.join(descriptions)

def generate_explanation(description):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": description}
        ]
    )
    return response['choices'][0]['message']['content']
def ana_video():
    frames_folder = r'.\tmp_img_folder'
    descriptions = []
    for frame_file in sorted(os.listdir(frames_folder)):
        if frame_file.endswith('.png'):
            frame_path = os.path.join(frames_folder, frame_file)
            description = analyze_image(frame_path)
            descriptions.append(f"Frame {frame_file}: {description}")

    full_description = ' '.join(descriptions)
    explanation = generate_explanation(full_description)
    print("Generated Explanation:")
    print(explanation)
def run():
    last_time = time.time()
    while True:
        # 1920 windowed mode
        screen = grab_screen(region=(0,40,1920,1120))
        img = cv2.resize(screen,None,fx=1,fy=1)
        height,width,channels = img.shape
        #detecting objects
        cv2.imwrite(r".\tmp_img_folder\temp.png", img)
        ana_video()
        last_time = time.time()
        cv2.imshow('window', img)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

if __name__ == '__main__':
    run()