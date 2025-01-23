# Transcrição e Sumarização de Áudio

Este projeto utiliza as bibliotecas `whisper` e `langchain` para transcrever áudios e gerar um resumo dos pontos-chave do texto transcrito.

## Funcionalidades

1. **Transcrição de Áudio**:

   - Utiliza o modelo Whisper para converter arquivos de áudio (formato `.mp3`) em texto.

2. **Geração de Resumo**:

   - Usa o modelo Ollama (especificamente `llama3.2:1b`) para resumir o texto transcrito e destacar os principais pontos-chave.

## Requisitos

Antes de executar o código, certifique-se de ter instalado as dependências necessárias.

### Dependências

- Python 3.8 ou superior
- Bibliotecas Python:
  - `openai-whisper`
  - `langchain`
  - `langchain_ollama`
- FFmpeg (necessário para o funcionamento do Whisper)

#### Instalação do FFmpeg

Siga as instruções abaixo para instalar o FFmpeg em seu sistema:

- **No Windows**:
  1. Baixe o FFmpeg no site oficial: [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html).
  2. Extraia o conteúdo do arquivo baixado.
  3. Adicione o diretório `bin` do FFmpeg ao PATH do sistema.

- **No macOS**:
  Execute o comando:
  ```bash
  brew install ffmpeg
  ```

- **No Linux**:
  Execute o comando:
  ```bash
  sudo apt update && sudo apt install ffmpeg
  ```

Para verificar se o FFmpeg foi instalado corretamente, execute:
```bash
ffmpeg -version
```

### Instalação das Dependências Python

Para instalar as dependências Python, execute:
```bash
pip install openai-whisper langchain langchain_ollama
```

## Como Usar

1. **Prepare o arquivo de áudio**:

   - Coloque o arquivo de áudio que você deseja transcrever no mesmo diretório do código e nomeie-o como `Gravacao.mp3`.

2. **Execute o código**:

   - Rode o script Python:

   ```bash
   python transcricao_resumo.py
   ```

3. **Saída esperada**:

   - O texto transcrito do áudio será exibido no console.
   - O resumo gerado com os principais pontos-chave será mostrado na sequência.

## Estrutura do Projeto

- `transcricao_resumo.py`: Script principal que realiza a transcrição e sumarização.
- `Gravacao.mp3`: Arquivo de áudio de exemplo (deve ser fornecido pelo usuário).

## Exemplos de Aplicação

Este projeto pode ser aplicado em diversas áreas, incluindo:

1. **Transcrição de Reuniões Corporativas**:
   - Empresas podem utilizar o projeto para transcrever reuniões, gerando registros e resumos de forma automatizada.

2. **Jornalismo e Entrevistas**:
   - Jornalistas podem gravar entrevistas e transformar o áudio em texto, com resumos prontos para edição e publicação.

3. **Educação e Palestras**:
   - Alunos e professores podem transcrever palestras ou aulas gravadas, facilitando o estudo e o compartilhamento de conhecimento.

4. **Acessibilidade**:
   - Pessoas com deficiência auditiva podem usar o sistema para transcrever áudios de vídeos, podcasts ou conversas.

5. **Atendimento ao Cliente**:
   - Call centers podem transcrever e resumir chamadas para análises de qualidade ou geração de insights.

6. **Produção de Conteúdo Multimídia**:
   - Criadores de conteúdo podem transcrever podcasts ou vídeos para criar legendas, artigos ou resumos.

7. **Análise Jurídica**:
   - Escritórios de advocacia podem transcrever depoimentos ou gravações de audiências, extraindo os pontos mais relevantes.

8. **Pesquisa de Mercado**:
   - Empresas podem transcrever grupos focais ou entrevistas com consumidores, gerando insights dos principais temas discutidos.


## Observações

- Certifique-se de que o arquivo de áudio esteja em um formato suportado pelo Whisper.
- Ajuste o modelo Ollama e o template de prompt para atender às suas necessidades específicas.

