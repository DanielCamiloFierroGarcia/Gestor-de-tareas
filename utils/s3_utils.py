import boto3
import os
from datetime import datetime
from botocore.exceptions import ClientError

# Cliente S3 global
s3 = boto3.client("s3")
BUCKET_NAME = "nombre-de-tu-bucket"  # Cambia si usas otro

def bucket_existe(nombre_bucket):
    try:
        s3.head_bucket(Bucket=nombre_bucket)
        return True
    except ClientError as e:
        codigo = e.response["Error"]["Code"]
        if codigo == "404":
            return False
        print("❌ Error al verificar bucket:", codigo)
        return False


def subir_backup(archivo_local):
    if not os.path.exists(archivo_local):
        print("❌ El archivo no existe.")
        return
    if not bucket_existe(BUCKET_NAME):
        print("❌ El bucket no existe. No se puede subir.")
        return

    hoy = datetime.now().strftime("%Y-%m-%d")
    nombre_archivo = os.path.basename(archivo_local)
    clave_s3 = f"backup/{hoy}/{nombre_archivo}"

    try:
        s3.upload_file(archivo_local, BUCKET_NAME, clave_s3)
        print(f"✅ Backup subido a: {clave_s3}")
        #registrar_log("SUBIDA", archivo_local, clave_s3)
    except ClientError as e:
        print("❌ Error al subir:", e)
        
def descargar_backup(fecha, destino_local):
    nombre_archivo = os.path.basename(destino_local)
    clave_s3 = f"backup/{fecha}/{nombre_archivo}"
    
    try:
        s3.head_object(Bucket=BUCKET_NAME, Key=clave_s3)
        s3.download_file(BUCKET_NAME, clave_s3, destino_local)
        print(f"✅ Archivo restaurado como '{destino_local}'")
    except ClientError as e:
        if e.response["Error"]["Code"] == "404":
            print("❌ No existe un backup para esa fecha.")
        else:
            print("❌ Error al descargar:", e)
