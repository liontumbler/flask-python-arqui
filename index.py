import psutil
cpu_usage = psutil.cpu_percent(interval=1)
print(f"Uso de CPU: {cpu_usage}%")

import GPUtil
gpus = GPUtil.getGPUs()
print(gpus)
#gpu = gpus[0]
#print(gpu)
"""
for gpu in gpus:
    print(f"GPU: {gpu.name}")
    print(f"Uso de GPU: {gpu.load * 100}%")
    print(f"Memoria libre: {gpu.memoryFree}MB")
    print(f"Memoria utilizada: {gpu.memoryUsed}MB")
    print(f"Memoria total: {gpu.memoryTotal}MB")
    print(f"Temperatura: {gpu.temperature} C")
"""

from flask import Flask
from src.routes.routes import init_routes

app = Flask(__name__)

init_routes(app)

if __name__ == '__main__':
    app.run(debug=True, port=5000)