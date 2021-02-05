import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from api import GPT, Example, UIConfig
from api import demo_web_app


# Construct GPT object and show some examples
gpt = GPT(engine="davinci",
          temperature=0.5,
          max_tokens=80)

#Create a call to action for product

gpt.add_example(Example("""CopyAi, an AI powered copywriter for small businesses and entrepreneurs""",
"""“Sign up now and use CopyAi to automate your company blog!"""))

gpt.add_example(Example("""CopyAi, an AI powered copywriter for small businesses and entrepreneurs""",
"""“Try CopyAi risk-free for 10 days"""))


gpt.add_example(Example("""rooting hormone that will build stronger roots faster.""",
"""“Get 3X faster plant growth today (CLICK HERE)."""))


gpt.add_example(Example("""rooting hormone that will build stronger roots faster.""",
"""“Go check out the best rooting hormone"""))

# Define UI configuration
config = UIConfig(description="Create a Call-To-Action for your product.",
                  button_text="Create",
                  placeholder="Product (optional), description of product")

demo_web_app(gpt, config)