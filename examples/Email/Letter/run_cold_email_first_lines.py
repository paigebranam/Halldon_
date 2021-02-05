import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from api import GPT, Example, UIConfig
from api import demo_web_app


# Construct GPT object and show some examples
gpt = GPT(engine="davinci",
          temperature=0.8,
          max_tokens=80)

#This bot sends slightly informal compliments based on the company/position and info on the recipient.


gpt.add_example(Example("""Boston SEO agency, Were on Clutch as a top rated SEO and marketing agency in Boston, Massachusetts""",
"""“Congrats on being recognized by Clutch as a top SEO & marketing agency in Boston. Heavy competition."""))

gpt.add_example(Example("""Chicago Bulls content creator, Have training camp videos that are all-access.""",
"""“The all-access training camp episodes this year are so well edited - nice work.Hopefully with Donovan 
& your talent maturing you can make noise this year."""))

gpt.add_example(Example("""ad agency music supervisor, Helped direct a number of movies including Searching""",
"""“Your Searching trailers you helped supervise are epic - that movie was ahead of it's time."""))

gpt.add_example(Example("""RPA, an ad agency, Made an animated short about kids with cancer""",
"""“The animations you created for kids with cancer a few years back were powerful - you made a big difference."""))

gpt.add_example(Example("""Direct, Featured a recent case study for an online university that improved conversion rates by 15%""",
"""“Your 15% boost in conversion rate for an online university means a lot of new students - online classes must've skyrocketed since COVID."""))


# Define UI configuration
config = UIConfig(description="Generate cold openings for e-mails",
                  button_text="Generate",
                  placeholder="Company/Position, Info about the company")

demo_web_app(gpt, config)