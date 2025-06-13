import boto3
import os
from botocore.exceptions import ClientError

s3 = boto3.client("s3")

def verificar_o_crear_bucket(nombre_bucket, region="us-east-1"):
    try:
        s3.head_bucket(Bucket=nombre_bucket)
        print(f"✅ El bucket '{nombre_bucket}' ya existe.")
    except ClientError as e:
        error_code = int(e.response["Error"]["Code"])
        if error_code == 404:
            print(f"ℹ️ El bucket '{nombre_bucket}' no existe. Creando...")

            if region == "us-east-1":
                # en us-east-1 NO se especifica configuración
                s3.create_bucket(Bucket=nombre_bucket)
            else:
                s3.create_bucket(
                    Bucket=nombre_bucket,
                    CreateBucketConfiguration={"LocationConstraint": region}
                )

            print("✅ Bucket creado correctamente.")
        else:
            raise

def subir_archivo(nombre_bucket, archivo_local, clave_destino):
    try:
        s3.upload_file(archivo_local, nombre_bucket, clave_destino)
        print(f"📤 Archivo '{archivo_local}' subido como '{clave_destino}' en el bucket '{nombre_bucket}'.")
    except FileNotFoundError:
        print("❌ El archivo local no fue encontrado.")
    except ClientError as e:
        print("❌ Error al subir el archivo:", e)

# 🔽 CONFIGURA ESTO ABAJO 🔽
nombre_bucket = "daniel-bucket-demo-curso"
archivo_local = "tareas.json"  # Reemplaza con el nombre del archivo que tengas
clave_destino = "backup/tareas.json"  # Nombre con el que se guardará en S3

# 🚀 Ejecutar pasos
verificar_o_crear_bucket(nombre_bucket)
subir_archivo(nombre_bucket, archivo_local, clave_destino)
