import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from api import GPT, Example, UIConfig
from api import demo_web_app


# Construct GPT object and show some examples
gpt = GPT(engine="davinci",
          temperature=0.5,
          max_tokens=80)

#Create a Carousel post for attention grabbing

gpt.add_example(Example("""the mountains""",
"""It’s a reflection of how I live my life. Every day is an adventure, and to me, being in the mountains is as exciting as it gets."""))

gpt.add_example(Example("""the mountains""",
"""“It’s not the mountain we conquer, but ourselves. – Sir Edmund Hillary”⁣ .⁣"""))

gpt.add_example(Example("""the mountains""",
"""“Getting back to the roots, rejuvenating in nature. 🌲🏔⁣"""))

gpt.add_example(Example("""tips for writing better code""",
"""“Now that you’ve spent some time learning Python, it’s time to try writing some code. 
You’ll learn more from planning out your code before writing it than any other method. 
Develop an approach to coding that works for⁣ you"""))

gpt.add_example(Example("""tips for writing better code""",
"""“Work smarter, not harder, to speed up the development cycle. Write better code."""))

# Define UI configuration
config = UIConfig(description="Create a caption for your social media post",
                  button_text="Create",
                  placeholder="What is your post about?")

demo_web_app(gpt, config)