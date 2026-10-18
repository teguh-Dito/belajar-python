# modules matematika

PI = 3.14159

NAMA_PEMBUAT = "Tim Matematika"

def tambah(a, b):
    """
    Menambah dua angka
    """
    return a + b

def kurang(a, b):
    """
    Mengurangi dua angka
    """
    return a - b

def kali(a, b):
    """
    Kali dua angka
    """
    return a * b

def bagi(a, b):
    """Bagi dua angka"""
    if b != 0:
        return a / b
    else:
        return "Error: Bilangan tidak boleh 0"

if __name__ == "__main__":
    print("Program ini tidak bisa dijalankan sebagai modul")