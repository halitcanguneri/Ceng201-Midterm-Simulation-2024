import tkinter as tk
from tkinter import font as tkfont

# Sorular ve cevaplar
sorular = [
    {"soru": "Aşağıdakilerden hangisi ekrana çıktı (output) vermez?", "cevaplar": ['print("Merhaba Dünya!")', 'x = 5', 'print(3 + 4)', 'print(len("Python"))'], "dogru_cevap": 'x = 5'},
    {"soru": "Aşağıdaki Python ifadelerinden hangisi hata (error) üretir?", "cevaplar": ['print("Bugün günlerden " + str(3))', 'print(6 / 3)', 'for i in range(5): print(i)', 'print(len(5))'], "dogru_cevap": 'print(len(5))'},
    {"soru": "Aşağıdakilerden hangisi bir fonksiyon tanımlaması değildir?", "cevaplar": ['def topla(x, y): return x + y', 'def selamVer(): print("Merhaba!")', 'topla = lambda x, y: x + y', 'x = topla(3, 4)'], "dogru_cevap": 'x = topla(3, 4)'},
    {"soru": "Aşağıdaki print ifadelerinden hangisi bir hata üretir?", "cevaplar": ['print("Elma" + "Armut")', 'print("Elma", 5)', 'print("Elma" + 5)', 'print("Elma", "Armut")'], "dogru_cevap": 'print("Elma" + 5)'},
    {"soru": "Aşağıdaki print ifadelerinden hangisi 'Python' ve 'Programlama' \n kelimelerini aynı satırda, aralarında bir boşluk bırakarak yazdırır?", "cevaplar": ['print("Python" + "Programlama")', 'print("Python", "Programlama")', 'print("Python" "Programlama")', 'print("Python - Programlama")'], "dogru_cevap": 'print("Python", "Programlama")'},
    # Diğer sorularınızı buraya ekleyebilirsiniz.
]

# Global değişkenler
soru_index = 0
puan = 0
tampuan = 100
cizim_rengi = "black"
kullanici_cevaplari = []
canvas_cizimleri = []

# Ana pencereyi oluşturma
root = tk.Tk()
root.title("Ceng-201-Midterm-Simulation")
root.geometry("600x600")

def cevap_ver(secilen_cevap):
    global soru_index, puan
    kullanici_cevaplari.append(sorular[soru_index]["cevaplar"][secilen_cevap])
    # Canvas'ı bir PNG dosyası olarak kaydetmek için ekstra kodlar gerekebilir.
    # canvas_cizimleri.append(canvas)

    dogru_cevap = sorular[soru_index]["dogru_cevap"]
    if sorular[soru_index]["cevaplar"][secilen_cevap] == dogru_cevap:
        puan += 20
    
    soru_index += 1
    if soru_index < len(sorular):
        soru_goster()
    else:
        oyunu_ozetle()

def oyunu_ozetle():
    ozet_penceresi = tk.Toplevel(root)
    ozet_penceresi.title("Oyun Özeti")
    ozet_penceresi.geometry("800x600")

    for i, soru in enumerate(sorular):
        tk.Label(ozet_penceresi, text=f"Soru {i + 1}: {soru['soru']}", anchor='w', justify='left').pack(fill='x')
        tk.Label(ozet_penceresi, text=f"Verdiğiniz Cevap: {kullanici_cevaplari[i]}", anchor='w', justify='left').pack(fill='x')
        tk.Label(ozet_penceresi, text=f"Doğru Cevap: {soru['dogru_cevap']}", anchor='w', justify='left').pack(fill='x')
        # Burada her sorunun canvas çizimini göstermek için ekstra kodlar gerekebilir.
        # Örneğin, canvas_cizimleri[i] ile ilgili çizimi gösterebilirsiniz.



    yazi_fontu = tkfont.Font(family="Helvetica", size=12, weight="bold")
    yazi_etiketi = tk.Label(ozet_penceresi, text="Dersten aldığın not 0(sıfır), Çünkü ben tatmin olmadım.", fg="red", font=yazi_fontu, anchor='s')
    yazi_etiketi.pack(fill='x')

    tk.Label(ozet_penceresi, text=f"Hak ettiğiniz not: {puan}/{tampuan}", anchor='e').pack(fill='x')
    foto = tk.PhotoImage(file="Hoca1.png")
    resim_etiketi = tk.Label(ozet_penceresi, image=foto)
    resim_etiketi.image = foto  # Bu referansı saklamak önemli
    resim_etiketi.pack()

def soru_goster():
    global soru_index, canvas
    # Mevcut widget'ları temizle
    for widget in root.winfo_children():
        widget.destroy()

    soru_etiketi = tk.Label(root, text=sorular[soru_index]["soru"])
    soru_etiketi.pack()

    for i, cevap in enumerate(sorular[soru_index]["cevaplar"]):
        cevap_butonu = tk.Button(root, text=cevap, command=lambda i=i: cevap_ver(i))
        cevap_butonu.pack()


    canvas = tk.Canvas(root, width=400, height=200, borderwidth=2, relief="solid")
    canvas.pack()
    canvas.bind("<B1-Motion>", ciz)
    canvas.bind("<Button-1>", cizim_baslat)
    otomatik_cizim_yap(canvas)

def otomatik_cizim_yap(canvas):

    # Canvas boyutlarına göre metnin koordinatlarını ayarlayın
    canvas_width = canvas.winfo_reqwidth()
    canvas_height = canvas.winfo_reqheight()

    # Örnek olarak, canvas üzerine bir daire çiziyoruz
    # canvas.create_oval(100, 50, 300, 150, fill="lightblue")

    # Veya bir metin yazdırabilirsiniz

    canvas.create_text(canvas_width / 2, canvas_height/15, text="Soruyu açıklayın!", font=("Arial", 16), fill="black")
    # canvas.create_text(200, 100, text="Buraya çizin", font=("Arial", 16))

    
def cizim_baslat(event):
    global son_x, son_y
    son_x, son_y = event.x, event.y

def ciz(event):
    global son_x, son_y, cizim_rengi, canvas
    canvas.create_line((son_x, son_y, event.x, event.y), fill=cizim_rengi)
    son_x, son_y = event.x, event.y
# İlk soruyu göster
soru_goster()

# Ana döngüyü başlat
root.mainloop()
