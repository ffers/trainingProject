from dotenv import load_dotenv
from application.services.ai_agent import TestAIAgent

load_dotenv()



def main():
    agent = TestAIAgent()
    print("Type 'quit' to exit.")
    while True:
        message = input('You: ')
        if message.lower() == 'quit':
            break
        reply = agent.respond(message)
        print('Agent:', reply)


if __name__ == '__main__':
    main()

