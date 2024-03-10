# Desafio Fabrica de Software

# Inicialização e Execução do projeto

* Inicializar o env
    ```
    python -m venv env
    ```
* Entrar no workspace do python
    ```
    .\env\Scripts\activate
    ```

* Instalar as dependências
    ```
    pip install django djangorestframework requests
    ```

* Executar as migrations
    ```
    python manage.py migrate
    ```

* Execute o servidor
    ```
    python manage.py runserver 
    ````
* O servidor foi aberto na porta `8000` utilize a collection disponibilizada para a realização de testes

# API Externa
Para este desafio foi utilizada a api externa [Google Books API](https://developers.google.com/books/docs/overview?hl=pt-br) que permite a realização de pesquisas por nome de livros.