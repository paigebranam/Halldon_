import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from api import GPT, Example, UIConfig
from api import demo_web_app


# Construct GPT object and show some examples
gpt = GPT(engine="davinci",
          temperature=0.5,
          max_tokens=80)

#Create a short text hook for product


gpt.add_example(Example("""CopyAi, AI powered copywriter for small businesses and entrepreneurs""",
"""AI powered copywriter for small businesses and entrepreneurs
If you're any kind of businessperson then you've probably written an ad
There's an alternative to expensive marketing firms.
A thread 👇👇"""))

gpt.add_example(Example("""CopyAi, AI powered copywriter for small businesses and entrepreneurs""",
"""AI powered copywriter for small businesses and entrepreneurs
The founder of CopyAi turned a $6,000 investment into a multi-million dollar business.
Let's explore the model in this thread."""))

gpt.add_example(Example("""CopyAi, AI powered copywriter for small businesses and entrepreneurs""",
"""AI powered copywriter for small businesses and entrepreneurs
I'll go into what makes this AI copywriter different to many others,
explain the market it serves, give my review of its services so far,
and show you what you can achieve with it."""))



# Define UI configuration
config = UIConfig(description="Create an attention grabbing hook for your products or blog posts.",
                  button_text="Create",
                  placeholder="Product (optional), description of product")

demo_web_app(gpt, config)