import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from api import GPT, Example, UIConfig
from api import demo_web_app


# Construct GPT object and show some examples
gpt = GPT(engine="davinci",
          temperature=0.5,
          max_tokens=80)

#Create a rhyming poem based off a topic

gpt.add_example(Example("""Cocoon""",
"""“I am cocooned in sheets but I do not emerge a butterfly
My arm touches the soft cold fabric of the sheets
Where your heart should be
I wake, startled
You are gone
And I can bet a heavy wager
I know what you did
As I lay with hair across my face and mouth ajar
My body hot, my face cold
You wouldn’t have known how I felt
You never kissed my cheek or stroked my hair
You never snuggled up to my warm body
Fingers caressing my stomach
And I know you never stopped to look at my face
Even though I was cocooned
Buried in blankets and sheets and I know you didn’t think
“My God, she’s beautiful”
Even when she sleeps
I was asleep but I know what you did
Crept away early in the morning
Stood sighing into the stream of hot water
Enveloped by steam, your own cocoon
You didn’t want to leave
You found your keys and you pulled out the drive
Without a second glance at the upstairs window where I slept
Peacefully
Dreaming that you
Stroked my hair
Woke me up by mistake
Said sorry, kissed my cheek
Knew how lucky you was even though I’m not a butterfly
Yet
But I will be
But now I am cocooned in sheets
Then I will be cocooned in bags of clothes
Debts, hatred, sorrow, regret
And I don’t know who said it but I remember these words:
The best time to plant a tree is twenty years ago
And the second best time is now
I sit up and brush my hair out of my face
There is a suitcase on top of the wardrobe
I rise from my cocoon but it is still there
Like it’s trying to give me a hug but struggles to take my pain
To help me grow
I must writhe and shift like the caterpillar and
One day I will be free
But for now I am cocooned
One day I will be where I need to be
Soon
A butterfly I’ll be
I will emerge
Glorious, wings of gold
Like a phoenix reborn from the ashes
I have transformed
And you absence will be a distant memory"""))



# Define UI configuration
config = UIConfig(description="Create a rhyming poem",
                  button_text="Create",
                  placeholder="Topic (i.e.: Cocoon)")

demo_web_app(gpt, config)