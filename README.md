# Repositório Auxiliar para Download da Base de Dados do Spotify

Este repositório contém um script em Python para baixar e limpar a base de dados
de músicas do Spotify a partir da API do Kaggle. Este repositório não faz parte
da entrega final do trabalho prático de AEDs3, mas serve como uma ferramenta
auxiliar para facilitar a obtenção e o pré-processamento dos dados brutos.

## Papel no Projeto Mais Amplo

No projeto principal, implementado em Java com Maven, trabalhamos com uma base
de dados contendo aproximadamente 900 mil registros de músicas do Spotify. Este
repositório auxilia ao fornecer um meio automatizado de baixar essa base de
dados diretamente do Kaggle, garantindo que os dados utilizados estejam sempre
atualizados e consistentes.

## Pré-requisitos

Antes de começar, certifique-se de ter o seguinte:

- Python 3 (testado com Python 3.13.1)
- Módulo `venv` (geralmente incluído na instalação do Python)
- Conta registrada no [Kaggle](https://kaggle.com)

## Configuração da API do Kaggle

1. Faça login na sua conta do Kaggle.
2. Acesse a aba _“Account”_ na sua
   [página de perfil](https://www.kaggle.com/settings/account) e clique em
   _“Create New API Token”_. Um arquivo chamado `kaggle.json` será baixado.
3. Coloque o arquivo `kaggle.json` na pasta `.kaggle` no diretório _home_ do seu
   usuário:

   - **Linux/macOS/BSD/Unix**:

     ```sh
     mkdir -p ~/.kaggle
     mv /path/to/kaggle.json ~/.kaggle/
     chmod 600 ~/.kaggle/kaggle.json
     ```

   - **Windows**:
     ```cmd
     mkdir %USERPROFILE%\.kaggle
     move \path\to\kaggle.json %USERPROFILE%\.kaggle\
     ```

## Configuração do Ambiente

1. Clone este repositório:

   ```sh
   git clone https://github.com/lucca-pellegrini/aeds3-dataset.git
   cd aeds3-dataset
   ```

2. Crie um ambiente virtual:

   ```sh
   python -m venv venv
   ```

3. Ative o ambiente virtual:

   - **Linux/macOS/BSD/Unix**:

     ```sh
     source venv/bin/activate
     ```

   - **Windows**:
     ```cmd
     .\venv\Scripts\activate
     ```

4. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```

## Execução do Script

Para executar o script, baixando e limpando a base de dados, utilize o seguinte
comando:

```sh
python dataset.py
```

## Estrutura do Repositório

- `dataset.py`: script principal para baixar a base de dados do Spotify a partir
  da API do Kaggle.
- `requirements.txt`: arquivo de dependências do Python.

## Notas Adicionais

- Certifique-se de que o arquivo `kaggle.json` está corretamente configurado,
  pois ele é necessário para autenticar sua conta do Kaggle.
- Não compartilhe esse arquivo com ninguém, pois ele pode conceder acesso
  irrestrito à sua conta no Kaggle.
- O script `dataset.py` está configurado para baixar a base de dados para o
  diretório atual. Modifique o script conforme necessário para atender às suas
  necessidades específicas.

## Licença

Este projeto está licenciado sob a [ISC License](LICENSE).
