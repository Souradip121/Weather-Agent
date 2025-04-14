from agents.fire_agent import FireAssistant

def main():
    agent = FireAssistant()
    print("🔥 Welcome to FireBot (powered by Gemini AI)")

    while True:
        q = input("\n🗣️ Ask your question (or type 'exit'): ").strip()
        if q.lower() in ['exit', 'quit']:
            print("👋 Goodbye!")
            break
        agent.handle_query(q)

if __name__ == "__main__":
    main()
