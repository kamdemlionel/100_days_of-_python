import streamlit as st

# Caesar Cipher Alphabet
alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

# Encrypt function
def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            cipher_text += alphabet[new_position]
        else:
            cipher_text += letter  # Keep spaces/punctuation unchanged
    return cipher_text

# Decrypt function
def decrypt(text, shift):
    original_text = ""
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position - shift
            original_text += alphabet[new_position]
        else:
            original_text += letter
    return original_text


# ================= Streamlit UI ==================
st.title("🔐 Caesar Cipher App")
st.write("Encrypt or Decrypt your secret messages using Caesar Cipher.")

# Select direction
direction = st.radio("Choose an option:", ["Encode", "Decode"])

# Input fields
text = st.text_area("Enter your message:", "").lower()
shift = st.number_input("Enter shift number:", min_value=1, max_value=25, value=5)

# Process button
if st.button("Run Cipher"):
    if direction == "Encode":
        result = encrypt(text, shift)
        st.success(f"✅ Encoded text: {result}")
    else:
        result = decrypt(text, shift)
        st.success(f"✅ Decoded text: {result}")
