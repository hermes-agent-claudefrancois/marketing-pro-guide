#!/usr/bin/env python3
"""
MVP Générateur de Contenu d'Affiliation
Génère des articles SEO pour Systeme.io avec liens d'affiliation
Utilise les modèles gratuits OpenRouter (qwen3-coder:free)
"""

import argparse
import json
import os
import requests
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, Optional

# Configuration
OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"
DEFAULT_MODEL = "qwen/qwen3-coder:free"  # Modèle gratuit
FALLBACK_MODEL = "google/gemma-4-31b-it:free"  # Fallback gratuit

# Liens d'affiliation (à remplacer par vos vrais liens)
AFFILIATE_LINKS = {
    "systeme_io": "https://systeme.io/?sa=sa0268466764645998886fff8b439ed15072d58eb1",
    "semrush": "https://www.semrush.com/affiliate/",
    "getresponse": "https://www.getresponse.com/affiliate",
    "hostinger": "https://www.hostinger.fr/affiliates",
}

# Structure des articles
def get_article_prompt(topic: str, article_type: str, keywords: list) -> str:
    """Génère le prompt pour l'article"""
    
    base_prompt = f"""Tu es un expert en marketing digital et rédaction SEO.

Écris un article de blog complet en FRANÇAIS sur: "{topic}"

TYPE D'ARTICLE: {article_type}
MOTS-CLÉS À INTÉGRER: {', '.join(keywords)}

STRUCTURE REQUISE:
1. Titre H1 accrocheur (max 60 caractères, inclut le mot-clé principal)
2. Introduction engageante (2-3 phrases qui captent l'attention)
3. Table des matières (avec ancres vers les sections)
4. Contenu principal avec H2 et H3:
   - Problématique/Contexte
   - Solution détaillée
   - Avantages/Inconvénients (si review/comparison)
   - Guide étape par étape (si tutoriel)
   - Conseils d'expert
5. FAQ (5 questions pertinentes)
6. Conclusion avec Call-to-Action

RÈGLES SEO:
- Densité des mots-clés: 1-2%
- Paragraphes courts (3-4 phrases max)
- Utilise des listes à puces pour la lisibilité
- Ton: professionnel mais accessible
- Public cible: freelances et entrepreneurs débutants

AFFILIATION:
- Intègre naturellement 2-3 recommandations de produits/services
- Mentionne Systeme.io comme solution principale quand pertinent
- Inclus un encart "Notre recommandation" avant la conclusion

FORMAT: Markdown uniquement (pas de balises HTML, pas de code fences autour du texte)

Méta-description (à placer en début d'article, commentaire HTML):
<!-- Meta: [description 160 caractères max] -->"""

    return base_prompt


def generate_with_openrouter(prompt: str, model: str = DEFAULT_MODEL) -> Optional[str]:
    """Génère du contenu via OpenRouter API"""
    
    api_key = os.environ.get("OPENROUTER_API_KEY", "")
    if not api_key:
        print("⚠️  OPENROUTER_API_KEY non défini. Utilisation du mode simulation.")
        return None
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://hermes-agent.local",
        "X-Title": "Hermes Affiliate MVP"
    }
    
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": "Tu es un rédacteur SEO expert spécialisé en marketing digital. Tu écris en français uniquement."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7,
        "max_tokens": 4000
    }
    
    try:
        response = requests.post(OPENROUTER_API_URL, headers=headers, json=payload, timeout=120)
        response.raise_for_status()
        data = response.json()
        return data["choices"][0]["message"]["content"]
    except Exception as e:
        print(f"❌ Erreur API: {e}")
        return None


