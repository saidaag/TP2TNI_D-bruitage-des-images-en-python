import numpy as np
import cv2
import random
import matplotlib.pyplot as plt

def add_noise(image, percentage, noise_type):

    noisy_image = image.copy()
    num_pixels = int(image.size * percentage / 100)

    for _ in range(num_pixels):
        x, y = random.randint(0, image.shape[1]-1), random.randint(0, image.shape[0]-1)
        if noise_type == "poivre":
            noisy_image[y, x] = 0 
        elif noise_type == "sel":
            noisy_image[y, x] = 255  
        elif noise_type == "poivre_et_sel":
            noisy_image[y, x] = 0 if random.random() < 0.5 else 255  

    return noisy_image

img = cv2.imread("lenam.bmp", cv2.IMREAD_GRAYSCALE)
if img is None:
    raise FileNotFoundError("L'image 'lenam.bmp' est introuvable.")

# 1 Ajout du bruit poivre et sel avec différents niveaux (10%, 20%, 30%)
noise_levels = [10, 20, 30]
noisy_images = [add_noise(img, p, "poivre_et_sel") for p in noise_levels]

# 2 Application des filtres moyenneur et médian
filter_sizes = [3, 5, 7, 11]  # Tailles des fenêtres de filtrage

for size in filter_sizes:
    plt.figure(figsize=(12, 8))
    plt.suptitle(f"Comparaison des filtres Moyenneur et Médian - Taille {size}x{size}")

    for i, noisy_img in enumerate(noisy_images):
        # Filtre Moyenneur
        avg_filtered = cv2.blur(noisy_img, (size, size))  
        # Filtre Médian
        median_filtered = cv2.medianBlur(noisy_img, size)  

        plt.subplot(3, 3, i+1)
        plt.imshow(noisy_img, cmap="gray")
        plt.title(f"Bruit {noise_levels[i]}%")
        plt.axis("off")

        plt.subplot(3, 3, i+4)
        plt.imshow(avg_filtered, cmap="gray")
        plt.title(f"Moyenneur {noise_levels[i]}%")
        plt.axis("off")

        plt.subplot(3, 3, i+7)
        plt.imshow(median_filtered, cmap="gray")
        plt.title(f"Médian {noise_levels[i]}%")
        plt.axis("off")

    plt.tight_layout()
    plt.show()

# 3 Ajout du bruit Poivre et Sel séparément
noise_type_list = ["poivre", "sel"]
for noise_type in noise_type_list:
    noisy_image = add_noise(img, 10, noise_type)  # Fixe à 10% pour la comparaison

    plt.figure(figsize=(12, 8))
    plt.suptitle(f"Débruitage du bruit {noise_type.upper()} avec différents filtres")

    for j, size in enumerate(filter_sizes):
        min_filter = cv2.erode(noisy_image, np.ones((size, size)))  # Filtre Min
        max_filter = cv2.dilate(noisy_image, np.ones((size, size)))  # Filtre Max
        median_filter = cv2.medianBlur(noisy_image, size)  # Filtre Médian
        avg_filter = cv2.blur(noisy_image, (size, size))  # Filtre Moyenneur

        titles = ["Original", "Min", "Max", "Médian", "Moyenneur"]
        images = [noisy_image, min_filter, max_filter, median_filter, avg_filter]

        for i in range(5):
            plt.subplot(len(filter_sizes), 5, j*5 + i + 1)
            plt.imshow(images[i], cmap="gray")
            if j == 0:
                plt.title(titles[i])
            plt.axis("off")

    plt.tight_layout()
    plt.show()
