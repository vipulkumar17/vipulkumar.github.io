from flask import Flask, render_template, request, jsonify
from transformers import T5ForConditionalGeneration, T5Tokenizer

app = Flask(__name__)

# Load the T5 model and tokenizer for summarization
model_name = "t5-small"
model = T5ForConditionalGeneration.from_pretrained(model_name)
tokenizer = T5Tokenizer.from_pretrained(model_name)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    # Get the input text from the POST request
    input_text = request.json.get('text')

    # Preprocess the input text
    input_text = "summarize: " + input_text
    inputs = tokenizer(input_text, return_tensors="pt", max_length=512, truncation=True)
    outputs = model.generate(inputs["input_ids"], max_length=150, num_beams=4, early_stopping=True)

    # Decode the output summary
    summary = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # Return the summary in JSON format
    return jsonify({'summary': summary})

if __name__ == '__main__':
    app.run(debug=True)
