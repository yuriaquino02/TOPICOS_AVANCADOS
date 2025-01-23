import whisper                                       
from langchain import PromptTemplate                 
from langchain_ollama.llms import OllamaLLM         

#definindo a utilização do modelo "small" do whisper
model = whisper.load_model("small")          

#retorna um dicionário resultado da transcrição do áudio
result = model.transcribe("Gravacao.mp3")       

#converte o dicionário em string e exibe o resultado
transcription = result['text']             
print("\n","TEXTO TRANSCRITO", transcription)   

# Define o modelo do Ollama para interpretação da transcrição
model_ollama = OllamaLLM(model="llama3.2:1b")

#Instruções que será enviada para o modelo 
template = """

Resuma e diga os principais pontos-chave do seguinte texto em português:
Texto: {texto}
Resumo: 

"""

# Cria um prompt formatado com o texto transcrito
prompt = PromptTemplate(input_variables=["texto"], template = template) 
prompt_text = prompt.format(texto = transcription)
print(prompt_text)

# Obtém o resumo do texto utilizando o modelo Ollama e exibe o resultado
resumo = model_ollama.invoke(prompt_text)
print("RESUMO DO TEXTO TRANSCRITO", resumo)