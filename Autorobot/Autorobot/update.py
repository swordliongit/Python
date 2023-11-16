import io
import json
import subprocess
import sys
from threading import Thread, Timer
from tkinter.messagebox import showinfo
import requests
import zipfile
import customtkinter as ctk
import os


from dotenv import load_dotenv
from packaging import version
from cryptography.fernet import Fernet

current_dir = os.path.dirname(__file__)
# Construct a path to the parent directory
parent_directory = os.path.join(current_dir, "..")

load_dotenv(dotenv_path=os.path.join(current_dir, ".env"))

encryption_key = os.getenv("ENCRYPTION_KEY")
cipher_suite = Fernet(encryption_key.encode())


class Update:
    def __init__(self) -> None:
        self.session = requests.Session()

    def Get_Envar(self, var):
        return cipher_suite.decrypt(os.getenv(var).encode()).decode()

    def Login(self):
        """_summary_

        Args:
            session (requests.Session): _description_

        Returns:
            requests.Session: _description_
        """
        raw_data = {
            "jsonrpc": "2.0",
            "params": {
                "login": cipher_suite.decrypt(os.getenv("LOGIN").encode()).decode(),
                "password": cipher_suite.decrypt(os.getenv("PASSWORD").encode()).decode(),
                "db": cipher_suite.decrypt(os.getenv("DB").encode()).decode(),
            },
        }

        headers = {
            "content-type": "application/json",
        }

        payload = json.dumps(raw_data)
        response = self.session.post(url=self.Get_Envar("URL_LOGIN"), data=payload, headers=headers)

        # print(response.content)

    def Read(self):
        raw_data = {
            "id": 35,
            "jsonrpc": "2.0",
            "method": "call",
            "params": {
                "model": self.Get_Envar("MODEL"),
                "domain": [["name", "=", "Prototype"]],
                "fields": ["name", "version", "push_update", "developer"],
                "limit": 80,
                "sort": "",
                "context": {
                    "lang": "en_US",
                    "tz": "Europe/Istanbul",
                    "uid": 2,
                    "allowed_company_ids": [1],
                    "params": {"menu_id": 106, "action": 146, "cids": 1},
                    "bin_size": True,
                },
            },
        }

        headers = {
            "authority": "swordlion.org",
            "accept": "*/*",
            "accept-language": "en-US,en;q=0.9,tr;q=0.8",
            "content-type": "application/json",
            "origin": self.Get_Envar("HEADERS_ORIGIN"),
            "referer": self.Get_Envar("HEADERS_REFERER"),
            "sec-ch-ua": '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
        }

        payload = json.dumps(raw_data)
        response = self.session.post(url=self.Get_Envar("URL_READ"), data=payload, headers=headers)
        response_data = response.json()
        isUpdateAvailable = response_data["result"]["records"][0]["push_update"]
        version_cloud = response_data["result"]["records"][0]["version"]
        developer = response_data["result"]["records"][0]["developer"]
        version_current = ""
        with open(os.path.join(current_dir, ".version"), "r") as vfile:
            version_current = vfile.readline()
        if version.parse(version_current) < version.parse(version_cloud) and not developer:
            return isUpdateAvailable
        else:
            return False

    def IsUpdateAvailable(self) -> bool:
        """_summary_

        Returns:
            bool: _description_
        """
        try:
            self.Login()
        except requests.exceptions.ConnectionError as e:
            raise Exception("Connection Error")
        else:
            return self.Read()

    def ApplyUpdate(self, DownloadDialog: ctk.CTkToplevel, Master: ctk.CTkToplevel):
        """_summary_"""

        if os.path.exists(os.path.join(current_dir, self.Get_Envar("UPDATE_SAVE_PATH"))):
            showinfo("Autorobot", "Güncelleme İndirildi. Uygulama yeniden başlatılacak.")
            subprocess.Popen([os.path.join(parent_directory, "Autorobot_Updater.exe")])
            DownloadDialog.destroy()
            Master.destroy()

        else:
            if self.DownloadUpdate(DownloadDialog):
                showinfo("Autorobot", "Güncelleme İndirildi. Uygulama yeniden başlatılacak.")
                subprocess.Popen([os.path.join(parent_directory, "Autorobot_Updater.exe")])
                DownloadDialog.destroy()
                Master.destroy()

    def DownloadUpdate(self, DownloadDialog: ctk.CTkToplevel):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "Referer": self.Get_Envar("HEADERS_REFERER"),
            "Upgrade-Insecure-Requests": "1",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-User": "?1",
            "TE": "trailers",
        }
        response = self.session.get(url=self.Get_Envar("URL_UPDATE"), headers=headers, stream=True)
        # print(response.content)
        # Check if the request was successful
        if response.status_code == 200:
            total_size = int(response.headers.get("content-length", 0))
            print(total_size)
            downloaded_size = 0
            progress_value = 0
            buffer_size = 1024 * 1024
            with open(os.path.join(current_dir, self.Get_Envar("UPDATE_SAVE_PATH")), "wb") as file:
                buffered_writer = io.BufferedWriter(file, buffer_size=buffer_size)
                for chunk in response.iter_content(chunk_size=buffer_size):
                    buffered_writer.write(chunk)

                    downloaded_size += len(chunk)
                    print((downloaded_size / total_size))
                    DownloadDialog.percent.set(str(int((downloaded_size / total_size) * 100)) + "%")
                    # Calculate progress percentage
                    progress_value = downloaded_size / total_size
                    DownloadDialog.progressbar_1.set(progress_value)
                    DownloadDialog.update_idletasks()
                buffered_writer.flush()

            return True
        else:
            print(f"Failed to download the update. Status code: {response.status_code}")
            return False


if __name__ == "__main__":
    pass
