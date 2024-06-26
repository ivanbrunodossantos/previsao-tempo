# Previsão do Tempo

Este é um projeto simples de previsão do tempo em Python, que utiliza a API gratuita do OpenWeatherMap para obter dados de previsão do tempo para uma determinada cidade.

## Instalação

1. Clone o repositório:
git clone https://github.com/ivanbrunodossantos/previsao-tempo.git


2. Instale as dependências:
pip install -r requirements.txt


3. Crie um arquivo `.env` na raiz do projeto e adicione sua chave de API do OpenWeatherMap:
API_KEY=SuaChaveDeAPIAqui


## Como Usar

1. Execute o arquivo `main.py`:
python main.py


## Como Obter uma Chave de API do OpenWeatherMap

Para obter uma chave de API do OpenWeatherMap, siga estas etapas:

1. **Crie uma conta no OpenWeatherMap**:
- Acesse o site do [OpenWeatherMap](https://home.openweathermap.org/users/sign_up) e crie uma conta gratuita.

2. **Confirme o seu e-mail**:
- Após criar a conta, verifique seu e-mail e siga as instruções para confirmar sua conta.

3. **Faça login na sua conta**:
- Acesse o [OpenWeatherMap](https://home.openweathermap.org/users/sign_in) com suas credenciais.

4. **Acesse a página da API**:
- Depois de fazer login, vá para a [página da API](https://home.openweathermap.org/api_keys).

5. **Obtenha sua chave de API**:
- Na página da API, você encontrará sua chave de API única. Ela será necessária para fazer solicitações à API do OpenWeatherMap.

6. **Copie sua chave de API**:
- Copie sua chave de API para que você possa usá-la em seu projeto. Geralmente, ela se parece com uma sequência alfanumérica, como `abcdef1234567890`.

7. **Use sua chave de API em seu projeto**:
- Cole sua chave de API em seu arquivo `.env` (ou `.env.example`) como `API_KEY=SuaChaveDeAPIAqui`.