from autogen import ConversableAgent, register_function
from autogen.oai.client import AzureOpenAI
from tools import fire_tools

def create_fire_agent():
    agent = ConversableAgent(
        name="FireMonitor",
        system_message="You are a fire monitoring assistant for India. Use tools to summarize satellite fire data.",
        llm_config={
            "config_list": [
                {
                    "model": "gpt-4o",
                    "base_url": "https://aishi-m9hf1ep2-eastus2.cognitiveservices.azure.com/",
                    "api_key": "8qTRERMol98uKNCMgBdmokHRgRqMqtWfwHt1snPG8g8UmDoyXAoJJQQJ99BDACHYHv6XJ3w3AAAAACOG7Tk7",
                    "api_version": "2025-01-01-preview",
                    "api_type": "azure"
                }
            ]
        },
    )

    register_function(
        f=fire_tools.summarize_fire_data,
        caller=agent,
        executor=agent,
        name="summarize_fire_data",
        description="Summarizes fire locations in India using FIRMS satellite data."
    )

    return agent
