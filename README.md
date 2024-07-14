# Desafio salesrun
## Descrição:
O desafio consiste em criar um portal de controle para desafios, onde administradores podem criar desafios e usuários podem visualizar os desafios atribuidos a eles.

## Tecnologias utilizadas:
- Python
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
- Aceitar e recusar desafios
- Validação de formulários

## Como rodar o projeto:
1. Esteja em uma máquina com linux.
2. Clone o repositório, [documentação para clonar repositório](https://www.cloudbees.com/blog/git-pull-how-it-works-with-detailed-examples).
3. Renomeio o arquivo `.env.example` para `.env` e preencha a variável `DJANGO_SECRET_KEY` com uma secret key do Django.
    - Você pode gerar uma secret key utilizando o a função `get_random_secret_key'` do próprio Django.
4. Crie na raiz do projeto uma pasta chamada média.
5. Se você não tiver o `docker` e o `docker-compose` instalados, instale-os.
6. Abra o terminal na pasta do projeto e execute o comando `docker compose up app`.
7. Acesse o projeto em `http://localhost:8080`.
