import os
import sys
API_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..')
sys.path.append(API_PATH)

from api import GPT, Example, UIConfig
from api import demo_web_app


# Construct GPT object and show some examples
gpt = GPT(engine="davinci",
          temperature=0.5,
          max_tokens=80)

#Create new ideas for products

gpt.add_example(Example("""CopyAi, an AI powered copywriter for small businesses and entrepreneurs""",
"""“An AI powered virtual assistant, scheduling meetings with relevant contacts and preparing a sales call"""))

gpt.add_example(Example("""CopyAi, an AI powered copywriter for small businesses and entrepreneurs""",
"""“An AI powered Virtual assistant"""))

gpt.add_example(Example("""CopyAi, an AI powered copywriter for small businesses and entrepreneurs""",
"""“AI powered sales page builder"""))

gpt.add_example(Example("""CopyAi, an AI powered copywriter for small businesses and entrepreneurs""",
"""“CopyAi optimizes websites for SEO purposes."""))

gpt.add_example(Example("""CopyAi, an AI powered copywriter for small businesses and entrepreneurs""",
"""“CopyAi automates sales letters and ad copy for advertising"""))


# Define UI configuration
config = UIConfig(description="Generate new ideas for products",
                  button_text="Generate",
                  placeholder="Product (optional), description of product")

demo_web_app(gpt, config)
