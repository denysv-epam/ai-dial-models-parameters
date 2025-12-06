from task.app.main import run

# TODO:
#  Try the `temperature` parameter that controls the randomness of the output. It's a parameter for balancing creativity
#        and determinism. Range: 0.0 to 2.0, Default: 1.0
#  User massage: Describe the sound that the color purple makes when it's angry

# TODO:
#  Use `temperature` parameter with value in range from 0.0 to 1.0!
#  (Optional) Use `temperature` parameter with value 2.1 and check what happens
run(deployment_name="gpt-4o", print_only_content=True, temperature=2)

# Results
# Below temperature = 1 its quite deterministic, uses facts.
# When temperature is higher that 1 it's became more "creative", imagining that colors
#  may produce sound. And temperature = 2 will result with absolute gibberish,
#  using random tokens to answer.

