from autogen import ConversableAgent, register_function
from autogen.oai.client import AzureOpenAI
from tools import fire_tools
from autogen.coding import LocalCommandLineCodeExecutor
import tempfile
temp_dir = None
def create_fire_agent():
    global temp_dir
    temp_dir = tempfile.TemporaryDirectory()
    executor = LocalCommandLineCodeExecutor(
    timeout=20,  # Timeout for each code execution in seconds.
    work_dir=temp_dir.name  # Use the temporary directory to store the code files.
    )
    
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
        code_execution_config={"executor": executor},
        human_input_mode="ALWAYS"
    )
    
    
    # register_function(
    #     f=fire_tools.summarize_fire_data,
    #     caller=agent,
    #     executor=agent,
    #     name="summarize_fire_data",
    #     description="Summarizes fire locations in India using FIRMS satellite data."
    # )

    return agent
