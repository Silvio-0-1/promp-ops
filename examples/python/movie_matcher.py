import os

from dotenv import load_dotenv
from braintrust import init_logger, wrap_openai, Eval
from autoevals import ExactMatch
from openai import AzureOpenAI

load_dotenv()

PROJECT_NAME = os.getenv("BRAINTRUST_DEFAULT_PROJECT_NAME", "PromptOps Demo")
logger = init_logger(project=PROJECT_NAME)

azure_client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
)
client = wrap_openai(azure_client)

SYSTEM_PROMPT = (
    "Based on the following description, identify the movie. "
    "Reply with only the exact title (no year, no quotes, no extra words)."
)


def task(movie_description: str) -> str:
    resp = client.chat.completions.create(
        model=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": movie_description},
        ],
        temperature=0,
    )
    return resp.choices[0].message.content.strip()


Eval(
    PROJECT_NAME,
    experiment_name="Movie matcher (Azure)",
    data=[
        {"input": "A detective investigates a series of murders based on the seven deadly sins.", "expected": "Se7en"},
        {"input": "A thief who steals corporate secrets through dream-sharing tech is tasked with planting an idea.", "expected": "Inception"},
        {"input": "A hacker learns the true nature of reality and fights its controllers.", "expected": "The Matrix"},
        {"input": "A cowboy doll gets jealous of a new spaceman toy.", "expected": "Toy Story"},
        {"input": "An orphan discovers he's a wizard and goes to Hogwarts.", "expected": "Harry Potter and the Sorcerer's Stone"},
    ],
    task=task,
    scores=[ExactMatch()],
)
