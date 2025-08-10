import numpy as np
import cv2
import matplotlib.pyplot as plt

f1 = np.array([
    [1, 1, 3, 1, 2, 1, 1],
    [3, 0, 3, 1, 3, 2, 0],
    [1, 3, 6, 5, 9, 6, 0],
    [0, 3, 4, 5, 7, 8, 2],
    [2, 0, 1, 0, 4, 6, 0],
    [0, 2, 1, 2, 7, 4, 0]
])

f2 = np.array([
    [0, 2, 0, 3, 5, 7, 0],
    [1, 2, 1, 1, 6, 6, 0],
    [0, 1, 0, 0, 3, 1, 0],
    [2, 0, 1, 3, 2, 1, 0],
    [2, 1, 3, 1, 1, 3, 0],
    [3, 2, 1, 2, 3, 1, 0]
])

f_sum = f1 + f2

f1_median = cv2.medianBlur(f1.astype(np.uint8), 3)
f2_median = cv2.medianBlur(f2.astype(np.uint8), 3)
f_sum_median = cv2.medianBlur(f_sum.astype(np.uint8), 3)

print("Image f1 filtrée :\n", f1_median)
print("Image f2 filtrée :\n", f2_median)
print("Image f1 + f2 filtrée :\n", f_sum_median)


#2

img = cv2.imread("lenam.bmp", cv2.IMREAD_GRAYSCALE)

filter_sizes = [3, 5, 7, 9, 11]

plt.figure(figsize=(12, 6))
plt.subplot(1, len(filter_sizes) + 1, 1)
plt.imshow(img, cmap="gray")
plt.title("Originale")
plt.axis("off")

for i, k in enumerate(filter_sizes):
    img_filtered = cv2.medianBlur(img, k)
    
    plt.subplot(1, len(filter_sizes) + 1, i + 2)
    plt.imshow(img_filtered, cmap="gray")
    plt.title(f"Filtre {k}x{k}")
    plt.axis("off")

    cv2.imwrite(f"lenam_filtered_{k}x{k}.bmp", img_filtered)

plt.show()
plt.close('all')  
