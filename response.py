
def getResponse(text):
    prompt = text+'in brief'
    response = requests.post('ngrok-url/generate', data={"prompt": prompt})

    if response.status_code == 200:
        answer=shortAnswer(response.text)
        return answer
    else:
        return (f"some Error: {response.status_code}")

def shortAnswer(ans):
    text=ans
    pattern = r'\[/INST\](.*?)(?=\d+\s*\[INST\]|$)'
    matches = re.findall(pattern, text, re.DOTALL)
    
    for match in matches:
        answer = match.strip()
        sentences = re.split(r'(?<=[.?!])\s+', answer)
        # sentences = re.split(r'(?<=\[.?!\])\s+|^\d+\.\s*', answer)
        shortened_answer = ' '.join(sentences[:5]) 
        return shortened_answer



ques='are fairies real'
getResponse(ques)


