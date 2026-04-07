from InquirerPy import prompt

perguntas = [
    {
        "type": "list",
        "massage": "Qual é a sua linguagem de programação favorita?", 
        "choices": ["Python", "JavaScript", "Java", "C++", "Ruby"]
    }
]

resultado = prompt(perguntas)