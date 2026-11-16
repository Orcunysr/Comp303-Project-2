# COMP 303 – Project 2: Comparison of Two Shortest Path Algorithms

Dijkstra (Part 1) ve A* (Part 2) en kısa yol algoritmalarının Python3 ile gerçeklenmesi ve karşılaştırılması (Part 3).

## Gereksinimler

- Python 3.10+ (geliştirme Python 3.12 ile yapıldı)
- `requirements.txt` içindeki paketler (`matplotlib`, `numpy`)

## Kurulum

### 1. Repoyu klonla

```bash
git clone https://github.com/Orcunysr/Comp304-Project-2.git
cd Comp304-Project-2
```


Aktif olduğunda terminal satırının başında `(.venv)` görünür.

### 3. Bağımlılıkları yükle

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Çalıştır

```bash
python src/main.py
```

İşin bitince ortamdan çıkmak için:

```bash
deactivate
```

## Klasör yapısı

```
.
├── src/              # Kaynak kodlar (Dijkstra, A*)
├── requirements.txt  # Python bağımlılıkları
└── README.md
```

## Yeni paket eklerken

```bash
pip install <paket>
```

Ardından paketi `requirements.txt` dosyasına ekle.
