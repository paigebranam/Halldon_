import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from api import GPT, Example, UIConfig
from api import demo_web_app


# Construct GPT object and show some examples
gpt = GPT(engine="davinci",
          temperature=0.5,
          max_tokens=80)

#Create a hook for the intro of a video


gpt.add_example(Example("""tips for writing better code""",
"""“Coming soon: I'll be releasing a new course that teaches you tips and tricks for writing better code. 
Sign up for my newsletter to get notified when it's available ."""))

gpt.add_example(Example("""tips for writing better code""",
"""“If you're still writing code like a caveman, here's the tips for you."""))

gpt.add_example(Example("""tips for writing better code""",
"""“Do you wanna be a code ninja?"""))

gpt.add_example(Example("""5 easy ways to come up with content ideas""",
"""“If you're stuck with what to blog about, watch this video and never be stuck again."""))

gpt.add_example(Example("""5 easy ways to come up with content ideas""",
"""“How do you come up with ideas for things to film?"""))

gpt.add_example(Example("""Pandas for python""",
"""“Python for Pandas - learn pandas by watching a video a day."""))

gpt.add_example(Example("""Pandas for python""",
"""“Hey pythonistas. We're going to learn how to work with pandas today."""))


# Define UI configuration
config = UIConfig(description="Create an attention grabbing hook for your video intro.",
                  button_text="Create",
                  placeholder="What is your video about?")

demo_web_app(gpt, config)