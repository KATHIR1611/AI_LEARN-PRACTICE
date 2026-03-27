import ollama
import os

input_file = r"D:\Kathirvelan\Projects\AI AGENT\Machines.txt"
output_file = r"D:\Kathirvelan\Projects\AI AGENT\Final.txt"

if not os.path.exists(input_file):
    print(f"Input File {input_file} not exist")
    exit(1)

with open(input_file,"r") as file:
    machines=file.read().strip()

prompt=f"""
You are an assistant who categorizes the fighter jets based on the country of origin

{machines}

Rules:
1. You must clearly verify the country of origin of each jet.
2. Sort based on the year of introduced and attach its one top power for which they have been used.
3. Present the categorized list in a clear and readable manner"""

response=ollama.generate(model="gemma3:4b",prompt=prompt,stream=True)

with open(output_file,"w",encoding="utf-8") as f:
    for chunk in response:
        text=chunk.get("response","")
        print(text,end="",flush=True)
        f.write(text)

