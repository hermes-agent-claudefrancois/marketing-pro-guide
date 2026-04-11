#!/bin/bash

# Script de déploiement sur GitHub Pages
# Usage: ./deploy.sh [github_username] [repo_name]

set -e

# Configuration
GITHUB_USERNAME="${1:-claw6548}"
REPO_NAME="${2:-marketing-pro-guide}"
EMAIL="claw98464@gmail.com"
SITE_DIR="site"
DEPLOY_BRANCH="gh-pages"

echo "🚀 Déploiement GitHub Pages"
echo "============================"
echo "GitHub Username: $GITHUB_USERNAME"
echo "Repository: $REPO_NAME"
echo "Email: $EMAIL"
echo ""

# Vérifier que le dossier site existe
if [ ! -d "$SITE_DIR" ]; then
    echo "❌ Erreur: Dossier '$SITE_DIR' non trouvé"
    exit 1
fi

# Aller dans le dossier site
cd "$SITE_DIR"

# Initialiser git si nécessaire
if [ ! -d ".git" ]; then
    echo "📦 Initialisation du repository git..."
    git init
    git config user.email "$EMAIL"
    git config user.name "Marketing Pro Guide"
fi

# Créer la branche gh-pages si elle n'existe pas
if ! git show-ref --verify --quiet refs/heads/$DEPLOY_BRANCH; then
    echo "🌿 Création de la branche $DEPLOY_BRANCH..."
    git checkout -b $DEPLOY_BRANCH
else
    git checkout $DEPLOY_BRANCH
fi

# Ajouter le remote GitHub (ignorer l'erreur si déjà configuré)
echo "🔗 Configuration du remote GitHub..."
git remote remove origin 2>/dev/null || true
git remote add origin "https://github.com/$GITHUB_USERNAME/$REPO_NAME.git" 2>/dev/null || true

# Ajouter tous les fichiers
echo "📁 Ajout des fichiers..."
git add -A

# Commit
if git diff --cached --quiet; then
    echo "ℹ️ Aucun changement à committer"
else
    echo "💾 Commit des changements..."
    git commit -m "Deploy: $(date '+%Y-%m-%d %H:%M:%S')"
fi

# Instructions de déploiement
echo ""
echo "✅ Prêt pour le déploiement!"
echo ""
echo "📋 Prochaines étapes manuelles:"
echo ""
echo "1. Créer le repository sur GitHub:"
echo "   https://github.com/new"
echo "   Nom: $REPO_NAME"
echo "   Visibility: Public"
echo ""
echo "2. Pousser le code:"
echo "   cd $SITE_DIR"
echo "   git push -u origin $DEPLOY_BRANCH --force"
echo ""
echo "3. Activer GitHub Pages:"
echo "   - Aller sur https://github.com/$GITHUB_USERNAME/$REPO_NAME/settings/pages"
echo "   - Source: Deploy from a branch"
echo "   - Branch: $DEPLOY_BRANCH / (root)"
echo "   - Save"
echo ""
echo "4. Votre site sera accessible sur:"
echo "   https://$GITHUB_USERNAME.github.io/$REPO_NAME/"
echo ""
echo "📝 Configuration initiale (une seule fois):"
echo "   git config --global user.email \"$EMAIL\""
echo "   git config --global user.name \"Marketing Pro Guide\""
echo ""
