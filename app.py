import PyPDF2
import os

''' Configuração das pastas'''

INPUT_FOLDER = 'PDFs'
OUTPUT_FOLDER = 'PDFs_merged'
OUTPUT_FILENAME = 'merged.pdf'

''' Criação das pastas se não existirem '''
if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)
    print(f'Pasta {OUTPUT_FOLDER} criada com sucesso!')

merger = PyPDF2.PdfMerger()
pdfs_encontrados = False

print(f'Procurando arquivos PDF na pasta {INPUT_FOLDER}...')

"""Core logic"""

for filename in os.listdir(INPUT_FOLDER):
    if filename.endswith('.pdf'):
        filepath = os.path.join(INPUT_FOLDER, filename)
        
        print(f'Adicionando {filename}...')
        try:
            merger.append(filepath)
            pdfs_encontrados = True
        except PyPDF2.utils.PdfReadError:
            print(f'Erro ao ler o arquivo {filename}. Verifique se ele está corrompido ou protegido por senha.')
        except Exception as e:
            print(f'Ocorreu um erro ao processar o arquivo {filename}: {e}')
            
""" Salvando o PDF mesclado em OUTPUT_FOLDER """

if pdfs_encontrados:
    output_filepath = os.path.join(OUTPUT_FOLDER, OUTPUT_FILENAME)
    try:
        merger.write(output_filepath)
        print(f'PDFs mesclados com sucesso em {output_filepath}!')
    except Exception as e:
        print(f'Ocorreu um erro ao salvar o {OUTPUT_FILENAME} : {e}')
else:
    print(f'Nehum arquivo PDF encontrado na pasta {INPUT_FOLDER}. Verifique se os arquivos estão no formato correto.')
    
merger.close()
