
# CheckOrder

Este script Python extrai nomes e códigos de produtos de um arquivo HTML e os exporta para um arquivo Excel. Utiliza `BeautifulSoup` para parsing do HTML e `pandas` para criar e exportar o DataFrame como um arquivo Excel. É uma ferramenta útil para automatizar a extração de informações de produtos de páginas da web.

## Objetivo
Criei este programa para me ajudar a validar a ordenação dos produtos no e-commerce pois antes era necessário uma validação manual, oque resultava em uma perda de tempo desnecessária.

## Como usar

1. Certifique-se de que você tenha Python instalado em sua máquina.
2. Instale as dependências necessárias usando o comando:
   ```
   pip install beautifulsoup4 pandas
   ```
3. Clone este repositório para sua máquina local ou baixe o script.
4. Execute o script da seguinte maneira:
   ```
   python extrator_produtos_codigos.py caminho_para_o_arquivo_html
   ```
   Substitua `caminho_para_o_arquivo_html` pelo caminho do arquivo HTML do qual você deseja extrair os dados.

## Requisitos

- Python 3.x
- BeautifulSoup4
- pandas

## Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
