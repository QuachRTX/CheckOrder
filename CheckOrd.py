from bs4 import BeautifulSoup
import pandas as pd
import sys
import os

def extrair_produtos_e_codigos(arquivo_html):
    with open(arquivo_html, "r", encoding="utf-8") as file:
        html_content = file.read()
    
    soup = BeautifulSoup(html_content, 'html.parser')
    produtos_e_codigos = []
    
    for link in soup.find_all('a', href=True):
        href = link['href']
        if "/p/" in href and "?" in href:
            path_parts = href.split("/p/")[1].split("?")[0]
            product_name, product_code = path_parts.split("/") if "/" in path_parts else (path_parts, "")
            if product_name and product_code:
                produtos_e_codigos.append((product_name.replace("-", " ").title(), product_code))
    return produtos_e_codigos

def remover_duplicatas_preservando_ordem(lista):
    seen = set()
    seen_add = seen.add
    return [x for x in lista if not (x in seen or seen_add(x))]

def exportar_para_excel(produtos_e_codigos, nome_arquivo):
    df = pd.DataFrame(produtos_e_codigos, columns=['Produto', 'Código'])
    df.to_excel(nome_arquivo, index=False)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Por favor, arraste um arquivo HTML sobre o programa.")
        sys.exit(1)
    
    arquivo_html = sys.argv[1]
    produtos_e_codigos = extrair_produtos_e_codigos(arquivo_html)
    produtos_e_codigos_unicos = remover_duplicatas_preservando_ordem(produtos_e_codigos)
    
    # Caminho da área de trabalho
    desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    nome_arquivo_excel = os.path.join(desktop_path, 'produtos_e_codigos.xlsx')
    
    exportar_para_excel(produtos_e_codigos_unicos, nome_arquivo_excel)
    
    print(f"Arquivo '{nome_arquivo_excel}' criado com sucesso na área de trabalho.")
