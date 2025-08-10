####  Filtre moyenneur #####

import cv2
import numpy as np
import matplotlib.pyplot as plt

images = ["hhrec.bmp", "lenam.bmp", "objectm.bmp"]
filter_sizes = [3, 5, 7, 11]

for img_name in images:
    img = cv2.imread(img_name, cv2.IMREAD_GRAYSCALE)

    plt.figure(figsize=(10, 5))
    plt.subplot(1, len(filter_sizes) + 1, 1)
    plt.imshow(img, cmap="gray")
    plt.title("Originale")
    plt.axis("off")

    for i, k in enumerate(filter_sizes):
        img_filtered = cv2.blur(img, (k, k))  
        plt.subplot(1, len(filter_sizes) + 1, i + 2)
        plt.imshow(img_filtered, cmap="gray")
        plt.title(f"Filtre {k}x{k}")
        plt.axis("off")
        cv2.imwrite(f"{img_name.split('.')[0]}_filtered_{k}x{k}.bmp", img_filtered)

    plt.show()
