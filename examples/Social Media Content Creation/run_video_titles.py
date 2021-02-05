import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from api import GPT, Example, UIConfig
from api import demo_web_app


# Construct GPT object and show some examples
gpt = GPT(engine="davinci",
          temperature=0.5,
          max_tokens=80)

#Create video titles

gpt.add_example(Example("""skincare for acne treatment""",
"""DIY Skin Care Routine (For Acne)"""))

gpt.add_example(Example("""skincare for acne treatment""",
"""Skincare For Acne"""))

gpt.add_example(Example("""skincare for acne treatment""",
"""Acne Care- Best Skin Care Products On Amazon"""))

gpt.add_example(Example("""Hot tips for marketing""",
"""HOT Marketing Tips You Can Use Right Now | Jeff Markowitz"""))

gpt.add_example(Example("""Hot tips for marketing""",
"""Hot Tips From A Marketing Expert"""))

gpt.add_example(Example("""Hot tips for marketing""",
"""Hot Tips From The Best Marketers"""))


gpt.add_example(Example("""Ahsoka Tano""",
"""Star Wars: Ahsoka Tano"""))

gpt.add_example(Example("""Ahsoka Tano""",
"""Ahsoka Tano and the lightsabers"""))

gpt.add_example(Example("""Ahsoka Tano""",
"""Star Wars Fan Theory: Ahsoka is Anakin's Daughter"""))

gpt.add_example(Example("""Ahsoka Tano""",
"""Ahsoka Tano - The Force Unleashed"""))


# Define UI configuration
config = UIConfig(description="Create a title for your video",
                  button_text="Create",
                  placeholder="What is the video about?")

demo_web_app(gpt, config)