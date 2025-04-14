from agents.fire_tool_agent import create_fire_agent

def main():
    agent = create_fire_agent()
    print("🔥 Welcome to FireBot (AutoGen + Azure OpenAI + NASA FIRMS)")

    while True:
        q = input("\n🗣️ Ask your question (or 'exit'): ").strip()
        if q.lower() in ['exit', 'quit']:
            break
        result = agent.generate_reply(messages=[{"role": "user", "content": q}])
        print("\n💬 Reply:\n", result)

if __name__ == "__main__":
    main()
