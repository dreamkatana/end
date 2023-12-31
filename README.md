# Loja REST API

Este projeto é uma aplicação Flask que expõe uma API REST para operações em "Lojas" e "Itens". Cada "Loja" pode ter vários "Itens".

## Instalação

### Requisitos
- Python 3.7+
- Flask 1.1.2+
- Flask-Smorest 0.31.0+
- SQLAlchemy 1.3.23+

### Instruções

1. Clone o repositório para sua máquina local usando `[https://github.com/dreamkatana/end/yourrepository.git](https://github.com/dreamkatana/end.git)`.

2. Navegue até o diretório do projeto: `cd yourrepository`

3. Crie um ambiente virtual Python: `python3 -m venv venv`

4. Ative o ambiente virtual: 
    - Linux/macOS: `source venv/bin/activate`
    - Windows: `venv\Scripts\activate`

5. Instale as dependências: `pip install -r requirements.txt`

## Utilização

1. Para iniciar o servidor, execute: `flask run`

2. A API estará disponível em `http://localhost:5000`.

3. Você pode interagir com a API usando uma ferramenta como cURL, Postman ou um navegador web.

## Endpoints

- `POST /loja` : Cria uma nova loja.
    - Exemplo de corpo da requisição: `{ "name": "Loja1" }`
    
- `GET /loja/<name>` : Retorna os detalhes de uma loja específica.
    
- `POST /item` : Cria um novo item em uma loja.
    - Exemplo de corpo da requisição: `{ "name": "Item1", "price": 19.99, "store_id": 1 }`
    
- `GET /item/<id>` : Retorna os detalhes de um item específico.

## Contribuição

Contribuições são sempre bem-vindas! Por favor, veja o arquivo `CONTRIBUTING.md` para mais detalhes.

## Suporte

Se você encontrar um bug ou tiver alguma sugestão, por favor, abra uma issue no GitHub.

## Licença

Este projeto é licenciado sob a licença MIT. Veja o arquivo `LICENSE.md` para mais detalhes.
