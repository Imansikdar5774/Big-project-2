# simple_chatbot.py
print("Hello! Main aapka dost chatbot hoon 😄")
print("Mujhse baat karne ke liye kuch bhi type karo (exit likh kar band kar sakte ho)")

while True:
    user_input = input("You: ").lower().strip()

    if user_input in ["bye", "goodbye", "exit", "band karo", "bas"]:
        print("Bot: Bye bye! Phir milte hain! 👋")
        break

    elif "hello" in user_input or "hi" in user_input or "hey" in user_input:
        print("Bot: Hello ji! Kya haal hai? 😊")

    elif "kaise ho" in user_input or "kaisa hai" in user_input:
        print("Bot: Mast hoon yaar! Tu suna? 😉")

    elif "naam" in user_input:
        print("Bot: Mera naam Grok hai... lekin tu mujhe jo bulaaye, main wahi ban jaunga! 😄")

    elif "padhai" in user_input or "study" in user_input or "exam" in user_input:
        print("Bot: Padhai kar le bhai... warna mummy maar degi! 📚😅")

    elif "?" in user_input:
        print("Bot: Hmm... yeh toh interesting sawaal hai! Lekin mujhe abhi jawab nahi pata... 😅")

    else:
        print("Bot: Hmm... samajh nahi aaya. Aur kuch aur bol na! 🧐")

print("\nChat khatam! Thanks for chatting ❤️")