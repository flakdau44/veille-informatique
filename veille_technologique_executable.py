import tkinter as tk
from tkinter import messagebox
import feedparser
import smtplib
from email.mime.text import MIMEText

# Dictionnaire des flux RSS avec leur catégorie
rss_feeds = {
    "Réseau": "https://www.lemondeinformatique.fr/flux-rss/thematique/reseaux/rss.xml",
    "Cloud Computing": "https://www.lemondeinformatique.fr/flux-rss/thematique/le-monde-du-cloud-computing/rss.xml",
    "Datacenter": "https://www.lemondeinformatique.fr/flux-rss/thematique/datacenter/rss.xml",
    "Hardware": "https://www.lemondeinformatique.fr/flux-rss/thematique/hardware/rss.xml",
    "Internet": "https://www.lemondeinformatique.fr/flux-rss/thematique/internet/rss.xml",
    "Juridique": "https://www.lemondeinformatique.fr/flux-rss/thematique/juridique/rss.xml",
    "Logiciel": "https://www.lemondeinformatique.fr/flux-rss/thematique/logiciel/rss.xml",
    "OS": "https://www.lemondeinformatique.fr/flux-rss/thematique/os/rss.xml",
    "Poste de travail": "https://www.lemondeinformatique.fr/flux-rss/thematique/poste-de-travail/rss.xml",
    "Sécurité": "https://www.lemondeinformatique.fr/flux-rss/thematique/securite/rss.xml",
    "Services IT": "https://www.lemondeinformatique.fr/flux-rss/thematique/services-it/rss.xml",
    "Stockage": "https://www.lemondeinformatique.fr/flux-rss/thematique/stockage/rss.xml",
    "Korben": "https://korben.info/feed",
    "TechRadar": "https://politepol.com/fd/RXYRAkIMnRWX",
}

def get_news():
    news_dict = {}
    for category, feed in rss_feeds.items():
        try:
            data = feedparser.parse(feed)
            if not data.entries:
                continue
            news_dict[category] = [f"- {entry.title}\n  {entry.link}\n" for entry in data.entries[:5]]
        except Exception as e:
            print(f"Erreur lors du chargement du flux {feed} : {e}")
    
    if not news_dict:
        return "Aucune nouvelle actualité disponible."
    
    return "\n\n".join(
        f"📌 {category}\n" + "\n".join(articles) for category, articles in news_dict.items()
    )

def send_email():
    sender = email_entry.get()
    password = password_entry.get()
    news = get_news()
    
    if not sender or not password:
        messagebox.showerror("Erreur", "Veuillez entrer votre e-mail et mot de passe d'application.")
        return
    
    receiver = sender
    subject = "📢 Alerte IT - Veille Technologique"
    
    msg = MIMEText(news, "plain", "utf-8")
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = receiver
    
    try:
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(sender, password)
        server.sendmail(sender, receiver, msg.as_string())
        server.quit()
        messagebox.showinfo("Succès", "E-mail envoyé avec succès !")
    except Exception as e:
        messagebox.showerror("Erreur", f"Erreur lors de l'envoi de l'email : {e}")

# Création de la fenêtre Tkinter
root = tk.Tk()
root.title("Veille Technologique - Envoi Email")
root.geometry("400x250")

tk.Label(root, text="Adresse e-mail :").pack(pady=5)
email_entry = tk.Entry(root, width=40)
email_entry.pack(pady=5)

tk.Label(root, text="Mot de passe d'application :").pack(pady=5)
password_entry = tk.Entry(root, width=40, show="*")
password_entry.pack(pady=5)

tk.Button(root, text="Envoyer l'email", command=send_email).pack(pady=20)

root.mainloop()
