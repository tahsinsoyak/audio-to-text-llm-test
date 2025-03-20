import os
from groq import Groq
from portkey_ai import Portkey
from dotenv import load_dotenv

# Read the text from a .txt file
txt_file_path = "text.txt"
with open(txt_file_path, "r", encoding="utf-8") as file:
    text = file.read()
    
    

# Load environment variables from .env
load_dotenv()

# Now you can retrieve the variables using os.environ.get(...)
groq_api_key = os.environ.get("GROQ_API_KEY")

portkey = Portkey(
    api_key=os.environ.get("Portkey_API_KEY"),
    virtual_key=os.environ.get("Portkey_Virtual_KEY")
)




# Create the prompt using the text from the .txt file and the follow-up question
chat_completion = portkey.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are a highly skilled academic with expertise in multiple disciplines, \
                        fluent in Turkish. Write a formal, structured project proposal in Turkish, using a clear and professional tone. \
                        Organize the content logically with sections like introduction, objectives, methodology, and conclusions. \
                        Use data and citations to support your points, and ensure your writing is both insightful and accessible. \
                        Focus on critical analysis, providing evaluations and recommendations, and maintain a clear goal-oriented approach throughout the proposal.",
        },
        {
            "role": "user",
            "content": f"Here is the extracted content from the .txt file:\n{text}\n  \
            Now, based on this content, can you help me rewrite 'Proje Özeti' in turkish and detailed."
        },
    ],
    model="llama3-8b-8192",
)

# Output the response
print(chat_completion.choices[0].message.content)
