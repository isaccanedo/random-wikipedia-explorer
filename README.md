# Wiki Buscador de Páginas Aleatórias

Um script Python simples que busca páginas aleatórias da Wikipédia e permite que o usuário selecione uma para abrir em seu navegador padrão.

## Características

- Busca 10 páginas aleatórias da Wikipédia por vez;
- Exibe a lista de páginas aleatórias com títulos e índices;

Permite ao usuário:

- Abrir uma página inserindo seu índice;
- Tentar buscar novas páginas aleatórias novamente;
- Sair do programa;
- Lidar com entradas inválidas graciosamente.

## Requirementos

- Python 3.5 or higher
- Libraries:
  - `requests`
  - `webbrowser`

## Instalação

1. Clone este repositório ou baixe o arquivo de script diretamente;
2. Certifique-se de que o Python esteja instalado no seu sistema;
3. Instale as dependências necessárias usando pip:
   ```bash
   pip install requests
   ```

## Uso

Execute o script no seu terminal:

```bash
python wiki_random.py
```

Siga as instruções na tela:

- Insira o índice da página que você deseja abrir;
- Digite `r` para buscar um novo conjunto de páginas aleatórias;
- Digite `n` para sair do programa.

## Exemplo de saída

```
0: Python (programming language)
1: Artificial intelligence
2: Neural networks
3: Data science
4: Machine learning
5: Robotics
6: Deep learning
7: Open source
8: Cloud computing
9: Quantum computing
10: AI

Digite o índice da página para abrir, 'r' para tentar novamente ou 'n' para sair:
```







