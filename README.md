💇‍♂️ Agenda Salão — Django + React

Sistema full-stack para gerenciamento de agendamentos em salões de beleza e barbearias. O projeto une o poder do Django REST Framework no backend com a reatividade do React no frontend.

📂 Estrutura do Projeto

agenda_salao/
├── agenda_django/   # Configurações do projeto Django
├── tarefas/         # App Django (Modelos e Lógica de Negócio)
├── frontend/        # Aplicação React (Interface do Usuário)
├── manage.py        # CLI do Django
└── db.sqlite3       # Banco de dados (SQLite)
🛠️ Tecnologias Utilizadas

    Backend: Python 3.x, Django 5.x, Django REST Framework.

    Frontend: React, React Router Dom, Hooks.

    Banco de Dados: SQLite (Desenvolvimento).

🚀 Progresso do Desenvolvimento
⚙️ Backend (Django)

    [x] Configuração inicial do projeto e aplicação tarefas.

    [ ] Modelagem do banco de dados:

        Servico: Nome, duração e preço.

        Cliente: Nome e telefone.

        Agendamento: Relacionamento entre cliente/serviço, data/hora e status.

    [ ] Implementação de Serializers e Views (DRF).

    [ ] Configuração de CORS para integração com React.

💻 Frontend (React)

    [x] Estrutura base da aplicação com create-react-app.

    [x] Sistema de rotas com react-router-dom.

    [ ] Componentes de UI:

        Sidebar: Menu lateral persistente.

        DashboardCard: Cards de métricas rápidas.

        Dashboard: Página principal de visão geral.

    [ ] Integração com API via Axios.

🎨 Próximos Passos

    Visualização de Dados: Implementar gráficos com Recharts ou Chart.js no Dashboard.

    Novas Telas: Desenvolver interfaces para /agendamentos, /servicos e /clientes.

    Conexão API: Criar os endpoints no Django e consumi-los no React.

    Segurança: Implementar sistema de login e autenticação JWT.

🔧 Como Executar

Backend
# Migrar o banco de dados
python manage.py migrate

# Iniciar o servidor (http://127.0.0.1:8000)
python manage.py runserver

Frontend
cd frontend

# Instalar dependências
npm install

# Iniciar o React (http://localhost:3000)
npm start