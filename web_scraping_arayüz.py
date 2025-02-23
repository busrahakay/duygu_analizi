import time
import tkinter as tk
from tkinter import messagebox, filedialog
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


# YouTube yorumları çekme fonksiyonu
def fetch_comments(url):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url)
    time.sleep(3)

    last_height = driver.execute_script("return document.documentElement.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
        time.sleep(5)
        new_height = driver.execute_script("return document.documentElement.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    comments = []
    try:
        comment_elements = WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.XPATH, '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]'
                                                           '/ytd-comments/ytd-item-section-renderer/div[3]'))
        )
        comments = [comment.text for comment in comment_elements if comment.text.strip() != ""]
    except Exception as e:
        messagebox.showerror("Hata", f"Yorumlar yüklenemedi: {e}")
    finally:
        driver.quit()

    return comments


# Yorumları arayüzde gösterme ve kaydetme fonksiyonu
def get_video_comments():
    url = url_entry.get().strip()
    if not url:
        messagebox.showerror("Hata", "Lütfen bir YouTube URL'si girin.")
        return

    comments = fetch_comments(url)

    if comments:
        comment_text.delete(1.0, tk.END)
        for comment in comments:
            comment_text.insert(tk.END, f"{comment}\n\n")
    else:
        messagebox.showinfo("Bilgi", "Yorum bulunamadı.")


# Arayüzü oluşturma
app = tk.Tk()
app.title("YouTube Yorum Çekme Aracı")
app.geometry("700x500")
app.configure(bg="#2C3E50")

# URL etiketi ve giriş kutusu
url_label = tk.Label(app, text="YouTube Video URL'si:", font=("Helvetica", 12, "bold"), fg="white", bg="#2C3E50")
url_label.pack(pady=10)
url_entry = tk.Entry(app, width=50, font=("Helvetica", 10))
url_entry.pack(pady=5)

# Yorumları getir butonu
fetch_button = tk.Button(app, text="Yorumları Getir", command=get_video_comments, font=("Helvetica", 12, "bold"),
                         bg="#3498DB", fg="white", activebackground="#2980B9", relief="raised", padx=10, pady=5)
fetch_button.pack(pady=15)

# Yorumları listeleyen bir metin kutusu
comment_text = tk.Text(app, width=80, height=15, wrap='word', font=("Helvetica", 10), bg="#ECF0F1")
comment_text.pack(pady=10)

# Kaydırma çubuğu ekleme
scrollbar = tk.Scrollbar(app, command=comment_text.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
comment_text.config(yscrollcommand=scrollbar.set)

app.mainloop()