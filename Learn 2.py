import ollama

#For direct chat using chat
'''res=ollama.chat(
    model="gemma3:4b",
    messages=[{"role":"user","content":"The top 5 oldest languages in world"}],
    stream=True
)
for chunk in res:
    print(chunk["message"]["content"],end="",flush=True)'''


#For creating another bot and using generate
'''ollama.create(model="Quickie",from_="llama3:8b",parameters={"temperature":0.4},system="You are Quickie who responds immediately and accurately")

response=ollama.generate(
    model="Quickie",prompt="In short way explain the difference between LangChain and LangGraph ",stream=True
)

for chunks in response:
    print(chunks.get("response",""),end="",flush=True)'''

