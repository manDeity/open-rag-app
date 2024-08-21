from transformers import AutoModelForCausalLM, AutoTokenizer

# Load the model and tokenizer
model_name = "EleutherAI/gpt-j-6B"  # Hugging Face GPT-J Model
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Function to generate text
def generate_text(prompt):
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**inputs, max_new_tokens=50)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# Example usage
if __name__ == "__main__":
    prompt = "The future of AI is"
    print(generate_text(prompt))
