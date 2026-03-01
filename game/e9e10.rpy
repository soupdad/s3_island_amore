# #########################################################################
# ## Episode 9 Part 1
# #########################################################################
label s3e9p1:
    scene sand with dissolve
    $ on_screen = []

    show screen day_title(9, 1) with Pause(4)
    hide screen day_title with dissolve
    "Previously on Love Island..."
    "There was a recoupling and..."
    "[s3_name] and [s3_li] coupled up!"
    $ entering("s3_mc_image")
    s3_mc "The person I want to couple up with is..."
    s3_mc "[s3_li]!"
    $ leaving("s3_mc_image")
    $ outfit = "pjs"
    "Everything is on the up..."
    "The Islanders wake up."
    s3_li "Morning, gorgeous."
    $ leaving("s3_li_image")
    "And Ciaran thinks the others are making stuff up..."
    ciaran "What on earth is brunch?"
    $ leaving("ciaran")
    "Poor sweet Ciaran."
    "I'd cook you avocado toast any day of the week."
    "If I had avocados. Or a toaster."
    $ outfit = "swim"
    "But you know what they say. What goes up..."
    s3_bff "But are they loyal?"
    $ leaving("s3_bff_image")
    "Must come down..."
    $ entering("s3_bff_image")
    s3_bff "I got a text!"
    $ leaving("s3_bff_image")

    scene s3-bedroom-day with dissolve
    $ new_scene()
    $ outfit = "pjs"

    $ pronouns(s3_li)

    "You wipe away the sleep in your eyes."
    if s3_li == "Ciaran" or s3_li == "Tai" or s3_li == "Camilo" or s3_li == "AJ":
        "[s3_li] is tickling your nose with a feather."
        s3_mc "Ah, aah..."
        s3_mc "Choo!"
        "You sneeze."
        s3_li "Oops."
        s3_li "Sorry!"
        s3_li "I just really wanted to wake you up with this feather."
        s3_li "It was stuck to you for ages and I just kept thinking of how much of an angel you were."
        s3_mc "So, you stuck it up my nose?"
        s3_li "Yeah..."

        # CHOICE
        menu:
            thought "[s3_li] says I'm an angel."
            "Say some cheesy chat up line":
                "You peer around [s3_li]'s neck."
                s3_li "What are you doing?"
                s3_mc "Looking for the 'made in heaven' tag."
                s3_li "Is that a ladder in your tights or a stairway to heaven?"
                $ s3_mc.like(s3_li)
                "You stick your tongue out at [s3_li]."
                s3_mc "I'm not wearing any tights."
                s3_li "It's still funny."
            "Stick the feather up [s3_li]'s nose":
                "You grab the feather out of [s3_li]'s hand and tickle [him_her] right on the nose."
                s3_li "Ah, aah!"
                s3_li "Choo!"
                "Nicky walks in and grabs his water bottle."
                nicky "Does someone keep sneezing in here?"
                s3_li "Yes, that would be us."
                s3_li "We're making each other sneeze because it's a cute thing to do."
                nicky "Sure you are..."
                nicky "Another day in paradise."
                nicky "I'll leave you two to it."
                "He walks out again."
                "[s3_li] laughs, a little nervously."
            "Cuddle up to [him_her]":
                "You brush the feather away and cuddle closer up to [s3_li]."

    else:
        s3_mc "Morning, you."
        s3_li "Morning."
        "A loose feather is stuck on [s3_li]'s nose."

        # CHOICE
        menu:
            thought "I should..."
            "Just cuddle up to [him_her]":
                "You snuggle closer to [s3_li]."
                "[s3_li] brushes the feather off [his_her] nose."
                s3_li "You're the best cuddler ever."
                $ s3_mc.like(s3_li)
                s3_mc "On a scale from one to ten?"
                s3_li "You're off the scale!"
            "Tickle [him_her] with the feather":
                "You grab the feather and tickle [s3_li] right on the nose."
                "[he_she!c] sneezes loudly."
            "Take it off for [him_her]":
                "You pick the feather of [s3_li]'s nose."
                "[he_she!c] looks at you a little confused."
                s3_li "OK..."
                s3_mc "You had a feather on your nose."
                s3_li "Oh, it's one of those white ones."
                s3_li "I've heard you can make a wish on these."
                s3_li "I know exactly what I'm wishing for..."
                $ s3_mc.like(s3_li)
                s3_li "Want to know what it is?"

                # CHOICE
                menu:
                    thought "Do I want [s3_li] to tell me what [he_she]'s wishing for?"
                    "Yeah, go on!":
                        "[s3_li] smiles."
                        s3_li "I wish for more mornings like this one."
                        s3_li "Being right here in your arms is all I could ever wish for."
                        s3_mc "Aw, that's so sweet!"
                    "Don't you mean 'who'?":
                        "[s3_li] smiles."
                        s3_li "I wish for more mornings like this one."
                        s3_li "Being right here in your arms is all I could ever wish for."
                        s3_mc "Aw, that's so sweet!"
                    "No, it might not come true":
                        "[s3_li] smiles."
                        s3_li "Good thinking."

                "[s3_li] blows on the feather."
                "It floats off in the bedroom."
            
    "[he_she!c] stretches [his_her] arms up, yawning loudly."
    "As [his_her] arms come down, [he_she] wraps one around you."
    "You lie in each other's arms for a while, watching [s3_li]'s chest rise and fall with each breath."
    if s3_li == "Bill" or s3_li == "Harry" or s3_li == "Camilo" or s3_li == "AJ":
        s3_li "I'm just so happy that we get to wake up next to each other in the morning."
    elif s3_mc.past_partners[2] == "Ciaran" or s3_mc.past_partners[2] == "Tai" or s3_mc.past_partners[2] == "Yasmin":
        s3_li "I really love waking up next to you in the morning."
        s3_li "It's the best thing ever."
    else:
        s3_li "I'm just so happy that we get to wake up next to each other in the morning."

    # CHOICE
    menu:
        thought "[s3_li] likes waking up next to me!"
        "Me too, this is perfect":
            "[s3_li] smiles and strokes your cheek."
            $ s3_mc.like(s3_li)
        "You should, I am a treasure":
            s3_mc "You've just woken up at the end of the rainbow, hun."
            s3_li "You crack me up."
            s3_li "I hope you like what's in my pot of gold."
        "Great! Now can we make breakfast?":
            s3_li "We will, we will."
            s3_li "I just want to say something."
    
    s3_li "I wanted to say, like, I really can't tell you how happy I am that you picked me."

    # CHOICE
    menu:
        thought "[s3_li] is pleased that I picked [him_her]..."
        "Reassure [him_her]":
            "[s3_li] grins and blushes a little."
            $ s3_mc.like(s3_li)
        "Ask if [he_she] was nervous":
            s3_li "No."
            s3_li "I don't want that to sound, like, arrogant."
            s3_li "But I was pretty sure you'd pick me."
        "Joke about not wanting to choose anybody":
            s3_mc "I was like, 'I'd rather go home than have to choose from these losers'."
            s3_li "Really?"
            s3_mc "Nah."
            s3_li "Phew!"

    if s3_li == "Bill":
        "Bill holds out his arms and you snuggle up close to him."
        s3_li "It's well nice being here with you."
        s3_li "Is it what you expected? I mean, is this how you imagined life in the Villa?"

        # CHOICE
        menu:
            thought "Is the Villa what I expected?"
            "It's been really chill":
                s3_mc "I was expecting a nice, chilled-out holiday, but it's been a lot of drama."
                s3_li "Yeah. I'm really not a fan of drama."
            "I thought there'd be more drama":
                s3_mc "I was kind of expecting it to be some kind of unending firestorm of drama, but everyone is really nice."
                s3_li "Wow... deep."
                s3_mc "You have that effect on me."
                s3_li "You thought it was all drama-free? What happened on day one?"
                s3_mc "Miki was really just playing the game."
                s3_li "I agree. I don't get on with drama."
            "I didn't expect to find someone like you":
                s3_mc "I was expecting fun, flirty times and a free holiday."
                s3_mc "You kind of knocked me off my feet."
                "He smiles back at you."
                s3_li "I could say the same."

        s3_mc "I love just being able to relax without doing any adulting."
        s3_li "What do you mean?"
        s3_mc "You know, pay your bills, go shopping, make the bed..."
        s3_li "Oh, I getcha. I barely even make my bed, though."
        s3_mc "You what?"
        s3_li "Just not necessary, is it? Nobody sees my bed during the day."
        s3_li "And if they do, they're not gonna care if it's a bit messy."

        # CHOICE
        menu:
            thought "Bill has never made his bed..."
            "Right, it's just a waste of time":
                s3_mc "People spend too much time on things that don't really have a point."
                s3_li "I knew you'd get me."
            "I don't agree with that at all":
                s3_mc "It's just a part of life, you know?"
                s3_mc "You may as well not clean your house."
                s3_li "That's totally different. Not making your bed isn't dirty, is it? It's just saving your effort for things that matter."
                s3_mc "Hmm."
            "Didn't your mum make you when you were a kid?":
                s3_li "Yeah, and it was a massive waste of time then, too."
                s3_mc "So what do you do with all the time you save not making your bed?"
                s3_li "Make a cuppa, obviously."
                s3_li "Means, I get it that little bit sooner in the day, and that's a lifesaver at times."
        
        s3_mc "So is there anything else you've never done?"
        s3_li "Nothing that matters. But if you're interested, let's see..."
        s3_li "I've never spent money on a book. Library's free, innit?"
        s3_li "I've never eaten a peach. It's just an apple being extra."
        s3_li "I've never had a salad with meat in it. Meat's a separate food."
        s3_li "I've never been to America. I've seen it on TV and that's enough."
        s3_mc "OK, OK, I think that's plenty!"

        # CHOICE
        menu:
            thought "There seem to be a lot of things Bill's not done..."
            "I really admire the strength of your convictions":
                s3_mc "Not many people know their own minds as much as you do."
                s3_mc "Even when I don't agree, I think it's really cool that you stick to your guns."
                s3_mc "Maybe I could try and change your mind on one or two things once we leave the island, though?"
                s3_mc "I think it could be fun."
            "Aren't you worried about missing out?":
                s3_li "Not really. I don't need to eat a peach to know it's a weird apple, you know?"
                s3_mc "Yeah, but you might like some of these things."
                s3_mc "You might love peaches!"
                s3_mc "You'll never know until you try."
            "When we leave here, we're gonna do all these things together":
                s3_mc "No buts. We're gonna try loads of new things, and you might even like some of them."
        
        "Bill chews his lip."
        s3_li "This will sound weird, but, I feel like when people think 'Bill' they think 'the guy with the opinions'."
        s3_mc "What do you mean?"
        s3_li "I mean it's hard to change my mind on anything because I'm known for never doing that."
        s3_li "Sometimes I worry that I've backed myself into a bit of a corner."
        s3_mc "Well, maybe I can help you out of it. We can work on Bill 2.0 'the guy who keeps surprising you', what do you say?"
        "Bill smiles, and reaches out to brush your hair with his fingertips."
        s3_li "Sounds great, babe."
        s3_mc "At least try a peach."

    elif s3_li == "Harry":
        s3_li "You're so beautiful, [s3_name]."
        s3_li "I just wanna treat you like a princess and shower you with gifts."

        # CHOICE
        menu:
            thought "Harry wants to shower me with gifts..."
            "Relationships aren't about gifts":
                # NEED TO FILL
                "EMPTY"
            "I love getting gifts":
                s3_li "That's good, 'cause I love giving them."
            "Do I get to buy you gifts too?":
                s3_li "Of course! I just think little presents are a great way to show you care."
        
        s3_li "It's because I'm a total bee."
        s3_mc surprised "A bee?"
        s3_li "Yeah, it's one of the four Affection Animals. Have you heard of them before?"
        s3_mc neutral "No, I haven't."
        s3_li surprised "Basically, it's a way of categorising people based on how they give and receive love and affection."
        s3_li "I'm a bee. We work, we build and give as a way of showing our partners how we feel."
        s3_li neutral "Then you've got Wolves, who show their affection through being present. Standing guard, staying loyal, spending quality time together."
        s3_li "Dolphins are communicative and friendly. They tend to be the first to say 'I love you'."
        s3_li "And then you've got Octopuses. Octopi. Octopeese?"
        s3_mc "I don't think it's octopeese."
        s3_li "It's 'geese', isn't it?"
        s3_mc "That's totally different."
        s3_li "OK, whatever. If you're an Octopus, you're all about physical touch, sex and that."
        s3_mc cheeky "I see."
        s3_li "So which do you think you are?"
        show s3_mc_image neutral

        # CHOICE
        menu:
            s3_mc "I'm definitely"
            "An Octopus":
                # NEED TO FILL
                "EMPTY"
            "A Dolphin":
                s3_li "Nice. I've almost dated Dolphins in the past."
                s3_mc "So that's why they don't let you into the aquarium anymore?"
                "He laughs."
                s3_li "Seriously though, I do tend to get on well with Dolphin-type people. I like how up-front they are."
                s3_li "Sometimes Dolphin/Bee relationships can lack physical intimacy, but I don't think we have that problem."
            "A Bee":
                "Harry grins broadly."
                s3_li "That's like me! That's good news for our compatibility."
                s3_li "Two bees tend to have awesome adventures and do a lot together."
                s3_li "But we've got to be careful that we don't rely on actions too much and forget to communicate clearly."
            "A Wolf":
                s3_li "Cool. Wolves and Bees are meant to get on well, especially when it comes to starting a family and building a home together."
                "He blushes."
                s3_li blush "I mean, not saying we're definitely there yet or anything, but... you know."
                s3_li surprised "But we've got to be careful we don't focus too much on each other and neglect our other relationships."

        # CHOICE
        menu:
            s3_mc "This system..."
            "Makes no sense at all":
                # NEED TO FILL
                "EMPTY"
            "Makes a lot of sense":
                s3_li "Yeah, I really like it. It can tell you a lot about you and your partner."
                s3_li "I'm not into all stuff like that. I think dividing people up based on their personality is mega fun."
            "Would work better with fruit":
                s3_li neutral "Fruit? How would that work? Dolphins are talkative.. What's a talkative fruit?"

                # CHOICE
                menu:
                    s3_mc "Easy. That's a..."
                    "Pineapple":
                        pass
                    "Star fruit":
                        pass
                    "Watermelon":
                        pass
                
                s3_li surprised "Why?"
                "You shrug."
                s3_mc surprised "Wait, don't tell me I'm the only one who has conversations with fruit?"
                "Harry laughs."
        
        show s3_li_image happy
        show s3_mc_image happy
        "He weaves his fingers into yours and pulls you closer. You press up to his chest and he cuddles you tight."

    elif s3_li == "Camilo":
        "Camilo runs his fingers down your cheek and neck. The light touch leaves goosebumps on your skin."

        # CHOICE
        menu:
            thought "Should I kiss him?"
            "No":
                # NEED TO FILL
                "EMPTY"
            "Do the same back to him":
                # NEED TO FILL
                "EMPTY"
            "Yes":
                "You drape your arms around his neck and tilt your head towards him."
                "He kisses you slow and sweet, and for a moment the world melts away and there's only the two of you."
                "At long last, he pulls away and gives you one of his incredible smiles before wrapping you in his arms."
        s3_li "It's so weird to think that this'll all be coming to an end sooner or later."
        s3_mc "I don't want it to be over."
        s3_li "Yeah... back to the real world..."
        s3_li "Having to go down to the supermarket..."
        s3_mc "Having to work!"
        if s3_mc.job == "Athlete": 
            s3_li "You're a pro athlete, right?"
        else:
            s3_li "You're a [s3_mc.job!l], right?"
        s3_mc "Yeah, that's right."
        s3_li "You like it?"

        # CHOICE
        menu:
            thought "How do I feel about my job?"
            "It's fine, but not my dream job":
                # NEED TO FILL
                "EMPTY"
            "I don't like it":
                # NEED TO FILL
                "EMPTY"
            "I love it - it's my dream job":
                s3_mc "Yup. Wouldn't change it for the world."
                s3_mc "It was basically all I've ever wanted to do since I was a little girl."
                if s3_mc.job == "Athlete":
                    s3_mc "The other day, my mum found all these pictures I'd drawn when I was five, and in every single one I was a pro athlete."
                else:
                    s3_mc "The other day, my mum found all these pictures I'd drawn when I was five, and in every single one I was a [s3_mc.job!l]."
                s3_li "That's great."
    
        s3_mc "How do you feel about working in your family's shop?"
        s3_li "I'm not gonna say I hate it, because I don't."
        s3_li "I love chatting with people and that. Plus, I get to big up my mum's empanadas, which are lush."
        s3_li "But it's not my dream job, you get me?"
        s3_mc "Why don't you do something else?"
        s3_li "Not that easy, babe. I took over after my dad got ill. If I leave, who's gonna do it?"
        s3_li "I'd proper love to try something else, but I just can't. It is what it is."

        # CHOICE
        menu:
            thought "Camilo wishes he could leave his job..."
            "You don't have to be responsible for everyone":
                # NEED TO FILL
                "EMPTY"
            "Don't you have a million family members, who could take over?":
                # NEED TO FILL
                "EMPTY"
            "You deserve to be happy":
                s3_mc "I think it's great that you're so into doing the right thing by your family."
                s3_mc "But, like... don't put everyone else above yourself."
                s3_mc "You get to prioritise yourself sometimes. I'm sure your family doesn't want you to support them at the cost of your happiness."
        
        s3_li "But it's about, like, duty, innit?"
        s3_li "It's like giving your word. You can't go back on it."

        # CHOICE
        menu:
            thought "Camilo says he can't quit because he gave his word..."
            "I don't think it's so black-and-white":
                # NEED TO FILL
                "EMPTY"
            "I'm sure your family would understand if you quit":
                # NEED TO FILL
                "EMPTY"
            "That's so noble it hurts":
                s3_li "It's not like I'm some kinda saint."
                s3_li "Just a bloke who does right by his family."
        
        s3_mc "So what would you do if you could do anything?"
        s3_li "BJJ competitor?"
        s3_li "I used to want to do that. But I think I enjoy it more as a hobby."
        s3_li "I think now I'd want to be..."
        s3_li "Actually, it's kind of a secret. Is it OK if I don't tell you right now?"
        s3_mc "Of course. I'd love to hear it one day, though."
        s3_li "Definitely."

    elif s3_li == "AJ":
        s3_li "Ugh, I want to kiss you so bad."

        # CHOICE
        menu:
            thought "AJ wants to kiss me."
            "Blow her a kiss":
                # NEED TO FILL
                "EMPTY"
            "Kiss her softly":
                "You lean towards AJ. she closes her eyes again."
                "Your lips gently touch for a moment. It's soft and earnest."
                "You melt into one another for a few moments."
                "Your hands explore each other's bodies as you rhythmically in sync with each other."
                "Your heart flutters a little as you both pull away."
                s3_li "Wow!"
                $ s3_li.like(s3_li)
                s3_li "You're such a good kisser."
            "Make out passionately":
                "Your lips touch and in an instant your hands are exploring her toned body."
                "She lets out a small moan of pleasure, taking your wrists lightly, pulling you closer into her."
                "You kiss her urgently. For a moment, her touch is all that matters until you both pull away."
                s3_li "Hot damn."
                s3_li "That was..."
                "AJ seems a little bit out of breath."
                s3_li "Hot!"
        
        s3_li "Oh, I was wondering..."
        s3_li "You know, my usual general nosiness."
        s3_li "What kind of stuff gets you in the mood?"
        s3_mc "What kind of mood?"
        s3_li "You know, a sexy mood... in the bedroom."
        s3_li "My coach always says communication."
        s3_mc "Your coach said that to you in the bedroom?"
        "AJ blushes and bursts out laughing."
        s3_li "No!"
        s3_li "What's the one thing that gets you in the mood?"

        # CHOICE
        menu:
            thought "What gets me in the mood..."
            "When someone plays with my hair":
                # NEED TO FILL
                "EMPTY"
            "Just say my name three times while looking in a mirror":
                # NEED TO FILL
                "EMPTY"
            "I love it when people kiss my neck":
                s3_li "Aw, really?"
                "She leans in closer to you."
                s3_li "Mind if I kiss your neck now?"

                # CHOICE
                menu:
                    thought "AJ wants to kiss my neck!"
                    "No thanks, not right now":
                        # NEED TO FILL
                        "EMPTY"
                    "Go for it":
                        "She gently kisses you, sending shivers down your spine."
                        s3_mc "Perfect."
                        s3_li "I try."

        s3_mc "Hey, isn't it your birthday today?"
        s3_li "You remembered!"
        s3_mc "Of course."
        "She hugs you tightly."

        # CHOICE
        menu:
            thought "It's AJ's birthday!"
            "Sing happy birthday":
                # NEED TO FILL
                "EMPTY"
            "Suggest birthday bits":
                s3_mc "So, you up for some birthday bits?"
            "Give her a happy birthday kiss":
                "You lean in and kiss her on the cheek."
        
        "She grins."
        s3_li "I already know this is going to be the best birthday ever."
        s3_li "I get to spend it with you."

    elif s3_li == "Tai":
        "Tai's dark eyes crinkle with his smile."
        s3_li "I was just thinking about my dad. I hope he's having fun watching this."
        s3_li "Not, er, all of it, though."
        "He leans closer, his gaze inviting."

        # CHOICE
        menu:
            thought "Tai wants to kiss me!"
            "Not with his dad watching":
                # NEED TO FILL
                "EMPTY"
            "Kiss him while looking for a camera":
                "You eye up your surroundings before leaning in and kissing Tai firmly on the mouth."
                "Tai draws back and murmurs something you can't quite hear against your neck."
                s3_mc "Wait."
                "You put your hand up over your faces like you're avoiding paparazzi."
                s3_mc "Now no one can see."
                "He kisses very lightly down to the hollow of your throat, then along your collarbones."
                "It's a little ticklish, but the sensation gives you shivers."
                "When you break apart, you still feel warm from Tai's touch."
                "His smile is wonderfully bright."
            "Kiss him":
                "You lose yourself in the kiss. Tai draws back and murmurs something you can't quite hear against your neck."
                "He kisses very lightly down to the hollow of your throat, then along your collarbones."
                "It's a little ticklish, but the sensation gives you shivers."
                "When you break apart, you still feel warm from Tai's touch."
                "His smile is wonderfully bright."
        
        s3_li "Before I came to the Villa, I wondered if I'd get bored. I should've known better."
        s3_mc "I can't picture you being bored."
        s3_li "I thought there might be loads of lying around doing nothing."
        s3_li "Don't get me wrong. I love sunbathing as much as the next guy."
        s3_li "But I didn't want to end up twiddling my thumbs, you know?"

        # CHOICE
        menu:
            thought "Tai didn't want to get bored on Love Island..."
            "Could anyone get bored here?":
                # NEED TO FILL
                "EMPTY"
            "I didn't want to get bored either":
                s3_mc "I didn't really know what it would be like."
                s3_mc "You see it on TV, but that's not the same as seeing it with your own eyes."
                s3_mc "I wondered if there'd be enough to do."
                s3_mc "But it ended up with even more than I could have hoped!"
            "I'd stop you getting bored":
                s3_mc "Anytime you feel yourself getting bored, you can count on me."
                s3_li "I take it you don't mean for a game of Snap?"
                s3_li "Though I did play strip Snap once."
                s3_mc "How'd that go?"
                s3_li "I got very cold."
                s3_li "I'll definitely count on you if I'm at a loose end."
                s3_li "Or, y'know, anytime."
        
        s3_li "It's funny, normally I never stop moving. I think that's why I thought I might get bored."
        s3_li "But this is like a dream holiday."
        s3_li "If I was in London right now, it'd probably be raining."
        s3_li "What would you be up to if you weren't in the Villa?"

        # CHOICE
        menu:
            s3_mc "If I wasn't in the Villa, I'd be..."
            "Busy with work":
                s3_mc "I'd probably have my nose to the grindstone."
            "Chilling with my friends":
                s3_mc "Probably hanging out with my friends."
                s3_mc "Hopefully I wouldn't have my nose to the grindstone."
            "Watching Love Island":
                s3_mc "As if I could be doing anything else!"
                s3_mc "I'd be parked on my sofa watching you on Love Island."
                s3_li "And I bet you'd fancy me."

                # CHOICE
                menu:
                    thought "Tai thinks I'd fancy him if I saw him on TV..."
                    "I'd be jealous of whoever you were with":
                        s3_li "Aww, don't be jealous. I'd care about you, too."
                        s3_li "Not that the other person would be real."
                        s3_li "Anyway, I'm glad you'd be doing something fun with your summer."
                        s3_mc "Yeah, hopefully I wouldn't have my nose to the grindstone."
                    "Of course I would":
                        s3_mc "You're irresistible."
                        s3_li "Right back at you."
                        $ s3_mc.like(s3_li)
                        s3_li "I'm glad you'd be doing something fun with your summer."
                        s3_mc "Yeah, hopefully I wouldn't have my nose to the grindstone."
                    "But I wouldn't know you":
                        s3_mc "You're fit."
                        s3_li "Of course."
                        s3_li "But I wouldn't know you the way I do now. It's not the same."
                        "For a couple of moments, Tai searches for the right word."
                        $ s3_mc.like(s3_li)
                        s3_li "That's awesome."
                        s3_li "Anyway, I'm glad you'd be doing something fun with your summer."
                        s3_mc "Yeah, hopefully I wouldn't have my nose to the grindstone."
            
        s3_li "The what to the what-stone?"
        s3_li "I've never heard that before, say it again!"
        s3_mc "Nose to the grindstone!"
        s3_mc "It's when you're working really hard."
        s3_li "But where's the grindstone coming in?"
        s3_li "Maybe it's a stone you grind on, like a pole in a club."
        thought "Tai's thinking too much about this."

        # CHOICE
        menu:
            thought "How shall I distract him?"
            "Tickle him":
                # NEED TO FILL
                "EMPTY"
            "Give him a kiss":
                s3_mc "Hey, Tai. You're thinking too much."
                "Tai returns his attention to you just in time for you to lean close and kiss him on the forehead."
                "He laughs and strokes your hair back from your face."
                s3_li "You've got a point."
                $ s3_mc.like(s3_li)
            "Say 'grindstone' sexily":
                s3_mc "Hey, Tai. Over here."
                "Tai returns his attention to you, and you lean in very close to his ear."
                s3_mc "Grindstone."
                "Tai shivers."
                s3_li "Told you. Anything you say, boom! It's hot."

    elif s3_li == "ciaran":
        s3_li "Hey, [s3_name]?"
        s3_mc "Yeah?"
        s3_li "I was thinking where I want to take you when we're out of the Villa."
        s3_li "Like, on dates."
        s3_li "That's another thing I think about on long shifts. Potential date ideas for my perfect woman."

        # CHOICE
        menu:
            s3_mc "That's..."
            "Cheesy":
                # NEED TO FILL
                "EMPTY"
            "Accurate":
                # NEED TO FILL
                "EMPTY"
            "Cute":
                s3_mc "You really are a sweetheart, aren't you?"
                "Ciaran blushes and smiles."
                s3_li "I suppose."
                s3_li "Obviously I want to show you Waterford, but I also want to take you and Kerry to the beach."
                s3_li "Make a nice picnic, get one of those massive umbrellas."
                s3_li "Does that sound nice?"

                # CHOICE
                menu:
                    thought "Do I want to go to the beach with Ciaran?"
                    "I don't like the beach":
                        # NEED TO FILL
                        "EMPTY"
                    "Sounds perfect":
                        s3_li "Oh, good."
                        s3_li "We'll pencil it in, then."
                    "As long as it's somewhere sunny":
                        s3_mc "I'm thinking the Med or the Caribbean."
                        s3_li "Woah! Might be tricky with a dog and all, but I'm sure we can make it."
            
        s3_mc "So, you haven't asked me whether I still like you today."
        s3_li "Oh gosh, I forgot!"
        s3_li "Do you?! Please say yes."
        s3_mc "Yes!"
        s3_mc "It's nice. It's like you're starting to actually believe it now."
        s3_li "You're right. I didn't think about whether you'd want to come on the date with me. I just thought about where I'd want to take you."
        s3_li "Watch out, you're looking at the new and improved Ciaran!"
        s3_li "Any tips on how to use my new confidence? For good or evil?"

        # CHOICE
        menu:
            thought "What do I want Ciaran to do with his confidence?"
            "Act cocky":
                # NEED TO FILL
                "EMPTY"
            "Believe in your sauce":
                s3_mc "Have more faith in your writing!"
                s3_mc "The world needs to hear about Captain Kerry and her adventures with the smoking hot Ciaran-man."
                s3_li "Aw, [s3_name], that means so much to me."
                s3_mc "Besides, who else is going to fight evil for planet Earth?"
                s3_li "We must step up to the challenge!"
            "Graft on me":
                s3_mc "Show me your grafting skills."
                s3_li "You already know I'm terrible at that."
                s3_mc "New day, new you! C'mon, show me what you've got."
                s3_li "OK, er, let me think."
                "His brow furrows. He appears deep in thought."
                s3_li "Oh, I've got something."
                "He takes one of your hands in both of his."
                s3_li "[s3_name], I honestly think, with all sincerity, you are the most beautiful woman I've ever seen."
                "Your heart skips a beat."
                s3_li "How was that?"
                s3_mc "Uh... yeah, Ciaran, that was good."
                s3_mc "I'd say that's Ciaran-brand grafting."
                s3_li "Good!"
    
        s3_li "OK, I have a handle on it now, I think."
        s3_li "Ciaran-man is ready for action."
        s3_li "Anything else you want me to do?"

        # CHOICE
        menu:
            thought "Shall I make Ciaran do anything else?"
            "Nah":
                # NEED TO FILL
                "EMPTY"
            "Kiss me!":
                s3_mc "I want to see you kiss me for a change."
                s3_li "That's something I can handle..."
                "He moves closer to you, slowly, with a sly smile."
                "Gently, he puts both hands on your waist, and moves his lips so they're inches from yours."
                "He laughs and kisses you fiercely, his grip on your waist tightening. You run your hands into his hair and let him take control of the kiss."
                "You are left breathless, staring at him as he grins mischievously."
                s3_mc "OK. You have to do that more often."
                s3_li "Agreed."

        s3_li "You know, [s3_name], you make me feel so different."
        s3_li "It's a really good different."
        s3_li "I'm really glad I met you."
        s3_mc "I'm glad, too."

    elif s3_li == "Yasmin":
        s3_li "So... do you remember what I said, about how I never want to be in a long distance relationship?"
        s3_mc "Yeah?"
        "She slowly strokes her thumb across the back of your hand."
        s3_li "I was just wondering how you feel about all that."
        s3_li "Have you ever tried it?"

        # CHOICE
        menu:
            thought "Have I ever been in a long distance relationship?"
            "Yeah, it worked for me":
                # NEED TO FILL
                "EMPTY"
            "Yes, but I didn't like it":
                # NEED TO FILL
                "EMPTY"
            "Nope, I've never tried it":
                s3_li "Do you think you ever would?"

                # CHOICE
                menu:
                    thought "Would I ever be in a long distance relationship?"
                    "No, I wouldn't like it":
                        # NEED TO FILL
                        "EMPTY"
                    "Sure, I'd be open to it":
                        s3_li "Noted."
                    "Only if it was with you":
                        s3_li "Aw, babe."
                        $ s3_mc.like(s3_li)
        
        s3_li "I only ask because I was wondering..."
        s3_li "How you and I might potentially work outside the Villa. You know, if we decided that was going to be a thing."
        s3_li "We might leave here and suddenly find ourselves living in totally different parts of the world."

        # CHOICE
        menu:
            thought "If me and Yasmin ended up living far apart..."
            "You'd have to move closer to me":
                # NEED TO FILL
                "EMPTY"
            "We'd make it work long distance":
                # NEED TO FILL
                "EMPTY"
            "I'd move to be closer to you":
                s3_mc "Wherever you go, I can go too."
                s3_li "Babe..."
                $ s3_mc.like(s3_li)
                s3_li "You don't know how much that means to me."
        
        s3_li "Your presence is intoxicating. The way you make me feel when you're here beside me..."
        s3_li "I don't want to lose that."
        s3_li "And if we lived apart, I wouldn't be able to do this..."
        "She cups your face in her hands and smiles."

        # CHOICE
        menu:
            thought "Yasmin's going in for a kiss"
            "Turn your face away":
                # NEED TO FILL
                "EMPTY"
            "Keep it short and sweet":
                "You close your eyes as she presses a tender kiss to your mouth."
                "You enjoy the feeling of her lips against yours for a moment, before pulling back."
            "Make it last":
                "You sink into a slow, deep kiss."
                $ s3_mc.like(s3_li)
                "Yasmin strokes your hair. Her hand travels the length of your neck before slipping lower, down your back."
                "Finally, she rests her forehead against yours and gazes into your eyes."
        
        s3_li "Let's just say..."
        s3_li "There's a lot of things I'd miss if you were far away."
    
    s3_mc "Are we the only ones still in bed?"
    "You hear a rustle of sheets."
    s3_other_f "Nope, you're not alone."
    "[s3_other_f] gets out of her bed and looks over briefly."
    s3_li "Oops. Sorry, babe."
    "[s3_li] whispers in your ear."
    s3_li "I totally didn't notice that [s3_other_f] was here."
    "[he_she!c] bites [his_her] lip as [he_she] gets up from the bed."
    s3_li "I'm going for a shower."
    "[s3_li] whispers in your ear as [he_she] leans over the side of the bed to grab a towel."
    s3_li "You can come and join me if you want."
    "[he_she!c] gets up and goes to the bathroom, a towel over [his_her] shoulder."

    # CHOICE
    menu:
        thought "Maybe I should follow [s3_li] for that sexy shower..."
        "Heck yeah I want to shower with [s3_li]":
            $ s3e9p1_shower = True
            call s3e9p1_shower from _call_s3e9p1_shower
        "Nah, I'll just go and get changed":
            "You get out of bed and walk over the dressing room."

    scene s3-dressing-room with dissolve
    $ new_scene()

    thought "Hmm..."
    thought "I don't know what today will bring at all."
    thought "I better go out with a fierce look so I'm ready for anything and everything."
    
    # Outfit change to swimwear

    $ outfit = "swim"
    call customize_outfit from _call_customize_outfit_14
