import cohere

co = cohere.ClientV2("7Vrkkt1PwJjspHHmMUc839FxdIwbRAkrifwFxctT")
response = co.chat(
    model="command-r-plus", 
    messages=[{"role": "user", "content": "hello world!"}]
)

print(response.message.content[0].text)
