import pytesseract 
from PIL import Image
import openai


# png, pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' #enter tesseract file directory here
img = Image.open('') #enter the image you want to read
image_text = (pytesseract.image_to_string(img)) #pytesseract extracts words from png file

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