# thought "Oh, I love this thing."
# thought "Oh this is the real deal."
# thought "I look great!"
# You shrug.
# thought "This will have to do, I suppose."
    if s3e9p1_shower == False:
        "[s3_li] walks in, towel drying [his_her] hair."
        s3_mc "Nice shower?"
        s3_li "It would have been better with you in it."
    else:
        s3_li "Clean now, babe?"
        "[s3_li] winks at you, towel drying [his_her] hair."
        s3_mc "Totally."
# Liona "I love it when you wear that, by the way."
# s3_mc "What, this old thing?"
# Liona "Yeah, it's gorgeous."
# Liona "You look gorgeous in that, by the way. (you get 🤩 with LI)"
# s3_mc "Aw, thanks hun!"
# Liona "You look great in anything, obviously. But you'd look even better in nothing, I think."
    "Your stomach rumbles."
    s3_li "Hungry?"
    s3_mc "Starving."
    s3_li "You go get yourself something to eat while I sort myself out."
    s3_mc "Oh, OK. Sure."
    "You head downstairs to the kitchen for breakfast."

    scene s3-kitchen-day with dissolve
    $ new_scene()
    "You walk down into the kitchen. [s3_bff] is making breakfast."
    s3_bff "Cup of something, [s3_name]?"
    $ pronouns(s3_bff)
    # CHOICE
    menu:
        thought "I want a cup of..."
        "Tea":
            s3_bff "One tea coming up."
        "Coffee":
            s3_bff "One coffee coming up."
        "Wheatgrass smoothie":
            s3_bff "A what?"
            s3_mc "A wheatgrass smoothie."
            s3_mc "Don't you know what a wheatgrass smoothie is?"
            s3_mc "They were all the rage last summer."
            s3_bff "Really? OK, I'll see if we have any."
            "[s3_bff] crouches down and searches through a cupboard, confusion still etched around [his_her] face."
            s3_bff "Hmm, I don't think we have that here."

    $ entering("ciaran")
    "Ciaran comes over clutching a mug."
    if s3_li == "Ciaran":
        "Ciaran blushes when he sees you."
        ciaran "Hey again."
        s3_mc "Hey."
    ciaran "Can I get some of that water once it's boiled, please?"
    s3_bff "Sure. What are you after?"
    ciaran "Cuppa tea, please."
    s3_bff "I'll bring it over to you."
    "Ciaran smiles."
    ciaran "Grand."
    $ leaving("ciaran")
    "[s3_bff] puts the kettle on to boil."

    if s3_bff == "Elladine":
        s3_bff "So, babes. What's your go-to breakfast?"

        # CHOICE
        menu:
            thought "Elladine wants to know my go-to breakfast..."
            "Cereal. All day, every day":
                # NEED TO FILL
                "EMPTY"
            "I like a continental breakfast":
                # NEED TO FILL
                "EMPTY"
            "Most days I just have a quick snack":
                # NEED TO FILL
                "EMPTY"
            "It's a fry-up, obvs":
                s3_bff "Knew, you were my friend for a reason."
                s3_bff "Can't be dealing with anyone who badmouths a full English."
                s3_bff "And I make the best one around."
                s3_bff "Important questions time. Do you have the black pudding?"

                # CHOICE
                menu:
                    thought "Do I take pudding with my fry-ups?"
                    "Obviously":
                        pass
                    "Never":
                        pass
                    "Only when I'm feeling adventurous":
                        pass
                s3_bff "Sound. And your opinion on hash browns?"

                # CHOICE
                menu:
                    thought "Hash browns in a fry-up?"
                    "Hate 'em":
                        # NEED TO FILL
                        "EMTPY"
                    "Love 'em, but not in a fry up":
                        # NEED TO FILL
                        "EMPTY"
                    "Love 'em":
                        s3_bff "Correct choice."
        
        s3_bff "Alright, what about a drink? Orange juice, tea, or something else?"

        # CHOICE
        menu:
            thought "What drink do I have with my fry-up?"
            "Milk":
                s3_bff "Not a bad choice."
                s3_bff "But it's not as good as tea. It's the best thing for early mornings."
            "Tea":
                s3_bff "Ding ding!"
                s3_bff "Not sure how anyone can drink anything else, to be honest."
            "Orange juice":
                s3_bff "Not a bad choice."
                s3_bff "But it's not as good as tea. It's the best thing for early mornings."
        
        s3_bff "Maybe it's just in my blood? I like to joke about that sometimes..."
        s3_bff "What thing do Brits and Iranians have most in common?"
        s3_mc "I don't know, what?"
        s3_bff "They both love tea way too much."
        s3_mc "I never realised you had such strong opinions on fry-ups."
        s3_bff "Yeah, I sound like Bill, now, don't I?"
        
        s3_bff "Alright, since I'm here grilling you already about your morning routine, how about another question?"
        s3_mc "Go for it."
        s3_bff "Morning sex?"
        s3_mc "Woah. That took a turn."
        s3_bff "Sorry. Guess I have sausage on my brain."
        s3_mc "Was that even a question?"
        s3_bff "I mean, what do you think of it?"
        s3_bff "When you've literally just woken up. Is it fun? Or just good in theory?"
        s3_mc "You've never done it?"
        s3_bff "Um, no. I just sort of figured... well, there's all that bad breath, and you're all sweaty from the night..."
        s3_bff "At least I usually am. First thing I have to do in the morning is shower."
        s3_bff "I can't do anything else until then."
        s3_bff "So... is it good?"
        s3_bff "Nicky mentioned it, you see, so..."

        # CHOICE
        menu:
            thought "What do I think of morning sex?"
            "You're right, it's just icky":
                # NEED TO FILL
                "EMPTY"
            "I've never really done it either":
                s3_mc "Sorry I can't help you! I'd not really thought about it until now, but I guess I'm just as new to it as you."
                s3_mc "Guess the only way for us to find out is to try!"
                s3_bff "Guess you're right."
                s3_bff "I'll, uh..."
                s3_bff "...I'll float the idea by him, I suppose."
            "I love it":
                s3_mc "Honestly, babe. If Nicky wants to do it, and you're feeling adventurous, go for it."
                s3_mc "There's something so primal and basic about it."
                s3_mc "And what's hotter than someone waking up and their first thought being what they could do with you."
                s3_bff "Yeah... when you put it like that."
                s3_bff "I think, well, I'll talk to Nicky about it."
        
        s3_bff "Thanks, hun."
        s3_mc "No problem!"
        "The kettle clicks as it finishes boiling. Elladine pours you a cup of tea."
        s3_bff "OK, one more?"
        s3_mc "Sure."
        s3_bff "Early bird or night owl?"
        s3_mc "Ooh, good one!"

        # CHOICE
        menu:
            thought "Am I an early bird or night owl?"
            "Early bird":
                s3_mc "Gotta seize the day, early bird catches the worm, and all that jazz."
                s3_bff "And there's more than a few worms to catch in the Villa, right?"
                s3_mc "Elladine!"
                s3_bff "What? It's true isn't it?"
                s3_bff "Anyway I'm the same."
            "Night owl":
                s3_bff "Ah. I always think there's something romantic about that."
                s3_bff "Like, in movies the night owls are all those tortured creative souls who can only work by the moonlight."
                s3_bff "As cool as that sounds, I can't hack it."
        
        s3_bff "I have to be in bed early or I start falling asleep."
        s3_bff "My friends used to always joke about me falling asleep on the dance floor."
        s3_bff "I just get lost in the music sometimes!"
        s3_mc "Just 'resting your eyes', right?"
        s3_bff "Exactly."

    elif s3_bff == "Genevieve":
        s3_bff "You know, I think things are going to be different with Seb."
        s3_bff "Compared to my past relationships, that is."
        s3_mc "How so?"
        s3_bff "I'm going to explain it in kind of a weird way, but stick with me..."
        s3_bff "So, I read this book called 'Creating Your Feminine Breeze'. It's about how women are always the caregivers and men try to take advantage of that."
        s3_bff "Basically women are goddesses, and men are mortals trying to suck out our power for their own gain."
        s3_bff "Does that make sense?"

        # CHOICE
        menu:
            thought "Do I understand what Viv is saying?"
            "No":
                s3_mc "They're trying to suck what out of us?!"
                s3_bff "No! Not physically. Emotionally."
            "Yes":
                s3_mc "Goddesses are naturally generous, and it intimidates mortals."
                s3_bff "Exactly!"
            "I've read that book too!":
                s3_mc "It changed my life."
                s3_mc "Goddesses are naturally generous, and it intimidates mortals."
                s3_bff "Exactly!"
                
        s3_bff "It's like, I went out with a guy who told me he was going to be an entrepreneur."
        s3_bff "It impressed me at first, but then I found out that 'being an entrepreneur' largely involved him playing Duty Calls."
        s3_bff "I paid that guy's rent for almost a year. Plus every bill when we went out for dinner so he wouldn't have to wash dishes."
        s3_bff "All while getting my PhD."
        s3_bff "I dumped him eventually, but not soon enough."
        s3_bff "And that book helped me realise that if a mortal wants to be with a goddess, he has to help her shine."
        s3_mc "Seb's definitely that guy."
        s3_bff "I think so too."
        s3_bff "I'm not too proud to admit I've been taken advantage of before."

        # CHOICE
        menu:
            thought "Viv's been taken advantage of..."
            "That's horrible":
                s3_bff "Yeah, it is."
            "It's cos you're so caring":
                s3_bff "Aw, that's nice of you to say."
                s3_bff "You're probably right. Not a lot of people would pay someone else's rent, but  I suppose he targeted me cos he knew I would."
            "Me too":
                s3_bff "Babe, I'm sorry."
                s3_mc "Thanks."
        
        "She holds up her fist and bumps yours."
        s3_bff "To new beginnings!"

    elif s3_bff == "Nicky":
        s3_bff "Here's something."
        s3_bff "I might have a proposal for Seb. But I wanna get your take on it before I ask him."

        # CHOICE
        menu:
            thought "A 'proposal' for Seb?"
            "You're going to rob a bank together?":
                s3_bff "Hmm. Someday, maybe."
                s3_mc "Do you think he'd be any good?"
                s3_bff "You never know. I think he'd be good at moving silently, so maybe he can be the one who does the actual stealing."
                s3_bff "I'm the ringleader and the planner, obviously."
                s3_bff "And you can be the one who distracts the guards with your womanly charm."
            "You're going to ask him to marry you?":
                s3_bff "Ha, not yet. He doesn't seem like the marrying sort."
                s3_mc "No offence, but I don't think you're his type, either."
                s3_bff "Tragic but true."
                s3_bff "Well, you never know. Maybe someday he'll get married in a graveyard or something and live gloomily ever after."
                s3_bff "He could have a bat for the officiant."
            "You're going to buy out his shop?":
                s3_bff "God, no. Can you imagine?"
                s3_bff "I'd have to shut it down and turn it into a shoe shop or something."
                s3_bff "I don't understand how he stays in business. Who's buying records anymore? And from Seb, of all people?"
                s3_bff "Can you imagine his customer service? How does he do it?"
                s3_mc "I think he said the shop has a little café as part of it, so it's not just records."
                s3_mc "But I know what you mean."

        s3_mc "What does this have to do with your proposal?"
        s3_bff "Oh, right, yeah. The thing."
        s3_bff "I was thinking about asking Seb to do a podcast with me, once all this is over."
        s3_bff "'Cause he actually really knows his stuff when it comes to music, and obviously I take an interest, 'cause it's my job."
        s3_bff "And we could talk about our favourite artists, do reviews, that kind of thing."
        s3_bff "What d'you think? Would anybody listen to that?"

        # CHOICE
        menu:
            thought "Nicky wants to ask Seb to host a podcast with him..."
            "He'll never agree to that":
                # NEED TO FILL
                "EMPTY"
            "Yeah, that's a great idea!":
                s3_mc "You guys are both smart, and you're funny together, too. I think it'll be a great combination."
                s3_bff "Cheers! I'm really glad you think so."
            "If you're sure he's up to it...":
                s3_mc "Talking to people isn't exactly Seb's favourite thing in the world."
                s3_mc "I know he's come out of his shell a bit since we've been here, but it's still a big ask."
                s3_bff "True, but don't forget, he did apply to come on Love Island. And he's done well so far."
                s3_bff "After this, I reckon a little podcast will be no trouble."
        
        s3_bff "To be honest, and don't tell him this..."
        s3_bff "....Part of the reason I want to ask him is so we have an excuse to stay in touch after Love Island."
        s3_bff "I don't want him to just retreat into this cave when it ends and none of us ever see him again, y'know?"

        # CHOICE
        menu:
            thought "Nicky's doing this as an excuse to stay friends with Seb..."
            "That's silly, you should just tell him you want to hang out":
                # NEED TO FILL
                "EMPTY"
            "Aw, that's actually pretty cute":
                s3_mc "I won't tell him. I think it might be too much sweetness for him to handle all at once."
                s3_bff "Yeah, that's my thinking."
                s3_bff "Friendship is still new to him. He just needs time to get used to it."
            "Then why aren't you asking me to host a podcast with you?":
                s3_bff "'Cause you're not like Seb. I don't need to trick you into hanging out with me."
                s3_mc "Well, maybe, but you should at least be trying!"
        
        "Nicky grins."

    elif s3_bff == "Seb":
        s3_bff "Hey, [s3_name]. Have you ever made a mixtape for someone you fancied?"
        s3_mc "A 'mixtape'?"
        s3_bff "You know what I mean. A playlist."
        
        # CHOICE
        menu:
            thought "Have I ever made a playlist for someone I fancied?"
            "Come on, I'm not that melty":
                # NEED TO FILL
                "EMPTY"
            "Yeah, it's a great way to flirt":
                s3_mc "I love it. So romantic."
                s3_bff "Yes! Me too."
            "No, but it's a cute idea":
                s3_mc "I think I'd just melt if someone did that for me."
                s3_bff "Oh, good. I wasn't sure if any girls actually liked it."
                s3_mc "Tried it before, have you?"
                s3_bff "Only a lot."
                s3_mc "Does it work?"
                s3_bff "...Sometimes."
        
        s3_bff "It's like a reflex. When I really like a girl, I just have to start making a playlist for her."
        s3_bff "With all the songs we've talked about together, or songs I think she'll like, or songs that remind me of her."
        s3_bff "I'm thinking about making one for Viv."
        s3_bff "Obvs. I have to do it in my head until I get home."
        s3_bff "And I know it's too soon! I know that. But I can't help it."
        s3_bff "I can't stop thinking of things I could do to try and make her smile."
        s3_bff "Her smile is just... mate, it goes right through me."

        # CHOICE
        menu:
            thought "Seb's going on about Viv..."
            "You two are adorable":
                s3_mc "You make such a cute couple."
                s3_bff "We're not... I mean, we're not a proper couple. Like, officially."
                s3_bff "I think."
            "Come on, give it a rest":
                s3_mc "Dude, I don't want this friendship to turn into you banging on about how great your girlfriend is."
                s3_bff "She's not my girlfriend!"
            "Have you told her this?":
                s3_bff "Told her what?"
                s3_mc "Uh, that you're in love with her?"
                s3_bff "What? No I'm not!"
        
        s3_mc "Well, it seems like you're already halfway there, at least."
        s3_mc "Just a few days ago you told me you 'never fall for girls like her'."
        s3_mc "And now you're talking about her like you've fallen head over heels."
        s3_bff "You're right. I mean, I always wished I could be with a girl like that."
        s3_bff "And now I think I've finally done it."
        s3_bff "I've fallen for someone nice who actually likes me back."

        # CHOICE
        menu:
            thought "Seb's feeling good about falling for Genevieve..."
            "Alright, now just try not to mess it up":
                # NEED TO FILL
                "EMPTY"
            "I'm really happy for you":
                s3_mc "I think you're gonna be good for each other."
                s3_bff "Thanks, mate."
            "I wouldn't get too excited yet":
                s3_mc "Look, I know being happy is still new and exciting for you, but don't get carried away."
                s3_mc "You haven't actually known each other that long. You don't know how things will be outside the Villa."
                s3_bff "You're right. I'll try to keep my feet on the ground."

        s3_bff "I'm finally starting to feel like I do belong here after all."
        s3_bff "Actually, I think that chat we had the other day really helped."
        s3_bff "It turns out nice things happen sometimes when you're not always on the lookout for the next disaster."
        s3_mc "Who knew?"
        "Seb grins."

    s3_bff "So, how are you feeling about last night?"

    # CHOICE
    menu:
        thought "How do I feel about getting with [s3_li]?"
        "[s3_li] is punching up, to be honest":
            "[s3_bff] frowns."
            s3_bff "I don't think that's very fair."
            s3_bff "You're both, like, solid tens for sure."
            "You shrug."
            s3_mc "If you say so."
            "[s3_bff] looks awkwardly at the ground."
        "I couldn't be happier":
            "[s3_bff] smiles."
            s3_bff "You two look great together."
            if s3_li == "Harry" and s3_bff == "Genevieve":
                s3_bff "Oh, and [s3_name], I really wanted to say that I'm happy for you and Harry."
                s3_bff "So don't worry about me."
                s3_bff "In case you were."
                "Genevieve smiles at you."
                s3_bff "And I'm actually kind of excited to see where this whole thing with Seb goes."
            else:    
                s3_bff "I'm so, like, happy for you both."
        "It was fate, nothing could stop us":
            $ s3e9p1_fate = True
            s3_bff "Ha, yeah, I guess you're right!"
            if s3_li == "Harry" and s3_bff == "Genevieve":
                s3_bff "Oh, and [s3_name], I really wanted to say that I'm happy for you and Harry."
                s3_bff "So don't worry about me."
                s3_bff "In case you were."
                "Genevieve smiles at you."
                s3_bff "And I'm actually kind of excited to see where this whole thing with Seb goes."
            else:    
                s3_bff "I'm so, like, happy for you both."
    
    s3_bff "Your speech was amazing, by the way."

    # CHOICE
    menu:
        thought "[s3_bff] liked my recoupling speech."
        "Yay! I worked really hard on it":
            s3_bff "You could tell!"
        "Really? It was totally improvised":
            if s3_bff == "Genevieve" or s3_bff == "Elladine":
                s3_bff "Sometimes improvisation gives us the most genuine words."
            else:
                s3_bff "That's well brave. I couldn't have done that."
        "Thanks, it came from the bottom of my heart":
            $ s3e9p1_bottom_of_heart = True
            "[s3_bff] starts to sniff the air."
            s3_bff "Can you smell that?"
            "[he_she!c] sniffs your shoulder."
            s3_bff "Smells like cheese."
            s3_mc "Very funny."
            s3_bff "I'm kidding. You're both class."

    "The kettle stops boiling."
    s3_bff "So..."
    "[s3_bff] pours out the water into some mugs."
    s3_mc "So?"
    s3_bff "It seems like things are all good for you two."
    if s3e9p1_fate == True and s3e9p1_bottom_of_heart == True:
        s3_bff "Yeah, from everything you've said, you seem really smitten."
    if s3_bff == "Genevieve":
        "Genevieve pours out the hot water."
    if s3e9p1_shower_bits == True:
        if s3_bff == "Genevieve" or s3_bff == "Elladine":
            s3_bff "Did I hear that mouse in the bathroom earlier?"
            s3_mc "Um..."
            s3_bff "I definitely heard some squeaking."
            s3_mc "No, I didn't see any mice."
            s3_bff "Huh, I thought I could hear it when you and [s3_li] were in the bathroom."
            s3_bff "I must have pool water in my ear or something."
        else:
            s3_bff "And it certainly sounded like you two were having fun in the shower."
            s3_mc "You heard us?"
            s3_bff "I know a sexy noise when I hear one."
            "You blush."
    s3_bff "But, like, between you and me..."
    s3_bff "Do you think you'll be loyal with [s3_li] for, like, the rest of the time in the Villa?"

    # CHOICE
    menu:
        thought "Will I be loyal with [s3_li]?"
        "Yeah, I want to be loyal":
            s3_bff "That's cool."
            s3_bff "But seriously."
        "My head could turn":
            s3_bff "Really?"
            s3_mc "You never know what will happen in this place."
            "[s3_bff] sighs."
            s3_bff "Yeah, I guess you're right."
        "We will rule the land together forever":
            s3_bff "I meant loyal, not royal."
            s3_mc "I know."
            s3_mc "And we will reign as the best, most royally loyal couple ever."
            "[s3_bff] laughs, spitting out [his_her] tea a little."
            s3_bff "You're so funny."
            s3_bff "But seriously."

    $ pronouns(s3_li)
    s3_bff "Have you had a chat with [s3_li] about, like, loyalty and stuff?"
    s3_mc "Nope, not exactly..."
    s3_bff "Hmm..."
    s3_bff "Do you think [he_she]'s a loyal person?"

    # CHOICE
    menu:
        thought "Do I think [s3_li] is loyal?"
        "Yeah, I think we're pretty solid":
            s3_bff "Well, that's good."
            s3_bff "I don't want you to worry or anything."
        "[he_she!c]'s [his_her] own person, I'm not forcing anything":
            s3_bff "That's a good headspace to be in."
            s3_bff "I don't want you to worry or anything."
        "If [he_she] knows what's good for [him_her] then [he_she] will be":
            s3_bff "Don't you think that's, like, a bit threatening?"
            "You sigh."
            s3_mc "I guess..."
            s3_bff "You don't want to come across, like, possessive."
            s3_bff "I don't want you to worry or anything."

    "[s3_bff] grabs a spoon from the drawer and starts to stir the tea."
    s3_bff "But it's good to keep an eye on these things."
    "The sound of the teaspoon hitting the china rings across the kitchen."
    s3_mc "Um, [s3_bff]..."
    s3_mc "What are you saying?"
    s3_bff "I'm not insinuating anything, [s3_name]."
    s3_mc "Has [he_she] said something about me to you?"
    s3_bff "I'm just thinking out loud."
    s3_bff "Ignore me, [s3_name]."
    "[s3_bff] picks up the mugs."
    s3_bff "I'm sure it'll be fine."
    s3_bff "Ah, phew, it's Ciaran."
    "[s3_bff] glances at you, looking a little flustered."
    s3_bff "Tea's ready."
    ciaran "Ta, [s3_bff]."
    "He blows on it and then takes an indulgent sip."
    ciaran "That's cracking, cheers."
    "Some other Islanders saunter into the kitchen."
    thought "What if [s3_li] isn't as loyal as I thought?"
    "[s3_li] heads over to the fridge."
    thought "Could [s3_bff] be right?"
    if s3_li == "Ciaran":
        ciaran "I am in such a snacking mood today."
    else:
        s3_li "I am in such a snacking mood today."
    thought "I guess that's [his_her] priority right now."
    thought "Food."
    if s3e9p1_shower_bits == True and (s3_bff == "Seb" or s3_bff == "Nicky") and (s3_li == "Harry" or s3_li == "Camilo" or s3_li == "Tai"):
        s3_bff "Did you hear a mouse earlier, [s3_li]? I could hear, like, weird noises coming from the bathroom earlier."
        s3_li "From the bathroom?"
        "[s3_li] laughs."
        s3_li "Oh, we were just cleaning the tiles, like, really hard."
        s3_bff "Aw, that's nice of you."
    s3_other_f "What's going on in here?"
    yasmin "It's snack time."
