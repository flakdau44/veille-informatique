import feedparser
import smtplib
from email.mime.text import MIMEText

# Liste des flux RSS
rss_feeds = [
    "https://www.lemondeinformatique.fr/flux-rss/thematique/reseaux/rss.xml" # Réseau
    "https://www.lemondeinformatique.fr/flux-rss/thematique/le-monde-du-cloud-computing/rss.xml" # Cloud
    "https://www.lemondeinformatique.fr/flux-rss/thematique/datacenter/rss.xml" # Datacenter
    "https://www.lemondeinformatique.fr/flux-rss/thematique/hardware/rss.xml" # Hardware
    "https://www.lemondeinformatique.fr/flux-rss/thematique/internet/rss.xml" # Internet
    "https://www.lemondeinformatique.fr/flux-rss/thematique/juridique/rss.xml" # Juridique
    "https://www.lemondeinformatique.fr/flux-rss/thematique/logiciel/rss.xml" # Software
    "https://www.lemondeinformatique.fr/flux-rss/thematique/os/rss.xml" # OS
    "https://www.lemondeinformatique.fr/flux-rss/thematique/poste-de-travail/rss.xml" # Desktop
    "https://www.lemondeinformatique.fr/flux-rss/thematique/reseaux/rss.xml" # Réseau
    "https://www.lemondeinformatique.fr/flux-rss/thematique/securite/rss.xml" # Sécurité
    "https://www.lemondeinformatique.fr/flux-rss/thematique/services-it/rss.xml" # Services IT
    "https://www.lemondeinformatique.fr/flux-rss/thematique/stockage/rss.xml" # Stockage
]

# Fonction pour récupérer les articles récents
def get_news():
    news_list = []
    
    for feed in rss_feeds:
        print(f"🔍 Récupération des articles depuis : {feed}")  # Debugging

        try:
            data = feedparser.parse(feed)

            # Afficher le contenu complet du flux pour le débogage
            print(f"🔹 Contenu du flux récupéré : {data}")

            if not data.entries:
                print(f"⚠️ Aucun article trouvé pour {feed}")
                continue  # Passe au flux suivant

            for entry in data.entries[:10]:  # Limite à 10 articles par source
                print(f"✅ Article trouvé : {entry.title}")
                news_list.append(f"{entry.title}\n{entry.link}\n")

        except Exception as e:
            print(f"❌ Erreur lors du chargement du flux {feed} : {e}")

    if not news_list:
        return "⚠️ Aucune nouvelle actualité disponible pour l’instant."

    return "\n".join(news_list)

# Fonction pour envoyer un email via Gmail
def send_email(news):
    sender = "ton_email@gmail.com"
    receiver = "ton_email@gmail.com"
    subject = "📢 Alerte IT - Veille Technologique"
    password = "ton_mdp_application"  # Utilise le mot de passe d'application

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