def generate_article_local(topic: str, article_type: str, keywords: list) -> str:
    """Génère un article avec template local (fallback si API indisponible)"""
    
    date_str = datetime.now().strftime("%d/%m/%Y")
    year = datetime.now().year
    
    templates = {
        "review": f"""# {topic} : Avis Complet et Test {year}

<!-- Meta: Découvrez notre avis complet sur {topic}. Test, fonctionnalités, prix et notre verdict. Guide pour freelances et entrepreneurs. -->

**Date de publication:** {date_str}  
**Temps de lecture:** 8 minutes

---

## Introduction

Vous cherchez une solution tout-en-un pour votre business en ligne ? {topic} fait beaucoup parler de lui dans le monde du marketing digital. Dans cet avis complet, nous analysons en profondeur cette plateforme pour vous aider à faire le bon choix.

## Table des matières

- [Qu'est-ce que {topic} ?](#quest-ce-que)
- [Fonctionnalités principales](#fonctionnalites)
- [Avantages et inconvénients](#avantages-inconvenients)
- [Tarifs et formules](#tarifs)
- [Comment démarrer](#demarrer)
- [FAQ](#faq)
- [Notre verdict](#verdict)

## Qu'est-ce que {topic} ?

{topic} est une plateforme marketing tout-en-one conçue pour les entrepreneurs, freelances et petites entreprises. Elle combine :

- **Création de funnels de vente**
- **Email marketing automation**
- **Hébergement de formations en ligne**
- **Gestion d'affiliation**
- **Blog et site web**

## Fonctionnalités principales

### 1. Constructeur de funnels

Interface drag-and-drop intuitive pour créer des pages de capture, de vente et de remerciement sans coder.

### 2. Email marketing

- Autorépondeurs illimités
- Segmentation avancée
- Templates d'emails professionnels
- Taux de livrabilité élevé

### 3. Formation en ligne

Hébergez et vendez vos cours directement sur la plateforme avec protection du contenu.

## Avantages et inconvénients

| ✅ Avantages | ❌ Inconvénients |
|-------------|------------------|
| Plan gratuit généreux | Courbe d'apprentissage |
| Tout-en-un | Moins de templates que certains concurrents |
| Commission affiliation 60% | Support uniquement en anglais |
| Prix très compétitifs | |

## Tarifs et formules

{topic} propose plusieurs formules :

- **Gratuit** : Jusqu'à 2 000 contacts, 3 funnels
- **Startup** (27€/mois) : 5 000 contacts, 10 funnels
- **Webinar** (47€/mois) : 10 000 contacts, webinars illimités
- **Entreprise** (97€/mois) : Contacts illimités

## Notre recommandation

💡 **Pour débuter gratuitement:** [Essayer {topic} sans carte bancaire]({AFFILIATE_LINKS.get('systeme_io', '#')})

Si vous cherchez une alternative complète avec plus de fonctionnalités SEO, nous recommandons également de jeter un œil à [Semrush]({AFFILIATE_LINKS.get('semrush', '#')}) pour l'analyse de vos concurrents.

## FAQ

### {topic} est-il vraiment gratuit ?

Oui, le plan gratuit est fonctionnel et sans limite de temps. Parfait pour tester la plateforme.

### Puis-je migrer depuis ClickFunnels ?

Oui, {topic} propose des ressources et un support pour faciliter la migration.

### Le support client est-il efficace ?

Le support est réactif, principalement en anglais. La communauté francophone est active sur les réseaux.

### Quelle est la durée du cookie d'affiliation ?

**À vie !** C'est l'un des meilleurs programmes d'affiliation du marché.

### Puis-je vendre mes formations ?

Absolument. La plateforme est conçue pour créer, héberger et vendre des formations en ligne.

## Notre verdict

{topic} est une excellente solution pour les entrepreneurs qui veulent centraliser leurs outils marketing sans se ruiner. Le rapport qualité-prix est imbattable, surtout avec le plan gratuit.

**Note finale : 4.5/5** ⭐

👉 **[Commencer gratuitement avec {topic}]({AFFILIATE_LINKS.get('systeme_io', '#')})**

---

*Cet article contient des liens d'affiliation. Si vous vous inscrivez via nos liens, nous recevons une commission sans aucun coût supplémentaire pour vous.*
""",
        
        "comparison": f"""# {topic} : Comparatif Complet {datetime.now().year}

<!-- Meta: Comparatif détaillé : {topic}. Découvrez lequel choisir selon vos besoins et votre budget. Guide expert pour entrepreneurs. -->

**Date de publication:** {date_str}

---

## Introduction

Le choix de la bonne plateforme marketing peut faire la différence entre un business qui décolle et un qui stagne. Dans ce comparatif, nous analysons {topic} pour vous aider à faire le meilleur choix.

## Sommaire

- [Critères de comparaison](#criteres)
- [Comparatif technique](#comparatif)
- [Rapport qualité-prix](#rapport)
- [Recommandations par profil](#profils)
- [Verdict final](#verdict)

## Critères de comparaison

Nous avons évalué ces solutions sur :

1. **Prix et value for money**
2. **Facilité d'utilisation**
3. **Fonctionnalités marketing**
4. **Support client**
5. **Intégrations disponibles**

## Comparatif technique

| Critère | Systeme.io | ClickFunnels | Kartra |
|---------|------------|--------------|--------|
| Prix départ | Gratuit | 97$/mois | 99$/mois |
| Funnels illimités | ❌ (3 gratuit) | ✅ | ✅ |
| Contacts | 2 000 (gratuit) | Illimité | 2 500 |
| Commission aff. | 60% vie | 40% | 40% |
| Formation incluse | ✅ | ✅ | ✅ |
| Email marketing | ✅ | ❌ (extra) | ✅ |

## Rapport qualité-prix

**Systeme.io** remporte haut la main cette catégorie avec :
- Un plan gratuit véritablement utilisable
- Des prix 3 à 4 fois moins chers que la concurrence
- Des fonctionnalités comparables

## Recommandations par profil

### Débutant avec budget limité
👉 **Systeme.io** - Commencez gratuitement, évoluez selon vos besoins

### Entrepreneur confirmé
👉 **Kartra** - Plus de puissance pour les opérations avancées

### Marketeur agressif
👉 **ClickFunnels** - La référence mais prix élevé

## Notre recommandation

Pour 90% des freelances et entrepreneurs francophones, **Systeme.io** est le choix le plus pertinent en {year}.

🎯 **[Tester Systeme.io gratuitement]({AFFILIATE_LINKS.get('systeme_io', '#')})**

## Verdict final

| Rang | Solution | Score | Meilleur pour |
|------|----------|-------|---------------|
| 🥇 | Systeme.io | 9/10 | Budget + features |
| 🥈 | Kartra | 7.5/10 | Power users |
| 🥉 | ClickFunnels | 7/10 | Marketing agressif |

---

*Liens d'affiliation présents dans cet article. Votre soutien nous permet de créer du contenu gratuit de qualité.*
""",
        
        "tutorial": f"""# {topic} : Guide Étape par Étape {datetime.now().year}

<!-- Meta: Apprenez {topic} avec notre guide complet. Tutoriel pas à pas pour débutants. Maîtrisez l'outil en 30 minutes. -->

**Date:** {date_str} | **Niveau:** Débutant | **Temps:** 30 min

---

## Introduction

Dans ce tutoriel complet, vous allez apprendre {topic}. Que vous soyez débutant complet ou que vous cherchiez à optimiser votre workflow, ce guide est fait pour vous.

## Prérequis

- Un compte (gratuit suffit)
- 30 minutes de temps
- Une idée de produit/service à promouvoir

## Sommaire

1. [Configuration initiale](#config)
2. [Création de votre premier funnel](#funnel)
3. [Configuration des emails](#emails)
4. [Mise en ligne](#publication)
5. [Optimisations](#optimisation)

## Configuration initiale

### Étape 1 : Créer votre compte

Rendez-vous sur [Systeme.io]({AFFILIATE_LINKS.get('systeme_io', '#')}) et créez un compte gratuit. Le processus prend moins de 2 minutes.

### Étape 2 : Configurer votre profil

- Ajoutez votre photo de profil
- Renseignez vos informations de paiement
- Configurez votre fuseau horaire

## Création de votre premier funnel

### Étape 3 : Choisir un template

1. Allez dans "Funnels"
2. Cliquez sur "Créer un funnel"
3. Sélectionnez "Squeeze page" pour commencer

### Étape 4 : Personnaliser la page

- Modifier le titre (incluez votre mot-clé principal)
- Ajouter une image accrocheuse
- Rédiger un call-to-action clair

## Configuration des emails

### Étape 5 : Créer une séquence

1. Section "Emails"
2. "Créer une campagne"
3. Rédigez 3-5 emails de nurture

**Template email de bienvenue:**
```
Objet: Bienvenue ! Voici votre [lead magnet]

Bonjour {{contact.name}},

Merci de votre intérêt ! Voici ce que vous allez découvrir...
```

## Notre recommandation

💡 Pour accélérer vos résultats, intégrez un outil d'analyse SEO comme [Semrush]({AFFILIATE_LINKS.get('semrush', '#')}) pour identifier les opportunités de mots-clés.

## Mise en ligne

### Étape 6 : Tester votre funnel

- Vérifiez tous les liens
- Testez le formulaire d'inscription
- Contrôlez l'apparence mobile

### Étape 7 : Publier

Cliquez sur "Rendre public" et votre funnel est en ligne !

## Optimisations

### Conseils d'expert

1. **A/B testez vos pages** - Changez un élément à la fois
2. **Suivez vos métriques** - Taux de conversion, ouverture d'emails
3. **Segmentez votre audience** - Messages personnalisés = meilleurs résultats

## FAQ

### Combien de temps avant de voir des résultats ?

Avec une promotion cohérente, comptez 2-4 semaines pour vos premiers leads qualifiés.

### Puis-je connecter mon nom de domaine ?

Oui, dès le plan Startup (27€/mois) vous pouvez utiliser votre domaine personnalisé.

### Faut-il des compétences techniques ?

Non, l'interface est conçue pour les débutants. Aucun code requis.

## Conclusion

Vous savez maintenant {topic}. La clé du succès est la régularité : appliquez ces étapes et ajustez selon vos résultats.

🚀 **Prochaine étape:** [Créer votre compte gratuit]({AFFILIATE_LINKS.get('systeme_io', '#')}) et mettez ce tutoriel en pratique dès aujourd'hui !

---

*Ce tutoriel vous a aidé ? Partagez-le avec d'autres entrepreneurs !*
"""
    }
    
    return templates.get(article_type, templates["review"])


