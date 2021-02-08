import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from api import GPT, Example, UIConfig
from api import demo_web_app


# Construct GPT object and show some examples
gpt = GPT(engine="davinci",
          temperature=0.4,
          max_tokens=60)


gpt.add_example(Example("""Halldon, We create websites that make you money.""",
"""Get a website that brings you clients. Halldon enables businesses to build and grow their online presence 
by providing smart and affordable websites with nationwide support."""))

gpt.add_example(Example("""Halldon, We create websites that make you money.""",
"""Our web design specialists can craft a stunning looking website for your business that will grow your revenue and boost your profits."""))

gpt.add_example(Example("""root your plants faster with this rooting hormone""",
"""Root enhancer for cuttings and strong growth when rooting plants"""))

gpt.add_example(Example("""root your plants faster with this rooting hormone""",
"""Get more root depth and diameter with easy to use liquid hormones."""))




# Define UI configuration
config = UIConfig(description="Create subheaders for your website",
                  button_text="Create",
                  placeholder="Enter a product (optional), describe your product.")

demo_web_app(gpt, config)
