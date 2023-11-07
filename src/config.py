"""Configuration for the LLM Apps Course"""
from types import SimpleNamespace

TEAM = None
PROJECT = "llmapps"
JOB_TYPE = "production"

default_config = SimpleNamespace(
    project=PROJECT,
    entity=TEAM,
    job_type=JOB_TYPE,
    vector_store_artifact="arrogantemartin/llmapps/vector_store:v2",
    chat_prompt_artifact="arrogantemartin/llmapps/chat_prompt:v0",
    chat_temperature=0.3,
    max_fallback_retries=2,
    model_name="gpt-3.5-turbo",
    eval_model="gpt-3.5-turbo",
    eval_artifact="arrogantemartin/llmapps/generated_examples:v0",
)