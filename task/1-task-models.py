from task.app.main import run

# HINT: All available models you can find here: https://ai-proxy.lab.epam.com/openai/models

# TODO:
#  Try different models (`deployment_name`) with such user request:
#  User massage: What LLMs can do?

# Models to try:
# - gpt-4o
# - claude-3-7-sonnet@20250219
# - gemini-2.5-pro

run(
    deployment_name="gemini-2.5-pro",
    print_request=False,  # Switch to False if you do not want to see the request in console
    print_only_content=False,  # Switch to True if you want to see only content from response
)

# The main goal of this task is to explore the functional capabilities of DIAL to be able to work with different
# LLMs through unified API

# -----------------------------------------------------------------------------
# Results
# `gpt-4o` and `gemini-2.5-pro` provide more detailed answers,
#  while claude-3-7-sonnet@20250219 tends to give shorter responses.
# The gemini-2.5-pro includes custom_content.stages[] fields with additional content.
#  This seems to be Gemini-specific extension that represents the reasoning or
#  thinking stages of the model's response generation process.
# Overall all three test modals answering the given question.

