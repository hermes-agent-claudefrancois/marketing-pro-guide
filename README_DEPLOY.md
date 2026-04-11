# 🚀 GUIDE DE DÉPLOIEMENT RAPIDE

## Étape 1: Créer le compte GitHub (2 min)
1. Aller sur https://github.com/signup
2. Email: `claw98464@gmail.com`
3. Username suggéré: `claw6548`
4. Vérifier l'email

## Étape 2: Créer le repository (1 min)
1. Aller sur https://github.com/new
2. Repository name: `marketing-pro-guide`
3. Description: `Guide des meilleurs outils marketing pour entrepreneurs`
4. Visibility: **Public**
5. ✅ Initialize with README: NON (décocher)
6. Click "Create repository"

## Étape 3: Déployer le site (3 min)

```bash
# Se rendre dans le dossier site
cd /home/ubuntu/.hermes/revenue/mvp_saas_affiliation/site

# Initialiser git
git init
git config user.email "claw98464@gmail.com"
git config user.name "Marketing Pro Guide"

# Ajouter tous les fichiers
git add -A

# Commit
git commit -m "Initial commit: MVP Marketing Pro Guide"

# Créer branche gh-pages
git branch -M gh-pages

# Connecter au remote (remplacer USERNAME si différent)
git remote add origin https://github.com/claw6548/marketing-pro-guide.git

# Push
git push -u origin gh-pages --force
```

## Étape 4: Activer GitHub Pages (2 min)
1. Aller sur: `https://github.com/USERNAME/marketing-pro-guide/settings/pages`
2. Source: **Deploy from a branch**
3. Branch: **gh-pages** / (root)
4. Click "Save"
5. Attendre 2-5 minutes
6. Le site sera accessible sur: `https://USERNAME.github.io/marketing-pro-guide/`

## Étape 5: S'inscrire au programme d'affiliation (5 min)
1. Aller sur: https://systeme.io/affiliate
2. Créer un compte avec: `claw98464@gmail.com`
3. Récupérer son lien d'affiliation personnalisé
4. Remplacer le lien dans les articles si nécessaire

## Étape 6: Google Search Console (5 min)
1. Aller sur: https://search.google.com/search-console
2. Se connecter avec: `claw98464@gmail.com`
3. Ajouter propriété > Préfixe d'URL
4. Entrer: `https://USERNAME.github.io/marketing-pro-guide/`
5. Méthode de vérification: **Fichier HTML**
6. Télécharger le fichier de vérification
7. Le placer dans `/site/` et push
8. Soumettre le sitemap: `/sitemap.xml`

## ✅ VÉRIFICATION

Après déploiement, vérifier:
- [ ] Site accessible: https://USERNAME.github.io/marketing-pro-guide/
- [ ] 5 articles visibles sur la page d'accueil
- [ ] Liens "Essayer Gratuitement" fonctionnels
- [ ] Page disclosure affiliation présente
- [ ] Sitemap accessible: /sitemap.xml

## 🔗 URLS FINALES

| Ressource | URL |
|-----------|-----|
| **Site principal** | https://claw6548.github.io/marketing-pro-guide/ |
| **Article 1** | /articles/systeme-io-avis.html |
| **Article 2** | /articles/systeme-io-vs-clickfunnels.html |
| **Article 3** | /articles/creer-funnel-systeme-io.html |
| **Article 4** | /articles/email-marketing-freelances.html |
| **Article 5** | /articles/landing-page-conversion.html |

## 📞 SUPPORT

En cas de problème:
1. Vérifier que le repo est en mode Public
2. Vérifier que GitHub Pages est activé sur la branche gh-pages
3. Vérifier les logs dans Settings > Pages
