import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from api import GPT, Example, UIConfig
from api import demo_web_app

# Construct GPT object and show some examples
gpt = GPT(engine="davinci",
          temperature=0.5,
          max_tokens=100)


##Generate Google headlines for website.

gpt.add_example(Example("""CopyAi, An AI powered copywriter for small businesses and entrepreneurs.""",
"""Let CopyAi Automate Your Content"""))

gpt.add_example(Example("""CopyAi, An AI powered copywriter for small businesses and entrepreneurs.""",
"""Your words, written by artificial intelligence."""))

gpt.add_example(Example("""CopyAi, An AI powered copywriter for small businesses and entrepreneurs.""",
"""Generate content for your business."""))


# Define UI configuration
config = UIConfig(description="Create Google headlines for your social ads.",
                  button_text="Create",
                  placeholder="Enter a product (optional) and a description of the product.")

demo_web_app(gpt, config)