# yasmin "And MC as usual is looking like a snack."
# s3_mc "Cheers, Yasmin."
    genevieve "But it's still, like, the morning, isn't it?"
    s3_other_f "I feel like it's basically brunch now."
    "Elladine claps her hands enthusiastically."
    elladine "Oh, I am so going to have a good brunch."
    s3_other_f "It's a marketing tactic, babe."
    s3_other_f "Don't fall for it."
    ciaran "What on earth is brunch?"
    tai "How can you not know what brunch is, Ciaran?"

    # CHOICE
    menu:
        thought "Ciaran asked what brunch is..."
        "It's a late morning meal":
            pass
        "It's a ploy to make you spend more money":
            pass
        "It's when you have a brilliant hunch about something":
            pass
        
    tai "I'll make you the best brunch of your life, Ciaran."
    tai "You just wait and see."
    tai "I am a master brunch-maker."
    s3_other_m "BBQ king and brunch expert..."
    s3_other_m "Is there no limit to your skills?"
    "Tai crouches down and starts to rummage in a cupboard."
    tai "Nope."
    tai "It's all about the presentation, young bruncher."
    ciaran "Oh, really?"
    tai "It sure is."
    if s3_li == "Yasmin" or s3_li == "AJ":
        "He brings out a bag of baps and piles them on the counter."
        tai "Baps?"
        "Ciaran smiles."
        ciaran "I love them."
        tai "I know."
        tai "Prepare for the best bap of your life!"
        tai "I need avocados."
    "He gets out a couple of avocados from the fridge."
    ciaran "So what's the secret?"
    tai "As long as it looks good you can't go wrong."
    "Tai mushes up some avocado with raw egg."
    s3_other_m "You're meant to at least boil the egg first, Tai."
    if s3_other_m == "Bill":
        s3_other_m "Raw egg is, like, worse than celery."
        s3_other_m "Did you know that an uncooked egg doesn't give you, like, barely any of the protein a cooked one would?"
    else:
        s3_other_m "I'm all for experimenting in the kitchen, but this is, like, actually dangerous."
    tai "Nonsense."
    "Tai continues to mash the sticky green mixture."
    "He packs it into some baps and garnishes it with a leaf of basil."
    s3_other_m "Looks like the boogey monster sneezed on the baps."
    tai "Nah, mate. You wouldn't know good food if it ate you."
    "[s3_other_m] sighs."
    s3_other_m "I'm not even going to dignify that with a response."
    s3_other_f "Yeah, sorry hun, that's inedible."
    s3_other_f "You can't really eat raw eggs."

    # CHOICE
    menu:
        thought "Raw egg and avocado in a bap..."
        "You've ruined a good bap":
            tai sad "I didn't mean to..."
            $ s3_mc.dislike("Tai")
        "I wouldn't eat that even if you paid me":
            tai sad "Oh..."
            $ s3_mc.dislike("Tai")
        "Sounds like a good hair mousse":
            s3_other_f "That's actually a really good shout."
            "Tai sighs."
            tai sad "Yeah..."
            "He pokes at the bap. Green stuff oozes out."
    
    if s3_li != "Yasmin" and s3_li != "AJ":
        tai "Think I got a bit carried away."
        "Tai dejectedly scrapes the bap into the bin."
    else:
        tai "Think I got a bit carried away."
        tai "Sorry Ciaran..."
        ciaran "It's the thought that counts. Don't worry about it."
        ciaran "We can get brunch in my hometown together when we get out if you'd like."
        "Tai smiles, scraping the bap in the bin."
        tai "Yeah, I'd like that."
    if s3_li == "Tai":
        tai "I'm still hungry though..."
    else:
        s3_li "I'm still hungry though..."
    "A text rings out."
    s3_bff "Oh."
    s3_bff "Hold that bap."
    s3_bff "I got a text!"
    "Everyone crowds around [s3_bff]'s screen."
    text "Islanders, put your best foot forward because two new Islanders will be arriving sometime today. #twosaparty #thirteenisacrowd"
    if s3_li == "Tai":
        tai "Ooh, new people!"
        tai "Exciting..."
    else:
        s3_li "Ooh, new people!"
        s3_li "Exciting..."
    s3_bff "New Islanders?"
    "[s3_bff] looks at you in shock."

    # CHOICE
    menu:
        thought "New Islanders are coming into the Villa!"
        "Yay! That means more friends":
            thought "It's always great to meet new people!"
            thought "I wonder if [s3_li] will just see them like a friend though..."
        "I hope [s3_li]'s head doesn't turn...":
            thought "I'd hate to lose [him_her] now!"
        "I hope they sweep me off my feet":
            thought "[s3_li] is old news."
            thought "I'm ready to be, like, properly swept off my feet."
            "You glance over at [s3_li]."
            "[he_she!c]'s smiling at you, unaware of your thoughts."
    
    if s3_other_m == s3_li:
        s3_li "I wonder how they're going to arrive."
    else:
        s3_other_m "I wonder how they're going to arrive."
    genevieve "Giant suitcase?"
    elladine "Forget how."
    elladine "When are they going to arrive?"
    elladine "And who are they going to break up?"

    scene sand with dissolve
    $ on_screen = []
    
    "Ah, Elladine."
    "You know what they say?"
    "The more..."
    "The merrier."
    "Or maybe it should be messier."
    "Can someone please get the Islanders to clean up that dressing room?"
    "I can see a mug that is wearing a green fuzzy jacket."
    "Not that my shed is any better..."
    "It gets pretty damp in here."
    "Coming up..."
    "Two new Islanders are on the way into the Villa."
    aj "This is the whole point of being here, to meet new people!"
    $ leaving("aj")
    "And it gets hard finding space to fit them all in!"
    harry "What if the only space available is a cupboard?"
    $ leaving("harry")
    "My hut is strictly off limits until I sort out this damp problem."

    jump s3e9p2
    return


