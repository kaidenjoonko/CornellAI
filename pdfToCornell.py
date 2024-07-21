import openai
from pypdf import PdfReader


# pdf, PdfReader
reader = PdfReader('') #enter the pdf file name here
image_text = "" 
for i in range(len(reader.pages)): #loop through all the pdf pages
    page = reader.pages[i] #extract text from each pdf page
    image_text = image_text + page.extract_text() 

openai.api_key = "" #enter openai API here


def chatGPT_answer(image_text):
    conversation = [
        {
            "role": "system",
            "content": "Cornell Notes are an unique way of notetaking in which based off the text you write a question and follow the question by answer the question." +
                       "I am giving you text straight out of a textbook. Please write 20 cornell styled notes based on the given text.", #prompt given to chatGBT
        },
        {"role": "user", "content": image_text}, #text from the textbook given to chatGBT
    ]
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=conversation)

    # Extract the chatGBT's reply
    reply = response["choices"][0]["message"]["content"].strip()
    # Return the reply as a string
    return str(reply)


with open('CornellNotes.txt', 'wt') as f:  #access a txt file
    print(chatGPT_answer(image_text), file=f)  #print chatGBT's answer in a txt file to store
