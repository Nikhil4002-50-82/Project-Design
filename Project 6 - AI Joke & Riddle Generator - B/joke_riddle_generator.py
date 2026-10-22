# Task 1 - Set Your Google Gemini API Key
# Step 1: Import LangChain Modules
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser

# Step 2: Configure Free Gemini API Key
GEMINI_API_KEY = "PASTE_YOUR_GEMINI_API_KEY_HERE"

# Task 2 - Initialize the Gemini Model
# Step 1: Instantiate ChatGoogleGenerativeAI with gemini-3.8-flash
llm = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    google_api_key=GEMINI_API_KEY
)

# Task 3 - Create the Joke Generator Chain
# Step 1: Define Joke PromptTemplate
joke_prompt = PromptTemplate.from_template(
    "Tell me a short, clean, funny joke about {topic}."
)
# Step 2: Assemble the Joke Pipeline
joke_chain = joke_prompt | llm | StrOutputParser()

# Task 4 - Create the Riddle Challenge Chain
# Step 1: Define Riddle PromptTemplate
riddle_prompt = PromptTemplate.from_template(
    "Tell me a fun riddle about {topic}. Include the riddle, a hint, and the answer."
)
# Step 2: Assemble the Riddle Pipeline
riddle_chain = riddle_prompt | llm | StrOutputParser()

# Task 5 - Create the Pun Generator Chain
# Step 1: Define Pun PromptTemplate
pun_prompt = PromptTemplate.from_template(
    "Tell me one clever pun about {topic}."
)
# Step 2: Assemble the Pun Pipeline
pun_chain = pun_prompt | llm | StrOutputParser()

# Task 6 - Build the Interactive Menu and Application Loop
def main():
    # Step 1: Display Header and Options
    print("Welcome to the AI Joke & Riddle Generator!")
    print("1. Generate Joke")
    print("2. Generate Riddle")
    print("3. Generate Pun")
    choice = input("Enter choice (1-3): ").strip()

    # Step 2: Route Selection to Chains
    if choice == "1":
        topic = input("Enter a topic (e.g. computers, coffee): ").strip()
        print("\n" + joke_chain.invoke({"topic": topic}))
    elif choice == "2":
        topic = input("Enter a riddle topic (e.g. space, animals): ").strip()
        print("\n" + riddle_chain.invoke({"topic": topic}))
    elif choice == "3":
        topic = input("Enter a pun topic (e.g. math, food): ").strip()
        print("\n" + pun_chain.invoke({"topic": topic}))

if __name__ == "__main__":
    main()
