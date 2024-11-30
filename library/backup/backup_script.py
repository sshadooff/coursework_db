import os
import json
import datetime
import shutil
import yadisk
import subprocess

# Параметры подключения к базе данных
with open("config.json") as config_file:
    config = json.load(config_file)

DB_NAME = config["DB_SETTINGS"]["DB_NAME"]
DB_USER = config["DB_SETTINGS"]["DB_USER"]
DB_PASSWORD = config["DB_SETTINGS"]["DB_PASSWORD"]
DB_HOST = config["DB_SETTINGS"]["DB_HOST"]
DB_PORT = config["DB_SETTINGS"]["DB_PORT"]

# Параметры Яндекс.Диска
YANDEX_TOKEN = config["YANDEX_TOKEN"]
YANDEX_DIR = "/backups/"

# Директория для хранения резервной копии
BACKUP_DIR = "backup"
os.makedirs(BACKUP_DIR, exist_ok=True)

# Имя файла резервной копии
TIMESTAMP = str(datetime.date.today())
BACKUP_FILE = os.path.join(BACKUP_DIR, f"db_backup_{TIMESTAMP}.sql")
ZIP_NAME = f"{TIMESTAMP}.zip"


def create_backup():
    try:
        # Создаем резервную копию базы данных с помощью subprocess
        command = [
            "pg_dumpall",
            f"--username={DB_USER}",
            f"--host={DB_HOST}",
            f"--port={DB_PORT}",
            "--no-password",
            "-f",
            BACKUP_FILE,
        ]

        # Устанавливаем окружение с паролем
        env = os.environ.copy()
        env["PGPASSWORD"] = DB_PASSWORD

        # Выполнение команды pg_dumpall
        subprocess.run(command, env=env, check=True)
        print(f"Резервная копия базы данных создана: {BACKUP_FILE}")

        # Архивируем резервную копию
        shutil.make_archive(os.path.join(BACKUP_DIR, TIMESTAMP), "zip", BACKUP_DIR)
        print(f"Архив создан: {BACKUP_DIR}/{ZIP_NAME}")

        # Загрузка на Яндекс.Диск
        upload_to_yandex_disk()

    except subprocess.CalledProcessError as e:
        print(f"Ошибка создания резервной копии базы данных: {e}")
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")


def upload_to_yandex_disk():
    y = yadisk.YaDisk(token=YANDEX_TOKEN)
    try:
        if not y.exists(YANDEX_DIR):
            y.mkdir(YANDEX_DIR)

        y.upload(os.path.join(BACKUP_DIR, ZIP_NAME), f"{YANDEX_DIR}{ZIP_NAME}")
        print(f"Резервная копия загружена на Яндекс.Диск: {YANDEX_DIR}{ZIP_NAME}")

    except Exception as e:
        print(f"Ошибка при загрузке на Яндекс.Диск: {str(e)}")


if __name__ == "__main__":
    create_backup()
