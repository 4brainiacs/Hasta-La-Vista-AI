# Hasta-La-Vista-AI
“Hasta La Vista AI” is a Python script designed to generate high-quality content through artificial intelligence. By leveraging OpenAI's powerful chatGPT API architecture, the script facilitates seamless, human-like conversations between two chatbots, which in turn generate insightful and engaging articles.

The chatbots discuss the benefits and challenges of any topic you want, critical aspects of well-written articles, and practical tips to improve writing. 
The two chatbots are a Content Writer and an Editor.
The Editor is critical and comes with critical feedback to the Writer.

The program uses OpenAI's GPT-3 API to generate the chatbot responses.


Here are some explanations of the script's components and how it works:

Imports: The script imports necessary libraries such as Openai, json, and tenacity. These libraries provide functions to interact with OpenAI's GPT-3 API, handle JSON files, and implement retry mechanisms for API requests, respectively.

API key and configuration: The script reads the OpenAI API key and organization ID from a config.json file. 
You need your own API credentials, required to access OpenAI's GPT-3 API. You can get an OpenAI API by creating your own OpenAI API account. The price is affordable. I was playing with the script quite extensively during the test process and I was spending $9. You have also a limit you can set in your OpenAI API account.


generate_response() function: This function takes a language model, a message history, and a chatbot name as input. It combines the message history into a prompt and uses the OpenAI API to generate a response from the given model. 

The function limits the conversation history to 3500 characters to prevent reaching the API's maximum token limit. It also sets the response generation temperature to 1.2 to introduce more randomness in the chatbot responses.

generate_response_with_retry() function: This function is a wrapper around the generate_response() function. It adds a retry mechanism using the tenacity library. This function will retry the API request up to 3 times, with an exponential backoff waiting time between retries, in case of failures or errors.

Initial messages: The script reads the initial messages for both chatbots from text files (chatbot1.txt and chatbot2.txt). These initial messages set the context for the chatbots' conversation.

Conversation topic: The conversation topic is defined as a string, which includes discussing any topic you are interested in, and aspects of well-written articles. In the script, you will find the line where you just have to remove the brackets and add your own topic of interest.

Message history: The script initializes a message history list with a system message setting the context and roles, followed by the user and assistant initial messages.

Generate initial response: The script calls the generate_response_with_retry() function to generate an initial response for Chatbot1, using the conversation topic and initial messages.

Conversation loop: The script runs a conversation loop for a specified number of turns (10 in this case), but you can increase or decrease this number of turns based on your topic and at your discretion. Each iteration, alternates between Chatbot1 and Chatbot2, using the generate_response_with_retry() function to generate their responses. The message history is updated after each response.


Extract the article: The script extracts the chatbot responses to create an article by concatenating all the assistant's messages with newline separators.

Save the article: The script saves the generated article to a text file named hasta_la_vista_article.txt. 
The article is saved in the same folder with the chatbot1.txt, chatbot2.txt with the Python script, and the config.json file.

This script is helpful for generating a conversational article on a specific topic by simulating a discussion between two AI chatbots. 
It can be used to generate diverse and engaging content related to any topic you are interested in writing articles and writing tips, 
which can then be used for publishing, blogging, or learning purposes.

By automating the initial stages of content generation, Hasta La Vista AI script not only enhances efficiency and productivity but also empowers 
content writers and editors to focus on what they do best – creating exceptional content that drives results. 

As the digital landscape continues to evolve, embracing AI-driven solutions like Hasta La Vista AI will be key to the ongoing success of content writers, 
editors, and SEO agencies alike.


