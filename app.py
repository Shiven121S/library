import streamlit as st
import smtplib
from datetime import date

# Function to send an email
def send_email(subject, body):
    # Replace with your email and password
    sender_email = "vishalsingla82@gmail.com"
    password = "zhhqsdbbbwgcoooc"

    # Recipient's email (you can keep it the same for testing purposes)
    receiver_email = "omnis316@gmail.com"

    # Message formatting
    message = f"Subject: {subject}\n\n{body}"

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

# Streamlit app
def main():
    st.title("Email Button App")

    # Custom CSS styles to make it look like Discord
    st.markdown(
        """
        <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
            line-height: 1.6;
            color: #dcddde;
            background-color: #36393f;
        }
        .stButton>button {
            color: #dcddde;
            background-color: #7289da;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 14px;
            margin: 4px 2px;
            transition-duration: 0.4s;
            box-shadow: 0 2px 2px 0 rgba(0, 0, 0, 0.14),
                        0 1px 5px 0 rgba(0, 0, 0, 0.12),
                        0 3px 1px -2px rgba(0, 0, 0, 0.2);
        }
        .stButton>button:hover {
            background-color: #677bc4;
        }
        .stButton>button:active {
            background-color: #5865a6;
            box-shadow: 0 5px #666;
            transform: translateY(4px);
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.write("Please enter your 6-digit ID number, your name, and the name of the book:")
    
    # Input fields for ID number, name, and book
    id_number = st.text_input("ID Number", max_chars=6)
    name = st.text_input("Name")
    book = st.text_input("Book")

    # Button becomes clickable only if all fields are filled
    if id_number and name and book:
        if st.button("Send Email"):
            # Email subject and body formatting
            subject = f"{name}; {book}"
            body = f"{id_number}\n{name}\n{book}\n{date.today()}"

            # Send the email
            send_email(subject, body)
            st.success(f"Email sent for {name}!")

if __name__ == "__main__":
    main()
