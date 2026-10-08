import requests
from pathlib import Path
import zipfile
import io

URL_GIS = "https://raw.githubusercontent.com/vhgauto/gistaq_parana/main/datos/base_de_datos_gis_acolite.csv"
URL_LAB = "https://raw.githubusercontent.com/vhgauto/gistaq_parana/main/datos/base_de_datos_lab.csv"
URL_REPO_ZIP = "https://github.com/vhgauto/gistaq_parana/archive/refs/heads/main.zip"

RUTA_INPUT = Path(r"D:\GIT\Turbidez\Input")
RUTA_RECORTES = Path(r"D:\GIT\Turbidez\Input\recorte_acolite")


def descargar_archivo(url: str, destino: Path):
    destino.parent.mkdir(parents=True, exist_ok=True)
    r = requests.get(url)
    r.raise_for_status()
    destino.write_bytes(r.content)


def descargar_recortes_zip(url_zip: str, destino: Path, carpeta_origen="recorte_acolite"):
    r = requests.get(url_zip)
    r.raise_for_status()
    with zipfile.ZipFile(io.BytesIO(r.content)) as z:
        for f in z.infolist():
            if f.filename.startswith(f"gistaq_parana-main/{carpeta_origen}/"):
                ruta_local = destino / Path(f.filename).relative_to(f"gistaq_parana-main/{carpeta_origen}")
                if f.is_dir():
                    ruta_local.mkdir(parents=True, exist_ok=True)
                else:
                    ruta_local.parent.mkdir(parents=True, exist_ok=True)
                    ruta_local.write_bytes(z.read(f.filename))


def main():
    descargar_archivo(URL_GIS, RUTA_INPUT / "base_de_datos_gis_acolite.csv")
    descargar_archivo(URL_LAB, RUTA_INPUT / "base_de_datos_lab.csv")
    descargar_recortes_zip(URL_REPO_ZIP, RUTA_RECORTES)


if __name__ == "__main__":
    main()
