import gradio as gr
from dotenv import load_dotenv
from research_manager import ResearchManager
import os
from openai import AsyncOpenAI
from agents import set_default_openai_client, set_default_openai_api

load_dotenv(override=True)

# Get OpenRouter configuration from environment variables
base_url = os.getenv('OPENROUTER_BASE_URL')
api_key = os.getenv('OPENROUTER_API_KEY')

# Create AsyncOpenAI client with OpenRouter configuration
custom_client = AsyncOpenAI(
    base_url=base_url,
    api_key=api_key
)

set_default_openai_client(custom_client)

# Use Chat Completions API (recommended for OpenRouter)
set_default_openai_api("chat_completions")

async def run(query: str):
    async for chunk in ResearchManager().run(query):
        yield chunk


with gr.Blocks(theme=gr.themes.Default(primary_hue="sky")) as ui:
    gr.Markdown("# Deep Research")
    query_textbox = gr.Textbox(label="What topic would you like to research?")
    run_button = gr.Button("Run", variant="primary")
    report = gr.Markdown(label="Report")
    
    run_button.click(fn=run, inputs=query_textbox, outputs=report)
    query_textbox.submit(fn=run, inputs=query_textbox, outputs=report)

ui.launch(inbrowser=True)

