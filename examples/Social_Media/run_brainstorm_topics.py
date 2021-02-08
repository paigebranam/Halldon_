import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from api import GPT, Example, UIConfig
from api import demo_web_app


# Construct GPT object and show some examples
gpt = GPT(engine="davinci",
          temperature=0.5,
          max_tokens=80)

#Create a brainstorming generator

gpt.add_example(Example("""The benefits of e-mail campaigns""",
"""“how to use e-mail marketing"""))

gpt.add_example(Example("""The benefits of e-mail campaigns""",
"""“create your own e-mail marketing campaign"""))

gpt.add_example(Example("""The benefits of e-mail campaigns""",
"""“how to send out mailers to promote online courses"""))

gpt.add_example(Example("""The benefits of e-mail campaigns""",
"""“email marketing tools to increase customer base"""))

gpt.add_example(Example("""The benefits of e-mail campaigns""",
"""“how to grow my email list quickly"""))

gpt.add_example(Example("""The benefits of e-mail campaigns""",
"""“marketing automation strategies"""))

gpt.add_example(Example("""The best camera gear on the market""",
"""“our favorite camera gear for filmmakers"""))

gpt.add_example(Example("""The best camera gear on the market""",
"""“how to make money as a photographer"""))

gpt.add_example(Example("""The best camera gear on the market""",
"""“the best canon lenses for beginners"""))



# Define UI configuration
config = UIConfig(description="Brainstorm topics",
                  button_text="Create",
                  placeholder="What is your topic?")

demo_web_app(gpt, config)