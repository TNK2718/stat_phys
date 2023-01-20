from PIL import Image
from io import BytesIO
import numpy as np
import os

def main():
    os.makedirs('./output', exist_ok=True)

    height = 100
    width = 100
    grids = np.zeros((width, height), dtype=int)
    # mainloop
    iter_num = 1000
    for iter in range(iter_num):
        col = np.random.randint(0, width)
        h = height - 1
        while True:
            if grids[col, h - 1] > 0:
                break
            if grids[col - 1, h] > 0:
                break
            if col + 1 < width and grids[col + 1, h] > 0:
                break
            if col + 1 >= width and grids[width - 1 - (col + 1 - width), h] > 0:
                break
            if h == 0:
                break
            h -= 1
        grids[col, h] = 255
        
        # save image
        pil_img = Image.fromarray(grids.astype(np.uint8)).rotate(90)
        pil_img.save('./output/ballistic_aggregation_{0}.jpg'.format(iter))

if __name__ == '__main__':
    main()