import os

print("Folder saat ini", os.getcwd())

print("Sistem Operasi", os.name)

print("main.py", os.path.exists("main.py"))

fila_path = "/Users/khannedy/Developments/PYTHON/belajar-python-modules/main.py"
print("Directory", os.path.dirname(fila_path))
print("File", os.path.basename(fila_path))