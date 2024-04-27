from flask import Flask, request, jsonify
from transformers import GPT2LMHeadModel, GPT2Tokenizer, GPT2Config, TextDataset, DataCollatorForLanguageModeling
from transformers import Trainer, TrainingArguments
import pandas as pd

# Inicialização do Flask
app = Flask(__name__)

# Carregar o tokenizador e o modelo uma vez e reutilizá-los
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

# Preparar o dataset para treinamento
def encode(examples):
    return tokenizer(examples["question"] + tokenizer.eos_token, truncation=True, padding='max_length')

class CustomDataset(TextDataset):
    def __init__(self, tokenizer, file_path, block_size):
        super().__init__(
            tokenizer=tokenizer,
            file_path=file_path,
            block_size=block_size,
        )

# Aqui você precisaria salvar seu dataset em um arquivo e passar o caminho para o CustomDataset
# Por simplicidade, vamos assumir que você já fez isso e tem um arquivo chamado 'dataset.txt'

dataset = CustomDataset(
    tokenizer=tokenizer,
    file_path="dataset.txt",
    block_size=128,
)

# Configurar os argumentos de treinamento com um tamanho de lote maior e uma taxa de aprendizado ajustada
training_args = TrainingArguments(
    output_dir="./results",
    num_train_epochs=3,
    per_device_train_batch_size=16, # Aumentar o tamanho do lote para acelerar o treinamento
    learning_rate=5e-5, # Ajustar a taxa de aprendizado conforme necessário
    save_steps=10_000,
    save_total_limit=2,
)

# Configurar o Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    data_collator=DataCollatorForLanguageModeling(
        tokenizer=tokenizer, mlm=False,
    ),
    train_dataset=dataset,
)

# Treinar o modelo
trainer.train()

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    question = data.get('question')
    if not question:
        return jsonify({"error": "No question provided"}), 400
    
    # Tokenizar a pergunta
    inputs = tokenizer.encode(question, return_tensors='pt')
    
    # Gerar a resposta
    outputs = model.generate(inputs, max_length=150, num_return_sequences=1)
    answer = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    return jsonify({"answer": answer})

if __name__ == '__main__':
    app.run(debug=True)
