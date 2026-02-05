# Agenda Salão - Django + React

Este projeto é um sistema de agendamento para salões de beleza/barbearias, utilizando **Django** no backend e **React** no frontend.

---

## 📂 Estrutura do Projeto

agenda_salao/ 
│── agenda_django/   # Configurações principais do Django 
│── tarefas/         # App Django para agendamentos, serviços e clientes 
│── frontend/        # Aplicação React (interface do usuário) 
│── manage.py        # Gerenciador do Django 
│── db.sqlite3       # Banco de dados SQLite


---

## 🚀 Passos realizados

### 1. Backend (Django)
- Criação do projeto Django:
  ```bash
  django-admin startproject agenda_django .
  python manage.py startapp tarefas