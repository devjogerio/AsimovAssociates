# Configuração do Repositório GitHub

## 📋 Checklist de Configuração

### 1. Criar Repositório no GitHub
- [ ] Acesse [GitHub](https://github.com)
- [ ] Clique em "New Repository"
- [ ] Nome: `AsimovAssociates`
- [ ] Descrição: "Sistema de Gestão Jurídica desenvolvido em Python com Dash"
- [ ] Marque como "Public" ou "Private"
- [ ] **NÃO** marque "Initialize with README" (já temos um)

### 2. Conectar Repositório Local

```bash
# Inicializar repositório Git
git init

# Adicionar arquivos
git add .

# Primeiro commit
git commit -m "Initial commit: Sistema de gestão jurídica"

# Conectar com repositório remoto
git branch -M main
git remote add origin https://github.com/SEU-USUARIO/AsimovAssociates.git

# Enviar código
git push -u origin main
```

### 3. Configurar Secrets para Deploy

#### Para Heroku:
1. Vá em: **Settings** → **Secrets and variables** → **Actions**
2. Adicione os seguintes secrets:
   - `HEROKU_API_KEY`: Sua chave de API do Heroku
   - `HEROKU_APP_NAME`: Nome da sua app no Heroku
   - `HEROKU_EMAIL`: Seu email do Heroku

#### Para Railway:
1. Vá em: **Settings** → **Secrets and variables** → **Actions**
2. Adicione os seguintes secrets:
   - `RAILWAY_TOKEN`: Token da Railway
   - `RAILWAY_SERVICE_ID`: ID do serviço Railway

### 4. Configurar Deploy Automático

Os workflows já estão configurados em `.github/workflows/`:
- `deploy.yml`: Deploy para Heroku
- `railway.yml`: Deploy para Railway

### 5. Proteger Branch Principal

1. Vá em: **Settings** → **Branches**
2. Clique em "Add rule"
3. Configure:
   - Branch name pattern: `main`
   - ✅ Require pull request reviews before merging
   - ✅ Require status checks to pass before merging
   - ✅ Require branches to be up to date before merging

### 6. Configurar Issues Template

Crie `.github/ISSUE_TEMPLATE/bug_report.md` e `feature_request.md` para padronizar issues.

### 7. Adicionar Badge de Status

Adicione ao README.md:
```markdown
![Build Status](https://github.com/SEU-USUARIO/AsimovAssociates/workflows/Deploy%20to%20Heroku/badge.svg)
```

## 🔧 Comandos Git Úteis

```bash
# Ver status dos arquivos
git status

# Adicionar arquivos específicos
git add arquivo.py

# Commit com mensagem
git commit -m "Descrição da alteração"

# Enviar alterações
git push

# Criar nova branch
git checkout -b nova-feature

# Voltar para main
git checkout main

# Merge de branch
git merge nova-feature

# Ver histórico
git log --oneline
```

## 🚀 Deploy Manual

### Heroku
```bash
# Instalar Heroku CLI
# https://devcenter.heroku.com/articles/heroku-cli

# Login
heroku login

# Criar app
heroku create nome-da-app

# Deploy
git push heroku main

# Ver logs
heroku logs --tail
```

### Railway
```bash
# Instalar Railway CLI
npm install -g @railway/cli

# Login
railway login

# Deploy
railway up
```

## 📝 Próximos Passos

1. Configure o deploy em uma das plataformas
2. Teste a aplicação em produção
3. Configure monitoramento de erros
4. Implemente backup do banco de dados
5. Configure domínio personalizado