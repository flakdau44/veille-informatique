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

# Fonction pour récupérer les articles récents
def get_news():
    news_dict = {}  # Dictionnaire pour stocker les articles par catégorie
    
    for category, feed in rss_feeds.items():
        print(f"🔍 Récupération des articles pour la catégorie : {category}")

        try:
            data = feedparser.parse(feed)

            if not data.entries:
                print(f"⚠️ Aucun article trouvé pour {category}")
                continue  

            # Stocker les articles sous la catégorie correspondante
            news_dict[category] = [
                f"- {entry.title}\n  {entry.link}\n" for entry in data.entries[:5]
            ]

        except Exception as e:
            print(f"❌ Erreur lors du chargement du flux {feed} : {e}")

    if not news_dict:
        return "⚠️ Aucune nouvelle actualité disponible pour l’instant."

    # Construire le message avec des sections par catégorie
    formatted_news = "\n\n".join(
        f"📌 {category}\n" + "\n".join(articles)
        for category, articles in news_dict.items()
    )

    return formatted_news

# Fonction pour envoyer un email via Gmail
def send_email(news):
    sender = "lchevet.simplon@gmail.com"
    receiver = "lchevet.simplon@gmail.com"
    subject = "📢 Alerte IT - Veille Technologique"
    password = "rjru grmz aqzm swtm"  # Utilise le mot de passe d'application

    msg = MIMEText(news, "plain", "utf-8")
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = receiver

    try:
        # Connexion SMTP pour Gmail
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(sender, password)
        server.sendmail(sender, receiver, msg.as_string())
        server.quit()
        print("✅ Email envoyé avec succès via Gmail !")
    except Exception as e:
        print(f"❌ Erreur lors de l'envoi de l'email : {e}")

# Exécuter le script
if __name__ == "__main__":
    news = get_news()
    print("\n📊 Résumé des articles récupérés :\n")
    print(news)  # Affichage des articles récupérés dans le terminal
    send_email(news)  # Envoi des articles par email
