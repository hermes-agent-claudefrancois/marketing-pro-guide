# 🚀 MVP Affiliation SaaS - Systeme.io

Projet de génération de revenus par affiliation marketing, ciblant les freelances et entrepreneurs francophones avec Systeme.io comme produit phare.

## 📁 Structure du Projet

```
.
├── content/                    # Articles en Markdown
│   ├── 01-systeme-io-avis.md
│   ├── 02-systeme-io-vs-clickfunnels.md
│   └── 03-creer-funnel-systeme-io.md
├── site/                       # Site web statique
│   ├── index.html             # Page d'accueil
│   └── articles/              # Articles HTML
├── scripts/                    # Outils d'automatisation
│   ├── content_generator.py   # Générateur d'articles
│   └── convert_to_html.py     # Convertisseur MD→HTML
├── PLAN_REVENUS.md            # Plan de revenus détaillé
└── README.md                  # Ce fichier
```

## 🎯 Objectif

Générer **20€/mois** de revenus passifs en 30 jours via l'affiliation Systeme.io (60% commission à vie).

## 🚀 Démarrage Rapide

### 1. Générer un nouvel article

```bash
cd /home/ubuntu/.hermes/revenue/mvp_saas_affiliation

# Avis/Review
python3 scripts/content_generator.py \
  --topic "Systeme.io Avis" \
  --type review \
  --output content/mon-article.md \
  --keywords "systeme.io,avis,test"

# Comparatif
python3 scripts/content_generator.py \
  --topic "Systeme.io vs Kartra" \
  --type comparison \
  --output content/comparatif.md

# Tutoriel
python3 scripts/content_generator.py \
  --topic "Créer une landing page" \
  --type tutorial \
  --output content/tutoriel.md
```

### 2. Convertir en HTML

```bash
python3 scripts/convert_to_html.py \
  --input content/mon-article.md \
  --output site/articles/mon-article.html
```

### 3. Déployer

Le site est statique (HTML/CSS) et peut être déployé sur :
- **GitHub Pages** (gratuit, recommandé)
- **Netlify** (gratuit)
- **Vercel** (gratuit)

## 💰 Programme d'Affiliation

### Systeme.io (Recommandé)
- **Commission** : 60% à vie
- **Cookie** : Lifetime (last-cookie)
- **URL** : https://systeme.io/affiliate
- **Lien affilié** : `https://systeme.io/?sa=sa0268466764645998886fff8b439ed15072d58eb1`

### Alternatives
- **Semrush** : 40% récurrent
- **GetResponse** : 33% récurrent ou 100$ CPA
- **Hostinger** : Commissions variables

## 📝 Stratégie de Contenu

### Types d'Articles

1. **Review/Avis** (SEO: "[produit] avis 2025")
   - Test approfondi
   - Avantages/inconvénients
   - Verdict avec CTA

2. **Comparatif** (SEO: "[produit] vs [concurrent]")
   - Tableau comparatif
   - Recommandation par profil
   - Lien affilié gagnant

3. **Tutoriel** (SEO: "comment [faire quelque chose]")
   - Guide étape par étape
   - Outil recommandé = produit affilié
   - Résultat rapide

### Calendrier Éditorial

| Semaine | Articles | Focus |
|---------|----------|-------|
| 1 | 3 | Review + Comparatif + Tutoriel |
| 2 | 2 | Expansion longue traîne |
| 3 | 2 | Optimisation existant |
| 4 | 3 | Scaling contenu |

## 🔧 Personnalisation

### Modifier les liens d'affiliation

Éditer `scripts/content_generator.py` :
```python
AFFILIATE_LINKS = {
    "systeme_io": "VOTRE_LIEN_ICI",
    "semrush": "VOTRE_LIEN_ICI",
    # ...
}
```

### Utiliser OpenRouter (optionnel)

Pour générer du contenu avec IA (gratuit) :
```bash
export OPENROUTER_API_KEY="votre_clé_api"
python3 scripts/content_generator.py --topic "..." --output "..."
```

Modèles gratuits disponibles :
- `qwen/qwen3-coder:free`
- `google/gemma-4-31b-it:free`

## 📊 Suivi des Performances

### Métriques à suivre

- **Visites organiques** (Google Search Console)
- **Clics liens affiliation** (bitly ou plugin)
- **Inscriptions** (dashboard affilié)
- **Conversions payantes** (dashboard affilié)
- **Revenus générés** (dashboard affilié)

### Outils recommandés

- **Google Analytics 4** : Trafic gratuit
- **Google Search Console** : SEO
- **Bitly** : Tracking liens (gratuit)

## 🎣 Stratégie Promotion

### SEO (Long terme)
- Mots-clés longue traîne
- Contenu de qualité
- Netlinking naturel

### Promotion directe (Court terme)
- Commentaires blogs marketing
- Reddit r/entrepreneur, r/freelance
- Groupes Facebook entrepreneurs
- Twitter/X #MarketingDigital

## 💡 Tips Conversion

1. **CTA clairs** : "Essayer gratuitement" > "S'inscrire"
2. **Social proof** : Stats, témoignages
3. **Urgence** : "Offre limitée", "Prix va augmenter"
4. **Guarantee** : Mentionner garantie 30j
5. **Scarcity** : "Derniers jours du plan gratuit"

## 📅 Roadmap

### Semaine 1 - Setup
- [x] Créer structure projet
- [x] Générer 3 articles
- [ ] Déployer sur GitHub Pages
- [ ] Inscription programme affiliation

### Semaine 2 - Contenu
- [ ] 5 articles supplémentaires
- [ ] Optimisation SEO on-page
- [ ] Backlinks initiaux

### Semaine 3 - Optimisation
- [ ] Analytics setup
- [ ] A/B test titres
- [ ] Amélioration conversions

### Semaine 4 - Scaling
- [ ] 10+ articles
- [ ] Automatisation
- [ ] Newsletter setup

## ⚠️ Legal

### Disclosure obligatoire
Inclure sur chaque page :
```
Ce site contient des liens d'affiliation. Si vous effectuez un achat 
via nos liens, nous recevons une commission sans surcoût pour vous.
```

### RGPD
- Banner cookies (si tracking)
- Mention légale
- Politique confidentialité

## 🤝 Contribution

Pour ajouter des fonctionnalités :
1. Fork le repo
2. Créer une branche
3. Commiter les changements
4. Ouvrir une PR

## 📞 Support

En cas de problème :
1. Vérifier les logs scripts
2. Consulter la documentation OpenRouter
3. Ouvrir une issue

---

**Objectif** : 20€/mois en 30 jours  
**Investissement** : 0€ (temps uniquement)  
**ROI attendu** : ∞ (pas d'investissement initial)

*Projet Hermes Agent - Équipe BETA Revenue*
