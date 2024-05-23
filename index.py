from flask import Flask
from src.routes.routes import init_routes

import psutil
import GPUtil

cpu_usage = psutil.cpu_percent(interval=1)
print(f"Uso de CPU: {cpu_usage}%")

gpus = GPUtil.getGPUs()
for gpu in gpus:
    print(f"GPU: {gpu.name}")
    print(f"Uso de GPU: {gpu.load * 100}%")
    print(f"Memoria libre: {gpu.memoryFree}MB")
    print(f"Memoria utilizada: {gpu.memoryUsed}MB")
    print(f"Memoria total: {gpu.memoryTotal}MB")
    print(f"Temperatura: {gpu.temperature} C")

app = Flask(__name__)

init_routes(app)

if __name__ == '__main__':
    app.run(debug=True, port=5000)