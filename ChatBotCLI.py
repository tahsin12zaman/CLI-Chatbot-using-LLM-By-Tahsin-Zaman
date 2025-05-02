
from model_loader import model, tokenizer, device
import torch


chat_history = []

print("Bot: Hello! I'm your LLM-powered chatbot. Type 'exit' to quit.\n")

while True:

    user_input = input("User: ")


    if user_input.lower() == "exit":
        print("Bot: Goodbye!")
        break

    # Add the user's message to history
    chat_history.append({"role": "user", "content": user_input})

    prompt_parts = []
    for message in chat_history:
        role = message["role"]
        content = message["content"]
        if role == "user":
            prompt_parts.append(f"User: {content}")
        else:
            prompt_parts.append(f"Bot: {content}")
    prompt_parts.append("Bot: ")
    prompt = "\n".join(prompt_parts)


    inputs = tokenizer(prompt, return_tensors="pt").to(device)

    inputs = {k: v.to(dtype=torch.long) for k, v in inputs.items()}


    outputs = model.generate(
        **inputs,
        max_new_tokens=500,
        do_sample=True,
        top_p=0.95,
        temperature=0.7,
        pad_token_id=tokenizer.eos_token_id
    )


    full_output = tokenizer.decode(outputs[0], skip_special_tokens=True)


    bot_reply = full_output[len(prompt):].strip().split("\n")[0]


    print(f"Bot: {bot_reply}\n")


    chat_history.append({"role": "bot", "content": bot_reply})
