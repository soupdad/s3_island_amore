#########################################################################
## Episode 3, Part 1
#########################################################################

label s3e3p1:
    scene sand with dissolve
    $ on_screen = []

    show screen day_title(3, 1) with Pause(4)
    hide screen day_title with dissolve

    "Welcome back to Island Amore!"
    "Last night, the boys cooked dinner..."
    "...well, 'cooked' might be an overstatement."
    nicky "I guess-timated."
    $ leaving("nicky")

    "Come to think of it, 'dinner' might be generous as well..."
    elladine "How's this a fruit salad? It's just watermelon."
    $ leaving("elladine")

    if s3e2p3_food_fight:
        "Though in the end, most of it ended up on the Islanders..."

    "But fear not, Camilo's steaming empanadas saved the day!"
    aj "This is better than sex."
    $ leaving("aj")

    "Look out for a surge in empanada-making courses this summer."
    "Coming up!"
    "Elladine shoots for the stars!"
    elladine "Then he took me out to the balcony..."
    $ leaving("elladine")

    "Wish I had a balcony."
    "...or a window, for that matter."
    "Nobody made dinner for me last night, by the way."
    "I had a microwave cheeseburger."
    "Thanks for asking."

    scene s3-bedroom-day with dissolve
    $ new_scene()

    "The lights are on in the bedroom as you awake."
    "You stretch out across the bed."

    # CHOICE
    menu:
        thought "I've got so much space..."
        "I wish I had someone to share it with":
            thought "I'd sleep better if there was someone next to me."
            thought "Or maybe I wouldn't."
        "It'll be a shame when I have to share it":
            thought "There are benefits to coupling, sure..."
            thought "But do they really outweigh a great night's sleep?"
        "Maybe I should slip into someone else's bed...":
            thought "I can think of at least one person's bed I'd like to get into."

    "Looking around, you realise that you're the only person in the bedroom."

    # CHOICE
    menu:
        thought "Oops, looks like I overslept again..."
        "Nice of them to let me sleep":
            thought "I'd have been so grumpy if they'd interrupted my beauty sleep."
            thought "I need every advantage I can get for grafting today!"
        "Maybe they all got abducted by aliens":
            thought "Well, I guess it's up to me to save humanity."
            thought "Step one: get out of bed."
        "I'm missing valuable grafting time":
            thought "I can't afford to waste a single moment."
            thought "Time to get cracking!"

    # ADD BACK ONE MC HAS IMAGES
    thought "Hmm, let's see. What should I wear?"
    # MC outfit change to swimwear
    
    $ outfit = "swim"
    call customize_outfit from _call_customize_outfit_6

    thought "Watch out everyone. Here I come!"
    # thought "This outfit already has a proven track record of turning heads."
    # s3_mc "It's perf."
    # thought "I guess I'll have to rely on my sparkling personality."

    scene s3-kitchen-day with dissolve
    $ new_scene()

    "Nicky, Seb, Genevieve and Elladine are hanging out in the kitchen."
    # ADD BACK ONCE MC HAS IMAGES
    elladine "Wow, [s3_name], that outfit really brings out your...everything."
    # elladine "Hi [s3_name]."
    # elladine "Have I told you that I love that outfit?"
    # elladine "Because I do."
    # elladine "I think you could probably wear it every day and get away with it."
    # elladine "Hi MC."
    # elladine "You know, you're so pretty that I bet you could get away with wearing something a bit more daring."
    elladine "We were just talking about dreams."
    elladine "Nicky and I both had dirty ones last night."
    nicky "Mine was about some girl called 'Stacey'."
    nicky "I don't even know a Stacey."
    nicky "Elladine won't tell us who hers was about, though."

    # CHOICE
    menu:
        thought "Who do I think Elladine had a sex dream about?"
        "Nicky":
            s3_mc "Well, it's got to be Nicky, then, hasn't it?"
            "Elladine blushes."
            nicky "That's what I said!"
            elladine "It wasn't you!"
            elladine "Sorry, I mean, not that I... you know, it's just that I..."
            elladine "Ack...sorry."
            nicky "It's OK. We've only known each other a couple of days, after all."
        "Another Islander":
            s3_mc "I bet it was someone else in here. Like Camilo, or Bill..."
            elladine "Nope."
            s3_mc "One of the girls, then?"
            elladine "Not my style, babes."
            elladine "It wasn't anyone in here."
        "A random celebrity":
            s3_mc "I bet it was someone weird, like a politician or something."
            elladine "You're getting warmer."
            elladine "It was someone I'd never go for in a million years."

    s3_mc "Don't keep us in suspense, babes."
    seb "We're all friends here. No judgement."
    elladine "OK, so, in the dream I was at a fancy party."
    elladine "Like a ball type of thing."
    elladine "Candles, dresses, the whole shebang."
    elladine "It was really romantic."
    elladine "And I was dancing with... Matt McKinnon."
    s3_mc "Who's that?"
    nicky "Oh no. Not that guy."
    "He facepalms dramatically."
    nicky "He's this singer. He's well cheesy."
    nicky "When's the next recoupling?"
    "Elladine gives him a playful shove."
    genevieve "Oh, I love him! He's got that song, 'Your Eyes and Mine'."
    genevieve "It's really romantic."
    seb "It's pants. I can see why Elladine was embarrassed."
    elladine "Yeah, I don't even fancy him!"
    elladine "So the song finished, and we kissed."
    elladine "Then he took me out to the balcony..."
    seb "I hope the sex was better than his music."
    "She blushes."
    elladine "I don't remember the details, but it was very good."
    elladine "It's because I had a glass of milk before bed."
    elladine "Always gives me the weirdest dreams."
    seb "It's curry for me. Any time I have a curry for tea, I have a pure nonsense dream."
    seb "What about you, [s3_name]? Any foods give you strange dreams?"

    # CHOICE
    menu:
        thought "Is there any food that gives me weird dreams?"
        "Yeah, totally":
            # SUB-CHOICE
            menu:
                s3_mc "Oh yeah, definitely. It's..."
                "Cheese":
                    pass
                "Chocolate":
                    pass
                "Blackcurrant juice":
                    pass
            seb "Oh yeah, that'll do it."
            nicky "What was the last dream you had?"
            call s3e3p1_dream from _call_s3e3p1_dream
        "I have weird dreams anyway":
            s3_mc "I don't need food to give me bizarre dreams. They happen anyway!"
            nicky "What was the last dream you had?"
            call s3e3p1_dream from _call_s3e3p1_dream_1
        "I don't really dream much":
            s3_mc "I'm not a big dreamer, to be honest."
            s3_mc "My friends are always telling me about their dreams and I'm just like 'I had a nice sleep'."
            seb "Sleep's important."
            seb "Wish it didn't always feel like I need more of it.."

    genevieve "I'm going to hit the gym for a bit."
    thought "I should go see what everyone else is up to. "

    call screen s3e3p1_select_who_to_talk_to

    call screen s3e3p1_select_who_to_talk_to

    menu:
        "Talk to last group?"
        "Sure":
            call screen s3e3p1_select_who_to_talk_to
        "No, I'm done chatting":
            "Are you bantering?"
            "There are still Islanders waiting to talk to you. You can continue onto the next stage if you want, but you might miss out on juicy gossip!"
            menu:
                "Talk to rest of Islanders":
                    call screen s3e3p1_select_who_to_talk_to
                "No thanks":
                    pass         
                    
    jump s3e3p1_ending
    return

    label s3e3p1_dream:
        # SUB-CHOICE
        menu:
            s3_mc "It was..."
            "Sexy":
                s3_mc "It involved more than one other person."
                elladine "Wow, you get it, girl."
                s3_mc "They were people I know as well."
                nicky "I wasn't there, was I?"
                s3_mc "No, it wasn't about anyone in this room."
                nicky "Phew."
                "Seb looks relieved too."
            "Scary":
                s3_mc "I woke up in a cold sweat."
                seb "What was it about?"
                s3_mc "You."
                seb "What?"
                s3_mc "Just kidding."
            "Completely bizarre":
                s3_mc "I barely understand what happened."
                s3_mc "The Villa was in it, but it was... a castle?"
                s3_mc "Made of glass."
                s3_mc "And for some reason I had to make a load of cakes."
                s3_mc "And the other Islanders were getting more and more impatient."
                s3_mc "Then suddenly the lava-crown people attacked!"
                seb "Eh?"
                s3_mc "I have no idea. That's when I woke up."
        return

# Map Choice "AJ and Genevieve at the gym"
label s3e3p1_gym:
    scene s3-gym-day
    $ new_scene()
    $ s3e3p1_visited.append("Gym")

    "AJ and Genevieve are in the gym. Genevieve has a serious look on her face. AJ is doing a cross-body shoulder stretch."
    s3_mc "What's going on?"
    genevieve "We were talking about our arm day routines and it kinda... escalated."
    aj "We're gonna arm wrestle!"

    # CHOICE
    menu:
        thought "AJ and Genevieve are going to arm-wrestle each other."
        "That's fun":
            s3_mc "A good old-fashioned battle of strength."
            s3_mc "I like it."
        "That's silly":
            s3_mc "What are you trying to prove?"
            genevieve "Who would win in an arm wrestle, obviously."
        "I hope nobody gets hurt":
            s3_mc "What if your arms come off?"
            genevieve "I'm strong, but I don't think I'm that strong."
            "AJ looks genuinely worried for a moment."
            aj "That can't happen, can it?"

    genevieve "Ready, AJ?"
    aj "I'm not sure about this."
    genevieve "Scared?"
    aj "No! I just don't want to hurt you."
    genevieve "She's confident."
    genevieve "Will you be the ref, [s3_name]?"
    s3_mc "Sure."
    aj "Who are you gonna bet on?"

    # CHOICE
    menu:
        thought "Who's my money on to win the arm wrestle?"
        "AJ":
            $ s3e3p1_bet = "AJ"
            s3_mc "My money's on AJ. You go, girl!"
            genevieve "Hang on, the ref can't have a favourite!"
            aj "Well, I'm fine with it."
        "Genevieve":
            $ s3e3p1_bet = "Genevieve"
            s3_mc "Hmm, I think Viv's got this in the bag."
            aj "Just you wait!"
        "The ref's gotta be neutral":
            aj "Boo, what a cop-out!"
            "Genevieve nods approvingly."
            genevieve "Proper respect for the role. I like that."

    s3_mc "Now, I want a good clean wrestle."
    s3_mc "You can brace against the table but I want to see feet firmly planted on the floor."
    "You raise your arm as the two women lock hands."
    s3_mc "Go!"
    "They start to strain."

    # CHOICE
    menu:
        thought "What should I do?"
        "Make some noise":
            "You shout and whoop like you're watching a cage fight."
            "Genevieve grits her teeth and tries to concentrate. AJ bites her lip to keep from laughing."
            "Suddenly, Genevieve's hand comes crashing to the table."
        "Cover your eyes":
            "You turn away and put your hand in front of your eyes."
            genevieve "What...are...you...doing?"
            s3_mc "I can't watch! It's too much!"
            "Behind you, there's a thud. You turn round and see AJ grinning."
        "Distract them":
            "You start to dance around the table, pulling silly faces and making strange noises."
            "Genevieve grits her teeth and tries to concentrate. AJ bites her lip to keep from laughing."
            "Suddenly, Genevieve's hand comes crashing to the table."

    aj "Booyah!"

    if s3e3p1_bet == "Genevieve":
        s3_mc "Now that I think about it, I probably should have bet on the professional athlete."
    elif s3e3p1_bet == "AJ":
        s3_mc "Woohoo! I knew you could do it!"

    genevieve "Nice one, AJ. Talk about strong biceps."
    aj "I'm so sorry! I did warn you."
    genevieve "You did."
    genevieve "Right, I'm off to make some breakfast... and put a heat pack on my arm."
    "She walks off towards the kitchen."

    if s3e3p1_bet == "AJ":
        aj "Hey, thanks for believing in me. I was pretty happy when you said you thought I'd win."

    if s3_like_aj:
        s3_mc "I've been admiring those biceps for a while..."
        s3_mc "It was sexy watching you use them."
        aj "Any time, [s3_name]."

    "AJ flexes her arm, wiggling her fingers. She winks at you."
    aj "Wanna try your luck?"

    # CHOICE
    menu:
        thought "AJ's challenging me to an arm wrestle..."
        "Oh, it's on":
            $ s3e3p1_arm_wrestle = True
            aj "Yay! Let's do this."
            "You lock hands. AJ's skin is warm and her palms are rougher than you expected."
        "Go easy on me!" if s3_like_aj == False:
            $ s3e3p1_arm_wrestle = True
            s3_mc "OK, but I don't fancy my chances."
            s3_mc "I'm pretty sure you're gonna win against me just like you did with Genevieve."
            aj "I guess we'll find out."
            "You lock hands. AJ's skin is warm and her palms are rougher than you expected."
        "Anything to hold your hand" if s3_like_aj == True:
            $ s3_mc.like("AJ")
            $ s3e3p1_arm_wrestle = True
            aj "You don't have to arm wrestle me to hold my hand, you know."
            s3_mc "I'll have to remember that."
            "You lock hands. AJ's skin is warm and her palms are rougher than you expected."
        "I'm good, thanks":
            s3_mc "Thanks but no thanks."
            s3_mc "I saw what you did to poor Viv!"
            aj "Do you think she's upset?"
            # SUB-CHOICE
            menu:
                "AJ is really worried about Genevieve..."
                "I'm sure she's fine":
                    s3_mc "Nah, it's OK."
                    s3_mc "She should have known better than to tangle with you!"
                    aj "Thanks."
                "You might have hurt her pride a bit":
                    aj "Oh, no..."
                    aj "What if she hates me now?"
                    s3_mc "Don't worry, she doesn't hate you."
                    s3_mc "How could she? You're awesome."
                    aj "I hope you're right..."
                "I love how caring you are":
                    s3_mc "I really like it."
                    aj "I think it comes from being on a team, you know?"
                    aj "On the field, everyone's gotta have each other's backs."


    if s3e3p1_arm_wrestle:
        if s3_mc.job == "Athlete":
            "You're evenly matched for strength, but your technique is better. After a minute or two of vigorous effort, you emerge victorious."
            aj "Wow. You are strong!"
            aj "You'll have to give me a rematch sometime!"
        else:
            "You manage to put up a surprisingly good fight, but in the end, AJ's boundless energy is too much for you."
            s3_mc "You're a machine! I probably could have seen that coming."
            aj "That was fun! Let's do it again sometime!"

    "AJ stands up and stretches."
    aj "I'm gonna go have a shower before breakfast."

    if s3_like_aj:
        "She squeezes past, and you end up pressed against each other for a moment."
        aj "Sorry!"
        # CHOICE
        menu:
            thought "AJ is pressed up against me..."
            "I should have moved, sorry":
                # FILL IN
                "EMPTY"
            "We still haven't moved...":
                "You look at AJ. She looks at you. You're both very aware of how close you are."
                aj "I should be going!"
            "I'm enjoying it":
                "AJ blushes more."
                aj "Me too..."
                aj "Anyway, I should be going!"

    "AJ jogs off towards the Villa."
    thought "I wonder what everyone else is up to?"

    return

# Map Choice "Bill and Camilo at beanbags (s3e3p1_bean_bags)"
label s3e3p1_bean_bags:
    scene s3-bean-bags-day with dissolve
    $ new_scene()
    $ s3e3p1_visited.append("Bean Bags")

    "Bill and Camilo are in the middle of a heated discussion when you arrive. You plop down on a beanbag between them."
    camilo "Nah bruv, it's aji picante all the way."
    bill "Nope, the best sauce is mayo."
    camilo "Have you even had aji picante?"
    bill "No, but that's my point, innit. Mayo goes with anything."
    bill "I haven't had aji picante because it's too posh to be a truly great sauce. Hot sauces are only good for kebabs."
    camilo "Only for kebabs? Mate, you can have it with empanadas, patacones, you name it."
    camilo "Just because you can't put aji picante on a baked potato..."
    camilo "Wait, scratch that. That actually sounds lush."
    bill "Mayo can be used on everything and aji picante can't. Face it."
    camilo "[s3_name], tell me you don't prefer mayo to a real condiment!"
    bill "Real condiment? You little..."
    camilo "Shh. Let [s3_name] speak."

    # CHOICE
    menu:
        thought "What's my opinion on sauces?"
        "Spicy all the way":
            $ s3_mc.like("Camilo")
            camilo "I knew you were a woman of taste."
            "He winks at you and blows you a kiss."
            bill "I see how it is..."
            s3_mc "What can I say? I like a bit of excitement."
        "I prefer a milder sauce":
            $ s3_mc.like("Bill")
            bill "See, mate? [s3_name] knows where it's at."
            "He winks at you and flashes you a smile that feels like a shared secret."
            camilo "You guys are beyond help..."
            s3_mc "What can I say? I guess I'm just a down-to-earth person at heart."
        "How long have you been arguing about this?":
            bill "Er..."
            camilo "Um..."
            bill "Half an hour?"
            camilo "Give or take."
            s3_mc "Honestly, you boys!"

    camilo "Reminds me of a joke."
    camilo "Hey [s3_name], what do you call a noble hot sauce?"

    # CHOICE
    menu:
        thought "What do you call a noble hot sauce?"
        "King Hot Sauce":
            camilo "That's not exactly a punchline, is it?"
            s3_mc "Hey, it fits the brief, doesn't it?"
            camilo "I guess so. Apart from not being a joke!"
            s3_mc "Come on then, what's the real punchline?"
            camilo "Sir Racha!"
        "Aristobasco":
            camilo "Aw, that's actually better than what I was gonna say."
            camilo "You're so funny!"
            s3_mc "I try my best."
            s3_mc "Come on then, what's the real punchline?"
            camilo "Sir Racha!"
        "Sir Racha":
            camilo "Aw, you knew it already."
            s3_mc "Yeah, my friend's boyfriend told it to me. He loves sriracha."
            s3_mc "I can pretend I didn't know it if you like?"
            camilo "OK."
            s3_mc "I don't know, what do you call a noble hot sauce?"
            camilo "Sir Racha!"

    bill "Give me strength."
    bill "Hot sauce doesn't even make a good joke, mate."
    "He turns to you before Camilo can respond."
    bill "So how goes the grafting?"

    # CHOICE
    menu:
        thought "What should I do?"
        "Flirt with Camilo":
            $ s3_mc.like("Camilo")
            s3_mc "Pretty well. I managed to grab some alone time with a guy I'm really into?"
            "You lightly stroke Camilo's leg with your foot. When he looks at you, you give him your best sexy eyes."
            s3_mc "Maybe next time we chat it'll be a different kind of saucy."
            camilo "Mint."
            camilo "You know, like mint sauce."
            s3_mc "Very good."
            "Bill raises his eyebrows and gives you a look."
            thought "Oh, this is kinda awkward with Bill here..."
        "Flirt with Bill":
            $ s3_mc.like("Bill")
            s3_mc "I haven't spent time with the one person I really want to."
            "You lightly stroke Bill's leg with your foot. When he looks at you, you give him your best sexy eyes."
            s3_mc "Maybe next time we chat it'll be a different kind of saucy."
            bill "You still won't find a better sauce than mayo."
            s3_mc "No, Bill, I'm flirting with you."
            bill "Obviously I know that!"
            bill "I'm just messing with you."
            "Camilo makes a kissy face."
            s3_mc "Way to kill the mood, Camilo!"
            "Bill looks at Camilo and rolls his eyes."
        "Play it cool":
            s3_mc "I'd say I'm doing OK."
            s3_mc "How are things going with you boys?"
            camilo "S'alright. Iona's really fun, but she's a bit of a handful."
            camilo "I tend to go for girls with a bit more chill."
            bill "Miki's a really sweet girl. It's been fun so far, but we're fairly different."
            # SUB-CHOICE
            menu:
                thought "That doesn't sound like they're completely sure..."
                "I'd chill with Camilo any day":
                    $ s3_mc.like("Camilo")
                    "You stare steadily at Camilo."
                    "He sees you looking and winks."
                    s3_mc "Well, I hope things improve for you lads."
                "I'd show Bill how fun I can be":
                    $ s3_mc.like("Bill")
                    "You stare steadily at Bill."
                    "He sees you looking and tilts his head slightly."
                    s3_mc "Well, I hope things improve for you lads."
                "I hope things improve for them":
                    s3_mc "Well, I hope things improve for you lads."

    s3_mc "Right, I'm going to let you get back to your argument."
    s3_mc "See you around, boys."
    bill "See you."
    camilo "Later!"

    return

# iona and miki at pool (s3e3p1_pool)
label s3e3p1_pool:
    scene s3-poolside-day with dissolve
    $ new_scene()
    $ s3e3p1_visited.append("Pool")

    "Iona and Miki are having a swim. Harry is lounging by the pool."
    harry "Hey, [s3_name]. How's it going?"
    s3_mc "Not too bad."
    s3_mc "The sun's shining, I'm free and single, and I've got a Villa full of hotties to graft on."
    s3_mc "Still, it'd be nice to have something to cuddle up with."
    harry "Anyone particular in mind?"

    # CHOICE
    menu:
        thought "Who am I interested in?"
        "You":
            $ s3_mc.like("Harry")
            $ s3_like_harry = True
            "He grins."
            harry "That's well good news."
            if s3_mc.current_partner == "Harry":
                harry "I was worried you might have changed your mind. "
                s3_mc "Nope."
            harry "I'm into you as well, obviously."
            s3_mc "Don't let Genevieve hear you say that."
            harry "Hey, it's early days. Genevieve is great but I fancy the pants off you too."
            harry "You're total fresh mozzarella."
        "One of the other boys":
            $ s3_like_harry = False
            if s3_mc.current_partner == "Harry":
                "He looks a little disappointed."
                harry "Cool. I just thought..."
                harry "Never mind."
            harry "The other guys are great. They feel like bros already!"
            harry "And I know they all think you're fresh mozzarella."
        "AJ" if s3_like_aj:
            harry "AJ's really cool. I find her really easy to talk to."
            harry "She's never a downer, you know?"
            harry "Chatting with her always gets me pumped up and excited about whatever's going on."
            harry "And I know she thinks you're fresh mozzarella."
        "Nobody's really turned my head yet":
            $ s3_like_harry = False
            if s3_mc.current_partner == "Harry":
                harry "Oh.. I see."
                harry "I just thought..."
                harry "Never mind."
            harry "There are bound to be some more peeps along soon, right?"
            # SUB-CHOICE
            menu:
                s3_mc "Yeah. I hope someone turns up who's..."
                "Cute and likes dogs":
                    $ s3_mc.like("Ciaran")
                "Charming and sporty":
                    $ s3_mc.like("Tai")
                "Mysterious and musical":
                    $ s3_mc.like("Yasmin");
            s3_mc "And they like me, too!"
            harry "Don't worry. You are fresh mozzarella"

    s3_mc "Fresh mozzarella?"
    harry "Oh, soz, it's a thing from my uni mates."
    harry "It means, like, you know. A really, really fit girl."
    s3_mc "That's good then."
    s3_mc "I think..."

    "Suddenly, cool water splashes your sun-warmed skin."
    "Miki's face pops up from the edge of the pool with a mischievous grin on her face. Iona is bobbing behind her."
    miki "Come on in! The water's so nice."

    # CHOICE
    menu:
        thought "Should I join them in the pool?"
        "Jump in and splash Harry":
            $ s3e3p1_get_in_pool = True
            "You take a running jump and land in the pool with a mighty splash. Iona and Miki laugh."
            harry "Hey!"
            "Harry's soaking wet."
            s3_mc "Oops, sorry!"
            thought "I didn't think it would be that big..."
            harry "It's OK. I'm going to go find a towel and dry off."
            "He gets up and quickly walks off."
            s3_mc "I feel bad..."
            iona "He'll be fine. It's just a bit of water."
        "Get in sexily" if s3_like_harry == True:
            $ s3e3p1_get_in_pool = True
            "You slide into the pool, making sure Harry is watching. You really take your time."
            "When you're finished, he applauds. Miki and Iona join in."
            "You do a little bow as best you can in the pool."
            harry "That was... wow."
            "You give him your best sexy smile and stick your tongue out."
            "Harry gets up."
            harry "I think I'm gonna see what's Viv up to."
            bill "Bye!"
            "He heads off towards the kitchen quite quickly."
            iona "That poor boy's gonna need a cold shower."
        "Politely decline":
            $ s3e3p1_get_in_pool = False
            s3_mc "I'm good, thanks. I'm actually going to go have a bit of a wander."
            miki "All right! Bye bye!"
            iona "Catch you later."
            harry "Later, [s3_name]."

    if s3e3p1_get_in_pool:
        iona "Thanks for joining us, [s3_name]."
        iona "Maybe now I won't have to hear anything more about this fandan Lorenzo Martinez."
        miki "Hey! He's not a fandan!"
        miki "...What's a fandan?"
        iona "A fandan's a silk-shirt-wearing scunner."
        miki "OK... And what's a scunner?"
        iona "The kinda lad who'd take Carla Montano to dinner right before she was due to marry his evil twin brother disguised as his cousin."
        miki "Oh, I get it!"
        iona "Oh no, you talked about it so much that it got into my brain!"
        iona "I hope it didn't replace something important..."
        miki "You have to watch 'Amor en el Rancho', both of you."
        miki "It's this amazing Telenovela."
        miki "You'd love it. I promise. There's so much drama!"
        # SUB-CHOICE
        menu:
            thought "Miki wants me to watch a Telenovela called 'Amor en el Rancho'..."
            "I've seen every episode":
                miki "Oh my gosh, yay!"
                miki "Sometimes I pretend I'm Zelda."
                s3_mc "Me too, babes."
                iona "Both of you lasses are lovely as you are."
                s3_mc "Yeah, but Zelda is Zelda."
                "Miki nods in agreement."
            "It's not really my thing":
                miki "Oh... I guess it's a bit silly..."
                s3_mc "There's nothing wrong with liking fun TV programmes!"
                s3_mc "Telenovelas just aren't my thing, really."
                s3_mc "I'm more of a 'Dragon's Game' kind of person!"
                iona "Now that's a quality show."
                iona "Though this Amor thing is starting to sound intriguing..."
            "Sounds interesting...":
                miki "Oh, it is. Trust me."
                iona "I think I might be interested as well."
                iona "Group watch after we get out of here?"
                miki "Definitely."
                s3_mc "You're on!"
            "What's a Telenovela?":
                s3_mc "I've never heard of this thing."
                miki "Yeah, they're not such a big deal in the UK I think."
                miki "They're basically these really schmaltzy romantic TV soaps."
                miki "They're huge in Spain and South America. Once you get hooked there's like this whole world to explore."
                iona "Group watch after we get out of here?"
                miki "Definitely."
                s3_mc "You're on!"

        "You splash about with Miki and Iona for a bit, competing to see who can make the biggest wave with their arms."
        # SUB-CHOICE
        menu:
            s3_mc "Forget telenovela characters! I wanna be..."
            "A dolphin!":
                "You swim as fast as you can towards the other end of the pool, and Iona and Miki join you."
                "Despite your head start, Iona nearly catches up."
                s3_mc "Phew, you're good at this!"
                iona "Me and my family used to go wild swimming in Loch Morlich, up in the Carnigorms."
                iona "You have to be fast or you turn into an ice cube."
                iona "We're spoiled with this heated malarkey!"
            "A mermaid!":
                miki "I used to dream I'd wake up one day and be a mermaid."
                iona "Aw, that's cute. As a little girl?"
                miki "...yes. I definitely didn't make a video about wanting to be a mermaid last year."
                s3_mc "I think it would be great. How does that song go?"
                s3_mc "Something about it being really awesome under the water?"
                iona "I think I know the one you mean."
            "An octopus!":
                "You swim after Miki and Iona, waving your arms like an octopus."
                "They laugh and try to get away from you, but you manage to catch them. It turns into an impromptu game of octopus tag."

        iona "Phew all that splashing about made me hungry."
        iona "I'm gonna go hunt down some brekkie."
        miki "Ooh, me too."
        "The three of you get out of the pool. Miki and Iona head off to the Villa."

    return

label s3e3p1_ending:
    scene s3-kitchen-day with dissolve
    $ new_scene()

    "You find Genevieve in the kitchen."
    "The air sizzles with the sound and scent of frying onions."
    genevieve "Oh, hey [s3_name]. I thought I'd make some breakfast for everyone."
    genevieve "This is my famous Indian Frittata. I make a big one almost every week and take it cold to work."
    "She tips a bowl of ground spices into the pan. While the onions brown, Genevieve starts beating eggs."

    # CHOICE
    menu:
        s3_mc "It looks..."
        "Amazing":
            genevieve "Thanks!"
            genevieve "It's usually pretty popular when I make it for parties."
        "Very spicy...":
            genevieve "Well that depends on your definition of 'very spicy', I suppose..."
            genevieve "I'd describe it as 'just right'."
        "Kind of weird":
            genevieve "Well, that's fair enough."
            genevieve "Spicy eggs and cabbage aren't for anyone, I suppose."

    harry "What smells so good?"
    genevieve "Hey, babe! I'm just whipping up a frittata for everyone."
    harry "Awesome. I'm starving!"
    genevieve "Could you pass me the coriander?"
    "Harry looks doubtful for a second."
    harry "Um, sure. Here you go."
    genevieve "Right, it's just about done."
    genevieve "I'm gonna let it rest a bit while I go freshen up."
    genevieve "Make sure it doesn't run off, OK?"
    harry "Run off?"
    genevieve "Or someone might eat it, I don't know."
    genevieve "Either way, keep an eye on it, yeah?"
    harry "Sure thing."
    "Genevieve heads inside."
    $ leaving("genevieve")
    
    "Harry turns to you with a glum look on his face."
    s3_mc "What's up?"
    harry "I didn't want to say it to Viv, but I really hate coriander."
    harry "It tastes like soap."
    harry "I don't think I can eat this."
    s3_mc "Oh no! It looks so good!"
    harry "Yeah... I guess I'll just have bread. Again."
    "He starts slicing the end off yesterday's bread."
    thought "He's just going to eat bread? By itself? That's really tragic."

    # CHOICE
    menu:
        thought "Maybe I could win him over with my cooking skills?"
        "Teach him to make something":
            $ s3_mc.like("Harry")
            $ s3e3p1_teach_harry = True
            s3_mc "Why don't I teach you something?"
            harry "Seriously?"
            harry "That would be mint."

            # SUB-CHOICE
            menu:
                s3_mc "How about..."
                "French toast":
                    $ s3e3p1_harry_bfast = "french toast"
                    harry "Sounds good!"
                    harry "I love French toast, but I never knew how to make it."
                "American pancakes":
                    $ s3e3p1_harry_bfast = "American pancakes"
                    harry "Sounds good!"
                    harry "I think I made British-style ones once."
                    harry "But I always wanted to know how to make the fluffy ones!"
                "Poached eggs on toast":
                    $ s3e3p1_harry_bfast = "poached eggs on toast"
                    harry "I love poached eggs!"
                    harry "They're pretty tricky, though, right?"
                    s3_mc "Don't worry. There's a knack to it."
                "Vegan American pancakes":
                    $ s3e3p1_harry_bfast = "vegan American pancakes"
                    harry "Sounds good!"
                    harry "I think I made British-style ones once."
                    harry "But I always wanted to know how to make the fluffy ones!"

            # SUB-CHOICE
            menu:
                thought "What's my approach here?"
                "A serious lesson":
                    "You take your time working through all the steps, making sure Harry's following along."
                    harry "Hey, this is actually pretty easy when you know how to do it."
                    s3_mc "You're a quick learner!"
                "Have a laugh":
                    "You and Harry joke around in the kitchen. You pretend to toss an egg across to him."
                    harry "Wait!"
                    s3_mc "Don't worry, I wasn't really going to throw it!"
                    "You go put the egg on the counter, but misjudge it and drop the egg straight onto the floor."
                    "Both of you dissolve into hopeless giggles as you try and clean up the egg."
                "Make it flirty and sexy":
                    "You stand behind Harry as he uses the pan and put your hands on his, pressing into his body from behind."
                    "He looks back over his shoulder at you and smiles. You push a little closer, feeling the warmth of his skin on yours."
                    harry "Hi."
                    s3_mc "Hi."
                    "The spell is broken as the pan starts spitting."
                    "You cough."
                    s3_mc "Anyway, now for the next step..."

            "When you've finished making breakfast, the two of you grab a plate and eat together."
            "You put down your fork and notice Harry looking at you."
            harry "Hey, [s3_name]..."
            s3_mc "Yeah?"
            harry "I know I'm coupled up with Genevieve, but you and me... there's a spark there. "
            harry "Right?"

            # SUB-CHOICE
            menu:
                "Harry says he feels a spark between us..."
                "You're not really my type, sorry":
                    $ s3_mc.dislike("Harry")
                    "His face falls."
                    harry "Oh. OK. That's fair enough."
                    harry "I had to give it a shot, you know."
                    s3_mc "Genevieve's well fit, though."
                    harry "Yeah, you're right."
                "Maybe, but I can't do that to Genevieve":
                    $ s3_mc.dislike("Harry")
                    s3_mc "Sorry, but Viv's one of my closest friends in here."
                    s3_mc "I think you're really great, but I can't go behind her back like that."
                    harry "Girl code, right?"
                    s3_mc "Something like that, yeah."
                    harry "I understand."
                "I feel it too":
                    $ s3_mc.like("Harry")
                    s3_mc "I'd like to see where things go with us."
                    harry "Oh wow."
                    "Harry smiles confidently at you, but his cheeks are a little pink."
                    harry "I've been really looking forward to getting some alone time with you."
                    # SUB-CHOICE
                    menu:
                        thought "How do I feel about alone time with Harry?"
                        "I wish it could have been sooner":
                            harry "Yeah. I've barely been able to keep my eyes off you this whole time, though."
                            harry "I think you're super fit. Like wow!"
                            "He moves towards you. His aftershave is bright and citrusy."
                            s3_mc "You smell like a lemon. A good lemon."
                            "He laughs."
                            harry "I'll take it."
                        "Are you blushing?":
                            "He blushes even more."
                            harry "I can't help it! You're just so... fit."
                            s3_mc "It's nice to know I have an effect on you."
                            harry "You do."
                            harry "You defo do."
                        "Let's sing a song to celebrate":
                            harry "A song?"
                            s3_mc "Yeah! Why not?"
                            "He starts to sing. His voice isn't good, exactly, but he's really confident."
                            harry "Harry and [s3_name], together, at last..."
                            harry "Singing  song..."
                            harry "Having a blast!"
                            "He looks really proud of finding a rhyme."
                            s3_mc "Very good."

                    "Suddenly, you both realise how close you are. The air is warm and soft around you."
                    # SUB-CHOICE
                    menu:
                        thought "Harry is really close..."
                        "Kiss him":
                            "You push up against his lean body and put your arms around his neck."
                            harry "Hi there."
                            "He puts his hands on your waist. You lean towards him, your lips meet, and for a moment, that's all there is in the world."
                            "He kisses you passionately, like he's never wanted anything more than this."
                            "Eventually, you stop kissing and the real world comes back into focus."
                            harry "Woah."
                            s3_mc "Yeah. That was pretty special."
                            s3_mc "I can't wait to get to know you."
                        "Pull him closer":
                            "You pull him in gently, letting a slight smile play over your lips."
                            "Harry wastes no time in moving in and kissing you. For a moment, that's all there is in the world."
                            "He kisses you passionately, like he's never wanted anything more than this."
                            "Eventually, you stop kissing and the real world comes back into focus."
                            harry "Woah."
                            s3_mc "Yeah. That was pretty special."
                            s3_mc "I can't wait to get to know you."
                        "Pull away for now":
                            "You gently pull back and Harry smiles at you reassuringly."
                            s3_mc "Let's talk for a bit."
                            harry "Sure thing."

                    # SUB-CHOICE
                    menu:
                        thought "I'm gonna ask him an intimate question..."
                        "Do you have a sex playlist?":
                            harry "Oh yeah. Doesn't everyone?"
                            s3_mc "What's on it?"
                            harry "I usually listen to movie soundtracks. Thriller and superhero soundtracks. "
                            harry "It makes things seem so much more epic!"
                            harry "And then you both feel awesome, like you're saving the world."
                            harry "What songs get you in the mood?"
                            # SUB-CHOICE 
                            menu:
                                thought "The songs I find sexiest tend to be..."
                                "Fast and exciting":
                                    pass
                                "Smooth and chilled":
                                    pass
                                "Up-tempo and bouncy":
                                    pass
                            harry "I'll bear that in mind."
                        "What was your first time like?":
                            harry "It was really good."
                            harry "Well, as good as first times can be."
                            s3_mc "Who was it with?"
                            harry "A girl called Clare. We weren't dating really, but she was a friend of my sister's and we'd liked each other for ages."
                            s3_mc "That's nice."
                            harry "Yeah, it was. If you're friends first I think it makes the sex way better."
                            s3_mc "Maybe we'd better become good friends, then."
                            "He blushes."
                            harry "I feel like we already are."
                            harry "What was your first time like?"
                            # SUB-CHOICE
                            menu:
                                thought "How was my first time?"
                                "It was great":
                                    s3_mc "It was very nice as well."
                                    harry "That's good. You deserve the best."
                                    s3_mc "Well, 'best' might be stretching it!"
                                "Like most first times: short":
                                    "He laughs."
                                    harry "Yeah... I'd be lying if I said mine wasn't the same!"
                                "I don't want to talk about it":
                                    "He touches your arm lightly."
                                    harry "That's OK. We don't have to."
                        "What's your favourite sex position?":
                            harry "Straight to the point."
                            s3_mc "It's how I roll."
                            "He grins."
                            harry "Works for me."
                            harry "So... it's not exactly a position, but there is something I really like."
                            s3_mc "What is it? I'm curious."
                            harry "Roleplay. I think it's really fun."
                            s3_mc "Like, acting out sexy situations in bed?"
                            harry "Yeah, basically."
                            # SUB-CHOICE
                            menu:
                                "Harry likes roleplay..."
                                "Like what?":
                                    harry "Now that'd be telling."
                                "Me too!":
                                    harry "Are you kidding?"
                                    s3_mc "Nope. Maybe it's something we can explore together."
                                    harry "I'd love that."
                                "Isn't it a bit weird?":
                                    harry "Nah, it's so much fun."
                                    harry "You just have to give it a go."
                                    s3_mc "Well maybe I could be convinced..."
                                    s3_mc "We'll just have to see, won't we?"

                    "Harry grins at you, and smooths down his hair with one hand."
                    harry "I hope we get to spend more time together."
                    harry "Away from the others."
                    # SUB-CHOICE
                    menu:
                        thought "Harry wants to spend more time with me..."
                        "I'd like to get to know you better":
                            "You smile at him."
                            s3_mc "I'm looking forward to learning more about you."
                            s3_mc "I haven't quite figured you out yet. I like that."
                            harry "That's because I'm a man of mystery. Like a super spy."
                            s3_mc "A super spy who actually has respect for women. What a concept!"
                            "You both laugh."
                            harry "This is going to be fun. "
                        "Who knows what could happen":
                            "You run your finger along his collarbone and lightly brush it down his chest."
                            s3_mc "Play your cards right and maybe next time we can..."
                            s3_mc "Get to know each other a little better."
                            harry "I'd enjoy that."
                            harry "I'd really enjoy that. Like, a lot."
                            s3_mc "I guess we'll see, won't we?"
                            harry "This going to be fun. "
                        "Maybe we should sneak out":
                            harry "Like, away from the Villa?"
                            s3_mc "We'll slip past the cameras, jump the wall and make our getaway across the sea."
                            harry "I know a guy who's in mega-yachts. I'm sure I could pull a few strings."
                            s3_mc "And then away we go, making our mega-escape in mega-luxury together."
                            harry "I wish we could do that..."
                            s3_mc "Well, we'll have to make the most of our alone time, won't we?"
                            "He grins."
                            harry "This is going to be fun. "


            "You and Harry finish your breakfast."
            harry "This is so good. I can't believe I half-made it."
            s3_mc "I bet you'll be able to make it yourself next time."
            harry "I dunno, I might need an amazingly hot girl helping every time."
            s3_mc "Well maybe that can be arranged."
            "You begin clearing the plates away."

        "Watch him eat his sad breakfast":
            "Harry manages to find some butter. He slowly eats his toast with an air of resignation."

    "Eventually, Genevieve comes back into the kitchen, and shouts out across the lawn."
    genevieve "Who wants breakfast?!"
    camilo "That smells amazing!"
    nicky "What a treat."
    genevieve "I made enough for everyone, so help yourselves."
    
    if s3e3p1_teach_harry:
        "Everyone apart from you and Harry takes a slice of frittata and sits or stands around munching down on it. "
        genevieve "Not hungry, guys?"
        harry "Um, nope."
        s3_mc "Me too."
        genevieve "Oh well, more for everyone else, I guess!"
        "You give Harry a sly wink and he grins back at you."
        aj "This is amazing, thanks Viv!"
    else:
        "Everyone apart from Harry takes a slice of frittata and sits or stands around munching down on it."
        genevieve "Not hungry, Harry?"
        harry "Um, nope."
        s3_mc "This is amazing, thanks babes."

    genevieve "You're welcome!"
    elladine "Yeah, seriously amazing."
    genevieve "Oh, it's me! Guys, I've got a text!"
    text "Islanders, it's time to take an old favourite and make it better. Gather in the garden and get ready for a game of Truth and Dare! #allin #nohalfmeasures"
    "Everyone starts talking at once."
    genevieve "Truth and Dare?"
    "Hey, save me some of the frittata, will you?"
    "They can't hear me. They'll probably save me some anyway because we're such good mates."
    "Aren't we, guys?"
    "They still can't hear me."

    scene sand with dissolve
    $ on_screen = []

    "Coming up, the Islanders get up to what can only be called 'shenanigans' in a game of 'Truth and Dare'!"
    "And we introduce a new Islander. He sounds exactly like Bill, behaves exactly like Bill, but is a lot more handsome than Bill."
    bill "Hello?"
    "Until next time!"

    jump s3e3p2

    return

#########################################################################
## Episode 3, Part 2
#########################################################################
label s3e3p2:
    scene sand with dissolve
    $ on_screen = []

    show screen day_title(3, 2) with Pause(4)
    hide screen day_title with dissolve

    "Previously, the Islanders discussed sexy dreams..."
    
    elladine "I don't remember the details."
    $ leaving("elladine")

    "And [s3_name], Genevieve, and AJ got physical..."
    "In an arm wrestling competition!"
    aj "Wanna try your luck?"
    $ leaving("aj")

    "You're on, AJ."
    "I've been single forever."
    "Which means I have a distinct advantage when it comes to arm wrestling with my right hand."
    "Coming up!"
    "The Islanders get stuck in a game of Truth and Dare."
    camilo "What are you doing down there?"
    $ leaving("camilo")

    "And Bill is looking a little pail..."
    show bill bucket at npc_center
    $ leaving("bill")

    "Sorry Bill, can't help you there."
    "The last time I did a dare..."
    "I ended up having to be a voice over for ten people in their swimwear."
    "Here comes [s3_name], AJ, Camilo, Harry, Bill, Genevieve, Elladine, Nicky, Seb and Iona."
    "They're raring to get daring!"
    "Sigh."
    "I wonder if I'll ever escape."

    scene s3-sun-loungers-day with dissolve
    $ new_scene()

    "You shield your eyes from the hot summer sun as the other Islanders hurry over."
    "Nicky is sipping from his water bottle."

    # ADD BACK ONCE MC HAS IMAGES
    # nicky "Is that the sun that's making me all hot, or is it just MC? "
    # nicky "Ha! Just kidding. But seriously, I love the swimsuit today. You look great!"
    # s3_mc "Aw, thanks Nicky!"
    # nicky "I know you don't need to, but MC, you could totally get away with something more adventurous."
    # nicky "Not that you don't already look beautiful, of course."
    # s3_mc "Aw, thanks Nicky!"

    nicky "So, what's the stitch?"
    bill "I guess we have to wait for another..."
    s3_mc "Text!"
    bill "What does it say?"
    text "Islanders, you will each be competing to complete three secret dares. The first Islander to complete all their dares will be the winner. #daretowin #dontyoudare"
    camilo "Ooh, spicy."
    harry "Healthy competition. I love it."
    aj "I've got a text."
    elladine "Same."
    "All of the Islanders look at their phones. Everyone seems to have a different dare."
    iona "Oh, this is going to be easy."
    elladine "How the heck am I going to get someone to do that?"
    "Your phone goes off again in your hand."
    thought "This must be my dare."
    text "[s3_name], your first dare is to get another Islander to give you a massage, and to make sex noises while they do it."

    # CHOICE
    menu:
        thought "I've got to make sex noises while someone massages me."
        "I could do that in my sleep":
            thought "This is going to be easy."
        "This is going to be embarrassing":
            thought "I'm never going to live this down!"
        "Finally! Unleash the she-wolf":
            "You howl like a wolf."
            "The other Islanders turn to look at you."
            genevieve "You alright, hun?"
            s3_mc "Just limbering up, babe."

    "Iona walks over to Nicky."
    iona "What's that over there, Nicky?"
    "Nicky turns around. Iona snatches his water bottle and quickly backs away from him."
    nicky "Huh?"
    "Iona receives another text. She reads it while backing away from Nicky."
    iona "One dare down."
    iona "Two to go!"
    "She runs off into the Villa laughing."
    nicky "OK, what just happened?"

    # CHOICE
    menu:
        thought "Iona just stole Nicky's water bottle..."
        "That must have been her first dare":
            s3_mc "She's got a head start."
            elladine "[s3_name] is right."
        "Offer him your water bottle":
            $ s3_mc.like("Nicky")
            s3_mc "You can use mine if you need to stay hydrated."
            nicky "Aw, thanks [s3_name]!"
            nicky "But, like, why did she do that?"
            elladine "It's her dare, duh."
        "Iona is clearly very thirsty":
            s3_mc "Maybe she just needed some water, like, before the challenge."
            aj "Yeah! A Challenge is thirsty work."
            elladine "No, I bet that was her first dare."

    elladine "She's ahead of us all already!"
    harry "Looks like the game is on!"
    "The other Islanders all start to disperse around the Villa, laughing as they go."
    thought "Oh, I've got another text."
    thought "But I haven't done my first dare yet!"
    "You look down at your phone."
    text "[s3_name], As the only single Islander in the Villa you have the chance to accept a secret dare. You can try and kiss other Islanders...as long as they want you to of course!"
    text "Each time you kiss an Islander, it will count as one point. This is your chance to get grafting and win the challenge! #getkissywithit #throwkissestothewind"
    thought "Nice! I can finally do some cheeky flirting with some of the Islanders..."
    thought "And win the challenge!"
    thought "Well, I'm pretty sure I've got a few keen admirers here..."
    thought "So I'm sure that wouldn't be a problem."

    # CHOICE
    menu:
        thought "Maybe I should take this opportunity to graft!"
        "Let's get kissing!":
            $ s3e3p2_getting_kissy = True
            thought "Who wouldn't want an excuse to go around kissing this gorgeous lot?"
            thought "I'm so down for this."

        "Nah, I don't want to kiss anyone":
            $ s3e3p2_getting_kissy = False
            thought "I think I'll pass."

    "You see Iona chasing Nicky with a broom across the lawn."
    thought "I better get cracking if I want to win this challenge!"

    call screen s3e3p2_select_who_to_talk_to

    text "[s3_name], your next dare is to lick the face of another Islander #putyourneckintoit"

    # CHOICE
    menu:
        thought "I have to lick someone's face!"
        "I hope they all use lotion":
            thought "I need a smooth surface area to get a good licking."
        "Let's get licking!":
            thought "Time to lick, lick, lick!"
        "Gross. Ew. Yuck.":
            "You shudder."
            thought "This is so weird!"

    call screen s3e3p2_select_who_to_talk_to

    text "[s3_name], your next dare is to suck the toe of another Islanders. #taketoetotown"

    # CHOICE
    menu: 
        thought "I need to suck a toe..."
        "This is a hard one":
            thought "Yuck."
            thought "This challenge just climbed onto a whole new level of hard."
        "This is a gross one":
            thought "Yuck."
            thought "This challenge just climbed onto a whole new level of hard."
        "This is my dream come true":
            thought "I am so excited to suck a toe!"

    call screen s3e3p2_select_who_to_talk_to

    if s3e3p2_getting_kissy:
        call screen s3e3p2_select_who_to_talk_to

    jump s3e3p2_ending
    return

label s3e3p2_lounge:
    scene s3-lounge as dissolve
    $ new_scene()
    $ s3e3p2_dare_count += 1
    $ s3e3p2_visited.append("Lounge")

    "Someone is slumped on the sofa with a bucket on their head."
    bill bucket "Hello?"
    bill bucket "Is anybody there?"
    bill "It's me!"
    s3_mc "Hello me."
    bill "[s3_name]?"
    bill "It's Bill!"
    bill "Help."
    bill "I'm stuck!"

    # CHOICE
    menu:
        thought "Bill's got his head stuck in a bucket."
        "Try and help him get out of the bucket":
            s3_mc "I'll help you Bill."
            "You tug on the bucket but it's stuck."
            bill "It's no use."
        "Laugh at him and his helplessness":
            s3_mc "How are you stuck? It's a bucket!"
            bill "Don't laugh at me!"
        "Ask how he got in this situation":
            s3_mc "How did you get yourself into this situation?"

    bill "It was sort of a dare."
    bill "But it went wrong."
    bill "If that wasn't already obvious."

    thought "Maybe I could do my dare on Bill..."
    thought "I'm sure it'll still count...even with a bucket on his head!"

    # CHOICE
    menu:
        thought "What should I do with Bill?"
        "Kiss Bill's bucket head" if s3e3p2_getting_kissy:
            $ s3e3p2_kiss_count += 1
            $ s3e3p2_kiss_bill = True
            s3_mc "I've got to say... you actually look so cute in that bucket."
            bill "Really?"
            s3_mc "Yeah. It's proper doing things to me."
            s3_mc "Mind if I kiss it?"
            bill "You want to kiss it?"
            s3_mc "Yeah. I want to kiss the bucket."
            bill "Um, sure. Why not?"
            bill "My lips are somewhere around here."
            "He points to the centre of the bucket."
            "You lean towards Bill and gently kiss where you think his lips are."
            "He pulls you closer, you straddle him on the sofa while you kiss the plastic bucket with passion."
            "The bucket clunks against the wall."
            bill "Ouch."
            thought "We'd better stop that before we get carried away."
            "You get off Bill. He rubs his bucket head."
            bill "Got to say... That was one of the hottest kisses I've ever had with a bucket on my head."
            bill "Not that I had loads of anything."
            bill "You can't see it, but I am proper hot under here after that."
        "Ask Bill for a massage" if s3e3p2_dare_count == 1:
            $ s3e3p2_completed_dare_count += 1
            $ s3e3p2_masseur = "Bill"
            s3_mc "Bill..."
            bill "Yeah?"
            s3_mc "Mind giving me a massage?"
            bill "What, right now?"
            bill "But I can't see!"
            s3_mc "You don't need to see. You just need to feel."
            bill "To be fair, I think my massages are actually, like, pretty decent quality."
            bill "Even with a bucket on my head."
            "You sit down in front of him. He starts massaging your earlobes by accident."
            "Though it actually feels quite good."
            s3_mc "Hmm..."
            s3_mc "Oh."
            s3_mc "Oh! Yes!"
            s3_mc "This feels so good."
            bill "You like that, huh?"
            s3_mc "Oh, yes! Hmm. Yes! Yes!"
            "Bill coughs awkwardly."
            bill "OK. I think you're all massaged out now."
            "You stand up feeling refreshed."
        "Lick Bill's bucket head" if s3e3p2_dare_count == 2:
            $ s3e3p2_completed_dare_count += 1
            "You lean forward and lick the bucket. The plastic is cold against your tongue."
            bill "What are you doing?"
            bill "Why can I hear you breathing?"
            bill "Is that your tongue?"
            "You pull away, your tongue a little dryer than before."
            s3_mc "Don't mind me."
            "Bill shakes his bucket head."
            bill "I don't know if I'm horrified or horny."
        "Suck Bill's toe" if s3e3p2_dare_count == 3:
            $ s3e3p2_completed_dare_count += 1
            "You kneel down beside his feet and pop his toe in your mouth."
            bill "Ahh!"
            "Bill leaps out of the chair and falls on the floor."
            bill "What the!?"
            s3_mc "Sorry Bill!"
            s3_mc "I didn't mean to scare you."
            "He shakes his head."
        "Draw a face on his bucket":
            $ s3e3p2_draw_on_bucket = True
            thought "Hmm... something is missing from that bucket."
            s3_mc "Wait right there, Bill."
            "You run up to the dressing room."
            thought "What do I need?"
            "You see an eyeliner."
            thought "Ah ha!"
            "You grab the eyeliner and run back downstairs to Bill."
            bill "Hello?"
            bill "[s3_name]?"
            bill "Are you still there?"
            s3_mc "Just hold still, Bill."
            "You draw a face on his bucket."

            $ bucket = "smile"

            s3_mc "There you go!"
            bill "Are you giving it a face?"
            s3_mc "Yeah!"
            bill "Argh."
        "Just leave him to it":
            "You let out an uncontrollable bubble of laughter. Bill sighs."

    bill "I need to try and get this thing off."
    "Bill walks off with his hands outstretched, trying not to bump into anything."

    return
    
label s3e3p2_bean_bags:
    scene s3-bean-bags-day with dissolve
    $ new_scene()
    $ s3e3p2_dare_count += 1
    $ s3e3p2_visited.append("Bean Bags")

    "AJ and Seb by the beanbags"
    "You wander over to AJ and Seb."
    "They are tied together with multiple pairs of G-strings."
    seb "I can't believe this."
    seb "She told me to stand still and close my eyes."
    seb "Next thing I know I'm tied to her by her knick-knocks."
    aj "To be clear, they're all fresh out of the laundry."

    # CHOICE
    menu:
        thought "AJ has tied Seb to her with her underwear!"
        "What a cute bonding exercise for you guys":
            aj "That's actually not what I was going for but..."
            aj "Yeah!"
            seb "I feel very..."
            seb "Bonded."
        "I wouldn't mind getting tangled up in AJ's underwear":
            if s3_like_aj:
                $ s3_mc.like("AJ")
                "AJ winks."
                aj "Easy tiger."
            else:
                "AJ and Seb laugh."
        "Why don't you just untie yourself?":
            seb "I tried."
            seb "But this girl seriously knows how to tie a knot."
            "AJ winks mischievously."

    seb "And why exactly am I tied up?"
    aj "Two stones, one bird."
    seb "That's not quite how the saying goes..."
    aj "Whatever. It's two of my dares in one!"
    aj "I first got a text saying I have to put some underwear on full display."
    aj "I got my pants out and started wearing them like a scarf."
    aj "And then I got another text saying I have to spend the afternoon tied up to an Islander."
    aj "So I combined the two!"
    "She grins, looking proud of herself."

    # CHOICE
    menu:
        thought "AJ's done two of her dares already!"
        "You're on a roll, babe":
            aj "You bet I am!"
        "Your dares were so easy":
            $ s3_mc.dislike("AJ")
            aj "Hey!"
            aj "You try and tie a constrictor knot with nothing but panties."
            aj "It's harder than it looks."
        "What are your dares, Seb?":
            "Seb frowns at you and AJ."

    seb "I'm not sure you're meant to, like, tell us what your dares are..."
    aj "Oh."

    thought "I could do one of my dares on AJ while she's tied up to Seb!"

    # CHOICE
    menu:
        thought "What dare should I do?"
        "Kiss AJ" if s3e3p2_getting_kissy and s3_mc.bisexual:
            $ s3e3p2_kiss_count += 1
            $ s3_mc.like("AJ")
            s3_mc "You can help me out with one of my dares if you like, AJ."
            aj "Sure, what is it?"
            "You whisper in her ear."
            s3_mc "To kiss you."
            seb "Again with the telling and the dares?"
            "AJ nudges Seb playfully out of the way."
            aj "Shush you."
            "She leans towards you and closes her eyes."
            "Your lips meet. Her free hand travels down to your lower back, pulling you closer towards her."
            "The rest of the Villa melts away for a moment."
            "Eventually AJ pulls away."
            aj "Woah."
            "Seb coughs awkwardly."
            seb "Ehem."
            "AJ is blushing profusely."
            aj "Sorry, mate!"
            "Seb laughs and tickles her."
            seb "I think AJ's got a crush."
            aj "Stop! I'm so ticklish."
        "Ask AJ for massage" if s3e3p2_dare_count == 1:
            $ s3e3p2_completed_dare_count += 1
            $ s3e3p2_masseur = "AJ"
            s3_mc "Hey AJ."
            s3_mc "Reckon you could, like, give me a massage?"
            "She smiles and scootches Seb out of the way a little."
            aj "Sure can."
            aj "I can give great head massages."
            "You lean your head back. AJs voice drops into a silky smooth and calming tone."
            aj "Great. Let's begin."
            "Her fingertips dance circles around your scalp."
            aj "How's the pressure?"
            s3_mc "It's nice! Wow. Oh, AJ, you're really good."
            "You let out a moan of pleasure."
            aj "You like that, don't you?"
            s3_mc "Oh. Oh!"
            s3_mc "Oh, yeah. That's good."
            aj "Yeah?"
            s3_mc "Oh! Yes! Yes!"
            "AJ stops and starts laughing uncontrollably."
            seb "OK. Seriously. What is going on?!"
            s3_mc "Don't stop, babe. Don't stop."
            s3_mc "Please! I'm so close."
            "AJ howls with laughter."
            seb "I can't believe what I'm hearing."
            seb "Is AJ really that good at massages?"
            aj "I'm sorry, [s3_name]. I can't go on!"
        "Lick AJ's face" if s3e3p2_dare_count == 2:
            $ s3e3p2_completed_dare_count += 1
            s3_mc "I'm sorry, AJ!"
            "You lean in and lick the side of her face."
            seb "Um, woah."
            aj "Ew! That's so wet!"
            aj "It tickles!"
        "Suck AJ's toe" if s3e3p2_dare_count == 3:
            $ s3e3p2_completed_dare_count += 1
            "You kneel down beside AJ."
            seb "Are you proposing to us, [s3_name]?"
            s3_mc "Not exactly..."
            "You take off AJ's sandal."
            aj "Oh, am I Cinderella?"
            aj "Are you my Princess Charming?"
            "You stick her toe in your mouth."
            seb "Oh, OK."
            "She squeals loudly and falls to the floor, dragging Seb with her."
            aj "[s3_name]!"
            s3_mc "Umm?"
            seb "What are you doing?"
            aj "She's put my toe... in her mouth!"
            seb "I can see that. But, like, why?"
            aj "Ahh, stop. It tickles!"
            "She yanks her toe out of your mouth, laughing uncontrollably."
            aj "It tickled so much!"
        "Hypnotise Seb to find out his dares":
            $ s3e3p2_hypnotise_seb = True
            "You start pretending to hypnotise him with your finger, swaying it from side to side in front of his eyes."
            s3_mc "Look into my eyes and tell us."
            s3_mc "Tell us."
            s3_mc "Tell us."
            "AJ starts giggling uncontrollably at your hypnotic attempts. Seb crosses his arms and shakes his head."
            seb "No."
        "Just leave them to it":
            "Seb is trying to undo one of the knots."
            seb "Argh, it's too tight!"
            "AJ starts giggling uncontrollably at Seb's frustration."
            s3_mc "I think I'm going to go..."

    "AJ falls over into a heap of giggles."
    "A pair of pants split in half."
    aj "No!"
    aj "I might not win the challenge now."
    aj "We need to back up pants, Seb."
    aj "Pronto!"
    seb "Really?"
    "Seb groans. AJ drags Seb into the Villa."

    return

label s3e3p2_pool:
    scene s3-poolside-day with dissolve
    $ new_scene()
    $ s3e3p2_dare_count += 1
    $ s3e3p2_visited.append("Pool")

    "You walk over to Nicky and Camilo. Nicky is wearing bright pink lipstick and holding a broom."
    camilo "Hey, [s3_name]!"
    "Camilo adjusts his shorts."
    camilo "Y'know, silk feels really good against my skin."
    camilo "It's so comfy."
    s3_mc "What are you on about?"
    "He winks and pulls down an inch of his swim shorts, revealing a pair of lacy pants."

    # CHOICE
    menu:
        thought "Camilo is wearing a girl's pair of underwear!"
        "They look so hot on you, Camilo":
            $ s3_mc.like("Camilo")
            camilo "You think?"
            s3_mc "Totally."
            s3_mc "I wish I could get a view of the whole package."
            "Camilo winks."
            camilo "Maybe one day."
            camilo "They're Iona's. I'm borrowing them."
        "Did you get dressed in the dark?":
            "Camilo shrugs."
            camilo "No, of course not."
            camilo "They're Iona's. I'm borrowing them."
        "Whose underwear are they?":
            camilo "They're Iona's. I'm borrowing them."

    thought "Camilo looks like he'd be up for a dare..."

    # CHOICE
    menu:
        thought "What should I do?"
        "Kiss Camilo" if s3e3p2_getting_kissy:
            $ s3_mc.like("Camilo")
            $ s3e3p2_kiss_count += 1
            $ s3e3p2_kiss_camilo = True
            "You bite your bottom lip."
            s3_mc "Fancy a quick kiss?"
            "Camilo raises an eyebrow and steps closer."
            camilo "Why?"
            camilo "These pants doing it for you?"
            s3_mc "Oh yeah."
            camilo "Go on then."
            "You lean in and kiss him."
            "Camilo's hands pull you in closer to him."
            "His warmth radiates around you as he kisses you harder."
            nicky "Guys!"
            "You both pull away. Camilo rolls his eyes at Nicky."
            nicky "I hope Iona didn't see that."
            camilo "Get on with your cleaning, Nicky, and mind your own business."
            "Nicky gives Camilo a little scowl before diving back under."
            show nicky at npc_exit
            pause .3
            $ renpy.hide("nicky")
            $ on_screen.remove("nicky")

            show camilo at move_center

            camilo "That was a good kiss, [s3_name]."
            s3_mc "I try my best."
            "Camilo squints a little bit, looking a tad uncomfortable."
            s3_mc "Are you alright?"
            camilo "Yeah, yeah that kiss was amazing..."
            camilo "But downstairs is getting a little tight."
            s3_mc "Oh, the pants?"
            "He lunges to the side, nodding."
            camilo "Yeah..."
            camilo "I'm going to go and sort them out."
            camilo "But seriously, wow. What a kiss."
            "Camilo hobbles over to the Villa."
            thought "I wonder who else I can get my kiss on with..."
        "Ask Camilo for a massage" if s3e3p2_dare_count == 1:
            $ s3e3p2_completed_dare_count += 1
            $ s3e3p2_interact_camilo = True
            $ s3e3p2_masseur = "Camilo"
            s3_mc "Speaking of feeling comfy..."
            s3_mc "I could really do with a massage."
            camilo "Say no more."
            "He sits down cross legged and pats the floor in front of him."
            camilo "I can take care of that."
            "You sit down in between his legs. He works his way around your shoulders."
            "His hands are strong. Powerful."
            "You instantly feel at ease and you start to let out moans of pleasure."
            s3_mc "Oh. Oh!"
            s3_mc "Oh."
            camilo "You like that, huh?"
            s3_mc "Oh, yes! Yes, Camilo! Yes!"
            camilo "Yeah, does that feel good?"
            s3_mc "It feels so good. Oh, wow."
            s3_mc "Oh."
            s3_mc "Oh!"
            s3_mc "Oooooh."
            nicky "Get a room you two!"
            camilo "You love it, mate."
            iona "What's going on here, babe?"
            camilo "Just giving [s3_name] the massage of her life."
            iona "Mind if i get in on that?"
            "She gives you a little glare."
            iona "Inside."
            "Camilo gets up. He stretches out a hand and helps you up from the ground."
            camilo "Sorry, [s3_name]."
            camilo "Supply and demand."
            "He winks at you and struts over to the Villa with Iona."
        "Lick Camilo's face" if s3e3p2_dare_count == 2:
            $ s3e3p2_completed_dare_count += 1
            $ s3e3p2_interact_camilo = True
            "You step closer to Camilo."
            camilo "Um... you OK, [s3_name]?"
            "You nod as you lean in towards him and lick his forehead."
            camilo "Um..."
            camilo "Ew!"
            "He quickly rubs the wet patch with his arm and wipes it back on you."
            camilo "Not today, satan. Not today."
            "Camilo walks off into the Villa, still rubbing at his forehead, looking back at you to make sure you're not following him."
            thought "Oops. He didn't like that!"
        "Suck Camilo's toe" if s3e3p2_dare_count == 3:
            $ s3e3p2_completed_dare_count += 1
            $ s3e3p2_interact_camilo = True
            "You kneel down on the floor."
            camilo "Did you drop something?"
            s3_mc "Not exactly..."
            "You pick up his foot."
            camilo "That's my foot, [s3_name]."
            s3_mc "I know."
            "You put his little toe in your mouth."
            camilo "And now you're eating my toe!"
            camilo "Nicky, mate, she's eating my toe."
            camilo "Help!"
            "Nicky doesn't hear him. He's swimming underwater. You take Camilo's toe out of your mouth."
            camilo "I think my whole life just flashed before my eyes."
            "He legs it back into the Villa, slightly hopping on one leg."
            s3_mc "Oops."
        "Get him to do a catwalk":
            $ s3e3p2_interact_camilo = True
            s3_mc "Come on, Camilo."
            s3_mc "Give us a strut."
            camilo "Sure."
            "He struts up and down the pool while posing sexily."
            camilo "I am serving up Iona-Underwear realness with this look."
            s3_mc "Yes, Camilo."
            s3_mc "Work it from head to toe."
            "He pivots but stumbles slightly."
            camilo "Oh."
            camilo "Ouch."
            camilo "Um..."
            camilo "I'll see you around, [s3_name]."
            camilo "I've got to go and untuck something in the lounge."
            "Camilo limps off into the Villa."
        "Just leave him to it":
            s3_mc "You do you, Camilo."
            camilo "Sure thing."
            "He heads off into the Villa, lunging from side to side."
    
    return

label s3e3p2_kitchen:
    scene s3-kitchen-day with dissolve
    $ new_scene()
    $ s3e3p2_dare_count += 1
    $ s3e3p2_visited.append("Kitchen")

    "Genevieve seems to be bending over in front of Harry, grinding against him."
    "Harry sees you and nervously laughs."
    harry "Um... oh, hi [s3_name]."
    "He quickly moves to one side. Genevieve nearly falls over."
    genevieve "Harry! Why'd you move?"
    genevieve "I was just getting started the grind-a-thon!"

    # CHOICE
    menu:
        thought "Harry and Genevieve are doing a grind-a-thon"
        "What is that?":
            "Genevieve winks and taps her nose."
            harry "It's apparently this proper competition."
            s3_mc "Oh, really?"
        "Can I join in the grind-a-thon?":
            genevieve "Sure!"
            "Harry's face flushes red."
            harry "Um, OK. Let's win this grind-a-thon!"
            "You rub against Harry."
            "Genevieve does the same. He squirms with excitement."
            harry "It's my lucky day."
        "I should do a dare on Harry":
            thought "I wonder how I can do it with Genevieve here..."

    harry "After this grind-a-thon I am going to be way too tired to, like, move."
    harry "If someone wants to give me a piggyback that would be awesome."
    "Genevieve leans over to you and whispers in your ear."
    genevieve "You know this grind-a-thon isn't a real thing, right?"
    "She grins a little suspiciously."
    thought "I bet this is her dare."
    thought "I better do a dare so Genevieve doesn't take the lead."

    # CHOICE
    menu:
        thought "What should I do to Harry?"
        "Kiss Harry" if s3e3p2_getting_kissy:
            $ s3_mc.like("Harry")
            $ s3e3p2_kiss_harry = True
            $ s3e3p2_kiss_count += 1
            thought "I'll need to distract Genevieve."
            "You clutch your mouth dramatically."
            s3_mc "Ouch."
            s3_mc "Um, Genevieve..."
            s3_mc "Could you get me a toothpick or something?"
            genevieve "Sure! I'll go and get that."
            s3_mc "Mind if we have a cheeky kiss while we're alone?"
            harry "Oh!"
            "Harry looks a little taken aback, but smiles cheekily."
            harry "Don't you, like, want to get whatever is in your teeth out first?"
            s3_mc "That was just a decoy to distract."
            harry "Oh, right. Sneaky."
            harry "Well, then... yeah, sure, why not?"
            "He looks around, making sure Genevieve hasn't come back."
            harry "A kiss in the kitchen won't hurt."
            "You lean and kiss Harry on the lips."
            "He's hesitant at first. But his touch is soft and gentle."
            "He moves in closer, exploring your body with his hands."
            "As you pull away just as Genevieve comes back in."
            genevieve "Sorry, babe."
            "Harry flushes red. He looks apologetically at you and whispers in your ear."
            harry "Damn."
            genevieve "I couldn't find the toothpick."
            s3_mc "Aw, don't worry hun."
            s3_mc "I got what I wanted."
            genevieve "What?"
            harry "Um..."
            s3_mc "I mean, I got it out. "
            genevieve "Ah, right."
        "Ask Harry for a massage" if s3e3p2_dare_count == 1:
            $ s3e3p2_completed_dare_count += 1
            $ s3e3p2_masseur = "Harry"
            "You stretch out your arms and yawn."
            s3_mc "You know what we could also do?"
            harry "What?"
            s3_mc "I bet you give the best massages, Harry."
            harry "Like a massage-a-thon."
            s3_mc "Yeah, sure...."
            "Harry pretends to roll up his sleeves and flexes his muscles."
            harry "Let me put my skills to the test."
            "His fingers work their way down from your upper back. They instantly ease you of your stresses."
            s3_mc "Oh..."
            s3_mc "Oh, yes!"
            s3_mc "Right there."
            harry "There?"
            s3_mc "Yes! Yeah, right, oh wow."
            genevieve "Um."
            genevieve "Can I get in on some of that?"
            "Harry goes to move to Genevieve, but you pull him back."
            s3_mc "No, don't stop Harry, please, don't stop. Oh. Wow! Yes! Yes! Yes!"
            "You close your eyes, enjoying the moment of fake pleasure."
            harry "I mean, I knew I was good but..."
            "Genevieve scoffs."
            genevieve "It sounds like [s3_name] really enjoyed that."
        "Lick Harry's face" if s3e3p2_dare_count == 2:
            $ s3e3p2_completed_dare_count += 1
            "You stick your tongue out and lick his face."
            genevieve "Um!?"
            "Harry squeals with delight."
            harry "Oooh!"
            genevieve "You hungry, [s3_name]?"
            s3_mc "I guess I am a little."
            genevieve "Well there is a whole kitchen here."
            genevieve "Harry isn't for eating!"
            "Harry laughs."
            harry "That made me feel all tingly inside."
        "Suck Harry's toe" if s3e3p2_dare_count == 3:
            $ s3e3p2_completed_dare_count += 1
            $ s3_mc.like("Harry")
            "You get down on one knee and pick up Harry's foot."
            "He loses his balance, but quickly grabs the kitchen counter."
            harry "Um, [s3_name]?"
            harry "That's not how people give you a piggy back."
            "You pinch one of his toes."
            s3_mc "This little piggy went to the market..."
            "You pinch another, bigger toe."
            s3_mc "And this little piggy went in my mouth."
            harry "What?"
            "You put his toe in your mouth."
            "He squeals like a pig."
            harry "Aaah!"
            genevieve "What are you doing, [s3_name]?"
            "You keep sucking. Harry doesn't move. It feels like he relaxes into it."
            harry "Ooh."
            harry "Ooh, that feels kinda good."
            "You take Harry's toe out of your mouth and stand up."
            genevieve "Can't believe what I just witnessed."
            "Harry regains his balance, looking a little lustful."
            harry "I really need someone to carry me after that."
        "Give him a piggyback":
            "You hoist him up on your back and run a few lengths around the kitchen."
            harry "Yes!"
            harry "Giddy up!"
            "He starts to slip from your grip."
            harry "Ahh!"
            "He falls to the ground."
            harry "Ouch."
            "He looks over at Genevieve."
        "Leave them to their grind-a-thon":
            harry "Genevieve, you wanna give me a ride-a-thon?"

    "Genevieve gestures to her back."
    genevieve "You still want that ride?"
    genevieve "Hop on, Harry."
    genevieve "I'll carry you, hun."
    "Harry grins."

    if s3e3p2_kiss_harry:
        "As he climbs onto Genevieve's back he glances over at you."
        "A lustful look still caught in his eyes."
        harry "OK. Let's ride."
    
    return

label s3e3p2_ending:
    if s3e3p2_draw_on_bucket:
        $ bucket = "smile-kiss"
    else:
        $ bucket = "kiss"

    if s3e3p2_getting_kissy == False and s3e3p2_dare_count == 3:
        thought "I've finished my last dare!"
        thought "I wonder what I have to do..."

    "A text tone interrupts you mid thought."
    s3_mc "I've got a text!"
    text "Islanders, the winner of the challenge has been decided. Please make your way to the lawn. #thewinnertakesitall"

    if s3e3p2_getting_kissy == False and s3e3p2_dare_count == 3:
        thought "Ooh, I hope it was me who managed to do three dares first!"
    elif s3e3p2_getting_kissy == True or s3e3p2_dare_count != 3:
        thought "Oh, I guess it's time to see who won the challenge."

    "You head over to the lawn."

    scene s3-lawn-day with dissolve
    $ new_scene()

    "AJ and Seb are still tied together."
    "She giggles."

    if "Bean Bags" in s3e3p2_visited:  
        s3_mc "You patched up your pants then, AJ? "
        aj "Yeah."
        aj "I didn't manage to do my final dare though."
        seb "Sorry babe."

        if s3e3p2_hypnotise_seb:
            seb "Don't try hypnotising me again, please, [s3_name]."
            seb "It was a mockery to the art form."

    "Camilo runs over, followed by Harry and Nicky."

    if s3e3p2_interact_camilo:
        "Camilo tries to avoid your eye contact."
    elif s3e3p2_kiss_camilo:
        "He blushes a little when he sees you."

    "Nicky's lipstick looks a little smudged."
    miki "That's a good lipstick shade on you, Nicky."
    "Bill is being guided by Genevieve and Miki."
    "The bucket is still on his head."

    if s3e3p2_draw_on_bucket:
        miki "Aw, someone drew a face on you, hun!"
        bill bucket "That would be that cheeky one."
        "He points randomly towards no one."
        s3_mc "He means me."
        miki "It's cute!"
    
    "And he is covered with bright pink lipstick kisses."

    # CHOICE
    menu:
        thought "Bill has been kissed all over!"
        "I wish got to kiss him" if s3e3p2_getting_kissy == False:
            "Maybe I should have accepted that secret kissy dare after all."
        "I don't remember kissing him everywhere!" if s3e3p2_kiss_bill:
            pass
        "Who did this to you, Bill?":
            pass
        "I'd give anything to be that bucket right now":
            thought "What a lucky piece of plastic."

    "Nicky chuckles."
    bill bucket "Nicky?"
    "Bill wanders around a little aimlessly."
    bill bucket "You coming back for round two?"
    nicky "Don't want to smudge my lippy any more, mate."

    if s3e3p2_kiss_count > 0:
        thought "I hope my lipstick isn't smudged after all that kissing."

    if s3e3p2_completed_dare_count >= 3:
        $ s3e3p2_win_challenge = True
        "Looks like all that toe sucking, face licking and massage moaning wasn't for nothing."
    elif s3e3p2_kiss_count > 1:
        $ s3e3p2_win_challenge = True
        "Looks like [s3_name] got her kiss on in this challenge."
        "And it was worth it!"
    else:
        $ s3e3p2_win_challenge = False

    if s3e3p2_win_challenge:
        "Cue the text!"
        s3_mc "I've got a text!"

        text "[s3_name], congratulations! You are the winner of the Truth And Dare challenge. As the winner, you now get to ask one other Islander a truth."
        text " You may only ask the Islanders who completed fewer than two dares. These Islanders are AJ, Bill, Camilo and Harry. #tellitstraighttomyface"
        thought "I won!"

        "AJ, Bill, Camilo and Harry step forward."
        aj "Looks like you've got the power, [s3_name]."
        bill "What do you want to know?"
        iona "Make it juicy, [s3_name]!"
        genevieve "Yeah, find out some good gossip."

        # CHOICE
        menu:
            thought "Who should I ask?"
            "AJ":
                $ s3e3p2_ask_question = "AJ"
            "Bill":
                $ s3e3p2_ask_question = "Bill"
            "Harry":
                $ s3e3p2_ask_question = "Harry"
            "Camilo":
                $ s3e3p2_ask_question = "Camilo"

        $ pronouns(s3e3p2_ask_question)

        if s3e3p2_ask_question == "AJ":
            s3_mc "[s3e3p2_ask_question]! Please step forward."
            "[s3e3p2_ask_question] steps forward, hands on [his_her] hips."
            aj "Come on then. Let's have it."
        elif s3e3p2_ask_question == "Bill":
            s3_mc "[s3e3p2_ask_question]! Please step forward."
            "[s3e3p2_ask_question] steps forward, hands on [his_her] hips."
            bill "Come on then. Let's have it."
        elif s3e3p2_ask_question == "Camilo":
            s3_mc "[s3e3p2_ask_question]! Please step forward."
            "[s3e3p2_ask_question] steps forward, hands on [his_her] hips."
            camilo "Come on then. Let's have it."
        elif s3e3p2_ask_question == "Harry":
            s3_mc "[s3e3p2_ask_question]! Please step forward."
            "[s3e3p2_ask_question] steps forward, hands on [his_her] hips."
            harry "Come on then. Let's have it."

        # CHOICE
        menu:
            thought "What should I ask [s3e3p2_ask_question]?"
            "What is your wildest sexy fantasy?":
                "[s3e3p2_ask_question] laughs."

                if s3e3p2_ask_question == "AJ":
                    aj "Think you lot can handle it?"
                    s3_mc "Try us."
                    aj "I really want to do it in one of those bath tubs in the middle of a room, with like, super big windows."
                    seb "Woah!"
                    aj "But I want the hotel room to be, like, really high up so no one sees us."
                    harry "People flying drones might catch you."
                    aj "Yeah, the risk is still there, obviously, for maximum hotness."
                    "Everyone cheers for AJ."
                    aj "Feels good to get that off my chest."
                elif s3e3p2_ask_question == "Bill":
                    bill "Think you lot can handle it?"
                    s3_mc "Try us."
                    bill "I want to order every single dinner off the menu down the pub."
                    "Camilo scoffs."
                    camilo "No change there then."
                    miki "Yeah, what's sexy about that?"
                    bill "Oh, we'll get it all delivered to my room and be, like, naked while we eat it."
                    miki "Brilliant."
                    "Everyone cheers for Bill."
                    bill "Feels good to get that off my chest."
                elif s3e3p2_ask_question == "Camilo":
                    camilo "Think you lot can handle it?"
                    s3_mc "Try us."
                    camilo "I want to do it with a weather person."
                    s3_mc "On TV?!"
                    camilo "Yeah."
                    camilo "They always know what's coming."
                    camilo "Just when they're announcing that it's wet outside."
                    iona "Golden sunshine with a chance of showers."
                    camilo "Exactly."
                    "Everyone cheers for Camilo."
                    camilo "Feels good to get that off my chest."
                elif s3e3p2_ask_question == "Harry":
                    harry "Think you lot can handle it?"
                    s3_mc "Try us."
                    harry "I want to have sex in an elevator."
                    harry "So I can say I'm up and coming."
                    "Genevieve scoffs."
                    genevieve "Course you do, Harry."
                    "Everyone cheers for Harry."
                    harry "Feels good to get that off my chest."
                        
                elladine "You are filthy, babe."
            "What turns you on and what turns you off?":
                if s3e3p2_ask_question == "AJ":
                    aj "Oh, good question."
                    aj "I love watching a girl work out, like, intensely."
                    aj "Also when smart people tell stuff in a way that doesn't make me feel, like, silly."
                    aj "Smart people can be super hot."
                    aj "I'm not sure about my turn offs."
                    aj "Maybe, like, if people are unkind or snobby. I'm not too keen on that."
                    seb "Yeah, I get that."
                elif s3e3p2_ask_question == "Bill":
                    bill "Oh, good question."
                    bill "My ultimate turn offs are loud eaters and drama seekers."
                    bill "My turns on are people that like going to the pub for a date."
                    bill "And someone that is just happy to spend a lazy Sunday just playing video games."
                    "Miki rolls her eyes."
                    miki "You've got low expectations, darling."
                elif s3e3p2_ask_question == "Camilo":
                    camilo "Oh, good question."
                    camilo "I love it when people are, like, kinda competitive and strong."
                    s3_mc "And what turns you off?"
                    camilo "When people are controlling."
                    camilo "Can't stand that."
                    bill "Good answer, mate."
                    "Iona scoffs."
                    iona "You could have just said 'me'. But whatever."
                elif s3e3p2_ask_question == "Harry":
                    harry "Oh, good question."
                    harry "I get well turned on when girls, wear, like, formalwear."
                    genevieve "Oh, really?"
                    genevieve "That's random."
                    genevieve "I don't usually wear that kind of thing."
                    "Harry shrugs."
                    harry "Turns off would have be when people take things for granted. I can't stand that."
                
            "If I was a food, what would I be, and how would you eat me?":
                "Everyone laughs at your question. [s3e3p2_ask_question] looks a little concerned."

                if s3e3p2_ask_question == "AJ":
                    aj "OK. That's kind of random."
                    "You shrug."
                    s3_mc "I'm just asking the important questions here."
                    aj "I think you'd be a pomegranate sorbet with sliced strawberries on top."
                    aj "Sweet and cool."
                    aj "And I'd lick you all up."
                elif s3e3p2_ask_question == "Bill":
                    bill "OK. That's kind of random."
                    "You shrug."
                    s3_mc "I'm just asking the important questions here."
                    bill "You'd be sweet potato fries and I'd eat you with some homemade mayo."
                    s3_mc "Why potato fries?"
                    bill "Because, like, the upgraded version of any dish has sweet potato fries with it."
                    bill "And you're, like, totally an upgrade."
                    "Miki and Genevieve look a little defensive."
                    genevieve "An upgrade from what?"
                    bill "Um, like, just in general."
                    miki "Right..."
                elif s3e3p2_ask_question == "Camilo":
                    camilo "OK. That's kind of random."
                    "You shrug."
                    s3_mc "I'm just asking the important questions here."
                    camilo "You'd be sweet potato fries and I'd eat you with some homemade mayo."
                    s3_mc "Why potato fries?"
                    camilo "Because, like, the upgraded version of any dish has sweet potato fries with it."
                    camilo "And you're, like, totally an upgrade."
                    "Miki and Genevieve look a little defensive."
                    genevieve "An upgrade from what?"
                    camilo "Um, like, just in general."
                    miki "Right..."
                elif s3e3p2_ask_question == "Harry":
                    harry "OK. That's kind of random."
                    "You shrug."
                    s3_mc "I'm just asking the important questions here."
                    harry "I think you'd be a pomegranate sorbet with sliced strawberries on top."
                    harry "Sweet and cool."
                    harry "And I'd lick you all up."

        # CHOICE
        menu:
            s3_mc "[s3e3p2_ask_question]'s answer was..."
            "A good truthful answer":
                s3_mc "You really bared your soul to me and I appreciate that."

                if s3e3p2_ask_question == "Bill":
                    "Bill does a little bow."
                    bill "You'll have to trust me that I'm smiling."
                else:
                    "[s3e3p2_ask_question] smiles and does a little bow. The others laugh and cheer [him_her] on."
                
            "Pure and utter complete filth":
                "You pretend to wipe [s3e3p2_ask_question] down."

                if s3e3p2_ask_question == "AJ":
                    aj "What are you doing?"
                    s3_mc "Just cleaning you up."
                    s3_mc "Because you are serving some filth!"
                    aj "How?"
                    s3_mc "I can read between the lines."
                    aj "Nope, sorry. You've lost me there."
                elif s3e3p2_ask_question == "Bill":
                    bill "What are you doing?"
                    s3_mc "Just cleaning you up."
                    s3_mc "Because you are serving some filth!"
                    "Everyone laughs."
                    "Bill brushes himself off."
                    bill "I know, I know. I'm pure dirt."
                elif s3e3p2_ask_question == "Camilo":
                    camilo "What are you doing?"
                    s3_mc "Just cleaning you up."
                    s3_mc "Because you are serving some filth!"
                    "Everyone laughs."
                    "Camilo brushes himself off."
                    camilo "I know, I know. I'm pure dirt."
                elif s3e3p2_ask_question == "Harry":
                    harry "What are you doing?"
                    s3_mc "Just cleaning you up."
                    s3_mc "Because you are serving some filth!"
                    harry "How?"
                    s3_mc "I can read between the lines."
                    "Harry winks at you."
                    harry "You get me too well."
            "So weak! I want another go":
                s3_mc "That answer was weak sauce, and you know it!"
                "You stomp your feet."
                s3_mc "I want another question."
                "[s3e3p2_ask_question] looks a little hurt. Everyone looks at each other awkwardly."
                "[s3_mc.bff] laughs and nudges you."
                if s3_mc.bff == "Genevieve":
                    genevieve "I don't think that's how the game works, [s3_name]."
                elif s3_mc.bff == "Elladine":
                    elladine "I don't think that's how the game works, [s3_name]."
                elif s3_mc.bff == "Nicky":
                    nicky "I don't think that's how the game works, [s3_name]."
                elif s3_mc.bff == "Seb":
                    seb "I don't think that's how the game works, [s3_name]."
                s3_mc "Aw..."
    else:
        iona "I've got a text!"
        text "Iona, congratulations! You are the winner of the dares challenge. You now get to ask one other Islander a truth. #Tellitstraighttomyface"

        # CHOICE
        menu:
            thought "Iona won!"
            "It's totally rigged":
                pass
            "I hope she has a good question":
                pass
            "She had a head start":
                pass
        
        "Iona smiles at you all mischievously."
        nicky "Who are you going to ask, Iona?"
        "She struts over to Camilo."
        iona "OK hun."
        iona "I want to know exactly what you look for in a woman."
        "He looks over to you for a brief moment."
        camilo "Um..."
        iona "Come on."
        "Iona taps her foot."
        iona "We haven't got all day."
        camilo "I guess I like girls who are chill."
        "Iona's foot taps quicker."
        camilo "And, like, not controlling or people who think that they're better than anyone else."
        "The guys cheer. Iona looks a little cross."
        bill "Good answer mate."
        seb "Yeah, no one likes superiority complex."
        iona "Yeah, well, the right answer was me."
        iona "But whatever."
        "Camilo rolls his eyes."

    nicky "I've got a text!"
    text "Islanders, tonight is a recoupling. The boys will be picking who they want to couple up with. Please get ready and gather around the firepit. #gentlemenschoice"
    "Everyone is silent for a moment."
    aj "Uh oh."
    thought "A boy's choice recoupling."
    "Then, all at once, the boys cheer."
    camilo "Get in!"
    thought "Who's going to pick me?"
    "Everyone looks at you."
    s3_mc "Oh!"
    s3_mc "I've got a text as well..."
    text "[s3_name], as the only single Islander you also will be choosing in tonight's recoupling. You will be picking first. #firstcomesfirstserve #ladiesfirst"
    s3_mc "I get to choose someone"
    s3_mc "And I'm picking first."
    "Iona crosses her arms. Genevieve nervously bites her nails."
    "The boys all look at one another."
    thought "It's about time!"
    "[s3_name] is absolutely right."
    "It is about time!"

    scene sand with dissolve
    $ on_screen = []

    "Coming up..."
    aj "Alright, lads! Excited for this?"
    $ leaving("aj")

    "Excited is an understatement."
    "This is a recoupling, people!"
    
    elladine "And the most exciting part of the recoupling is what comes after."
    $ leaving("elladine")
    "Don't worry, Elladine. I'll make sure someone stocks up the fruit bowl."

    jump s3e3p3

    return

#########################################################################
## Episode 3, Part 3
#########################################################################

label s3e3p3:
    scene sand with dissolve
    $ on_screen = []

    show screen day_title(3, 3) with Pause(4)
    hide screen day_title with dissolve

    "Last time on Love Island..."
    "The Islanders played a bit of Truth and Dare, and it all went as smoothly as you'd imagine."
    bill "I was starting to feel dizzy."
    nicky "Don't want to smudge my lippy any more, mate."
    $ leaving("bill")
    $ leaving("nicky")

    "I play Truth and Dare every time I make a cup of tea."
    "The Dare is to put milk in it, even though that bottle's been in there for weeks."
    "The Truth is that I need to make some changes in my life."
    "Anyway, tonight..."
    "It's recoupling time!"
    "This time it's the boys' turn to pick...but they'll have to get in line behind [s3_name]."
    "She's had a whale of a time being the only single girl, but now's the time to stop grafting and make a decision."
    "Are her wild days behind her? Or are they only just beginning?"
    "And who will she choose to couple up with?"

    $ s3_fav_li = favorite_li()

    s3_mc "I really hit it off with [s3_fav_li]..."

    "I remember the last time I had to make a big decision."
    "Was I going to stick with what I knew, and choose pepperoni?"
    "Or try something strange and new, and ask for pineapple on my pizza?"
    "I played it safe that time, but ever since then I've wondered..."
    "What if?"
    "What might my life have been like, if only I'd chosen differently that day?"
    "..."
    "I need to get out more."
    "There's an air of nervous excitement in the dressing room as the girls get ready for the recoupling."

    scene s3-dressing-room with dissolve
    $ new_scene()

    thought "This recoupling is a big deal."

    # Add back one MC has images in game
    # thought "So if there was a time to push the boat out, it's now..."
    # # MC outfit change to evening wear
    # thought "I've got compliments about this one before. It's tried and true. "
    # genevieve "The boys will love that, [s3_name]. Nice choice. "
    # genevieve "Wow, [s3_name]!"
    # genevieve "You look amazing!"
    # thought "Well, it's not like I need to turn heads when I'm the one picking."
    # genevieve "I'm sure I'll probably live to regret it, but you should really thinking about something more daring, babe!"
    # genevieve "You know, to get the boys' attention tonight. I know you could pull it off."
    # "You check out your look in the mirror and nod to yourself."
    # thought "Nice."

    "Miki peeks over your shoulder at her reflection and starts anxiously rearranging her hair."
    miki "I'm so nervous about tonight."
    miki "You're so lucky to get to choose first, [s3_name]."
    iona "Yeah, you're in the best position out of everyone!"
    genevieve "You must be on top of the world."

    # CHOICE
    menu:
        thought "How do I feel about the recoupling?"
        "I'm well excited":
            s3_mc "I've been looking forward to this since day one. It's gonna be great."
            elladine "Yeah it is, babes!"
        "I'm actually nervous":
            s3_mc "Just because I'm going first doesn't mean I can be all chill about it. Anything could still happen."
            elladine "I'm sure you'll be fine, babes."
        "I'm not sure yet":
            s3_mc "We haven't had a proper recoupling yet, so I'm not sure what to expect."
            elladine "I'm sure you'll be fine, babes."

    elladine "And the most exciting part of the recoupling is what comes after."
    elladine "Once you're safely coupled up, how are you going to celebrate?"

    # CHOICE
    menu:
        s3_mc "I want to celebrate the recoupling with..."
        "Some time alone with my partner":
            s3_mc "It'll be great to feel all cute and secure in a couple for once."
            s3_mc "No grafting, no pressure. Just the two of us, enjoying each other's company."
        "Some 'alone time' with my partner...":
            s3_mc "...if you know what I mean."
            elladine "Celebration bits?"
            s3_mc "Celebration bits."
        "An early night":
            s3_mc "I'm gonna need a rest after all this excitement."
            s3_mc "And it'll be great to finally have someone to share a bed with."

    if s3_mc.bff == "Genevieve":
        genevieve "That sounds so nice, babes."
    else:
        elladine "That sounds so nice, babes."

    $ leaving("genevieve")
    $ leaving("elladine")
    
    $ outfit = "evening"
    call customize_outfit from _call_customize_outfit_7

    "Iona mists herself with one last squirt of strawberry-scented perfume."
    iona "Right, is everyone ready?"
    miki "As I'll ever be!"
    aj "Then let's go, team!"
    "The six of you head out of the dressing room and towards the firepit."

    scene s3-firepit-night with dissolve
    $ new_scene()

    if s3_mc.bff == "Genevieve" or s3_mc.bff == "Elladine":
        "[s3_mc.bff] gives your hand a supportive squeeze as you."

    "There's the same nervous energy in the air at the firepit, where the boys are already waiting."
    "They all look impressed by your outfit. [s3_fav_li] even does a double take."

    if s3_fav_li == "AJ":
        aj "Wow, [s3_name]. Looking good."
    elif s3_fav_li == "Bill":
        bill "Wow, [s3_name]. Looking good."
    elif s3_fav_li == "Camilo":
        camilo "Wow, [s3_name]. Looking good."
    elif s3_fav_li == "Harry":
        harry "Wow, [s3_name]. Looking good."

    aj "Alright, lads! Excited for this?"
    harry "Of course!"
    "Harry grins, but you can tell he's worried."
    camilo "Excited, but a bit nervous as well, y'know?"
    bill "Yeah, I'm the same myself, to be honest."

    # CHOICE
    menu:
        thought "The boys seem a little bit nervous..."
        "Then let's hurry up and get on with it!":
            s3_mc "What are we waiting for?"
            elladine "A text?"
        "Don't stress boys, you'll be fine":
            s3_mc "Come on, boys."
            s3_mc "There's nothing to be scared of."
            s3_mc "You're the ones doing the choosing tonight, remember?"
            s3_mc "Well, once I had my go, obviously."
        "How about a group hug before we start?":
            $ s3_mc.like("Harry")
            $ s3_mc.like("Bill")
            $ s3_mc.like("Camilo")
            "You hold out your arms."
            s3_mc "Bring it in, guys."
            "Laughing, the other Islanders all crowd around in a group hug."
            harry "This is nice."
            bill "Yeah, I won't lie, this is actually making me feel better."
            camilo "You big softie, [s3_name]."

    "Everyone gets into position for the recoupling."
    "The boys sit around the firepit, and the girls stand opposite them in a row."
    "You sit with the boys."
    elladine "A text!"
    s3_mc "I think it was mine!"
    "You check your phone."
    text "[s3_name], as you are currently the only single Islander, you will be choosing first. Please tell the group who you'd like to couple up with and why."
    "A hush falls."
    "You step up to the fire and look at the boys lined up opposite you."
    thought "Here we go. Moment of truth."
    thought "It's pretty clear Bill, Camilo and Harry all fancy me."
    thought "So I can choose whichever one of them I like."
    thought "I'll be stealing someone's partner no matter who I pick, but there's no avoiding that."
    thought "Right. Let's do this."
    "You clear your throat and start your speech."
    s3_mc "Okay."

    # CHOICE
    menu:
        s3_mc "I want to couple up with this Islander because..."
        "They have great chat":
            s3_mc "When we talk, I'm always laughing or learning something new."
        "They're ridiculously fit":
            s3_mc "Just the hottest. Like, the kind of hot that has to be seen to be believed."
        "They're the whole package":
            s3_mc "Fit and funny and interesting all at once. I couldn't ask for anything more."

    # CHOICE
    menu: 
        s3_mc "And I'm looking forward to..."
        "Sharing a bed with this person":
            s3_mc "I'm done with sleeping alone."
        "Getting to know each other better":
            s3_mc "I've loved all our chats so far."
            s3_mc "I can't wait to spend more time together and see how that spark develops."
            s3_mc "I can't wait for tonight."
        "A long, happy future together":
            s3_mc "I know it's happened fast, but that's really how I feel."
            s3_mc "The connection we've made is already so strong."

    # CHOICE
    menu:
        s3_mc "So the Islander I want to couple up with is..."
        "Bill":
            $ s3_mc.current_partner = "Bill"
            $ s3_mc.past_partners.append("Bill")
            $ s3_mc.like_mc["Bill"] += 5
        "Harry":
            $ s3_mc.current_partner = "Harry"
            $ s3_mc.past_partners.append("Harry")
            $ s3_mc.like_mc["Harry"] += 5
        "Camilo":
            $ s3_mc.current_partner = "Camilo"
            $ s3_mc.past_partners.append("Camilo")
            $ s3_mc.like_mc["Camilo"] += 5
        "AJ" if s3_mc.bisexual:
            $ s3_mc.current_partner = "AJ"
            $ s3_mc.past_partners.append("AJ")
            $ s3_mc.like_mc["AJ"] += 5

    $ pronouns(s3_mc.current_partner)

    "[s3_mc.current_partner]'s face breaks into a big smile."

    if s3_mc.current_partner == "Bill":
        bill "Get in."
    elif s3_mc.current_partner == "Camilo":
        camilo "Get in."
    elif s3_mc.current_partner == "Harry":
        harry "Get in."
    elif s3_mc.current_partner == "AJ":
        aj "Get in."

    "[he_she!c] comes over to take your hand."

    # CHOICE
    menu:
        "[s3_mc.current_partner] seems pleased!"
        "Hug [him_her]":
            "You wrap your arms around [his_her] waist and squeeze."
            "[he_she!c] grins and squeezes you back."
        "Kiss [him_her]":
            $ s3_mc.like(s3_mc.current_partner)
            "You take [his_her] face in your hands and press a kiss to [his_her] lips."
            "You can feel [him_her] pressing back, smiling against your mouth."
        "Just sit down":
            pass

    "Together, you go to sit beside the firepit."

    if (s3_mc.bff == "Genevieve" and s3_mc.current_partner == "Harry") or (s3_mc.bff == "Seb" and s3_mc.current_partner == "AJ"):
        "The other Islanders are cheering and clapping for you"
    else:
        "The other Islanders are cheering and clapping for you, led by [s3_mc.bff], who gives a whoop of celebration." 

    if s3_mc.current_partner == "Bill":
        "As you take your seats, you see Miki biting her lip, looking down at the ground."
    elif s3_mc.current_partner == "Camilo":
        "As you take your seats, you see Iona biting her lip, looking down at the ground."
    elif s3_mc.current_partner == "Harry":
        "As you take your seats, you see Genevieve biting her lip, looking down at the ground."
    elif s3_mc.current_partner == "AJ":
        "As you take your seats, you see Seb biting his lip, looking down at the ground."

    "[s3_mc.current_partner] wraps an arm around your waist."
    "[he_she!c] whispers to you, [his_her] breath tickling sweetly against your neck..."

    if s3_mc.current_partner == "Bill":
        bill "Thank you for choosing me."
    elif s3_mc.current_partner == "Camilo":
        camilo "Thank you for choosing me."
    elif s3_mc.current_partner == "Harry":
        harry "Thank you for choosing me."
    elif s3_mc.current_partner == "AJ":
        aj "Thank you for choosing me."


    nicky "Hey, I've got a text."
    nicky "It's my turn to choose."
    "Nicky steps forward and looks at the remaining girls."
    nicky "OK, I've been proper thinking about this all day, 'cause I don't want to make this choice for the wrong reason."
    nicky "See, at first I was thinking, it'd be too easy to just choose this girl because I'm in my comfort zone with her."
    nicky "But then I realised that's actually exactly what I like about her."
    nicky "She does make me feel comfy. When I'm with her, I can be myself."
    nicky "So the girl I want to couple up with is..."
    nicky "Elladine."
    "Elladine squeals happily and throws her arms around Nicky's neck."
    "The two of them sit down next to you and [s3_mc.current_partner]."
    "[s3_mc.current_partner] whispers to you."

    if s3_mc.current_partner == "Bill":
        bill "This was a pretty good speech."
        bill "Not as good as yours, though."
    elif s3_mc.current_partner == "Camilo":
        camilo "This was a pretty good speech."
        camilo "Not as good as yours, though."
    elif s3_mc.current_partner == "Harry":
        harry "This was a pretty good speech."
        harry "Not as good as yours, though."
    elif s3_mc.current_partner == "AJ":
        aj "This was a pretty good speech."
        aj "Not as good as yours, though."

    # CHOICE
    menu:
        s3_mc "Nicky and Elladine..."
        "They make a good couple":
            s3_mc "I think they go really well together."
            s3_mc "We'll see them in the final for sure."
            if s3_mc.current_partner == "Bill":
                bill "I think you're probably right there..."
            elif s3_mc.current_partner == "Camilo":
                camilo "I think you're probably right there..."
            elif s3_mc.current_partner == "Harry":
                harry "I think you're probably right there..."
            elif s3_mc.current_partner == "AJ":
                aj "I think you're probably right there..."
        "They're totally fake":
            s3_mc "They're acting all cute now, but I'm not buying it. I don't think it'll last."
            if s3_mc.current_partner == "Bill":
                bill "Aw, I thought you and Elladine were mates."
            elif s3_mc.current_partner == "Camilo":
                camilo "Aw, I thought you and Elladine were mates."
            elif s3_mc.current_partner == "Harry":
                harry "Aw, I thought you and Elladine were mates."
            elif s3_mc.current_partner == "AJ":
                aj "Aw, I thought you and Elladine were mates."
            s3_mc "You can like two people separately without liking them together."
            s3_mc "I just don't buy it. There's no way they'd work outside of the Villa."
            if s3_mc.current_partner == "Bill":
                bill "If you say so..."
            elif s3_mc.current_partner == "Camilo":
                camilo "If you say so..."
            elif s3_mc.current_partner == "Harry":
                harry "If you say so..."
            elif s3_mc.current_partner == "AJ":
                aj "If you say so..."
        "They're not as cute as us":
            s3_mc "They're alright, but you and me take the top spot, no contest."
            if s3_mc.current_partner == "Bill":
                $ s3_mc.like("Bill")
                bill "Good answer."
            elif s3_mc.current_partner == "Camilo":
                $ s3_mc.like("Camilo")
                camilo "Good answer."
            elif s3_mc.current_partner == "Harry":
                $ s3_mc.like("Harry")
                harry "Good answer."
            elif s3_mc.current_partner == "AJ":
                $ s3_mc.like("AJ")
                aj "Good answer."

    "In turn, the remaining boys choose their partners."

    if s3_mc.current_partner != "Bill":
        bill "I was really flattered when this girl chose me, so now I get to return the favour."
        bill "The girl I want to couple up with is Miki."
        miki "Yay!"

    if s3_mc.current_partner != "Camilo":
        camilo "This girl is a legend, but we haven't actually spent that much quality time together yet."
        camilo "So the girl I want to couple up with is Iona."
        iona "Get in!"

    if s3_mc.current_partner != "Harry":
        harry "This girl is just the nicest human being. She's been a good partner to me over the past few days."
        harry "So the girl I want to couple up with is Genevieve."
        genevieve "Thanks, sweetheart."
        
    if s3_mc.current_partner != "AJ":
        seb "We're not into each other romantically, but she's an amazing human being and I'm really lucky to have her as a friend."
        seb "And I don't want her to be at risk at going home, because I know she'll find the right person for her any day now."
        seb "So the girl I want to couple up with is AJ."
        aj "Phew! Thanks, mate!"

    "AJ gives Seb a high five. Laughing, they sit down."
    "Finally, there are five couples sitting around the firepit."
    elladine "Is that everyone?"

    $ s3e3p3_lonely_one = s3_3rd_girl_options[s3_mc.current_partner]

    $ pronouns(s3e3p3_lonely_one)

    if s3_mc.current_partner == "Bill":
        bill "Wait...where's [s3e3p3_lonely_one]?"
    elif s3_mc.current_partner == "Camilo":
        camilo "Wait...where's [s3e3p3_lonely_one]?"
    elif s3_mc.current_partner == "Harry":
        harry "Wait...where's [s3e3p3_lonely_one]?"
    elif s3_mc.current_partner == "AJ":
        aj "Wait...where's [s3e3p3_lonely_one]?"


    nicky "[he_she!c]'s wandered off."
    elladine "Poor thing. [he_she!c] must be gutted."
    thought "Right, [s3e3p3_lonely_one] is single because nobody else ended up with [him_her] after I took [s3_mc.current_partner]."
    thought "I hope [he_she]'s alright..."
    "[s3_mc.current_partner] looks concerned."

    if s3_mc.current_partner == "Bill":
        bill "Me and [s3_name] should go check on [him_her]."
    elif s3_mc.current_partner == "Camilo":
        camilo "Me and [s3_name] should go check on [him_her]."
    elif s3_mc.current_partner == "Harry":
        harry "Me and [s3_name] should go check on [him_her]."
    elif s3_mc.current_partner == "AJ":
        aj "Me and [s3_name] should go check on [him_her]."
    
    elladine "Yeah, I think that'd be a good idea."

    # CHOICE
    menu:
        "[s3_mc.current_partner] wants us to go and check on [s3e3p3_lonely_one]..."
        "That's a good idea":
            $ s3_mc.like(s3_mc.current_partner)
            $ s3_mc.like(s3e3p3_lonely_one)
            s3_mc "Just to make sure [he_she]'s OK. We owe [him_her] that much."
            s3_mc "[s3_mc.bff] was there for me after the first recoupling, so I know what a difference it can make."
            if s3_mc.current_partner == "Bill":
                bill "Exactly."
            elif s3_mc.current_partner == "Camilo":
                camilo "Exactly."
            elif s3_mc.current_partner == "Harry":
                harry "Exactly."
            elif s3_mc.current_partner == "AJ":
                aj "Exactly."
        "I'd rather go alone":
            $ s3e3p3_go_alone = True
            $ s3_mc.like(s3_mc.current_partner)
            $ s3_mc.like(s3e3p3_lonely_one)
            s3_mc "I think I'm probably the one [he_she] wants to talk to right now."
            s3_mc "[s3_mc.bff] was there for me after the first recoupling, so I know what a difference it can make."
            if s3_mc.current_partner == "Bill":
                bill "That's so thoughtful, [s3_name]."
                bill "I'll see you in a bit, then, babe."
            elif s3_mc.current_partner == "Camilo":
                camilo "That's so thoughtful, [s3_name]."
                camilo "I'll see you in a bit, then, babe."
            elif s3_mc.current_partner == "Harry":
                harry "That's so thoughtful, [s3_name]."
                harry "I'll see you in a bit, then, babe."
            elif s3_mc.current_partner == "AJ":
                aj "That's so thoughtful, [s3_name]."
                aj "I'll see you in a bit, then, babe."
            "[s3_mc.current_partner] gives you a kiss on the cheek before you set off away from the firepit."
        "Ugh, do we have to?":
            $ s3_mc.dislike(s3_mc.current_partner)
            $ s3_mc.dislike(s3e3p3_lonely_one)
            if s3_mc.current_partner == "Bill":
                bill "I just want to make sure [he_she]'s OK. We owe her that much."
                bill "Remember how [s3_mc.bff] was there for you after the first recoupling?"
                bill "This is your chance to be that person for [s3e3p3_lonely_one]."
            elif s3_mc.current_partner == "Camilo":
                camilo "I just want to make sure [he_she]'s OK. We owe her that much."
                camilo "Remember how [s3_mc.bff] was there for you after the first recoupling?"
                camilo "This is your chance to be that person for [s3e3p3_lonely_one]."
            elif s3_mc.current_partner == "Harry":
                harry "I just want to make sure [he_she]'s OK. We owe her that much."
                harry "Remember how [s3_mc.bff] was there for you after the first recoupling?"
                harry "This is your chance to be that person for [s3e3p3_lonely_one]."
            elif s3_mc.current_partner == "AJ":
                aj "I just want to make sure [he_she]'s OK. We owe her that much."
                aj "Remember how [s3_mc.bff] was there for you after the first recoupling?"
                aj "This is your chance to be that person for [s3e3p3_lonely_one]."  
            s3_mc "Fine..."

    scene s3-poolside-night with dissolve
    $ new_scene()

    if s3e3p3_go_alone:
        $ s3_mc.like(s3e3p3_lonely_one)
        "You find [s3e3p3_lonely_one] sitting alone by the pool, lost in thought."
        "[he_she!c] jumps when you sit down next to [him_her]."

        if s3_mc.current_partner == "Bill":
            miki "Oh! Sorry, you scared me."
            miki "What are you doing here?"
        elif s3_mc.current_partner == "Camilo":
            iona "Oh! Sorry, you scared me."
            iona "What are you doing here?"
        elif s3_mc.current_partner == "Harry":
            genevieve "Oh! Sorry, you scared me."
            genevieve "What are you doing here?"
        elif s3_mc.current_partner == "AJ":
            seb "Oh! Sorry, you scared me."
            seb "What are you doing here?"

        s3_mc "I just thought I'd come and check on you."
        s3_mc "Y'know, to make sure you're feeling OK, after the recoupling."

        if s3_mc.current_partner == "Bill":
            miki "[s3_name]...that's really nice of you. Thank you."
        elif s3_mc.current_partner == "Camilo":
            iona "[s3_name]...that's really nice of you. Thank you."
        elif s3_mc.current_partner == "Harry":
            genevieve "[s3_name]...that's really nice of you. Thank you."
        elif s3_mc.current_partner == "AJ":
            seb "[s3_name]...that's really nice of you. Thank you."
        
    else:
        "With a smile, [s3_mc.current_partner] takes your arm and leads you away from the firepit."
        "You find [s3e3p3_lonely_one] sitting alone by the pool, lost in thought."
        "[he_she!c] jumps when you sit down next to [him_her]."
        if s3_mc.current_partner == "Bill":
            miki "Oh! Sorry, you scared me."
            miki "What are you doing here?"
            bill "We just thought we'd come and check on you."
            bill "Y'know, to make sure you're feeling OK, after the recoupling."
            miki "You guys...that's really nice of you. Thank you."
        elif s3_mc.current_partner == "Camilo":
            iona "Oh! Sorry, you scared me."
            iona "What are you doing here?"
            camilo "We just thought we'd come and check on you."
            camilo "Y'know, to make sure you're feeling OK, after the recoupling."
            iona "You guys...that's really nice of you. Thank you."
        elif s3_mc.current_partner == "Harry":
            genevieve "Oh! Sorry, you scared me."
            genevieve "What are you doing here?"
            harry "We just thought we'd come and check on you."
            harry "Y'know, to make sure you're feeling OK, after the recoupling."
            genevieve "You guys...that's really nice of you. Thank you."
        elif s3_mc.current_partner == "AJ":
            seb "Oh! Sorry, you scared me."
            seb "What are you doing here?"
            aj "We just thought we'd come and check on you."
            aj "Y'know, to make sure you're feeling OK, after the recoupling."
            seb "You guys...that's really nice of you. Thank you."
    

    if s3_mc.current_partner == "Bill":
        "[he_she!c] looks out across the pool and sighs."
        miki "I really didn't want to cause a scene."
        miki "This is your big moment. I didn't want to ruin it for you."
        miki "'Cause I do like you, [s3_name]. I want us to be friends."
        miki "So I don't want you to think I'm in a mood with you or anything. I'm not."
        miki "It's just..."
        miki "It's a bit scary to find yourself single in here. You know that better than anyone."
        miki "Plus, I was kinda holding onto hope for me and [s3_mc.current_partner]."
        miki "It leaves me wondering what I'm supposed to do now."
    elif s3_mc.current_partner == "Camilo":
        "[he_she!c] looks out across the pool and sighs."
        iona "I really didn't want to cause a scene."
        iona "This is your big moment. I didn't want to ruin it for you."
        iona "'Cause I do like you, [s3_name]. I want us to be friends."
        iona "So I don't want you to think I'm in a mood with you or anything. I'm not."
        iona "It's just..."
        iona "It's a bit scary to find yourself single in here. You know that better than anyone."
        iona "Plus, I was kinda holding onto hope for me and [s3_mc.current_partner]."
        iona "It leaves me wondering what I'm supposed to do now."
    elif s3_mc.current_partner == "Harry":
        "[he_she!c] looks out across the pool and sighs."
        genevieve "I really didn't want to cause a scene."
        genevieve "This is your big moment. I didn't want to ruin it for you."
        if s3_mc.bff == "Genevieve":
            genevieve "Especially for you, [s3_name]. I definitely think of you as a friend."
        else:
            genevieve "'Cause I do like you, [s3_name]. I want us to be friends."
        genevieve "So I don't want you to think I'm in a mood with you or anything. I'm not."
        genevieve "It's just..."
        genevieve "It's a bit scary to find yourself single in here. You know that better than anyone."
        genevieve "Plus, I was kinda holding onto hope for me and [s3_mc.current_partner]."
        genevieve "It leaves me wondering what I'm supposed to do now."
    elif s3_mc.current_partner == "AJ":
        "[he_she!c] looks out across the pool and sighs."
        seb "I really didn't want to cause a scene."
        seb "This is your big moment. I didn't want to ruin it for you."
        if s3_mc.bff == "Genevieve":
            seb "Especially for you, [s3_name]. I definitely think of you as a friend."
        else:
            seb "'Cause I do like you, [s3_name]. I want us to be friends."
        seb "So I don't want you to think I'm in a mood with you or anything. I'm not."
        seb "It's just..."
        seb "It's a bit scary to find yourself single in here. You know that better than anyone."
        seb "And I know me and AJ weren't compatible in that way, like, at all. So it's a silly thing to get upset about."
        seb "But it really leaves me wondering what I'm gonna do next."

    # CHOICE
    menu:
        thought "[s3e3p3_lonely_one] doesn't know what to do now [he_she]'s single..."
        "Just stay positive, babes":
            $ s3_mc.like(s3e3p3_lonely_one)
            s3_mc "I've been there too, so you can take it from me. It can actually be really fun and liberating."
            s3_mc "And it's still early days. You've got loads of time to meet someone else."
            s3_mc "Just keep your chin up, OK? We're all here for you."
            "[he_she!c] smiles gratefully."
            if s3_mc.current_partner == "Bill":
                miki "Thanks, [s3_name]. I'll try to keep that in mind."
            elif s3_mc.current_partner == "Camilo":
                iona "Thanks, [s3_name]. I'll try to keep that in mind."
            elif s3_mc.current_partner == "Harry":
                genevieve "Thanks, [s3_name]. I'll try to keep that in mind."
            elif s3_mc.current_partner == "AJ":
                seb "Thanks, [s3_name]. I'll try to keep that in mind."
        "Better get grafting, then!":
            $ s3_mc.like(s3e3p3_lonely_one)
            s3_mc "I've been there too, so you can take it from me. Being single can be great fun, but you've got to graft."
            s3_mc "Just turn that charm up to eleven and keep cracking on until you find the one."
            "[s3e3p3_lonely_one] laughs despite herself."
            if s3_mc.current_partner == "Bill":
                miki "Thanks, [s3_name]. I'll try to keep that in mind."
            elif s3_mc.current_partner == "Camilo":
                iona "Thanks, [s3_name]. I'll try to keep that in mind."
            elif s3_mc.current_partner == "Harry":
                genevieve "Thanks, [s3_name]. I'll try to keep that in mind."
            elif s3_mc.current_partner == "AJ":
                seb "Thanks, [s3_name]. I'll try to keep that in mind."
        "Just stay away from [s3_mc.current_partner]":
            $ s3_mc.dislike(s3e3p3_lonely_one)
            s3_mc "I don't care what you do, as long as you don't go getting any ideas."
            s3_mc "[s3_mc.current_partner] is with me now, so get used to it."
            if s3_mc.current_partner == "Bill":
                miki "That's not what this is about."
                miki "I'm not gonna try and split you up. I know i've got to move on."
            elif s3_mc.current_partner == "Camilo":
                iona "That's not what this is about."
                iona "I'm not gonna try and split you up. I know i've got to move on."
            elif s3_mc.current_partner == "Harry":
                genevieve "That's not what this is about."
                genevieve "I'm not gonna try and split you up. I know i've got to move on."
            elif s3_mc.current_partner == "AJ":
                seb "That's not what this is about."
                seb "I'm not gonna try and split you up."

    if s3_mc.current_partner == "Bill":
        miki "I'm trying to see it as a positive thing. I'm free to start getting to know somebody new!"
        miki "It's just a shame there's nobody else I really have my eye on yet."
    elif s3_mc.current_partner == "Camilo":
        iona "I'm trying to see it as a positive thing. I'm free to start getting to know somebody new!"
        iona "It's just a shame there's nobody else I really have my eye on yet."
    elif s3_mc.current_partner == "Harry":
        genevieve "I'm trying to see it as a positive thing. I'm free to start getting to know somebody new!"
        genevieve "It's just a shame there's nobody else I really have my eye on yet."
    elif s3_mc.current_partner == "AJ":
        seb "I'm trying to see it as a positive thing. I'm free to start getting to know somebody new!"
        seb "It's just a shame there's nobody else I really have my eye on yet."

    s3_mc "You've got loads of options!"

    if s3_mc.current_partner != "AJ":
        # CHOICE - For the Women
        menu:
            s3_mc "Maybe you should be getting to know..."
            "Bill" if s3_mc.current_partner != 'Bill':
                $ s3e3p3_get_to_know = "Bill"
            "Camilo" if s3_mc.current_partner != 'Camilo':
                $ s3e3p3_get_to_know = "Camilo"
            "Harry" if s3_mc.current_partner != 'Harry':
                $ s3e3p3_get_to_know = "Harry"
            "Nicky":
                $ s3e3p3_get_to_know = "Nicky"
            "Seb":
                s3_mc "He's still in a friendship couple with AJ, so there's no reason not to be chatting to him."
                "She thinks about it seriously for a moment."
                if s3_mc.current_partner == "Bill":
                    miki "That's... actually a really good idea."
                    miki "Thanks, hun."
                elif s3_mc.current_partner == "Camilo":
                    iona "That's... actually a really good idea."
                    iona "Thanks, hun."
                elif s3_mc.current_partner == "Harry":
                    genevieve "That's... actually a really good idea."
                    genevieve "Thanks, hun."
        if s3e3p3_get_to_know != "Seb" or s3e3p3_get_to_know != "Nicky":
            $ s3e3p3_get_to_know_current_partner = s3_3rd_girl_options[s3e3p3_get_to_know]

        if s3e3p3_get_to_know == "Bill" or s3e3p3_get_to_know == "Camilo" or s3e3p3_get_to_know == "Harry" or s3e3p3_get_to_know ==  "Nicky":
            if s3e3p3_get_to_know == "Nicky":
                s3_mc "I know people see him and Elladine as a solid couple, but I think his could still be turned."
            else:
                s3_mc "I know he's with [s3e3p3_get_to_know_current_partner], but I don't think they're serious yet. His head could def still be turned."

            if s3_mc.current_partner == "Bill":
                miki "I don't know. He's not the kind of guy I'd usually go for."
                miki "But he is cool. Maybe I'll try talking to him tomorrow."
                miki "Thanks, hun."
            elif s3_mc.current_partner == "Camilo":
                iona "I don't know. He's not the kind of guy I'd usually go for."
                iona "But he is cool. Maybe I'll try talking to him tomorrow."
                iona "Thanks, hun."
            elif s3_mc.current_partner == "Harry":
                genevieve "I don't know. He's not the kind of guy I'd usually go for."
                genevieve "But he is cool. Maybe I'll try talking to him tomorrow."
                genevieve "Thanks, hun."
    else:
        # CHOICE - For Seb
        menu:
            s3_mc "Maybe you should be getting to know..."
            "Elladine":
                # FILL (I'm going to put something but it isn't canon lol)
                $ s3e3p3_get_to_know = "Elladine"
                s3_mc "I know people see her and Nicky as a solid couple, but I think her could still be turned."
                seb "I don't know. She's not the kind of girl I'd usually go for."
                seb "But she is cool. Maybe I'll try talking to her tomorrow."
                seb "Thanks mate."
            "Miki":
                $ s3e3p3_get_to_know = "Miki"
                s3_mc "I know she likes Bill, but I don't think they're serious yet. Her head could def still be turned."
                seb "Hm,maybe. Miki's one of these well romantic girls. I think I might be a bit too cynical for her."
                seb "But she is cool. Maybe I'll try talking to her a bit tomorrow."
                seb "Thanks mate."
            "Iona":
                $ s3e3p3_get_to_know = "Iona"
                s3_mc "I know she likes Camilo, but I don't think they're serious yet. Her head could def still be turned."
                seb "Iona's great, but she's so high-energy. I think I might just end up dragging her down."
                seb "But she is cool. Maybe I'll try talking to her a bit tomorrow."
                seb "Thanks mate."
            "Genevieve":
                $ s3e3p3_get_to_know = "Genevieve"
                s3_mc "I know she likes Harry, but I don't think they're serious yet. Her head could def still be turned."
                "He thinks about it seriously for a moment."
                seb "That's... actually a really good idea."
                seb "Thanks mate."

    if s3e3p3_go_alone:
        "You look over your shoulder to see [s3_mc.current_partner] coming closer across the lawn. [s3e3p3_lonely_one] smiles."

    if s3_mc.current_partner == "Bill":
        miki "I guess I should be getting to bed. Give you two a little privacy."
    elif s3_mc.current_partner == "Camilo":
        iona "I guess I should be getting to bed. Give you two a little privacy."
    elif s3_mc.current_partner == "Harry":
        genevieve "I guess I should be getting to bed. Give you two a little privacy."
    elif s3_mc.current_partner == "AJ":
        seb "I guess I should be getting to bed. Give you two a little privacy."

    "[he_she!c] winks as gets to [his_her] feet."

    if s3_mc.current_partner == "Bill":
        show miki at npc_exit
        pause .3
        $ renpy.hide("miki")
        $ on_screen.remove("miki")

        show bill at move_center
    elif s3_mc.current_partner == "Camilo":
        show iona at npc_exit
        pause .3
        $ renpy.hide("iona")
        $ on_screen.remove("iona")

        show camilo at move_center
    elif s3_mc.current_partner == "Harry":
        show genevieve at npc_exit
        pause .3
        $ renpy.hide("genevieve")
        $ on_screen.remove("genevieve")

        show harry at move_center
    elif s3_mc.current_partner == "AJ":
        show seb at npc_exit
        pause .3
        $ renpy.hide("seb")
        $ on_screen.remove("seb")

        show seb at move_center

    "[s3e3p3_lonely_one] walks away towards the Villa, leaving you alone by the pool."

    if s3e3p3_go_alone:
        "A moment later, [s3_mc.current_partner] arrives and sits down next to you."

        if s3_mc.current_partner == "Bill":
            bill "How did it go?"
            s3_mc "OK, I think. [he_she] didn't seem annoyed with me or anything."
            bill "That's good."
        elif s3_mc.current_partner == "Camilo":
            camilo "How did it go?"
            s3_mc "OK, I think. [he_she] didn't seem annoyed with me or anything."
            camilo "That's good."
        elif s3_mc.current_partner == "Harry":
            harry "How did it go?"
            s3_mc "OK, I think. [he_she] didn't seem annoyed with me or anything."
            harry "That's good."
        elif s3_mc.current_partner == "AJ":
            aj "How did it go?"
            s3_mc "OK, I think. [he_she] didn't seem annoyed with me or anything."
            aj "That's good."
            
            
    if s3_mc.current_partner == "Bill":
        bill "Thanks for talking to [him_her]. It really means a lot to me."
        bill "Anyway, let's not worry about it any more for now."
        bill "This should be our night!"
    elif s3_mc.current_partner == "Camilo":
        camilo "Thanks for talking to [him_her]. It really means a lot to me."
        camilo "Anyway, let's not worry about it any more for now."
        camilo "This should be our night!"
    elif s3_mc.current_partner == "Harry":
        harry "Thanks for talking to [him_her]. It really means a lot to me."
        harry "Anyway, let's not worry about it any more for now."
        harry "This should be our night!"
    elif s3_mc.current_partner == "AJ":
        aj "Thanks for talking to [him_her]. It really means a lot to me."
        aj "Anyway, let's not worry about it any more for now."
        aj "This should be our night!"
    
    "A warm breeze sends ripples across the surface of the pool."

    if s3_mc.current_partner == "Bill":
        "Bill smiles at you, his blue eyes twinkling."

        # CHOICE
        menu:
            bill "Alright there, beautiful?"
            "Kiss him":
                "You run your fingers down his muscular chest before kissing him deeply on the lips."
                "For a few seconds, there's nothing but his lips on yours and the warm press of your bodies against one another."
                "When you pull away, Bill speaks first."
                bill "Now that was a good kiss."
                bill "Not too forceful, but just a little bit firm. Good rhythm, too."
                bill "Like a goldilocks kiss."
                s3_mc "Do you just have an opinion on, like, everything?"
                bill "Yes and no."
                s3_mc "What does that mean?"
                bill "I'm always one-hundred-percent genuine with myself and the things I believe in."
                bill "I don't mind speaking what I think, but also don't give a monkeys' ass if people don't agree."
                bill "They can be wrong if they want to."
                s3_mc "But I've seen you arguing with people. The other night you and Camilo were debating smoked versus unsmoked bacon until two in the morning."
                bill "How could he even think unsmoked is better?"
                "He shakes his head."
                bill "But I don't care about making him come around. It's the back and forth I like."
                bill "Helps people see where you're coming from, and let's you see the same, you know?"
                bill "I think it makes everyone understand each other better."
                # SUB-CHOICE
                menu:
                    thought "Bill thinks arguing helps the group..."
                    "I see your point":
                        s3_mc "I can see that. Maybe I'll even help you stir up some debates in future!"
                        bill "I'd love that!"
                    "I think there's a time and a place":
                        s3_mc "Sometimes that might be true."
                        s3_mc "But sometimes, causing a debate is just gonna annoy people."
                        bill "Well, that's their choice, isn't it?"
                        s3_mc "You're the worst."
                        bill "That's up for debate..."
                    "Not everyone thinks like you do":
                        s3_mc "Fair enough, but you don't get a lot of people doing that."
                        s3_mc "People just want to be able to have their own opinions without someone jumping down their throat."
                        bill "I don't shove it down their throat. I state my opinion. If they want to debate, they can."
                        s3_mc "I'm not sure everyone sees it like that..."
                        bill "Well, that's their choice, isn't it?"
                        s3_mc "You're doing it right now, aren't you?"
                        bill "Am I?"
                        s3_mc "Yeah! You're even debating if we're debating."
                        bill "I guess I can't help it!"
            "Flirt with him":
                s3_mc "How come you're extra good-looking today?"
                bill "Well, that's cos I put extra effort in today, just for you."
                bill "And you? The only word I can think of right now is..."
                bill "Um..."
                bill "Fit."
                bill "I thought I had a better one. Wait..."
                bill "You look banging."
                bill "That's better, right?"
                s3_mc "Hah, thanks."
                # SUB-CHOICE
                menu:
                    s3_mc "If I had to describe you in one word, it would be..."
                    "Charming":
                        s3_mc "You've got a great attitude. Respectful, confident, but not too cocky."
                        s3_mc "And really level-headed."
                        bill "Cheers."
                        "He pauses and smiles in thought."
                        bill "That actually means a lot to me."
                    "Hot":
                        s3_mc "I mean oof."
                        s3_mc "Have you looked in a mirror lately?"
                        bill "Thanks, babe. I know I'm not bad looking, but it's nice to hear it, you know?"
                    "Bill":
                        "He frowns."
                        bill "Like, my name?"
                        s3_mc "Yeah."
                        "He pauses, stroking his chin, milling it over."
                        bill "All right, I'll take it."
                        bill "It gets right to the point."
                        s3_mc "Just like you."
                        "He laughs."

                bill "My last girlfriend didn't compliment me. She felt like she had to, I dunno, 'keep me on my toes' or something."
                s3_mc "That sucks."
                bill "Yeah. I get it, though, she'd been cheated on by lads in the past. It made her well insecure."
                bill "She didn't let on how much she liked me in case I took her for granted."
                bill "But, in my opinion, relationships should be open and honest."
            "Tell him a joke":
                s3_mc "I've got a joke for you."
                bill "Go for it."

                # SUB-CHOICE
                menu:
                    "What joke should I tell Bill?"
                    "What do you call a talking turtle?":
                        bill "A money-making opportunity?"
                        s3_mc "Whatever his name is."
                    "Why did the dinosaur say 'hello' to the girl?":
                        bill "Because he wanted a snack?"
                        s3_mc "Because he was being polite."
                    "What ended after 2002?":
                        bill "My belief in Father Christmas..."
                        s3_mc "Nope!"
                        s3_mc "Well, maybe, but also..."
                        s3_mc "2003!"

                "Bill snorts, but then looks at you."
                bill "Wait, what's the joke?"
                s3_mc "That was it. That was the joke."
                bill "No, that wasn't a joke."
                s3_mc "It made you laugh, didn't it?"
                bill "Yeah, but it's not a joke, right? A joke has to be, like, wordplay or something."
                s3_mc "I guess you could call them anti-jokes."
                bill "Exactly. They're not jokes."

                # SUB-CHOICE
                menu:
                    thought "Bill doesn't think my jokes were real jokes..."
                    "Agree":
                        s3_mc "You have a point there."
                        bill "Right?"
                    "Disagree":
                        s3_mc "You're not going to convince me."
                        bill "Then I'll stop trying. I'll just know how wrong you are."
                        s3_mc "I can live with that!"
                    "Tell him another":
                        s3_mc "OK, what about this..."
                        s3_mc "What did one lawyer say to the other lawyer?"
                        bill "I don't know..."
                        s3_mc "'We're both lawyers!'"
                        bill "Argh! That wasn't a joke either! That's gotta be on purpose."
                        s3_mc " You got me."

    elif s3_mc.current_partner == "Camilo":
        "The air is warm and heavy, Camilo strokes your arm softly and murmurs into your ear."
        camilo "Eres muy guapa."
        s3_mc "What?"
        camilo "It's Spanish. Means 'you're really pretty'."

        # CHOICE
        menu:
            thought "Maybe I should try some Spanish of my own. How do you say 'it's so hot' again?"
            "I'll just stick to English":
                thought "Better not risk saying something silly in Spanish."
                s3_mc "Is it just me, or is it hot in here?"
                camilo "Not as hot as you, mamacita."
                s3_mc "I thought about trying some Spanish on you, but decided against it."
                camilo "Appreciate it. I'm not a big fan of pulling the GCSE Spanish on me."
                camilo "Like it's OK if they get it right. But they never get it right."
                "He reaches out and touches your cheek."
                camilo "I really feel like you get me."
            "Tengo calor":
                "You grin at him and pretend to fan yourself."
                s3_mc "Tengo calor."
                "He whistles."
                camilo "Beauty and brains. What can't you do?"
                camilo "It was pretty sexy."
                camilo "Say it again."
                s3_mc "Tengo calor?"
                "He pretends to shiver."
                camilo "Ooh!"
                s3_mc "Tengo calor, tengo calor, tengo calor!"
                "He reaches out and touches your cheek."
                camilo "I have so much fun with you."
            "Estoy muy caliente":
                "You grin at him and pretend to fan yourself."
                s3_mc "Estoy muy caliente."
                "He laughs."
                camilo "Well, at least you're honest. I like that in a girl."
                camilo "In Colombia, that means 'I'm horny'."

                # SUB-CHOICE
                menu:
                    thought "I just told Camilo I'm horny..."
                    "Oh no, that's so embarrassing":
                        s3_mc "Nooo!"
                        camilo "Like I said, I like a girl who's up front."
                        s3_mc "I don't think I'll try my Spanish skills again any time soon..."
                        camilo "Aw, I didn't mean to tease you.I love that you tried. Promise me you'll try again?"
                        s3_mc "I'll think about it. Maybe after buying a Colombian phrasebook."
                    "But that's how he said it!":
                        camilo "Who?"
                        s3_mc "That hot tour guide."
                        camilo "Oh, did he now?"
                        s3_mc "Eww! I can't believe he told me it meant it was hot!"
                        camilo "Hey, don't worry. I love that you tried. Promise me you'll try again?"
                        s3_mc "I'll think about it."
                    "I meant what I said":
                        s3_mc "Why are you assuming that's not what I meant?"
                        camilo "What, really?"
                        "You wink at him."
                        s3_mc "If you play your cards right, maybe you'll find out."

        "He comes closer. He moves like a dancer, smooth and practised. His fingers run gently down the line of your jaw."

        # CHOICE
        menu:
            thought "Oof, he's so sexy..."
            "Kiss him":
                "You lean in and press your lips to his. Camilo puts his hands up to cup your chin and you lose yourself in warm sweetness."
                "You don't stop kissing for several minutes. When you pull away at last, you see he's wearing the biggest grin."
                s3_mc "What's so funny?"
                camilo "Nothing. Just thinking about how well we got on."
                camilo "You're gorgeous, and I like kissing you, but I like chatting to you as well."
            "Wait for him to kiss you":
                "You hold Camilo's gaze and let a faint smile touch your lips. He leans in and tilts you chin up with one hand, then presses his lips to yours."
                "You don't stop kissing for several minutes. When you pull away at last, you see he's wearing the biggest grin."
                s3_mc "What's so funny?"
                camilo "Nothing. Just thinking about how well we got on."
                camilo "You're gorgeous, and I like kissing you, but I like chatting to you as well."
            "Tease him a little instead":
                "You lean in as if to kiss him, but stop short of touching his lips. You can feel his breath on your skin."
                "You lightly touch him behind his ear, running your fingernails down his neck."
                camilo "You're incredible."
                s3_mc "You don't mind that I didn't kiss you?"
                camilo "Of course not."
                camilo "I'd wait forever for a kiss from you, chica."
                s3_mc "Right answer."

    elif s3_mc.current_partner == "Harry":
        "Harry's dark eyes look out at you from under long eyelashes. A small smile plays across his lips."

        # CHOICE
        menu:
            thought "He's unbearably cute..."
            "Smother him in kisses":
                "You plant tiny little kisses all over his cheeks, down the muscle of his neck to his shoulders."
                "He puts his arms around you as you keep kissing him, finally putting your lips to his."
                "You pull apart and look at each other for a moment. Harry looks a little dazed."
                harry "Wow."
                s3_mc "More."
                "He kisses you again."
                harry "Wish granted."
            "Give him one deep kiss":
                "You slowly kiss him on the lips, pressing against him."
                "You can feel the heat between you."
                "He wraps his arms around you, and you thread your fingers through the hair at the back of his neck."
                "You pull back and look at each other for a moment."
                harry "Wow."
                s3_mc "More."
                "He kisses you again."
                harry "Wish granted."
            "Talk to him":
                s3_mc "Do you mind if we chat for a bit?"
                "He smiles"
                harry "Of course not."
                harry "Your wish is my command."

        s3_mc "So you're a genie now?"
        harry "Yup."
        s3_mc "Roleplay already?"
        s3_mc "What other wishes can you grant?"
        harry "What kind of wish would you like?"

        # CHOICE
        menu:
            thought "What do I want?"
            "To find romance":
                "He smiles a brilliant smile at you."
                harry "Great choice."
                harry "Usually genies can't grant wishes like that, but in your case I think I can make an exception."
                s3_mc "That's good, because I fancy the genie. Is that allowed?"
                harry "Let me check the Genie Code."
                "He pretends to flip through a book."
                harry "Nope, looks like we're good to go."
                "He puts his arms around your waist and kisses you softly and sweetly."
            "To find happiness":
                harry "Right for the big guns, eh?"
                harry "That's a tricky one."
                harry "Because, like, happiness is different for different people, right?"
                harry "Some people's idea of happiness might be owning a mega-yacht by 45."
                harry "Or founding a startup and selling it for billions."
                s3_mc "To select two examples totally at random."
                "He grins and winks at you."
                harry "It might sound pretty shallow, but it's not the yacht or the money that would make me happy."
                harry "It's knowing I'm successful."
                harry "What about you? What does happiness look like to you?"

                # SUB-CHOICE
                menu:
                    thought "What's my idea of happiness?"
                    "An active, stimulating life ":
                        harry "That's pretty important, too."
                    "A family who loves me":
                        harry "That's pretty important, too."
                    "Being able to help people":
                        harry "That's pretty important, too"
                    "To find success":
                        "Harry beams."
                        harry "That's exactly what I was thinking."
                        harry "I always said I want to own a mega-yacht by the age of 45."
                        harry "But it's not like the yacht would be the thing making me happy."
                        harry "It's being able to look around and know that I succeeded at what I do."

                        # SUB-SUB-CHOICE
                        menu:
                            s3_mc "To me, success means..."
                            "Providing for my family":
                                harry "Yeah, I get that."
                                harry "I think you're already amazing, though."
                            "Being in celebrity magazines":
                                harry "Yeah, I get that."
                                harry "I think you're already amazing, though."
                            "Honing my skills as a [s3_mc.job.lower()]":
                                harry "Yeah, I get that."
                                harry "I think you're already amazing, though."

    elif s3_mc.current_partner == "AJ":
        "AJ tucks a strand of hair behind her ear."
        aj "So, [s3_name]..."
        aj "I was wondering, like, out of just general nosiness and stuff..."
        aj "How did you realise you liked girls?"

        # CHOICE
        menu:
            thought "How did I realise I liked girls?"
            "I had a teacher crush":
                # NEED TO FILL
                "EMPTY"
            "I've literally always known":
                s3_mc "Even when I was a kid I knew I liked women."
                aj "Yeah, I feel that."
                aj "Looking back, there were definitely signs and stuff."
                aj "But my biggest sign was the fact that I was totally in love with my first hockey coach."
            "I was totes in love with my friend":
                aj "That must have been so stressful."
                s3_mc "Yeah, it was."
                s3_mc "Like, I always had to pretend it was just friendly love."
                s3_mc "When really she was eating at my heart from the inside out."
                aj "Oh, you poor thing."
                s3_mc "Yeah, unrequited love is the hardest thing."
                "She holds your hand and squeezes it reassuringly."
                aj "At least, you're here now, hanging out with me."
                aj "And there is nothing one sided about us."
                "She gestures to you and her."
                aj "I had that whole unrequited love with my first hockey coach so I sorta can relate."
                aj "She was the one who made me realise."
            "You made me realise, AJ":
                $ s3_mc.like("AJ")
                aj "Oh, woah."
                aj "I did?"
                "You hold AJ's hands."
                s3_mc "Yeah, you did."
                "She squeezes your hand reassuringly."
                aj "That's, like, the loveliest thing ever."
                aj "Wow."
                aj "I feel, like, all warm inside."
                aj "That means so much."
                aj "I don't think anyone's ever said that to me before!"
                "She grins and hugs you."
                s3_mc "What about you?"
                aj "I knew before coming here."
                aj "It was my first hockey coach who made me realise."

        aj "She was, like, proper patient with teaching me."
        aj "I'm sporty, but I used to struggle with the hockey theory and stuff."
        aj "She always took her time to explain things to me when I didn't get it."
        "AJ smiles at you."
        aj "It's always so good to chat with you about stuff."
        aj "Feels chill, and like, we can just be ourselves around each other."
        "Her hair falls in front of her face again."
        "She edges her body closer to you and stretches."
        aj "Speaking of relaxing..."
        aj "My back is tense from being at the gym earlier."

        # CHOICE
        menu:
            thought "I should..."
            "Suggest she takes up yoga":
                # NEED TO FILL
                "EMPTY"
            "Make out with AJ":
                s3_mc "I know what could help relieve the tension."
                "You lean forward and kiss her lips."
                "She kisses you back, urgent at first, but slowly relaxes into your touch."
                aj "Hmm..."
                "AJ lets out a little moan as you kiss her."
                aj "That's one way to relieve the tension."
                s3_mc "Yeah, feeling better?"
                aj "Much better."
                "AJ grins at you."
            "Give AJ a massage":
                $ s3_mc.like("AJ")
                s3_mc "Do you want a massage, hun?"
                aj "Oh, [s3_name]! You read my mind."
                "AJ turns around and points in between her shoulder blades."
                aj "It's right there where it's proper tense."
                "You massage her back gently. She moans with pleasure."
                aj "I don't know what you're doing..."
                aj "But that feels amazing."
                "Her body relaxes into you as you vary the pressure."
                s3_mc "Better?"
                aj "Much better."

        "AJ leans her head onto your shoulder."
        "You enjoy a moment of closeness and comfortable silence together."

    "You sit in comfortable silence for a moment, until [s3_mc.current_partner] speaks again."

    $ pronouns(s3_mc.current_partner)

    if s3_mc.current_partner == "Bill":
        bill "[s3_name]..."
        bill "It's cool if you're not in the mood, but..."
        "[he_she!c] bites [his_her] lip."
        bill "I really want to do something naughty with you."
        bill "How about we go up to the roof terrace and see what happens?"
        bill "We'll have more privacy up there than the bedroom..."
    elif s3_mc.current_partner == "Camilo":
        camilo "[s3_name]..."
        camilo "It's cool if you're not in the mood, but..."
        "[he_she!c] bites [his_her] lip."
        camilo "I really want to do something naughty with you."
        camilo "How about we go up to the roof terrace and see what happens?"
        camilo "We'll have more privacy up there than the bedroom..."
    elif s3_mc.current_partner == "Harry":
        harry "[s3_name]..."
        harry "It's cool if you're not in the mood, but..."
        "[he_she!c] bites [his_her] lip."
        harry "I really want to do something naughty with you."
        harry "How about we go up to the roof terrace and see what happens?"
        harry "We'll have more privacy up there than the bedroom..."
    elif s3_mc.current_partner == "AJ":
        aj "[s3_name]..."
        aj "It's cool if you're not in the mood, but..."
        "[he_she!c] bites [his_her] lip."
        aj "I really want to do something naughty with you."
        aj "How about we go up to the roof terrace and see what happens?"
        aj "We'll have more privacy up there than the bedroom..."


    thought "This is my chance to spend some private time with [s3_mc.current_partner]!"
    thought "If I say yes, we could even take our relationship to the next level..."

    # CHOICE
    menu:
        thought "Should we...?"
        "Sneak off for some private time on the roof terrace":
            $ s3_mc.like(s3_mc.current_partner)
            s3_mc "I thought you'd never ask."
            "[s3_mc.current_partner] grins and takes your hand."
            if s3_mc.current_partner == "Bill":
                bill "Let's go, babe."
            elif s3_mc.current_partner == "Camilo":
                camilo "Let's go, babe."
            elif s3_mc.current_partner == "Harry":
                harry "Let's go, babe."
            elif s3_mc.current_partner == "AJ":
                aj "Let's go, babe."
            "Together you head back towards the Villa."
            jump s3e3p3_roof_sex
        "Not tonight.":
            s3_mc "I'm a bit tired."
            aj "Oh yeah, I don't blame you. It's been a long day."
            aj "Let's go get some rest."
            "[he_she] stands up and puts out a hand to help you to your feet."
            "Together you head back towards the Villa."
            jump s3e3p3_ending

    return

    
label s3e3p3_roof_sex:
    scene s3-roof-night with dissolve
    $ new_scene()
    $ s3_mc.like_mc[s3_mc.current_partner] += 3
    $ pronouns(s3_mc.current_partner)
    $ s3e3p3_roof_sex = True

    "You step out onto the roof terrace with [s3_mc.current_partner]."

    if s3_mc.current_partner == "Bill":
        bill "This is blatantly the best place in the Villa to be alone. 'Cause in the bedroom, you're bound to be overheard."
        bill "And anywhere else there's always a chance someone'll look out a window and spot you."
        bill "But up here, nobody can see a thing. Basic common sense, innit."
    elif s3_mc.current_partner == "Camilo":
        camilo "This is totally the most romantic place to be alone."
        camilo "There's something about being outside with someone at night that's like... I dunno."
        camilo "It makes me wish I was the kind of guy who knows poetry, so I could say something all poetic about it."
    elif s3_mc.current_partner == "Harry":
        harry "Wow. Look at me, alone on the roof with a glamorous woman. Makes me feel like James Bond."
        harry "Except without any of the intense secret agent stuff."
        harry "Just the bits with the glamorous women."
        s3_mc "Women? Plural?"
        harry "Woman! I mean woman singular. Obviously."
    elif s3_mc.current_partner == "AJ":
        aj "I never would've thought to come up here to be alone, but I heard the others talking about it."
        aj "Like, it makes sense, doesn't it? You can't do anything in the bedroom without being overheard."
        aj "But up here we'll be fine, as long as we're quiet!"
        "She realises she's raising her voice and quickly drops to a whisper, smiling sheepishly."
        aj "Sorry. Got a bit overexcited there. I'll try to keep the noise down."

    "For a while you just stand there, your hands clasped in [his_hers], gazing into each other's eyes."
    "The night is clear and quiet, with only a slight breeze rustling through the trees far below."
    if s3_mc.current_partner == "Bill":
        bill "You're so beautiful."
        bill "That outfit makes you look too good to be real. Like you're in a magazine or a painting or something."
        bill "Except you're right here in front of me."
        bill "I could look at you all night."
    elif s3_mc.current_partner == "Camilo":
        camilo "You're so beautiful."
        camilo "That outfit makes you look too good to be real. Like you're in a magazine or a painting or something."
        camilo "Except you're right here in front of me."
        camilo "I could look at you all night."
    elif s3_mc.current_partner == "Harry":
        harry "You're so beautiful."
        harry "That outfit makes you look too good to be real. Like you're in a magazine or a painting or something."
        harry "Except you're right here in front of me."
        harry "I could look at you all night."
    elif s3_mc.current_partner == "AJ":
        aj "You're so beautiful."
        aj "That outfit makes you look too good to be real. Like you're in a magazine or a painting or something."
        aj "Except you're right here in front of me."
        aj "I could look at you all night."

    # CHOICE
    menu:
        thought "[s3_mc.current_partner] could look at me all night..."
        "Well yeah, you're only human":
            s3_mc "I can't blame you for admiring the view."
        "You look gorgeous, too":
            s3_mc "I can't take my eyes off you."
            s3_mc "We make such a hot couple."
        "Shut up and kiss me":
            "[s3_mc.current_partner] grins and takes your face in both hands."
            "[he_she!c] kisses you gently on the corner of your mouth before pulling away to stare into your eyes again."

    $ s3_mc.like(s3_mc.current_partner)
    "[s3_mc.current_partner] smiles."
    "[he_she!c] leans in close and whispers, [his_her] voice low."

    if s3_mc.current_partner == "Bill":
        bill "[s3_name]..."
        bill "I want you."
        bill "And..."
        "He slips a condom out of his pocket."
        bill "I brought this, just in case you feel the same."
    elif s3_mc.current_partner == "Camilo":
        camilo "[s3_name]..."
        camilo "I wanna make you feel amazing."
        camilo "And..."
        "He slips a condom out of his pocket."
        camilo "I brought this, just in case you feel the same."
    elif s3_mc.current_partner == "Harry":
        harry "[s3_name]..."
        harry "I'm ready."
        s3_mc "You sure?"
        harry "I've never been more sure about anything."
        harry "And..."
        "He slips a condom out of his pocket."
        harry "I brought this, just in case you feel the same."
    elif s3_mc.current_partner == "AJ":
        aj "[s3_name]..."
        aj "Is it OK if I just come out and say it?"
        aj "I really wanna..."
        "She blushes."
        aj "OK, I'm actually too nervous to just come out and say it."

    # CHOICE
    menu:
        thought "This is my chance to do bits with [s3_mc.current_partner]..."
        "No, I'd rather just cuddle":
            $ s3e3p3_just_cuddle = True
            "[s3_mc.current_partner] smiles and strokes your hair."

            if s3_mc.current_partner == "Bill":
                bill "That sounds great, babe."
            elif s3_mc.current_partner == "Camilo":
                camilo "That sounds great, babe."
            elif s3_mc.current_partner == "Harry":
                harry "That sounds great, babe."
            elif s3_mc.current_partner == "AJ":
                aj "That sounds great, babe."
        "Yes, let's get right down to it!":
            s3_mc "I want you, too..."
            "You reach for [s3_mc.current_partner]'s clothes and start pulling them off as fast as you can."
            "[he_she!c] slips you out of your outfit in one smooth motion, leaving it crumpled on the floor."
            "You fall into each other's arms, kissing roughly and passionately, as the rest of the world seems to fall away."
        "Yes, let's savour every moment":
            s3_mc "It's our first time together. Let's make the most of it."
            "You run your hand slowly down the length of [s3_mc.current_partner]'s neck and along [his_her] shoulder, making [him_her] shiver."
            "[he_she!c] caresses your back, stroking you through your clothes, enjoying every shape and curve of your body."
            "Finally you both start to get undressed, revealing yourselves one step at a time."


    if s3e3p3_just_cuddle == False:
        if s3_mc.current_partner == "Bill":
            "Bill's body fits perfectly against yours, from his large hands on your hips, to his strong jaw nuzzling your throat."
            "He seems confident, guiding your moves with ease."
            bill "Is this OK?"
        elif s3_mc.current_partner == "Camilo":
            "Camilo's hips roll against yours with a fluidity that's almost like dancing, every movement perfectly in sync."
            "He seems confident, guiding your moves with ease."
            camilo "Is this OK?"
        elif s3_mc.current_partner == "Harry":
            "Harry's slender fingers trace patterns across your skin, urgent and somehow gentle at the same time."
            "He seems confident, guiding your moves with ease."
            harry "Is this OK?"
        elif s3_mc.current_partner == "AJ":
            "AJ's hair drapes across your chest, soft and shimmering in the moonlight, as her hands slide around your waist."
            "She follows your movements, waiting for you to decide what happens next."

        # CHOICE
        menu:
            thought "How should we do this?"
            "Let's just play it by ear":
                s3_mc "As long as I'm with you, I'm happy."

                if s3_mc.current_partner == "Bill":
                    bill "Me too, babe."
                elif s3_mc.current_partner == "Camilo":
                    camilo "Me too, babe."
                elif s3_mc.current_partner == "Harry":
                    harry "Me too, babe."
                elif s3_mc.current_partner == "AJ":
                    aj "Me too, babe."
            "I want to take the lead":
                "You wrap your legs around [s3_mc.current_partner] and roll on top of him."
                "You touch [him_her] everywhere [he_she] wants to be touched."
                s3_mc "How's that?"

                if s3_mc.current_partner == "Bill":
                    bill "It's amazing..."
                elif s3_mc.current_partner == "Camilo":
                    camilo "It's amazing..."
                elif s3_mc.current_partner == "Harry":
                    harry "It's amazing..."
                elif s3_mc.current_partner == "AJ":
                    aj "It's amazing..."
            "I want [s3_mc.current_partner] to take the lead":
                "[s3_mc.current_partner] wraps [his_her] legs around you and rolls on top of you."
                "[he_she!c] touches you everywhere you want to be touched."

                if s3_mc.current_partner == "Bill":
                    bill "How's that?"
                elif s3_mc.current_partner == "Camilo":
                    camilo "How's that?"
                elif s3_mc.current_partner == "Harry":
                    harry "How's that?"
                elif s3_mc.current_partner == "AJ":
                    aj "How's that?"
                s3_mc "It's amazing..."

        "You lose yourselves in a long, deep kiss."
        "For a while, it's like you're the only two people in the world."
        "Afterwards, you lie on the roof together, sweaty and tired and happy."

        if s3_mc.current_partner == "Bill":
            bill "Wow."
            bill "Now that is what I call good sex."
            s3_mc "You're always so matter of fact."
            bill "Of course I am. That's what you like about me."
        elif s3_mc.current_partner == "Camilo":
            camilo "Wow."
            camilo "It's never felt exactly like that before."
            s3_mc "In a good way, right?"
            camilo "In a wicked good way."
        elif s3_mc.current_partner == "Harry":
            harry "Wow."
            harry "If this really was a James Bond movie, I think that scene would've had to fade to black."
            harry "Which is a shame. I wouldn't want to miss a single second of it."
        elif s3_mc.current_partner == "AJ":
            aj "Wow."
            aj "Sorry if I got a little overexcited again. I tried to keep the noise down, but you didn't make it easy."
            s3_mc "Do you think anyone overheard us?"
            aj "Right now, I don't even care if they did."

    "You cuddle close in the warm night air."

    if s3_mc.current_partner == "Bill":
        bill "I'm so glad you picked me tonight."
        bill "I was hoping you would. You were definitely giving me those vibes."
        bill "But I was trying not to get my hopes up too much, just in case."
        if s3e2p2_special_spark == s3_mc.current_partner:
            bill "I guess I should've known after what you said yesterday. About this spark between us."
        else:
            bill "I loved what you said in your speech tonight. I love knowing you like me the same way I like you."
    elif s3_mc.current_partner == "Camilo":
        camilo "I'm so glad you picked me tonight."
        camilo "I was hoping you would. You were definitely giving me those vibes."
        camilo "But I was trying not to get my hopes up too much, just in case."
        if s3e2p2_special_spark == s3_mc.current_partner:
            camilo "I guess I should've known after what you said yesterday. About this spark between us."
        else:
            camilo "I loved what you said in your speech tonight. I love knowing you like me the same way I like you."
    elif s3_mc.current_partner == "Harry":
        harry "I'm so glad you picked me tonight."
        harry "I was hoping you would. You were definitely giving me those vibes."
        harry "But I was trying not to get my hopes up too much, just in case."
        if s3e2p2_special_spark == s3_mc.current_partner:
            harry "I guess I should've known after what you said yesterday. About this spark between us."
        else:
            harry "I loved what you said in your speech tonight. I love knowing you like me the same way I like you."
    elif s3_mc.current_partner == "AJ":
        aj "I'm so glad you picked me tonight."
        aj "I was hoping you would. You were definitely giving me those vibes."
        aj "But I was trying not to get my hopes up too much, just in case."
        if s3e2p2_special_spark == s3_mc.current_partner:
            aj "I guess I should've known after what you said yesterday. About this spark between us."
        else:
            aj "I loved what you said in your speech tonight. I love knowing you like me the same way I like you."

    # CHOICE
    menu:
        s3_mc "Choosing to couple up with [s3_mc.current_partner]..."
        "It was a tough decision":
            s3_mc "I really had to think about it. I didn't want to just rush into this without being sure."
            s3_mc "But in the end, it had to be you."
        "It was an easy decision":
            $ s3_mc.like(s3_mc.current_partner)
            s3_mc "I knew you were the one I wanted. No contest."
        "I flipped a coin ":
            s3_mc "Well, a few coins. I had to narrow down my options."
            "[s3_mc.current_partner] laughs."

            if s3_mc.current_partner == "Bill":
                bill "Is that really how you make decisions?"
            elif s3_mc.current_partner == "Camilo":
                camilo "Is that really how you make decisions?"
            elif s3_mc.current_partner == "Harry":
                harry "Is that really how you make decisions?"
            elif s3_mc.current_partner == "AJ":
                aj "Is that really how you make decisions?"
                
            s3_mc "It's always worked for me so far."

    "[he_she!c] squeezes you closer to [his_her] chest."
    "You can feel [his_her] heart beating. It's incredibly soothing."
    "[s3_mc.current_partner]'s hand gently strokes your back as you feel your eyes start to get heavy..."

    if s3_mc.current_partner == "Bill":
        bill "Hey sleepyhead."
        s3_mc "Huh? Did I fall asleep?"
        bill "I think you just dozed off for a second."
        bill "Maybe we should go back inside and get some sleep."
        bill "I've had a great time up here with you."
    elif s3_mc.current_partner == "Camilo":
        camilo "Hey sleepyhead."
        s3_mc "Huh? Did I fall asleep?"
        camilo "I think you just dozed off for a second."
        camilo "Maybe we should go back inside and get some sleep."
        camilo "I've had a great time up here with you."
    elif s3_mc.current_partner == "Harry":
        harry "Hey sleepyhead."
        s3_mc "Huh? Did I fall asleep?"
        harry "I think you just dozed off for a second."
        harry "Maybe we should go back inside and get some sleep."
        harry "I've had a great time up here with you."
    elif s3_mc.current_partner == "AJ":
        aj "Hey sleepyhead."
        s3_mc "Huh? Did I fall asleep?"
        aj "I think you just dozed off for a second."
        aj "Maybe we should go back inside and get some sleep."
        aj "I've had a great time up here with you."

    # CHOICE
    menu:
        thought "Hanging out with [s3_mc.current_partner] on the roof terrace..."
        "We should totally do this again":
            s3_mc "It's been so nice. I want to spend every night up here with you."
            if s3_mc.current_partner == "Bill":
                bill "That would be fun."
                bill "But I think the others would definitely start asking questions..."
            elif s3_mc.current_partner == "Camilo":
                camilo "That would be fun."
                camilo "But I think the others would definitely start asking questions..."
            elif s3_mc.current_partner == "Harry":
                harry "That would be fun."
                harry "But I think the others would definitely start asking questions..."
            elif s3_mc.current_partner == "AJ":
                aj "That would be fun."
                aj "But I think the others would definitely start asking questions..."
            s3_mc "Let them ask."
        "I'd rather be in a nice soft bed":
            s3_mc "This is cool and all, but beds are beds for a reason. 'Cause they're comfy."
            if s3_mc.current_partner == "Bill":
                bill "Then let's go."
            elif s3_mc.current_partner == "Camilo":
                camilo "Then let's go."
            elif s3_mc.current_partner == "Harry":
                harry "Then let's go."
            elif s3_mc.current_partner == "AJ":
                aj "Then let's go."
        "As long as we're together, I don't care":
            s3_mc "We could do this in any room of the Villa and I'd enjoy it just as much."
            if s3_mc.current_partner == "Bill":
                bill "Even the kitchen?"
            elif s3_mc.current_partner == "Camilo":
                camilo "Even the kitchen?"
            elif s3_mc.current_partner == "Harry":
                harry "Even the kitchen?"
            elif s3_mc.current_partner == "AJ":
                aj "Even the kitchen?"
            s3_mc "What part of 'any room' don't you understand?"

    "[he_she!c] grins and takes your hand."
    "Together, you go back down the steps into the Villa."

    jump s3e3p3_ending
    return

label s3e3p3_ending:
    scene s3-bedroom-night with dissolve
    $ new_scene()

    "When you arrive in the bedroom, the other Islanders are already getting into bed."
    thought "Hmm, I should probably get into some comfier clothes..."

    scene s3-dressing-room with dissolve
    $ new_scene()

    # Add back one MC has images in game
    # "MC outfit change to sleepwear"
    # "Hey, babe." -> always
    # "You look so great in those." -> if one of current partner fav outfits, else nothing

    "You get changed into your pjs."
    
    $ outfit = "pjs"
    call customize_outfit from _call_customize_outfit_8
    
    thought "That's better."

    scene s3-bedroom-night with dissolve
    $ new_scene()

    if s3_mc.current_partner == "Bill":
        bill "Hey, babe."
        bill "You look so great in those."
        if s3e3p3_roof_sex:
            bill "Oops, forgot to brush my teeth."
            bill "Back in a second!"
    elif s3_mc.current_partner == "Camilo":
        camilo "Hey, babe."
        camilo "You look so great in those."
        if s3e3p3_roof_sex:
            camilo "Oops, forgot to brush my teeth."
            camilo "Back in a second!"
    elif s3_mc.current_partner == "Harry":
        harry "Hey, babe."
        harry "You look so great in those."
        if s3e3p3_roof_sex:
            harry "Oops, forgot to brush my teeth."
            harry "Back in a second!"
    elif s3_mc.current_partner == "AJ":
        aj "Hey, babe."
        aj "You look so great in those."
        if s3e3p3_roof_sex:
            aj "Oops, forgot to brush my teeth."
            aj "Back in a second!"

    "[s3_mc.current_partner] hurries off towards the bathroom."

    if s3_mc.current_partner == "Bill":
        $ leaving("bill")
    elif s3_mc.current_partner == "Camilo":
        $ leaving("camilo")
    elif s3_mc.current_partner == "Harry":
        $ leaving("harry")
    elif s3_mc.current_partner == "AJ":
        $ leaving("aj")

    $ pronouns(s3_mc.bff)
    "[s3_mc.bff] flashes you a sly smile."
    seb "There you are, [s3_name]. Where have you and [s3_mc.current_partner] been all this time?"
    "[he_she!c] leans in conspiratorially."
    seb "Any exciting developments?"

    # CHOICE
    menu:
        s3_mc "Me and [s3_mc.current_partner]..."
        "We had sex on the roof!" if s3e3p3_roof_sex and s3e3p3_just_cuddle == False:
            if s3_mc.bff == "Elladine":
                elladine "No way!"
                s3_mc "Yes way!"
                elladine "Aah, that's so exciting!"
                elladine "And a really romantic place for your first time as a couple, too."
                elladine "Ugh, you two are such goals already."
                elladine "I'm so happy for you."
            elif s3_mc.bff == "Genevieve":
                genevieve "No way!"
                s3_mc "Yes way!"
                genevieve "Aah, that's so exciting!"
                genevieve "And a really romantic place for your first time as a couple, too."
                genevieve "Ugh, you two are such goals already."
                genevieve "I'm so happy for you."
            elif s3_mc.bff == "Nicky":
                nicky "No way!"
                s3_mc "Yes way!"
                nicky "Aah, that's so exciting!"
                nicky "And a really romantic place for your first time as a couple, too."
                nicky "Is that going to be a problem now that you're coupled up? You and [s3_mc.current_partner] being disgustingly cute all over the place?"
                s3_mc "Shut up."
                nicky "I'm kidding. I'm really happy for you."
            elif s3_mc.bff == "Seb":
                seb "No way!"
                s3_mc "Yes way!"
                seb "Aah, that's so exciting!"
                seb "And a really romantic place for your first time as a couple, too."
                seb "Is that going to be a problem now that you're coupled up? You and [s3_mc.current_partner] being disgustingly cute all over the place?"
                s3_mc "Shut up."
                seb "I'm kidding. I'm really happy for you."
        "We went to the roof to snuggle" if s3e3p3_roof_sex and s3e3p3_just_cuddle == True:
            if s3_mc.bff == "Elladine":
                elladine "Aw, that's a romantic way to spend your first night as a couple!"
                elladine "Ugh, you two are such goals already."
                elladine "I'm so happy for you."
            elif s3_mc.bff == "Genevieve":
                genevieve "Aw, that's a romantic way to spend your first night as a couple!"
                genevieve "Ugh, you two are such goals already."
                genevieve "I'm so happy for you."
            elif s3_mc.bff == "Nicky":
                nicky "Aw, that's a romantic way to spend your first night as a couple!"
                nicky "Is that going to be a problem now that you're coupled up? You and [s3_mc.current_partner] being disgustingly cute all over the place?"
                s3_mc "Shut up."
                nicky "I'm kidding. I'm really happy for you."
            elif s3_mc.bff == "Seb":
                seb "Aw, that's a romantic way to spend your first night as a couple!"
                seb "Is that going to be a problem now that you're coupled up? You and [s3_mc.current_partner] being disgustingly cute all over the place?"
                s3_mc "Shut up."
                seb "I'm kidding. I'm really happy for you."
        "Wouldn't you like to know...":
            if s3_mc.bff == "Elladine":
                elladine "Uh, yeah! I wanna know all your gossip!"
                s3_mc "Sorry, but you'll just have to keep guessing."
                elladine "You're so mysterious!"
                elladine "So you don't mind if I just assume the truth is something really saucy and scandalous, right?"
                s3_mc "Be my guest. You're not getting a word out of me."
            elif s3_mc.bff == "Genevieve":
                genevieve "Uh, yeah! I wanna know all your gossip!"
                s3_mc "Sorry, but you'll just have to keep guessing."
                genevieve "You're so mysterious!"
                genevieve "So you don't mind if I just assume the truth is something really saucy and scandalous, right?"
                s3_mc "Be my guest. You're not getting a word out of me."
            elif s3_mc.bff == "Nicky":
                nicky "Uh, yeah! I wanna know all your gossip!"
                s3_mc "Sorry, but you'll just have to keep guessing."
                nicky "You're so mysterious!"
                nicky "So you don't mind if I just assume the truth is something really saucy and scandalous, right?"
                s3_mc "Be my guest. You're not getting a word out of me."
            elif s3_mc.bff == "Seb":
                seb "Uh, yeah! I wanna know all your gossip!"
                s3_mc "Sorry, but you'll just have to keep guessing."
                seb "You're so mysterious!"
                seb "So you don't mind if I just assume the truth is something really saucy and scandalous, right?"
                s3_mc "Be my guest. You're not getting a word out of me."
        "We were just getting coffee":
            if s3_mc.bff == "Elladine":
                elladine "Coffee?"
                elladine "But... it's night time."
                s3_mc "Nothing wrong with a nice cup of night time coffee."
                s3_mc "Gets you feeling all warm and cosy and ready for bed."
                elladine "Are you sure you mean 'coffee'? You don't mean something else?"
                s3_mc "Coffee. The brown bean juice, sometimes with milk. You know."
                s3_mc "Coffee."
                elladine "I don't know how to break this to you, but I think you're doing coffee wrong."
            elif s3_mc.bff == "Genevieve":
                genevieve "Coffee?"
                genevieve "But... it's night time."
                s3_mc "Nothing wrong with a nice cup of night time coffee."
                s3_mc "Gets you feeling all warm and cosy and ready for bed."
                genevieve "Are you sure you mean 'coffee'? You don't mean something else?"
                s3_mc "Coffee. The brown bean juice, sometimes with milk. You know."
                s3_mc "Coffee."
                genevieve "I don't know how to break this to you, but I think you're doing coffee wrong."
            elif s3_mc.bff == "Nicky":
                nicky "Coffee?"
                nicky "But... it's night time."
                s3_mc "Nothing wrong with a nice cup of night time coffee."
                s3_mc "Gets you feeling all warm and cosy and ready for bed."
                nicky "Are you sure you mean 'coffee'? You don't mean something else?"
                s3_mc "Coffee. The brown bean juice, sometimes with milk. You know."
                s3_mc "Coffee."
                nicky "I don't know how to break this to you, but I think you're doing coffee wrong."
            elif s3_mc.bff == "Seb":
                seb "Coffee?"
                seb "But... it's night time."
                s3_mc "Nothing wrong with a nice cup of night time coffee."
                s3_mc "Gets you feeling all warm and cosy and ready for bed."
                seb "Are you sure you mean 'coffee'? You don't mean something else?"
                s3_mc "Coffee. The brown bean juice, sometimes with milk. You know."
                s3_mc "Coffee."
                seb "I don't know how to break this to you, but I think you're doing coffee wrong."

    $ pronouns(s3_mc.current_partner)
    "[s3_mc.current_partner] comes back from the bathroom, [his_her] breath smelling of mint."

    if s3_mc.current_partner == "Bill":
        bill "What did I miss?"
    elif s3_mc.current_partner == "Camilo":
        camilo "What did I miss?"
    elif s3_mc.current_partner == "Harry":
        harry "What did I miss?"
    elif s3_mc.current_partner == "AJ":
        aj "What did I miss?"

    if s3_mc.bff == "Elladine":
        elladine "Nothing..."
        $ leaving("elladine")
    elif s3_mc.bff == "Genevieve":
        genevieve "Nothing..."
        $ leaving("genevieve")
    elif s3_mc.bff == "Nicky":
        nicky "Nothing..."
        $ leaving("nicky")
    elif s3_mc.bff == "Seb":
        seb "Nothing..."
        $ leaving("seb")

    # if s3_mc.current_partner == "Bill":
    #     show bill at move_center
    # elif s3_mc.current_partner == "Camilo":
    #     show camilo at move_center
    # elif s3_mc.current_partner == "Harry":
    #     show harry at move_center
    # elif s3_mc.current_partner == "AJ":
    #     show aj at move_center

    "[s3_mc.current_partner] cheerfully climbs onto your bed. You settle in next to [him_her]."

    if s3_mc.current_partner == "Bill":
        bill "Hey, don't worry. Sharing a bed with me is really easy."
        s3_mc "What do you mean?"
        bill "I'm a well heavy sleeper. Nothing wakes me up. Once I'm out you could be playing the drums right by my ears, doesn't matter."
        bill "It comes from hammering on roofs all day, see. You get used to the noise."
    elif s3_mc.current_partner == "Camilo":
        camilo "Are you a heavy sleeper or a light sleeper?"
        camilo "For me it kinda depends on how tired I am. Sometimes after a long day on my feet, I go out like a light, and that's me."
        camilo "But other times I have nights where anything can wake me up."
    elif s3_mc.current_partner == "Harry":
        harry "I hope you're not a light sleeper, by the way."
        harry "I usually wake up early, like, really early. To do my affirmations. So I don't wanna disturb you."
    elif s3_mc.current_partner == "AJ":
        aj "Sorry in advance, by the way."
        s3_mc "What for?"
        aj "I tend to move around a lot in my sleep. I'm usually dreaming about playing hockey."
        aj "So don't worry if my legs are kicking and stuff, it's totally normal. But it might wake you up, if you're a light sleeper."

    # CHOICE
    menu:
        thought "Am I a light sleeper?"
        "Yeah, I get woken up pretty easily":
            if s3_mc.current_partner == "Bill":
                bill "Got it. I'll do my best not to wake you up, then."
            elif s3_mc.current_partner == "Camilo":
                camilo "Got it. I'll do my best not to wake you up, then."
            elif s3_mc.current_partner == "Harry":
                harry "Got it. I'll do my best not to wake you up, then."
            elif s3_mc.current_partner == "AJ":
                aj "Got it. I'll do my best not to wake you up, then."
        "Nah, I sleep through most things":
            if s3_mc.current_partner == "Bill":
                bill "Awesome. This should be easy, then."
            elif s3_mc.current_partner == "Camilo":
                camilo "Awesome. This should be easy, then."
            elif s3_mc.current_partner == "Harry":
                harry "Awesome. This should be easy, then."
            elif s3_mc.current_partner == "AJ":
                aj "Awesome. This should be easy, then."
        "I don't mind being woken up by you":
            $ s3_mc.like(s3_mc.current_partner)
            if s3_mc.current_partner == "Bill":
                bill "Aw, babe."
                bill "Still, I'll try not to wake you up till the morning."
                bill "Whatever happens tomorrow, we don't wanna be all tired for it, right?"
            elif s3_mc.current_partner == "Camilo":
                camilo "Aw, babe."
                camilo "Still, I'll try not to wake you up till the morning."
                camilo "Whatever happens tomorrow, we don't wanna be all tired for it, right?"
            elif s3_mc.current_partner == "Harry":
                harry "Aw, babe."
                harry "Still, I'll try not to wake you up till the morning."
                harry "Whatever happens tomorrow, we don't wanna be all tired for it, right?"
            elif s3_mc.current_partner == "AJ":
                aj "Aw, babe."
                aj "Still, I'll try not to wake you up till the morning."
                aj "Whatever happens tomorrow, we don't wanna be all tired for it, right?"
            s3_mc "Totally."

    "You make yourselves comfortable under the covers."
    "A hush falls over the bedroom as the Islanders settle in to sleep. The only sound is [s3_mc.current_partner]'s breathing beside you."
    thought "This is nice."
    "[s3_mc.current_partner] leans on [his_her] hands beside you and whispers."

    if s3_mc.current_partner == "Bill":
        bill "So, do you like your personal space at night..."
        bill "Or are you down for a cuddle?"
    elif s3_mc.current_partner == "Camilo":
        camilo "So, do you like your personal space at night..."
        camilo "Or are you down for a cuddle?"
    elif s3_mc.current_partner == "Harry":
        harry "So, do you like your personal space at night..."
        harry "Or are you down for a cuddle?"
    elif s3_mc.current_partner == "AJ":
        aj "So, do you like your personal space at night..."
        aj "Or are you down for a cuddle?"

    # CHOICE
    menu:
        thought "Should I cuddle up to [s3_mc.current_partner]?"
        "Wrap your arms around [him_her]":
            $ s3_mc.like(s3_mc.current_partner)
            "You gently put your arms around [s3_mc.current_partner]'s body."
            "[he_she!c] snuggles closer against your chest and makes a small, happy, sleepy noise."
            thought "[he_she!c]'s so warm."
            thought "And I feel so safe."
        "Ask [him_her] to spoon you":
            $ s3_mc.like(s3_mc.current_partner)
            s3_mc "Can I be the little spoon?"
            "[he_she!c] murmurs in agreement and wraps [his_her] arms around you."
            "You roll over so your back is pressed into [his_her] chest, [his_her] hands holding you firmly around your waist."
            thought "[he_she!c]'s so warm."
            thought "And I feel so safe."
        "I'd rather just go to sleep":
            if s3_mc.current_partner == "Bill":
                bill "Alright. Sleep well."
            elif s3_mc.current_partner == "Camilo":
                camilo "Alright. Sleep well."
            elif s3_mc.current_partner == "Harry":
                harry "Alright. Sleep well."
            elif s3_mc.current_partner == "AJ":
                aj "Alright. Sleep well."

    "You close your eyes and drift into a deep, comfortable sleep."

    scene sand with dissolve
    $ on_screen = []

    "It's strange to think that this morning, [s3_name] was the only single girl in the Villa..."
    "And now she's coupled up with [s3_mc.current_partner]."
    "They're so cute together, I totally can't even."
    "Sorry, what it actually says here is I need to 'totally clean the oven.'"
    "Alright, I see what's happened here. I'm just reading off my to-do list."

    if s3e3p3_roof_sex:
        "Anyway, that moment with the two of them on the roof terrace?"
        "Most romantic thing I've seen so far this year."
        "And that's including the slow-burn romance between Bill's tastebuds and Camilo's empanadas."

    $ outfit = "swim"

    "Next time..."
    "The Islanders buy washing powder and defrost the freezer!"
    "Nope, sorry, that's my to-do list again."
    "Next time..."
    "Our happy couples will be put to the ultimate test."
    camilo "Are those...?"
    bill "Just follow the instructions, mate. It's simple."
    harry "All my ice cream melted."
    "Will [s3_name] and [s3_mc.current_partner]'s relationship be strong enough to survive?"

    jump s3e4p1
    return

#########################################################################
## Episode 4, Part 1
#########################################################################
label s3e4p1:
    scene sand with dissolve
    $ on_screen = []

    show screen day_title(4, 1) with Pause(4)
    hide screen day_title with dissolve

    $ outfit = "evening"

    "Last time on Love Island..."
    "The ball was finally back in [s3_name]'s court."

    if s3_mc.past_partners[0] == s3_mc.current_partner:
        "No prizes for guessing who she went for..."
        s3_mc "The person I'd like to couple up with is... [s3_mc.current_partner]."
        "Yes, two days after losing him, she's back with [s3_mc.current_partner]..."
        "It's like watching a ping pong match in slow motion."
    else:
        "And instead of going for [s3_mc.past_partners[0]], she decided to surprise everyone and change things up..."
        s3_mc "The person I'd like to couple up with is... [s3_mc.current_partner]."

    "As expected, there was no end of crying, accusations of broken girl code and..."

    if s3_mc.current_partner == "Bill":
        miki "I really didn't want to cause a scene."
        miki "I don't want you to think I'm in a mood with you or anything. I'm not."
        $ leaving("miki")
    elif s3_mc.current_partner == "Camilo":
        iona "I really didn't want to cause a scene."
        iona "I don't want you to think I'm in a mood with you or anything. I'm not."
        $ leaving("iona")
    elif s3_mc.current_partner == "Harry":
        genevieve "I really didn't want to cause a scene."
        genevieve "I don't want you to think I'm in a mood with you or anything. I'm not."
        $ leaving("genevieve")
    elif s3_mc.current_partner == "AJ":
        seb "I really didn't want to cause a scene."
        seb "I don't want you to think I'm in a mood with you or anything. I'm not."
        $ leaving("seb")

    "Wait, what? I must have tuned into the wrong channel. It looked like [s3e3p3_lonely_one] was handling it well."
    "Coming up..."
    "One of the boys isn't in the mood for some friendly ribbing..."

    $ outfit = "swim"
    bill "What are you doing, mate?"
    $ leaving("bill")

    "And there was me thinking it was just going to be a nice relaxing day by the pool."

    $ pronouns(s3_mc.current_partner)

    scene s3-bedroom-day with dissolve
    $ new_scene()

    $ outfit = "pjs"

    "All is quiet in the Villa, except for a few soft snores."
    "You wake up wrapped up in [s3_mc.current_partner]'s strong arms."
    "You take a moment to watch [him_her] sleep."
    thought "After all that time being single, it's actually nice to wake up next to someone."

    # CHOICE
    menu:
        thought "[s3_mc.current_partner] looks..."
        "Cute as a button":
            thought "I could stare at [him_her] for hours."
        "Hot like fiyah":
            thought "It's ridiculous. Who looks that hot first thing in the morning?"
        "Funny...":
            thought "[he_she!c] looks totally out of it. I could totally draw on his face..."

    "[s3_mc.current_partner] stirs, opens [his_her] eyes and catches you gazing at [him_her]."

    if s3_mc.current_partner == "Bill":
        bill "Were you watching me sleep?"
    elif s3_mc.current_partner == "Camilo":
        camilo "Were you watching me sleep?"
    elif s3_mc.current_partner == "Harry":
        harry "Were you watching me sleep?"
    elif s3_mc.current_partner == "AJ":
        aj "Were you watching me sleep?"

    # CHOICE
    menu:
        thought "[s3_mc.current_partner] caught me watching [him_her]..."
        "Can you blame me?":
            $ s3_mc.like(s3_mc.current_partner)
            s3_mc "You're gorgeous. I couldn't help myself."

            if s3_mc.current_partner == "Bill":
                bill "You're not too bad yourself."
            elif s3_mc.current_partner == "Camilo":
                camilo "You're not too bad yourself."
            elif s3_mc.current_partner == "Harry":
                harry "You're not too bad yourself."
            elif s3_mc.current_partner == "AJ":
                aj "You're pretty fit too."
        "You sleep funny":
            $ s3_mc.dislike(s3_mc.current_partner)
            s3_mc "You stick your arms out so wide, you look like a scarecrow."

            if s3_mc.current_partner == "Bill":
                bill "Is that a good thing?"
                s3_mc "It's funny!"
                bill "I'll take your word for it."
                bill "Let's start again."
            elif s3_mc.current_partner == "Camilo":
                camilo "Is that a good thing?"
                s3_mc "It's funny!"
                camilo "I'll take your word for it."
                camilo "Let's start again."
            elif s3_mc.current_partner == "Harry":
                harry "Is that a good thing?"
                s3_mc "It's funny!"
                harry "I'll take your word for it."
                harry "Let's start again."
            elif s3_mc.current_partner == "AJ":
                aj "Is that a good thing?"
                s3_mc "It's funny!"
                aj "I'll take your word for it."
                aj "Let's start again."
        "Who, me?":
            if s3_mc.current_partner == "Bill":
                bill "Yeah you, silly."
                s3_mc "I don't know what you're talking about."
                bill "Aw, you're embarrassed. I thought it was cute."
            elif s3_mc.current_partner == "Camilo":
                camilo "Yeah you, silly."
                s3_mc "I don't know what you're talking about."
                camilo "Aw, you're embarrassed. I thought it was cute."
            elif s3_mc.current_partner == "Harry":
                harry "Yeah you, silly."
                s3_mc "I don't know what you're talking about."
                harry "Aw, you're embarrassed. I thought it was cute."
            elif s3_mc.current_partner == "AJ":
                aj "Yeah you, silly."
                s3_mc "I don't know what you're talking about."
                aj "Aw, you're embarrassed. I thought it was cute."

    "[s3_mc.current_partner] smiles and stretches before wrapping [his_her] arms around you and pulling you closer."

    if s3_mc.current_partner == "Bill":
        bill "Morning."
        "You're so close your noses are almost touching. You can feel the warmth of [s3_mc.current_partner]'s breath."
        bill "This is nice. You and me, all coupled up. I don't think it could get any better."
        s3_mc "I can think of one thing that would make it better..."
        bill "Oh really? And what would that be?"
    elif s3_mc.current_partner == "Camilo":
        camilo "Morning."
        "You're so close your noses are almost touching. You can feel the warmth of [s3_mc.current_partner]'s breath."
        camilo "This is nice. You and me, all coupled up. I don't think it could get any better."
        s3_mc "I can think of one thing that would make it better..."
        camilo "Oh really? And what would that be?"
    elif s3_mc.current_partner == "Harry":
        harry "Morning."
        "You're so close your noses are almost touching. You can feel the warmth of [s3_mc.current_partner]'s breath."
        harry "This is nice. You and me, all coupled up. I don't think it could get any better."
        s3_mc "I can think of one thing that would make it better..."
        harry "Oh really? And what would that be?"
    elif s3_mc.current_partner == "AJ":
        aj "Morning."
        "You're so close your noses are almost touching. You can feel the warmth of [s3_mc.current_partner]'s breath."
        aj "This is nice. You and me, all coupled up. I don't think it could get any better."
        s3_mc "I can think of one thing that would make it better..."
        aj "Oh really? And what would that be?"
    
    # CHOICE
    menu:
        thought "Hmm, what would make this moment even better?"
        "A kiss":
            $ s3_mc.like(s3_mc.current_partner)
            $ s3e4p1_kiss_or_cuddle = True
            "You lean closer."

            if s3_mc.current_partner == "Bill":
                bill "Oh, you mean..."
            elif s3_mc.current_partner == "Camilo":
                camilo "Oh, you mean..."
            elif s3_mc.current_partner == "Harry":
                harry "Oh, you mean..."
            elif s3_mc.current_partner == "AJ":
                aj "Oh, you mean..."

            "[s3_mc.current_partner] smiles seductively and pulls you closer. [his_her!c] lips press firmly against yours."

            if s3_mc.current_partner == "Bill" or s3_mc.current_partner == "Harry":
                "The kiss starts gently but builds in intensity."
                "His kisses move towards your collar bone, sending tingles down your spine."
            elif s3_mc.current_partner == "AJ" or s3_mc.current_partner == "Camilo":
                "You feel [his_her] tongue trace your lips and then [he_she] gently bites your bottom lip."
                if s3_mc.current_partner == "Camilo":
                    camilo "I could eat you."
                else:
                    aj "I could eat you."
                "[he_she!c] nibbles down your neck, making you giggle."

            "You pull away, a little breathless."
            s3_mc "We're going to wake everyone up."

            if s3_mc.current_partner == "Bill":
                bill "Good. They should be up anyway."
            elif s3_mc.current_partner == "Camilo":
                camilo "Good. They should be up anyway."
            elif s3_mc.current_partner == "Harry":
                harry "Good. They should be up anyway."
            elif s3_mc.current_partner == "AJ":
                aj "Good. They should be up anyway."
        "A cuddle":
            $ s3_mc.like(s3_mc.current_partner)
            $ s3e4p1_kiss_or_cuddle = True
            "You roll over, facing away from [him_her]. Then start to wiggle backwards until your body is nuzzled into [him_her]."

            if s3_mc.current_partner == "Bill":
                bill "Woah, what are you doing?"
            elif s3_mc.current_partner == "Camilo":
                camilo "Woah, what are you doing?"
            elif s3_mc.current_partner == "Harry":
                harry "Woah, what are you doing?"
            elif s3_mc.current_partner == "AJ":
                aj "Woah, what are you doing?"

            s3_mc "Being the little spoon."
            "You take [s3_mc.current_partner]'s arms and pull them in tight around your waist."
            s3_mc "Morning cuddles are the best."
            "[he_she!c] rests [his_her] chin on your shoulder."
            "You feel [his_her] body envelop yours. It's warm and reassuring."

            if s3_mc.current_partner == "Bill":
                bill "Hmm, I could get used to this."
            elif s3_mc.current_partner == "Camilo":
                camilo "Hmm, I could get used to this."
            elif s3_mc.current_partner == "Harry":
                harry "Hmm, I could get used to this."
            elif s3_mc.current_partner == "AJ":
                aj "Hmm, I could get used to this."
        "A cuppa":
            "You beckon [s3_mc.current_partner] closer with your finger. [he_she!c] smiles and leans in."
            s3_mc "What I'd really love..."

            if s3_mc.current_partner == "Bill":
                bill "Yeah..."
            elif s3_mc.current_partner == "Camilo":
                camilo "Yeah..."
            elif s3_mc.current_partner == "Harry":
                harry "Yeah..."
            elif s3_mc.current_partner == "AJ":
                aj "Yeah..."

            s3_mc "It's a nice, hot, sweet..."
            s3_mc "...cup of tea."

            if s3_mc.current_partner == "Bill":
                bill "Oh. You want a cuppa."
                bill "Actually, I could really go for one too."
            elif s3_mc.current_partner == "Camilo":
                camilo "Oh. You want a cuppa."
                camilo "Actually, I could really go for one too."
            elif s3_mc.current_partner == "Harry":
                harry "Oh. You want a cuppa."
                harry "Actually, I could really go for one too."
            elif s3_mc.current_partner == "AJ":
                aj "Oh. You want a cuppa."
                aj "Actually, I could really go for one too."

    "As Genevieve emerges and switches the lights on, Seb puts a pillow over his head and groans."
    seb "Ugh, turn it off!"
    genevieve "You're awake already! Your body clock says it's time to get up."
    seb "Can I put my body clock on snooze?"
    seb "I just need another hour. I'm knackered."
    nicky "Come on man! Today's the best day ever."

    if s3_mc.current_partner != "AJ":
        "Seb shivers and looks over at AJ who has taken all the sheets."
        seb "You didn't have to wrestle AJ for a sliver of duvet."
        "AJ stirs and Seb takes the opportunity to steal some back."
        aj "Hey!"
        "AJ sits up sleepily."
        aj "Might as well get up then."
        nicky "C'mon, it's the furthest we're going to be from another recoupling."
        s3_mc "Nicky's got a point. That's worth celebrating."
        seb "Fair point."
        "Seb jumps out of the bed and the Islanders cheer."
        seb "Time to seize the day."
        "AJ jumps up with a smile and starts jogging on the spot."
        aj "Yes! That's the Seb I've been waiting for!"
        aj "What do you say? A couple of laps and then we hit the gym?"
        seb "Er, maybe after brekkie. You get a head start and I'll join you."
        "AJ smiles brightly and bounds into the dressing room."
        nicky "You're going to hit the gym?"
        seb "No way. But have you tried to say no to AJ?"
        seb "I just haven't got the energy."
        camilo "The name of Seb's sex tape."
    else:
        "Seb looks over at you and AJ before covering his face with the duvet."
        seb "Unless you missed it, my night didn't end so well."
        s3_mc "C'mon Seb, remember our chat? The Villa's your oyster now!"
        seb "Can't stand oysters. They're like giant bogies in shells."
        
        "[s3e3p3_get_to_know] sits up and throws a pillow at Seb. He smiles."

        if s3e3p3_get_to_know != "Genevieve":
            if s3e3p3_get_to_know == "Miki":
                miki "Wow, a smile. I must have the magic touch."
            elif s3e3p3_get_to_know == "Iona":
                iona "Wow, a smile. I must have the magic touch."
            elif s3e3p3_get_to_know == "Elladine":
                elladine "Wow, a smile. I must have the magic touch."

            "Seb glances in your direction and you give him a wink."
            thought "Was she flirting?"
            thought "I may have actually given Seb some good advice."
        else:
            genevieve "Right, misery guts. I am putting a smile on that face today even if I have to draw it on."
            seb "You won't be able to. I'm notoriously sour faced. Ask my mum."
            genevieve "Well, Seb's mum, prepare to be amazed."
            "A smile touches the corner of his lips and he shoots you a knowing look."
            thought "Viv definitely brings out his softer side."
            thought "They'd make a lovely couple."


    "Camilo jumps out of bed and stretches."
    camilo "Ain't gonna lie, we're all set for a sexy day."
    "Bill claps his hands together with a grin."
    bill "Come on girls, time to get all leathery in the sun."


    if s3_mc.current_partner != "AJ":
        "[s3e3p3_lonely_one] chucks a pillow at Bill and it hits him square in the face."
        bill "Someone woke up in a mood."

        if s3_3rd_girl_options[s3_mc.current_partner] == "Miki":
            miki "Actually, I feel great."
            miki "It's nice having the whole bed to yourself."
            miki "Especially after sharing a bed with that human starfish..."
            bill "You could've asked me for more space..."
        elif s3_3rd_girl_options[s3_mc.current_partner] == "Iona":
            iona "Actually, I feel great."
            iona "It's nice having the whole bed to yourself."
            iona "It beats being almost pushed off the bed."
            camilo "I can't help it if I'm a cuddler."
        elif s3_3rd_girl_options[s3_mc.current_partner] == "Genevieve":
            genevieve "Actually, I feel great."
            genevieve "It's nice having the whole bed to yourself."
            genevieve "No more being woken up at the crack of dawn."
            harry "You said you didn't even notice when I got up!"
    else:
        seb "Right, who's getting in the kitchen to cook me up some brekkie?"
        "A flurry of pillows go flying towards Seb."
        seb "Fine. Cereal out the box it is."

    if s3e4p1_kiss_or_cuddle == True:
        if s3_mc.current_partner == "Bill":
            bill "Right, enough chit-chat. I'm off to get this one a morning beverage."
        elif s3_mc.current_partner == "Camilo":
            camilo "Right, enough chit-chat. I'm off to get this one a morning beverage."
        elif s3_mc.current_partner == "Harry":
            harry "Right, enough chit-chat. I'm off to get this one a morning beverage."
        elif s3_mc.current_partner == "AJ":
            aj "Right, enough chit-chat. I'm off to get this one a morning beverage."

        # CHOICE
        menu:
            thought "[s3_mc.current_partner] is going to get me a drink. I want..."
            "A glass of bubbles":
                pass
            "A cuppa":
                pass
            "A matcha latte":
                pass

        if s3_mc.current_partner == "Bill":
            bill "I could probably rustle you up a regular breakfast tea..."
        elif s3_mc.current_partner == "Camilo":
            camilo "I could probably rustle you up a regular breakfast tea..."
        elif s3_mc.current_partner == "Harry":
            harry "I could probably rustle you up a regular breakfast tea..."
        elif s3_mc.current_partner == "AJ":
            aj "I could probably rustle you up a regular breakfast tea..."
    else:
        if s3_mc.current_partner == "Bill":
            bill "You still fancy that tea?"
            s3_mc "Is an elephant heavy?"
            bill "I'll get on it then."
        elif s3_mc.current_partner == "Camilo":
            camilo "You still fancy that tea?"
            s3_mc "Is an elephant heavy?"
            camilo "I'll get on it then."
        elif s3_mc.current_partner == "Harry":
            harry "You still fancy that tea?"
            s3_mc "Is an elephant heavy?"
            harry "I'll get on it then."
        elif s3_mc.current_partner == "AJ":
            aj "You still fancy that tea?"
            s3_mc "Is an elephant heavy?"
            aj "I'll get on it then."

    "You jump out of bed."
    s3_mc "I'm coming with you."
    elladine "Aw, I am loving this. You two are such a couple already. No offence [s3e3p3_lonely_one]."

    if s3_3rd_girl_options[s3_mc.current_partner] == "Miki":
        miki "Nah, it's proper cute."
    elif s3_3rd_girl_options[s3_mc.current_partner] == "Iona":
        iona "Nah, it's proper cute."
    elif s3_3rd_girl_options[s3_mc.current_partner] == "Genevieve":
        genevieve "Nah, it's proper cute."
    elif s3_3rd_girl_options[s3_mc.current_partner] == "Seb":
        seb "Nah, it's proper cute."

    s3_mc "I just want to make sure [he_she] gets it just the way I like it."

    if s3_mc.current_partner == "Bill":
        bill "I can make a cuppa."
        bill "My way's foolproof. First you need to..."
    elif s3_mc.current_partner == "Camilo":
        camilo "That's sweet. I like having someone in the kitchen with me."
        camilo "And I wouldn't want to mess up your tea."
    elif s3_mc.current_partner == "Harry":
        harry "I'm from Yorkshire, we practically invented tea."
        s3_mc "Less talk, more tea!"
    elif s3_mc.current_partner == "AJ":
        bill "Make sure you unplug the toaster."
        nicky "I'll alert the fire brigade."
        s3_mc "Very funny."
        aj "That might not be a bad idea."

    s3_mc "But first I'm going to get changed. See you in the kitchen, babe."
    "You bound off towards the dressing room."

    scene s3-dressing-room with dissolve
    $ new_scene()

    "You quickly check yourself out in the mirror and tousle your hair."

    # CHOICE
    menu:
        thought "I am looking good."
        "Blow yourself a kiss":
            "You blow your reflection a kiss."
            thought "Morning gorgeous."
        "Compliment your fine self":
            thought "Damn girl. You are looking fine. [s3_mc.current_partner] is one lucky Islander."
        "Spray your face with toner":
            "You close your eyes and spray the cool water onto your face."
            thought "So refreshing."

    thought "All I need now is a gorgeous outfit!"
    thought "Something that'll say to [s3_mc.current_partner] 'you just levelled up, hun'."

    # Add back once MC images are added to the game.
    # MC outfit changes to swimwear
    $ outfit = "swim"
    call customize_outfit from _call_customize_outfit_9
    # thought "Meh, this will do I guess."
    # thought "It's tea time!"
    thought "Looks good to me!"
    thought "Yup. This is definitely the ticket."

    scene s3-kitchen-day with dissolve
    $ new_scene()

    "You never forget your first."
    "Mine was in a bed and breakfast in Dorset."
    "The sun was just coming up..."
    "Gold top milk, two sugar cubes..."
    "What did you lot think I was talking about? Mind in the gutter..."
    "[s3_mc.current_partner] is in the kitchen filling up the kettle."

    $ pronouns(s3_li)

    # Add back when MC images are added to the game.
    # "[he_she!c] spies you coming towards [him_her]."
    # if s3_mc.current_partner == "Bill":
    #     bill "There's my girl. Ready for your tea?"
    # elif s3_mc.current_partner == "Camilo":
    #     camilo "There's my girl. Ready for your tea?"
    # elif s3_mc.current_partner == "Harry":
    #     harry "There's my girl. Ready for your tea?"
    # elif s3_mc.current_partner == "AJ":
    #     aj "There's my girl. Ready for your tea?"
    # s3_mc "Am I ever."
    
    # if s3_mc.current_partner == "Bill":
    #     bill "Oh really?"
    #     s3_mc "Where's this brew then?"
    #     bill "Oh, yeah. The tea."
    # elif s3_mc.current_partner == "Camilo":
    #     camilo "Oh really?"
    #     s3_mc "Where's this brew then?"
    #     camilo "Oh, yeah. The tea."
    # elif s3_mc.current_partner == "Harry":
    #     harry "Oh really?"
    #     s3_mc "Where's this brew then?"
    #     harry "Oh, yeah. The tea."
    # elif s3_mc.current_partner == "AJ":
    #     aj "Oh really?"
    #     s3_mc "Where's this brew then?"
    #     aj "Oh, yeah. The tea."

    "[he_she!c] spies you coming towards [him_her]."
    if s3_mc.current_partner == "Bill":
        bill "There's my girl, pretty as always."
    elif s3_mc.current_partner == "Camilo":
        camilo "There's my girl, pretty as always."
    elif s3_mc.current_partner == "Harry":
        harry "There's my girl, pretty as always."
    elif s3_mc.current_partner == "AJ":
        aj "There's my girl, pretty as always."
    s3_mc "You're so sweet."
    s3_mc "And thirsty."

    # "[he_she!c] spies you coming towards [him_her] and does a double take."

    # if s3_mc.current_partner == "Bill":
    #     bill "Wow. You are just... wow."
    #     bill "I want to make you two cups of tea now."
    # elif s3_mc.current_partner == "Camilo":
    #     camilo "Wow. You are just... wow."
    #     camilo "I want to make you two cups of tea now."
    # elif s3_mc.current_partner == "Harry":
    #     harry "Wow. You are just... wow."
    #     harry "I want to make you two cups of tea now."
    # elif s3_mc.current_partner == "AJ":
    #     aj "Wow. You are just... wow."
    #     aj "I want to make you two cups of tea now."

    # s3_mc "You're so sweet."
    # s3_mc "And thirsty."

    if s3_mc.current_partner == "Bill":
        bill "Oh really?"
        s3_mc "Where's this brew then?"
        bill "Oh, yeah. The tea."
    elif s3_mc.current_partner == "Camilo":
        camilo "Oh really?"
        s3_mc "Where's this brew then?"
        camilo "Oh, yeah. The tea."
    elif s3_mc.current_partner == "Harry":
        harry "Oh really?"
        s3_mc "Where's this brew then?"
        harry "Oh, yeah. The tea."
    elif s3_mc.current_partner == "AJ":
        aj "Oh really?"
        s3_mc "Where's this brew then?"
        aj "Oh, yeah. The tea."

    "[s3_mc.current_partner] grabs two mugs, sugar and the box of teabags. [he_she] puts the kettle on."
    s3_mc "You look so focused."
    aj "I'm trying to impress you aren't I?"

    # CHOICE
    menu:
        thought "[s3_mc.current_partner] wants to impress me..."
        "You don't need to impress me":
            "[s3_mc.current_partner] turns and wraps [his_her] arms around your waist."

            if s3_mc.current_partner == "Bill":
                bill "I know. But I really want to."
                s3_mc "That's really sweet, hun."
                s3_mc "I hope you're this keen to please all the time..."
                bill "You'll find out soon enough."
            elif s3_mc.current_partner == "Camilo":
                camilo "I know. But I really want to."
                s3_mc "That's really sweet, hun."
                s3_mc "I hope you're this keen to please all the time..."
                camilo "You'll find out soon enough."
            elif s3_mc.current_partner == "Harry":
                harry "I know. But I really want to."
                s3_mc "That's really sweet, hun."
                s3_mc "I hope you're this keen to please all the time..."
                harry "You'll find out soon enough."
            elif s3_mc.current_partner == "AJ":
                aj "I know. But I really want to."
                s3_mc "That's really sweet, hun."
                s3_mc "I hope you're this keen to please all the time..."
                aj "You'll find out soon enough."
        "Tea isn't really impressive":
            if s3_mc.current_partner == "Bill":
                bill "Oh. Yeah. I mean, like, as a start."
                s3_mc "If tea's where this all starts, I'm not sure I want to see where it's going."
                bill "Wow, high maintenance, are you?"
                s3_mc "Let's just say it takes a lot to impress me."
                bill "Challenge accepted."
            elif s3_mc.current_partner == "Camilo":
                camilo "Oh. Yeah. I mean, like, as a start."
                s3_mc "If tea's where this all starts, I'm not sure I want to see where it's going."
                camilo "Wow, high maintenance, are you?"
                s3_mc "Let's just say it takes a lot to impress me."
                camilo "Challenge accepted."
            elif s3_mc.current_partner == "Harry":
                harry "Oh. Yeah. I mean, like, as a start."
                s3_mc "If tea's where this all starts, I'm not sure I want to see where it's going."
                harry "Wow, high maintenance, are you?"
                s3_mc "Let's just say it takes a lot to impress me."
                harry "Challenge accepted."
            elif s3_mc.current_partner == "AJ":
                aj "Oh. Yeah. I mean, like, as a start."
                s3_mc "If tea's where this all starts, I'm not sure I want to see where it's going."
                aj "Wow, high maintenance, are you?"
                s3_mc "Let's just say it takes a lot to impress me."
                aj "Challenge accepted."
        "Buy me diamonds!":
            "[s3_mc.current_partner] raises an eyebrow."

            if s3_mc.current_partner == "Bill":
                bill "You want diamonds?"
                s3_mc "Ooh yeah, a big one. Princess cut."
                bill "A diamond ring..."
                s3_mc "Or a necklace. No! Wait! A tiara."
                bill "Let's start with the tea."
            elif s3_mc.current_partner == "Camilo":
                camilo "You want diamonds?"
                s3_mc "Ooh yeah, a big one. Princess cut."
                camilo "A diamond ring..."
                s3_mc "Or a necklace. No! Wait! A tiara."
                camilo "Let's start with the tea."
            elif s3_mc.current_partner == "Harry":
                harry "You want diamonds?"
                s3_mc "Ooh yeah, a big one. Princess cut."
                harry "A diamond ring..."
                s3_mc "Or a necklace. No! Wait! A tiara."
                harry "Let's start with the tea."
            elif s3_mc.current_partner == "AJ":
                aj "You want diamonds?"
                s3_mc "Ooh yeah, a big one. Princess cut."
                aj "A diamond ring..."
                s3_mc "Or a necklace. No! Wait! A tiara."
                aj "Let's start with the tea."

    "The hiss of the kettle interrupts you both. [s3_mc.current_partner] grabs the mugs."
    s3_mc "Now this is where it gets serious."
    s3_mc "You can tell a lot about a person from the way they like their tea."

    if s3_mc.current_partner == "Bill":
        bill "Is that right now?"
        bill "Right, I've got a bit of a confession to make."
        s3_mc "You don't know how to make tea?"
        bill "I'm not that bad! Just, I'm more of a coffee drinker."
        "[he_she!c] pops a teabag in the mug, adds a teaspoon of sugar and gives the cup a stir."
        "After a few moments [he_she] removes the teabag and adds milk."
    elif s3_mc.current_partner == "Camilo":
        camilo "Is that right now?"
        "Camilo grabs the milk and pours a splash into a mug. He adds a teabag and tops it up with hot water."
    elif s3_mc.current_partner == "Harry":
        harry "Is that right now?"
        "Harry pops in a spoon of sugar and a teabag, and fills the mug up halfway with hot water."
        "He then tops it up with milk and takes out the teabag."
        "He takes a sip of the milky drink."
    elif s3_mc.current_partner == "AJ":
        aj "Is that right now?"
        aj "Right, I've got a bit of a confession to make."
        s3_mc "You don't know how to make tea?"
        aj "I'm not that bad! Just, I'm more of a coffee drinker."
        "[he_she!c] pops a teabag in the mug, adds a teaspoon of sugar and gives the cup a stir."
        "After a few moments [he_she] removes the teabag and adds milk."

    # CHOICE
    menu:
        s3_mc "The way you make a cup of tea is..."
        "Poetry in motion":
            $ s3_mc.like(s3_mc.current_partner)
            if s3_mc.current_partner == "Bill":
                bill "It's not rocket science, just a teabag in a mug."
                s3_mc "I'll have mine just the same."
                bill "Coming right up."
            elif s3_mc.current_partner == "Camilo":
                camilo "It's not rocket science, just a teabag in a mug."
                s3_mc "I'll have mine just the same."
                camilo "Coming right up."
            elif s3_mc.current_partner == "Harry":
                harry "It's not rocket science, just a teabag in a mug."
                s3_mc "I'll have mine just the same."
                harry "Coming right up."
            elif s3_mc.current_partner == "AJ":
                aj "It's not rocket science, just a teabag in a mug."
                s3_mc "I'll have mine just the same."
                aj "Coming right up."
            "[s3_mc.current_partner] makes you the tea with a silly smile plastered on [his_her] face."
        "A crime against humani-tea":
            $ s3_mc.dislike(s3_mc.current_partner)
            if s3_mc.current_partner == "Bill":
                bill "What's wrong with how I make it?"
                s3_mc "Two teabags? Four sugars!"
                s3_mc "Let's just say you should stick to coffee, babe."
            elif s3_mc.current_partner == "Camilo":
                camilo "What's wrong with how I make it?"
                s3_mc "Milk first? Ugh."
            elif s3_mc.current_partner == "Harry":
                harry "What's wrong with how I make it?"
                s3_mc "The tea bag was only in the mug for two seconds!"
            elif s3_mc.current_partner == "AJ":
                aj "What's wrong with how I make it?"
                s3_mc "Two teabags? Four sugars!"
                s3_mc "Let's just say you should stick to coffee, babe."    
            s3_mc "I'll make my own."
        "Not very entertaining...":
            if s3_mc.current_partner == "Bill":
                bill "When is watching someone making tea entertaining?"
                s3_mc "Sometimes there's a bit of showmanship."
                bill "Like what? Fireworks and a striptease?"
                s3_mc "That would have been entertaining."
                bill "What are you like."
            elif s3_mc.current_partner == "Camilo":
                camilo "When is watching someone making tea entertaining?"
                s3_mc "Sometimes there's a bit of showmanship."
                camilo "Like what? Fireworks and a striptease?"
                s3_mc "That would have been entertaining."
                camilo "What are you like."
            elif s3_mc.current_partner == "Harry":
                harry "When is watching someone making tea entertaining?"
                s3_mc "Sometimes there's a bit of showmanship."
                harry "Like what? Fireworks and a striptease?"
                s3_mc "That would have been entertaining."
                harry "What are you like."
            elif s3_mc.current_partner == "AJ":
                aj "When is watching someone making tea entertaining?"
                s3_mc "Sometimes there's a bit of showmanship."
                aj "Like what? Fireworks and a striptease?"
                s3_mc "That would have been entertaining."
                aj "What are you like."

            "[s3_mc.current_partner] slides you your tea."

    "You both sip your cuppa."
    "[s3_mc.current_partner] glances at you over the rim of [his_her] mug. You see a smile touch the corner of [his_her] lips."

    if s3_mc.current_partner == "Bill":
        bill "I could get used to starting my day like this."
        bill "Sexy girl in front of me, sipping a steamy beverage..."
    elif s3_mc.current_partner == "Camilo":
        camilo "I could get used to starting my day like this."
        camilo "Sexy girl in front of me, sipping a steamy beverage..."
    elif s3_mc.current_partner == "Harry":
        harry "I could get used to starting my day like this."
        harry "Sexy girl in front of me, sipping a steamy beverage..."
    elif s3_mc.current_partner == "AJ":
        aj "I could get used to starting my day like this."
        aj "Sexy girl in front of me, sipping a steamy beverage..."

    # CHOICE
    menu:
        thought "[s3_mc.current_partner] is flirting with me. I should..."
        "Get a cheeky snog in":
            "You step towards [s3_mc.current_partner] and go in for a kiss."
            "[his_her!c] hands tighten around your waist. The faint taste of tea remains on [his_her] lips."
            if s3_mc.current_partner == "Bill":
                bill "Yeah, I could definitely do this every morning."
            elif s3_mc.current_partner == "Camilo":
                camilo "Yeah, I could definitely do this every morning."
            elif s3_mc.current_partner == "Harry":
                harry "Yeah, I could definitely do this every morning."
            elif s3_mc.current_partner == "AJ":
                aj "Yeah, I could definitely do this every morning."
        "Play it cool":
            "You take a sip of your tea and smile coyly."
            s3_mc "We'll see how it goes."
        "Flirt back":
            s3_mc "This is great, but I can think of at least one thing that could top it."
            "You run your fingers up [s3_mc.current_partner]'s arm and [he_she] bites [his_her] bottom lip."
            if s3_mc.current_partner == "Bill":
                bill "Maybe we can start today again..."
            elif s3_mc.current_partner == "Camilo":
                camilo "Maybe we can start today again..."
            elif s3_mc.current_partner == "Harry":
                harry "Maybe we can start today again..."
            elif s3_mc.current_partner == "AJ":
                aj "Maybe we can start today again..."

    if s3_mc.bff == "Elladine":
        elladine "Hey..."
        elladine "You two weren't cracking on in the kitchen, were you?"
    elif s3_mc.bff == "Genevieve":
        genevieve "Hey..."
        genevieve "You two weren't cracking on in the kitchen, were you?"
    elif s3_mc.bff == "Nicky":
        nicky "Hey..."
        nicky "You two weren't cracking on in the kitchen, were you?"
    elif s3_mc.bff == "Seb":
        seb "Hey..."
        seb "You two weren't cracking on in the kitchen, were you?"

    "[s3_mc.current_partner] scratches the back of [his_her] neck and you carry on drinking your tea."
    s3_mc "Just enjoying some time alone."

    if s3_mc.current_partner == "Bill":
        bill "Having a chat."
    elif s3_mc.current_partner == "Camilo":
        camilo "Having a chat."
    elif s3_mc.current_partner == "Harry":
        harry "Having a chat."
    elif s3_mc.current_partner == "AJ":
        aj "Having a chat."

    if s3_mc.bff == "Elladine":
        elladine "Well, we're over by the loungers for when you two are done doing whatever it is you're doing."
    elif s3_mc.bff == "Genevieve":
        genevieve "Well, we're over by the loungers for when you two are done doing whatever it is you're doing."
    elif s3_mc.bff == "Nicky":
        nicky "Well, we're over by the loungers for when you two are done doing whatever it is you're doing."
    elif s3_mc.bff == "Seb":
        seb "Well, we're over by the loungers for when you two are done doing whatever it is you're doing."

    "[s3_mc.bff] gives you a wink, grabs some fruit and heads out."

    if s3_mc.bff == "Elladine":
        show elladine at npc_exit
    elif s3_mc.bff == "Genevieve":
        show genevieve at npc_exit
    elif s3_mc.bff == "Nicky":
        show nicky at npc_exit
    elif s3_mc.bff == "Seb":
        show seb at npc_exit

    pause .3
    $ renpy.hide(s3_mc.bff.lower())
    $ on_screen.remove(s3_mc.bff.lower())

    s3_mc "Well, it was nice while it lasted."
    "[s3_mc.current_partner] smiles at you warmly. You both make your way to the loungers."

    scene s3-sun-loungers-day with dissolve
    $ new_scene()

    "You, [s3_mc.current_partner] and the other Islanders are lounging by the pool. Your empty mug sits by your side. Laughter fills the air."

    "Bill's setting the world to rights and he's starting with vegetables."
    bill "And that's why you're better off using a cucumber."
    harry "Mate, I want to agree with you, but it just sounds disgusting."
    camilo "It's a risotto! Who puts cucumber in it?"
    "Well, I'm glad someone cleared that up for me..."
    iona "I don't know, they kinda do look exactly the same."
    bill "Exactly! Only a courgette is fanicer. A cucumber works just as well."
    camilo "Name of Bill's sex tape."
    "The girls giggle and Bill just rolls his eyes."
    iona "If you were going to make a sex tape what would you actually call it?"
    nicky "Easy. True Grit."
    "The Islanders groan and Elladine pulls a face of disgust."
    iona "How is that sexy?"
    nicky "It's not, I just think it's a great movie. Wait, you meant sex tape?"
    elladine "Mine would be something sensual..."
    "She thinks for a moment, then says something in Welsh."
    miki "That's a bit of a mouthful, isn't it?"
    genevieve "Name of Miki's sex tape!"
    "Camilo and Genevieve high five. Miki shakes her head, laughing."
    miki "What about you, [s3_name]? What would you name your naughty video?"
    "The Islanders turn to you."

    # CHOICE
    menu:
        s3_mc "Hmm, my sex tape would be called..."
        "Inspect Her Gadget":
            if s3_mc.current_partner == "Bill":
                bill "You don't have to ask me twice..."
            elif s3_mc.current_partner == "Camilo":
                camilo "You don't have to ask me twice..."
            elif s3_mc.current_partner == "Harry":
                harry "You don't have to ask me twice..."
            elif s3_mc.current_partner == "AJ":
                aj "You don't have to ask me twice..."
            elladine "[s3_name], you're so dirty!"
        "Missionary Impossible":
            camilo "Did you just came up with that?"
            s3_mc "What can I say, I'm a natural."
        "Sin-derella":
            bill "If the shoe fits..."
            s3_mc "Very funny."
        "I wouldn't make one!":
            seb "That's a crap name for a... Oh, I see what you did there."
            if s3_mc.current_partner == "Bill":
                bill "I get it, it's not for everybody."
            elif s3_mc.current_partner == "Camilo":
                camilo "I get it, it's not for everybody."
            elif s3_mc.current_partner == "Harry":
                harry "I get it, it's not for everybody."
            elif s3_mc.current_partner == "AJ":
                aj "I get it, it's not for everybody."
            s3_mc "No judgement guys, just not my thing."
            "[s3_mc.current_partner] smiles and squeezes your hand."

    bill "Fast and Furious would be a good one too. You wouldn't even need to change the name."
    harry "I've actually driven one of those cars."
    iona "From the film? For real? That's so cool."
    harry "Yeah, normally you need special training, but I know my way around a car."
    bill "Yeah, all the way round to the passenger side."
    "The Islanders all laugh, except for Harry who sits up."
    harry "I do, actually. They said I was a natural."
    bill "Yeah, course. Next thing he'll be saying is he was Arnie's stunt double in Expendables 2."
    bill "What did you do after? Go on a date with Zendaya? Regular James Bond this one."
    "The Islanders laugh playfully."
    "Harry frowns, and his jaw tightens. It's clear the vibe has changed."
    thought "Harry doesn't look like he's finding this funny."
    thought "I should decide if I want to be around this conversation."

    # CHOICE
    menu:
        thought "Shall I get involved?"
        "I'll say something":
            $ s3e4p1_harry_incident = True
            # SUB-CHOICE
            menu: 
                thought "Hmm, what shall I say?"
                "Tell Bill to stop":
                    s3_mc "Give it a rest, Bill."
                    bill "What? He was the one who brought it up."
                "Ask if Harry's OK":
                    "You catch Harry's eye and mouth 'Are you OK'?"
                    "He forces a smile and nods."
                    thought "Bill's still talking..."
                "Change the subject":
                    s3_mc "You know what's a good film? Any film with Ryan Gosling."
                    iona "I would. He is so fit."
                    bill "Yeah, Drive was awesome. Did you have a go on that car too, Harry?"

            "Harry folds his arms and lies back down."
            bill "Sorry, mate, I was just playing around. Tell us about the car then."
            "Harry inhales deeply, still frowning."
            harry "No thanks."
            seb "C'mon mate, what was it like? Fast or furious?"
            "Harry shakes his head stubbornly."
            bill "Mate, there's no need to be weird about it, it was just a..."
            "Harry jumps up."
            bill "What are you doing, mate?"
            harry "Everyone needs to stop talking to me."
            
            scene s3-poolside-day with dissolve
            $ new_scene()

            "Harry strides towards the pool and dives in."
            s3_mc "Woah!"
            bill "My hair!"
            "You watch as Harry resurfaces. He walks back slowly, looking more relaxed, and lies down on a lounger."

            # SUB-CHOICE
            menu:
                thought "That's one way of ending a discussion..."
                "Lie back and enjoy the sun":
                    bill "I'm not trying to be funny or anything, but what just happened, mate?"
                "Ask what was that about":
                    s3_mc "Hey Harry, what just happened?"
                "Nudge Bill to say something":
                    bill "I'm not trying to be funny or anything, but what just happened, mate?"

            aj "Harry literally just jumped into the..."
            bill "We know what literally happened, AJ."
            harry "I'm sorry. I've always had a short temper. Ever since I was a kid."
            harry "You wouldn't think it, but I was always getting into fights."
            iona "I know plenty of folk who've got anger management issues."
            harry "Yeah, I guess you could call it that. I've been getting therapy for it though."
            harry "I don't lose it with anyone anymore, but sometimes the littlest thing can set me off."
            aj "And so... you jump in the pool?"

            # SUB-CHOICE
            menu:
                thought "Harry jumped into the pool because he was angry..."
                "I don't get it":
                    s3_mc "I mean, why jump in the pool?"
                "I totally get it":
                    s3_mc "It cools you off, right?"
                    harry "Something like that."
                "What happens if there's no pool?":
                    s3_mc "I mean do you just go all Hulk?"

            "Harry exhales."
            harry "It doesn't have to be a pool. Sometimes I just splash my face with water."
            harry "It's something we came up with in therapy."
            genevieve "It's a distraction thing, right?"
            harry "Yeah! Sort of."
            harry "Your body temperature goes up when you get angry, so you're literally cooling yourself down."
            "Harry smiles, then turns back to Bill."
            harry "I know you were kidding. The anger just builds up sometimes. I feel like a right doughnut."
            bill "I didn't mean to upset you, mate. I was genuinely just messing about."
            seb "You're not a doughnut. You've found your own way of coping with a really tricky emotion."
            seb "That's really cool."
            harry "Yeah, therapy helped me out. Big time."
            bill "I'm glad to hear it, mate. I'm sorry again."
            harry "I know. I'm fine now, don't worry about it."
            "Bill gets up and walks over to the pool edge."
            "He grins at Harry and then flops into the pool."
            miki "Bill! My hair! You've soaked me completely!"
            "Harry looks surprised as Bill pulls himself out of the pool and comes to sit by his side."
            harry "What did you go and do that for?"
            bill "You said you felt like a doughnut. That makes two of us now."
            bill "Two wet doughnuts."
            "Harry grins and Bill messes up his hair."

            # SUB-CHOICE
            menu:
                thought "Bill jumped in the pool to make Harry feel better..."
                "That makes no sense":
                    thought "Who even understands these boys?"
                "That was really sweet":
                    thought "He cares about his mates."
                    "Bill catches you looking at him and smiles."
                "Now they're both wet and it's kinda hot":
                    "You bite your bottom lip and stare. Bill and Harry notice."
                    harry "You alright there, [s3_name]?"
                    s3_mc "Er, yeah, fine. I might jump in the pool myself."

            "Another splash rings out. AJ and Camilo have dived into the pool."

        "I'd rather go and grab a snack":
            scene s3-kitchen-day with dissolve
            $ new_scene()

            "You head to the kitchen and pick out a selection of fruit."

            scene s3-poolside-day with dissolve
            $ new_scene()
            "Bearing a huge bowl, you emerge to see the other Islanders splashing around in the pool."
            "Harry seems to have relaxed."

    aj "[s3_name]! Jump in!"
    camilo "Yeah, it's lovely. Good call Harry."

    # CHOICE
    menu:
        "Should I jump into the pool?"
        "Move out of the way, here comes the cannon ball":
            "You take a running jump towards the pool."
            "You tuck in your limbs and hit the water with an enormous splash."
        "I can't...My hair!":
            genevieve "Well, if you won't I will."
            "Genevieve whoops and jumps into the pool, splashing Miki."

    miki "You have got to be kidding me."
    "You look over and see Harry and Bill grinning."
    miki "Right, I might as well get in now. I'm already wet."
    miki "Wait! That could be the name of my sex tape!"
    camilo "Yes, Miki! You nailed it."
    harry "And that can be the name of yours, Camilo."
    "You climb out of the pool and dry off."
    thought "My shoulders are a bit stiff, I could do with a workout..."
    thought "And it would give me a chance for some good old-fashioned grafting."

    # CHOICE
    menu:
        "Who shall I invite to the gym?"
        "Bill":
            $ s3e4p1_invite_gym = "Bill"
        "Camilo":
            $ s3e4p1_invite_gym = "Camilo"
        "Harry":
            $ s3e4p1_invite_gym = "Harry"
        "AJ":
            $ s3e4p1_invite_gym = "AJ"

    $ pronouns(s3e4p1_invite_gym)

    s3_mc "Hey, [s3e4p1_invite_gym], fancy a workout?"
    "[s3e4p1_invite_gym] gives you a flirty look."

    if s3e4p1_invite_gym == "Bill":
        bill "You know it."
    elif s3e4p1_invite_gym == "Camilo":
        camilo "You know it."
    elif s3e4p1_invite_gym == "Harry":
        harry "You know it."
    elif s3e4p1_invite_gym == "AJ":
        aj "You know it."

    scene s3-gym-day with dissolve
    $ new_scene()

    thought "Time to work up a sweat!"
    "The breeze caresses your skins as you watch [s3e4p1_invite_gym] straddle the lat pulldown machine."
    thought "I wish I was that machine right now..."

    if s3_mc.job == "Athlete":
        if s3e4p1_invite_gym == "Bill":
            bill "I don't need to explain to you how one of these works..."
        elif s3e4p1_invite_gym == "Camilo":
            camilo "I don't need to explain to you how one of these works..."
        elif s3e4p1_invite_gym == "Harry":
            harry "I don't need to explain to you how one of these works..."
        elif s3e4p1_invite_gym == "AJ":
            aj "I don't need to explain to you how one of these works..."
    else:
        if s3e4p1_invite_gym == "Bill":
            bill "I always love getting my heart going on one of these. How about you?"
        elif s3e4p1_invite_gym == "Camilo":
            camilo "I always love getting my heart going on one of these. How about you?"
        elif s3e4p1_invite_gym == "Harry":
            harry "I always love getting my heart going on one of these. How about you?"
        elif s3e4p1_invite_gym == "AJ":
            aj "I always love getting my heart going on one of these. How about you?"

    # CHOICE
    menu:
        thought "[s3e4p1_invite_gym] wants to know if I train..."
        "Of course I do":
            s3_mc "I love to break a sweat."
            if s3e4p1_invite_gym == "Bill":
                bill "Nothing hotter than someone who trains."
            elif s3e4p1_invite_gym == "Camilo":
                camilo "Nothing hotter than someone who trains."
            elif s3e4p1_invite_gym == "Harry":
                harry "Nothing hotter than someone who trains."
            elif s3e4p1_invite_gym == "AJ":
                aj "Nothing hotter than someone who trains."
        "It's not really my thing":
            if s3e4p1_invite_gym == "Bill":
                bill "Then I'll show you the ropes."
                bill "Er, not that we're doing anything with ropes today."
            elif s3e4p1_invite_gym == "Camilo":
                camilo "Then I'll show you the ropes."
                camilo "Er, not that we're doing anything with ropes today."
            elif s3e4p1_invite_gym == "Harry":
                harry "Then I'll show you the ropes."
                harry "Er, not that we're doing anything with ropes today."
            elif s3e4p1_invite_gym == "AJ":
                aj "Then I'll show you the ropes."
                aj "Er, not that we're doing anything with ropes today."

    if s3e4p1_invite_gym == "Bill":
        bill "I'll get a firm grip on these handles..."
    elif s3e4p1_invite_gym == "Camilo":
        camilo "I'll get a firm grip on these handles..."
    elif s3e4p1_invite_gym == "Harry":
        harry "I'll get a firm grip on these handles..."
    elif s3e4p1_invite_gym == "AJ":
        aj "I'll get a firm grip on these handles..."

    thought "Hmm, that looks pretty heavy..."
    "[he_she!c] pulls down towards [his_her] chest."
    s3_mc "Are you sure that's not too much weight?"

    if s3e4p1_invite_gym == "Bill":
        bill "Hey, don't you worry about me."
    elif s3e4p1_invite_gym == "Camilo":
        camilo "Hey, don't you worry about me."
    elif s3e4p1_invite_gym == "Harry":
        harry "Hey, don't you worry about me."
    elif s3e4p1_invite_gym == "AJ":
        aj "Hey, don't you worry about me."

    "[s3e4p1_invite_gym] pulls and there is little movement. [he_she!c] tries again."
    s3_mc "Are you showing off for me?"

    if s3e4p1_invite_gym == "Bill":
        bill "Maybe a bit..."
        bill "I can do it!"
    elif s3e4p1_invite_gym == "Camilo":
        camilo "Maybe a bit..."
        camilo "I can do it!"
    elif s3e4p1_invite_gym == "Harry":
        harry "Maybe a bit..."
        harry "I can do it!"
    elif s3e4p1_invite_gym == "AJ":
        aj "Maybe a bit..."
        aj "I can do it!"

    "[s3e4p1_invite_gym] tries again to no avail. [he_she!c] stops and has a look at the weight."

    if s3e4p1_invite_gym == "Bill":
        bill "Who was last on this? The Rock?"
    elif s3e4p1_invite_gym == "Camilo":
        camilo "Who was last on this? The Rock?"
    elif s3e4p1_invite_gym == "Harry":
        harry "Who was last on this? The Rock?"
    elif s3e4p1_invite_gym == "AJ":
        aj "Who was last on this? The Rock?"

    if s3_mc.job == "Athlete":
        s3_mc "Me!"
        if s3e4p1_invite_gym == "Bill":
            bill "Woah... you're something else."
        elif s3e4p1_invite_gym == "Camilo":
            camilo "Woah... you're something else."
        elif s3e4p1_invite_gym == "Harry":
            harry "Woah... you're something else."
        elif s3e4p1_invite_gym == "AJ":
            aj "Woah... you're something else."
    else:
        s3_mc "I think it was Iona..."
        if s3e4p1_invite_gym == "Bill":
            bill "Woah. Does she put the pylons up by hand?"
        elif s3e4p1_invite_gym == "Camilo":
            camilo "Woah. Does she put the pylons up by hand?"
        elif s3e4p1_invite_gym == "Harry":
            harry "Woah. Does she put the pylons up by hand?"
        elif s3e4p1_invite_gym == "AJ":
            aj "Woah. Does she put the pylons up by hand?"

    "[s3e4p1_invite_gym] rubs [his_her] shoulder."
    s3_mc "Is your shoulder sore?"

    if s3e4p1_invite_gym == "Bill":
        bill "A little bit."
    elif s3e4p1_invite_gym == "Camilo":
        camilo "A little bit."
    elif s3e4p1_invite_gym == "Harry":
        harry "A little bit."
    elif s3e4p1_invite_gym == "AJ":
        aj "A little bit."

    thought "Poor [s3e4p1_invite_gym]..."
    thought "What if I give [him_her] a proper massage?"

    if s3e3p2_masseur == s3e4p1_invite_gym:
        thought "[he_she!c] gave me an amazing massage yesterday... "
        thought "It would be cute to return the favour."
        thought "Who knows, this time I might be able to get [him_her] to make some noise..."

    thought "They say touch brings you closer..."
    thought "And we could do with some of that."

    # CHOICE
    menu:
        thought "I should..."
        "Offer to give [s3e4p1_invite_gym] a massage":
            $ s3e4p1_massage = True
            $ s3_mc.like(s3e4p1_invite_massage)
            call s3e4p1_massage from _call_s3e4p1_massage
        "Take [him_her] to Viv to be checked out":
            s3_mc "If you're sore, Viv should take a look at you."
            if s3e4p1_invite_gym == "Bill":
                bill "Good idea. I don't want to get achey."
            elif s3e4p1_invite_gym == "Camilo":
                camilo "Good idea. I don't want to get achey."
            elif s3e4p1_invite_gym == "Harry":
                harry "Good idea. I don't want to get achey."
            elif s3e4p1_invite_gym == "AJ":
                aj "Good idea. I don't want to get achey."
            "You both stand up and head towards the pool."

    scene sand with dissolve
    $ on_screen = []

    if s3e4p1_massage:
        "Is it hot in here or is it just me?"
        "It's only going to get hotter on the next episode of Love Island..."
    else:
        "Oh [s3_name], [s3e4p1_invite_gym] thought [his_her] luck was in..."
        "Don't worry [s3e4p1_invite_gym]. Things sound like they'll be heating up in the challenge..."
    
    if s3_mc.current_partner == "Bill":
        bill "My rod's so stiff..."
    elif s3_mc.current_partner == "Camilo":
        camilo "My rod's so stiff..."
    elif s3_mc.current_partner == "Harry":
        harry "My rod's so stiff..."
    elif s3_mc.current_partner == "AJ":
        aj "I just can't find the hole!"

    "Sounds like it's going to be a right carry on..."

    jump s3e4p2
    return

label s3e4p1_massage:
    s3_mc "You're really tense. Do you want a massage?"

    if s3e4p1_invite_gym == "Bill":
        bill "You are a mind reader."
    elif s3e4p1_invite_gym == "Camilo":
        camilo "You are a mind reader."
    elif s3e4p1_invite_gym == "Harry":
        harry "You are a mind reader."
    elif s3e4p1_invite_gym == "AJ":
        aj "You are a mind reader."

    "You rub your hands over [s3e4p1_invite_gym]'s shoulders."
    "[he_she!c] lets out a sigh of pleasure."
    aj "Wow, that feels great. Have you done this before?"

    # CHOICE
    menu:
        thought "[s3e4p1_invite_gym] wants to know if I've done this before..."
        "I do it all the time":
            pass
        "Not very often":
            pass
        "I've got the magic touch":
            pass

    aj "Mmm, well, it feels amazing."
    "[he_she!c] stretches luxuriously, looking like a very happy cat."
    "Then [he_she] sighs."

    if s3e4p1_invite_gym == "Bill" and s3e4p1_harry_incident:
        bill "I feel bad about what happened with Harry."
        bill "I was just having a laugh. I didn't know he'd take it so personal."

        # CHOICE
        menu:
            thought "Bill feels bad about what happened with Harry..."
            "Be supportive":
                s3_mc "Hey, you didn't know."
                s3_mc "What matters is you listened, and you took the time to understand."
                bill "You're right."
            "Be critical":
                s3_mc "Just don't do it again."
                bill "He's a top lad. I was just having a laugh."
                bill "Trust me, I won't tease him again. Not now I know."
            "Focus on the massage":
                "You let your hands do the talking. Bill gives a happier sigh."

    if s3e4p1_invite_gym == "Harry" and s3e4p1_harry_incident:
        harry "Sorry about earlier. I'm a bit embarrassed if I'm honest."
        harry "I'm not very good at talking about my feelings."
        "You feel his shoulders tense."
        harry "Just I get so frustrated, and I bottle it all up inside and then before I know it..."
        s3_mc "You need to jump in the pool?"
        "Harry laughs."
        harry "Yeah."

        # CHOICE
        menu:
            thought "Harry's feeling a bit bad about what happened earlier. I'll..."
            "Make him smile":
                s3_mc "You wanna know what I want to know?"
                s3_mc "How is a cucumber anything like a courgette?"
                "Harry wipes his eyes and laughs, properly this time."
            "Reassure him":
                s3_mc "Hey, you're among friends. We understand. Don't overthink this."
                "Harry wipes his eyes and takes a deep breath before turning to face you."
            "Focus on the massage":
                "You let your hands do the talking. Harry wipes his eyes and gives a happier sigh."

    thought "[he_she!c]'s obviously enjoying this a lot!"
    "You carry on kneading [s3e4p1_invite_gym]'s shoulders."

    # CHOICE
    menu:
        thought "I should..."
        "Move into a head massage":
            "You slide your hands up [his_her] neck and as [he_she] moans with pleasure, you work your fingers into [his_her] hair."
        "Slide my hands down to [his_her] lower back":
            "Goosebumpbs appear on [his_her] shoulders as you work your way down [his_her] back."
            "[he_she!c] moans with delight as you work your fingertips into [his_her] hips."
        "Stick to the shoulder":
            "You keep kneading [his_her] shoulders. Your fingers work their way down [his_her] strong arms."
            "You feel [his_her] skin break out in goosebumps as [he_she] exhales deeply."

    s3_mc "Does that feel good?"

    if s3e4p1_invite_gym == "Bill":
        bill "So good."
    elif s3e4p1_invite_gym == "Camilo":
        camilo "So good."
    elif s3e4p1_invite_gym == "Harry":
        harry "So good."
    elif s3e4p1_invite_gym == "AJ":
        aj "So good."

    "[s3e4p1_invite_gym] turns around, a mischievous look in [his_her] eyes."

    if s3e4p1_invite_gym == "Bill":
        bill "If this was some master plan to get me right where you want me, mm..."
        bill "Well done."
        s3_mc "Oh really?"
        bill "You can run your hands all over me, if you want."
    elif s3e4p1_invite_gym == "Camilo":
        camilo "If this was some master plan to get me right where you want me, mm..."
        camilo "Well done."
        s3_mc "Oh really?"
        camilo "You can run your hands all over me, if you want."
    elif s3e4p1_invite_gym == "Harry":
        harry "If this was some master plan to get me right where you want me, mm..."
        harry "Well done."
        s3_mc "Oh really?"
        harry "You can run your hands all over me, if you want."
    elif s3e4p1_invite_gym == "AJ":
        aj "If this was some master plan to get me right where you want me, mm..."
        aj "Well done."
        s3_mc "Oh really?"
        aj "You can run your hands all over me, if you want."

    "You sit close behind [him_her]."

    # CHOICE
    menu:
        "[s3e4p1_invite_gym] says I can do whatever I like..."
        "Stroke [his_her] stomach":
            "You slowly slide your finger tips around [his_her] waist."
            "[his_her!c] skin is warm. You gently drag your nails over [his_her] tight abs."
            "[he_she!c] trembles at your touch."
        "Run my hands over [his_her] legs":
            "You slide your hands along [his_her] muscular thighs, letting your nails drag gently over [his_her] warm skin."
            "[he_she!c] murmurs with pleasure."
        "Kiss [his_her] neck":
            "You lean in close and your lips gently brush [his_her] neck."
            "[he_she!c] murmurs with pleasure as you slowly kiss [his_her] warm skin."

    s3_mc "Feeling better?"
    "[s3e4p1_invite_gym] bites his bottom lip and looks at you hungrily. "

    if s3e4p1_invite_gym == "Bill":
        bill "Like a brand new man."
    elif s3e4p1_invite_gym == "Camilo":
        camilo "Like a brand new man."
    elif s3e4p1_invite_gym == "Harry":
        harry "Like a brand new man."
    elif s3e4p1_invite_gym == "AJ":
        aj "Like a brand new woman."

    "[he_she] leans closer until the tips of your noses touch. [his_her] hands rest firmly on your hips."

    if s3e4p1_invite_gym == "Bill":
        bill "Have I told you how fit you are?"
    elif s3e4p1_invite_gym == "Camilo":
        camilo "Have I told you how fit you are?"
    elif s3e4p1_invite_gym == "Harry":
        harry "Have I told you how fit you are?"
    elif s3e4p1_invite_gym == "AJ":
        aj "Have I told you how fit you are?"
        
    s3_mc "Tell me again..."
    "[he_she] grimaces suddenly."
    s3_mc "You alright?"

    if s3e4p1_invite_gym == "Bill":
        bill "My shoulder's still aching..."
    elif s3e4p1_invite_gym == "Camilo":
        camilo "My shoulder's still aching..."
    elif s3e4p1_invite_gym == "Harry":
        harry "My shoulder's still aching..."
    elif s3e4p1_invite_gym == "AJ":
        aj "My shoulder's still aching..."

    s3_mc "OK, I insist we go and find Genevieve."
    "[s3e4p1_invite_gym] groans."

    if s3e4p1_invite_gym == "Bill":
        bill "OK..."
    elif s3e4p1_invite_gym == "Camilo":
        camilo "OK..."
    elif s3e4p1_invite_gym == "Harry":
        harry "OK..."
    elif s3e4p1_invite_gym == "AJ":
        aj "OK..."

    "You stand up to go. [s3e4p1_invite_gym] coils an arm around your waist and you head over to the pool."

    return


#########################################################################
## Episode 4, Part 2
#########################################################################
label s3e4p2:
    scene sand with dissolve
    $ on_screen = []

    show screen day_title(4, 2) with Pause(4)
    hide screen day_title with dissolve

    "Welcome back to Love Land! The best theme park in this hemisphere."
    "Our feature attraction is [s3_mc.current_partner], The Ride."
    "Which [s3_name] is having a lot of fun on right now."
    "Did I just do that whole bit for the sake of a pun? You're damn right I did."
    "Previously on Love Island..."
    "Things got a little heated when Bill did a Bill..."
    harry "Normally you need a special training, but I know my way around a car."
    bill "Yeah, all the way round to the passenger side."

    $ leaving("bill")
    $ leaving("harry")

    "And did we have a special guest in the Villa?"

    if s3e4p1_invite_gym == "Bill":
        bill "Who was last on this machine? The Rock?"
        $ leaving("bill")
    elif s3e4p1_invite_gym == "Camilo":
        camilo "Who was last on this machine? The Rock?"
        $ leaving("camilo")
    elif s3e4p1_invite_gym == "Harry":
        harry "Who was last on this machine? The Rock?"
        $ leaving("harry")
    elif s3e4p1_invite_gym == "AJ":
        aj "Who was last on this machine? The Rock?"
        $ leaving("aj")

    "Sadly not. But I do have a pet rock to keep me company during the long, dark nights here."
    "I call him 'Rocky' in honour of Bill's favourite film franchise."
    "Coming up!"
    "Iona shouts about her job a lot."

    iona "I rig pylons!"
    $ leaving("iona")

    "And innuendos are abound as our Islanders all pitch in for today's in-tents challenge."

    if s3_mc.current_partner == "Bill":
        bill "My rod's so stiff..."
        $ leaving("bill")
    elif s3_mc.current_partner == "Camilo":
        camilo "My rod's so stiff..."
        $ leaving("camilo")
    elif s3_mc.current_partner == "Harry":
        harry "My rod's so stiff..."
        $ leaving("harry")
    elif s3_mc.current_partner == "AJ":
        aj "I just can't find the hole!"
        $ leaving("aj")

    "Strap yourselves in! This is one rollercoaster you don't want to miss."
    "Sun's out, birds are singing, and our Islanders..."
    "...are in the lounge."
    "I don't know why we even flew them out here. Next time we'll send them to Skegness."

    scene s3-lounge with dissolve
    $ new_scene()

    "You lie sprawled across a sofa, your head resting on [s3_mc.current_partner]'s lap."
    "Iona fans herself with a palm leaf."
    miki "It's nice to get out of the heat for a while."
    camilo "Yeah, bruv. It's an oven out there..."
    iona "It's an oven in here!"

    if s3_mc.current_partner == "Bill":
        bill "Nah, that's just [s3_name].I mean, have you seen how hot she is?"
        s3_mc "[s3_mc.current_partner]!"
        bill "Don't even try and deny it."
    elif s3_mc.current_partner == "Camilo":
        camilo "Nah, that's just [s3_name].I mean, have you seen how hot she is?"
        s3_mc "[s3_mc.current_partner]!"
        camilo "Don't even try and deny it."
    elif s3_mc.current_partner == "Harry":
        harry "Nah, that's just [s3_name].I mean, have you seen how hot she is?"
        s3_mc "[s3_mc.current_partner]!"
        harry "Don't even try and deny it."
    elif s3_mc.current_partner == "AJ":
        aj "Nah, that's just [s3_name].I mean, have you seen how hot she is?"
        s3_mc "[s3_mc.current_partner]!"
        aj "Don't even try and deny it."
    
    iona "Pack it in, you two. I don't think I can take any more."

    # Can add back dialog option once MC images are in game
    # aj "Nah, that's just [s3_name]. I mean, have you seen her outfit today?"
    # s3_mc "You already said that earlier, babe."
    # aj "And?"

    harry "This is nothing. One time, my flat's boiler went on the blink and set itself to forty degrees!"
    harry "My ice lolly melted all over my head..."

    # CHOICE
    menu:
        s3_mc "You think this is hot? I once..."
        "Got stranded in Death Valley":
            s3_mc "Our car broke down in the middle of it. We were stuck there for half a day!"
            bill "Why were you even out there?"
            s3_mc "To sightsee! But like, there's nothing there. Just heat."
            nicky "It's meant to be pretty, tough, right?"
            s3_mc "Sure, if you like beige..."
            bill "That's a solid colour, to be fair."
        "Sat next to Tessa Thompson":
            "AJ lets out a squeal."
            aj "What?"
            aj "I would have been a mess!"
            nicky "She's proper cute, man."
            s3_mc "Even cuter in person."
            aj "I would give anything to just, like, touch her face."
            aj "Not for long or anything. Just like..."
            aj "...boop."
        "Was in a lift with Jason Momoa":
            "Iona's breath catches in her throat."
            iona "Shut up! No way!"
            s3_mc "Yeah way. He's... impressive."
            iona "That's an understatement."
            iona "Ugh, I'd let him blast me with his trident any day."
            genevieve "Oh my gosh, Iona."
        "Looked in a mirror":
            if s3_mc.current_partner == "Bill":
                bill "You're not wrong!"
            elif s3_mc.current_partner == "Camilo":
                camilo "You're not wrong!"
            elif s3_mc.current_partner == "Harry":
                harry "You're not wrong!"
            elif s3_mc.current_partner == "AJ":
                aj "You're not wrong!"
            iona "I love the confidence you have, babe."

    "The others laugh."
    nicky "Tell you what, this one time during a heatwave, an ex's cat hid this box of prawns we'd just bought."
    nicky "The next day we were tearing the place apart looking for what was causing the smell!"
    nicky "She even put my shoes outside."

    # CHOICE
    menu:
        thought "Are we seriously talking about your ex's prawns...?"
        "Can we change the subject?":
            # NEED TO FILL
            "EMPTY"
        "I mean, it's funny, keep going":
            $ s3_mc.like("Nicky")
            s3_mc "It's just weird is all..."
            nicky "Right so, we've looked everywhere. Changed the litter box. Bleached all the drains and all this."
            nicky "And it still honks."
            nicky "We're knackered by now, so we crash down onto the sofa..."
            nicky "... and a prawn slides out from under a cushion."
            s3_mc "What?"
            nicky "The little bugger had hid the box under our sofa cushion."
        "Tell me more about this cat...":
            $ s3_mc.dislike("Nicky")
            nicky "He was a proper terror."
            nicky "Adorable. But, like, a demon."
            nicky "This fluffy white thing whose favourite game was jumping on my head from a height..."
            nicky "Turns out he'd hidden the prawns under the sofa cushions."

    nicky "It took two boil washes to stop the fabric smelling like Billingsgate fish market..."
    seb "That's cats for you, man."
    "There's something fishy about that story."
    "But we won't get to the bottom of it now. It's challenge time!"
    miki "Oh, I got a text."
    text "Islanders, please make your way to the lawn for today's challenge. #someassemblyrequired #mightyerections"
    genevieve "I wonder what it is?"
    "Camilo looks out of the window."
    camilo "What're all those bundles on the lawn?"

    scene s3-lawn-day with dissolve
    $ new_scene()

    "In today's challenge, our girls have to help the lads pitch a tent."
    "No, not like that..."
    "An actual tent."
    "You lot are filthy."
    "All across the lawn are bundles of nylon, tent pegs, and collapsed metal poles."
    s3_mc "I've got a text."
    text "Islanders, it's time to find out how good you are with your hands in today's pitch a tent challenge."
    text "The couple with the best tent, as voted by the others, get to decide what everyone eats tonight. #tentlife #grabapole #canvastheneighbourhood"
    harry "Aw, man. I've never put up a proper tent. Even when I got to Glasto, I just use a pop up..."
    seb "Pop ups all the way, man. Tents are a faff."
    genevieve "We always get medical crew tents at festivals. I've never put one up before..."
    iona "Pfft. I rig pylons for a living, which are basically just big tents."
    elladine "They are?"
    iona "Well, no, but they're mostly wires and poles and stuff. This'll be a cinch."
    camilo "This is gonna be a huge pain."
    bill "Just follow the instructions, mate. It's simple."
    aj "Yeah! I used to put tents up in the Brownies all the time. It's really not that hard."

    # CHOICE
    menu:
        thought "Can I put up a tent?"
        "We've got this!":
            if s3_mc.current_partner == "Bill":
                bill "You know it, babe!"
            elif s3_mc.current_partner == "Camilo":
                camilo "I hope that means you're good at this..."
            elif s3_mc.current_partner == "Harry":
                harry "I hope that means you're good at this..."
            elif s3_mc.current_partner == "AJ":
                aj "You know it, babe!"
        "We're doomed":
            if s3_mc.current_partner == "Bill":
                bill "Nah, I believe in you, babe. I'll be here to help, too!"
            elif s3_mc.current_partner == "Camilo":
                camilo "Don't say that! Let's at least give it a go..."
            elif s3_mc.current_partner == "Harry":
                harry "Don't say that! Let's at least give it a go..."
            elif s3_mc.current_partner == "AJ":
                aj "Nah, I believe in you, babe. I'll be here to help, too!"
        "I care more about what we do in the tent...":
            $ s3_mc.like(s3_mc.current_partner)
            if s3_mc.current_partner == "Bill":
                bill "You and me both..."
            elif s3_mc.current_partner == "Camilo":
                camilo "You and me both..."
            elif s3_mc.current_partner == "Harry":
                harry "You and me both..."
            elif s3_mc.current_partner == "AJ":
                aj "You and me both..."

    elladine "Alright, let's quit the nattering and get on with it then!"
    miki "Woah, Elladine's got a competitive side."
    elladine "It's a task that needs completing. Nicky, grab those poles, we're going to do this right."
    nicky "No problem, babe."
    "He goes over to their bundle and picks it up."
    "Something comes undone, and the poles and small metal rings clatter to the ground."
    nicky "We may now have a problem."

    $ leaving("miki")
    $ leaving("nicky")

    "You and [s3_mc.current_partner] look down at your unassembled tent."

    if s3_mc.current_partner == "Bill":
        bill "Right then, first things first."
        "[he_she!c] scans through the instructions."
        bill "Seems simple enough."
        bill "We need to thread these rods through the, um, tenty bits."
        s3_mc "The holes?"
        bill "Yeah, tenty bits."
    elif s3_mc.current_partner == "Camilo":
        camilo "Right so... how'd we do this?"
        s3_mc "We've got the instructions right here."
        "He looks at them."
        camilo "I don't get this at all. It's like they're written in another language..."
        s3_mc "They're pictures?"
        camilo "Confusing pictures. But, I think I see what we need to do first..."
        camilo "We need to thread these rods through the, um, tenty bits."
        s3_mc "The holes?"
        camilo "Yeah, tenty bits."
    elif s3_mc.current_partner == "Harry":
        harry "Right so... how'd we do this?"
        s3_mc "We've got the instructions right here."
        "He looks at them."
        harry "I don't get this at all. It's like they're written in another language..."
        s3_mc "They're pictures?"
        harry "Confusing pictures. But, I think I see what we need to do first..."
        harry "We need to thread these rods through the, um, tenty bits."
        s3_mc "The holes?"
        harry "Yeah, tenty bits."
    elif s3_mc.current_partner == "AJ":
        aj "Right then, first things first."
        "[he_she!c] scans through the instructions."
        aj "Seems simple enough."
        aj "We need to thread these rods through the, um, tenty bits."
        s3_mc "The holes?"
        aj "Yeah, tenty bits."

    # CHOICE
    menu:
        thought "We need to thread the poles through the tenty bits..."
        "Do as the instructions say":
            $ s3e4p2_good_tent = True
            "You pick up one of the rods and assemble it, then carefully slide it through one of the tent holes."
            if s3_mc.current_partner == "Bill":
                bill "Nice one. You've done this before."
                "[s3_mc.current_partner] does the same."
                bill "People get themselves in a right mess putting up a tent. I've never understood why. It's pretty straightforward."
            elif s3_mc.current_partner == "Camilo":
                camilo "Wow, you really seem to know what you're doing, babe."
                "He stands and watches you."
                camilo "Keep at it!"
            elif s3_mc.current_partner == "Harry":
                harry "Wow, you really seem to know what you're doing, babe."
                "He stands and watches you."
                harry "Keep at it!"
            elif s3_mc.current_partner == "AJ":
                aj "Nice one. You've done this before."
                "[s3_mc.current_partner] does the same."
                aj "People get themselves in a right mess putting up a tent. I've never understood why. It's pretty straightforward."
        "Do a sexy dance with the pole":
            "You wedge one of the poles into the ground and start to twirl around it, kicking a leg up and arching your back down."
            if s3_mc.current_partner == "Bill":
                bill "This isn't distracting or anything..."
                "As you pull yourself back up, you lean too heavily on the pole. It snaps in half."
                bill "Nice one, babe!"
            elif s3_mc.current_partner == "Camilo":
                camilo "This isn't distracting or anything..."
                "As you pull yourself back up, you lean too heavily on the pole. It snaps in half."
                camilo "Nice one, babe!"
            elif s3_mc.current_partner == "Harry":
                harry "This isn't distracting or anything..."
                "As you pull yourself back up, you lean too heavily on the pole. It snaps in half."
                harry "Nice one, babe!"
            elif s3_mc.current_partner == "AJ":
                aj "This isn't distracting or anything..."
                "As you pull yourself back up, you lean too heavily on the pole. It snaps in half."
                aj "Nice one, babe!"
            s3_mc "Whoops..."
            thought "Maybe not the best idea."
            thought "But who cares? I had fun."
            if s3_mc.current_partner == "Bill":
                bill "Alright, step aside."
            elif s3_mc.current_partner == "Camilo":
                camilo "Alright, step aside."
            elif s3_mc.current_partner == "Harry":
                harry "Alright, step aside."
            elif s3_mc.current_partner == "AJ":
                aj "Alright, step aside."
        "Cocoon yourself in the nylon":
            "You toss your rod aside and scoop up the nylon tent."
            if s3_mc.current_partner == "Bill":
                bill "What are you...?"
                "Before [s3_mc.current_partner] can say anymore, you wrap yourself in the material until only your face is poking out."
                bill "Oh."
                bill "Anyway, you've had your fun..."
                bill "Can I have the tent back?"
                bill "We need to actually put it up."
                s3_mc "But I'm a tent burrito!"
                bill "Aw, you're very cute, but come on. Unwrap yourself."
                "Pouting, you slip out of the fabric."
                bill "We're getting nowhere with this..."
            elif s3_mc.current_partner == "Camilo":
                camilo "What are you...?"
                "Before [s3_mc.current_partner] can say anymore, you wrap yourself in the material until only your face is poking out."
                camilo "Oh."
                camilo "Why doesn't everyone use tents like that?"
                camilo "Stops us having to put them up at least!"
                "He looks around at the others."
                camilo "Although..."
                camilo "We need to actually put it up."
                s3_mc "But I'm a tent burrito!"
                camilo "Aw, you're very cute, but come on. Unwrap yourself."
                "Pouting, you slip out of the fabric."
                camilo "We're getting nowhere with this..."
            elif s3_mc.current_partner == "Harry":
                harry "What are you...?"
                "Before [s3_mc.current_partner] can say anymore, you wrap yourself in the material until only your face is poking out."
                harry "Oh."
                harry "Why doesn't everyone use tents like that?"
                harry "Stops us having to put them up at least!"
                "He looks around at the others."
                harry "Although..."
                harry "We need to actually put it up."
                s3_mc "But I'm a tent burrito!"
                harry "Aw, you're very cute, but come on. Unwrap yourself."
                "Pouting, you slip out of the fabric."
                harry "We're getting nowhere with this..."
            elif s3_mc.current_partner == "AJ":
                aj "What are you...?"
                "Before [s3_mc.current_partner] can say anymore, you wrap yourself in the material until only your face is poking out."
                aj "Oh."
                aj "Anyway, you've had your fun..."
                aj "Can I have the tent back?"
                aj "We need to actually put it up."
                s3_mc "But I'm a tent burrito!"
                aj "Aw, you're very cute, but come on. Unwrap yourself."
                "Pouting, you slip out of the fabric."
                aj "We're getting nowhere with this..."

    if s3_mc.current_partner != "AJ":
        "[s3_mc.current_partner] picks up another pole, but struggles to put it together."

        if s3_mc.current_partner == "Bill":
            bill "My rod's so stiff."
        elif s3_mc.current_partner == "Camilo":
            camilo "My rod's so stiff."
        elif s3_mc.current_partner == "Harry":
            harry "My rod's so stiff."

        # CHOICE
        menu:
            thought "[s3_mc.current_partner] just said his rod is stiff..."
            "Roll your eyes":
                # NEED TO FILL
                "EMPTY - Route: Coupled with any of the available boys."
            "That better be true later":
                if s3_mc.current_partner == "Bill":
                    bill "Oh, don't you worry."
                elif s3_mc.current_partner == "Camilo":
                    camilo "Oh, don't you worry."
                elif s3_mc.current_partner == "Harry":
                    harry "Oh, don't you worry."
            "Give it a good tug":
                if s3_mc.current_partner == "Bill":
                    bill "I'm tugging as hard as I can!"
                    bill "It's not been oiled well enough."
                elif s3_mc.current_partner == "Camilo":
                    camilo "I'm tugging as hard as I can!"
                    camilo "It's not been oiled well enough."
                elif s3_mc.current_partner == "Harry":
                    harry "I'm tugging as hard as I can!"
                    harry "It's not been oiled well enough."
            "Need a hand?":
                if s3_mc.current_partner == "Bill":
                    bill "Yeah. You pull that end while I tug on this one."
                    bill "You should feel when it's about to give..."
                elif s3_mc.current_partner == "Camilo":
                    camilo "Yeah. You pull that end while I tug on this one."
                    camilo "You should feel when it's about to give..."
                elif s3_mc.current_partner == "Harry":
                    harry "Yeah. You pull that end while I tug on this one."
                    harry "You should feel when it's about to give..."

        "Eventually the pole loosens and he threads it into place."
    else:
        "AJ goes to thread the last rod through its eyelet, but keeps losing track of where it is."
        aj "I can't find the hole!"

        # CHOICE
        menu:
            thought "AJ says she can't find the hole..."
            "Roll your eyes":
                # NEED TO FILL
                "EMPTY - Route: Coupled with AJ"
            "That's what she said":
                aj "Who? Has someone else figured out how to do it?"
                "She looks round at the other Islanders."
                s3_mc "Not quite what I meant."
                aj "Oh! I see."
                aj "Good one."
            "Explore it with your fingertips":
                aj "How will that help? I've already..."
                aj "...Oh!"
                aj "Those kind of jokes always go over my head."

        "Eventually, she manages to find the eyelet and slips the rod through it."

    "You look around at the others."
    if s3e4p2_good_tent:
        if s3_mc.current_partner == "Bill" or s3_mc.current_partner == "AJ":
            "You and [s3_mc.current_partner] seem to be smashing it. The others are nowhere near finished."
            thought "We've got this in the bag."
        elif s3_mc.current_partner == "Camilo" or s3_mc.current_partner == "Harry":
            "You and [s3_mc.current_partner]'s is the most complete, with Elladine and Nicky close behind."
            thought "Ours can still be better."
    else:
        "You and [s3_mc.current_partner] are lagging behind the others, who all have their tents up and in pretty good shape."
        "Except Iona's."
        "Iona kneels on the lawn, swaddled in a mass of rope."
        if s3_mc.current_partner != "Camilo":
            camilo "Um, babe, are you OK?"
            "You look over to see Iona's hands tied together in the rope."
            iona "I don't know how this has happened. This stuff's so fiddly."
            "Camilo looks over at her and rolls his eyes, then looks back to the instructions."
            iona "Camilo, babe, as much as I want to be tied up with you, could you maybe help me out."
            camilo "Oh! Sorry. You just seemed like you had it in hand, you know?"
            iona "I do have it! Putting up tents isn't difficult. I've just gotten tangled up somehow."
        else:
            iona "Wait! I've done this the wrong way round..."
            iona "...I think?"
            iona "Or maybe it's fine? I can't tell! How are these instructions so impossible to follow?"
            iona "I rig pylons!"

    "Elladine's voice rings out across the lawn."
    elladine "Nicky, come and hold this corner while I set the pegs."
    nicky "Why?"
    elladine "I don't want the wind to take the tent away. Come quickly!"
    nicky "There's no wind, though?"
    "Just a large gust starts to lift their tent."
    elladine "Quick, hurry!"

    $ leaving("elladine")
    $ leaving("nicky")

    # CHOICE
    menu:
        thought "Next we need to hammer the pegs in..."
        "Hulk out and smash them!":
            s3_mc "[s3_name] smash!"
            "You raise the rubber mallet high in the air before bringing it crashing down onto one of the pegs."
            "It goes straight into the ground without any resistance."
            if s3_mc.current_partner == "Bill":
                bill "Woah..."
            elif s3_mc.current_partner == "Camilo":
                camilo "Woah..."
            elif s3_mc.current_partner == "Harry":
                harry "Woah..."
            elif s3_mc.current_partner == "AJ":
                aj "Woah..."
            "You continue your rampage, you start to hit the ground, or sometimes the tent, and a few pegs are bent under the force."
            if s3_mc.current_partner == "Bill":
                bill "Um, how about I do the rest?"
                s3_mc "No, I've got this!"
                "You don't have this."
                "One of the pegs gives way, and the tent sags sideways."
                s3_mc "Whoops..."
                bill "It's all good, babe. It's kind of like, art now, or something."
            elif s3_mc.current_partner == "Camilo":
                camilo "[s3_mc.current_partner] smash, too!"
                "He joins you in smashing down the pegs. Some bend, but enough seem to survive."
            elif s3_mc.current_partner == "Harry":
                harry "[s3_mc.current_partner] smash, too!"
                "He joins you in smashing down the pegs. Some bend, but enough seem to survive."
            elif s3_mc.current_partner == "AJ":
                aj "Um, how about I do the rest?"
                s3_mc "No, I've got this!"
                "You don't have this."
                "One of the pegs gives way, and the tent sags sideways."
                s3_mc "Whoops..."
                aj "It's all good, babe. It's kind of like, art now, or something."
        "Ask [s3_mc.current_partner] to do it":
            s3_mc "Ugh, babe, this is hard."
            s3_mc "Could, you, like, to the rest?"
            if s3_mc.current_partner == "Bill":
                bill "I..."
            elif s3_mc.current_partner == "Camilo":
                camilo "I..."
            elif s3_mc.current_partner == "Harry":
                harry "I..."
            elif s3_mc.current_partner == "AJ":
                aj "I..."
            s3_mc "Pleeease..."
            if s3_mc.current_partner == "Bill":
                bill "Why can't you do it? "
                s3_mc "My fingers ache."
                s3_mc "It's an actual thing."
                bill "I'll do it for now, but I'm not going to be a pushover for you all the time."
                "[he_she!c] goes around the tent and has it pegged down in no time."
            elif s3_mc.current_partner == "Camilo":
                camilo "And you can't help because...?"
                s3_mc "I just want to watch you use those big muscles of yours."
                camilo "...Fair."
                "He uses his big muscles a bit too effectively. By the time he's done, most of the tent pegs are bent."
                camilo "Oops..."
            elif s3_mc.current_partner == "Harry":
                harry "And you can't help because...?"
                s3_mc "I just want to watch you use those big muscles of yours."
                harry "...Fair."
                "He uses his big muscles a bit too effectively. By the time he's done, most of the tent pegs are bent."
                harry "Oops..."
            elif s3_mc.current_partner == "AJ":
                aj "Why can't you do it? "
                s3_mc "My fingers ache."
                s3_mc "It's an actual thing."
                aj "I'll do it for now, but I'm not going to be a pushover for you all the time."
                "[he_she!c] goes around the tent and has it pegged down in no time."
        "Say something dirty...":
            $ s3e4p2_say_dirty = True
            s3_mc "This tent won't be the only thing getting nailed if I'm lucky..."
            "[s3_mc.current_partner] looks at you confused."
            if s3_mc.current_partner == "Bill":
                bill "I don't get it?"
            elif s3_mc.current_partner == "Camilo":
                camilo "I don't get it?"
            elif s3_mc.current_partner == "Harry":
                harry "I don't get it?"
            elif s3_mc.current_partner == "AJ":
                aj "I don't get it?"
            s3_mc "Oh, don't worry..."
            s3_mc "...you will."

    scene s3-lawn-tents-day with dissolve
    $ new_scene()

    # CHOICE
    menu:
        thought "Right, the pegs are in. Me and [s3_mc.current_partner] put up a tent together!"
        "Pretend to give [him_her] the keys to your first home":
            $ s3_mc.like(s3_mc.current_partner)
            $ s3e4p2_give_rock = True
            s3_mc "Hey, babe..."
            if s3_mc.current_partner == "Bill":
                bill "Yeah?"
            elif s3_mc.current_partner == "Camilo":
                camilo "Yeah?"
            elif s3_mc.current_partner == "Harry":
                harry "Yeah?"
            elif s3_mc.current_partner == "AJ":
                aj "Yeah?"
            "You pick up a small pebble and walk up to [s3_mc.current_partner]."
            s3_mc "Hold out your hand and close your eyes."
            if s3_mc.current_partner == "Bill":
                bill "OK..."
                "[he_she] does what you say. You drop the pebble into [his_her] outstretched palm."
                "[s3_mc.current_partner] frowns and opens their eyes."
                bill "What's this?"
            elif s3_mc.current_partner == "Camilo":
                camilo "OK..."
                "[he_she] does what you say. You drop the pebble into [his_her] outstretched palm."
                "[s3_mc.current_partner] frowns and opens their eyes."
                camilo "What's this?"
            elif s3_mc.current_partner == "Harry":
                harry "OK..."
                "[he_she] does what you say. You drop the pebble into [his_her] outstretched palm."
                "[s3_mc.current_partner] frowns and opens their eyes."
                harry "What's this?"
            elif s3_mc.current_partner == "AJ":
                aj "OK..."
                "[he_she] does what you say. You drop the pebble into [his_her] outstretched palm."
                "[s3_mc.current_partner] frowns and opens their eyes."
                aj "What's this?"
            s3_mc "The keys to our first home..."
            if s3_mc.current_partner == "Bill":
                "Bill looks at the tent."
                bill "Oh, man. We really fluffed it on that mortgage deal, eh?"
                "He turns to you."
                bill "Still, any place with you would be a cracking home..."
            elif s3_mc.current_partner == "Camilo":
                camilo "Woah, you're saying I'm a homeowner already?"
                camilo "It's a bit small to fit my family in as well, though..."
                s3_mc "Huh?"
                camilo "Relax, I'm just joshing you."
            elif s3_mc.current_partner == "Harry":
                harry "Though I always thought my first home would be a little bigger, you know?"
                harry "I guess it at least has a pool."
                harry "But no garage for my sports car."
            elif s3_mc.current_partner == "AJ":
                aj "But it's a tent?"
                s3_mc "It's symbolism, babe!"
                aj "Oooh!"
                aj "That's so sweet!"
        "Tell [him_her] to take his shoes off inside":
            s3_mc "Hey, babe..."
            if s3_mc.current_partner == "Bill":
                bill "Yeah?"
                s3_mc "Don't forget to remove your shoes before you go into the tent."
                "[s3_mc.current_partner] looks down at [his_her] feet."
                bill "I'm not wearing any?"
                s3_mc "Ah, but you might be later, and then you'd get dirt all over our nice tent."
                if s3e4p2_good_tent:
                    bill "I guess we did make it look pretty great..."
                else:
                    bill "Um, have you seen our tent?"
                s3_mc "It's just a pet peeve of mine, OK. I like shoes off in a house."
                bill "It's a tent, but, I guess..."
                bill "...OK."
            elif s3_mc.current_partner == "Camilo":
                camilo "Yeah?"
                s3_mc "Don't forget to remove your shoes before you go into the tent."
                "[s3_mc.current_partner] looks down at [his_her] feet."
                camilo "I'm not wearing any?"
                s3_mc "Ah, but you might be later, and then you'd get dirt all over our nice tent."
                if s3e4p2_good_tent:
                    camilo "I guess we did make it look pretty great..."
                else:
                    camilo "Um, have you seen our tent?"
                s3_mc "It's just a pet peeve of mine, OK. I like shoes off in a house."
                camilo "It's a tent, but, I guess..."
                camilo "...OK."
            elif s3_mc.current_partner == "Harry":
                harry "Yeah?"
                s3_mc "Don't forget to remove your shoes before you go into the tent."
                "[s3_mc.current_partner] looks down at [his_her] feet."
                harry "I'm not wearing any?"
                s3_mc "Ah, but you might be later, and then you'd get dirt all over our nice tent."
                if s3e4p2_good_tent:
                    harry "I guess we did make it look pretty great..."
                else:
                    harry "Um, have you seen our tent?"
                s3_mc "It's just a pet peeve of mine, OK. I like shoes off in a house."
                harry "It's a tent, but, I guess..."
                harry "...OK."
            elif s3_mc.current_partner == "AJ":
                aj "Yeah?"
                s3_mc "Don't forget to remove your shoes before you go into the tent."
                "[s3_mc.current_partner] looks down at [his_her] feet."
                aj "I'm not wearing any?"
                s3_mc "Ah, but you might be later, and then you'd get dirt all over our nice tent."
                if s3e4p2_good_tent:
                    aj "I guess we did make it look pretty great..."
                else:
                    aj "Um, have you seen our tent?"
                s3_mc "It's just a pet peeve of mine, OK. I like shoes off in a house."
                aj "It's a tent, but, I guess..."
                aj "...OK."
        "Whisper in [his_her] ear the naughty things you want to do in it":
            $ s3_mc.like(s3_mc.current_partner)
            s3_mc "Hey, babe..."
            if s3_mc.current_partner == "Bill":
                bill "Yeah?"
            elif s3_mc.current_partner == "Camilo":
                camilo "Yeah?"
            elif s3_mc.current_partner == "Harry":
                harry "Yeah?"
            elif s3_mc.current_partner == "AJ":
                aj "Yeah?"
            s3_mc "Come over here for a second..."
            "[s3_mc.current_partner] walks over. You lean close to [his_her] ear."

            # SUB-CHOICE
            menu:
                s3_mc "When we get into this tent..."
                "I'm going to nibble every inch of you":
                    $ s3_mc.like(s3_mc.current_partner)
                    if s3_mc.current_partner == "Bill":
                        "[s3_mc.current_partner]'s cheeks flush red."
                        bill "That's a lot of me..."
                        bill "Where would you even start?"
                    elif s3_mc.current_partner == "Camilo":
                        "[s3_mc.current_partner] bites [his_her] lip and grins at you."
                        camilo "Every inch, eh? Where would you start?"
                        s3_mc "Wherever you'd want me to..."
                    elif s3_mc.current_partner == "Harry":
                        "[s3_mc.current_partner]'s cheeks flush red."
                        harry "That's a lot of me..."
                        harry "Where would you even start?"
                    elif s3_mc.current_partner == "AJ":
                        "[s3_mc.current_partner] bites [his_her] lip and grins at you."
                        aj "Every inch, eh? Where would you start?"
                        s3_mc "Wherever you'd want me to..."
                "I want you to tie me up with the rope":
                    $ s3_mc.like(s3_mc.current_partner)
                    if s3_mc.current_partner == "Bill":
                        "[s3_mc.current_partner] swallows hard."
                        bill "Oh...? I mean, we have some rope going spare."
                        bill "I just better remember some decent knots."
                    elif s3_mc.current_partner == "Camilo":
                        "A sly grin spreads across [s3_mc.current_partner]'s face."
                        camilo "Oh yeah? I think we have some rope going spare..."
                        camilo "I just better remember some decent knots."
                    elif s3_mc.current_partner == "Harry":
                        "[s3_mc.current_partner] swallows hard."
                        harry "Oh...? I mean, we have some rope going spare."
                        harry "I just better remember some decent knots."
                    elif s3_mc.current_partner == "AJ":
                        "A sly grin spreads across [s3_mc.current_partner]'s face."
                        aj "Oh yeah? I think we have some rope going spare..."
                        aj "I just better remember some decent knots."
                "We're going to get down to some serious canoodling...":
                    if s3_mc.current_partner == "Bill":
                        bill "Canoodling? What does that mean?"
                        bill "I mean, I'm not saying no or anything..."
                        s3_mc "Like, kissing and stuff."
                        bill "Oh, OK!"
                    elif s3_mc.current_partner == "Camilo":
                        # NEED TO FILL
                        "EMPTY - Route: Coupled up with Camilo or AJ"
                    elif s3_mc.current_partner == "Harry":
                        harry "Canoodling? What does that mean?"
                        harry "I mean, I'm not saying no or anything..."
                        s3_mc "Like, kissing and stuff."
                        harry "Oh, OK!"
                    elif s3_mc.current_partner == "AJ":
                        # NEED TO FILL
                        "EMPTY - Route: Coupled up with Camilo or AJ"

    "While the others are still finishing up around you, you stand back and look at your tent."

    if s3e4p2_good_tent:
        s3_mc "Our tent looks amazing!"
        if s3_mc.current_partner == "Bill":
            bill "Yeah, babe. We smashed it."
        elif s3_mc.current_partner == "Camilo":
            camilo "Yeah, babe. We smashed it."
        elif s3_mc.current_partner == "Harry":
            harry "Yeah, babe. We smashed it."
        elif s3_mc.current_partner == "AJ":
            aj "Yeah, babe. We smashed it."
        thought "Hmm, it could be even better..."
        thought "I could go make it super sexy! We'd definitely win the challenge then, and [s3_mc.current_partner] would love it..."
    else:
        s3_mc "Our tent looks really sad."
        if s3_mc.current_partner == "Bill":
            bill "Yeah, we did a rubbish job of it..."
        elif s3_mc.current_partner == "Camilo":
            camilo "Yeah, we did a rubbish job of it..."
        elif s3_mc.current_partner == "Harry":
            harry "Yeah, we did a rubbish job of it..."
        elif s3_mc.current_partner == "AJ":
            aj "Yeah, we did a rubbish job of it..."
        thought "I think I can fix this. If I grab stuff from around the Villa, I can make the tent look amazing!"
        thought "[s3_mc.current_partner] would love it."
    
    # CHOICE
    menu:
        thought "Should I go all out to make this tent look great?"
        "Yeah, make the tent look banging":
            $ s3e4p2_decorate_tent = True
            jump s3e4p2_decorate_tent
        "Nah, it's fine as is...":
            pass

    "All around you, the other Islanders rush about, putting their final touches to their tents."
    "[s3_mc.current_partner] whistles at the tent."
    if s3e4p2_good_tent:
        if s3_mc.current_partner == "Bill":
            bill "Our tent is amazing, babe."
        elif s3_mc.current_partner == "Camilo":
            camilo "Our tent is amazing, babe."
        elif s3_mc.current_partner == "Harry":
            harry "Our tent is amazing, babe."
        elif s3_mc.current_partner == "AJ":
            aj "Our tent is amazing, babe."
    else:
        if s3_mc.current_partner == "Bill":
            bill "I'm not gonna lie. I'm worried about this tent falling down during the night."
        elif s3_mc.current_partner == "Camilo":
            camilo "I'm not gonna lie. I'm worried about this tent falling down during the night."
        elif s3_mc.current_partner == "Harry":
            harry "I'm not gonna lie. I'm worried about this tent falling down during the night."
        elif s3_mc.current_partner == "AJ":
            aj "I'm not gonna lie. I'm worried about this tent falling down during the night."

    "A loud, metallic snap followed by a crash makes the two of you turn around."
    iona "Dammit! How'd that pole snap?"
    genevieve "Do you need help, hun?"
    iona "No!"

    if s3_mc.current_partner != "Camilo":
        camilo "Um, I think we do..."
        
    iona "But..."
    iona "I can riga  pylon! I don't need help with this!"
    nicky "You sure?"
    iona "...Fine. Help, please."
    "The others go over and hold up her tent while she sets about taping together the pole."

    jump s3e4p2_ending
    return

label s3e4p2_decorate_tent:
    s3_mc "I've got an idea!"
    aj "Huh?"
    s3_mc "Just close your eyes, I'm going to do something fun."

    if s3e4p2_give_rock:
        if s3_mc.current_partner == "Bill":
            bill "Again?"
            bill "You're not going to drop more rocks into my hand are you?"
            s3_mc "Just close them and don't open them until I say so! "
            bill "OK..."
        elif s3_mc.current_partner == "Camilo":
            camilo "Again?"
            camilo "You're not going to drop more rocks into my hand are you?"
            s3_mc "Just close them and don't open them until I say so! "
            camilo "OK..."
        elif s3_mc.current_partner == "Harry":
            harry "Again?"
            harry "You're not going to drop more rocks into my hand are you?"
            s3_mc "Just close them and don't open them until I say so! "
            harry "OK..."
        elif s3_mc.current_partner == "AJ":
            aj "Again?"
            aj "You're not going to drop more rocks into my hand are you?"
            s3_mc "Just close them and don't open them until I say so! "
            aj "OK..."

    "[he_she] closes [his_her] eyes."
    "You crawl inside the tent."

    if s3e4p2_good_tent:
        thought "Hmm, it definitely looks better on the outside than on the inside..."
    else:
        thought "As bad on the inside as it is on the outside..."

    thought "Time to fix that!"
    thought "I think the lounge has a plush rug and some fluffy cushions..."
    "You make your way there."

    scene s3-kitchen-day with dissolve
    $ new_scene()

    "On your way, you spot some fairy lights hanging from the kitchen ceiling."
    thought "They'd give the tent some nice mood lighting..."
    "You start to take down the fairy lights when you hear a voice behind you."

    if s3_mc.bff == "Elladine":
        elladine "Um, [s3_name]...what are you doing?"
    elif s3_mc.bff == "Genevieve":
        genevieve "Um, [s3_name]...what are you doing?"
    elif s3_mc.bff == "Nicky":
        nicky "Um, [s3_name]...what are you doing?"
    elif s3_mc.bff == "Seb":
        seb "Um, [s3_name]...what are you doing?"
    
    # CHOICE
    menu:
        s3_mc "Oh...this?"
        "I need them for sex!":
            # NEED TO FILL
            "EMPTY"
        "I'm making our tent look lush":
            $ s3_mc.like(s3_mc.bff)
            s3_mc "I want to make it look super cosy for [s3_mc.current_partner]."
            if s3_mc.bff == "Elladine":
                elladine "'Cosy', eh?"
            elif s3_mc.bff == "Genevieve":
                genevieve "'Cosy', eh?"
            elif s3_mc.bff == "Nicky":
                nicky "'Cosy', eh?"
            elif s3_mc.bff == "Seb":
                seb "'Cosy', eh?"
        "It isn't what it looks like":
            if s3_mc.bff == "Elladine":
                elladine "Oh really? Because it looks like you're taking a string of fairy lights."
                s3_mc "Hmm... I guess it's exactly how it looks, then."
                s3_mc "I want to use them to make my tent cosier..."
                elladine "'Cosy', eh?"
            elif s3_mc.bff == "Genevieve":
                genevieve "Oh really? Because it looks like you're taking a string of fairy lights."
                s3_mc "Hmm... I guess it's exactly how it looks, then."
                s3_mc "I want to use them to make my tent cosier..."
                genevieve "'Cosy', eh?"
            elif s3_mc.bff == "Nicky":
                nicky "Oh really? Because it looks like you're taking a string of fairy lights."
                s3_mc "Hmm... I guess it's exactly how it looks, then."
                s3_mc "I want to use them to make my tent cosier..."
                nicky "'Cosy', eh?"
            elif s3_mc.bff == "Seb":
                seb "Oh really? Because it looks like you're taking a string of fairy lights."
                s3_mc "Hmm... I guess it's exactly how it looks, then."
                s3_mc "I want to use them to make my tent cosier..."
                seb "'Cosy', eh?"

    if s3_mc.bff == "Elladine":
        elladine "So to achieve the best mood lightning, I suggest you zig-zag these across the top of the tent."
        elladine "Set up mirrors around it, too. That way, they'll catch the light and be a good stand in for candles."
        s3_mc "How do you know this?"
        elladine "I'm an artist, hun. I have an eye for aesthetics, yeah?"
        elladine "And do you not think I know how to get some sexy mood light going?"
    elif s3_mc.bff == "Genevieve":
        genevieve "Oh! You could drape some colourful sheets around them. It'll dim the light and make the tent a funky colour."
        genevieve "I've seen people at festivals do all kinds of fun stuff to decorate their tents."
        genevieve "Do you think we can find a smoke machine lying around here at all?"
        s3_mc "No?"
        genevieve "Shame...what about a bubble one?"
    elif s3_mc.bff == "Nicky":
        nicky "Say no more. I'm all up for helping you score."
        s3_mc "Nicky!"
        nicky "What?"
        s3_mc "You're just so blunt."
        nicky "Only way to be."
    elif s3_mc.bff == "Seb":
        seb "This is weird."
        s3_mc "..."
        seb "But I like weird, so let me help."

    scene s3-lounge with dissolve

    $ pronouns(s3_mc.bff)
    "You and [s3_mc.bff] take down the fairy lights. [he_she!c] then helps you lug some fluffy pillows and the plush rug from the lounge to your tent."

    scene s3-lawn-tents-day with dissolve
    $ new_scene()

    $ pronouns(s3_mc.current_partner)
    "You pass [s3_mc.current_partner] who still has [his_her] eyes closed."

    if s3_mc.current_partner == "Bill":
        bill "Is that you, babe? Can I open my eyes yet?"
        s3_mc "No! It's still a surprise."
        bill "Aww..."
        show bill at npc_exit
        pause .3
        $ renpy.hide(s3_mc.current_partner.lower())
        $ on_screen.remove(s3_mc.current_partner.lower())
    elif s3_mc.current_partner == "Camilo":
        camilo "Is that you, babe? Can I open my eyes yet?"
        s3_mc "No! It's still a surprise."
        camilo "Aww..."
        show camilo at npc_exit
        pause .3
        $ renpy.hide(s3_mc.current_partner.lower())
        $ on_screen.remove(s3_mc.current_partner.lower())
    elif s3_mc.current_partner == "Harry":
        harry "Is that you, babe? Can I open my eyes yet?"
        s3_mc "No! It's still a surprise."
        harry "Aww..."
        show harry at npc_exit
        pause .3
        $ renpy.hide(s3_mc.current_partner.lower())
        $ on_screen.remove(s3_mc.current_partner.lower())
    elif s3_mc.current_partner == "AJ":
        aj "Is that you, babe? Can I open my eyes yet?"
        s3_mc "No! It's still a surprise."
        aj "Aww..."
        show aj at npc_exit
        pause .3
        $ renpy.hide(s3_mc.current_partner.lower())
        $ on_screen.remove(s3_mc.current_partner.lower())
        
    "Before you know it, you have the nicest tent out of everyone."

    if s3_mc.bff == "Elladine":
        elladine "Woah, now I'm jealous. Can we all just cram in here?"
        s3_mc "Nope!"
        elladine "Hmph, fair."
        "[s3_mc.bff] looks out of the tent towards [s3_mc.current_partner], who's still standing there with closed eyes."
        elladine "Well, looks like it's time for me to leave."
        elladine "You two have some... cosiness to get up to."
        "[s3_mc.bff] winks at you before slipping out of the tent."
        show elladine at npc_exit
        pause .3
        $ renpy.hide(s3_mc.bff.lower())
        $ on_screen.remove(s3_mc.bff.lower())
    elif s3_mc.bff == "Genevieve":
        genevieve "Woah, now I'm jealous. Can we all just cram in here?"
        s3_mc "Nope!"
        genevieve "Hmph, fair."
        "[s3_mc.bff] looks out of the tent towards [s3_mc.current_partner], who's still standing there with closed eyes."
        genevieve "Well, looks like it's time for me to leave."
        genevieve "You two have some... cosiness to get up to."
        "[s3_mc.bff] winks at you before slipping out of the tent."
        show genevieve at npc_exit
        pause .3
        $ renpy.hide(s3_mc.bff.lower())
        $ on_screen.remove(s3_mc.bff.lower())
    elif s3_mc.bff == "Nicky":
        nicky "Woah, now I'm jealous. Can we all just cram in here?"
        s3_mc "Nope!"
        nicky "Hmph, fair."
        "[s3_mc.bff] looks out of the tent towards [s3_mc.current_partner], who's still standing there with closed eyes."
        nicky "Well, looks like it's time for me to leave."
        nicky "You two have some... cosiness to get up to."
        "[s3_mc.bff] winks at you before slipping out of the tent."
        show nicky at npc_exit
        pause .3
        $ renpy.hide(s3_mc.bff.lower())
        $ on_screen.remove(s3_mc.bff.lower())
    elif s3_mc.bff == "Seb":
        seb "Woah, now I'm jealous. Can we all just cram in here?"
        s3_mc "Nope!"
        seb "Hmph, fair."
        "[s3_mc.bff] looks out of the tent towards [s3_mc.current_partner], who's still standing there with closed eyes."
        seb "Well, looks like it's time for me to leave."
        seb "You two have some... cosiness to get up to."
        "[s3_mc.bff] winks at you before slipping out of the tent."
        show seb at npc_exit
        pause .3
        $ renpy.hide(s3_mc.bff.lower())
        $ on_screen.remove(s3_mc.bff.lower())

    s3_mc "Babe! You can come in now."
    "Still covering [his_her] eyes, [s3_mc.current_partner] finds his way into the tent."
    "[he_she!c] kneels in front of the door."
    s3_mc "Alright, open your eyes."

    scene s3-inside-tent-premium-day with dissolve

    "[his_her!c] jaw drops as [he_she] removes [his_her] hand and looks around the tent."

    if s3_mc.current_partner == "Bill":
        bill "What happened to the tent, babe?"
    elif s3_mc.current_partner == "Camilo":
        camilo "What happened to the tent, babe?"
    elif s3_mc.current_partner == "Harry":
        harry "What happened to the tent, babe?"
    elif s3_mc.current_partner == "AJ":
        aj "What happened to the tent, babe?"

    # CHOICE
    menu:
        s3_mc "Oh, the tent?"
        "I thought we'd have a romantic night in":
            $ s3_mc.like(s3_mc.current_partner)
            s3_mc "And if it meant pinching a bunch of stuff from the Villa, so be it..."
            if s3_mc.current_partner == "Bill":
                bill "I didn't realise you were so sappy!"
                bill "I like it."
            elif s3_mc.current_partner == "Camilo":
                camilo "This is legit one of the most romantic things anyone's ever done for me."
                camilo "Whoever said romance is dead was so wrong."
            elif s3_mc.current_partner == "Harry":
                harry "You've made this tent suddenly feel so much posher."
                harry "The perfect place for some romance..."
            elif s3_mc.current_partner == "AJ":
                aj "I didn't think a tent could be 'sexy'."
                aj "Not that, like, the tent itself is sexy..."
                aj "As in, it creates a mood, kind of thing."
                "She sighs."
                aj "You've done a fab job, babe."
        "You hate it don't you?":
            $ s3_mc.like(s3_mc.current_partner)
            if s3_mc.current_partner == "Bill":
                bill "Hate it?"
                bill "It's mint, babe!"
            elif s3_mc.current_partner == "Camilo":
                # NEED TO FILL
                "EMPTY - Route: Coupled with Camilo"
            elif s3_mc.current_partner == "Harry":
                # NEED TO FILL
                "EMPTY - Route: Coupled with Harry"
            elif s3_mc.current_partner == "AJ":
                # NEED TO FILL
                "EMPTY - Route: Coupled with AJ"
        "Welcome to my den of sin...":
            $ s3_mc.like(s3_mc.current_partner)
            if s3_mc.current_partner == "Bill":
                bill "I'd say it's the best den I've ever been in."
                s3_mc "Have you been in many?"
                bill "This is my first. Which makes it the best by default."
                bill "But even if I'd been in many, this would still be the best."
            elif s3_mc.current_partner == "Camilo":
                # NEED TO FILL
                "EMPTY - Route: Coupled with Camilo"
            elif s3_mc.current_partner == "Harry":
                harry "I always wanted a den."
                harry "You know, like a room full of video games and an ultra-wide-screen TV and a popcorn machine."
                s3_mc "Ahem. Focus on the now?"
                harry "Oh yeah, sorry! This tent is amazing."
            elif s3_mc.current_partner == "AJ":
                aj "Agh! I wished I'd known this was going to happen."
                aj "I have this sexy devil Halloween costume back at home which would have been perfect..."

    s3_mc "I'm glad you like it."
    s3_mc "I wanted it to look good for you, babe."
    "[his_her!c] cheeks flush red. For a moment, the only sound you hear is [s3_mc.current_partner]'s gentle breathing..."

    # CHOICE
    menu:
        thought "Should I kiss [s3_mc.current_partner]?"
        "Go in for a kiss":
            "You lean past [s3_mc.current_partner] towards the entrance of the tent and slowly pull and zipper shut."
            if s3_mc.current_partner == "Bill":
                bill "Want to give us some privacy?"
            elif s3_mc.current_partner == "Camilo":
                camilo "Want to give us some privacy?"
            elif s3_mc.current_partner == "Harry":
                harry "Want to give us some privacy?"
            elif s3_mc.current_partner == "AJ":
                aj "Want to give us some privacy?"
            "You don't say anything. Instead, you make your way over to [s3_mc.current_partner] and take hold of [his_her] hand."
            "[he_she!c] moves into your embrace and your lips meet."
            "You gently bite down on [s3_mc.current_partner]'s bottom lip and feel a shudder course through [his_her] body. [he_she] pulls away."
            if s3_mc.current_partner == "Bill":
                bill "I want you..."
            elif s3_mc.current_partner == "Camilo":
                camilo "I want you..."
            elif s3_mc.current_partner == "Harry":
                harry "I want you..."
            elif s3_mc.current_partner == "AJ":
                aj "I want you..."
            s3_mc "..."
        "Give [him_her] a hug":
            "You move across to [s3_mc.current_partner] and wrap your arms around [his_her] waist."
            "[he_she!c] puts [his_her] across your shoulders. As [his_her] arms envelope you, you can feel the warmth of [his_her] body against yours."
            "You're still for a moment, just enjoying the closeness..."
            "You two stay there for a while, under the glow of the fairy lights, just enjoying each other's touch."
            if s3_mc.current_partner == "Bill":
                bill "You're an amazing hugger..."
                s3_mc "And you're so warm!"
                bill "True. I'm pretty hot..."
            elif s3_mc.current_partner == "Camilo":
                camilo "You're an amazing hugger..."
                s3_mc "And you're so warm!"
                camilo "True. I'm pretty hot..."
            elif s3_mc.current_partner == "Harry":
                harry "You're an amazing hugger..."
                s3_mc "And you're so warm!"
                harry "True. I'm pretty hot..."
            elif s3_mc.current_partner == "AJ":
                aj "You're an amazing hugger..."
                s3_mc "And you're so warm!"
                aj "True. I'm pretty hot..."
        "Enjoy the silence":
            "You let out a deep breath and just enjoy the moment for what it is."
            "The sound of gentle wind hitting the side of the tent becomes hypnotic."
            "You're almost about to nod off when..."

    "A crash outside snaps you away from the moment."
    iona "Dammit! How'd that pole snap?"
    genevieve "Do you need help, hun?"
    iona "No!"

    if s3_mc.current_partner != "Camilo":
        camilo "Um, I think we do..."
        iona "But..."

    iona "I'm normally really good at stuff like this..."
    "[s3_mc.current_partner] laughs and turns back to you."

    if s3_mc.current_partner == "Bill":
        bill "Hmm, it's a bit 'busy' outside."
        bill "Maybe later?"
    elif s3_mc.current_partner == "Camilo":
        camilo "Hmm, it's a bit 'busy' outside."
        camilo "Maybe later?"
    elif s3_mc.current_partner == "Harry":
        harry "Hmm, it's a bit 'busy' outside."
        harry "Maybe later?"
    elif s3_mc.current_partner == "AJ":
        aj "Hmm, it's a bit 'busy' outside."
        aj "Maybe later?"

    s3_mc "You'll have to wait and see..."

    scene s3-lawn-tents-day with dissolve
    $ new_scene()

    "You step out of the tent."
    "You emerge from your tent to find the others holding Iona's tent up while she tapes a snapped pole back together."

    jump s3e4p2_ending
    return

label s3e4p2_ending:
    scene s3-lawn-tents-day with dissolve
    $ new_scene()

    "While the Islanders are busy putting up Iona's tent, [s3_mc.bff] walks over to you."

    if s3_mc.bff == "Elladine":
        elladine "This challenge has been a thing, eh?"
        s3_mc "Tell me about it."
        elladine "Well, we can't really help Iona. Too many chefs and all that."
        elladine "Guess the best thing we can do is stay out of the way."
    elif s3_mc.bff == "Genevieve":
        elladine "This challenge has been a thing, eh?"
        s3_mc "Tell me about it."
        elladine "Well, we can't really help Iona. Too many chefs and all that."
        elladine "Guess the best thing we can do is stay out of the way."
    elif s3_mc.bff == "Nicky":
        nicky "This challenge has been a thing, eh?"
        s3_mc "Tell me about it."
        nicky "Well, we can't really help Iona. Too many chefs and all that."
        nicky "Guess the best thing we can do is stay out of the way."
    elif s3_mc.bff == "Seb":
        seb "This challenge has been a thing, eh?"
        s3_mc "Tell me about it."
        seb "Well, we can't really help Iona. Too many chefs and all that."
        seb "Guess the best thing we can do is stay out of the way."

    if s3_mc.bff == "Elladine":
        elladine "Hey, [s3_name], could I ask you a quick question?"
        s3_mc "Sure, hun."
        elladine "Do you think I got a bit too much into this challenge?"
        elladine "Like, was I too bossy?"

        # CHOICE
        menu:
            s3_mc "Earlier you..."
            "Were a bit, yeah...":
                # NEED TO FILL
                "EMPTY"
            "Needed to give Nicky a push!":
                # NEED TO FILL
                "EMPTY"
            "Weren't bossy at all":
                "Elladine breathes a small sigh of relief."
                elladine "That's good to hear."

        s3_mc "Why do you ask?"
        "She twiddles her thumbs."
        elladine "One of my exes once said he thought I was too bossy..."
        elladine "I'm fine speaking up for myself! I give instructions in the workshop all the time and I don't worry about it."
        elladine "But then when it comes to romance... I worry Nicky might be put off like my ex was."
        elladine "Maybe I'm being silly..."

        # CHOICE
        menu:
            thought "Elladine says that a guy didn't like her attitude..."
            "Girl, same. It's been an issue for me, too":
                # NEED TO FILL
                "EMPTY"
            "Just for saying what you think?":
                $ s3_mc.like("Elladine")
                elladine "Yeah... I mean the way I say it."
                elladine "Maybe they think I'm unkind? Or want me to change?"
                s3_mc "Woah, hold on!"
                s3_mc "If you were unkind, you wouldn't be this worried about other people, so that's not even on the table."
                s3_mc "And second, never change just so someone can like you!"
                s3_mc "You're great and any guy that's worth it will love you just the way you are."
                "Elladine thinks for a moment."
                elladine "Yeah, you're right!"
                elladine "Thanks, hun."
            "You're not bossy, you're the boss!":
                s3_mc "If people have a problem with you telling it like it is, you just need to remember..."
                s3_mc "...it's them that has the problem!"
                elladine "Well, yeah! But that's easier said than done hun."
                elladine "I will try, though. I don't want to keep driving people away over such a silly thing."
                s3_mc "It's not a silly thing. No one should make you feel you have to change your personality for them to like you!"

        elladine "Thanks for letting me vent..."
        elladine "Enough about me now, what's on your mind?"

        # CHOICE
        menu:
            s3_mc "We should talk about..."
            "The big question. Would you live on Mars?":
                # NEED TO FILL
                "EMPTY"
            "Your biggest hopes and fears":
                elladine "Go big or go home, eh, babe?"
                elladine "Well my biggest hope is to display my art in galleries all around the world."
                elladine "Installations that draw in thousands of people..."
                elladine "I guess my biggest fear is that I don't do the rigging correctly and all of those pieces fall to the ground and shatter..."
                "She lets out a nervous chuckle."
                s3_mc "Is that really it?"
                elladine "Maybe, maybe not."
                elladine "Maybe, I'll tell you properly another time..."
            "This bossy side to you some more":
                elladine "No, hun."
                elladine "Thanks for checking, but I'm good."
                s3_mc "Sure?"
                elladine "Totes sure, you've done your free bit of therapy for the day!"

        "She smiles at you."
        elladine "I really like having these chats with you, hun. It feels like I can leave the rest of the Villa behind for a couple of minutes."

        # CHOICE
        menu:
            thought "I feel..."
            "Completely indifferent to them":
                # NEED TO FILL
                "EMPTY"
            "Like we should just take the money and run":
                # NEED TO FILL
                "EMPTY"
            "The same way about our chats":
                $ s3_mc.like("Elladine")
                elladine "I'm glad to hear it!"
                elladine "They really do make me feel better."

        "She sighs."

    elif s3_mc.bff == "Genevieve":
        genevieve "OK, so..."
        genevieve "I have this thing..."
        genevieve "Like, when you're on a night out, or camping in a field, or you're at a festival..."
        genevieve "Or you're in someone's house with abnormally long corridors and no working light..."
        genevieve "Basically anywhere that, like, might have a toilet in the dark..."
        "She shudders."
        genevieve "Sorry, totally lost my train of thought there."
        genevieve "What was I on about?"
        s3_mc "The thing with toilets in the dark."
        genevieve "Oh, yeah!"
        genevieve "I always try and make sure I have at least one dedicated friend with me who I know will accompany me on the going-to-the-toilet mission."
        genevieve "I call them my Bathroom Babe."
        genevieve "I think out of everyone here, you'd definitely be my main Bathroom Babe."
        genevieve "You just seem like someone I can really count on."

        if s3_mc.current_partner == "Harry":
            "She looks down at her feet."
            genevieve "And I don't want to let something silly like boys get between us."
            genevieve "No matter who Harry ends up with, our friendship is solid."

            # CHOICE
            menu:
                s3_mc "Aw, babe..."
                "This was all so awkward":
                    # NEED TO FILL
                    "EMPTY"
                "Boys smell":
                    # NEED TO FILL
                    "EMPTY"
                "I hope you can forgive me":
                    s3_mc "I stole him from you..."
                    genevieve "Nobody stole anything, and there's nothing to forgive."
                    genevieve "That's literally how it works in here."
                    genevieve "Besides, he wouldn't stop talking about you when we were together."
                    genevieve "And who can blame him? You're amazing."

        genevieve "A true Bathroom Babe."
        genevieve "And that's with a capital 'B' because it's a very important title."

        # CHOICE
        menu:
            thought "Genevieve wants me to be her Bathroom Babe!"
            "Yeah! Let's have a bath together":
                genevieve "Noo, not bathroom bathe."
                genevieve "Bathroom Babe!"
                "She laughs."
                genevieve "Though, now I'm imaging us sat in a bath sky high full of bubbles."
                genevieve "Sipping on wine and having a good soak."
                genevieve "Damn, that would be nice."
            "This is crucial, I hate going to the bathroom alone":
                "Genevieve puts a hand on your shoulder."
                genevieve "Girl."
                genevieve "You don't ever have to worry about that again."
                genevieve "I will go with you."
            "I didn't even know there was a bathroom thing":
                genevieve "Wait, what?"
                genevieve "You haven't used the loo since we got here?"
                s3_mc "Nope!"
                genevieve "That's kinda concerning. I'd speak to a doctor about that."
                genevieve "Oh, wait. I am a doctor."
                genevieve "Well, it's a conflict of interest, because I'm your mate."
                genevieve "Though as your mate, my recommendation is for you to see a doctor about that."
                genevieve "But anyway..."

        genevieve "We'll always stick together when we go to the bathroom at night."
        genevieve "And when we're out of here, we could go to festivals, nights out, and maybe even go on camping trips together!"

    elif s3_mc.bff == "Nicky":
        nicky "Y'know I was thinking about my little sister Rachel again earlier."
        nicky "Thinking about when she was at uni and she did a runner the day before an exam."
        s3_mc "What?"
        nicky "Yeah, she'd found out her boyfriend at the time was cheating on her. And she knew she was going to fail anyway."
        nicky "So she jumped on a bus to Aberdeen to see her ex, and spent the weekend partying with him and his mates."
        nicky "Don't tell anyone.She only told me because she needed to borrow money for the bus home."
        s3_mc "And this is the sister you think I have a lot in common with?"
        nicky "Well, not that stuff, necessarily. I mean, does it sound like the kind of thing you'd do?"

        # CHOICE
        menu:
            thought "Would I drop everything to travel across the country on an impulse?"
            "I would never do that":
                s3_mc "I couldn't be that irresponsible. I don't know if I'd even want to."
                nicky "Yeah, that's probably a good thing."
            "I've totally done that":
                s3_mc "Yeah, that's classic me, to be honest."
                nicky "Ah, I had my suspicions."
            "I'd like to try it someday":
                s3_mc "It's exciting to think about."
                s3_mc "I just haven't ever made that leap before."
                nicky "Well hey, it's never too late to start being spontaneous."

        nicky "You know, I think you'd be a good influence on Rach. I know what I said on our first night here..."
        nicky "How you kind of remind me of her. Just in the way you tend to be surrounded by chaos."
        nicky "And I stand by that, but now we've been here a few days, I wanna make one small disclaimer."
        nicky "You're like Rachel, except you can actually handle the drama going on around you."
        nicky "So even when it's always kicking off, you tend to take it in your stride a lot better."
        nicky "Whereas she's still a bit of a big kid. You're like a more mature version, if that makes sense."

        # CHOICE
        menu:
            thought "Nicky says I'm more like a mature version of his sister..."
            "But I still don't feel properly grown-up":
                s3_mc "Sometimes I look around and realise... I'm an adult now? With a job?!"
                nicky "Have you hit that point yet where people you went to school with start getting married and having kids?"
                s3_mc "Ugh, yes! It's so weird!"
                s3_mc "It feels like just yesterday we were all taking our GCSEs."
                nicky "You'll get used to it."
            "Yeah, I've always been old for my age":
                s3_mc "I think I'm more emotionally mature than most other people my age."
                nicky "Definitely. Though, to be fair, that's not a high bar."
            "Please stop comparing me to your little sister":
                s3_mc "It's weird. Next you're gonna be and helping me with my maths homework."
                nicky "Alright. That was the last time, I promise."

        nicky "Besides, you'll probably be a totally different person by the time you leave here."
        nicky "With everything that's already happened, and more on the horizon, most likely."
        nicky "It could, like, open up whole new parts of yourself you didn't even know about."

        # CHOICE
        menu:
            thought "WIll Love Island change me?"
            "No, I'm already who I want to be":
                # NEED TO FILL
                "EMPTY"
            "Yeah, I'm doing some growing here":
                s3_mc "Yeah, of course. I think this could end up being a turning point in my life."
                s3_mc "Especially if I end up leaving with someone I have real feelings for."
            "Only by making me more famous!":
                s3_mc "It's me who changes the world, not the other way round."
                nicky "Good point."

        s3_mc "What about you? D'you think you're changing by being here?"
        nicky "I hope not. Why would I wanna mess with perfection?"
        s3_mc "Yeah, yeah, okay."

    elif s3_mc.bff == "Seb":
        s3_mc "Oh, hey, by the way."
        s3_mc "How do you think Doom's doing?"
        seb "I'm trying not to think about her too much."
        seb "I know she's in safe hands, but I can't help worrying about her when I do."
        seb "It's weird to think she might've had her kittens already and I wouldn't even know."

        # CHOICE
        menu:
            s3_mc "You might go home to a lot more cats than you left behind..."
            "I wouldn't be looking forward to that":
                # NEED TO FILL
                "EMPTY"
            "Are you sure you're ready to be a dad?":
                "He groans."
                seb "I don't know!"
                seb "It's scary. I really want to do right by them."

                # SUB-CHOICE
                menu:
                    s3_mc "Just remember the most important thing..."
                    "Get them into a good school":
                        pass
                    "Train them to fetch the newspaper":
                        pass
                    "Set up them up on socials":
                        pass
                seb "I will do my best."

            "You're so lucky! Could I adopt one?":
                s3_mc "I'd love to have a new kitten in my life when I leave here."
                seb "Oh, yeah, of course! That's a nice idea."
                seb "Have you had cats before?"

                # CHOICE
                menu:
                    thought "Have I had cats before?"
                    "No, but I'd do my research":
                        pass
                    "Yeah; I've got some experience":
                        pass
                    "So many that it's almost weird":
                        pass
                seb "Cool. I wanna know all Doom's kids are gonna be in safe hands."

        seb "I mean, obviously I'll have to give most of them away, once they're old enough."
        seb "But I'd like to keep one or two around the shop, y'know?"
        seb "To take over Doom's duties someday."
        s3_mc "Have you decided what you're gonna call them?"
        seb "Oh man, I haven't even thought about it."

        # CHOICE
        menu:
            s3_mc "You should name the kittens after..."
            "Your exes":
                # NEED TO FILL
                "EMPTY"
            "Islanders":
                s3_mc "Like, if one of the kittens can explain in detail why it thinks wet food is objectively better than biscuits, you can call it Bill."
                seb "Sure. And 'Harry' can be the kitten with the most relentless ambition in its eyes."
                seb "And 'Genevieve' if one of the kittens turns out to be..."
                seb "No, I can't think of a joke for Genevieve."
            "Music genres":
                s3_mc "You've already got Doom! You could call the kittens Grunge, Sludge, Thrash..."
                seb "Adorable."
                seb "I'm glad we can talk about music."
                seb "I tried to make a joke about shoegaze to AJ the other day, and she thought I was talking about gay people who are into shoes."
                seb "Viv thought it was funny, though."

        "He sighs."
        seb "Viv's just nice. Like it comes naturally to her."
        seb "I wish I knew how she does it."

        # CHOICE
        menu:
            thought "Seb thinks Genevieve is 'nice...'"
            "She's not nice to me":
                # NEED TO FILL
                "EMPTY"
            "Yeah, she's a sweetheart":
                s3_mc "The kind of person who'd wait for your bus with you in the cold type of thing."
                seb "Yeah, exactly."
            "I think you just fancy her":
                "He stares off into space for a while, chewing his lip."
                seb "You might be onto something there."
                seb "It's kinda hard to tell."

        seb "She's the kinda girl I wish I could fall for, y'know? But that wouldn't be very... me."
        s3_mc "You go for bad girls, basically."
        seb "I guess I do."
        seb "Well, hey. If I was good at choosing girlfriends, I wouldn't be here in the first place."
        s3_mc "True."

    "After Iona's tent is finally up, Elladine beams a smile at the rest of you and claps."
    elladine "These tents are amazing!"
    genevieve "It's going to be really hard to choose whose is best!"
    iona "Uh-huh..."
    nicky "Oh, here we go. I've got a text."
    text "Islanders, in your couples, please say who you think has the best tent. You cannot nominate your own. #acontentiousdecision #nothingtoopretentious"
    iona "We can't nominate ourselves?"

    if s3_mc.current_partner != "Camilo":
        camilo "There goes our plan..."
    else:
        iona "Well, there goes my plan..."

    "You look around."

    if s3_mc.current_partner == "Bill":
        bill "Who do you think has the best tent?"
    elif s3_mc.current_partner == "Camilo":
        camilo "Who do you think has the best tent?"
    elif s3_mc.current_partner == "Harry":
        harry "Who do you think has the best tent?"
    elif s3_mc.current_partner == "AJ":
        aj "Who do you think has the best tent?"

    # CHOICE
    menu:
        s3_mc "The best tent is..."
        "[s3_mc.bff]'s one":
            $ s3_mc.like(s3_mc.bff)
            s3_mc "It's clearly the best tent."
            if s3_mc.bff == "Elladine":
                elladine "I couldn't have done it without Nicky's help."
                nicky "Yeah right. You're the organised one."
            elif s3_mc.bff == "Genevieve":
                genevieve "It was tough."
                elladine "I wouldn't have thought so. You just seemed to crack on with it."
                if s3_mc.current_partner != "Harry":
                    harry "That's what Viv's so good at, though."
            elif s3_mc.bff == "Nicky":
                nicky "It literally only exists because Elladine can sort this stuff out so well."
                elladine "Oh, shush. You did loads to help."
            elif s3_mc.bff == "Seb":
                seb "It's kind of you think that."
                if s3_mc.current_partner != "AJ":
                    aj "Stop being so negative! It looks great."
        "Elladine and Nicky's one" if s3_mc.bff != 'Nicky' or s3_mc.bff != 'Elladine':
            $ s3_mc.like("Elladine")
            $ s3_mc.like("Nicky")
            elladine "Thanks, hun!"
            nicky "I'd have been stumped without Elladine, that's for sure."
            elladine "Sorry if I pushed you a bit hard..."
        "Iona and Camilo's one" if s3_mc.current_partner != 'Camilo':
            iona "Um... what?"
            "At that moment, one of the ropes holding her tent up comes loose. Half the tent collapses in on itself."
            camilo "It's kind of you to say that, but it's obvious that we don't have the best tent."
            iona "But you know what? I'll take it."
        "Iona's one" if s3_mc.current_partner == 'Camilo':
            iona "Um... what?"
            "At that moment, one of the ropes holding her tent up comes loose. Half the tent collapses in on itself."
            iona "It's kind of you to say that, babe, but you don't need to make me feel better..."
            iona "But you know what? I'll take it."
        "Our one!":
            if s3_mc.current_partner == "Bill":
                bill "We can't vote for ourselves, babe."
                s3_mc "I don't care. We have the best tent!"
                bill "You're right about that, but..."
                bill "We actually need to vote for someone."
                bill "I think Elladine and Nicky's is the best, personally."
            elif s3_mc.current_partner == "Camilo":
                camilo "We can't vote for ourselves, babe."
                s3_mc "I don't care. We have the best tent!"
                camilo "You're right about that, but..."
                camilo "We actually need to vote for someone."
                camilo "I think Elladine and Nicky's is the best, personally."
            elif s3_mc.current_partner == "Harry":
                harry "We can't vote for ourselves, babe."
                s3_mc "I don't care. We have the best tent!"
                harry "You're right about that, but..."
                harry "We actually need to vote for someone."
                harry "I think Elladine and Nicky's is the best, personally."
            elif s3_mc.current_partner == "AJ":
                aj "We can't vote for ourselves, babe."
                s3_mc "I don't care. We have the best tent!"
                aj "You're right about that, but..."
                aj "We actually need to vote for someone."
                aj "I think Elladine and Nicky's is the best, personally."

    if s3_mc.bff == "Elladine":
        elladine "I think [s3_name] and [s3_mc.current_partner]'s tent is the best! It's got charm."
    elif s3_mc.bff == "Genevieve":
        genevieve "I think [s3_name] and [s3_mc.current_partner]'s tent is the best! It's got charm."
    elif s3_mc.bff == "Nicky":
        nicky "I think [s3_name] and [s3_mc.current_partner]'s tent is the best! It's got charm."
    elif s3_mc.bff == "Seb":
        seb "I think [s3_name] and [s3_mc.current_partner]'s tent is the best! It's got charm."

    if s3_mc.bff != "Nicky" or s3_mc.bff != "Elladine":
        elladine "We agree, too."
    elif s3_mc.bff == "Nicky":
        elladine "Nicky's right."
    elif s3_mc.bff == "Elladine":
        nicky "Yeah, it's got charm."

    "The others look at your tent."

    if s3e4p2_decorate_tent == False and s3e4p2_good_tent == False:
        iona "I'm going to say Elladine and Nicky's gets my vote."
        text "Congrats Elladine and Nicky! The other Islanders have voted your tent as the best. As a reward, you'll get to pick the food for tonight's meal. #foodforthought"
        s3_mc "We didn't win..."
        if s3_mc.current_partner == "Bill":
            bill "You've seen our tent, right?"
        elif s3_mc.current_partner == "Camilo":
            camilo "You've seen our tent, right?"
        elif s3_mc.current_partner == "Harry":
            harry "You've seen our tent, right?"
        elif s3_mc.current_partner == "AJ":
            aj "You've seen our tent, right?"
        "It leans at an odd angle, amongst the rest of the Islanders' tents."
    elif s3e4p2_decorate_tent == True or s3e4p2_good_tent == True:
        iona "Yeah, [s3_name] gets my vote, too."
        miki "And mine!"

        if s3_mc.current_partner == "AJ":
            aj "Mine, too!"

        if s3_mc.current_partner == "Camilo":
            camilo "Agreed."

        if s3_mc.current_partner == "Harry":
            harry "It's definitely the nicest one here."

        if s3_mc.current_partner == "Bill":
            bill "That makes the most sense to me."

        thought "Everyone voted for our tent!"
        "Your phone pings loudly."
        text "Congrats [s3_name] and [s3_mc.current_partner]! The other Islanders have voted your tent as the best. As a reward, you'll get to pick the food for tonight's meal. #foodforthought"
        s3_mc "We won!"

        if s3_mc.current_partner == "Bill":
            bill "Of course! Our tent does look proper good."
        elif s3_mc.current_partner == "Camilo":
            camilo "Of course! Our tent does look proper good."
        elif s3_mc.current_partner == "Harry":
            harry "Of course! Our tent does look proper good."
        elif s3_mc.current_partner == "AJ":
            aj "Of course! Our tent does look proper good."

    "It stands proud amongst the rest of the Islanders' tents. Clearly the best one."
    elladine "Congrats, guys!"
    "You see Miki peek into her tent."
    miki "Hmm, they're still missing something..."
    iona "What?"
    miki "Sleeping bags and things!"

    if s3e4p2_decorate_tent:
        miki "Just like how [s3_name] did with her tent up!"

    nicky "What's the point? It's not like we'll be sleeping here tonight."
    "You pull out your phone."
    text "Islanders, tonight you will be camping out in your tents! #intense #intents"
    nicky "Oh. Well, that answers that."

    # CHOICE
    menu:
        thought "Camping outdoors?"
        "Hell yeah!":
            s3_mc "It's going to be so cosy!"
        "But what about the bugs?":
            if s3_mc.current_partner == "Bill":
                bill "Don't worry about them, babe. Just stay in my arms."
                bill "I'll keep you safe."
            elif s3_mc.current_partner == "Camilo":
                camilo "Don't worry about them, babe. Just stay in my arms."
                camilo "I'll keep you safe."
            elif s3_mc.current_partner == "Harry":
                harry "Don't worry about them, babe. Just stay in my arms."
                harry "I'll keep you safe."
            elif s3_mc.current_partner == "AJ":
                aj "Don't worry about them, babe. Just stay in my arms."
                aj "I'll keep you safe."
        "You can get up to a lot in a tent...":
            if s3_mc.current_partner == "Bill":
                harry "They're a bit cramped, if I'm honest..."
                harry "But I'm still up for this."
            elif s3_mc.current_partner == "Camilo":
                # NEED TO FILL
                "EMPTY - Route: Coupled with Camilo"
            elif s3_mc.current_partner == "Harry":
                harry "They're a bit cramped, if I'm honest..."
                harry "But I'm still up for this."
            elif s3_mc.current_partner == "AJ":
                aj "Yeah! Once me and a friend drained this guy's keg of beer at Reading."
                aj "He had no idea!"
                s3_mc "I was thinking something a little sexier..."
                aj "Oooh..."

    elladine "This is so exciting! I can't wait to camp out tonight. It's been years since I last went camping."

    # CHOICE
    menu:
        s3_mc "Camping is the..."
        "Best way to connect with nature":
            $ s3_mc.like("Miki")
            miki "Camping's one of the reasons I bought my barge."
            miki "I wouldn't want to live in a tent forever, but I knew a normal house wasn't my thing."
            seb "Sounds like a good way to have all your stuff sink to the bottom of a river..."
            miki "Why would it sink?"
            "Seb shrugs."
            seb "Pirates."
            s3_mc "In a Cambridge canal?"
            seb "Canal pirates."
        "Perfect way to ruin a good weekend":
            s3_mc "Why do people want to sleep on the ground?"
            miki "What? It's so peaceful, though!"
            seb "Nah, [s3_name]'s got the right outlook."
            seb "It's called a B&B. I'll take an actual mattress any day."
            miki "Don't you camp for festivals, though?"
            seb "Yeah, but I don't sleep much."
        "Leading cause of tent related injuries":
            bill "Well, yeah? Where else would you get tent related injuries?"
            "The others think."
            aj "In a... tent factory?"
            bill "Oh, that's true. In fact, I bet they're way more dangerous than just camping."
            s3_mc "Yeah, but how many people work in a tent factory versus how many people go camping?"
            bill "Also a good point."
            camilo "This is well hard to answer."
            iona "Then maybe we... don't?"

    elladine "I'm so lost in this conversation..."
    elladine "But I don't care. Let's grab some bedding so we can do all the camping things!"
    elladine "Shame we don't have marshmallows..."

    scene sand with dissolve
    $ on_screen = []

    "And so, with their tents erected, our Islanders are ready for tonight's big camp out."
    "Except for Iona, whose tent skills have made me scared to go near any pylon in Scotland."
    "At least [s3_name] and [s3_mc.current_partner] don't have to worry about their tent!"
    "I've never seen such a sturdy structure, and I once spent two years in Alcatraz."
    "Worst sightseeing tour of my life..."
    "Coming up!"
    "Things get spooky..."

    $ outfit = "evening"

    genevieve "Be gone, shiny demon!"
    $ leaving("genevieve")

    "And will the wind be the only thing shaking the tents?"
    
    $ outfit = "pjs"

    if s3_mc.current_partner == "Bill":
        bill "How about it then?"
    elif s3_mc.current_partner == "Camilo":
        camilo "How about it then?"
    elif s3_mc.current_partner == "Harry":
        harry "How about it then?"
    elif s3_mc.current_partner == "AJ":
        aj "How about it then?"

    jump s3e4p3
    return


#########################################################################
## Episode 4, Part 3
#########################################################################
label s3e4p3:
    scene sand with dissolve
    $ on_screen = []
    $ outfit = "swim"

    show screen day_title(4, 3) with Pause(4)
    hide screen day_title with dissolve

    $ pronouns(s3_mc.current_partner)

    "Previously, our Islanders put their construction skills to the test..."
    aj "I can't find the hole!"
    $ leaving("aj")

    "By pitching some tents in the back garden."
    elladine "Run!"
    $ leaving("elladine")

    "You can't run through a campsite, Elladine!"
    "You can only ran."
    "Why?"
    "Because it's past tents."
    "Prime time content here, folks."
    "Tonight on Love Island..."
    "The Islanders have a big camp out in their erected tents."

    if s3_mc.current_partner == "Bill":
        bill "This is the first time we get to spend the night together..."
        bill "Alone!"
    elif s3_mc.current_partner == "Camilo":
        camilo "This is the first time we get to spend the night together..."
        camilo "Alone!"
    elif s3_mc.current_partner == "Harry":
        harry "This is the first time we get to spend the night together..."
        harry "Alone!"
    elif s3_mc.current_partner == "AJ":
        aj "This is the first time we get to spend the night together..."
        aj "Alone!"
    
    "Need I say more?"

    scene s3-dressing-room with dissolve
    $ new_scene()

    $ outfit = "pjs"

    "You're in the dressing room trying to find something to wear for tonight's camp out."
    thought "What am I going to wear to sleep outside?"
    "Someone knocks at the door."

    if s3_mc.current_partner == "Bill":
        bill "[s3_name], are you up here?"
    elif s3_mc.current_partner == "Camilo":
        camilo "[s3_name], are you up here?"
    elif s3_mc.current_partner == "Harry":
        harry "[s3_name], are you up here?"
    elif s3_mc.current_partner == "AJ":
        aj "[s3_name], are you up here?"

    s3_mc "I'm in here."
    "[s3_mc.current_partner] shuffles in, closing the door behind [him_her]."
    "[he_she!c]'s holding a top in [his_her] hand."

    if s3_mc.current_partner == "Bill":
        bill "If you want, you can borrow one of my tops to sleep in tonight, like, as an extra layer."
        bill "That's like a cute coupley thing that girls like, right?"
        bill "Steal their boyfriend's clothes."
        s3_mc "Totally."
        bill "I wore this thing the first time I ever plonked a tile on a roof."
        bill "It's kinda my lucky top, I guess."
        bill "I haven't actually worn it yet here."
        bill "But I think it would look cute on you."
    elif s3_mc.current_partner == "Camilo":
        camilo "If you want, you can borrow one of my tops to sleep in tonight, like, as an extra layer."
        camilo "That's like a cute coupley thing that girls like, right?"
        camilo "Steal their boyfriend's clothes."
        s3_mc "Totally."
        camilo "Whenever I go to Jiu Jitsu, I always have this on under my gi."
        s3_mc "That's really sweet."
        s3_mc "But also totally gross."
        camilo "It's been washed!"
        camilo "It's kinda my lucky top, I guess."
        camilo "I haven't actually worn it yet here."
        camilo "But I think it would look cute on you."
    elif s3_mc.current_partner == "Harry":
        harry "If you want, you can borrow one of my tops to sleep in tonight, like, as an extra layer."
        harry "That's like a cute coupley thing that girls like, right?"
        harry "Steal their boyfriend's clothes."
        s3_mc "Totally."
        harry "I always wear this under a shirt when I go for an interview."
        harry "It's kinda my lucky top, I guess."
        harry "I haven't actually worn it yet here."
        harry "But I think it would look cute on you."
    elif s3_mc.current_partner == "AJ":
        aj "If you want, you can borrow one of my tops to sleep in tonight, like, as an extra layer."
        aj "That's like a cute coupley thing that girls like, right?"
        aj "Sharing each other's entire wardrobe is a given when you're with a girl, right?"
        aj "And guys too, to be fair."
        aj "But it's harder to share jeans and stuff."
        s3_mc "I'm gonna steal all your clothes!"  
        aj "I wear this all the time under my hockey gear."
        s3_mc "That's really sweet."
        s3_mc "But also totally gross."
        aj "It's been washed!"
        aj "It's kinda my lucky top, I guess."
        aj "I haven't actually worn it yet here."
        aj "But I think it would look cute on you."

    # CHOICE
    menu:
        thought "[s3_mc.current_partner] wants me to wear his lucky top!"
        "Yeah, I'd love to wear it":
            # add in images of li's sleep shirt
            $ s3_mc.like(s3_mc.current_partner)
            $ s3e4p3_wear_shirt = True

            "[s3_mc.current_partner] smiles and hands it to you."
            if s3_mc.current_partner == "Bill":
                bill "Sweet."
                bill "I'll let you get changed."
            elif s3_mc.current_partner == "Camilo":
                camilo "Sweet."
                camilo "I'll let you get changed."
            elif s3_mc.current_partner == "Harry":
                harry "Sweet."
                harry "I'll let you get changed."
            elif s3_mc.current_partner == "AJ":
                aj "Sweet."
                aj "I'll let you get changed."
            "[he_she!c] looks away as you slip on the top."
            if s3_mc.current_partner == "Bill":
                bill "Perfect!"
                bill "Well, it's a bit baggy..."
                bill "But I find oversized clothes so sexy on a girl."
                bill "I'm never getting that back, am I?"
                s3_mc "Nope."
                bill "Fair enough, gorgeous."
                bill "Let's go down and find the others."
            elif s3_mc.current_partner == "Camilo":
                camilo "Oh, damn."
                camilo "That looks so hot on you."
                camilo "I'm never getting that back, am I?"
                s3_mc "Nope."
                camilo "Fair enough, gorgeous."
                camilo "Let's go down and find the others."
            elif s3_mc.current_partner == "Harry":
                harry "Dang, girl."
                harry "That t-shirt suits you to a T."
                harry "I'm never getting that back, am I?"
                s3_mc "Nope."
                harry "Fair enough, gorgeous."
                harry "Let's go down and find the others."
            elif s3_mc.current_partner == "AJ":
                aj "It looks so cute on you."
                aj "Way cuter than it looks on me!"
                aj "I'm never getting that back, am I?"
                s3_mc "Nope."
                aj "Fair enough, gorgeous."
                aj "Let's go down and find the others."
        "Nah, I'm alright":
            if s3_mc.current_partner == "Bill":
                bill "Aw, are you sure?"
                s3_mc "I prefer my clothes"
                bill "Oh, okay, fair enough!"
            elif s3_mc.current_partner == "Camilo":
                camilo "Aw, are you sure?"
                s3_mc "I prefer my clothes"
                camilo "Oh, okay, fair enough!"
            elif s3_mc.current_partner == "Harry":
                harry "Aw, are you sure?"
                s3_mc "I prefer my clothes"
                harry "Oh, okay, fair enough!"
            elif s3_mc.current_partner == "AJ":
                aj "Aw, are you sure?"
                s3_mc "I prefer my clothes"
                aj "Oh, okay, fair enough!"

            # ADD back once MC has images in game
            thought "Even if I don't want to wear [his_her] top, I still want to look good for [s3_mc.current_partner]."
            thought "This'll be our first night together, after all!"
            # MC outfit changes to sleepwear
            call customize_outfit from _call_customize_outfit_10
            # thought "Hmm. Got to leave some things to the imagination, though, right?"
            # B/H/Cam/aj "Not stressing about what to wear to bed, are you, MC?"
            # B/H/Cam/aj "You know I think you look hot regardless."
            # s3_mc "Thanks, babe."

    if s3_mc.current_partner == "Bill":
        bill "Wow, this is going to be the first time, we, like, properly get to spend the night together..."
        bill "Alone!"
    elif s3_mc.current_partner == "Camilo":
        camilo "Wow, this is going to be the first time, we, like, properly get to spend the night together..."
        camilo "Alone!"
    elif s3_mc.current_partner == "Harry":
        harry "Wow, this is going to be the first time, we, like, properly get to spend the night together..."
        harry "Alone!"
    elif s3_mc.current_partner == "AJ":
        aj "Wow, this is going to be the first time, we, like, properly get to spend the night together..."
        aj "Alone!"

    # CHOICE
    menu:
        thought "This is our first night alone together..."
        "I can't wait to get hot and sweaty in the tent":
            if s3_mc.current_partner == "Bill":
                bill "Yeah, we better get loads of blankets to keep warm."
                bill "Oh, wait... did you mean..."
                "You raise an eyebrow."
                bill "Ah, right. Gotcha."
                bill "Well, that can be arranged."
            elif s3_mc.current_partner == "Camilo":
                camilo "I'm literally a human radiator so, yeah."
                camilo "You bet it's going to be hot in there."
                s3_mc "That's not exactly what I..."
                camilo "Oh, you meant..."
                "[he_she!c] raises [his_her] eyebrows."
                camilo "Well, that can be arranged."
            elif s3_mc.current_partner == "Harry":
                harry "Yeah, we better get loads of blankets to keep warm."
                harry "Oh, wait... did you mean..."
                "You raise an eyebrow."
                harry "Ah, right. Gotcha."
                harry "Well, that can be arranged."
            elif s3_mc.current_partner == "AJ":
                aj "I'm literally a human radiator so, yeah."
                aj "You bet it's going to be hot in there."
                s3_mc "That's not exactly what I..."
                aj "Oh, you meant..."
                "[he_she!c] raises [his_her] eyebrows."
                aj "Well, that can be arranged."
        "I'm kinda scared of the dark...":
            if s3_mc.current_partner == "Bill":
                bill "Hey, don't worry about it."
                bill "I'll be there."
                bill "And if anything does happen..."
                "[he_she!c] grabs something from the dresser."
                bill "I'll defend you with this magic hairbrush!"
                s3_mc "Will that help?"
                bill "Absolutely. It works every time."
            elif s3_mc.current_partner == "Camilo":
                camilo "Hey, don't worry about it."
                camilo "I'll be there."
                camilo "And if anything does happen..."
                "[he_she!c] grabs something from the dresser."
                camilo "I'll defend you with this magic hairbrush!"
                s3_mc "Will that help?"
                camilo "Absolutely. It works every time."
            elif s3_mc.current_partner == "Harry":
                harry "Hey, don't worry about it."
                harry "I'll be there."
                harry "And if anything does happen..."
                "[he_she!c] grabs something from the dresser."
                harry "I'll defend you with this magic hairbrush!"
                s3_mc "Will that help?"
                harry "Absolutely. It works every time."
            elif s3_mc.current_partner == "AJ":
                aj "Hey, don't worry about it."
                aj "I'll be there."
                aj "And if anything does happen..."
                "[he_she!c] grabs something from the dresser."
                aj "I'll defend you with this magic hairbrush!"
                s3_mc "Will that help?"
                aj "Absolutely. It works every time."
        "I will miss sleeping in a room full of people":
            if s3_mc.current_partner == "Bill":
                bill "If that's what floats your boat..."
            elif s3_mc.current_partner == "Camilo":
                camilo "If that's what floats your boat..."
            elif s3_mc.current_partner == "Harry":
                harry "If that's what floats your boat..."
            elif s3_mc.current_partner == "AJ":
                aj "If that's what floats your boat..."
            s3_mc "It does."
            s3_mc "I love being surrounded by many, many, sleeping bodies."
            if s3_mc.current_partner == "Bill":
                bill "Well... I'm sure we'll only be spending one night in the tent."
            elif s3_mc.current_partner == "Camilo":
                camilo "Well... I'm sure we'll only be spending one night in the tent."
            elif s3_mc.current_partner == "Harry":
                harry "Well... I'm sure we'll only be spending one night in the tent."
            elif s3_mc.current_partner == "AJ":
                aj "Well... I'm sure we'll only be spending one night in the tent."

    if s3_mc.current_partner == "Bill":
        if s3e4p2_good_tent:
            bill "We'd better go choose what we want to eat at our camp out!"
        else:
            bill "I hope Elladine picks out some good stuff to eat for our camp out..."
    elif s3_mc.current_partner == "Camilo":
        if s3e4p2_good_tent:
            camilo "We'd better go choose what we want to eat at our camp out!"
        else:
            camilo "I hope Elladine picks out some good stuff to eat for our camp out..."
    elif s3_mc.current_partner == "Harry":
        if s3e4p2_good_tent:
            harry "We'd better go choose what we want to eat at our camp out!"
        else:
            harry "I hope Elladine picks out some good stuff to eat for our camp out..."
    elif s3_mc.current_partner == "AJ":
        if s3e4p2_good_tent:
            aj "We'd better go choose what we want to eat at our camp out!"
        else:
            aj "I hope Elladine picks out some good stuff to eat for our camp out..."

    "You both head down to the kitchen."

    scene s3-kitchen-night with dissolve
    $ new_scene()

    "You head downstairs. Elladine and Nicky are also in the kitchen."

    if s3e4p3_wear_shirt:
        "Elladine points at your top."
        elladine "That's not your top, is it?"
        elladine "I don't recognise it."
        s3_mc "It's [s3_mc.current_partner]'s."
        if s3_mc.current_partner == "Bill":
            bill "I lent it to her."
            "[s3_mc.current_partner] beams at you."
            bill "Looks cute, doesn't it?"
            elladine "So cute."
            nicky "You guys are the cutest."
            bill "We try."
        elif s3_mc.current_partner == "Camilo":
            camilo "I lent it to her."
            "[s3_mc.current_partner] beams at you."
            camilo "Looks cute, doesn't it?"
            elladine "So cute."
            nicky "You guys are the cutest."
            camilo "We try."
        elif s3_mc.current_partner == "Harry":
            harry "I lent it to her."
            "[s3_mc.current_partner] beams at you."
            harry "Looks cute, doesn't it?"
            elladine "So cute."
            nicky "You guys are the cutest."
            harry "We try."
        elif s3_mc.current_partner == "AJ":
            aj "I lent it to her."
            "[s3_mc.current_partner] beams at you."
            aj "Looks cute, doesn't it?"
            elladine "So cute."
            nicky "You guys are the cutest."
            aj "We try."
        "[s3_mc.current_partner] squeezes your hand affectionately."
        nicky "When can we start wearing each other's clothes, babe?"
        elladine "I don't share clothes, babe."
        nicky "Aw."

    if s3e4p2_good_tent or s3e4p2_decorate_tent:
        if s3_mc.current_partner == "Bill":
            bill "So, what food shall we have?"
        elif s3_mc.current_partner == "Camilo":
            camilo "So, what food shall we have?"
        elif s3_mc.current_partner == "Harry":
            harry "So, what food shall we have?"
        elif s3_mc.current_partner == "AJ":
            aj "So, what food shall we have?"

        # CHOICE
        menu:
            thought "What food should we choose for our camp out?"
            "Sausages and beans":
                $ s3e4p3_supper = "Beans"
                if s3_mc.current_partner == "Bill":
                    bill "Yes!"
                    if s3e2p1_bfast_with_bill:
                        $ s3_mc.like("Bill")
                        bill "Like we had on our first sort of breakfast date!"
                        s3_mc "Yeah, just like that!"
                        bill "Sausages and beans are the best part of the fry up."
                elif s3_mc.current_partner == "Camilo":
                    camilo "We can try to cook it over the fire."
                elif s3_mc.current_partner == "Harry":
                    harry "We can try to cook it over the fire."
                elif s3_mc.current_partner == "AJ":
                    aj "We can try to cook it over the fire."
                "[s3_mc.current_partner] gets some tins of beans out from the cupboard and packs of sausages out of the fridge."
                if s3_mc.diet != "Meat":
                    if s3_mc.current_partner == "Bill":
                        bill "We can do veggie sausages for you, [s3_name]."
                    elif s3_mc.current_partner == "Camilo":
                        camilo "We can do veggie sausages for you, [s3_name]."
                    elif s3_mc.current_partner == "Harry":
                        harry "We can do veggie sausages for you, [s3_name]."
                    elif s3_mc.current_partner == "AJ":
                        aj "We can do veggie sausages for you, [s3_name]."
                    s3_mc "Aw, you star. Thanks, babe!"
            "Marshmallows":
                $ s3e4p3_supper = "Marshmallows"
                if s3_mc.current_partner == "Bill":
                    bill "Reminds me of being a kid."
                    "[s3_mc.current_partner] rummages in a cupboard in search for some marshmallows."
                    if s3_mc.diet != "Meat":
                        bill "We've got veggie marshmallows for you, [s3_name]."
                        s3_mc "That's awesome. Thanks, babe!"
                    bill "Got some."
                elif s3_mc.current_partner == "Camilo":
                    camilo "Reminds me of being a kid."
                    "[s3_mc.current_partner] rummages in a cupboard in search for some marshmallows."
                    if s3_mc.diet != "Meat":
                        camilo "We've got veggie marshmallows for you, [s3_name]."
                        s3_mc "That's awesome. Thanks, babe!"
                    camilo "Got some."
                elif s3_mc.current_partner == "Harry":
                    harry "Reminds me of being a kid."
                    "[s3_mc.current_partner] rummages in a cupboard in search for some marshmallows."
                    if s3_mc.diet != "Meat":
                        harry "We've got veggie marshmallows for you, [s3_name]."
                        s3_mc "That's awesome. Thanks, babe!"
                    harry "Got some."
                elif s3_mc.current_partner == "AJ":
                    aj "Reminds me of being a kid."
                    "[s3_mc.current_partner] rummages in a cupboard in search for some marshmallows."
                    if s3_mc.diet != "Meat":
                        aj "We've got veggie marshmallows for you, [s3_name]."
                        s3_mc "That's awesome. Thanks, babe!"
                    aj "Got some."
                    "[s3_mc.current_partner] puts them on a counter, along with some wooden sticks to roast them."
            "Noodle soup":
                $ s3e4p3_supper = "Soup"
                if s3_mc.current_partner == "Bill":
                    bill "Soup?"
                    s3_mc "Yeah. Specifically noodle soup."
                    s3_mc "Nothing better than sitting around the fire pit sipping a mug of hot soup."
                    bill "Well, when you put it like that it sounds so wholesome."
                    "[s3_mc.current_partner] starts getting out some tins of soup and some mugs."
                elif s3_mc.current_partner == "Camilo":
                    camilo "Soup?"
                    s3_mc "Yeah. Specifically noodle soup."
                    s3_mc "Nothing better than sitting around the fire pit sipping a mug of hot soup."
                    camilo "Well, when you put it like that it sounds so wholesome."
                    "[s3_mc.current_partner] starts getting out some tins of soup and some mugs."
                elif s3_mc.current_partner == "Harry":
                    harry "Soup?"
                    s3_mc "Yeah. Specifically noodle soup."
                    s3_mc "Nothing better than sitting around the fire pit sipping a mug of hot soup."
                    harry "Well, when you put it like that it sounds so wholesome."
                    "[s3_mc.current_partner] starts getting out some tins of soup and some mugs."
                elif s3_mc.current_partner == "AJ":
                    aj "Soup?"
                    s3_mc "Yeah. Specifically noodle soup."
                    s3_mc "Nothing better than sitting around the fire pit sipping a mug of hot soup."
                    aj "Well, when you put it like that it sounds so wholesome."
                    "[s3_mc.current_partner] starts getting out some tins of soup and some mugs."
    else:
        elladine "Right. Time to plan out the food."
        nicky "I think we should go for marshmallows!"
        elladine "Nice choice."
        "Nicky rummages in the cupboards and the fridge."

    nicky "Do we need to get the campfire started?"
    elladine "Surely we'd just use the fire pit since, like, it's already there."
    nicky "But it's not camping without a proper fire!"
    s3_mc "Maybe this is safer. No one will lose an eyebrow."

    if s3_mc.current_partner == "Bill":
        bill "Nah, someone has to light it, surely."
    elif s3_mc.current_partner == "Camilo":
        camilo "Nah, someone has to light it, surely."
    elif s3_mc.current_partner == "Harry":
        harry "Nah, someone has to light it, surely."
    elif s3_mc.current_partner == "AJ":
        aj "Nah, someone has to light it, surely."

    nicky "Well, how hard can it be?"
    elladine "I'll show you."
    elladine "I'm a proper fire starter."

    scene s3-firepit-night with dissolve
    $ new_scene()

    "You, [s3_mc.current_partner] and Elladine head over to the firepit."

    "The warm red hues of the flames illuminate everyone's faces as they gather around the firepit."
    "A grill has been suspended over the flames."
    "You pile up everything you brought from the kitchen by the fire."
    elladine "Aw, it's already on."
    seb "You can't turn a fire on, Elladine."
    elladine "Well, I don't know?"
    elladine "This place could be hooked up to all sorts of magic."

    if s3_mc.current_partner == "Bill":
        miki "It was already on when we got here. I set the grill up, though."
    elif s3_mc.current_partner == "Camilo":
        iona "It was already on when we got here. I set the grill up, though."
    elif s3_mc.current_partner == "Harry":
        genevieve "It was already on when we got here. I set the grill up, though."
    elif s3_mc.current_partner == "AJ":
        seb "It was already on when we got here. I set the grill up, though."

    elladine "[s3e3p3_lonely_one] is a sorcerer."
    "[s3e3p3_lonely_one] gives [s3_mc.current_partner] a melancholy look."
    "Elladine smiles at her sympathetically."
    elladine "Thanks, hun."
    "[s3_mc.current_partner] edges closer to you and squeezes your hand reassuringly."

    if s3e4p2_decorate_tent:
        if s3_mc.current_partner == "Bill":
            miki "Your tent looks great, by the way."
            s3_mc "I wanted it to look nice for tonight."
            miki "Course you did."
        elif s3_mc.current_partner == "Camilo":
            iona "Your tent looks great, by the way."
            s3_mc "I wanted it to look nice for tonight."
            iona "Course you did."
        elif s3_mc.current_partner == "Harry":
            genevieve "Your tent looks great, by the way."
            s3_mc "I wanted it to look nice for tonight."
            genevieve "Course you did."
        elif s3_mc.current_partner == "AJ" and s3_mc.bff != "Seb":
            seb "Your tent looks great, by the way."
            s3_mc "I wanted it to look nice for tonight."
            seb "Course you did."

    genevieve "OK, for real. I'm starving!"
    genevieve "What food did you guys bring over?"

    if s3e4p2_good_tent or s3e4p2_decorate_tent:
        if s3e4p3_supper == "Beans":
            s3_mc "We brought sausages and beans!"
            genevieve "Aw, brilliant."
        elif s3e4p3_supper == "Marshmallows":
            s3_mc "We brought marshmallows!"
            genevieve "Aw, brilliant."
        elif s3e4p3_supper == "Soup":
            s3_mc "We brought noodle soup!"
            genevieve "Aw, brilliant."
            if s3_mc.current_partner != "Harry":
                harry "I always forget this stuff can come in tins. "
                harry "Much quicker to just cut open the little packets."
                harry "I'm all about low effort cooking."
    else:
        elladine "Marshmallows!"


    if s3e4p2_good_tent or s3e4p2_decorate_tent:
        if s3e4p3_supper == "Beans":
            "You put a frying pan on the grill and slap the sausages into the sizzling oil."
            "[s3_mc.current_partner] plops the baked beans into a saucepan."
            bill "Sausages and beans is, like, camping perfection."
            "The sausages and beans have been sizzling in a pan on the fire for a few minutes."
            "Genevieve pokes the sausage."
            genevieve "It doesn't look all that cooked to me..."
            "Camilo sticks a fork in it and holds the sausage up."
            camilo "It's all pink and floppy."
            miki "That's the name of your sex tape, Camilo."
            "Camilo playfully nudges her."
            iona "Give it a minute, babe."
            "[s3_mc.current_partner] is warming [his_her] hands by the fire."
            s3_mc "You cold, [s3_mc.current_partner]?"

            if s3_mc.current_partner == "Bill":
                bill "Nah, not majorly."
                bill "But if you want to warm me up I'm not going to object."
            elif s3_mc.current_partner == "Camilo":
                camilo "Nah, not majorly."
                camilo "But if you want to warm me up I'm not going to object."
            elif s3_mc.current_partner == "Harry":
                harry "Nah, not majorly."
                harry "But if you want to warm me up I'm not going to object."
            elif s3_mc.current_partner == "AJ":
                aj "Nah, not majorly."
                aj "But if you want to warm me up I'm not going to object."

            # CHOICE
            menu:
                thought "I should..."
                "Cuddle up to [him_her] by the fire":
                    s3_mc "Come here, you."
                    "You both snuggle up closer together."
                    "[s3_mc.current_partner] leans [his_her] head onto your shoulder and you wrap your arms around [him_her], enveloping [him_her] in your embrace."
                    if s3_mc.current_partner == "Bill":
                        bill "You're so comfy, babe."
                        bill "Like, I could literally fall asleep right here, right now."
                    elif s3_mc.current_partner == "Camilo":
                        camilo "You're so comfy, babe."
                        camilo "Like, I could literally fall asleep right here, right now."
                    elif s3_mc.current_partner == "Harry":
                        bill "You're so comfy, babe."
                        bill "Like, I could literally fall asleep right here, right now."
                    elif s3_mc.current_partner == "AJ":
                        aj "You're so comfy, babe."
                        aj "Like, I could literally fall asleep right here, right now."
                    "[s3_mc.current_partner] pretends to snore."
                    iona "Have you put [s3_mc.current_partner] under a sleeping spell?"
                    s3_mc "I'm afraid so."
                    "You start moving your fork towards [s3_mc.current_partner]'s plate."
                    s3_mc "I wanted a second helping of sausages and beans."
                    "Elladine laughs. [s3_mc.current_partner] sits up straight again."
                    if s3_mc.current_partner == "Bill":
                        bill "I'm awake! I'm awake!"
                    elif s3_mc.current_partner == "Camilo":
                        camilo "I'm awake! I'm awake!"
                    elif s3_mc.current_partner == "Harry":
                        harry "I'm awake! I'm awake!"
                    elif s3_mc.current_partner == "AJ":
                        aj "I'm awake! I'm awake!"
                "Whisper what I want to do to [him_her] tonight in [his_her] ear":
                    thought "That ought to warm [him_her] up."
                    "You lean in to [s3_mc.current_partner]'s ear and whisper."
                    s3_mc "Tonight..."
                    s3_mc "I have something I want to do to you..."
                    if s3_mc.current_partner == "Bill":
                        bill "Firepit.sausages.a.Oh.yeah."
                    elif s3_mc.current_partner == "Camilo":
                        camilo "Firepit.sausages.a.Oh.yeah."
                    elif s3_mc.current_partner == "Harry":
                        harry "Firepit.sausages.a.Oh.yeah."
                    elif s3_mc.current_partner == "AJ":
                        aj "Firepit.sausages.a.Oh.yeah."
                    s3_mc "It involves..."
                    "You slowly stroke [his_her] leg with your finger."
                    s3_mc "One hundred percent less clothes and for us to be very..."
                    s3_mc "Very..."
                    s3_mc "Close."
                    if s3_mc.current_partner == "Bill":
                        bill "You're so naughty."
                    elif s3_mc.current_partner == "Camilo":
                        camilo "You're so naughty."
                    elif s3_mc.current_partner == "Harry":
                        harry "You're so naughty."
                    elif s3_mc.current_partner == "AJ":
                        aj "You're so naughty."
                    "You smile seductively."
                    s3_mc "You have no idea."
                "Put some more logs on the fire":
                    "You get some logs from the side and pop them on the fire to keep it roaring, taking care to not knock the sausages."
                    if s3_mc.current_partner == "Bill":
                        bill "Good idea, babe!"
                    elif s3_mc.current_partner == "Camilo":
                        camilo "Good idea, babe!"
                    elif s3_mc.current_partner == "Harry":
                        harry "Good idea, babe!"
                    elif s3_mc.current_partner == "AJ":
                        aj "Good idea, babe!"
                    "[s3_mc.current_partner] busies himself warming [his_her] hands on the fire."
                    "You start moving your fork towards [s3_mc.current_partner]'s plate."
                    elladine "[s3_mc.current_partner]!"
                    "[s3_mc.current_partner]'s head whips round."
                    if s3_mc.current_partner == "Bill":
                        bill "Hey!"
                    elif s3_mc.current_partner == "Camilo":
                        camilo "Hey!"
                    elif s3_mc.current_partner == "Harry":
                        harry "Hey!"
                    elif s3_mc.current_partner == "AJ":
                        aj "Hey!"
                    s3_mc "Damn, I thought I distracted you! I wanted a second helping."

            seb "Don't think I've ever been, like, camping before."
            genevieve "Aw, really?"
            genevieve "I spend a bit of every summer working in a tent."
            seb "Oh yeah. You're, like, a doctor for campers sometimes aren't you?"
            "Genevieve shrugs."
            genevieve "Close enough. Festival goers."
            seb "You must see some right states."
            seb "Mosh pits, fights, and all sorts."
            "Iona stands up and starts dishing out the sausages and beans. Everyone quickly tucks in."
            iona "Yeah, do you ever get a chance to, like, unwind?"
            iona "It must be so hectic."
            genevieve "I love sneaking a cheeky second to go and watch some grime artists."
            genevieve "A good bop always puts me in a good mood."
            genevieve "And during my lunch breaks I go and see some stand up comedians in the comedy tents."
            genevieve "So, yeah. I think I'm pretty lucky in my job."
            genevieve "It's hard work but it's the highlight of the year"

        elif s3e4p3_supper == "Soup":
            "You put a pan on the griddle and pour in half a dozen tins of noodle soup."
            s3_mc "Pass the mugs out, [s3_mc.current_partner]."

            if s3_mc.current_partner == "Bill":
                bill "Sure, babe."
            elif s3_mc.current_partner == "Camilo":
                camilo "Sure, babe."
            elif s3_mc.current_partner == "Harry":
                harry "Sure, babe."
            elif s3_mc.current_partner == "AJ":
                aj "Sure, babe."

            "The soup begins to boil. You smell the air as it rises."
            "Nicky helps stir the pot."
            nicky "It looks about ready."

            if s3_mc.current_partner == "Bill":
                bill "I'll help serve it up."
            elif s3_mc.current_partner == "Camilo":
                camilo "I'll help serve it up."
            elif s3_mc.current_partner == "Harry":
                harry "I'll help serve it up."
            elif s3_mc.current_partner == "AJ":
                aj "I'll help serve it up."

            "[s3_mc.current_partner] ladles soup into everyone's mug."
            nicky "Cheers, [s3_mc.current_partner]."
            elladine "Yeah, thanks for that!"
            nicky "Noodle soup was such a good shout."
            "[s3_mc.current_partner] sits back down beside you, cradling the warm mug in [his_her] hands."

            if s3_mc.current_partner == "Bill":
                bill "Looks like it's going down well with the others."
            elif s3_mc.current_partner == "Camilo":
                camilo "Looks like it's going down well with the others."
            elif s3_mc.current_partner == "Harry":
                harry "Looks like it's going down well with the others."
            elif s3_mc.current_partner == "AJ":
                aj "Looks like it's going down well with the others."

            "[s3_mc.current_partner] slurps up a noodle in the soup."
            "It twists and turns before disappearing into [his_her] mouth."

            # CHOICE
            menu:
                thought "Hmm, noodle soup..."
                "Do a lady and the tramp thing with the noodle":
                    s3_mc "Shall we do a lil slurpin with the noodle thing..."
                    s3_mc "Like they do on Lady and The Tramp?"
                    "You slurp up a noodle and look at [him_her] with twinkly puppy-dog eyes."
                    if s3_mc.current_partner == "Bill":
                        bill "OK. You are the boss!"
                    elif s3_mc.current_partner == "Camilo":
                        camilo "OK. You are the boss!"
                    elif s3_mc.current_partner == "Harry":
                        harry "OK. You are the boss!"
                    elif s3_mc.current_partner == "AJ":
                        aj "OK. You are the boss!"
                    "[s3_mc.current_partner] takes out a long noodle and puts one end in [his_her] mouth."
                    "You take the other end in yours and slurp."
                    "The noodle piece disappears into your mouth and your lips meet."
                    "You only kiss for a moment, but it is a soft and tender one at that."
                    iona "Oh my word, you two. Get a room."
                    iona "Or a tent."
                    s3_mc "Sorry, you lot."
                    s3_mc "We're getting carried away."
                "Tie a knot in a noodle with your tongue":
                    "You slip a noodle into your mouth and your tongue does acrobats inside."
                    s3_mc "Tada!"
                    "You open your mouth and show [s3_mc.current_partner] your tongue knotting abilities."
                    if s3_mc.current_partner == "Bill":
                        bill "Um, ok wow."
                        bill "That's a real tongue twister."
                        "[he_she!c] leans over and whispers into your ear."
                        bill "I hope we get to put that tongue to good use later."
                    elif s3_mc.current_partner == "Camilo":
                        camilo "Um, ok wow."
                        camilo "That's a real tongue twister."
                        "[he_she!c] leans over and whispers into your ear."
                        camilo "I hope we get to put that tongue to good use later."
                    elif s3_mc.current_partner == "Harry":
                        harry "Um, ok wow."
                        harry "That's a real tongue twister."
                        "[he_she!c] leans over and whispers into your ear."
                        harry "I hope we get to put that tongue to good use later."
                    elif s3_mc.current_partner == "AJ":
                        aj "Um, ok wow."
                        aj "That's a real tongue twister."
                        "[he_she!c] leans over and whispers into your ear."
                        aj "I hope we get to put that tongue to good use later."
                    "You wink at [s3_mc.current_partner]."
                    s3_mc "You bet."
                "Just have a good slurp of the soup":
                    "You take an indulgent gulp of the soup. You can feel your whole body warming up."
                    s3_mc "Hmm, this is so tasty!"
                    if s3_mc.current_partner == "Bill":
                        bill "Yeah, it's delicious."
                    elif s3_mc.current_partner == "Camilo":
                        camilo "Yeah, it's delicious."
                    elif s3_mc.current_partner == "Harry":
                        harry "Yeah, it's delicious."
                    elif s3_mc.current_partner == "AJ":
                        aj "Yeah, it's delicious."

            "Nicky helps himself to another mug from the hot bubbling pot."
    else:
        if s3e4p2_decorate_tent or s3e4p2_good_tent:
            "You pass out the sticks and the marshmallows to everyone."
            iona "I feel like I'm a kid again, camping up on the mountains with my aunt and uncle."
            "She pretends to cheers your stick."
            iona "Cheers!"
        else:
            "Elladine passes out the sticks and the marshmallows to everyone."
            iona "I haven't had these since I went camping as a kid! My aunt and uncle would always bring them up the mountains with us. They're lush."
            seb "Yeah, banging choice, Elladine."

        "You reach over to the fire and turn the marshmallow around the stick until it goes crispy golden colour."
        "Out of the corner of your eye you see a small bright flame on the end of [s3_mc.current_partner]'s stick."

        if s3_mc.current_partner == "Bill":
            bill "Ah!"
            "[he_she!c] lets it drop into the pit. The sticky mess gets quickly engulfed by the flames."
            s3_mc "Perfect marshmallow roasting, hun. It's completely obliterated."
            bill "I don't have any technique whatsoever."
            bill "Yours looks amazing."
        elif s3_mc.current_partner == "Camilo":
            camilo "Ah!"
            "[he_she!c] lets it drop into the pit. The sticky mess gets quickly engulfed by the flames."
            s3_mc "Perfect marshmallow roasting, hun. It's completely obliterated."
            camilo "I don't have any technique whatsoever."
            camilo "Yours looks amazing."
        elif s3_mc.current_partner == "Harry":
            harry "Ah!"
            "[he_she!c] lets it drop into the pit. The sticky mess gets quickly engulfed by the flames."
            s3_mc "Perfect marshmallow roasting, hun. It's completely obliterated."
            harry "I don't have any technique whatsoever."
            harry "Yours looks amazing."
        elif s3_mc.current_partner == "AJ":
            aj "Ah!"
            "[he_she!c] lets it drop into the pit. The sticky mess gets quickly engulfed by the flames."
            s3_mc "Perfect marshmallow roasting, hun. It's completely obliterated."
            aj "I don't have any technique whatsoever."
            aj "Yours looks amazing."

        # CHOICE
        menu:
            thought "My marshmallow does look pretty good..."
            "Eat it all in one go":
                "You chomp down on the marshmallow."
                s3_mc "Nomnomnom."
                "The sugary sweet gooey goddess bursts through your mouth as you bite through the crispier parts."
                "It's a little hot, but you bite through the pain."
                if s3_mc.current_partner == "Bill":
                    bill "Nice?"
                    s3_mc "Delicious."
                    bill "That is one lucky marshmallow."
                elif s3_mc.current_partner == "Camilo":
                    camilo "Nice?"
                    s3_mc "Delicious."
                    camilo "That is one lucky marshmallow."
                elif s3_mc.current_partner == "Harry":
                    harry "Nice?"
                    s3_mc "Delicious."
                    harry "That is one lucky marshmallow."
                elif s3_mc.current_partner == "AJ":
                    aj "Nice?"
                    s3_mc "Delicious."
                    aj "That is one lucky marshmallow."
            "Feed [s3_mc.current_partner] the marshmallow":
                "You take the stick out of the fire and poke it towards [s3_mc.current_partner]'s face."
                s3_mc "Want a bite of my marshmallow?"
                if s3_mc.current_partner == "Bill":
                    "[s3_mc.current_partner] looks at it a little suspiciously."
                    bill "I've never actually had them before but, like, yeah sure."
                    bill "Let's try them."
                    "[s3_mc.current_partner] bites the marshmallow off your stick."
                    bill "Oh, okay. That's actually, like kinda weird but good."
                    bill "It's so sticky!"
                elif s3_mc.current_partner == "Camilo":
                    "[s3_mc.current_partner] looks at it a little suspiciously."
                    camilo "I've never actually had them before but, like, yeah sure."
                    camilo "Let's try them."
                    "[s3_mc.current_partner] bites the marshmallow off your stick."
                    camilo "Oh, okay. That's actually, like kinda weird but good."
                    camilo "It's so sticky!"
                elif s3_mc.current_partner == "Harry":
                    "[s3_mc.current_partner] gives you some sexy eyes and licks [his_her] lips."
                    harry "You don't have to ask me twice."
                    "[he_she!c] bites the marshmallow off your stick and licks [his_her] lips."
                    harry "Mmm! Delicious."
                    harry "I love marshmallows."
                elif s3_mc.current_partner == "AJ":
                    "[s3_mc.current_partner] gives you some sexy eyes and licks [his_her] lips."
                    aj "You don't have to ask me twice."
                    "[he_she!c] bites the marshmallow off your stick and licks [his_her] lips."
                    aj "Mmm! Delicious."
                    aj "I love marshmallows."
            "Set it on fire":
                "You leave the marshmallow on the flames."
                s3_mc "And it burns, burns, burns..."
                if s3_mc.current_partner == "Bill":
                    bill "Um..."
                elif s3_mc.current_partner == "Camilo":
                    camilo "Um..."
                elif s3_mc.current_partner == "Harry":
                    harry "Um..."
                elif s3_mc.current_partner == "AJ":
                    aj "Um..."
                s3_mc "The marshmallow of fire!"
                s3_mc "The marshmallow of fire..."
                "It catches fire."
                if s3e1p2_set_fire:
                    "Elladine laughs at you from across the circle."
                    elladine "[s3_name] is at it again."
                    elladine "We know what you're like around fire!"
                "Your marshmallow melts off your stick and is obliterated by the flames."
                if s3_mc.current_partner == "Bill":
                    bill "Proper roasted that one is."
                elif s3_mc.current_partner == "Camilo":
                    camilo "Proper roasted that one is."
                elif s3_mc.current_partner == "Harry":
                    harry "Proper roasted that one is."
                elif s3_mc.current_partner == "AJ":
                    aj "Proper roasted that one is."
                "You both laugh and grab another marshmallow to eat."

        miki "Camping always makes me think of this time I made this, like, marshmallow tower."
        camilo "You what?"
        iona "Come again?"
        miki "Oh, yeah, I did a whole YouTube series."
        miki "It was called Camping With Friends!"
        miki "In one of the videos we had this competition to see who could model the funniest thing out of marshmallows."
        "Camilo starts stacking the marshmallow on top of each other on the stick, trying to fashion his own marshmallow tower."
        "Elladine bursts out laughing."
        elladine "That's a very phallic looking tower indeed."
        camilo "It's proper pink and floppy."
        miki "That's the name of your sex tape, Camilo."
        "Camilo playfully pokes her with the stick of marshmallows."
        seb "Yum."

    "Genevieve looks around the Villa. She seems a little on edge."
    genevieve "I could have sworn I saw something moving over there."
    seb "Could have been the Villa's Ghost."
    genevieve "Er, what?"
    elladine "Ghost story time!"
    "Elladine gets out her phone, turns on the torch, and shines it under her chin."
    "Genevieve looks a little concerned while the others start to make spooky noises."
    elladine "It was a cold and lonely night."
    seb "Pretty sure it's dark and stormy."
    genevieve "I love that cocktail..."
    camilo "That's the name of your sex tape, Viv."
    elladine "Fine! It was a hot and steamy night..."

    if s3_mc.current_partner == "Bill":
        bill "That's more like it..."
    elif s3_mc.current_partner == "Camilo":
        camilo "That's more like it..."
    elif s3_mc.current_partner == "Harry":
        harry "That's more like it..."
    elif s3_mc.current_partner == "AJ":
        aj "That's more like it..."
        
    elladine "The Islanders were just settling down to a nice cup of..."

    # CHOICE
    menu:
        s3_mc "A nice cup of..."
        "Hot chocolate":
            $ s3e4p3_drink = "hot chocolate"
            miki "Oh, damn you [s3_name]."
            miki "Now I'm craving a hot chocolate."
            iona "Yeah, me too."
            elladine "Miki. Focus."
        "Fear of my enemies":
            $ s3e4p3_drink = "fear"
            elladine "A cup of fear?"
            s3_mc "Specifically, the fear of my enemies."
            "Seb and Iona snort loudly with laughter."
            s3_mc "What? I thought this was meant to be a scary story."
            iona "You can't cup fear."
            seb "I don't know."
            seb "If I leave my cups out for too long they start wearing fuzzy green jackets."
            seb "And that can be a little haunting."
            elladine "Ugh. Grim, but fine."
        "Kombucha":
            $ s3e4p3_drink = "kombucha"
            iona "Kombucha?"
            s3_mc "Yeah, that can be quite a scary drink to be honest because you don't know if you're going to like it."
            seb "I second that."
            elladine "OK..."

    elladine "The Islanders were just settling down to a nice cup of [s3e4p3_drink]."
    elladine "When all of a sudden..."
    "Seb jumps up."
    seb "There was a shiny demon!"
    "He points to the grass."
    seb "In the middle of the lawn."
    "Genevieve squeals."
    genevieve "Ah!"
    iona "That's not very ghostly though."
    genevieve "Demons are scary."
    seb "Yeah, and it's a hot and steamy night."
    seb "Perfect climate for a wild demon to appear."
    iona "I guess that explains the shininess."
    elladine "OK, all of a sudden a shiny demon popped up."
    harry "And it said..."

    # CHOICE
    menu:
        thought "What did the demon say to us?"
        "Welcome to Clown Island":
            camilo "Aw, I love clowns."
            s3_mc "Yeah, and on Clown Island do you know what we eat for breakfast, lunch, and dinner?"
            genevieve "Wha.. what?"
            s3_mc "Souls."
            s3_mc "I think it might be soul eating time."
            s3_mc "Said the shiny demon."
        "I'm seeking fresh souls":
            s3_mc "I'm seeking fresh souls, said the shiny demon."
            "Everyone is silent except the crackle of the fire."
            "Miki stands up and shouts."
            miki "Back off, you evil shiny demon."
            miki "You're not taking my friend's souls."
            genevieve "Yeah! You tell em'."
            if s3_mc.current_partner == "Bill":
                miki "The demon just grinned and said 'I may have sinned but there's no need to push me around.'"
                miki "And then, the demon latched onto [s3_mc.current_partner] and said..."
                miki "I've got [him_her] first so you can do your worst."
                miki "[he_she!c]'s going underground!"
            elif s3_mc.current_partner == "Camilo":
                iona "The demon just grinned and said 'I may have sinned but there's no need to push me around.'"
                iona "And then, the demon latched onto [s3_mc.current_partner] and said..."
                iona "I've got [him_her] first so you can do your worst."
                iona "[he_she!c]'s going underground!"
            elif s3_mc.current_partner == "Harry":
                genevieve "The demon just grinned and said 'I may have sinned but there's no need to push me around.'"
                genevieve "And then, the demon latched onto [s3_mc.current_partner] and said..."
                genevieve "I've got [him_her] first so you can do your worst."
                genevieve "[he_she!c]'s going underground!"
            elif s3_mc.current_partner == "AJ":
                seb "The demon just grinned and said 'I may have sinned but there's no need to push me around.'"
                seb "And then, the demon latched onto [s3_mc.current_partner] and said..."
                seb "I've got [him_her] first so you can do your worst."
                seb "[he_she!c]'s going underground!"
            "You and [s3_mc.current_partner] look at [s3e3p3_lonely_one], a little afraid."
            elladine "Go along with it, [s3_mc.current_partner]."
        "Hey, I'm the new Islander!":
            s3_mc "Hi, I'm the new Islanders, said the demon."
            if s3_mc.current_partner == "Bill":
                miki "Now that is terrifying."
                "[s3e3p3_lonely_one] stands up."
                miki "Yeah, and it's come to steal [s3_mc.current_partner]'s soul from [s3_name]!"
            elif s3_mc.current_partner == "Camilo":
                iona "Now that is terrifying."
                "[s3e3p3_lonely_one] stands up."
                iona "Yeah, and it's come to steal [s3_mc.current_partner]'s soul from [s3_name]!"
            elif s3_mc.current_partner == "Harry":
                genevieve "Now that is terrifying."
                "[s3e3p3_lonely_one] stands up."
                genevieve "Yeah, and it's come to steal [s3_mc.current_partner]'s soul from [s3_name]!"
            elif s3_mc.current_partner == "AJ":
                seb "Now that is terrifying."
                "[s3e3p3_lonely_one] stands up."
                seb "Yeah, and it's come to steal [s3_mc.current_partner]'s soul from [s3_name]!"
            "[s3e3p3_lonely_one] winks at you cheekily."
            s3_mc "No, not [s3_mc.current_partner]!"

    if s3_mc.current_partner == "Bill":
        bill "Save me, [s3_name]."
    elif s3_mc.current_partner == "Camilo":
        camilo "Save me, [s3_name]."
    elif s3_mc.current_partner == "Harry":
        harry "Save me, [s3_name]."
    elif s3_mc.current_partner == "AJ":
        aj "Save me, [s3_name]."

    # CHOICE
    menu:
        thought "[s3_mc.current_partner] soul is about to be stolen by the demon!"
        "Cling on to him tightly":
            $ s3_mc.like(s3_mc.current_partner)
            "You quickly grab onto [s3_mc.current_partner]."
            s3_mc "I'll protect your soul!"
            miki "Aw, you're like, soul mates."
            if s3_mc.current_partner == "Bill":
                bill "Thanks, [s3_name]."
                "[he_she!c] hugs you back, tightly."
                bill "And by the power of a cuddle the demon was shattered into a million pieces!"
            elif s3_mc.current_partner == "Camilo":
                camilo "Thanks, [s3_name]."
                "[he_she!c] hugs you back, tightly."
                camilo "And by the power of a cuddle the demon was shattered into a million pieces!"
            elif s3_mc.current_partner == "Harry":
                harry "Thanks, [s3_name]."
                "[he_she!c] hugs you back, tightly."
                harry "And by the power of a cuddle the demon was shattered into a million pieces!"
            elif s3_mc.current_partner == "AJ":
                aj "Thanks, [s3_name]."
                "[he_she!c] hugs you back, tightly."
                aj "And by the power of a cuddle the demon was shattered into a million pieces!"
            iona "A demon shattering cuddle?"
            iona "Really?"
        "Offer [s3_mc.current_partner] for a price":
            $ s3_mc.dislike(s3_mc.current_partner)
            s3_mc "Sorry, shiny demon. You can't just have [s3_mc.current_partner]."
            "[s3_mc.current_partner] smiles at you."
            s3_mc "Nothing is free these days."
            s3_mc "You've got to pay."
            s3_mc "I want to make a profit."
            "[s3_mc.current_partner]'s face drops into a frown."
            if s3_mc.current_partner == "Bill":
                bill "Oh."
            elif s3_mc.current_partner == "Camilo":
                camilo "Oh."
            elif s3_mc.current_partner == "Harry":
                harry "Oh."
            elif s3_mc.current_partner == "AJ":
                aj "Oh."
            seb "Looks like your soul's about to be sold, [s3_mc.current_partner]."
            seb "But the demon has forgotten his pin and [s3_mc.current_partner] costs more than the limit on contactless."
            seb "So the demon sulks away back to the underworld, sparing [s3_mc.current_partner]'s soul for another day."
            if s3_mc.current_partner == "Bill":
                bill "Phew."
            elif s3_mc.current_partner == "Camilo":
                camilo "Phew."
            elif s3_mc.current_partner == "Harry":
                harry "Phew."
            elif s3_mc.current_partner == "AJ":
                aj "Phew."
        "Throw the cup of [s3e4p3_drink] on it":
            s3_mc "I'll throw my cup of [s3e4p3_drink] over the demon."
            if s3e4p3_drink == "fear":
                $ s3e4p3_drink = "fear from [s3_name]'s enemies"
            miki "The metaphorical cup of [s3e4p3_drink] makes the demon flea into the hot and steamy night."

    "Genevieve cheers and claps excitedly."
    genevieve "Yay!"
    genevieve "Be gone, shiny demon!"
    seb "Unfortunately, the shiny demon left behind a ghostly presence..."
    seb "Which will haunt the Villa for years and years to come."
    "The wind picks up a little causing the shadows of the dancing flames to flicker."

    # CHOICE
    menu:
        thought "The tale is over..."
        "Well, that wasn't a very scary story":
            iona "Yeah, I agree."
            iona "There is nothing scary about a villain that just pops up without any kind of build up."
            iona "It is the anticipation of it that makes it frightening."
            if s3e4p3_drink == "fear from [s3_name]'s enemies":
                $ s3e4p3_drink = "fear"
            elladine "We were drinking a cup of [s3e4p3_drink]! That was the setup."
            iona "Terrifying."
            seb "Watch out..."
            seb "Iona Hitchcock is about."
            "Iona rolls her eyes."
        "What happens next? I want a sequel!":
            elladine "Yeah! We could do a whole novel about it."
            miki "Write the book and then make it into three separate movies ultimate gains."
            elladine "I'm too sleepy for that."
        "Can we get into the tents already?":
            "[s3_mc.current_partner] raises [his_her] eyebrows in surprise. Miki bursts out laughing."
            miki "Did a story about a shiny devil make you feel..."
            miki "Erotically charged?"
            "You wink?"
            s3_mc "Nah, I'm just feeling hot and steamy tonight."

    "You hear a light snoozing. Nicky has dozed off on Elladine's lap."
    camilo "Aw, he's so cute when he's sleeping."
    iona "I'm knackered too."
    genevieve "But it's getting pretty dark..."
    elladine "Yeah, bed time, I think."
    genevieve "Hm, yeah."
    "She looks around at the empty loungers."
    harry "Genevieve, the demon isn't actually real."

    if s3_mc.current_partner != "Harry":
        harry "It'll be fine, hun, I'm right with you! "
        "Genevieve begrudgingly follows Harry into their tent."
    
    if s3_mc.current_partner == "Bill":
        miki "I'm actually going to go and sleep inside, I think."
        bill "Are you sure you're OK?"
        miki "Yeah, no way I'm sleeping in a tent by myself."
        s3_mc "OK hun, whatever works for you."
        "[s3e3p3_lonely_one] heads inside the Villa."
    elif s3_mc.current_partner == "Camilo":
        iona "I'm actually going to go and sleep inside, I think."
        camilo "Are you sure you're OK?"
        iona "Yeah, no way I'm sleeping in a tent by myself."
        s3_mc "OK hun, whatever works for you."
        "[s3e3p3_lonely_one] heads inside the Villa."
    elif s3_mc.current_partner == "Harry":
        genevieve "I think I'm going to skip the camp out and sleep inside."
        genevieve "Don't fancy sleeping in a tent on my own in the dark outside."
        aj "You can share with me and Seb."
        aj "We're not going to be making anything go bump in the night."
        "AJ laughs. Seb rolls his eyes."
        seb "Truth to be told, yeah, if you want to share with us you totally can."
        seb "It might be squashed but it beats sleeping the Villa on your own."
        "Genevieve puts on a brace face."
        genevieve "Alright, alright."
        genevieve "That's real sweet of you guys."
        "They all squeeze into one tent together."
    elif s3_mc.current_partner == "AJ":
        seb "I'm actually going to go and sleep inside, I think."
        aj "Are you sure you're OK?"
        seb "Yeah, no way I'm sleeping in a tent by myself."
        s3_mc "OK hun, whatever works for you."
        "[s3e3p3_lonely_one] heads inside the Villa."


    if s3_mc.current_partner == "Bill":
        bill "Right, shall we get in our tent?"
    elif s3_mc.current_partner == "Camilo":
        camilo "Right, shall we get in our tent?"
    elif s3_mc.current_partner == "Harry":
        harry "Right, shall we get in our tent?"
    elif s3_mc.current_partner == "AJ":
        aj "Right, shall we get in our tent?"

    if s3e4p2_give_rock:
        if s3_mc.current_partner == "Bill":
            bill "Sorry, our new home."
            "[s3_mc.current_partner] opens [his_her] clenched fist and reveals the little pebble."
            s3_mc "Aw, you kept our keys!"
            bill "Yeah, of course."
            bill "Can't have any shiny demons trying to break in, can we?"
        elif s3_mc.current_partner == "Camilo":
            camilo "Sorry, our new home."
            "[s3_mc.current_partner] opens [his_her] clenched fist and reveals the little pebble."
            s3_mc "Aw, you kept our keys!"
            camilo "Yeah, of course."
            camilo "Can't have any shiny demons trying to break in, can we?"
        elif s3_mc.current_partner == "Harry":
            harry "Sorry, our new home."
            "[s3_mc.current_partner] opens [his_her] clenched fist and reveals the little pebble."
            s3_mc "Aw, you kept our keys!"
            harry "Yeah, of course."
            harry "Can't have any shiny demons trying to break in, can we?"
        elif s3_mc.current_partner == "AJ":
            aj "Sorry, our new home."
            "[s3_mc.current_partner] opens [his_her] clenched fist and reveals the little pebble."
            s3_mc "Aw, you kept our keys!"
            aj "Yeah, of course."
            aj "Can't have any shiny demons trying to break in, can we?"

        s3_mc "No way, not in our home."
        "[s3_mc.current_partner] unzips the tent and you clamber into your new home for the night."

    if s3e4p2_say_dirty:
        s3_mc "Sure, let's get in there and get filthy."
        "[he_she!c] unzips the tent. You take [s3_mc.current_partner]'s hand and lead [him_her] in."

    if s3e4p2_decorate_tent or s3e4p2_good_tent:
        "You and [s3_mc.current_partner] huddle in the tent. It's super cosy."
    else:
        "You and [s3_mc.current_partner] huddle in the tent. It's a bit chilly."

    scene s3-inside-tent-standard-night with dissolve
    $ new_scene()

    if s3e4p2_decorate_tent:
        if s3_mc.current_partner == "Bill":
            bill "It looks like someone is serving up some camping eleganza."
            bill "You did such a good job of doing it up."
        elif s3_mc.current_partner == "Camilo":
            camilo "It looks like someone is serving up some camping eleganza."
            camilo "You did such a good job of doing it up."
        elif s3_mc.current_partner == "Harry":
            harry "It looks like someone is serving up some camping eleganza."
            harry "You did such a good job of doing it up."
        elif s3_mc.current_partner == "AJ":
            aj "It looks like someone is serving up some camping eleganza."
            aj "You did such a good job of doing it up."
        s3_mc "Thanks babe."
    else:
        if s3_mc.current_partner == "Bill":
            bill "We're serving camping realness in here."
        elif s3_mc.current_partner == "Camilo":
            camilo "We're serving camping realness in here."
        elif s3_mc.current_partner == "Harry":
            harry "We're serving camping realness in here."
        elif s3_mc.current_partner == "AJ":
            aj "We're serving camping realness in here."

    thought "Hmm, we've got sleeping bags and a duvet..."

    # CHOICE
    menu:
        thought "Do I want to cuddle up to [s3_mc.current_partner] or put some distance between us?"
        "Spread out the duvet and cuddle":
            "You throw the duvet across you both."
            "[s3_mc.current_partner] quickly snuggles up to you, enveloping you in [his_her] arms."
            if s3_mc.current_partner == "Bill":
                bill "Huddle close before we get too cold."
            elif s3_mc.current_partner == "Camilo":
                camilo "Huddle close before we get too cold."
            elif s3_mc.current_partner == "Harry":
                harry "Huddle close before we get too cold."
            elif s3_mc.current_partner == "AJ":
                aj "Huddle close before we get too cold."
        "Get in the sleeping bag on your own":
            "You get in your sleeping bag. [s3_mc.current_partner] does the same."
        "Zip two sleeping bags together and share":
            s3_mc "Let's zip two sleeping bags together."
            "You fiddle with the zips of the two bags until they're joined as one big bag."
            if s3_mc.current_partner == "Bill":
                bill "You think we'll fit?"
                s3_mc "Of course!"
                "You slide into the sleeping bag beside [him_her]. It's not very roomy, but it's super cosy."
                bill "OK, this is comfier than I thought."
            elif s3_mc.current_partner == "Camilo":
                camilo "You think we'll fit?"
                s3_mc "Of course!"
                "You slide into the sleeping bag beside [him_her]. It's not very roomy, but it's super cosy."
                camilo "OK, this is comfier than I thought."
            elif s3_mc.current_partner == "Harry":
                harry "You think we'll fit?"
                s3_mc "Of course!"
                "You slide into the sleeping bag beside [him_her]. It's not very roomy, but it's super cosy."
                harry "OK, this is comfier than I thought."
            elif s3_mc.current_partner == "AJ":
                aj "You think we'll fit?"
                s3_mc "Of course!"
                "You slide into the sleeping bag beside [him_her]. It's not very roomy, but it's super cosy."
                aj "OK, this is comfier than I thought."

    "You lay beside each other, listening to the chirping of crickets."
    if s3_mc.current_partner == "Bill":
        bill "Honestly, I can't get over how, like, close we've gotten in such a short time."
    elif s3_mc.current_partner == "Camilo":
        camilo "Honestly, I can't get over how, like, close we've gotten in such a short time."
    elif s3_mc.current_partner == "Harry":
        harry "Honestly, I can't get over how, like, close we've gotten in such a short time."
    elif s3_mc.current_partner == "AJ":
        aj "Honestly, I can't get over how, like, close we've gotten in such a short time."

    # CHOICE
    menu: 
        thought "[s3_mc.current_partner] thinks we're getting closer!"
        "Yeah, I agree, it's lovely":
            if s3_mc.current_partner == "Bill":
                bill "It's like we've known each other for ages, isn't it?"
            elif s3_mc.current_partner == "Camilo":
                camilo "It's like we've known each other for ages, isn't it?"
            elif s3_mc.current_partner == "Harry":
                harry "It's like we've known each other for ages, isn't it?"
            elif s3_mc.current_partner == "AJ":
                aj "It's like we've known each other for ages, isn't it?"
            s3_mc "Totally."
        "We could get even closer...":
            if s3_mc.current_partner == "Bill":
                bill "Oh, yeah?"
                "[s3_mc.current_partner] winks at you."
                bill "I'm sure that could be arranged."
            elif s3_mc.current_partner == "Camilo":
                camilo "Oh, yeah?"
                "[s3_mc.current_partner] winks at you."
                camilo "I'm sure that could be arranged."
            elif s3_mc.current_partner == "Harry":
                harry "Oh, yeah?"
                "[s3_mc.current_partner] winks at you."
                harry "I'm sure that could be arranged."
            elif s3_mc.current_partner == "AJ":
                aj "Oh, yeah?"
                "[s3_mc.current_partner] winks at you."
                aj "I'm sure that could be arranged."
        "This tent is pretty cramped":
            if s3_mc.current_partner == "Bill":
                bill "Yeah, I guess it is!"
            elif s3_mc.current_partner == "Camilo":
                camilo "Yeah, I guess it is!"
            elif s3_mc.current_partner == "Harry":
                harry "Yeah, I guess it is!"
            elif s3_mc.current_partner == "AJ":
                aj "Yeah, I guess it is!"

    if s3_mc.current_partner == "Bill":
        bill "It's only been a few days and we're already on a sort of holiday away from home."
        s3_mc "How?"
        bill "That's what camping feels like to me, even if it's in your back garden."
        bill "We're literally already on holiday...so, it's like we're on a holiday away from a holiday!"
        "[s3_mc.current_partner] smiles at you, blushing a little."
        bill "It's so funny that this is the first time we've, like, actually slept alone."
    elif s3_mc.current_partner == "Camilo":
        camilo "It's only been a few days and we're already on a sort of holiday away from home."
        s3_mc "How?"
        camilo "That's what camping feels like to me, even if it's in your back garden."
        camilo "We're literally already on holiday...so, it's like we're on a holiday away from a holiday!"
        "[s3_mc.current_partner] smiles at you, blushing a little."
        camilo "It's so funny that this is the first time we've, like, actually slept alone."
    elif s3_mc.current_partner == "Harry":
        harry "It's only been a few days and we're already on a sort of holiday away from home."
        s3_mc "How?"
        harry "That's what camping feels like to me, even if it's in your back garden."
        harry "We're literally already on holiday...so, it's like we're on a holiday away from a holiday!"
        "[s3_mc.current_partner] smiles at you, blushing a little."
        harry "It's so funny that this is the first time we've, like, actually slept alone."
    elif s3_mc.current_partner == "AJ":
        aj "It's only been a few days and we're already on a sort of holiday away from home."
        s3_mc "How?"
        aj "That's what camping feels like to me, even if it's in your back garden."
        aj "We're literally already on holiday...so, it's like we're on a holiday away from a holiday!"
        "[s3_mc.current_partner] smiles at you, blushing a little."
        aj "It's so funny that this is the first time we've, like, actually slept alone."

    # CHOICE
    menu:
        thought "This is the first time me and [s3_mc.current_partner] have slept alone together!"
        "It's about time, right?":
            if s3_mc.current_partner == "Bill":
                bill "Totally."
            elif s3_mc.current_partner == "Camilo":
                camilo "Totally."
            elif s3_mc.current_partner == "Harry":
                harry "Totally."
            elif s3_mc.current_partner == "AJ":
                aj "Totally."
        "We should take advantage of it":
            if s3_mc.current_partner == "Bill":
                bill "You think?"
            elif s3_mc.current_partner == "Camilo":
                camilo "You think?"
            elif s3_mc.current_partner == "Harry":
                harry "You think?"
            elif s3_mc.current_partner == "AJ":
                aj "You think?"
            s3_mc "For sure."
        "It feels weird without the others!":
            if s3_mc.current_partner == "Bill":
                bill "Yeah..."
                bill "Isn't it weird how we now find it weird not having a bunch of other people sleeping next to you?"
            elif s3_mc.current_partner == "Camilo":
                camilo "Yeah..."
                camilo "Isn't it weird how we now find it weird not having a bunch of other people sleeping next to you?"
            elif s3_mc.current_partner == "Harry":
                harry "Yeah..."
                harry "Isn't it weird how we now find it weird not having a bunch of other people sleeping next to you?"
            elif s3_mc.current_partner == "AJ":
                aj "Yeah..."
                aj "Isn't it weird how we now find it weird not having a bunch of other people sleeping next to you?"
            s3_mc "Yeah, totally."

    if s3e4p3_wear_shirt:
        "[s3_mc.current_partner] gently strokes the sleeve of [his_her] top."
        if s3_mc.current_partner == "Bill":
            bill "By the way, you look so cute in my top."
            s3_mc "Thanks for lending it to me."
            bill "Any day."
            bill "You wear it better than me."
            bill "Are you sleepy?"
            bill "Or would you like to stay up talking and maybe..."
            "He shakes the tent a little."
            bill "Test to see if this tent is as strong as it looks?"
        elif s3_mc.current_partner == "Camilo":
            camilo "By the way, you look so cute in my top."
            s3_mc "Thanks for lending it to me."
            camilo "Any day."
            camilo "You wear it better than me."
            camilo "Are you sleepy?"
            camilo "Or shall we chill out in this tent.."
            camilo "And maybe take advantage of this alone time?"
        elif s3_mc.current_partner == "Harry":
            harry "By the way, you look so cute in my top."
            s3_mc "Thanks for lending it to me."
            harry "Any day."
            harry "You wear it better than me."
            harry "Are you sleepy?"
            harry "Or do you maybe want to..."
            "Harry raises his eyebrow."
            harry "Get up close and personal?"
        elif s3_mc.current_partner == "AJ":
            aj "By the way, you look so cute in my top."
            s3_mc "Thanks for lending it to me."
            aj "Any day."
            aj "You wear it better than me."
            aj "Are you sleepy?"
            aj "Or do you want to stay up all night talking and..."
            aj "Doing other stuff?"

    # CHOICE
    menu:
        thought "Do I want to go to sleep or spend some time with [s3_mc.current_partner]?"
        "Stay up with [s3_mc.current_partner]":
            $ s3e4p3_stay_up = True
            $ s3_mc.like(s3_mc.current_partner)
            jump s3e4p3_stay_up
        "Go to sleep":
            s3_mc "I'm so tired."
            s3_mc "I think I'll just go to sleep."
            if s3_mc.current_partner == "Bill":
                bill "That's fair enough!"
                bill "It's pretty late."
                bill "Night, gorgeous."
            elif s3_mc.current_partner == "Camilo":
                camilo "That's fair enough!"
                camilo "It's pretty late."
                camilo "Night, gorgeous."
            elif s3_mc.current_partner == "Harry":
                harry "That's fair enough!"
                harry "It's pretty late."
                harry "Night, gorgeous."
            elif s3_mc.current_partner == "AJ":
                aj "That's fair enough!"
                aj "It's pretty late."
                aj "Night, gorgeous."
            "You both settle down and drift off to sleep."

            jump s3e4p3_ending
    return

label s3e4p3_stay_up:
    s3_mc "We can stay up!"

    if s3_mc.current_partner == "Bill":
        bill "Cool."
        bill "We can have a proper good chat."
        bill "It's hard chatting at night with loads of people in the same room, isn't it?"
    elif s3_mc.current_partner == "Camilo":
        camilo "Cool."
        camilo "We can have a proper good chat."
        camilo "It's hard chatting at night with loads of people in the same room, isn't it?"
    elif s3_mc.current_partner == "Harry":
        harry "Cool."
        harry "We can have a proper good chat."
        harry "It's hard chatting at night with loads of people in the same room, isn't it?"
    elif s3_mc.current_partner == "AJ":
        aj "Cool."
        aj "We can have a proper good chat."
        aj "It's hard chatting at night with loads of people in the same room, isn't it?"
    s3_mc "Yeah, for sure."
    "You huddle closer to [s3_mc.current_partner]."

    if s3_mc.current_partner == "Bill":
        call s3e4p3_stay_up_bill from _call_s3e4p3_stay_up_bill
    elif s3_mc.current_partner == "Camilo":
        call s3e4p3_stay_up_camilo from _call_s3e4p3_stay_up_camilo
    elif s3_mc.current_partner == "Harry":
        call s3e4p3_stay_up_harry from _call_s3e4p3_stay_up_harry
    elif s3_mc.current_partner == "AJ":
        call s3e4p3_stay_up_aj from _call_s3e4p3_stay_up_aj

    "You can hear giggling from the other tents. Someone moans a little too loud."

    if s3_mc.current_partner == "Bill":
        bill "Sounds like the others are getting it on in their tents!"
    elif s3_mc.current_partner == "Camilo":
        camilo "This really reminds me of the times I used to pitch a tent with my girl in my back garden to get away from all my family."
        "He laughs, raising his voice a little so the other Islanders can hear him."
        camilo "Except my family weren't all around me getting it on as well."
        "Someone laughs. Someone else moans."
    elif s3_mc.current_partner == "Harry":
        harry "Sounds like the others are getting it on in their tents!"
    elif s3_mc.current_partner == "AJ":
        aj "Sounds like the others are getting it on in their tents!"

    "[s3_mc.current_partner] grins."
    
    # CHOICE
    menu:
        thought "Should me and [s3_mc.current_partner] do bits?"
        "Nah, we should just cuddle":
            if s3_mc.current_partner == "Bill":
                bill "Come here."
                "[he_she!c] wraps [his_her] arms around you, spooning you close."
                bill "I love a good cuddle."
                bill "You're by far the best person I've got to spoon."
                s3_mc "Oh, really?"
                bill "Yeah."
                bill " [s3_name]:The Best Spooner is what should be on your CV."
            elif s3_mc.current_partner == "Camilo":
                camilo "Come here."
                "[he_she!c] wraps [his_her] arms around you, spooning you close."
                camilo "I love a good cuddle."
                camilo "You're by far the best person I've got to spoon."
                s3_mc "Oh, really?"
                camilo "Yeah."
                camilo " [s3_name]:The Best Spooner is what should be on your CV."
            elif s3_mc.current_partner == "Harry":
                harry "Come here."
                "[he_she!c] wraps [his_her] arms around you, spooning you close."
                harry "I love a good cuddle."
                harry "You're by far the best person I've got to spoon."
                s3_mc "Oh, really?"
                harry "Yeah."
                harry " [s3_name]:The Best Spooner is what should be on your CV."
            elif s3_mc.current_partner == "AJ":
                aj "Come here."
                "[he_she!c] wraps [his_her] arms around you, spooning you close."
                aj "I love a good cuddle."
                aj "You're by far the best person I've got to spoon."
                s3_mc "Oh, really?"
                aj "Yeah."
                aj " [s3_name]:The Best Spooner is what should be on your CV."
            "You smile and snuggle further into [s3_mc.current_partner]."
        "Yes! Get on top of [him_her] and do bits":
            $ s3e4p3_tent_bits = True
            "You straddle [s3_mc.current_partner] and interlock your fingers with [his_her], gently holding [him_her] down on the tent ground."
            if s3_mc.current_partner == "Bill":
                "Bill gestures for you to come down to him and kiss him."
                "His hands squeeze your thighs as you kiss his neck."
                bill "I love having you on top of me like this."
            elif s3_mc.current_partner == "Camilo":
                "Camilo pulls you close to him and kisses you."
                "His hands stroke your lower waist."
                camilo "Damn. Girl, you are so hot."
            elif s3_mc.current_partner == "Harry":
                harry "Easy tiger!"
                "Harry balances up on his elbows and leans up to kiss you."
                "You lean down to his level and kiss his neck."
                harry "You're so sexy."
            elif s3_mc.current_partner == "AJ":
                "AJ tugs lightly on your wrists, pulling you closer to her."
                "She kisses you urgently."
                aj "I can't get enough of you."

            "The cool air doesn't stop you from stripping off."
            if s3_mc.current_partner == "Bill":
                bill "Woah."
                "As you move your hips [s3_mc.current_partner]'s breath quickens."
                bill "Oh, woah."
            elif s3_mc.current_partner == "Camilo":
                camilo "Woah."
                "As you move your hips [s3_mc.current_partner]'s breath quickens."
                camilo "Oh, woah."
            elif s3_mc.current_partner == "Harry":
                harry "Woah."
                "As you move your hips [s3_mc.current_partner]'s breath quickens."
                harry "Oh, woah."
            elif s3_mc.current_partner == "AJ":
                aj "Woah."
                "As you move your hips [s3_mc.current_partner]'s breath quickens."
                aj "Oh, woah."

            # CHOICE
            menu:
                thought "I should..."
                "Go lower":
                    pass
                "Go higher":
                    pass
                "Go deeper":
                    pass
                
            "You move slowly on top of [s3_mc.current_partner], trying not to dismantle the tent in the process."

    "Outside, you hear the rustling of the other tents."

    if s3_mc.current_partner == "Bill":
        "Bill pulls you closer and moans into your ear."
        bill "Let's give the others a proper show."
        "He rolls you onto your back and kisses your neck."
    elif s3_mc.current_partner == "Camilo":
        "He kisses you, hard."
        camilo "I wish it was just us right now."
        camilo "I would be so much louder if it was."
    elif s3_mc.current_partner == "Harry":
        harry "Oops."
        harry "I'll try and be a little bit quieter..."
    elif s3_mc.current_partner == "AJ":
        aj "This is so hot."
        aj "Don't let anything distract you."

    "You start to explore [his_her] body with your lips and tongue."
    "[s3_mc.current_partner] moans slightly louder than you expected."

    if s3_mc.current_partner != "AJ":
        elladine "Can someone turn it down?"
        elladine "Some of us are trying to sleep!"
    else:
        seb "Can someone turn it down?"
        elladine "Yeah, some of us are trying to sleep!"

    iona "Not all of us."

    $ leaving("elladine")
    $ leaving("iona")

    "You roll off [s3_mc.current_partner] and lie back in a fit of laughter."

    if s3_mc.current_partner == "Bill":
        bill "Oops."
    elif s3_mc.current_partner == "Camilo":
        camilo "Oops."
    elif s3_mc.current_partner == "Harry":
        harry "Oops."
    elif s3_mc.current_partner == "AJ":
        aj "Oops."

    "You cuddle up next to each other."
    "[s3_mc.current_partner]'s heat radiates around you."

    if s3_mc.current_partner == "Bill":
        bill "That was pretty intense."
        s3_mc "Because we're in tents?"
        bill "Yeah. I know. Weak."
        "You roll your eyes and hit [him_her] with a pillow."
        bill "Nah, I'm kidding."
        "[s3_mc.current_partner] sounds a little out of breath."
        bill "No jokes about that."
        bill "That was amazing."
        s3_mc "I know, I try."
        "[s3_mc.current_partner] rolls onto [his_her] side and kisses your cheek."
        bill "You don't even have to try, babe."
        bill "You're always amazing."
    elif s3_mc.current_partner == "Camilo":
        camilo "That was pretty intense."
        s3_mc "Because we're in tents?"
        camilo "Yeah. I know. Weak."
        "You roll your eyes and hit [him_her] with a pillow."
        camilo "Nah, I'm kidding."
        "[s3_mc.current_partner] sounds a little out of breath."
        camilo "No jokes about that."
        camilo "That was amazing."
        s3_mc "I know, I try."
        "[s3_mc.current_partner] rolls onto [his_her] side and kisses your cheek."
        camilo "You don't even have to try, babe."
        camilo "You're always amazing."
    elif s3_mc.current_partner == "Harry":
        harry "That was pretty intense."
        s3_mc "Because we're in tents?"
        harry "Yeah. I know. Weak."
        "You roll your eyes and hit [him_her] with a pillow."
        harry "Nah, I'm kidding."
        "[s3_mc.current_partner] sounds a little out of breath."
        harry "No jokes about that."
        harry "That was amazing."
        s3_mc "I know, I try."
        "[s3_mc.current_partner] rolls onto [his_her] side and kisses your cheek."
        harry "You don't even have to try, babe."
        harry "You're always amazing."
    elif s3_mc.current_partner == "AJ":
        aj "That was pretty intense."
        s3_mc "Because we're in tents?"
        aj "Yeah. I know. Weak."
        "You roll your eyes and hit [him_her] with a pillow."
        aj "Nah, I'm kidding."
        "[s3_mc.current_partner] sounds a little out of breath."
        aj "No jokes about that."
        aj "That was amazing."
        s3_mc "I know, I try."
        "[s3_mc.current_partner] rolls onto [his_her] side and kisses your cheek."
        aj "You don't even have to try, babe."
        aj "You're always amazing."

    jump s3e4p3_ending
    return

label s3e4p3_stay_up_bill:
    "Bill takes your hands in his and pulls you towards him, so close you can count his eyelashes."

    # CHOICE
    menu:
        thought "I'm so close to Bill..."
        "Kiss him fast":
            "You lean in and press your lips against his, clutching at his stubbled jaw."
            "He returns the kiss with the same passion as his hands run down your body."
        "Kiss him slow":
            "You brush your lips against his. He leans into it, but you pull back until you're only just maintaining contact."
            "You control the pace and he follows your lead until you're kissing fully and deeply. His hands run down your body."
        "Cuddle up to him":
            "You turn and press your head into his chest. It's warm and firm and you can hear his heart beating."
            "Bill lightly strokes your arm with his hand."

    s3_mc "I like your hands."
    bill "Grew them myself."
    s3_mc "Good job. They feel very...reliable."
    bill "They've gotta be. I'm a roofer, after all."
    bill "And I like to make stuff."
    bill "My granddad's a cabinet maker, and we sometimes make furniture together."
    s3_mc "Like, from scratch?"
    bill "Yup. We'd just finished a piano stool before I came here."
    bill "He knows a guy, who knows a guy, who gets decent timber for cheap. It's great to be around him."

    # CHOICE
    menu:
        thought "Bill makes furniture with his grandad..."
        "That's really sweet":
            "You stroke his fingers with yours."
            s3_mc "I think it's adorable."
            bill "I don't know about that, but I do really enjoy spending time with the old fella."
            bill "And it's not just that he's got good stories or bants, or whatever."
            bill "He's a solid person."
            bill "His head's bursting with common sense."
            s3_mc "That's exactly what I was picturing."
            s3_mc "I can imagine you being like that when you're old."
            s3_mc "Dispensing wisdom to the young'uns."
            "He smiles broadly."
            s3_mc "That's the dream, innit?"
        "What else can you do with your hands?":
            "You stroke his fingers with yours."
            s3_mc "What else can you do with your hands?"
            bill "Is there something in particular you want me to do?"
            "You wink."
            s3_mc "There might be."
            bill "Just to be clear, we're talking about sex, right?"
            s3_mc "You're so upfront, I love it."
            s3_mc "Yes, we're talking about sex."
            "He grins."
            bill "Good to know we're on the same page."
        "Does your dad ever help?":
            bill "My dad's not much of a woodworker. He'd sometimes take me round to his plumbing jobs, though."
            bill "He and my grandad have these big long arguments about whether plumbing or carpentry was harder."
            bill "It's all in good fun. Just their way of saying 'I love you'."
            s3_mc "So, that's where you get it from."

    s3_mc "What's your favourite thing you've ever made?"
    "He thinks about it for a moment."
    bill "Let me see..."
    bill "It'd have to be the spice rack we made."
    s3_mc "Erm...it took two of you to make a spice rack?"
    bill "It was the first thing my granddad showed me how to make. We didn't used to speak much before that."
    bill "He really warmed up showing me all the proper tools and stuff."
    bill "The spice rack is useless, obviously, but it was all about spending time together. We're proper mates now."
    s3_mc "That's lovely. But what did you mean by 'it's useless'?"
    bill "Well, most spices are unnecessary, you know?"
    bill "All you need is salt, pepper, curry powder, oregano and cinnamon. Everything else is just showing off."

    # CHOICE
    menu:
        thought "Bill thinks most spices are unnecessary..."
        "Agree with him":
            s3_mc "Tell me about it. Everything these days is cumin this, fennel that. It's just not necessary."
            bill "I knew you'd get it!"
            bill "Wait, are you taking the piss?"
            s3_mc "Not at all!"
            bill "Oh, good."
        "Argue the point":
            s3_mc "Doesn't that exclude like 90% of the world's cuisine?"
            bill "Might do, but it works for me."
            s3_mc "But you could be really missing out!"
            bill "It's never really bothered me..."
            s3_mc "One day I'm going to try and change your mind."
            s3_mc "There are some cracking spices out there."
            "He thinks for a moment. You can almost see the wrestling match going on inside his head."
            bill "Yeah, sure. Why not?"
            s3_mc "Great."
            bill "I wouldn't do this for anyone else, you know?"
        "Laugh it off":
            s3_mc "You and your opinions!"
            s3_mc "I feel like a fish that doesn't see the bait until it's been hooked."
            s3_mc "Or maybe it's something else that's got me hooked."
            "You put your arms around him."

    "He puts his arms around you and gives you a squeeze."

    return

label s3e4p3_stay_up_harry:
    "Harry smoothes out his hair with one hand. His biceps bulge pleasingly."
    harry "Alone again..."

    # CHOICE
    menu:
        thought "Alone with Harry..."
        "Kiss him":
            "You close the distance between you and brush your fingers down the side of his face."
            harry "H-"
            "Before he can start talking, you put a finger to his lips, then lean in and kiss him."
            "His arms envelop you. You melt into each other's lips and for a few moments, that's all there is."
        "Tell him to kiss you":
            "You gaze at him seductively."
            s3_mc "Kiss me."
            "He wastes no time in moving towards you, kissing you hard on the mouth. He softly bites your lower lip."
            "His arms envelop you. You melt into each other's lips and for a few moments, that's all there is."
        "Admire his body a bit more":
            "He chuckles softly."
            harry "What?"
            s3_mc "Just admiring the view."
            "Harry smiles confidently and flexes a little more."
            "You fan yourself."
            s3_mc "Could you be any hotter?"

    harry "When I'm with you, I feel like the coolest guy in the world."
    harry "Like a super-spy. 'The name's Zhōng. Harry Zhōng.'"

    # CHOICE
    menu:
        thought "Harry feels like a secret agent when he's with me..."
        "You don't have the snappiest name for it":
            # NEED TO FILL
            "EMPTY"
        "Do I get to be a spy too?":
            harry "Of course! Harry and [s3_name] a crime-fighting, super-spying duo."
            harry "We can both get proper sweet tuxedos."
            s3_mc "Or we could both wear sleek, sexy silk dresses."
            harry "Do you think I could pull it off?"
            s3_mc "I think you'd rock it."
        "Does that make me the femme fatale?":
            harry "I'm not sure I'd last very long if you were the enemy."
            harry "I'd be like 'see ya MI6, I'm off to join [s3_name] and take over the world'."
            "You pretend to pout."
            s3_mc "So you wouldn't even put up a fight?"
            "You run a finger slowly down his chest."
            s3_mc "Shame."
            "Harry grins."
            harry "Maybe just for show."

    s3_mc "Oh, you know what else spies have?"
    s3_mc "Cool gadgets."
    harry "Like a pen that's also a smoke bomb!"

    # CHOICE
    menu:
        s3_mc "Or a..."
        "Lighter":
            pass
        "Water bottle":
            pass
        "Torch":
            pass

    # CHOICE
    menu:
        s3_mc "That's also a..."
        "Tranquiliser dart":
            pass
        "Poison dispenser":
            pass
        "Laser":
            pass

    harry "I dunno, sounds... dangerous."
    s3_mc "That's the point!"
    harry "I meant dangerous for you."
    harry "I can see a hundred ways it could go wrong..."
    harry "Besides, you're forgetting the best gadget of all."
    s3_mc "What's that?"
    harry "The one in my pants."

    # CHOICE
    menu:
        s3_mc "That was... "
        "Confusing":
            # NEED TO FILL
            "EMPTY"
        "Sexy":
            harry "What would a spy be without his dry wit?"
            s3_mc "'Dry wit' might be pushing it, babe."
        "Hilarious":
            harry "Hmm, I was going for 'suave'."
            harry "But hilarious is a decent runner-up prize."
            s3_mc "It's actually the first prize."

    "You both laugh."

    return

label s3e4p3_stay_up_camilo:
    "Camilo runs his fingers down your arm and looks into your eyes. He winks."

    # CHOICE
    menu:
        thought "He looks good..."
        "Tease him":
            # NEED TO FILL
            "EMPTY"
        "Kiss him":
            "You lean in and kiss him, feeling his strong arms wrap around you and pull you in tighter."
            "The subtle, spicy scent of his aftershave washes over you."
            camilo "You're bloody fantastic."
            s3_mc "You're pretty great yourself."
        "Tease him and then kiss him":
            "You stroke his hair, and when he leans in for a kiss, you kiss his forehead."
            camilo "Keeping me on my toes?"
            "You respond by grabbing his chin and pulling him in for a fierce, passionate kiss."
            camilo "Whew, mamacita. That was amazing."

    "Camilo twirls a bit of your hair in his finger."
    camilo "[s3_name], can I ask a question?"
    s3_mc "Sure."
    camilo "Did you worry about coming in here? The Villa, I mean."
    s3_mc "In what way?"
    camilo "Well, like leaving your family behind."

    # CHOICE
    menu:
        thought "Was I worried about leaving my family?"
        "Not at all":
            s3_mc "I hadn't really thought about it, if I'm honest."
            s3_mc "I guess I don't have that kind of relationship with them."
            camilo "But won't they miss you?"
            s3_mc "Maybe?"
            s3_mc "But I'm sure they'll last a summer without me!"
        "Maybe my grandparents":
            s3_mc "Yeah, my grandparents especially."
            camilo "I get that. Mine are in Colombia and I miss them a lot."
            s3_mc "But the rest of my family will be fine without me for a summer!"
        "Yeah, definitely":
            s3_mc "Totally. I was a bit of a mess at the airport, haha!"
            camilo "I knew you'd feel me."
            camilo "I think about mine every day. Wondering how they're getting on and that."

    s3_mc "You're really close with yours, right?"
    camilo "Yeah, but more than that, they really depend on me."
    camilo "What with my dad being ill, and me being the oldest kid..."
    camilo "I dunno, I just feel really responsible for everyone."

    # CHOICE
    menu:
        thought "Camilo feels responsible for his family..."
        "I'm sure they appreciate it":
            s3_mc "They're really lucky to have you."
            s3_mc "I'm sure they appreciate everything you do."
            camilo "Yeah... It doesn't feel that way all the time."
            camilo "Don't get me wrong, I love my family to bits, but sometimes it feels like it's just one thing after another, you know?"
        "That's really noble":
            s3_mc "I admire that. I like a man who takes care of his family."
            camilo "It's not like I'm some kind of hero, though."
            camilo "I just did what had to be done. There wasn't anyone else to step up after my dad got sick."
            s3_mc "That takes courage."
            camilo "Maybe. I hadn't really thought about it, if I'm honest."
        "That must be tough":
            s3_mc "That's gotta be tough on you."
            "He shrugs."
            camilo "I dunno, I never thought about it really."
            camilo "After my dad got sick, I was the one who had to step up."
            camilo "Just the way it goes, innit."

    camilo "Just the way it goes, innit"
    "You put your arms around his neck. You feel the hard muscles in his shoulders relax a little."
    s3_mc "Well, I'm definitely glad you came here, mister."
    camilo "Yeah, lucky you, eh?"
    s3_mc "Seriously, though. You deserve to have a bit of fun and be happy."
    camilo "You're a big part of that, [s3_name]."
    s3_mc "Which one? Having a bit of fun or being happy?"
    camilo "Huh? Which one? What do you-"
    camilo "Oh, you're taking the mickey."
    camilo "You're bad!"
    s3_mc "I try."

    return

label s3e4p3_stay_up_aj:
    aj "I can't tell if you're sending me kiss-you-right-now signals or not..."

    # CHOICE
    menu:
        thought "Am I sending signals telling AJ to kiss me?"
        "Nah, I don't want to right now":
            # NEED TO FILL
            "EMPTY"
        "Yes! Kiss me, AJ":
            s3_mc "Yeah, I am!"
            s3_mc "Kiss me, AJ!"
            "She closes her eyes and leans in to kiss you."
            "You kiss passionately, your hands bring her closer towards you."
            "It is urgent and frantic. You can't get enough of each other. You can't get close enough."
            "She pulls away, you're both breathless."
            s3_mc "That was..."
            aj "Yeah..."
            aj "That was some kiss."
            aj "Wow."
            "She smiles, catching up with her breath."
            aj "You take my breath away, [s3_name]."
            aj "I'm normally awful at reading signals so I'm glad I got this one right."
        "Pucker your lips and kiss her":
            aj "I'll take that as a yes."
            "You lean in to kiss her."
            "You kiss passionately, your hands bring her closer towards you."
            "It is urgent and frantic. You can't get enough of each other. You can't get close enough."
            "She pulls away, you're both breathless."
            s3_mc "That was..."
            aj "Yeah..."
            aj "That was some kiss."
            aj "Wow."
            "She smiles, catching up with her breath."
            aj "You take my breath away, [s3_name]."
            aj "I'm normally awful at reading signals so I'm glad I got this one right."

    aj "I think flirty signals just fly right past me sometimes."
    aj "Do you notice it when people flirt with you?"

    # CHOICE
    menu:
        thought "Do I pick up on flirty vibes?"
        "Are you flirting with me right now?":
            # NEED TO FILL
            "EMPTY"
        "Yeah, I can always tell":
            aj "I wish I had that."
        "No one flirts with me":
            aj "Don't be silly. I know people flirt with you, [s3_name]!"
            aj "I'm one of them."

    aj "My friends always tease me and say they don't want to take me out of goal because I'm, like, so oblivious to obvious passes."
    aj "Even though I'm apparently a really big flirt."
    aj "How can you tell if someone likes you or not?"

    # CHOICE
    menu:
        thought "How can I tell if someone is into me?"
        "Cast a spell":
            # NEED TO FILL
            "EMPTY"
        "Body language":
            s3_mc "It's all about the body language."
            aj "Really?"
            aj "What should I look out for?"
            s3_mc "If it's open and they're leaning towards you that's a good sign."
            aj "Open like when someone's on the field and you pass the ball to them?"
            s3_mc "Yeah, that works."
        "Just ask them":
            aj "Yeah, to be honest, that's the way I usually go about it."
            aj "If I like them, I don't want to hang around waiting for them to maybe make a move."

    aj "At least with us it's pretty clear how we feel about each other."
    aj "I much prefer uncomplicated and straightforward things, do you get me?"

    # CHOICE
    menu:
        thought "AJ likes things to be simple..."
        "I love the thrill of the chase":
            # NEED TO FILL
            "EMPTY"
        "I'm just a simple love machine":
            $ s3_mc.like("AJ")
            aj "Me too!"
        "I've been told I can be a bit chaotic":
            aj "Oh, well, life can make us a bit like that sometimes."

    aj "And you know what?"
    aj "I'm totally dating my fantasy."

    return

label s3e4p3_ending:
    scene black with dissolve
    $ on_screen = []

    "Something rattles the sides of your tent, waking you up from your slumber."

    scene s3-inside-tent-standard-night with dissolve
    $ new_scene()

    genevieve "Psst."
    genevieve "[s3_name]?"
    "Genevieve pokes her head through the door."
    genevieve "Um, hun..."

    # CHOICE
    menu:
        thought "Genevieve?"
        "Give us some privacy":
            # NEED TO FILL
            "EMPTY"
        "Are you alright?":
            s3_mc "What's up, hun?"
        "I thought you were the demon!":
            "You back away a little."
            genevieve "I'm not the demon!"
            genevieve "But..."
        "Sorry, were we too loud?" if s3e4p3_tent_bits:
            genevieve "I mean, earlier, yeah. You were pretty loud."
            s3_mc "Oops, my bad."
            genevieve "It's chill, hun, I don't blame you for wanting to take advantage of this alone time."
            genevieve "But that's not what I was coming over here for."

    genevieve "Sorry, I just could have sworn I heard something, like, moving around out here."
    s3_mc "It could have been a bird or the wind."
    genevieve "Yeah. A bird."
    s3_mc "Or maybe one of the others had to go to the loo?"
    genevieve "You're probably right. I just hate how quiet and dark it is."
    genevieve "Anyway."
    genevieve "I'll leave you to your sleep..."
    "Genevieve reluctantly pops her head out of the tent."
    $ leaving("genevieve")

    thought "Hmm..."
    thought "I wonder what she heard?"

    "While these lot are all going bump in the night, I've made my own campsite on my floor for me, myself and I."
    "I don't have any sausages and beans though."
    "But I've got my floor."
    "And you know what? The floor is so supportive."
    "It's not like walls. It's there for you right where you need it."
    "Walls are always getting in my way."
    "Anyway, let's leave our Islanders 'sleeping' outside."

    scene sand with dissolve
    $ on_screen = []

    "Coming up..."
    "The Islanders are in for a few surprises."
    genevieve "Wait, those weren't there when we went to bed."
    genevieve "Who is in those tents?"
    $ leaving("genevieve")

    "Maybe a shiny demon?"
    "They're quite rare, actually."

    jump s3e5p1

    return