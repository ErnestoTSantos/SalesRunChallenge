# Desafio salesrun
## Descrição:
O desafio consiste em criar um portal de controle para desafios, onde administradores podem criar desafios e usuários podem visualizar os desafios atribuidos a eles.

## Tecnologias utilizadas:
- Django
- Django Templates
- PostgreSQL
- Docker
- Docker Compose
- HTML
- CSS

## Funcionalidades:
- Autenticação de usuários
- CRUD de desafios
- CRUD de usuários
- Visualização de desafios atribuidos ao usuário
- Validação de formulários
- Aceitar e recusar desafios

## Como rodar o projeto:
1. Esteja em uma máquina com linux.
2. Clone o repositório.
3. Renomeio o arquivo `.env.example` para `.env` e preencha a variável `DJANGO_SECRET_KEY` com uma secret key do Django.
    - Você pode gerar uma secret key utilizando o a função `get_random_secret_key'` do próprio Django.
4. Se você não tiver o `docker` e o `docker-compose` instalados, instale-os.
5. Abra o terminal na pasta do projeto e execute o comando `docker compose up app`.
6. Acesse o projeto em `http://localhost:8080`.
