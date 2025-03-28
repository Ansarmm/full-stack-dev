import requests
import numpy as np

response = requests.get('https://api.github.com')
print(f"Статус код ответа: {response.status_code}")

a = np.arange(15).reshape(3, 5)

print(a)
print(a.shape)
print(a.ndim)