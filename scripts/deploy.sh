#!/bin/bash
#
# Script de déploiement automatique sur GitHub Pages
# Usage: ./deploy.sh [nom-du-repo]
#

set -e

# Configuration
REPO_NAME="${1:-marketing-pro-guide}"
GITHUB_USER="${GITHUB_USER:-votre-username}"
SITE_DIR="site"
BRANCH="gh-pages"

# Couleurs
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${GREEN}🚀 Démarrage du déploiement...${NC}"
echo ""

# Vérifier que le dossier site existe
if [ ! -d "$SITE_DIR" ]; then
    echo -e "${RED}❌ Erreur: Dossier $SITE_DIR non trouvé${NC}"
    exit 1
fi

# Vérifier git
if ! command -v git &> /dev/null; then
    echo -e "${RED}❌ Git n'est pas installé${NC}"
    exit 1
fi

echo -e "${YELLOW}📦 Préparation du déploiement...${NC}"

# Créer dossier temporaire
TMP_DIR=$(mktemp -d)
cp -r "$SITE_DIR"/* "$TMP_DIR/"

# Créer fichier CNAME (optionnel - pour domaine custom)
# echo "www.votredomaine.com" > "$TMP_DIR/CNAME"

# Créer .nojekyll pour GitHub Pages
touch "$TMP_DIR/.nojekyll"

echo -e "${YELLOW}📤 Déploiement sur GitHub Pages...${NC}"

# Initialiser repo git temporaire
cd "$TMP_DIR"
git init
git add .
git commit -m "Deploy: $(date '+%Y-%m-%d %H:%M:%S')"

# Pousser vers gh-pages
git push --force "git@github.com:${GITHUB_USER}/${REPO_NAME}.git" main:$BRANCH 2>/dev/null || \
git push --force "https://github.com/${GITHUB_USER}/${REPO_NAME}.git" main:$BRANCH

# Nettoyage
cd -
rm -rf "$TMP_DIR"

echo ""
echo -e "${GREEN}✅ Déploiement réussi !${NC}"
echo ""
echo -e "🌐 Votre site est disponible sur:"
echo -e "   ${YELLOW}https://${GITHUB_USER}.github.io/${REPO_NAME}/${NC}"
echo ""
echo -e "📋 Prochaines étapes:"
echo -e "   1. Vérifier que le repository existe sur GitHub"
echo -e "   2. Activer GitHub Pages dans Settings > Pages"
echo -e "   3. Sélectionner la branche 'gh-pages' comme source"
echo ""