label s3e9p1_shower:
    scene s3-bedroom-day with dissolve
    $ new_scene()
    
    "You leap out of the bed and rush over to the bathroom."
    s3_mc "Let me get my steam on..."
    thought "I was so excited I forgot my towel!"
    "[s3_other_f] laughs."
    s3_other_f "Oh, [s3_name]..."
    "You grab a towel and head out to the bathroom."

    scene s3-shower with dissolve
    $ new_scene()
    
    "[s3_li] is already in the shower. A pile of [his_her] clothes are on the side."
    "The steam from the hot water rises around [his_her] body."
    s3_li "Is that you, [s3_name]?"
    s3_mc "Sure is, babe."
    s3_li "Come on in."
    "You slip out of your clothes and get into the shower."
    if s3_li == "Ciaran" or s3_li == "Tai" or s3_li == "Camilo" or s3_li == "AJ":
        "[s3_li] turns around stroking a large pile of white foamy soap in [his_her] arms."
        s3_li "I've been expecting you."
        s3_mc "I thought evil villains wore a grey smock, not..."
        "You look [s3_li] up and down."
        s3_mc "Absolutely nothing."
        "[s3_li] winks and whispers."
        s3_li "I'm wearing an invisible cloak."
        s3_mc "I can see that."
        "[he_she!c] laughs and splashes you gently with foam."
    s3_li "Thanks for joining me, babe."
    s3_mc "No sweat."
    "[he_she!c] starts to wash [his_her] body with soap."
    s3_mc "Literally."

    # CHOICE
    menu:
        thought "I should..."
        "Help [s3_li] wash [him_her]self":
            "You put some soap in your hand and give [s3_li] a back massage."
            s3_li "Oh, that feels well nice." #(you get 😏 with LI)
            s3_li "You're good with your hands."
        "Make loads of soapy bubbles":
            "You squeeze a bit of soap in your palms, cup your hands, and blow."
            "Large iridescent bubbles float around you both."
            "[s3_li] jumps up to catch one of the bubbles in [his_her] hand."
            s3_mc "Beautiful, huh?"
            s3_li "Yeah."
        "Give [s3_li] a funny hair style": #(AJ+Yasmin missing)
            "You put some soap in your hands and rub it into [s3_li]'s hair."
            if s3_li == "Tai":
                "His shoulders visibly relax." #(you get 😂 with Tai)
                s3_li "I actually love my hair being played with."
            if s3_li == "Bill" or s3_li == "Harry" or s3_li == "Tai" or s3_li == "Camilo" or s3_li == "Ciaran":
                "You fashion his hair into a spikey mess."        
            if s3_li == "Tai" or s3_li == "Camilo":
                "[s3_li] grins at you while putting soap in your hair and giving you the same spiked up look."
                s3_li "Perfection."
            elif s3_li == "Bill" or s3_li == "Harry" or s3_li == "Ciaran":
                s3_li "Not going to lie, back in the day that's what my hair used to look like."
            "You both fall about laughing and rinse away your masterpiece." #(you get 😂 with LI)
        
    "The warm water rolls off [s3_li]'s body."
    "[he_she!c] looks hotter than ever."
    s3_li "You know what the best thing about having a shower together is?"

    # CHOICE
    menu:
        thought "What's the best thing about having a shower with [s3_li]?"
        "I really needed a shower":
            # NEED TO FILL
            "EMPTY"
        "We can get some sexy alone time":
            s3_li "Wow, I was thinking it was good for the environment."
            s3_li "Also it's always what they do in spy movies so, like, we can be sure."
            s3_li "But I like your answer too."
        "It's good for environment":
            s3_li "Ding, ding, ding."
            s3_li "We have a winner."
            "[s3_li] winks."
            s3_li "It feels good to get hot and heavy for the sake of the planet."
    
    "You both rinse the shampoo off your hair, taking it in turns to get the best angle under the powerful shower."
    s3_mc "It sure is steamy in here."
    s3_li "Yeah..."
    if s3_li == "Ciaran" or s3_li == "Tai":
        "[s3_li] blushes a little."
    else:
        s3_li "Maybe we can make it a little more steamy..."
    
    # CHOICE
    menu:
        thought "I should..."
        "Splash [him_her]":
            "You flick water at [s3_li]."
            s3_li "Is that, like, a sexy move or something?"
            s3_mc "No, I'm just splashing you."
            s3_li "Oh! My bad."
            "[s3_li] quickly splashes you back."
        "Kiss [him_her]":
            "You lean in to [s3_li] and kiss [his_her] lips."
            "[he_she!c] pulls you in closer so your wet bodies are almost touching."
    
    "[he_she!c] turns around and lets the water spray into [his_her] face."
    "The water trickles down the nape of [his_her] neck."
    "It's just you and [s3_li]."
    s3_li "We don't get many alone moments in that bedroom, do we?"
    s3_mc "Nope, not really."

    # CHOICE
    menu:
        thought "This could be a perfect opportunity to..."
        "Just splash about":
            s3_li "Sure, we can splash about if you want!"
            "[s3_li] cups the head of the shower with [his_her] hands and then pours water all over you."
        "Do some sexy shower bits":
            $ s3e9p1_shower_bits = True
            "You grin at [him_her] cheekily."
            s3_mc "Shall we make the most of this private time?"
            if s3_li == "Ciaran":
                "He nods, hurriedly, blushing a little."
                ciaran "Hell, yeah!"
                "You step closer to his body."
            else:
                s3_li "You took the words right out of my head."
                "[he_she!c] pulls you closer towards [his_her] body."
            "In a flurry of passion, you gently but firmly press [s3_li] against the tilted wall."
            if s3_li == "Ciaran" or s3_li == "AJ":
                s3_li "That's cold."
                s3_mc "Oops."
            "[s3_li] breathes heavily as you explore each other's naked wet bodies."
            s3_li "I've never done it in the shower before."
            s3_mc "Has anyone ever told you that you're, like, a work of art?"
            s3_li "No, they haven't!"
            s3_mc "Well, I want to pin you up against the wall."
            s3_mc "Like the masterpiece you are."
            s3_li "Oh, [s3_name]..."
            "[s3_li] kisses you, desperate for you."
            if s3_li == "Ciaran" or s3_li == "Tai" or s3_li == "Camilo" or s3_li == "AJ":
                s3_li "Frame me."
            else:
                s3_li "Enough with the smooth lines."
                "[s3_li] kisses your lips and whispers in your ear."
                s3_li "I want you."
                "[his_her!c] body is wet to your touch."
                s3_li "I need you."
            "You kiss [his_her] neck, while your fingertips travel down [his_her] body."
            s3_li "Oh, wow."
            "[s3_li] shudders beneath your touch."
            "As [he_she] desperately pulls you close, you feel your breath catch."
            "Hot water trails down your body, along with [s3_li]'s hands."
            "Surging heat builds between you. Eventually, you're both satisfied."
            "As you slowly pull away from each other, [s3_li] breathes out heavily."
            s3_li "Hot damn."
            s3_li "That was amazing."

    "Suddenly there is a knock at the door."
    s3_other_f "Hello?"
    s3_other_f "Are you guys, like, OK in there?"
    s3_li "Um, sorry [s3_other_f]! Just a second."
    "[s3_li] and you laugh."
    s3_mc "Busted."
    s3_other_f "Come on, I really need the loo."
    $ leaving("s3_other_f_image")
    s3_li "We'd better get out."
    "[s3_li] steps out and wraps a towel around [him_her]self."
    "As you get out, [he_she] wraps one around you."
    s3_li "There."
    s3_li "Nice and clean now."
    s3_mc "Sort of."
    "[s3_li] winks at you."
    "You head over to the dressing room to get changed."

    return

