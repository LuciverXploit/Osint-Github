#CodeByLuciverXploit
#Jangan Di Recode Susah Bikinya awokawok
#Thanks To Scurity Cracker Indonesia And RAL Cyber Team
#copyright©2024

import requests
import os
import re
from datetime import datetime


user_cache = {}

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def validate_username(username):
    
    return re.match("^[a-zA-Z0-9_-]+$", username)

def get_github_user(username):
    if username in user_cache:
        cached_data = user_cache[username]
        
        if (datetime.now() - cached_data['timestamp']).total_seconds() < 300:
            return cached_data['data']
    
    url = f"https://api.github.com/users/{username}"
    try:
        response = requests.get(url)
        response.raise_for_status()  
        data = response.json()
        
        user_cache[username] = {
            'data': data,
            'timestamp': datetime.now()
        }
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None
    except requests.exceptions.HTTPError as e:
        print(f"Error: {e.response.status_code} - {e.response.reason}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

def print_user_info(data):
    if not data:
        return
    print("\nInformasi Pengguna GitHub:")
    print("- Login:", data.get("login"))
    print("- ID:", data.get("id"))
    print("- Nama:", data.get("name"))
    print("- Bio:", data.get("bio"))
    print("- Jumlah Repositori Publik:", data.get("public_repos"))
    print("- Pengikut:", data.get("followers"))
    print("- Mengikuti:", data.get("following"))
    print("- Tanggal dibuat:", data.get("created_at"))
    print("- Tanggal terakhir diupdate:", data.get("updated_at"))
    print("- Lokasi:", data.get("location"))
    print("- Perusahaan:", data.get("company"))
    print("- Email:", data.get("email"))
    print("- Tautan profil:", data.get("html_url"))
    print("- Tautan avatar:", data.get("avatar_url"))

def main():
    while True:
        clear_screen()
        target = input("- Masukkan username GitHub (kosongkan untuk keluar): ").strip()
        
        if not target:
            print("Keluar dari program.")
            break
        
        if not validate_username(target):
            print("Error: Username tidak valid. Pastikan hanya menggunakan huruf, angka, dash (-), atau underscore (_).")
            input("\nTekan Enter untuk melanjutkan...")
            continue
        
        user_data = get_github_user(target)
        if user_data:
            print_user_info(user_data)
        else:
            print(f"Error: Pengguna '{target}' tidak ditemukan atau terjadi kesalahan.")
        
        choice = input("\nApakah Anda ingin mencari pengguna lain? (y/n): ").strip().lower()
        if choice != 'y':
            print("Keluar dari program.")
            break

if __name__ == "__main__":
    main()