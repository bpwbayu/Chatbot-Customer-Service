import streamlit as st
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')

sia = SentimentIntensityAnalyzer()
responses = {
    "positive": "Thank you for your positive feedback! We're glad you enjoyed it 😄",
    "negative": "We're sorry to hear about your experience 😢",
    "neutral": "Thank you for your feedback. We'll keep improving our service."
}
    
def chatbot_response(text):
    text_lower = text.lower()
    greetings = ["hello", "hallo", "halo", "haloo", "hai", "hi", "hei", "heyy", "hey", "good morning", "morning", "good afternoon", "good evening", "help", "help me", "i need help", "need help"]
    farewells = ["bye", "goodbye", "see you", "thanks", "thank you"]
    if any(greet in text_lower for greet in greetings):
        return "Hi there! How can I help you today? 😊"
    
    score = sia.polarity_scores(text)['compound']
    if score > 0.05:
        return responses['positive']
    elif score < -0.05:
        return responses['negative']
    else:
        return responses['neutral']


st.set_page_config(page_title="Customer Support Chatbot", page_icon="💬", layout="centered")
st.title("💬 Chatbot Using VADER Sentiment Analyzer")
st.write("This chatbot analyzes the sentiment of your message and responds accordingly.")

user_input = st.text_input("Enter your message:")

if st.button("Send"):
    if user_input.strip():
        response = chatbot_response(user_input)
        st.markdown(f"**Chatbot:** {response}")
    else:
        st.warning("Please enter a message before sending.")

st.markdown("---")
st.caption("Built with ❤️ using Streamlit and NLTK (VADER)")