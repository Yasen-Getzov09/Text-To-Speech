import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Set speaking rate

# Optional: Select voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # You can change the index

print("Text-to-Speech is ready. Type something and press Enter.")
print("Type 'quit' to exit.\n")

while True:
    text = input("You: ")
    
    if text.lower() == "quit":
        print("Exiting Text-to-Speech. Goodbye!")
        break
    
    engine.say(text)
    engine.runAndWait()
