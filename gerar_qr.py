# Gera os 7 QR codes para a URL onde o mapa foi hospedado.
# Uso:  python gerar_qr.py https://SEU-USUARIO.github.io/mapa-oficina/
import sys, os
try:
    import qrcode
except ImportError:
    os.system(f'"{sys.executable}" -m pip install "qrcode[pil]"'); import qrcode
url = sys.argv[1].rstrip("/") + "/"
os.makedirs("QR codes", exist_ok=True)
for h in ["grupo-1","grupo-2","grupo-3","grupo-4","grupo-5","grupo-6","todos"]:
    qrcode.make(url + "#" + h).save(os.path.join("QR codes", f"qr_map_{h}.png")); print("gerado", h, "->", url + "#" + h)
