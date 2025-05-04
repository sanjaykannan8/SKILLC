from fastapi import FastAPI
import gen 
from fastapi.middleware.cors import CORSMiddleware
from typing import List

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/")
async def say_hello(message: List[str]):
    question = "\n".join(message)
    print(question)
    
    return gen.generate(question)
#     return {"""s = input()
# unique_chars = sorted(list(set(s)), reverse=True)
# print("".join(unique_chars))"""}

    