label s3e9p1_swim:
    scene s3-dressing-room with dissolve
    $ new_scene()

    thought "Hmm..."
    thought "I don't know what today will bring at all."
    thought "I better go out with a fierce look so I'm ready for anything and everything."

    # Outfit change to swimwear
    $ outfit = "swim"
    call customize_outfit from _call_customize_outfit_15

    # CHOICE for the outfit
    menu:
        thought "How do I feel about this outfit?"
        "I love it!":
            thought "Oh, I love this thing."
            thought "Oh this is the real deal."
            thought "I look great!"
            $ s3e9p1_shower = True # Setting flag for joining LI in shower/gem choice
        "It'll do":
            "You shrug."
            thought "This will have to do, I suppose."
            $ s3e9p1_shower = False

    $ pronouns(s3_li)
    
    if not s3e9p1_shower:
        # (not choosing the gem choice to join LI in the shower)
        "[s3_li] walks in, towel drying [his_her] hair."
        s3_mc "Nice shower?"
        s3_li "It would have been better with you in it."
    else:
        # (choosing the gem choice to join LI in the shower)
        s3_li "Clean now, babe?"
        "[s3_li] winks at you, towel drying [his_her] hair."
        s3_mc "Totally."
        s3_li "I love it when you wear that, by the way."
        s3_mc "What, this old thing?"
        s3_li "Yeah, it's gorgeous."
        s3_li "You look gorgeous in that, by the way."
        $ s3_mc.like(s3_li) # Gain approval/emoji with LI
        s3_mc "Aw, thanks hun!"
        s3_li "You look great in anything, obviously. But you'd look even better in nothing, I think."

    "Your stomach rumbles."
    s3_li "Hungry?"
    s3_mc "Starving."
    s3_li "You go get yourself something to eat while I sort myself out."
    s3_mc "Oh, OK. Sure."
    "You head downstairs to the kitchen for breakfast."

    scene s3-kitchen-day with dissolve
    $ new_scene()
    
    "You walk down into the kitchen. [s3_bff] is making breakfast."
    s3_bff "Cup of something, [s3_name]?"

    menu:
        "I want a cup of..."
        "Tea":
            s3_bff "One tea coming up."
        "Coffee":
            s3_bff "One coffee coming up."
        "Wheatgrass smoothie":
            s3_bff "A what?"
            s3_mc "A wheatgrass smoothie."
            s3_mc "Don't you know what a wheatgrass smoothie is?"
            s3_mc "They were all the rage last summer."
            s3_bff "Really? OK, I'll see if we have any."
            "[s3_bff] crouches down and searches through a cupboard, confusion still etched around [his_her] face."
            s3_bff "Hmm, I don't think we have that here."

    "Ciaran comes over clutching a mug."
    "Ciaran blushes when he sees you."
    ciaran "Hey again."
    s3_mc "Hey."
    ciaran "Can I get some of that water once it's boiled, please?"
    s3_bff "Sure. What are you after?"
    ciaran "Cuppa tea, please."
    s3_bff "I'll bring it over to you."
    "Ciaran smiles."
    ciaran "Grand."
    "[s3_bff] puts the kettle on to boil."

    elladine "So, babes. What's your go-to breakfast?"

    menu:
        "Elladine wants to know my go-to breakfast..."
        "Cereal. All day, every day":
            pass
        "I like a continental breakfast":
            pass
        "Most days I just have a quick snack":
            pass
        "It's a fry-up, obvs":
            elladine "Knew you were my friend for a reason."
            elladine "Can't be dealing with anyone who badmouths a full English."
            elladine "And I make the best one around."
            elladine "Important questions time. Do you have the black pudding?"

            menu:
                "Do I take pudding with my fry-ups?"
                "Obviously":
                    pass
                "Never":
                    pass
                "Only when I'm feeling adventurous":
                    pass

            elladine "Sound. And your opinion on hash browns?"

            menu:
                "Hash browns in a fry-up?"
                "Hate 'em":
                    pass
                "Love 'em, but not in a fry up":
                    pass
                "Love 'em":
                    elladine "Correct choice."

    elladine "Alright, what about a drink? Orange juice, tea, or something else?"
