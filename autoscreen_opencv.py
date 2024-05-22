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

FILE = Path(__file__).resolve()
ROOT = FILE.parents[0]  # YOLO root directory
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  # add ROOT to PATH
ROOT = Path(os.path.relpath(ROOT, Path.cwd()))  # relative

from models.common import DetectMultiBackend
from utils.dataloaders import IMG_FORMATS, VID_FORMATS, LoadImages, LoadScreenshots, LoadStreams,LoadImagesDirectly
from utils.general import (LOGGER, Profile, check_file, check_img_size, check_imshow, check_requirements, colorstr, cv2,
                           increment_path, non_max_suppression, print_args, scale_boxes, strip_optimizer, xyxy2xywh)
from utils.plots import Annotator, colors, save_one_box
from utils.torch_utils import select_device, smart_inference_mode

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
def run():
    last_time = time.time()
    while True:
        # 1920 windowed mode
        screen = grab_screen(region=(0,40,1920,1120))
        img = cv2.resize(screen,None,fx=1,fy=1)
        height,width,channels = img.shape
        #detecting objects
        cv2.imwrite("temp.png", img)
        # 屏幕缩放系数 mac缩放是2 windows一般是1
        screenScale = 1

        # 事先读取按钮截图
        target = cv2.imread(r"steam_logo.png", cv2.IMREAD_GRAYSCALE)

        # 读取图片 灰色会快
        temp = cv2.imread(r'temp.png', cv2.IMREAD_GRAYSCALE)

        theight, twidth = target.shape[:2]
        tempheight, tempwidth = temp.shape[:2]
        print("目标图宽高：" + str(twidth) + "-" + str(theight))
        print("模板图宽高：" + str(tempwidth) + "-" + str(tempheight))
        # 先缩放屏幕截图 INTER_LINEAR INTER_AREA
        scaleTemp = cv2.resize(temp, (int(tempwidth / screenScale), int(tempheight / screenScale)))
        stempheight, stempwidth = scaleTemp.shape[:2]
        print("缩放后模板图宽高：" + str(stempwidth) + "-" + str(stempheight))
        # 匹配图片
        cv2.imwrite("scaleTemp.png", scaleTemp)
        cv2.imwrite("target.png", target)
        res = cv2.matchTemplate(scaleTemp, target, cv2.TM_CCOEFF_NORMED)
        mn_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        if (max_val >= 0.9):
            # 计算出中心点
            top_left = max_loc
            bottom_right = (top_left[0] + twidth, top_left[1] + theight)
            tagHalfW = int(twidth / 2)
            tagHalfH = theight
            tagCenterX = top_left[0] + tagHalfW
            tagCenterY = top_left[1] + tagHalfH
            # 左键点击屏幕上的这个位置
            pyautogui.moveTo(tagCenterX, tagCenterY)
            pyautogui.doubleClick(tagCenterX, tagCenterY, button='left')
        else:
            print("没找到")

        last_time = time.time()
        cv2.imshow('window', img)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
if __name__ == '__main__':
    run()