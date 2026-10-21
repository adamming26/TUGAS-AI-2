# Penghitung jari (kamera langsung)

Mengenali 3 jari atau 5 jari dari kamera. Model sudah tertanam di `index.html`.

## Cara menjalankan (kamera pasti didukung lewat localhost)
- Windows: klik dua kali `jalankan.bat`
- macOS/Linux: `python3 jalankan.py`

Browser terbuka otomatis di http://localhost:8080/index.html. Klik **Mulai kamera**, lalu **Izinkan**.

## Tanpa Python
- Seret folder ini ke https://app.netlify.com/drop untuk mendapat tautan HTTPS, atau
- VS Code + ekstensi Live Server, atau `npx serve .` (Node.js).

## Jika kamera tidak muncul
- Pastikan alamat diawali `http://localhost` atau `https://`, bukan `file://`.
- Klik ikon kamera/gembok di address bar, pilih Izinkan.
- Tutup aplikasi lain yang memakai kamera (Zoom, Meet, dll).
- Cadangan: tombol **Ambil foto** / **Unggah foto**.
