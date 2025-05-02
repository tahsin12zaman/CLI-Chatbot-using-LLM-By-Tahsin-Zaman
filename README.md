# CLI Chatbot using LLM
_A project by S. M. Tahsin Zaman_

## 📋 Task Description
The objective of this project was to **build a CLI-based chatbot** (no graphical user interface) using a **DeepSeek R1 distilled LLM**.

The chatbot is designed to:
- Use LLM weights from available sources (no official or third-party API).
- Maintain **continuous conversation**, remembering user-provided information across turns.

## ⚙️ Implementation Details

This project was primarily implemented and tested on **Google Colab** with a **T4 GPU**, which provided:
- ✅ Optimal performance
- ✅ Smooth continuous conversation
- ✅ Fast inference within hardware limits

I also tested it on my **local PC (2GB VRAM)** using **PyCharm**, but due to hardware limitations, the chatbot did not perform as efficiently.  
For best results, please refer to and run the code in **Google Colab** (see notebook file).

## ✨ Key Features
- 🖥️ **CLI interface** — Lightweight, runs in terminal
- 🧠 **LLM-backed chatbot** — Maintains conversation memory
- 🔗 **No APIs required** — Uses locally available model weights
- ⚡ **Optimized for limited resources** — Tested in both Colab and low-VRAM PC

## 🛠️ Dependencies
- **Python**
- [Hugging Face Transformers](https://huggingface.co/docs/transformers/index)
- [PyTorch](https://pytorch.org/)
- [Bitsandbytes](https://github.com/TimDettmers/bitsandbytes) (for quantization)
- [Accelerate](https://huggingface.co/docs/accelerate/index) (for device mapping)

## 🚀 Usage
Clone the repository and follow the instructions in the **Colab notebook** or run locally (if sufficient hardware is available).
