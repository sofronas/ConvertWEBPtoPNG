from pathlib import Path
from PIL import Image
import os

def main():
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    for f in files:
        if f == "convert.py":
            continue
        im = Image.open(f).convert("RGB")
        kat = f[:-5] + ".png"
        im.save(kat,"png")
        #print(f[:-5])

if __name__ == '__main__':
    main()
