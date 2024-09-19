import math

#  Noktaların tanımlanması
points = [(1, 2), (3, 4), (5, 1), (7, 8), (2, 9)]  # Örnek noktalar

# Öklid mesafesi fonksiyonunun tanımlanması
def oklidMesafesi(nokta1, nokta2):
    return math.sqrt((nokta2[0] - nokta1[0])**2 + (nokta2[1] - nokta1[1])**2)

# Her nokta çifti arasındaki mesafeleri hesaplama
mesafeler = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        mesafe = oklidMesafesi(points[i], points[j])
        mesafeler.append(mesafe)

#  Minimum mesafeyi bulma ve yazdırma
min_mesafe = min(mesafeler)
print(f"Minimum Öklid Mesafesi: {min_mesafe}")