# Continuation from the drink choice with Elladine

    menu:
        "What drink do I have with my fry-up?"
        "Milk":
            elladine "Not a bad choice."
            elladine "But it's not as good as tea. It's the best thing for early mornings."
        "Tea":
            elladine "Ding ding!"
            elladine "Not sure how anyone can drink anything else, to be honest."
        "Orange juice":
            elladine "Not a bad choice."
            elladine "But it's not as good as tea. It's the best thing for early mornings."

    elladine "Maybe it's just in my blood? I like to joke about that sometimes…"
    elladine "What thing do Brits and Iranians have most in common?"
    s3_mc "I don't know, what?"
    elladine "They both love tea way too much."
    s3_mc "I never realised you had such strong opinions on fry-ups."
    elladine "Yeah, I sound like Bill now, don't I?"

    elladine "Alright, since I'm here grilling you already about your morning routine, how about another question?"
    s3_mc "Go for it."
    elladine "Morning sex?"
    s3_mc "Woah. That took a turn."
    elladine "Sorry. Guess I have sausage on my brain."
    s3_mc "Was that even a question?"
    elladine "I mean, what do you think of it?"
    elladine "When you've literally just woken up. Is it fun? Or just good in theory?"
    s3_mc "You've never done it?"
    elladine "Um, no. I just sort of figured… well, there's all that bad breath, and you're all sweaty from the night…"
    elladine "At least I usually am. First thing I have to do in the morning is shower."
    elladine "I can't do anything else until then."
    elladine "So… is it good?"
    elladine "Nicky mentioned it, you see, so…"

    menu:
        "What do I think of morning sex?"
        "You're right, it's just icky":
            $ s3_mc.dislike("elladine")
            pass
        "I've never really done it either":
            s3_mc "Sorry I can't help you! I'd not really thought about it until now, but I guess I'm just as new to it as you."
            s3_mc "Guess the only way for us to find out is to try!"
            elladine "Guess you're right."
            elladine "I'll, uh…"
            elladine "…I'll float the idea by him, I suppose."
        "I love it":
            s3_mc "Honestly, babe. If Nicky wants to do it, and you're feeling adventurous, go for it."
            s3_mc "There's something so primal and basic about it."
            s3_mc "And what's hotter than someone waking up and their first thought being what they could do with you."
            elladine "Yeah… when you put it like that."
            "You see a 😳 emoji above Elladine's head."
            $ s3_mc.like(elladine)
            elladine "I think, well, I'll talk to Nicky about it."

    elladine "Thanks, hun."
    s3_mc "No problem!"
    "The kettle clicks as it finishes boiling. Elladine pours you a cup of tea."
    elladine "OK, one more?"
    s3_mc "Sure."
    elladine "Early bird or night owl?"
    s3_mc "Ooh, good one!"

    menu:
        "Am I an early bird or night owl?"
        "Early bird":
            s3_mc "Gotta seize the day, early bird catches the worm, and all that jazz."
            elladine "And there's more than a few worms to catch in the Villa, right?"
            s3_mc "Elladine!"
            elladine "What? It's true isn't it?"
            elladine "Anyway I'm the same."
        "Night owl":
            elladine "Ah. I always think there's something romantic about that."
            elladine "Like, in movies the night owls are all those tortured creative souls who can only work by the moonlight."
            elladine "As cool as that sounds, I can't hack it."

    elladine "I have to be in bed early or I start falling asleep."
    elladine "My friends used to always joke about me falling asleep on the dance floor."
    elladine "I just get lost in the music sometimes!"
    s3_mc "Just 'resting your eyes', right?"
    elladine "Exactly."

    # Scene shift to Genevieve
    $ entering("genevieve")
    genevieve "You know, I think things are going to be different with Seb."
    genevieve "Compared to my past relationships, that is."
    s3_mc "How so?"
    genevieve "I'm going to explain it in kind of a weird way, but stick with me…"
    genevieve "So, I read this book called 'Creating Your Feminine Breeze'. It's about how women are always the caregivers and men try to take advantage of that."
    genevieve "Basically women are goddesses, and men are mortals trying to suck out our power for their own gain."
    genevieve "Does that make sense?"

    menu:
        "Do I understand what Viv is saying?"
        "No":
            s3_mc "They're trying to suck what out of us?!"
            genevieve "No! Not physically. Emotionally."
        "Yes":
            s3_mc "Goddesses are naturally generous, and it intimidates mortals."
            genevieve "Exactly!"
        "I've read that book too!":
            s3_mc "It changed my life."
            s3_mc "Goddesses are naturally generous, and it intimidates mortals."
            genevieve "Exactly!"

    genevieve "It's like, I went out with a guy who told me he was going to be an entrepreneur."
    genevieve "It impressed me at first, but then I found out that 'being an entrepreneur' largely involved him playing Duty Calls."
    genevieve "I paid that guy's rent for almost a year. Plus every bill when we went out for dinner so he wouldn't have to wash dishes."
    genevieve "All while getting my PhD."
    genevieve "I dumped him eventually, but not soon enough."
    genevieve "And that book helped me realise that if a mortal wants to be with a goddess, he has to help her shine."
    s3_mc "Seb's definitely that guy."
    genevieve "I think so too."
    genevieve "I'm not too proud to admit I've been taken advantage of before."

    menu:
        "Viv's been taken advantage of…"
        "That's horrible":
            genevieve "Yeah, it is."
        "It's cos you're so caring":
            genevieve "Aw, that's nice of you to say."
            genevieve "You're probably right. Not a lot of people would pay someone else's rent, but I suppose he targeted me cos he knew I would."
        "Me too":
            genevieve "Babe, I'm sorry."
            s3_mc "Thanks."

    "She holds up her fist and bumps yours."
    genevieve "To new beginnings!"
    $ leaving("genevieve")

    # Nicky's Segment
    $ entering("nicky")
    nicky "Here's something."
    nicky "I might have a proposal for Seb. But I wanna get your take on it before I ask him."

    menu:
        "A 'proposal' for Seb?"
        "You're going to rob a bank together?":
            nicky "Hmm. Someday, maybe."
            s3_mc "Do you think he'd be any good?"
            nicky "You never know. I think he'd be good at moving silently, so maybe he can be the one who does the actual stealing."
            nicky "I'm the ringleader and the planner, obviously."
            nicky "And you can be the one who distracts the guards with your womanly charm."
        "You're going to ask him to marry you?":
            nicky "Ha, not yet. He doesn't seem like the marrying sort."
            s3_mc "No offence, but I don't think you're his type, either."
            nicky "Tragic but true."
            nicky "Well, you never know. Maybe someday he'll get married in a graveyard or something and live gloomily ever after."
            nicky "He could have a bat for the officiant."
        "You're going to buy out his shop?":
            nicky "God, no. Can you imagine?"
            nicky "I'd have to shut it down and turn it into a shoe shop or something."
            nicky "I don't understand how he stays in business. Who's buying records anymore? And from Seb, of all people?"
            nicky "Can you imagine his customer service? How does he do it?"
            s3_mc "I think he said the shop has a little café as part of it, so it's not just records."
            s3_mc "But I know what you mean."

    s3_mc "What does this have to do with your proposal?"
    nicky "Oh, right, yeah. The thing."
    nicky "I was thinking about asking Seb to do a podcast with me, once all this is over."
    nicky "'Cause he actually really knows his stuff when it comes to music, and obviously I take an interest, 'cause it's my job."
    nicky "And we could talk about our favourite artists, do reviews, that kind of thing."
    nicky "What d'you think? Would anybody listen to that?"

    menu:
        "Nicky wants to ask Seb to host a podcast with him…"
        "He'll never agree to that":
            pass
        "Yeah, that's a great idea!":
            s3_mc "You guys are both smart, and you're funny together, too. I think it'll be a great combination."
            nicky "Cheers! I'm really glad you think so."
        "If you're sure he's up to it…":
            s3_mc "Talking to people isn't exactly Seb's favourite thing in the world."
            s3_mc "I know he's come out of his shell a bit since we've been here, but it's still a big ask."
            nicky "True, but don't forget, he did apply to come on Love Island. And he's done well so far."
            nicky "After this, I reckon a little podcast will be no trouble."

    nicky "To be honest, and don't tell him this…"
    nicky "….Part of the reason I want to ask him is so we have an excuse to stay in touch after Love Island."
    nicky "I don't want him to just retreat into this cave when it ends and none of us ever see him again, y'know?"

    menu:
        "Nicky's doing this as an excuse to stay friends with Seb…"
        "That's silly, you should just tell him you want to hang out":
            pass
        "Aw, that's actually pretty cute":
            s3_mc "I won't tell him. I think it might be too much sweetness for him to handle all at once."
            nicky "Yeah, that's my thinking."
            nicky "Friendship is still new to him. He just needs time to get used to it."
        "Then why aren't you asking me to host a podcast with you?":
            nicky "'Cause you're not like Seb. I don't need to trick you into hanging out with me."
            s3_mc "Well, maybe, but you should at least be trying!"

    "Nicky grins."
    $ leaving("nicky")

    # Seb's Segment
    $ entering("seb")
    seb "Hey, [s3_name]. Have you ever made a mixtape for someone you fancied?"
    s3_mc "A 'mixtape'?"
    seb "You know what I mean. A playlist."

    menu:
        "Have I ever made a playlist for someone I fancied?"
        "Come on, I'm not that melty":
            pass
        "Yeah, it's a great way to flirt":
            s3_mc "I love it. So romantic."
            seb "Yes! Me too."
        "No, but it's a cute idea":
            s3_mc "I think I'd just melt if someone did that for me."
            seb "Oh, good. I wasn't sure if any girls actually liked it."
            s3_mc "Tried it before, have you?"
            seb "Only a lot."
            s3_mc "Does it work?"
            seb "…Sometimes."

    seb "It's like a reflex. When I really like a girl, I just have to start making a playlist for her."
    seb "With all the songs we've talked about together, or songs I think she'll like, or songs that remind me of her."
    seb "I'm thinking about making one for Viv."
    seb "Obvs. I have to do it in my head until I get home."
    seb "And I know it's too soon! I know that. But I can't help it."
    seb "I can't stop thinking of things I could do to try and make her smile."
    seb "Her smile is just… mate, it goes right through me."

    menu:
        "Seb's going on about Viv…"
        "You two are adorable":
            s3_mc "You make such a cute couple."
            seb "We're not… I mean, we're not a proper couple. Like, officially."
            seb "I think."
        "Come on, give it a rest":
            s3_mc "Dude, I don't want this friendship to turn into you banging on about how great your girlfriend is."
            seb "She's not my girlfriend!"
        "Have you told her this?":
            seb "Told her what?"
            s3_mc "Uh, that you're in love with her?"
            seb "What? No I'm not!"

    s3_mc "Well, it seems like you're already halfway there, at least."
    s3_mc "Just a few days ago you told me you 'never fall for girls like her'."
    s3_mc "And now you're talking about her like you've fallen head over heels."
    seb "You're right. I mean, I always wished I could be with a girl like that."
    seb "And now I think I've finally done it."
    seb "I've fallen for someone nice who actually likes me back."

    menu:
        "Seb's feeling good about falling for Genevieve…"
        "Alright, now just try not to mess it up":
            pass
        "I'm really happy for you":
            s3_mc "I think you're gonna be good for each other."
            seb "Thanks, mate."
        "I wouldn't get too excited yet":
            s3_mc "Look, I know being happy is still new and exciting for you, but don't get carried away."
            s3_mc "You haven't actually known each other that long. You don't know how things will be outside the Villa."
            seb "You're right. I'll try to keep my feet on the ground."

    seb "I'm finally starting to feel like I do belong here after all."
    seb "Actually, I think that chat we had the other day really helped."
    seb "It turns out nice things happen sometimes when you're not always on the lookout for the next disaster."
    s3_mc "Who knew?"
    "Seb grins."
    $ leaving("seb")

    # Conversation with BFF
    $ entering("s3_bff_image")
    s3_bff "So, how are you feeling about last night?"

    menu:
        "How do I feel about getting with [s3_li]?"
        "[s3_li] is punching up, to be honest":
            "[s3_bff] frowns."
            s3_bff "I don't think that's very fair."
            s3_bff "You're both, like, solid tens for sure."
            "You shrug."
            s3_mc "If you say so."
            "[s3_bff] looks awkwardly at the ground."

        "I couldn't be happier":
            "[s3_bff] smiles."
            s3_bff "You two look great together."
            # Logic check for Harry/Genevieve drama
            if s3_li == "Harry":
                $ entering("genevieve")
                genevieve "Oh, and [s3_name], I really wanted to say that I'm happy for you and Harry."
                genevieve "So don't worry about me. In case you were."
                "Genevieve smiles at you."
                genevieve "And I'm actually kind of excited to see where this whole thing with Seb goes."
                $ leaving("genevieve")

        "It was fate, nothing could stop us":
            $ s3e9_fate = True # Flag for later dialogue
            s3_bff "Ha, yeah, I guess you're right!"
            if s3_li == "Harry":
                $ entering("genevieve")
                genevieve "Oh, and [s3_name], I really wanted to say that I'm happy for you and Harry."
                genevieve "So don't worry about me. In case you were."
                "Genevieve smiles at you."
                genevieve "And I'm actually kind of excited to see where this whole thing with Seb goes."
                $ leaving("genevieve")

    # Special condition: BFF is Genevieve and LI is Harry
    if not (s3_bff == "Genevieve" and s3_li == "Harry"):
        s3_bff "I'm so, like, happy for you both."

    s3_bff "Your speech was amazing, by the way."

    menu:
        "BFF liked my recoupling speech."
        "Yay! I worked really hard on it":
            s3_bff "You could tell!"
        "Really? It was totally improvised":
            if s3_bff in ["Genevieve", "Elladine"]:
                s3_bff "Sometimes improvisation gives us the most genuine words."
            else:
                s3_bff "That's well brave. I couldn't have done that."
        "Thanks, it came from the bottom of my heart":
            $ s3e9_heart = True # Flag for later dialogue
            "[s3_bff] starts to sniff the air."
            s3_bff "Can you smell that?"
            "[he_she_cap] sniffs your shoulder."
            s3_bff "Smells like cheese."
            s3_mc "Very funny."
            s3_bff "I'm kidding. You're both class."

    "The kettle stops boiling."
    s3_bff "So…"
    "[s3_bff] pours out the water into some mugs."
    s3_mc "So?"
    s3_bff "It seems like things are all good for you two."

    # smitten dialogue check
    # if s3e9_fate and s3e9_heart:
    #     s3_bff "Yeah, from everything you've said, you seem really smitten."

    # Shower check (using the flag from your previous prompt)
    if s3e9p1_shower:
        if s3_bff in ["Genevieve", "Elladine"]:
            s3_bff "Did I hear that mouse in the bathroom earlier?"
            s3_mc "Um…"
            s3_bff "I definitely heard some squeaking."
            s3_mc "No, I didn't see any mice."
            s3_bff "Huh, I thought I could hear it when you and [s3_li] were in the bathroom."
            s3_bff "I must have pool water in my ear or something."
        else:
            s3_bff "And it certainly sounded like you two were having fun in the shower."
            s3_mc "You heard us?"
            s3_bff "I know a sexy noise when I hear one."
            "You blush."

    s3_bff "But, like, between you and me…"
    s3_bff "Do you think you'll be loyal with [s3_li] for, like, the rest of the time in the Villa?"

    menu:
        "Will I be loyal with [s3_li]?"
        "Yeah, I want to be loyal":
            s3_bff "That's cool."
        "My head could turn":
            s3_bff "Really?"
            s3_mc "You never know what will happen in this place."
            "[s3_bff] sighs."
            s3_bff "Yeah, I guess you're right."
        "We will rule the land together forever":
            s3_bff "I meant loyal, not royal."
            s3_mc "I know."
            s3_mc "And we will reign as the best, most royally loyal couple ever."
            "[s3_bff] laughs, spitting out [his_her] tea a little."
            s3_bff "You're so funny."

    s3_bff "But seriously. Have you had a chat with [s3_li] about, like, loyalty and stuff?"
    s3_mc "Nope, not exactly…"
    s3_bff "Hmm… Do you think [he_she] is a loyal person?"

    menu:
        "Do I think [s3_li] is loyal?"
        "Yeah, I think we're pretty solid":
            s3_bff "Well, that's good."
        "[he_she!c]'s [his_her] own person, I'm not forcing anything":
            s3_bff "That's a good headspace to be in."
        "If [he_she] knows what's good for [him_her] then [he_she] will be":
            s3_bff "Don't you think that's, like, a bit threatening?"
            "You sigh."
            s3_mc "I guess…"
            s3_bff "You don't want to come across, like, possessive."

    s3_bff "I don't want you to worry or anything."
    "[s3_bff] grabs a spoon from the drawer and starts to stir the tea."
    "The sound of the teaspoon hitting the china rings across the kitchen."
    s3_mc "Um, [s3_bff]…"
    s3_mc "What are you saying?"
    s3_bff "I'm not insinuating anything, [s3_mc]."
    s3_mc "Has [he_she] said something about me to you?"
    s3_bff "I'm just thinking out loud. Ignore me, [s3_mc]."
    "[s3_bff] picks up the mugs."
    s3_bff "I'm sure it'll be fine. Ah, phew, it's Ciaran."
    "[s3_bff] glances at you, looking a little flustered."
    s3_bff "Tea's ready."
    
    $ entering("ciaran")
    ciaran "Ta, [s3_bff]."
    "He blows on it and then takes an indulgent sip."
    ciaran "That's cracking, cheers."

    "Some other Islanders saunter into the kitchen."
    thought "What if [s3_li] isn't as loyal as I thought?"
    
    $ entering("s3_li_image")
    "[s3_li] heads over to the fridge."
    thought "Could [s3_bff] be right?"
    s3_li "I am in such a snacking mood today."
    thought "I guess that's [his_her] priority right now."
    thought "Food."

    # Shower joke if BFF is Seb or Nicky and LI is male
    if s3e9p1_shower and s3_bff in ["Seb", "Nicky"] and s3_li in ["Harry", "Camilo", "Tai"]:
        s3_bff "Did you hear a mouse earlier, [s3_li]? I could hear, like, weird noises coming from the bathroom earlier."
        s3_li "From the bathroom?"
        "[s3_li] laughs."
        s3_li "Oh, we were just cleaning the tiles, like, really hard."
        s3_bff "Aw, that's nice of you."

    $ entering("yasmin")
    yasmin "It's snack time."
    yasmin "And [s3_mc] as usual is looking like a snack."
    s3_mc "Cheers, Yasmin."
    
    $ entering("elladine")
    elladine "Oh, I am so going to have a good brunch."
    
    $ entering("tai")
    ciaran "What on earth is brunch?"
    tai "How can you not know what brunch is, Ciaran?"

    menu:
        "Ciaran asked what brunch is…"
        "It's a late morning meal":
            pass
        "It's a ploy to make you spend more money":
            pass
        "It's when you have a brilliant hunch about something":
            pass

    tai "I'll make you the best brunch of your life, Ciaran."
    tai "You just wait and see. I am a master brunch-maker."

    # Check if MC is coupled with the girls
    if s3_li in ["Yasmin", "AJ"]:
        "He brings out a bag of baps and piles them on the counter."
        tai "Baps?"
        ciaran "I love them."
        tai "I know. Prepare for the best bap of your life! I need avocados."

    "Tai gets out a couple of avocados from the fridge."
    ciaran "So what's the secret?"
    tai "As long as it looks good you can't go wrong."
    "Tai mushes up some avocado with raw egg."
    
    
    s3_other_m "Raw egg is, like, worse than celery."
    s3_other_m "Did you know that an uncooked egg doesn't give you barely any of the protein a cooked one would?"
    
    tai "Nonsense."
    "Tai continues to mash the sticky green mixture and packs it into baps."
    s3_other_m "Looks like the boogey monster sneezed on the baps."

    menu:
        "Raw egg and avocado in a bap…"
        "You've ruined a good bap":
            $ s3_mc.dislike("Tai")
            tai "I didn't mean to…"
        "I wouldn't eat that even if you paid me":
            $ s3_mc.dislike("Tai")
            tai "Oh…"
        "Sounds like a good hair mousse":
            "Miki/Iona says: That's actually a really good shout."
            "Tai sighs."
            tai "Yeah…"

    "Tai pokes at the bap. Green stuff oozes out."

    if s3_li not in ["Yasmin", "AJ"]:
        tai "Think I got a bit carried away."
        "Tai dejectedly scrapes the bap into the bin."
    else:
        tai "Think I got a bit carried away. Sorry Ciaran…"
        ciaran "It's the thought that counts. Don't worry about it."
        ciaran "We can get brunch in my hometown together when we get out if you'd like."
        "Tai smiles, scraping the bap in the bin."
        tai "Yeah, I'd like that."

    s3_li "I'm still hungry though…"

    "A text rings out."
    s3_bff "Oh."
    s3_bff "Hold that bap."
    s3_bff "I got a text!"
    "Everyone crowds around [s3_bff]'s screen."

    text "Islanders, put your best foot forward because two new Islanders will be arriving sometime today. #twosaparty #thirteenisacrowd"

    $ pronouns(s3_li)
    s3_li "Ooh, new people!"
    s3_li "Exciting…"
    
    s3_bff "New Islanders?"
    "[s3_bff] looks at you in shock."

    menu:
        "New Islanders are coming into the Villa!"
        "Yay! That means more friends":
            thought "It's always great to meet new people!"
            thought "I wonder if [s3_li] will just see them like a friend though…"

        "I hope [s3_li]'s head doesn't turn…":
            thought "I'd hate to lose [him_her] now!"

        "I hope they sweep me off my feet":
            thought "[s3_li] is old news."
            thought "I'm ready to be, like, properly swept off my feet."
            "You glance over at [s3_li]."
            "[he_she_cap]'s smiling at you, unaware of your thoughts."

    # Using the bill_cam logic from before
    $ bill_cam = "Bill" if s3_li != "Bill" else "Camilo"
    "[bill_cam] says: I wonder how they're going to arrive."
    
    genevieve "Giant suitcase?"
    elladine "Forget how."
    elladine "When are they going to arrive?"
    elladine "And who are they going to break up?"

    # The Narrator's Interlude
    narrator "Ah, Elladine."
    narrator "You know what they say?"
    narrator "The more…"
    narrator "The merrier."
    narrator "Or maybe it should be messier."
    narrator "Can someone please get the Islanders to clean up that dressing room?"
    narrator "I can see a mug that is wearing a green fuzzy jacket."
    narrator "Not that my shed is any better…"
    narrator "It gets pretty damp in here."
    
    narrator "Coming up…"
    narrator "Two new Islanders are on the way into the Villa."
    
    $ entering("aj")
    aj "This is the whole point of being here, to meet new people!"
    narrator "And it gets hard finding space to fit them all in!"
    
    $ entering("harry")
    harry "What if the only space available is a cupboard?"
    narrator "My hut is strictly off limits until I sort out this damp problem."

    # End of Part 1
    jump s3e9p2
    return
