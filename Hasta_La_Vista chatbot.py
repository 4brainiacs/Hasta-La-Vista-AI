import openai
import json
from tenacity import retry, stop_after_attempt, wait_exponential

# Load API key and organization ID from config.json
with open("config.json", "r") as f:
    config = json.load(f)
    openai.api_key = config["OPENAI_API_KEY"]
    openai.organization = config["OPENAI_ORGANIZATION"]


def generate_response(model, messages, name):
    message_texts = [f"{message['role']}: {message['content']}" for message in messages]
    while len("\n".join(message_texts) + f"\n{name}: ") > 3500:  # Limit the conversation history
        message_texts.pop(0)
    prompt = "\n".join(message_texts) + f"\n{name}: "

    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=700,
        n=1,
        stop=None,
        temperature=1.2,  # Increase temperature to introduce more randomness
    )

    return response.choices[0].text.strip()


@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=2, max=60))
def generate_response_with_retry(model, messages, name):
    return generate_response(model, messages, name)


# Read initial messages from text files
with open("chatbot1.txt", "r") as f1, open("chatbot2.txt", "r") as f2:
    chatbot1_initial_message = f1.read().strip()
    chatbot2_initial_message = f2.read().strip()

conversation_topic = (
    "Discuss the benefits and challenges of (any topic you want) "
    "Also, discuss the key aspects of a "
    "well-written article and give practical tips to improve writing."
)
messages_history = [
    {
        "role": "system",
        "content": (
            "You are two chatbots having a conversation about (remove the brackets and add the topic you want the chatbots to discuss and write the article. 
            Don't forget that in Python is a limit of characters per line before you get a warning). "
            "Your goal is to discuss the benefits and challenges of (remove the brackets and add the goal you want to be accomplished by the chatbots). "
            f"{conversation_topic}"
        ),
    },
    {"role": "user", "content": chatbot1_initial_message},
    {"role": "assistant", "content": chatbot2_initial_message},
]

initial_response = generate_response_with_retry("text-davinci-002", messages_history, "Chatbot1")
print(initial_response)

# Run the conversation loop
num_turns = 10
for i in range(num_turns):
    role = "user" if i % 2 == 0 else "assistant"
    chatbot_name = "Chatbot1" if i % 2 == 0 else "Chatbot2"
    loop_response = generate_response_with_retry("text-davinci-002", messages_history, chatbot_name)
    print(f"{chatbot_name}: {loop_response}")
    messages_history.append({"role": role, "content": loop_response})

# Extract only the article from the conversation
article_text = ""
for msg in messages_history:
    if msg["role"] == "assistant":
        article_text += msg["content"] + "\n"

# Save the article to a text file
with open("hasta_la_vista_article.txt", "w") as f:
    f.write(article_text)
