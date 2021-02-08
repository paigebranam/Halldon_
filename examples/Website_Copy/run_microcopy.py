import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from api import GPT, Example, UIConfig
from api import demo_web_app

# Construct GPT object and show some examples
gpt = GPT(engine="davinci",
          temperature=0.5,
          max_tokens=100)


##Generate Microcopy

gpt.add_example(Example("""Thank you for signing up!""",
"""Thanks for signing up to The Hustle."""))


gpt.add_example(Example("""Thank you for signing up!""",
"""Thanks for joining us."""))

gpt.add_example(Example("""Thank you for signing up!""",
"""We have sent a confirmation email to your inbox."""))

gpt.add_example(Example("""Thank you for signing up!""",
"""Thank you! We'll start sending your daily email soon."""))


# Define UI configuration
config = UIConfig(description="Create Microcopies for your website.",
                  button_text="Create",
                  placeholder="What is teh microcopy for? (e.g.: thanks for signing up!")

demo_web_app(gpt, config)