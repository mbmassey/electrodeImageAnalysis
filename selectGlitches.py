import cv2
import pandas as pd
import os
import numpy as np
import math

def insert_row(x_coor, y_coor, radius, df)
    ds = pd.Series(dtype = 'float64')
    ds['x'] = int(x_coor)
    ds['y'] = int(y_coor)
    ds['area'] = np.pi*radius**2
    df = df.append(ds, ignore_index=True)

def draw_circle(event, x, y, flags, param):
    global x1, y1, x_coor, y_coor, radius, img, windowName, df
    if event == cv2.EVENT_LBUTTONDOWN:
        x1, y1, = x, y
        print("Button down")
    elif event == cv2.EVENT_LBUTTONUP:
        radius = math.hypot(x - x1, y - y1)
        cv2.circle(img, (x1,y1), int(radius), (255, 0, 255), 10)
        cv2.imshow(windowName, img)
        insert_row(x_coor, y_coor, radius, df)
        print("Button up")

def analyze_electrode(file_path, x_coor, y_coor, df): 
    rkey = ord('r')
    nextkey = ord('n')
    esckey = 27
    
    original = cv2.imread(file_path)
    img = original.copy()
    windowName = 'Drawing'
    cv2.namedWindow(windowName)
    cv2.setMouseCallback(windowName, draw_circle)
    cv2.imshow(windowName, img)
    while (True):
        key = cv2.waitKey(20) & 0xFF
        if key == esckey:
            cv2.destroyAllWindows()
            break
        elif key == rkey:
            img = original.copy()
            #delete entries with x,y
            print("restarting")
            cv2.imshow(windowName, img)
        elif key == nextkey:
            break

if __name__ == "__main__":
    indir = 'Gold Set 2/'
    regex = re.compile(r'^y(\d+)_x(\d+)\.JPG$')
    filenames = os.listdir(indir)
    file_list = [f for f in map(regex.match, filenames) if f is not None]
    df = pd.DataFrame()
    for f in file_list:
        curr_file = indir + f.group(0)
        analyze_electrode(curr_file, f.group(2), f.group(1), df)

