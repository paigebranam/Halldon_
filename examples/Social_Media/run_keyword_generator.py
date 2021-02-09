import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from api import GPT, Example, UIConfig
from api import demo_web_app

# Construct GPT object and show some examples
gpt = GPT(engine="davinci",
          temperature=0.5,
          max_tokens=100)


##Generate keywords based off of what you'd like to discuss.


gpt.add_example(Example("""The Pacific swift (Apus pacificus) is a bird that breeds in eastern Asia. This swift is strongly migratory, spending the northern 
hemisphere's winter in a wide range of habitats in Southeast Asia and Australia. The general shape and blackish plumage recall its relative, the common swift, 
from which it is distinguished by a white rump band and heavily marked underparts. Its main call is a screech typical of its family. It breeds in sheltered 
locations such as caves and rock crevices, or under the eaves of houses. The nest is a half-cup of dry grass and other fine material that is gathered in flight, 
cemented with saliva and attached to a vertical surface. Two or three white eggs are incubated for about seventeen days before hatching. Like all swifts, 
the Pacific swift feeds exclusively on insects caught in flight. The species has a large population that occurs as far afield as the US and New Zealand, 
and rarely in Europe.""",
"""Pacific swift, Apus pacificus, Black swift, Black Swift, swifts, swifts in flight"""))


gpt.add_example(Example("""The Pacific swift (Apus pacificus) is a bird that breeds in eastern Asia. This swift is strongly migratory, spending the northern 
hemisphere's winter in a wide range of habitats in Southeast Asia and Australia. The general shape and blackish plumage recall its relative, the common swift, 
from which it is distinguished by a white rump band and heavily marked underparts. Its main call is a screech typical of its family. It breeds in sheltered 
locations such as caves and rock crevices, or under the eaves of houses. The nest is a half-cup of dry grass and other fine material that is gathered in flight, 
cemented with saliva and attached to a vertical surface. Two or three white eggs are incubated for about seventeen days before hatching. Like all swifts, 
the Pacific swift feeds exclusively on insects caught in flight. The species has a large population that occurs as far afield as the US and New Zealand, 
and rarely in Europe.""",
"""Pacific swift, Apus pacificus, bird birdwatching fantastic creatures"""))

gpt.add_example(Example("""The pink-necked green pigeon (Treron vernans) is a species of bird in the dove family, Columbidae, 
common in Southeast Asia. It is primarily a frugivore, feeding in groups in the mid-canopy on figs and other fruits.""",
"""pigeon, green pigeon, pink-necked green pigeon, Asia, Southeast Asia"""))

gpt.add_example(Example("""The pink-necked green pigeon (Treron vernans) is a species of bird in the dove family, Columbidae, 
common in Southeast Asia. It is primarily a frugivore, feeding in groups in the mid-canopy on figs and other fruits.""",
"""Pink-necked Green Pigeon, Green Pigeon, Asian Green Pigeon"""))

gpt.add_example(Example("""The February 1998 Afghanistan earthquake occurred at 19:03 local time near the Afghanistan-Tajikistan border.""",
"""afghanistan earthquake, afghanistan, earthquake"""))

gpt.add_example(Example("""The February 1998 Afghanistan earthquake occurred at 19:03 local time near the Afghanistan-Tajikistan border.""",
"""earthquake, geography, topography, relief map of Afghanistan, mountain ranges of Afghanistan, natural disasters in Afghanistan, geology of 
Afghanistan, greenstone belts in Afghanistan"""))


# Define UI configuration
config = UIConfig(description="Create keywords for your text",
                  button_text="Create",
                  placeholder="What do you want to talk about?")

demo_web_app(gpt, config)