def generate_article(topic: str, article_type: str, output_file: str, keywords: list = None):
    """Génère un article complet"""
    
    print(f"📝 Génération article: {topic}")
    print(f"   Type: {article_type}")
    print(f"   Output: {output_file}")
    
    if keywords is None:
        keywords = [topic.lower(), "guide", "2025", "avis"]
    
    # Essayer API OpenRouter d'abord
    prompt = get_article_prompt(topic, article_type, keywords)
    content = generate_with_openrouter(prompt)
    
    # Fallback sur template local
    if content is None:
        print("   → Utilisation du template local (mode offline)")
        content = generate_article_local(topic, article_type, keywords)
    else:
        print("   ✓ Contenu généré via OpenRouter")
    
    # Ajouter en-tête
    header = f"""---
title: "{topic}"
type: {article_type}
date: {datetime.now().isoformat()}
keywords: {', '.join(keywords)}
affiliate_links: systeme_io, semrush
---

"""
    
    full_content = header + content
    
    # Sauvegarder
    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(full_content, encoding='utf-8')
    
    print(f"   ✓ Article sauvegardé: {output_file}")
    print(f"   Taille: {len(full_content)} caractères")
    
    return output_file


def main():
    parser = argparse.ArgumentParser(description="Générateur de contenu d'affiliation MVP")
    parser.add_argument("--topic", required=True, help="Sujet de l'article")
    parser.add_argument("--type", choices=["review", "comparison", "tutorial"], 
                       default="review", help="Type d'article")
    parser.add_argument("--output", required=True, help="Fichier de sortie")
    parser.add_argument("--keywords", help="Mots-clés séparés par des virgules")
    
    args = parser.parse_args()
    
    keywords = args.keywords.split(",") if args.keywords else None
    
    generate_article(args.topic, args.type, args.output, keywords)
    print("\n✅ Génération terminée!")


if __name__ == "__main__":
    main()
