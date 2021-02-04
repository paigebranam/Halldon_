import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from api import GPT, Example, UIConfig
from api import demo_web_app

# Construct GPT object and show some examples
gpt = GPT(engine="davinci",
          temperature=0.5,
          max_tokens=100)


##Generate feature to benefit for product


gpt.add_example(Example("""The girl took the dog for a very long walk""",
"""The girl took the dog for a long walk."""))

gpt.add_example(Example("""The girl took the dog for a very long walk""",
"""The girl took the dog on a long walk"""))

gpt.add_example(Example("""If a robot can have rights it should have rights""",
"""If a robot can have rights, then it should have rights"""))


# Define UI configuration
config = UIConfig(description="Simplify your sentences",
                  button_text="Create",
                  placeholder="Enter your sentence here")

demo_web_app(gpt, config)