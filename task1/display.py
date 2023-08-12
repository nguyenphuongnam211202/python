import tkinter as tk
from tkinter import ttk
from selenium import webdriver
from selenium.webdriver.common.by import By

def extract_data(url, content_xpath):
    extracted_data = []

    browser = webdriver.Chrome('chromedriver.exe')
    browser.get(url)
    
    items = browser.find_elements(By.XPATH, content_xpath)
    
    for item in items:
        extracted_data.append(item.text)
    
    browser.quit()
    return extracted_data

def on_extract_button_click():
    url = url_entry.get()
    content_xpath = xpath_entry.get()
    
    extracted_data = extract_data(url, content_xpath)
    
    result_text.delete(1.0, tk.END)
    for data in extracted_data:
        result_text.insert(tk.END, data + "\n")

root = tk.Tk()
root.title("Web Data Extractor")

# Tạo đối tượng Style để tùy chỉnh giao diện bằng CSS
style = ttk.Style(root)
style.configure("TLabel", font=("Helvetica", 12))
style.configure("TEntry", font=("Helvetica", 12))
style.configure("TButton", font=("Helvetica", 12))

url_label = ttk.Label(root, text="Enter URL:", style="TLabel")
url_label.pack(padx=10, pady=5)

url_entry = ttk.Entry(root, style="TEntry")
url_entry.pack(padx=10, pady=5, fill=tk.X)

xpath_label = ttk.Label(root, text="Enter Content XPath:", style="TLabel")
xpath_label.pack(padx=10, pady=5)

xpath_entry = ttk.Entry(root, style="TEntry")
xpath_entry.pack(padx=10, pady=5, fill=tk.X)

extract_button = ttk.Button(root, text="Extract Data", style="TButton", command=on_extract_button_click)
extract_button.pack(padx=10, pady=10)

result_label = ttk.Label(root, text="Extracted Data:", style="TLabel")
result_label.pack(padx=10, pady=5)

result_text = tk.Text(root, wrap=tk.WORD, height=10, width=40)
result_text.pack(padx=10, pady=5)

root.mainloop()
