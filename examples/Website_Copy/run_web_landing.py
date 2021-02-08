import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from api import GPT, Example, UIConfig
from api import demo_web_app

# Construct GPT object and show some examples
gpt = GPT(engine="davinci",
          temperature=0.5,
          max_tokens=100)


##Generate Landing Page Hero Text

gpt.add_example(Example("""CopyAi, An AI powered copywriter for small businesses and entrepreneurs.""",
"""Your AI-Powered Copywriter"""))

gpt.add_example(Example("""CopyAi, An AI powered copywriter for small businesses and entrepreneurs.""",
"""AI-powered copywriter for business"""))

gpt.add_example(Example("""CopyAi, An AI powered copywriter for small businesses and entrepreneurs.""",
"""Get professional copy for your website, sales page and social media messages in less"""))

gpt.add_example(Example("""CopyAi, An AI powered copywriter for small businesses and entrepreneurs.""",
"""Create sales generating content in minutes."""))

gpt.add_example(Example("""CopyAi, An AI powered copywriter for small businesses and entrepreneurs.""",
"""We write your content in less than 60 seconds."""))

gpt.add_example(Example("""Halldon, We create websites that make you money.""",
"""The Internet Needs a New Kind of Website"""))

gpt.add_example(Example("""Halldon, We create websites that make you money.""",
"""Good Websites Make Money"""))

# Define UI configuration
config = UIConfig(description="Create Landing Page Hero Text.",
                  button_text="Create",
                  placeholder="Enter a product (optional) and a description of the product.")

demo_web_app(gpt, config)