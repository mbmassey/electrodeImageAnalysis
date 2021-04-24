import cv2
import os
import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('evanstyle.mplstyle')

df = pd.DataFrame()

def insert_row(radius):
    global df
    ds = pd.Series(dtype = 'float64')
    ds['x'] = int(x_coor)
    ds['y'] = int(y_coor)
    ds['area'] = np.pi*radius**2
    df = df.append(ds, ignore_index=True)

def draw_circle(event, x, y, flags, param):
    global img, x1, y1
    if event == cv2.EVENT_LBUTTONDOWN:
        x1, y1, = x, y
        print("Button down")
    elif event == cv2.EVENT_LBUTTONUP:
        radius = np.hypot(x - x1, y - y1)
        cv2.circle(img, (x1,y1), int(radius), (255, 0, 255), 10)
        cv2.imshow(windowName, img)
        insert_row(radius)
        print("Button up")

def analyze_electrode(file_path, escpress): 
    global df, img, windowName
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
            escpress = True
            break
        elif key == rkey:
            img = original.copy()
            #delete entries with x,y
            print(df)
            df = df.drop(df[(df["x"] == int(x_coor)) & (df["y"] == int(y_coor))].index)
            print("restarting")
            print(df)
            cv2.imshow(windowName, img)

        elif key == nextkey:
            break
    return escpress

if __name__ == "__main__":
    global x_coor, y_coor
    indir = 'Gold Set 2/'
    regex = re.compile(r'^y(\d+)_x(\d+)\.JPG$')
    filenames = os.listdir(indir)
    file_list = [f for f in map(regex.match, filenames) if f is not None]
    escpress = False

    for f in file_list:
        curr_file = indir + f.group(0)
        x_coor, y_coor = f.group(2), f.group(1)
        escpress = analyze_electrode(curr_file, escpress)
        print(df.head(10))
        
        if escpress == True:
            cv2.destroyAllWindows()
            break

    hist = df.hist(column='area', bins=100, figsize = (12,8))
    for ax in hist.flatten():
        ax.grid(False)
        ax.set_xlabel("Area of glitch (pixels^2)")
        ax.set_ylabel("Number of glitches")
        ax.set_title("Area of distinct glitches")
    print("Histogram!")
    plt.show()
