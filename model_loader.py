
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Use the 7B distilled model
model_name = "deepseek-ai/DeepSeek-R1-Distill-7B"
tokenizer = AutoTokenizer.from_pretrained(model_name)


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float16,
    device_map="auto"
)


if hasattr(torch, 'compile'):
    model = torch.compile(model)


model.to(device)
