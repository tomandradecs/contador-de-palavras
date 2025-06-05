#Este projeto sera um programa simples em python que conta o numero e palavras em um texto. O usuario podera fornecer o texto diretamente ou indicar um arquivo de texto para leitura.
#É uma otima forma de praticar manipulacao de strings, trabalho com arquivos e estruturas de dados basicas.


#Oque voce vai aprender:
#Manipulacao de strings, funcoes, trabalho com arquivos, entrada e saida de daos, tratamento de erros.

#Funcionalidades: 
#Opcao de entrada, leitura do texto, processamenteo do texto, contagem de palavras, exibicao do resuldado.

def contar_palavras(texto):
    # Remove pontuacao e converte para minusculas
    texto = texto.lower()
    for char in '.,;:!?()[]{}"\'-':
        texto = texto.replace(char, ' ')
    
    # Divide o texto em palavras
    palavras = texto.split()
    
    # Conta as palavras
    contagem = len(palavras)
    
    return contagem
def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
        return conteudo
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' nao foi encontrado.")
        return None
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        return None
def main():
    print("Bem-vindo ao contador de palavras!")
    print("Escolha uma opcao:")
    print("1. Digitar texto diretamente")
    print("2. Ler texto de um arquivo")
    
    opcao = input("Digite 1 ou 2: ")
    
    if opcao == '1':
        texto = input("Digite o texto: ")
    elif opcao == '2':
        nome_arquivo = input("Digite o nome do arquivo (com extensao): ")
        texto = ler_arquivo(nome_arquivo)
        if texto is None:
            return
    else:
        print("Opcao invalida.")
        return
    
    contagem = contar_palavras(texto)
    print(f"O numero de palavras no texto e: {contagem}")
if __name__ == "__main__":
    main()
#Este codigo implementa um contador de palavras que pode ler texto diretamente do usuario ou de um arquivo. Ele remove pontuacao, converte o texto para minusculas e conta o numero de palavras.
#O programa trata erros de leitura de arquivo e exibe o resultado da contagem de palavras.
#O codigo e simples e facil de entender, ideal para iniciantes em Python.
#O codigo pode ser melhorado com funcionalidades adicionais, como contagem de caracteres, frases, ou ate mesmo analise de frequencia de palavras.
#Para melhorar o codigo, voce pode adicionar funcionalidades como:
#1. Contagem de caracteres: Adicionar uma funcao que conte o numero de caracteres no texto.
#2. Contagem de frases: Implementar uma funcao que conte o numero de frases no texto.
#3. Analise de frequencia de palavras: Criar uma funcao que retorne as palavras mais frequentes no texto.
#4. Interface grafica: Utilizar bibliotecas como Tkinter ou PyQt para criar uma interface grafica para o programa.
#5. Suporte a diferentes codificacoes de arquivo: Permitir que o usuario escolha a codificacao do arquivo ao ler.
#6. Exportar resultados: Adicionar a funcionalidade de exportar os resultados da contagem para um arquivo de texto ou CSV.
#7. Testes automatizados: Implementar testes unitarios para garantir que as funcoes funcionem corretamente.
#8. Documentacao: Adicionar docstrings e comentarios para melhorar a compreensao do codigo.
#9. Tratamento de erros: Melhorar o tratamento de erros para lidar com diferentes tipos de excecoes.
#10. Suporte a diferentes idiomas: Implementar suporte para contagem de palavras em diferentes idiomas, considerando regras gramaticais especificas.
#11. Contagem de palavras especificas: Adicionar uma funcionalidade que permita ao usuario contar a frequencia de palavras especificas no texto.
#12. Interface de linha de comando: Melhorar a interface de linha de comando para aceitar argumentos e opcoes adicionais.
#13. Analisar texto em tempo real: Implementar uma funcionalidade que analise o texto enquanto o usuario digita, atualizando a contagem de palavras em tempo real.
#14. Suporte a arquivos grandes: Otimizar a leitura de arquivos grandes, lendo em blocos em vez de carregar tudo na memoria de uma vez.
#15. Contagem de palavras compostas: Implementar uma funcionalidade que conte palavras compostas como uma unica palavra.
#16. Estatisticas adicionais: Adicionar estatisticas como comprimento medio das palavras, numero de palavras unicas, etc.
#17. Interface web: Criar uma interface web simples usando Flask ou Django para permitir que os usuarios interajam com o contador de palavras via navegador.
#18. Suporte a diferentes formatos de arquivo: Permitir que o usuario leia textos de diferentes formatos, como PDF ou DOCX, usando bibliotecas apropriadas.
#19. Personalizacao: Permitir que o usuario personalize a forma como as palavras sao contadas, como ignorar palavras comuns (stop words).
#20. Exportar resultados em diferentes formatos: Adicionar a funcionalidade de exportar os resultados da contagem em formatos como JSON ou XML.
#21. Contagem de palavras por categoria: Implementar uma funcionalidade que categorize as palavras e conte quantas pertencem a cada categoria (substantivos, verbos, adjetivos, etc.).
#22. Suporte a idiomas diferentes: Implementar suporte para contagem de palavras em diferentes idiomas, considerando regras gramaticais especificas.
#23. Analisar a complexidade do texto: Adicionar uma funcionalidade que analise a complexidade do texto, como o indice de legibilidade.
#24. Contagem de palavras em tempo real: Implementar uma funcionalidade que conte as palavras enquanto o usuario digita, atualizando a contagem em tempo real.
#25. Suporte a diferentes codificacoes de texto: Permitir que o usuario escolha a codificacao do texto ao ler de um arquivo.
#26. Contagem de palavras por paragrafo: Implementar uma funcionalidade que conte o numero de palavras em cada paragrafo do texto.
#27. Analisar a estrutura do texto: Adicionar uma funcionalidade que analise a estrutura do texto, como o numero de paragrafos, frases e palavras.
#28. Suporte a diferentes idiomas: Implementar suporte para contagem de palavras em diferentes idiomas, considerando regras gramaticais especificas.
#29. Interface grafica: Criar uma interface grafica simples usando Tkinter ou PyQt para permitir que os usuarios interajam com o contador de palavras de forma mais intuitiva.
#30. Exportar resultados em diferentes formatos: Adicionar a funcionalidade de exportar os resultados da contagem em formatos como CSV, JSON ou XML.
