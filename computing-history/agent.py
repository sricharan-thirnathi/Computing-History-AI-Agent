# Before running the sample:
#    pip install azure-ai-projects>=2.1.0

from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

endpoint = "https://charan-first-foundry-resource.services.ai.azure.com/api/projects/charan-first-foundry"

project_client = AIProjectClient(
    endpoint=endpoint,
    credential=DefaultAzureCredential(),
)

my_agent = "computing-historian"
my_version = "1"

openai_client = project_client.get_openai_client()

# Reference the agent to get a response
def run_loop():
    print('Enter a prompt for the agent (type "quit" to exit).')
    try:
        while True:
            prompt = input('> ').strip()
            if not prompt:
                continue
            if prompt.lower() == 'quit':
                print('Exiting.')
                break

            response = openai_client.responses.create(
                input=[{"role": "user", "content": prompt}],
                extra_body={"agent_reference": {"name": my_agent, "version": my_version, "type": "agent_reference"}},
            )

            print(f"Response output: {response.output_text}\n")
    except KeyboardInterrupt:
        print('\nInterrupted. Exiting.')


if __name__ == '__main__':
    run_loop()



