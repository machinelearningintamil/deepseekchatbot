import gradio as gr
import subprocess
from langchain_ollama import ChatOllama

# Function to check if model is available and download if necessary
def check_and_download_model(model_name):
    try:
        # Attempt to initialize the model
        model = ChatOllama(model=model_name, base_url="http://localhost:11434/")
        return model
    except Exception:
        return None

# Function to download model
def download_model(model_name):
    subprocess.run(["ollama", "pull", model_name], check=True)
    return f"Model '{model_name}' downloaded successfully."

# Function to initialize model
def initialize_model(model_name):
    model = check_and_download_model(model_name)
    if model is None:
        return "Model not found. Please download it first."
    global chat_model
    chat_model = model
    return "Model initialized successfully."

# Function to generate response
def generate_response(message, history):
    if chat_model is None:
        return "Please initialize the model first."
    # Invoke the model with user input
    response = chat_model.invoke(message)
    # Chunk it up for debugging
    chunk_size = 2000  # or whatever you like
    chunks = [response.content[i:i+chunk_size] for i in range(0, len(response.content), chunk_size)]
    # Return the text content so it shows up in the UI
    # return response.content
    # print(chunks)

    return chunks


# UI Elements
chat_model = None

with gr.Blocks() as demo:
    with gr.Row():
        model_name_box = gr.Textbox(label="Model Name", value="deepseek-r1:1.5b")
        download_button = gr.Button("Download Model")
        initialize_button = gr.Button("Initialize Model")
        status_box = gr.Textbox(label="Status", interactive=False)
    
    download_button.click(download_model, inputs=model_name_box, outputs=status_box)
    initialize_button.click(initialize_model, inputs=model_name_box, outputs=status_box)
    
    chat_interface = gr.ChatInterface(
        fn=generate_response,
        title="🔍 AI Chat Assistant with Ollama & Langchain",
        description=(
            "Ask me anything! Powered by Ollama and Langchain.\n\n"
            "Explore AI-powered conversations with Ollama. "
            "Learn more at [Machinelearning in Tamil](https://www.youtube.com/@mlintamil1992/)"
        ),
        theme="compact"
    )

if __name__ == "__main__":
    demo.launch()
