# Asimov Associates - Sistema de Gestão Jurídica

Sistema web desenvolvido em Python utilizando Dash para gestão de processos jurídicos e advogados.

## 🚀 Funcionalidades

- **Gestão de Processos**: Cadastro e acompanhamento de processos jurídicos
- **Gestão de Advogados**: Controle do quadro de profissionais
- **Interface Responsiva**: Design moderno com Bootstrap
- **Banco de Dados**: Armazenamento em SQLite
- **Dashboard Interativo**: Visualização de dados em tempo real

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **Dash** - Framework web para Python
- **Dash Bootstrap Components** - Componentes UI responsivos
- **Pandas** - Manipulação de dados
- **SQLite** - Banco de dados
- **Plotly** - Gráficos interativos

## 📋 Pré-requisitos

- Python 3.7 ou superior
- pip (gerenciador de pacotes Python)

## 🔧 Instalação

1. **Clone o repositório**
   ```bash
   git clone https://github.com/devjogerio/AsimovAssociates.git
   cd AsimovAssociates
   ```

2. **Crie um ambiente virtual (recomendado)**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # Linux/Mac
   source venv/bin/activate
   ```

3. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Como Executar

1. **Execute o servidor de desenvolvimento**
   ```bash
   python index.py
   ```

2. **Acesse o sistema**
   - Abra seu navegador
   - Vá para: `http://localhost:8050`

## 📁 Estrutura do Projeto

```
AsimovAssociates/
├── app.py                    # Configuração principal do Dash
├── index.py                  # Arquivo principal - ponto de entrada
├── sql_beta.py              # Conexão e operações com banco de dados
├── requirements.txt         # Dependências do projeto
├── Procfile                 # Configuração para deploy (Heroku)
├── sistema.db              # Banco de dados SQLite
├── assets/                 # Arquivos estáticos
│   ├── logo.svg
│   └── styles.css
└── components/             # Componentes da interface
    ├── home.py
    ├── sidebar.py
    ├── modal_advogados.py
    ├── modal_novo_advogado.py
    └── modal_novo_processo.py
```

## 🌐 Deploy

### Heroku

O projeto está configurado para deploy no Heroku:

1. **Crie uma conta no Heroku**
2. **Instale o Heroku CLI**
3. **Execute os comandos:**
   ```bash
   heroku create nome-da-sua-app
   git push heroku main
   ```

### Outras Plataformas

O projeto pode ser facilmente adaptado para outras plataformas como:
- **Railway**
- **Render**
- **PythonAnywhere**
- **Google Cloud Run**

## 🤝 Contribuindo

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 📞 Contato
Link do Projeto: [https://github.com/devjogerio/AsimovAssociates](https://github.com/devjogerio/AsimovAssociates)

## 🎯 Roadmap

- [ ] Implementar autenticação de usuários
- [ ] Adicionar relatórios PDF
- [ ] Integração com APIs de tribunais
- [ ] Sistema de notificações
- [ ] Backup automático de dados
- [ ] Dashboard de analytics avançado

## 🐛 Problemas Conhecidos

- Base de dados é resetada a cada deploy (implementar PostgreSQL para produção)
- Interface necessita de melhorias de UX

## 📊 Status do Projeto

![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)
![Python](https://img.shields.io/badge/python-3.7+-blue)
![Dash](https://img.shields.io/badge/dash-2.5.1-green)