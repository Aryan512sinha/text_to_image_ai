import gradio as gr
from transformers import pipeline  
model = pipeline("your-task", model="your-model-name")

def predict_fn(input_text):
    output = model(input_text)
    return output
gr.Interface(fn=predict_fn, inputs="text", outputs="text").launch()
