# load the large language model file
from llama_cpp import Llama


LLM = Llama(model_path="./llama-2-7b.Q8_0.gguf")

# create a text prompt
prompt = "Q: What are the names of the days of the week? A:"

# generate a response (takes several seconds)
output = LLM(prompt, max_tokens=0)

# display the response
print(output["choices"][0]["text"])
