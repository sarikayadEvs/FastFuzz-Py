import requests
import threading
import os
import urllib3
from tkinter import filedialog, Tk

urllib3.disable_warnings()

def dosya_sec():
    root = Tk()
    root.withdraw()
    yol = filedialog.askopenfilename()
    root.destroy()
    return yol

def tara(target, path, extler, ana_boyut):
    liste = [path]
    for e in extler:
        liste.append(f"{path}.{e}")

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/110.0.0.0'}
    
    for p in liste:
        url = f"{target.rstrip('/')}/{p}"
        try:
            r = requests.get(url, headers=headers, timeout=10, verify=False, allow_redirects=True)
            boyut = len(r.content)
            
            if r.status_code == 200:
                if abs(boyut - ana_boyut) > 50:
                    print(f" [+] BULUNDU: {url} | Boyut: {boyut}")
            elif r.status_code == 403:
                print(f" [!] YASAKLI: {url}")
        except:
            pass

def main():
    print("\n--- WEB FUZZER v2 ---")
    site = input("Hedef URL (https://...): ").strip()
    if not site.startswith("http"):
        site = "https://" + site

    print("Wordlist dosyasını seçin...")
    w_yol = dosya_sec()
    if not w_yol:
        print("Dosya seçilmedi, çıkılıyor.")
        return

    eklentiler = input("Uzantılar (virgülle ayır örn: php,html): ").split(",")
    eklentiler = [i.strip() for i in eklentiler if i.strip()]

    print("[*] Siteye bağlanılıyor...")
    try:
        r_ana = requests.get(site, timeout=15, verify=False)
        ana_boyut = len(r_ana.content)
        print(f"[*] Bağlantı tamam. Ana sayfa boyutu: {ana_boyut}\n")
    except Exception as e:
        print(f"Hata: Siteye bağlanılamadı. {e}")
        return

    with open(w_yol, "r", encoding="utf-8", errors="ignore") as f:
        satirlar = f.read().splitlines()

    print(f"[*] {len(satirlar)} kelime taranıyor...\n")

    threads = []
    for s in satirlar:
        t = threading.Thread(target=tara, args=(site, s, eklentiler, ana_boyut))
        t.start()
        threads.append(t)
        
        if len(threads) >= 15:
            for t in threads:
                t.join()
            threads = []

    for t in threads:
        t.join()

    print("\n[*] Tarama bitti.")

if __name__ == "__main__":
    main()