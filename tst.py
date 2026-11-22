import os

dev_dir = '/dev'
devices = os.listdir(dev_dir)

# Фильтрация только файлов устройств (например, sd*, nvme*, tty*)
for dev in sorted(devices):
    path = os.path.join(dev_dir, dev)
    if os.path.exists(path):
        # Можно проверить через os.stat, но простой перечень выглядит так:
        print(path)
