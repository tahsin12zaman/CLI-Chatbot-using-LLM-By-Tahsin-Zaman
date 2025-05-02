CLI Chatbot using LLM
A project by S. M. Tahsin Zaman (Ztrios)

Task Description
The objective of this project was to build a CLI-based chatbot (no graphical user interface) using a DeepSeek R1 distilled LLM. The chatbot is designed to:

Use LLM weights from available sources (without relying on any official or third-party API).

Maintain continuous conversation, allowing it to remember user-provided information across turns.

Implementation Details
This project was primarily implemented and tested on Google Colab with a T4 GPU. Running the model in Colab provided:

Optimal performance

Smooth continuous conversation

Fast inference within the available hardware limits

Additionally, I attempted to run the same code on my local PC (2GB VRAM) using PyCharm. However, due to hardware limitations, the chatbot did not perform as efficiently in terms of speed and conversational consistency.

For reference and to experience the optimal implementation, please review and run the code in Google Colab (provided in the notebook file).

Key Features
CLI interface — lightweight and simple to run in terminal/console

LLM-backed chatbot with conversation memory

Runs without APIs — using locally available model weights

Tested and optimized in resource-constrained environments

Dependencies
Python

Hugging Face Transformers (for model handling)

PyTorch (for backend inference)

Bitsandbytes (for quantization)

Accelerate (for device mapping and optimized loading)

Usage
Clone the repository and follow the instructions in the Colab notebook or run locally (if sufficient hardware is available).
