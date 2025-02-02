# veille-informatique
Création d'un script en Python pour recevoir des articles par mail dans le cadre de veille informatique.

## Fonctionnalités

- **Récupération des flux RSS** : Le script extrait les derniers articles de plusieurs catégories technologiques comme le réseau, le cloud computing, le datacenter, le hardware, etc.
- **Résumé des articles** : Il affiche les titres des articles avec leurs liens.
- **Envoi par email** : Les articles récupérés sont envoyés par email à une adresse spécifiée.

## Prérequis

Avant d'exécuter le script, assurez-vous d'avoir les éléments suivants :

1. **Python** installé sur votre machine. Ce script a été testé avec Python 3.x.
2. **Bibliothèques Python requises** :
   - `feedparser` : pour analyser les flux RSS.
   - `smtplib` et `email.mime.text` : pour l'envoi des emails.
   
   Vous pouvez installer `feedparser` avec pip :
   
   ```bash
   pip install feedparser
   ```

3. **Compte Gmail** : Vous aurez besoin d'un compte Gmail pour l'envoi des emails. Il est nécessaire de créer un mot de passe d'application si vous utilisez la vérification en deux étapes sur votre compte Google. Vous pouvez le créer [ici](https://myaccount.google.com/apppasswords).

## Configuration

1. **Personnalisez les flux RSS** : Vous pouvez ajouter, supprimer ou modifier les URL des flux RSS dans la liste `rss_feeds`.

2. **Configurez l'email** :
   - Modifiez la variable `sender` pour y mettre votre adresse email Gmail.
   - Modifiez la variable `receiver` pour spécifier l'adresse de réception des emails.
   - Remplacez `ton_mdp_application` par le mot de passe d'application généré par Google pour permettre l'envoi des emails.

## Utilisation

1. Ouvrez et exécutez le script :

   ```bash
   python veille_technologique.py
   ```

2. Le script récupérera les derniers articles des flux RSS et vous enverra un email avec un résumé des articles récents.

## Exemple de Sortie

Lors de l'exécution du script, vous devriez voir un message dans le terminal comme ceci :

```
🔍 Récupération des articles depuis : https://www.lemondeinformatique.fr/flux-rss/thematique/reseaux/rss.xml
🔹 Contenu du flux récupéré : {Contenu complet du flux RSS ici}
✅ Article trouvé : [Titre de l'article]
🔍 Récupération des articles depuis : https://www.lemondeinformatique.fr/flux-rss/thematique/le-monde-du-cloud-computing/rss.xml
...
📊 Résumé des articles récupérés :

[Titre de l'article 1]
[Lien de l'article 1]
[Titre de l'article 2]
[Lien de l'article 2]
...

✅ Email envoyé avec succès via Gmail !
```

L'email envoyé contiendra un résumé des articles récupérés.

## Aide et Dépannage

- Si vous avez des problèmes lors de l'envoi de l'email, assurez-vous que vous avez configuré correctement le mot de passe d'application.
- Si un flux RSS est incorrect ou inaccessible, le script affichera une erreur correspondante et passera au flux suivant.
