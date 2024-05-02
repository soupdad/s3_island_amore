#########################################################################
## Episode 1, Part 1
#########################################################################
label s3e1p1:

    scene sand

    show screen day_title(1, 1) with Pause(4)
    hide screen day_title with dissolve

    menu:
        "Have you played this game before?"
        "I'm a seasoned pro":
            $ s3_hints = False
        "I want some hints please":
            $ s3_hints = True

    "Finding love can be tough..."
    "Daily life is nothing but work, sleep, and repeat..."
    "How are you supposed to have time to search for that special someone?"
    "It's time to get off social media, and find love the old-fashioned way..."
    "On a reality TV show!"
    "You've been invited to a place where everything is different..."
    "A place where all you have to do all day is meet beautiful people, couple up, and fall in love..."
    "A place called Island Amore."

    scene s3-outside-villa-wide-shot-day
    with dissolve
    "We've taken a gorgeous Villa in a hot country and filled it with sexy singles."

    scene s3-lounge
    with dissolve
    "To stay in the Villa, they'll have to get together, and stay together."

    scene s3-bedroom-day
    with dissolve
    "And if they do find love, one lucky couple will also pocket fifty thousand pounds,"

    scene s3-hideaway-night
    with dissolve
    "But it won't be easy. We're going to throw in twists, turns, and challenges to see if their love can survive."

    scene s3-firepit-night
    with dissolve
    "Who will find eternal bliss, and who will find themselves on a plane home?"
    "Let there be love."

    ## MC Look Customizer Here
        # Defines name and maybe clothes and appearance if we get the images
    # Uncomment below once actually initializing, and change s3_name in characters.rpy to "You"

    $ bad_name = True

    while bad_name:
        $ s3_name = renpy.input("What do you want to be called?", length = 30)
        $ s3_name = s3_name.strip()
        if len(s3_name) == 0:
            "Sorry, you're name must be something. Try again :)"
        else:
            menu:
                "Your name is '[s3_name]'. Is this correct?"
                "Yes":
                    $ bad_name = False
                "No, please I need to change it":
                    "Ok, we are merciful."

    scene s3-outside-villa-entrance
    with dissolve

    "Your heel click on the driveway as you stride up to the Villa."

    thought "It's gorgeous!"
    thought "I can't believe this is going to be my home for the next two weeks!"
    thought "Unless I go home early."
    thought "I wonder where everybody is?"

    "A girl peeks her head out of the entrance."

    show elladine at npc_center

    "She yells in excitement when she sees you."

    elladine @ talk "Hey! You made it!"
    elladine @ happy "It's so nice to meet you! I'm Elladine."

    window hide
    show screen s3_character_profile("elladine") with Pause(3)
    hide screen s3_character_profile with dissolve

    # solo portrait shot of elladine
    "{i}Elladine\n
    -25, from Cardiff\n
    -Glassblower\n
    -Heard every 'blowing' joke a hundred times already{/i}"

    if s3_hints:
        "You're about to make your first choice. The islanders will remember what you say and might change their opinions of you, so choose carefully!"

    # CHOICE
    menu:
        s3_mc "I'm [s3_name]"
        "It's nice to meet you too":
            $ s3_mc.like("Elladine")
            s3_mc "I think we're the first ones here!"
            elladine "Amazing. This is one of those moments you remember forever, isn't it?"
            s3_mc "I think so!"
            elladine @ happy "I know we will."

        "Wow, I love your outfit":
            $ s3_mc.like("Elladine")
            s3_mc "It's stunning!"
            elladine @ happy "Babes, I was about to say the same to you!"
            elladine @ talk "Seriously. You've already set the bar super high."
            elladine @ happy "The boys are going to freak when they see us."

        "Warning, I'm here to win":
            $ s3e1p1_warning_here_to_win = True
            $ s3_mc.dislike("Elladine")
            s3_mc "Before we go getting too friendly, you need to know one thing about me."
            show elladine serious
            s3_mc "I'm here to find love, and I don't care how many toes I have to tread on to get it."
            s3_mc "So if you're tempted to cross me at some point while we're here..."
            s3_mc "Don't."
            s3_mc "Understood?"
            elladine @ sad "Um, sure. Understood."

    elladine @ sad "I've been feeling well nervous ever since I got here."
    elladine -serious "I mean it's exciting, but it's also a lot of pressure, isn't it?"

    # CHOICE
    menu:
        thought "How am I feeling?"
        "So nervous":
            s3_mc "I've never done anything like this before. It's a bit scary."
            elladine @ talk "At least we're all in the same boat!"

        "Just excited":
            s3_mc "I'm really excited to meet everyone!"

        "Kinda hungry":
            $ s3e1p1_feeling_hungry = True
            elladine awkward "You mean, like...hungry for love, or..?"
            s3_mc "Nope. Just hungry."
            elladine "Sounds like you need a snack."
            elladine happy "I hope there are some snacks lined up for us outside!"
            s3_mc "Why would there be snacks outside?"
            elladine @ talk "I mean like hot guys when you see someone hot and you say 'he's a snack'."
            s3_mc "That's not what I meant, though. I'm just hungry."
            s3_mc "I wish I had a banana or something."
            "Elladine looks like she's about to make another joke, but then decides against it."

    s3_mc "Are there any other girls here yet?"
    elladine "Only one. We've been waiting in the bedroom."
    elladine very_happy "Come on. I'll introduce you."

    scene s3-bedroom-day with dissolve
    $ on_screen = []

    "Elladine leads you into the bedroom, where another girl is waiting."
    "Her jaw drops when you walk in."

    aj @ awkward "Are you the new arrival?"
    aj @ sad "Man, I knew everyone here was gonna be gorgeous, but I wasn't prepared..."
    elladine @ talk "Stop staring and introduce yourself!"
    aj @ happy "Sorry, sorry!"
    aj "My name's AJ. It's nice to meet you."

    # solo portrait shot of aj
    window hide
    show screen s3_character_profile("aj") with Pause(3)
    hide screen s3_character_profile with dissolve

    "{i}AJ\n
    -21, from Bath\n
    -Professional hockey player\n
    -Knows how to handle a stick{/i}"

    s3_mc "I'm [s3_name]"
    if s3e1p1_warning_here_to_win == True:
        elladine @ sad "She, um.. she definitely means business."
    else:
        elladine "We were just talking outside. She's really nice."

    aj @ talk "I hope everyone's going to be cool. I don't want to get sucked into a load of drama."
    aj "I mean, we're all here to have fun, right?"

    # CHOICE
    menu:
        thought "AJ's here to have fun, not to get into drama..."
        "Me too! Let's keep it chill and friendly":
            $ s3_mc.like("AJ")
            s3_mc "Trust me, we're gonna have a great time."
            s3_mc "You're my girls now, and I don't let my girls turn on each other."
            aj @ very_happy "Yes! I'm so glad you said that."

        "But there's no fun without drama":
            s3_mc "It's so exciting when someone does something totally shocking, and you just know the fallout is gonna be huge."
            s3_mc "I can't wait to stir up some trouble around here."
            aj @ serious "Fair play! I guess we just have different priorities."
            aj "Friendship is really important to me."

        "I don't care, as long as I get what I want":
            $ s3_mc.dislike("AJ")
            s3_mc "I don't set out to create drama. But I will if I have to."
            s3_mc "At the end of the day, it's not called Friend Island."
            aj @ serious "Fair play! I guess we just have different priorities."
            aj "Friendship is really important to me."

    aj "That's what I love about my teammates back home."
    aj "We never mess around arguing about who passed the ball to who, or whatever. We just get on with it."
    aj @ happy "I want you all to be like my new teammates while we're here."


    # CHOICE (assigns your job)
    menu:
        elladine "What do you do on the outside, [s3_name]?"
        "Model":
            $ s3_mc.job = 'Model'
            aj @ talk "I knew it! As soon as you walked in, I was like, I bet she's a model."
            elladine @ talk "Yeah, I can't say I'm surprised either."
        "Scientist":
            $ s3_mc.job = 'Scientist'
            aj @ talk "Oh wow, that's really cool!"
            aj @ talk "It's not fair that someone as pretty as you gets to be smart as well."
        "Musician":
            $ s3_mc.job = 'Musician'
            elladine @ happy "I love musicians. If I find out one of the boys is in a band, I'm going to make a beeline straight for him."
        "Athlete":
            $ s3_mc.job = 'Athlete'
            aj @ talk "Snap!"
            aj @ very_happy "I knew I felt a connection with you as soon as you walked in here."


    "Suddenly, you hear a beeping noise."
    s3_mc "What was that?"
    elladine @ talk "It sounded like a text..."
    "AJ checks her phone and gasps."
    aj @ talk "Oh, it's me!"
    aj @ very_happy "I've got a text!"

    text "Girls, it's time to start meeting the boys. AJ, please make your way to the lawn and choose a boy to couple up with. Elladine and [s3_name], stand by in the bedroom. You'll be up next! #girlmeetsboy #getthepartystarted"

    aj "What? But the other girls still haven't arrived yet!"
    elladine @ awkward "I guess they'll be coming in later?"
    aj @ talk "I'd better go, then."
    aj "I'll see you out there, guys."
    elladine "Good luck!"

    "AJ races out of the bedroom. Her heels clack all the way to the lawn."

    show aj at npc_exit
    pause 0.3
    $ renpy.hide("aj")
    $ on_screen.remove("aj")
    
    elladine "She's got a lot of energy, hasn't she?"
    elladine @ awkward "I guess it's hard not to be excited when you know you're picking first."
    s3_mc "I wonder what the boys will be like?"
    elladine @ happy "I want a guy who's been around the block a bit, you know?"
    elladine @ happy "Someone who knows what he's about and takes it seriously."
    elladine "What about you? What's your type?"

    # CHOICE
    menu:
        thought "My type is..."
        "Funny and cute":
            s3_mc "I just want a boy to make me smile."
            elladine "Aw, I hope you find him, babes."

        "Smart and mature":
            s3_mc "I agree with you. I need a guy with a good head on his shoulders."
            elladine "Aw, I hope you find him, babes."

        "Whatever, as long as they're hot":
            s3_mc "Personality will never be as important as looks for me."
            elladine "Ha, lucky for you!"

    elladine "We won't have much time to chat before we choose, so we'll mostly be going off looks."
    elladine "And speaking of boys..."
    "She gestures to a box of condoms on a nearby table and giggles."
    elladine flirt "I guess we'll be needing a lot of those in the house, won't we?"


    # CHOICE
    menu:
        thought "Am I going to need the condoms?"
        "I'm not planning to have sex in here":
            s3_mc "Don't get me wrong, I love having sex...but not on TV!"
            s3_mc "I don't want all my family and friends to see me!"
            elladine @ awkward "Good point."

        "I'll take one now, just in case":
            "You take a single condom and hide it in your bikini for later."
            "Elladine giggles again."
            elladine @ very_happy "You go, girl!"

        "Grab a whole handful":
            $ s3e1p1_grab_some_condoms = True
            "You take a fistful of condoms and stuff them down your top."
            "Elladine giggles again."
            elladine @ very_happy "You go, girl!"

    elladine "I'm going to hold off for now."
    elladine "I probably won't do any big bits right away..."
    elladine -flirt "Unless the right guy comes along, obvs."
    elladine @ talk "Text! I think that means it's my turn!"
    "She gives you a quick hug before heading to the door."
    elladine "Good luck, [s3_name]. I'll see you down there."

    "She hurries towards the lawn, leaving you alone."

    show elladine at npc_exit
    pause 0.3
    $ renpy.hide("elladine")
    $ on_screen.remove("elladine")

    thought "There's still only three girls here!"
    thought "I wonder when the others will be arriving?"
    "You sit down on one of the beds. It's soft and springy."


    # CHOICE
    menu:
        thought "These beds are really comfy..."
        "Perfect for snuggling":
            thought "I can't wait till find someone to cuddle up to."
        
        "Perfect for doing bits":
            thought "I'm gonna have so much fun, the whole Villa will shake."
        
        "Maybe I'll take a nap...":
            $ s3e1p1_took_a_nap = True
            thought "Just a little one couldn't hurt..."
            "You lay your head on the pillow and close your eyes."
            "Maybe my Prince Charming will come and wake me with a kiss."
            "You drift off for a few minutes, but then..."

    "Your phone beeps."
    thought "Wait, is it my turn already?"

    text "[s3_name], come down to the lawn and couple up! The boys are waiting..."

    thought "Alright, let's do this!"

    scene s3-lawn-day with dissolve
    $ on_screen = []

    "You step out into the brilliant sunshine."
    "Waiting on the lawn are three boys, standing in a line."
    "Elladine and AJ are off to the side, already paired up with their boys."

    "Elladine shoots you an encouraging smile, and AJ gives you a thumbs up."

    "Those two have already picked their boys..."
    "Which leaves these three for me to choose from."
    thought "I wonder which one I should pick?"

    "The first boy steps forward with a cheeky smile."

    # Meeting Bill
    bill @ flirt "Alright, beautiful? I'm Bill."

    # solo portrait shot of bill
    window hide
    show screen s3_character_profile("bill") with Pause(3)
    hide screen s3_character_profile with dissolve

    "{i}Bill\n
    -24, from Surrey\n
    -Roofer\n
    -Strong opinions about sandwiches{/i}"

    bill happy "I'm gonna come right out and say it. You look like a bit of me."

    # CHOICE
    menu:
        thought "Bill says I'm a bit of him..."
        "Smile politely":
            "You smile at Bill, trying not to give too much away."
            "I'm definitely in there."
        
        "Wink at him":
            $ s3_mc.like("Bill")
            show bill very_happy
            "You shoot a wink in Bill's direction and his face lights up."
        
        "Roll your eyes":
            $ s3_mc.dislike("Bill")
            show bill sad
            "You roll your eyes at Bill and his face falls."

    show bill at npc_exit
    pause 0.3
    $ renpy.hide("bill")

    "You look down the line to the next boy."

    show camilo at npc_center
    camilo @ flirt "Hola chica. Welcome to the Villa. Amazing, isn't it?"
    s3_mc " Is it?"
    camilo @ happy "Well, it is now you're here."

    # solo portrait shot of camilo
    window hide
    show screen s3_character_profile("camilo") with Pause(3)
    hide screen s3_character_profile with dissolve

    "{i}Camilo\n
    -23, from Romford\n
    -Runs the family shop\n
    -A blackbelt in grafting (and Brazilian jiu-jitsu){/i}"

    camilo awkward "Sorry. That was really cheesy."
    camilo "It's just, I think me and Bill had the exact same reaction..."
    camilo happy "So I thought I should try and fancy it up a bit."

    # CHOICE
    menu:
        thought "Camilo definitely likes me..."
        "The feeling is mutual":
            $ s3_mc.like("Camilo")
            show camilo flirt
            "You give Camilo a dazzling smile and feel the chemistry crackling between you two."
            "I can't wait to get to know this one better."
        
        "It's too early to say":
            "You shrug and look away."
        
        "More like Camil-no":
            $ s3_mc.dislike("Camilo")
            show camilo sad
            "Camilo deflates a little when he sees you're not into him."
            camilo "Oh..."

    show camilo at npc_exit
    pause 0.3
    $ renpy.hide("camilo")

    "The third and final boy in the line seems nervous."
    "You raise your eyebrows at him and he smiles, trying to puff out his chest a bit."

    show harry at npc_center
    harry @ flirt "Hey, I'm Harry."

    # solo portrait shot of harry
    window hide
    show screen s3_character_profile("harry") with Pause(3)
    hide screen s3_character_profile with dissolve

    "{i}Harry\n
    -21, from York\n
    -Business student\n
    -Usually wears a tie with his swimsuit{/i}"

    harry @ happy "For what it's worth, I'm just as gobsmacked as these other two."
    harry "But I won't try to sway you. You've got to listen to your gut."
    harry awkward "Or your heart. Or, like whatever part of your body you trust to make these decisions."

    # CHOICE
    menu:
        thought "I think Harry's trying to flirt with me, too..."
        "It's working!":
            $ s3_mc.like("Harry")
            show harry awkward
            "You give Harry a flirty smile. He blushes hard."
            show harry flirt
            "He's definitely got my attention."
        
        "Bless his heart":
            "Cute, but I'm not sure he knows what he's doing."
        
        "Ugh, no thanks":
            $ s3_mc.dislike("Harry")
            show harry sad
            "You frown, leaving Harry looking embarrassed."

    show harry at npc_exit
    pause 0.3
    $ renpy.hide("harry")
    $ on_screen = []

    "Alright, so these three guys are my options for now."
    "It seems like they're all keen."
    "It's so tough to pick a boy when you know so little about them!"
    "I know more boys might come in later in the series, and I'll get chances to change who I'm coupled up with..."
    "...but for now, whoever I pick is the person I'm probably going to spend the most time with early on."
    "I hope they're all as good as they seem!"

    # CHOICE (appends who you're coupled up with to list)
    # add screen that shows the 3 guys lined up, full body profile shot, and you click on the one you want
    menu:
        thought "Who should I couple up with?"
        "Bill":
            $ s3_mc.past_partners.append("Bill")
            $ s3_mc.current_partner = "Bill"
            $ s3_mc.like("Bill")
            $ s3_mc.like("Bill")
            s3_mc "The boy I want to couple up with is... Bill!"
            "You stride over to Bill."
            "He grins like he can't hardly believe his luck."
            bill happy "Nice one."

        "Camilo":
            $ s3_mc.past_partners.append("Camilo")
            $ s3_mc.current_partner = "Camilo"
            $ s3_mc.like("Camilo")
            $ s3_mc.like("Camilo")
            s3_mc "The boy I want to couple up with is... Camilo!"
            "You stride over to Camilo."
            "He grins like he can't hardly believe his luck."
            camilo happy "Nice one."

        "Harry":
            $ s3_mc.past_partners.append("Harry")
            $ s3_mc.current_partner = "Harry"
            $ s3_mc.like("Harry")
            $ s3_mc.like("Harry")
            s3_mc "The boy I want to couple up with is... Harry!"
            "You stride over to Harry."
            "He grins like he can't hardly believe his luck."
            harry happy "Nice one."

    $ s3_3rd_girl = s3_3rd_girl_options[s3_mc.current_partner]

    menu:
        thought "Me and [s3_mc.current_partner] are officially coupled up..."
        "Hug him":
            "As you reach him, you throw your arms around his shoulders."
            "He hugs you back firmly. His hands are warm on the small of your back."
        "Kiss his cheek":
            "As you reach him, you plant a kiss on his cheek, being careful not to smudge your lipstick."
        "Hands off for now":
            "You stand politely at his side, just close enough for your elbows to brush."

    # IF STATEMENT
    if s3_mc.current_partner == "Bill":
        bill "I'm so glad you picked me."
        s3_mc "Did I make the right decision?"
        bill @ flirt -happy "Definitely. But I would say that, wouldn't I?"
    elif s3_mc.current_partner == "Camilo":
        camilo "I'm so glad you picked me."
        s3_mc "Did I make the right decision?"
        camilo @ flirt -happy "Definitely. But I would say that, wouldn't I?"
    elif s3_mc.current_partner == "Harry":
        harry happy "I'm so glad you picked me."
        s3_mc "Did I make the right decision?"
        harry @ flirt "Definitely. But I would say that, wouldn't I?"

    "The two of you go to stand next to the other couples."

    elladine @ very_happy "Hey girl! Congratulations!"
    elladine @ very_happy "You really bagged yourself a hottie there."
    elladine "Um, no offence, Nicky."

    nicky @ talk "None taken."
    nicky @ happy "Hi, by the way."
    nicky "I'm Nicky. I'm the lucky guy who's coupled up with Elladine."

    # solo portrait shot of nicky
    window hide
    show screen s3_character_profile("nicky") with Pause(3)
    hide screen s3_character_profile with dissolve

    "{i}Nicky\n
    -24, from Newcastle\n
    -Music tutor\n
    -Oldest sibling energy{/i}"

    elladine @ happy "As soon as I found out he was a musician, I was hooked."
    elladine @ happy "I've already got a really good feeling about this one."

    aj @ awkward "Er, yeah. Me too."
    show aj awkward
    "AJ doesn't sound so convinced about her guy..."

    seb @ happy "Alright? My name's Seb. I'm coupled up with AJ."

    # solo portrait shot of seb
    window hide
    show screen s3_character_profile("seb") with Pause(3)
    hide screen s3_character_profile with dissolve

    "{i}Seb\n
    -28, from Liverpool\n
    -Runs a music shop\n
    -Owns 52 t-shirts and 1 shirt{/i}"

    aj @ talk "I coupled up with a musician, too!"
    show aj
    seb "Well, no. I'm a shopkeeper."
    aj @ serious "But you must know about instruments to sell them, right?"
    seb "It's not that kind of music shop. I sell records."
    seb @ talk "You know, CDs and vinyl and stuff. There's a coffee shop, too."
    aj @ talk "Oh! With you now, sorry."

    "{i}You can't date Nicky or Seb in this season of Island Amore The Game, but that doesn't mean you can't be friends! And don't worry - all the other boys, and some of the girls, are options.{/i}"

    aj @ very_happy "This is so nice, you guys! We're already learning so much about each other!"

    nicky @ awkward "Whoa there."
    nicky "We're still waiting on two more new girls, right?"

    elladine @ awkward"Yeah. I wonder what they'll be like?"

    # CHOICE
    menu:
        s3_mc"The last two girls..."
        "I can't wait to meet them":
            s3_mc "We're not a complete Villa crew until everyone's here."
            aj @ talk "Right! I'm so excited for them to get here!"
            nicky @ talk "You're not the only ones."
            "Nicky looks over at the two remaining single boys."

        "They better stay away from [s3_mc.current_partner]":
            $ s3_mc.like(s3_mc.current_partner)
            nicky @ talk "Wow! So committed already, huh?"

            # IF STATEMENT
            if s3_mc.current_partner == "Bill":
                bill @ happy "I kinda like it."
                bill "It's nice to know [s3_name] is feeling it so strongly."
                bill @ talk "I mean, if another boy came in right now and tried to couple up with her, I'd have a thing or two to say about it, as well."
            elif s3_mc.current_partner == "Camilo":
                camilo @ happy "I kinda like it."
                camilo "It's nice to know [s3_name] is feeling it so strongly."
                camilo @ talk "I mean, if another boy came in right now and tried to couple up with her, I'd have a thing or two to say about it, as well."
            elif s3_mc.current_partner == "Harry":
                harry @ happy "I kinda like it."
                harry "It's nice to know [s3_name] is feeling it so strongly."
                harry @ talk "I mean, if another boy came in right now and tried to couple up with her, I'd have a thing or two to say about it, as well."

        "Maybe they got lost on the way here":
            s3_mc "This place isn't exactly well signposted."
            nicky @ talk "Bad news for the leftover boys if you're right."

    # IF STATEMENT
    if s3_mc.current_partner == "Bill":
        bill @ talk "I wonder if they'd be open to coupling up with each other."
    elif s3_mc.current_partner == "Camilo":
        camilo @ talk "I wonder if they'd be open to coupling up with each other."
    elif s3_mc.current_partner == "Harry":
        harry @ talk "I wonder if they'd be open to coupling up with each other."

    "[s3_mc.current_partner] looks over at the two remaining single boys."

    # IF STATEMENT
    if s3_mc.current_partner == "Bill":
        "Camilo's smile is still dazzling, but it looks a little more nervous now."
        "Harry stands up straight, trying to look confident."
    elif s3_mc.current_partner == "Camilo":
        "Bill is masking his disappointment by concentrating on the grass between his toes."
        "Harry stands up straight, trying to look confident."
    elif s3_mc.current_partner == "Harry":
        "Bill is masking his disappointment by concentrating on the grass between his toes."
        "Camilo's smile is still dazzling, but it looks a little more nervous now."

    aj @ serious "I feel bad for them. Nobody wants to get picked last."
    elladine @ sad "Yeah, and it's pretty obvious they both wanted to get picked by [s3_name]..."
    aj @ talk "Well, maybe their perfect soulmates are about to walk out of that door any second."
    seb @ serious "Let's not kid ourselves. That kind of thing never happens in the real world."
    nicky @ talk "Alright, but this isn't exactly a normal situation, is it?"
    nicky "It's Island Amore. Where dreams come true."
    seb @ talk "Wow, corny."
    nicky @ talk "Come on, mate. The magic only works if you believe in it."
    seb @ sad "Maybe that's why nothing magical ever happens to me."

    # CHOICE
    menu:
        thought "Do dreams come true in the Villa?"
        "Nicky's got it right!":
            $ s3_mc.like("Nicky")
            s3_mc "I can't wait for whatever's on the horizon!"
            nicky @ very_happy"That's the spirit."
        
        "I don't believe in magic":
            $ s3_mc.like("Seb")
            s3_mc "If we're gonna have fun in the Villa, it won't be from magic."
            s3_mc "It'll be from hard grafting."
            seb @ happy "You've got that right."
        
        "My dreams are too weird":
            $ s3_mc.like("Nicky")
            $ s3_mc.like("Seb")
            s3_mc "If they manage to make my dreams come true, I'll be impressed."
            s3_mc "Could they even fit a T-Rex in here?"

    "Everyone falls silent as a new girl emerges from the Villa."

    # IF STATEMENT (which women show up in villa first)
    if s3_mc.current_partner == "Harry":
        call s3e1p1_meet_miki from _call_s3e1p1_meet_miki
        call s3e1p1_meet_iona from _call_s3e1p1_meet_iona
    elif s3_mc.current_partner == "Bill":
        call s3e1p1_meet_iona from _call_s3e1p1_meet_iona_1
        call s3e1p1_meet_genevieve from _call_s3e1p1_meet_genevieve
    elif s3_mc.current_partner == "Camilo":
        call s3e1p1_meet_miki from _call_s3e1p1_meet_miki_1
        call s3e1p1_meet_genevieve from _call_s3e1p1_meet_genevieve_1

    # CHOICE
    menu:
        thought "They've made an impression on each other already..."
        "It's really cute":
            thought "I hope me and [s3_mc.current_partner] get on as well as they do!"
        
        "It's probably not real":
            thought "It's not like they really know each other..."
            thought "They're probably just showing off."
        
        "I'd be the filling in that sandwich":
            thought "They make such a hot couple!"

    elladine @ talk "I think that's everyone."
    bill @ happy "Five great ladies, five great gents, five great couples. Makes sense to me."
    aj @ awkward "Don't you think it's a bit early to say whether our couples are great or not?"

    # IF STATEMENT
    if s3_mc.current_partner == "Bill":
        bill @ flirt "I dunno. I've already got a pretty great feeling about this one."
        iona @ awkward "Well, it's not a competition."
    elif s3_mc.current_partner == "Camilo":
        camilo @ flirt "I dunno. I've already got a pretty great feeling about this one."
        miki @ awkward "Well, it's not a competition."
    elif s3_mc.current_partner == "Harry":
        harry @ flirt "I dunno. I've already got a pretty great feeling about this one."
        miki @ awkward "Well, it's not a competition."

    nicky @ talk "It sort of is, though. Only the strongest couple can win the fifty grand."

    # CHOICE
    menu:
        s3_mc "Based on first impressions, I think the strongest couple here will be..."
        "Me and [s3_mc.current_partner]":
            $ s3e1p1_strongest_couple = "MC"
            # IF STATEMENT
            $ s3_mc.like(s3_mc.current_partner)
            if s3_mc.current_partner == "Bill":
                bill @ happy "Not to bang my own drum or anything, but hard agree."
            elif s3_mc.current_partner == "Camilo":
                camilo @ happy "Not to bang my own drum or anything, but hard agree."
            elif s3_mc.current_partner == "Harry":
                harry @ happy "Not to bang my own drum or anything, but hard agree."
            elladine @ happy "I can't lie, you two do look super cute together."
        "Miki and Bill" if s3_mc.current_partner == 'Camilo' or s3_mc.current_partner == 'Harry':
            $ s3e1p1_strongest_couple = "Miki and Bill"
        "Iona and Camilo" if s3_mc.current_partner == 'Bill' or s3_mc.current_partner == 'Harry':
            $ s3e1p1_strongest_couple = "Iona and Camilo"
        "Genevieve and Harry" if s3_mc.current_partner == 'Camilo' or s3_mc.current_partner == 'Bill':
            $ s3e1p1_strongest_couple = "Genevieve and Harry"
        "Elladine and Nicky":
            $ s3e1p1_strongest_couple = "Elladine and Nicky"
            $ s3_mc.like('Nicky')
            $ s3_mc.like('Elladine')
            elladine @ flirt "Aw, babes."
        "AJ and Seb":
            $ s3e1p1_strongest_couple = "AJ and Seb"
            $ s3_mc.like('AJ')
            $ s3_mc.like('Seb')
            aj @ awkward "Wow, really?"
            seb @ awkward "That's, um... sweet of you to say."

    # IF STATEMENT
    if s3e1p1_strongest_couple == "Miki and Bill" or s3e1p1_strongest_couple == "Iona and Camilo" or s3e1p1_strongest_couple == "Genevieve and Harry":
        $ s3_mc.dislike(s3_mc.current_partner)
        if s3_mc.current_partner == "Bill":
            bill @ sad "Stronger than you and me?"
        elif s3_mc.current_partner == "Camilo":
            camilo @ sad "Stronger than you and me?"
        elif s3_mc.current_partner == "Harry":
            harry @ sad "Stronger than you and me?"
        s3_mc "I'm just being honest."

    # IF STATEMENT
    if s3_mc.current_partner == "Bill":
        iona @ talk "All I meant was, it might be a competition, but it doesn't really matter who wins."
        iona "We're all just here to find love, right?"
    elif s3_mc.current_partner == "Camilo" or s3_mc.current_partner == "Harry":
        miki @ talk "All I meant was, it might be a competition, but it doesn't really matter who wins."
        miki "We're all just here to find love, right?"

    # CHOICE
    menu:
        s3_mc "I'm here..."
        "To win the game":
            s3_mc "Don't get me wrong, we all want to find someone..."
            s3_mc "But that doesn't change the fact that this is a competition."
            s3_mc "There will be a winner."
            s3_mc "And that winner will be me."
            # IF STATEMENT
            if s3_mc.current_partner == "Bill":
                bill @ happy "Wow. Love that confidence."
            elif s3_mc.current_partner == "Camilo":
                camilo @ happy "Wow. Love that confidence."
            elif s3_mc.current_partner == "Harry":
                harry @ happy "Wow. Love that confidence."

        "To fall in love":
            s3_mc "She's right. At the end of the day, all that matters is finding the right person for you."
            s3_mc "That's the only prize worth winning, really."
            # IF STATEMENT
            if s3_mc.current_partner == "Bill":
                $ s3_mc.like("Iona")
                iona @ talk "Wow, yes. [s3_name] just said it better than I ever could."
            elif s3_mc.current_partner == "Camilo" or s3_mc.current_partner == "Harry":
                $ s3_mc.like("Miki")
                miki @ talk "Wow, yes. [s3_name] just said it better than I ever could."

        "To have fun":
            $ s3_mc.like("AJ")
            s3_mc "This is the holiday of a lifetime."
            s3_mc "Love is great and winning is fine, but why put so much pressure on it?"
            s3_mc "If all I get from this is a few cool new friends, I'll count myself a winner."
            aj @ talk "Wow, yes. [s3_name] just said it better than I ever could."

    # IF STATEMENT
    if s3_mc.current_partner == "Harry":
        iona @ happy "Oh my days, you guys!"
        iona @ very_happy "I've got a text!"
    elif s3_mc.current_partner == "Camilo" or s3_mc.current_partner == "Bill":
        genevieve @ happy "Oh my days, you guys!"
        genevieve @ very_happy "I've got a text!"

    text "Islanders, it's time to get to know each other a little better. Please make your way to the challenge platform and get ready to unpack some secrets about your fellow Islanders! #excessbaggage #gettingtoknowyou"

    seb @ serious "We've only just got here and we're already being challenged?"
    seb @ sad "I was hoping we could get a nap first."

    # IF STATEMENT
    if s3e1p1_took_a_nap:
        $ s3_mc.like("Seb")
        s3_mc "I had a little nap just before I came out!"
        seb @ talk "Oh mate, I wish I'd thought of that. Such a good move."
        seb "A little nap would be just the ticket."
    elif s3e1p1_feeling_hungry:
        $ s3_mc.like("Seb")
        seb @ talk "I'm a little peckish too."
        s3_mc "Me too! I was saying to Elladine, I'd love some kind of snack."
        if s3_mc.current_partner == "Bill":
            bill @ flirt "Maybe I'm the kind of snack you're after."
        elif s3_mc.current_partner == "Camilo":
            camilo @ flirt "Maybe I'm the kind of snack you're after."
        elif s3_mc.current_partner == "Harry":
            harry @ flirt "Maybe I'm the kind of snack you're after."
        s3_mc "That's not the kind of snack I mean."

    nicky @ talk "I hate to sound like a stuck record, but it's Island Amore."
    nicky "You have seen this show before, right? You didn't just get off at the wrong bus stop and end up here by mistake?"
    nicky "Because if that's what happened, the sooner you admit it, the less awkward it's going to be."
    elladine @ talk "Aw, stop teasing him. He just needs a bit of time to get used to it, that's all."
    camilo @ happy "The challenges are just a bit of fun! It'll help us all get closer as a group."
    bill @ flirt "More importantly, we'll find out everyone's saucy secrets."
    camilo @ awkward "Well, that too, I guess..."
    bill @ talk "Don't get me wrong. I've got nothing to hide."
    bill "But I'm excited to find out what the rest of you are holding back."
    harry @ talk "That's true, but we're not just here to mess around and relax, or dig up gossip on each other."
    aj @ awkward "We're not?"
    harry @ talk "No! We're here on an important mission! To find someone we love. It's serious business."
    harry "The challenge will focus our minds and get us ready for the road ahead."

    # CHOICE
    menu:
        s3_mc "Doing the challenge is mostly about..."
        "Getting closer as a group":
            $ s3_mc.like("Camilo")
            s3_mc "Camilo's right. This challenge sounds like a great way to get to know each other."
            s3_mc "This is what it's all about! I bet it's going to be a right laugh."
        
        "Uncovering everyone's secrets":
            $ s3_mc.like("Bill")
            s3_mc "Bill's right. This is a great chance to expose all our best and worst stories."
            s3_mc "I bet we've all got some really juicy ones, too."
        
        "Bringing out my competitive side":
            $ s3_mc.like("Harry")
            s3_mc "Harry's right. We've all got to be on the ball if we want to make the most of our time here."
            s3_mc "This challenge sounds like a great way to get into the right mindset."


    elladine @ talk "Well, there's only one way to find out."

    # IF STATEMENT
    if s3_mc.current_partner == "Harry":
        iona @ happy "Let's go."
    elif s3_mc.current_partner == "Camilo" or s3_mc.current_partner == "Bill":
        genevieve @ happy "Let's go."

    if s3_mc.current_partner == "Bill":
        iona @ happy "Woo! I can't wait!"
    elif s3_mc.current_partner == "Camilo" or s3_mc.current_partner == "Harry":
        miki @ happy "Woo! I can't wait!"

    scene s3-lawn-day with dissolve
    $ on_screen = []

    "Chattering and laughing, the Islanders head towards the challenge platform."
    "Before you can follow, [s3_mc.current_partner] quietly takes you to one side."


    # IF STATEMENT
    if s3_mc.current_partner == "Bill":
        bill @ awkward "Hey, [s3_name]. Sorry to hang back like this."
        bill @ happy "I just wanted to have a quick chat with you in private before the challenge, if that's OK."
    elif s3_mc.current_partner == "Camilo":
        camilo @ awkward "Hey, [s3_name]. Sorry to hang back like this."
        camilo @ happy "I just wanted to have a quick chat with you in private before the challenge, if that's OK."
    elif s3_mc.current_partner == "Harry":
        harry @ awkward "Hey, [s3_name]. Sorry to hang back like this."
        harry @ happy "I just wanted to have a quick chat with you in private before the challenge, if that's OK."

    # CHOICE
    menu:
        thought "[s3_mc.current_partner] wants a chat..."
        "I thought you'd never ask":
            $ s3e1p1_li_wants_chat_response = "Positive"
            $ s3_mc.like(s3_mc.current_partner)
            jump s3e1p1_cheeky_snog_before_game

        "Sure, what's up.":
            $ s3e1p1_li_wants_chat_response = "Neutral"
            jump s3e1p1_cheeky_snog_before_game

        "I'd rather just get going.":
            $ s3_mc.dislike(s3_mc.current_partner)
            $ s3e1p1_li_wants_chat_response = "Negative"
            jump s3e1p1_cheeky_snog_before_game

    label s3e1p1_cheeky_snog_before_game:
        # IF STATEMENT
        # Bill LI
        if s3_mc.current_partner == "Bill":
            if s3e1p1_li_wants_chat_response == "Positive":
                bill @ flirt "Well, I'm asking now."
            elif s3e1p1_li_wants_chat_response == "Negative":
                bill @ sad "Sorry, I'll try to make it quick."
            else:
                bill "Well..."

            bill @ happy "I just wanted to say thank you for choosing me."
            bill "You could probably see it on my face, but you absolutely made my day."
            bill "You're blatantly the best-looking girl here."
            bill @ flirt "And I'm no expert, but even I can see you're the best-dressed, too."

            # CHOICE
            menu:
                thought "This would be the perfect opportunity.."
                "Go in for a cheeky snog":
                    $ s3e1p1_cheeky_snog = True
                    $ s3_mc.like("Bill")
                    "You bet your eyelashes and tilt your face towards his."
                    "His eyes go wide. His gaze flickers down to your lips, then back up to your eyes."
                    "His voice is suddenly low and breathy."
                    bill @ serious "Are you sure?"
                    s3_mc "No time like the present."
                    "He bites his lip."
                    bill @ flirt "I can't argue with that."
                    "He smiles as your lips meet."
                    "His rough, calloused hands rest firmly on your hips."
                    "Something about his hands seems to fit, as if the two of you have been doing this for years."
                    "Finally, you both break away at the same time."
                    bill @ very_happy "Cor."
                    bill "I didn't see that coming."
                    s3_mc "Did you like it?"
                    bill @ talk "Did I like it? Did I like it? [s3_name]..."
                    bill @ very_happy "I loved it."
                    bill @ flirt "Do you think we could do it again? Like, right now?"
                    s3_mc "All in good time, babe."

                "Maybe later":
                    $ s3e1p1_cheeky_snog = False
                    "There's no rush. I only just got here."

            bill @ happy "You seem like a girl who says what's on her mind, and I really admire that."
            bill @ happy "I don't do subtlety, see. Whether I like someone or I don't like someone, I come right out and say so."
            bill "So, yeah."
            bill "Obviously I won't try anything on if you're not interested, but I didn't want today to go any further without saying..."
            bill @ happy "I'm excited to start getting to know you."

            # CHOICE
            menu:
                thought "Bill wants to get to know me..."
                "I'm excited to get to know you too":
                    $ s3_mc.like('Bill')
                    s3_mc "I picked you for a reason. I can't wait to see where it leads us."
                    bill @ very_happy "I'm glad you said that."

                "I'm not really interested, sorry":
                    $ s3_mc.dislike('Bill')
                    s3_mc "Look, no offence..."
                    s3_mc "But just because I liked you better than the other two, that doesn't mean I actually like you."
                    bill @ sad "Oh... OK. I'm sorry."
                    bill @ awkward "I just assumed..."
                    bill @ serious "I'll try to keep that in mind."

                "Let's wait and see how this goes":
                    s3_mc "It's still early days."
                    bill  "Yeah, of course."
            
                "Show him the condoms" if s3e1p1_grab_some_condoms:
                    $ s3_mc.like('Bill')
                    "You pull your bikini top out a bit and nod."
                    s3_mc " Check this out."
                    bill @ awkward "Uh, alright...?"
                    "Tentatively, he peers down inside."
                    "He lets out a sharp laugh when he sees the stash of condoms there."
                    bill @ talk "That's certainly not what I was expecting to see."
                    bill @ flirt "Are you trying to send me a message?"
                    bill "Because I already told you, I don't do subtlety."
                    s3_mc "I'm not trying to say anything."
                    s3_mc "I'm just a girl with a top full of condoms, and I thought you ought to know."
                    s3_mc "Seeing as we're being honest with each other right now."
                    bill @ happy "Amazing."

            bill @ talk "Well, I guess the others must be wondering where we've got to."
            bill "Let's head over for the challenge!"

        # Camilo LI
        elif s3_mc.current_partner == "Camilo":
            if s3e1p1_li_wants_chat_response == "Positive":
                camilo @ flirt "Well, I'm asking now."
            elif s3e1p1_li_wants_chat_response == "Negative":
                camilo @ sad "Sorry, I'll try to make it quick."
            else:
                camilo "Well..."

            camilo @ happy "I just wanted to say thank you for choosing me."
            camilo "You could probably see it on my face, but you absolutely made my day."
            camilo "You're blatantly the best-looking girl here."
            camilo @ flirt "And I'm no expert, but even I can see you're the best-dressed, too."

            # CHOICE
            menu:
                thought "This would be the perfect opportunity.."
                "Go in for a cheeky snog":
                    $ s3e1p1_cheeky_snog = True
                    $ s3_mc.like("Camilo")
                    "You bet your eyelashes and tilt your face towards his."
                    "His eyes go wide. His gaze flickers down to your lips, then back up to your eyes."
                    "His voice is suddenly low and breathy."
                    camilo @ serious "Are you sure?"
                    s3_mc "No time like the present."
                    "He bites his lip."
                    camilo "I can't argue with that."
                    "He draws you into a slow, sensual kiss."
                    "His Hands tangle gently in your hair, stirring up goosebumps on the back of your neck."
                    "Finally, you both break away at the same time."
                    camilo @ happy "Blimey."
                    camilo "I didn't see that coming."
                    s3_mc "Did you like it?"
                    camilo @ talk "Did I like it? Did I like it? [s3_name]..."
                    camilo @ very_happy "I loved it."
                    camilo @ flirt "Do you think we could do it again? Like, right now?"
                    s3_mc "All in good time, babe."

                "Maybe later":
                    $ s3e1p1_cheeky_snog = False
                    "There's no rush. I only just got here."

            camilo @ flirt "And I don't just mean looks-wise. I think we've got that spark, you know?"
            camilo @ happy "It makes me wanna know everything there is to know about you."
            camilo "So, yeah."
            camilo "Obviously I won't try anything on if you're not interested, but I didn't want today to go any further without saying..."
            camilo @ happy "I'm excited to start getting to know you."

            # CHOICE
            menu:
                thought "Camilo wants to get to know me..."
                "I'm excited to get to know you too":
                    $ s3_mc.like('Camilo')
                    s3_mc "I picked you for a reason. I can't wait to see where it leads us."
                    camilo @ happy "I'm glad you said that."

                "I'm not really interested, sorry":
                    $ s3_mc.dislike('Camilo')
                    s3_mc "Look, no offence..."
                    s3_mc "But just because I liked you better than the other two, that doesn't mean I actually like you."
                    camilo @ sad "Oh... OK. I'm sorry."
                    camilo @ awkward "I just assumed..."
                    camilo @ serious "I'll try to keep that in mind."

                "Let's wait and see how this goes":
                    s3_mc "It's still early days."
                    camilo "Yeah, of course."

                "Show him the condoms" if s3e1p1_grab_some_condoms:
                    $ s3_mc.like('Camilo')
                    "You pull your bikini top out a bit and nod."
                    s3_mc "Check this out."
                    camilo @ awkward "Uh, alright...?"
                    "Tentatively, he peers down inside."
                    "He lets out a sharp laugh when he sees the stash of condoms there."
                    camilo @ talk "That's certainly not what I was expecting to see."
                    camilo @ flirt "Are you trying to send me a message?"
                    s3_mc "I'm not trying to say anything."
                    s3_mc "I'm just a girl with a top full of condoms, and I thought you ought to know."
                    s3_mc "Seeing as we're being honest with each other right now."
                    camilo @ happy "Amazing."

            camilo @ talk "Well, I guess the others must be wondering where we've got to."
            camilo "Let's head over for the challenge!"

        # Harry LI
        elif s3_mc.current_partner == "Harry":
            if s3e1p1_li_wants_chat_response == "Positive":
                harry @ flirt "Well, I'm asking now."
            elif s3e1p1_li_wants_chat_response == "Negative":
                harry @ sad "Sorry, I'll try to make it quick."
            else:
                harry "Well..."

            harry @ happy "I just wanted to say thank you for choosing me."
            harry @ awkward "You could probably see it on my face, but you absolutely made my day."
            harry "You're blatantly the best-looking girl here."
            harry @ flirt "And I'm no expert, but even I can see you're the best-dressed, too."

            # CHOICE
            menu:
                thought "This would be the perfect opportunity.."
                "Go in for a cheeky snog":
                    $ s3e1p1_cheeky_snog = True
                    $ s3_mc.like('Harry')
                    "You bet your eyelashes and tilt your face towards his."
                    "His eyes go wide. His gaze flickers down to your lips, then back up to your eyes."
                    "His voice is suddenly low and breathy."
                    harry @ serious "Are you sure?"
                    s3_mc "No time like the present."
                    "He bites his lip."
                    harry @ flirt "I can't argue with that."
                    "He looks nervous and excited as you gently press your lips to his."
                    "His hands tentatively come to rest on your lower back."
                    "As the kiss goes on, he becomes more confident, pulling you close against him."
                    "Finally, you both break away at the same time."
                    harry @ awkward "Gosh."
                    harry @ happy "I didn't see that coming."
                    s3_mc "Did you like it?"
                    harry @ talk "Did I like it? Did I like it? [s3_name]..."
                    harry @ very_happy "I loved it."
                    harry @ flirt "Do you think we could do it again? Like, right now?"
                    s3_mc "All in good time, babe."

                "Maybe later":
                    $ s3e1p1_cheeky_snog = False
                    "There's no rush. I only just got here."

            harry @ awkward "Well..."
            harry "Obviously we've only really got a first impression to go on at the moment."
            harry @ flirt "But I already feel like you're exactly my type on paper."
            harry @ awkward "I'm over here trying to act all manly and confident, and then you walk in, and it all just... melts away."
            harry @ happy "And the weird thing is, I don't even mind."
            harry "So, yeah."
            harry "Obviously I won't try anything on if you're not interested, but I didn't want today to go any further without saying..."
            harry @ happy "I'm excited to start getting to know you."

            # CHOICE
            menu:
                thought "Harry wants to get to know me..."
                "I'm excited to get to know you too":
                    $ s3_mc.like('Harry')
                    s3_mc "I picked you for a reason. I can't wait to see where it leads us."
                    harry @ happy "I'm glad you said that."

                "I'm not really interested, sorry":
                    $ s3_mc.dislike('Harry')
                    s3_mc "Look, no offence..."
                    s3_mc "But just because I liked you better than the other two, that doesn't mean I actually like you."
                    harry @ sad "Oh...OK. I'm sorry."
                    harry @ awkward "I just assumed..."
                    harry @ serious "I'll try to keep that in mind."

                "Let's wait and see how this goes":
                    s3_mc "It's still early days."
                    harry "Yeah, of course."

                "Show him the condoms" if s3e1p1_grab_some_condoms:
                    $ s3_mc.like('Harry')
                    "You pull your bikini top out a bit and nod."
                    s3_mc "Check this out."
                    harry @ awkward "Uh, alright...?"
                    "Tentatively, he peers down inside."
                    "He lets out a sharp laugh when he sees the stash of condoms there."
                    harry @ talk "That's certainly not what I was expecting to see."
                    harry @ flirt "Are you trying to send me a message?"
                    s3_mc "I'm not trying to say anything."
                    s3_mc "I'm just a girl with a top full of condoms, and I thought you ought to know."
                    s3_mc "Seeing as we're being honest with each other right now."
                    harry @ happy "Amazing."

            harry @ talk "Well, I guess the others must be wondering where we've got to."
            harry "Let's head over for the challenge!"

    # CHOICE
    menu:
        s3_mc "We should go and meet the others at the challenge platform..."
        "Yep, let's go":
            s3_mc "I hope they haven't started without us!"

        "Race you!":
            s3_mc "Last one there has to clean the pool!"
            # IF STATEMENT
            if s3_mc.current_partner == "Bill":
                bill @ talk "Wait, wh..."
            elif s3_mc.current_partner == "Camilo":
                camilo @ talk "Wait, wh..."
            elif s3_mc.current_partner == "Harry":
                harry @ talk "Wait, wh..."
            "You're already off and running."
            "Seconds later, you hear him laugh, then the sound of his bare feet on the grass as he gives chase."

        "Why don't you carry me?":
            # IF STATEMENT
            if s3_mc.current_partner == "Bill":
                bill @ talk "Carry you?"
                s3_mc "That's what I said."
                s3_mc "You can do it, right? Or are these muscles just for show?"
                bill @ happy "He smirks and flexes his impressives arms."
                bill "Of course I can do it. Just watch."
                "He puts one hand on your back, scoops the other under your legs, and effortlessly sweeps you off your feet."
                bill @ flirt "To the challenge platform, m'lady?"
                s3_mc " To the challenge platform at once!"
                "He sets off, carrying you bridal-style across the lawn."
            elif s3_mc.current_partner == "Camilo":
                camilo @ talk "Carry you?"
                s3_mc "That's what I said."
                s3_mc "You can do it, right? Or are these muscles just for show?"
                camilo @ happy "He smirks and flexes his impressives arms."
                camilo "Of course I can do it. Just watch."
                "He puts one hand on your back, scoops the other under your legs, and effortlessly sweeps you off your feet."
                camilo @ flirt "To the challenge platform, m'lady?"
                s3_mc " To the challenge platform at once!"
                "He sets off, carrying you bridal-style across the lawn."
            elif s3_mc.current_partner == "Harry":
                harry @ talk "Carry you?"
                s3_mc "That's what I said."
                s3_mc "You can do it, right? Or are these muscles just for show?"
                harry @ awkward "Muscles?"
                "He looks down at his arms and gives them an optimistic flex."
                harry @ happy "Of course I can do it. Just watch."
                "He stretches a bit more, positions himself carefully, then scoops you up in his arms."
                "He's stronger than he looks."
                harry @ flirt "To the challenge platform, m'lady?"
                s3_mc "To the challenge platform at once!"
                "He sets off, carrying you bridal-style across the lawn."

    scene sand with dissolve
    $ on_screen = []

    "It's only day 1, and [s3_name] is already turning heads all over the Villa!"
    # IF STATEMENT
    if s3e1p1_cheeky_snog == True:
        "I think that snog might be one for the record books."
        "Five minutes from first sight to first kiss?"
        "The other girls will never catch up!"
    "She's coupled up with [s3_mc.current_partner] for now, but who knows what could happen at this afternoon's challenge?"

    elladine @ happy "We've got to kiss the boy we think the clue is about."

    show elladine at npc_exit
    pause 0.3
    $ renpy.hide("elladine")

    # IF STATEMENT
    if s3_mc.current_partner == "Bill":
        show genevieve at npc_center
        genevieve @ talk "I can't believe how big that is..."
        show genevieve at npc_exit
        pause 0.3
        $ renpy.hide("genevieve")
    elif s3_mc.current_partner == "Camilo" or s3_mc.current_partner == "Harry":
        show miki at npc_center
        miki @ talk "I can't believe how big that is..."
        show miki at npc_exit
        pause 0.3
        $ renpy.hide("miki")

    jump s3e1p2

    return

# LABELS FOR s3e1p1
label s3e1p1_meet_miki:

    miki @ very_happy "Hi everyone! It's so exciting to be here!"

    # solo profile shot of miki
    window hide
    show screen s3_character_profile("miki") with Pause(3)
    hide screen s3_character_profile with dissolve

    "{i}Miki\n
    -21, from Cambringe\n
    -Lifestyle vlogger\n
    -Loves it when you smash that subscribe button{/i}"

    miki "I mean, this is Island Amore, where dreams come true, right?"
    nicky @ talk "Told you so."
    miki @ talk "At first I was like, what happens if I totally don't like any of the boys who are left?"
    miki @ flirt "But now I see the two beautiful boys you've left for me to choose from..."
    miki "I don't know why I was worried."
    "Her eyes linger on Bill."
    miki @ flirt "What's your name, handsome?"
    bill @ flirt "I'm Bill. Pleased to meet you, love."
    miki "You seem like a rugged, down-to-earth kind of guy, Bill."
    miki @ happy "And they say opposites attract."
    miki "Fancy being coupled up with an offbeat, creative type like me?"
    bill @ happy "I'm not exactly going to say no, am I?"
    bill "Beautiful girl asks if you want to couple up, you say yes. Basic common sense, isn't it."
    "She laughs."
    miki @ very_happy "I'll take that as a yes."
    "She takes his hand. Together, they walk back to you and the others."

    return

label s3e1p1_meet_iona:

    "A new girl emerges from the Villa. Everyone falls silent."
    iona @ very_happy "Good morning, Island Amore!"
    iona @ happy "I don't know about the rest of you, but I'm about ready to do something wild."

    # solo profile shot of iona
    window hide
    show screen s3_character_profile("iona") with Pause(3)
    hide screen s3_character_profile with dissolve

    "{i}Iona\n
    -23, from Aberdeen\n
    -Apprentice pylon rigger\n
    -Spends all day making sparks fly{/i}"

    camilo @ flirt "You don't mess around, do you?"
    iona "I certainly don't, babe."
    iona @ flirt "Is that going to be a problem?"
    camilo @ happy "Not at all."
    camilo "In fact, I think it's going to be the opposite of a problem."
    iona @ very_happy "Well, now I just have to couple up with you, don't I?"
    "Iona smirks and walks over to him."
    "He gives her a little salsa-style spin and she laughs."
    "They stride over to stand beside you."

    return

label s3e1p1_meet_genevieve:
    "The door opens one last time, and everyone turns to look as another girl struts out onto the lawn."
    genevieve @ very_happy "Hello, darlings."
    genevieve @ happy "How are we all doing?"

    # solo profile shot of genevieve
    window hide
    show screen s3_character_profile("genevieve") with Pause(3)
    hide screen s3_character_profile with dissolve

    "{i}Genevieve\n
    -26, from Gastonbury\n
    -Junior doctor\n
    -Wants to crowd surf into your heart{/i}"

    "Seeing the rest of the Islanders already in their couples, she realises Harry is the only single boy left."
    "She looks him over and smiles."
    genevieve @ flirt "What's your name, sweetie?"
    harry "Sweetie."
    harry @ awkward "Er, I mean..."
    harry @ happy "Harry. It's Harry."
    genevieve @ happy "Lovely to meet you, Harry."
    genevieve @ flirt "How lucky am I that nobody got to you before me?"
    "She goes over to give him a hug."
    "The two of them come to stand with you, Camilo and the other couples."

    return



#########################################################################
## Episode 1, Part 2
#########################################################################
label s3e1p2:
    scene sand with dissolve
    $ on_screen = []

    show screen day_title(1, 2) with Pause(4)
    hide screen day_title with dissolve

    "Last time on this brand spanking new season of Island Amore..."
    "The Islander checked out what the Villa has to offer..."
    "...but it wasn't just the immaculately tucked sheets getting a once over."
    "Everyone met each other and hit it off!"

    # IF STATEMENT
    if s3_mc.current_partner == "Bill":
        bill "Obviously we've only really got a first impression to go on at the moment."
        bill @ flirt "But I already feel like you're exactly my type on paper."
        show bill at npc_exit
        pause 0.3
        $ renpy.hide("bill")
    elif s3_mc.current_partner == "Camilo":
        camilo "Obviously we've only really got a first impression to go on at the moment."
        camilo @ flirt "But I already feel like you're exactly my type on paper."
        show camilo at npc_exit
        pause 0.3
        $ renpy.hide("camilo")
    elif s3_mc.current_partner == "Harry":
        harry "Obviously we've only really got a first impression to go on at the moment."
        harry @ flirt "But I already feel like you're exactly my type on paper."
        show harry at npc_exit
        pause 0.3
        $ renpy.hide("harry")

    "Well, almost everyone."
    show aj at npc_center
    aj @ awkward "Don't you think it's a bit early to say whether our couples are great or not?"
    show aj at npc_exit
    pause 0.3
    $ renpy.hide("aj")

    "It's early days, AJ, early days."
    "But you know what they say..."
    "The early bird catches the worm."

    # IF STATEMENT
    if s3e1p1_cheeky_snog:
        "Or in this case, [s3_name] and [s3_mc.current_partner] get smooching!"
        if s3_mc.current_partner == "Bill":
            show bill at npc_center
            bill @ happy "Cor"
            show bill at npc_exit
            pause 0.3
            $ renpy.hide("bill")
        elif s3_mc.current_partner == "Camilo":
            show camilo at npc_center
            camilo @ happy "Blimey"
            show camilo at npc_exit
            pause 0.3
            $ renpy.hide("camilo")
        elif s3_mc.current_partner == "Harry":
            show harry at npc_center
            harry @ happy "Gosh"
            show harry at npc_exit
            pause 0.3
            $ renpy.hide("harry")
        "Well said, [s3_mc.current_partner]."

    "Coming up..."
    "The Islander get hands-on with each other's excess baggage."
    
    show aj at npc_center
    aj @ talk "What gave it away?"
    show aj at npc_exit
    pause 0.3
    $ renpy.hide("aj")

    "And one clue doesn't add up..."

    show bill at npc_center
    bill @ awkward "I have no idea who this is about."
    show bill at npc_exit
    pause 0.3
    $ renpy.hide("bill")

    scene s3-platform-excess-baggage with dissolve
    $ on_screen = []

    "You and [s3_mc.current_partner] make your way over to the platform where the other Islanders have already gathered."

    elladine @ happy "There you are..."

    # IF STATEMENT
    if s3e1p1_cheeky_snog:
        "Elladine points at your lips."
        elladine @ awkward "You've smudged your lipstick, hun. It's on your cheek."
        "You quickly wipe at your cheek. [s3_mc.current_partner] laughs a little."
        if s3_mc.current_partner == "Bill":
            bill @ flirt "Cheeky."
        elif s3_mc.current_partner == "Camilo":
            camilo @ flirt "Cheeky."
        elif s3_mc.current_partner == "Harry":
            harry @ flirt "Cheeky."

    "Everyone is standing around some suitcase on a carousel."
    bill @ talk "Those spinny things make me feel dizzy at airports."
    harry @ talk "I always want to lie on them and just go round and round."
    harry @ awkward "They look kinda comfy and you're always exhausted by the time you get to them."
    elladine @ talk "I got a text."
    elladine @ happy "Ooh, it's the rules of the challenge!"
    elladine "We're starting first."
    elladine "In each suitcase we'll find a secret clue about one of the guys..."
    elladine @ talk "Then we kiss the guy who we think the clue's about!"
    elladine "The guy who matches the clue steps forward and we'll see if we snogged the right person."
    elladine @ happy "Then it'll be the guys' turn."
    
    # IF STATEMENT
    if s3_mc.current_partner == "Harry":
        miki @ talk "So, do we actually have to kiss who we think the clue is about?"
        miki @ flirt "Or can we just use this as a way to kiss someone we think is hot?"
        elladine @ awkward "Well, you wouldn't win the game..."
        miki @ flirt "But you'd get to snog someone you like."
    elif s3_mc.current_partner == "Camilo" or s3_mc.current_partner == "Bill":
        genevieve @ talk "So, do we actually have to kiss who we think the clue is about?"
        genevieve @ flirt "Or can we just use this as a way to kiss someone we think is hot?"
        elladine @ awkward "Well, you wouldn't win the game..."
        genevieve @ flirt "But you'd get to snog someone you like."
    
    thought "Whoa, so much could be revealed today..."

    # CHOICE
    menu:
        thought "I wonder if any of the clues will be about my secret..."
        "sexual attraction to thunder":
            $ s3e1p2_mc_secret = "Thunder"
            thought "The way those clouds rumble when the storms are rolling."
            thought "It is so tantalising."
            thought "It just makes my body tingle..."
        "naughty adventure on a rollercoaster":
            $ s3e1p2_mc_secret = "Rollercoaster"
            thought "That was a ride and a half..."
        "tendency to get too excited by dimples":
            $ s3e1p2_mc_secret = "Dimples"
            thought "I just can't help it, they're just so cute."
            thought "I want to stick my finer in them and fall into a never ending dimple..."
        "fan fiction I wrote when I was younger":
            $ s3e1p2_mc_secret = "Fan Fiction"
            thought "There were some saucy times..."

    thought "It would be funny if that came out on the first day!"
    "[s3_mc.current_partner] coughs, looking at you."
    # IF STATEMENT
    if s3_mc.current_partner == "Bill":
        bill @ awkward "You alright, [s3_name]?"
    elif s3_mc.current_partner == "Camilo":
        camilo @ awkward "You alright, [s3_name]?"
    elif s3_mc.current_partner == "Harry":
        harry @ awkward "You alright, [s3_name]?"

    elladine @ awkward "Yeah, you look a little farway."
    thought "Oops, I just got lost in thought."
    s3_mc "It's nothing."

    # CHOICE
    menu:
        s3_mc "I can't wait to..."
        "Find out the gossip about the boys":
            aj @ very_happy "Same, we've got to find out all the dirt."
        "Win this challenge!":
            elladine @ talk "There are no losers or winners in this challenge!"
            elladine "We're just getting to know each other"
            "You and Harry groan."
            harry @ sad "What's the point in that then?"

            # IF STATEMENT
            if s3_mc.current_partner == "Bill" or s3_mc.current_partner == "Harry":
                iona @ happy "You might get a lot of kisses."
            elif s3_mc.current_partner == "Camilo":
                genevieve @ happy "You might get a lot of kisses."
            harry @ happy "Oh, OK."
            harry @ flirt "That doesn't sound too bad."
        "Just kiss some dudes":
            # IF STATEMENT
            if s3_mc.current_partner == "Bill":
                genevieve @ happy "I feel you hun."
                genevieve @ very_happy "Can't wait to get some action in here!"
            elif s3_mc.current_partner == "Harry" or s3_mc.current_partner == "Camilo":
                miki @ happy "I feel you hun."
                miki @ very_happy "Can't wait to get some action in here!"

    # IF STATEMENT
    if s3_mc.current_partner == "Bill":
        genevieve @ flirt "I'm just going to kiss whoever I think is the fittest."
        elladine @ talk "Right, let's get started!"
        elladine "Iona, can you do the honours?"
        "Iona rushes to the conveyor belt and grabs a suitcase."
        "She wheels it over to the girls and quickly unzips it."
        iona @ talk "OK, the clue is..."
        iona "'This boy once woke up spooning a badger...'"
        "The boys look at each other puzzled while the girls huddle closer together."
        aj @ happy "That sounds adorable!"
        elladine @ sad "It sounds scary! Badgers will mess you up."
        iona @ sad "How do you even end up in that situation?"
        genevieve "I bet it was a prank by his mates."
    elif s3_mc.current_partner == "Camilo":
        genevieve @ flirt "I'm just going to kiss whoever I think is the fittest."
        elladine @ talk "Right, let's get started!"
        elladine "Miki, can you do the honours?"
        "Miki rushes to the conveyor belt and grabs a suitcase."
        "She wheels it over to the girls and quickly unzips it."
        miki @ talk "OK, the clue is..."
        miki "'This boy once woke up spooning a badger...'"
        "The boys look at each other puzzled while the girls huddle closer together."
        aj @ happy "That sounds adorable!"
        elladine @ sad "It sounds scary! Badgers will mess you up."
        genevieve @ sad "How do you even end up in that situation?"
        miki "I bet it was a prank by his mates."
    elif s3_mc.current_partner == "Harry":
        miki @ flirt "I'm just going to kiss whoever I think is the fittest."
        elladine @ talk "Right, let's get started!"
        elladine "Iona, can you do the honours?"
        "Iona rushes to the conveyor belt and grabs a suitcase."
        "She wheels it over to the girls and quickly unzips it."
        iona @ talk "OK, the clue is..."
        iona "'This boy once woke up spooning a badger...'"
        "The boys look at each other puzzled while the girls huddle closer together."
        aj @ happy "That sounds adorable!"
        elladine @ sad "It sounds scary! Badgers will mess you up."
        iona @ sad "How do you even end up in that situation?"
        miki "I bet it was a prank by his mates."

    elladine @ talk "That's a terrible idea all round."
    aj @ talk "But which one of these guys do you think it is?"

    # CHOICE
    menu:
        thought "Who do I think woke up spooning a badger?"
        "Camilo":
            $ s3e1p2_spooned_a_badger = "Camilo"
        "Bill":
            $ s3e1p2_spooned_a_badger = "Bill"
        "Harry":
            $ s3e1p2_spooned_a_badger = "Harry"
        "Nicky":
            $ s3e1p2_spooned_a_badger = "Nicky"
        "Seb":
            $ s3e1p2_spooned_a_badger = "Seb"

    # IF STATEMENT
    if s3_mc.current_partner == "Bill" or s3_mc.current_partner == "Camilo":
        genevieve @ happy "I agree with [s3_name]."
        genevieve "There's something about [s3e1p2_spooned_a_badger] that makes me imagine him waking up next to a badger."
    elif s3_mc.current_partner == "Harry":
        miki @ happy "I agree with [s3_name]."
        miki "There's something about [s3e1p2_spooned_a_badger] that makes me imagine him waking up next to a badger."
    
    elladine @ happy "So, we've decided it's [s3e1p2_spooned_a_badger]?"
    s3_mc "I think so, yeah."
    aj @ talk "So who wants to go kiss him?"

    # IF STATEMENT
    if s3e1p2_spooned_a_badger == "Nicky" or s3e1p2_spooned_a_badger == "Seb":
        elladine @ flirt "Yeah, go on. I will."
        "Elladine kisses [s3e1p2_spooned_a_badger] on the lips. She leans in for a deep and romantic kiss."
    else:
        # CHOICE
        menu:
            thought "Should I volunteer to kiss [s3e1p2_spooned_a_badger]?"
            "No thanks, he's not my type":
                $ s3e1p2_challenge_kiss = False
                s3_mc "He's not for me."
                # IF STATEMENT
                if s3_mc.current_partner == "Bill" or s3_mc.current_partner == "Camilo":
                    elladine @ talk "Genevieve, you should kiss [s3e1p2_spooned_a_badger]."
                    aj @ talk "Yeah, you've dealt with these types before."
                    genevieve @ happy "Sure, sure."
                    "Genevieve kisses [s3e1p2_spooned_a_badger] on the lips."
                else:
                    elladine @ awkward "I'll take one for the team."
                    "She kisses him."
            "Go on then, it's only a game":
                $ s3e1p2_challenge_kiss = True
                $ s3_mc.like(s3e1p2_spooned_a_badger)
                s3_mc "I'll do it."
                s3_mc "I'll kiss him."
                # IF STATEMENT
                if s3_mc.current_partner == "Bill" or s3_mc.current_partner == "Harry":
                    iona @ very_happy "Go on, [s3_name]!"
                elif s3_mc.current_partner == "Camilo":
                    genevieve @ very_happy "Go on, [s3_name]!"
                "You wander over to [s3e1p2_spooned_a_badger]."
                # IF STATEMENT
                if s3e1p2_spooned_a_badger == "Bill":
                    bill @ flirt "Alright?"
                elif s3e1p2_spooned_a_badger == "Camilo":
                    camilo @ flirt "Alright?"
                elif s3e1p2_spooned_a_badger == "Harry":
                    harry @ flirt "Alright?"
                "You kiss [s3e1p2_spooned_a_badger] firmly on the lips."
                "It's tender yet urgent."
                "As you pull away he whispers in your ear."
                # IF STATEMENT
                if s3e1p2_spooned_a_badger == "Bill":
                    bill @ happy "You're a really good kisser."
                elif s3e1p2_spooned_a_badger == "Camilo":
                    camilo @ happy "You're a really good kisser."
                elif s3e1p2_spooned_a_badger == "Harry":
                    harry @ happy "You're a really good kisser."
                "You blush a little and go back to the girls."
            "Do I have to stop at kissing him?":
                $ s3e1p2_challenge_kiss = True
                $ s3_mc.like(s3e1p2_spooned_a_badger)
                s3_mc "Let me at him."
                # IF STATEMENT
                if s3e1p2_spooned_a_badger == "Bill":
                    "You stride over to [s3e1p2_spooned_a_badger] and kiss him hard on his lips. You grind your body against his."
                    bill @ talk "Woah!"
                    genevieve @ very_happy "Woop! Go girl."
                    "You finally pull away. He looks stunned as he wipes his brow."
                    bill @ flirt "You're seriously a hot kisser."
                elif s3e1p2_spooned_a_badger == "Camilo":
                    "You stride over to [s3e1p2_spooned_a_badger] and kiss him hard on his lips. You grind your body against his."
                    camilo @ talk "Woah!"
                    miki @ very_happy "Woop! Go girl."
                    "You finally pull away. He looks stunned as he wipes his brow."
                    camilo @ flirt "You're seriously a hot kisser."
                elif s3e1p2_spooned_a_badger == "Harry":
                    "You stride over to [s3e1p2_spooned_a_badger] and kiss him hard on his lips. You grind your body against his."
                    harry @ talk "Woah!"
                    miki @ very_happy "Woop! Go girl."
                    "You finally pull away. He looks stunned as he wipes his brow."
                    harry @ flirt "You're seriously a hot kisser."
                s3_mc "Thanks, babe."
                "You stride back over to the girls."
                aj @ very_happy "Go [s3_name]!"
                elladine @ very_happy "Now that's how you go from G to D."

    elladine @ talk "Ok, so whoever woke up to a terrifying bed companion..."
    elladine "Please step forward!"
    "The boys all look at each other."
    "Nicky steps forward."
    elladine @ talk "Nicky!"

    # IF STATEMENT
    if s3e1p2_spooned_a_badger == "Nicky":
        nicky @ awkward "How'd you know it was me?"
    else:
        aj @ sad "Argh, Nicky? I wouldn't have known."
        nicky @ happy "I mean, there's not much of a giveaway for that."
        # IF STATEMENT
        if s3e1p2_spooned_a_badger == "Bill":
            bill @ talk "Why'd you think it was me?"
        elif s3e1p2_spooned_a_badger == "Camilo":
            camilo @ talk "Why'd you think it was me?"
        elif s3e1p2_spooned_a_badger == "Harry":
            harry @ talk "Why'd you think it was me?"
        elif s3e1p2_spooned_a_badger == "Seb":
            seb @ talk "Why'd you think it was me?"
        aj @ awkward "I don't know! I could just see you spooning a badger is all."

    bill @ talk "Mate, how'd you end up with a badger?"
    nicky @ awkward "OK, so first off, it was a baby badger that had clearly got lost."
    nicky "It had been a really cold night, so it must have somehow got into my flat and found something warm to cuddle up to."
    nicky @ happy "Me."
    aj @ talk "So what did you do?"
    nicky @ happy "Handed it over to a local animal charity who would try to reunite it with its parents."
    nicky "Though it didn't stop clinging to me until they arrived..."
    camilo @ very_happy "Cute!"

    # IF STATEMENT
    if s3_mc.current_partner == "Bill" or s3_mc.current_partner == "Harry":
        iona @ happy "Adorable, but moving on..."
        iona "[s3_name], why don't you go and get the next suitcase?"
    elif s3_mc.current_partner == "Camilo":
        miki @ happy "Adorable, but moving on..."
        miki "[s3_name], why don't you go and get the next suitcase?"


    "You head over to the carousel where suitcases are going round and round, and grab one."
    aj @ very_happy "Bring it over, [s3_name]!"
    "You pop the case open. Inside is a label which says..."

    # IF STATEMENT
    if s3_mc.current_partner == "Bill":
        s3_mc "'This boy got caught having sex in his mum's wardrobe.'"
        aj @ talk "Woah."
        genevieve @ flirt "Filthy."
    elif s3_mc.current_partner == "Camilo":
        s3_mc "'This boy got caught having sex at work.'"
        aj @ talk "Woah."
        genevieve @ flirt "Filthy."
    elif s3_mc.current_partner == "Harry":
        s3_mc "'This boy got caught having sex on a roof by someone flying a drone.'"
        aj @ talk "Woah."
        miki @ flirt "Filthy."
    
    elladine @ awkward "I reckon that's something Seb would do."
    aj @ happy "Or maybe it's [s3_mc.current_partner]..."

    # CHOICE
    menu:
        thought "Which boy is the clue about?"
        "Camilo":
            $ s3e1p2_caught_having_sex = "Camilo"
        "Bill":
            $ s3e1p2_caught_having_sex = "Bill"
        "Harry":
            $ s3e1p2_caught_having_sex = "Harry"
        "Nicky":
            $ s3e1p2_caught_having_sex = "Nicky"
        "Seb":
            $ s3e1p2_caught_having_sex = "Seb"

    # IF STATEMENT
    if s3e1p2_caught_having_sex == "Seb":
        if s3_mc.current_partner == "Bill" or s3_mc.current_partner == "Harry":
            iona @ happy "OK, I'll go and kiss them."
            "Iona saunters over plants a kiss on his lips."
            seb @ happy "Thank you for that."
            "Iona smiles."
            iona @ happy "Any day"
        elif s3_mc.current_partner == "Camilo":
            genevieve @ happy "OK, I'll go and kiss them."
            "Genevieve saunters over plants a kiss on his lips."
            seb @ happy "Thank you for that."
            "Genevieve smiles."
            genevieve @ happy "Any day"
    elif s3e1p2_caught_having_sex == "Nicky":
        if s3_mc.current_partner == "Bill" or s3_mc.current_partner == "Harry":
            iona @ happy "OK, I'll go and kiss them."
            "Iona saunters over plants a kiss on his lips."
            nicky @ happy "Thank you for that."
            "Iona smiles."
            iona @ happy "Any day"
        elif s3_mc.current_partner == "Camilo":
            genevieve @ happy "OK, I'll go and kiss them."
            "Genevieve saunters over plants a kiss on his lips."
            nicky @ happy "Thank you for that."
            "Genevieve smiles."
            genevieve @ happy "Any day"
    else:
        # CHOICES
        menu:
            thought "Should I go and kiss him?"
            "Yes! Get in there with [s3e1p2_caught_having_sex]":
                $ s3e1p2_challenge_kiss = True
                $ s3_mc.like(s3e1p2_caught_having_sex)
                "You rush over to [s3e1p2_caught_having_sex] and plant a kiss on his lips."
                "[s3e1p2_caught_having_sex] blushes at your touch."
                "You wink at him as you walk back to the girls."
                # IF STATEMENT
                if s3e1p2_challenge_kiss:
                    if s3_mc.current_partner == "Bill" or s3_mc.current_partner == "Harry":
                        iona @ very_happy "Check out [s3_name] getting all the kisses..."
                        iona @ happy "You go, babe."
                    elif s3_mc.current_partner == "Camilo":
                        genevieve @ very_happy "Check out [s3_name] getting all the kisses..."
                        genevieve @ happy "You go, babe."
                    s3_mc "Thanks hun!"
                    "You blow all the girls a kiss. They all laugh."
            "Nah, let one of the other girls":
                # IF STATMENT
                if s3_mc.current_partner == "Bill":
                    genevieve @ happy "I'll kiss him!"
                    "Genevieve walks over and kisses [s3e1p2_caught_having_sex] quickly."
                    genevieve "Thank you, next!"
                elif s3_mc.current_partner == "Camilo" or s3_mc.current_partner == "Harry":
                    miki @ happy "I'll kiss him!"
                    "Miki walks over and kisses [s3e1p2_caught_having_sex] quickly."
                    miki "Thank you, next!"

    iona @ talk "Would the guy getting sweaty and sexy in the weird places please come forward?"
    s3_mc "Did I get it right?"
    "[s3_mc.current_partner] steps forward."

    # IF STATEMENT
    if s3_mc.current_partner == "Bill" and s3e1p2_caught_having_sex == "Bill":
        bill @ happy "Yeah, you did, hun."
    elif s3_mc.current_partner == "Camilo" and s3e1p2_caught_having_sex == "Camilo":
        camilo @ happy "Yeah, you did, hun."
    elif s3_mc.current_partner == "Harry" and s3e1p2_caught_having_sex == "Harry":
        harry @ happy "Yeah, you did, hun."
    elif s3_mc.current_partner != s3e1p2_caught_having_sex:
        if s3_mc.current_partner == "Bill":
            bill @ awkward "Nope. It was me."
        elif s3_mc.current_partner == "Camilo":
            camilo @ awkward "Nope. It was me."
        elif s3_mc.current_partner == "Harry":
            harry @ awkward "Nope. It was me."
        
        s3_mc "Aw, I didn't get it right!"

        if s3e1p2_caught_having_sex == "Bill":
            bill @ awkward "I can't believe you thought it was me."
        elif s3e1p2_caught_having_sex == "Camilo":
            camilo @ awkward "I can't believe you thought it was me."
        elif s3e1p2_caught_having_sex == "Harry":
            harry @ awkward "I can't believe you thought it was me."
        elif s3e1p2_caught_having_sex == "Nicky":
            nicky @ awkward "I can't believe you thought it was me."
        elif s3e1p2_caught_having_sex == "Seb":
            seb @ awkward "I can't believe you thought it was me."

    # IF STATEMENT
    if s3_mc.current_partner == "Bill":
        aj @ talk  "Why did you have sex in the wardrobe?"
        aj "Aren't there like coat hangers and stuff?"
        bill @ awkward "I was having a house party and there was zero privacy."
        aj @ awkward "Please say your mum didn't catch you."
        bill @ talk "No, no."
        bill "She actually has no idea that it happened."
        genevieve @ awkward "Until now."
        bill @ awkward "Oh yeah..."
        bill @ sad  "Awks..."
    elif s3_mc.current_partner == "Camilo":
        camilo @ talk "It was closed, OK? And like, I work at my parents' shop so it's basically my shop so it's basically my second house. It would have been fine..."
        camilo "But my dad still believes in getting milk in glass bottles, you know, to save the planet."
        camilo @ flirt "And, like, after closing up me and this girl decided to get down and dirty on these boxes..."
        camilo "Heat of the moment, like..."
        camilo @ awkward "But then the next thing I know a whole crate of these milk bottles have smashed and there is milk everywhere."
        harry @ talk "Remind me never to buy anything from your shop, like, ever."
    elif s3_mc.current_partner == "Harry":
        harry @ talk "We were up on the roof, getting into it, and then I hear this buzzing sound..."
        harry @ talk "And there's this drone up there!"
        harry "So I threw my shoe at it."
        aj @ talk "Wait, what about the pilot? You could have hurt someone!"
        harry @ talk "Drones don't have pilots, AJ. They're only small."
        aj @ awkward "Oh, right..."
        harry @ talk "And besides, it was breaking the law!"
        harry @ serious "You shouldn't fly them around built up areas."
        elladine @ awkward "Right, speaking of laws, what were you doing up on a roof?"
        harry @ flirt "Just checking out the sights of the city from a different angle."

    # IF STATEMENT
    if s3_mc.current_partner == "Bill" or s3_mc.current_partner == "Camilo":
        genevieve @ awkward "Moving swiftly on..."
        genevieve @ talk "I'll go next."
        "Genevieve grabs another suitcase and reads out the clue."
        genevieve "'This boy rescued a cat from a burning tree.'"
    elif s3_mc.current_partner == "Harry":
        miki @ awkward "Moving swiftly on..."
        miki @ talk "I'll go next."
        "Miki grabs another suitcase and reads out the clue."
        miki "'This boy rescued a cat from a burning tree.'"

    aj @ talk "Woah, how many cats get stuck up burning trees?"

    # CHOICE
    menu:
        thought "Who would rescue a cat?"
        "Camilo":
            $ s3e1p2_rescue_cat = "Camilo"
        "Bill":
            $ s3e1p2_rescue_cat = "Bill"
        "Harry":
            $ s3e1p2_rescue_cat = "Harry"
        "Nicky":
            $ s3e1p2_rescue_cat = "Nicky"
        "Seb":
            $ s3e1p2_rescue_cat = "Seb"

    s3_mc "I reckon it's [s3e1p2_rescue_cat]."

    # IF STATEMENT
    if s3e1p2_rescue_cat == "Seb" or s3e1p2_rescue_cat == "Nicky":
        aj @ talk "Yeah, me too."
        aj "I'll take this one."
        "AJ jogs over to [s3e1p2_rescue_cat] and kisses him, stroking his hair a little."
        aj @ flirt "Meow."
    else:
        # CHOICE
        menu:
            thought "Should I go and kiss [s3e1p2_rescue_cat]?"
            "Yes! Kiss him all over":
                $ s3_mc.like(s3e1p2_rescue_cat)
                "You rush over to [s3e1p2_rescue_cat] and smother him in kisses all over his body."
                s3_mc "You're just so kissable."
                "The girls and guys all cheer."
                camilo @ flirt "Woah."
                # IF STATEMENT
                if s3e1p2_challenge_kiss:
                    if s3_mc.current_partner == "Bill":
                        genevieve @ very_happy "[s3_name] is at it again!"
                    elif s3_mc.current_partner == "Camilo" or s3_mc.current_partner == "Harry":
                        miki @ happy "[s3_name] is at it again!"

            "Nah, I don't want to":
                if s3_mc.current_partner == "Bill" or s3_mc.current_partner == "Harry":
                    iona @ talk "I think it's Seb."
                    iona "I'm kissing him."
                    "Iona runs over to Seb and kisses him."
                    iona @ flirt "Am I right?"
                elif s3_mc.current_partner == "Camilo":
                    genevieve @ talk "I think it's Seb."
                    genevieve @ awkward "I'm kissing him."
                    "Genevieve runs over to Seb and kisses him."
                    genevieve @ flirt "Am I right?"

            "Just a quick peck will do":
                "You walk over to [s3e1p2_rescue_cat] and gently kiss him."
                if s3e1p2_challenge_kiss:
                    if s3_mc.current_partner == "Bill":
                        genevieve @ very_happy "[s3_name] is at it again!"
                    elif s3_mc.current_partner == "Camilo" or s3_mc.current_partner == "Harry":
                        miki @ flirt "[s3_name] is at it again!"

    # IF STATEMENT
    if s3_mc.current_partner == "Bill" or s3_mc.current_partner == "Camilo":
        genevieve @ talk "OK, can the man who risked his nine lives for a cat please come forward!"
    elif s3_mc.current_partner == "Harry":
        iona @ talk "OK, can the man who risked his nine lives for a cat please come forward!"

    "Seb steps forward."
    seb @ awkward "Yeah, it was me. I saved the cat."

    # IF STATEMENT
    if s3e1p2_rescue_cat == "Seb":
        seb @ happy "[s3_name] and AJ were right."

    elladine @ very_happy "That's so brave of you Seb."
    seb @ happy "We were camping in the middle of nowhere and had just built our campfire."
    seb "A stray cat climbed the tree next to us."
    seb @ talk "Then suddenly the wind picked up and the tree caught fire!"
    seb "So I climbed up and caught the cat."

    # CHOICE
    menu:
        thought "Whoa, Seb saved a cat from a burning tree!"
        "That's so brave":
            s3_mc "That's so brave, Seb!"
            seb @ flirt "Thanks, [s3_name]."
        "He's foolish":
            thought "He could have gotten hurt!"
            s3_mc "He should have waited for the emergency services."
        "Seb clearly loves cats":
            s3_mc "Oh, you must love cats then to risk your life for them."
            seb @ very_happy "Yeah, cats are pretty awesome."

    aj @ talk "Once there was a fire in my dad's kitchen and we were all panicking and trying to find the cats to make sure they were safe..."
    aj @ awkward "And we found them just stretching out on the floor in my bedroom, directly above where the fire was."
    seb @ happy "Cats are always proper dedicated to finding a warm spot."

    # IF STATEMENT
    if s3_mc.current_partner == "Bill":
        genevieve "Or..."
        genevieve @ very_happy "They started the fire to create the warm spot..."
        iona @ awkward "OK, OK, enough cat talk."
        iona @ talk "Final clue girls. Then it's the boy's turn to do the kissing."
        "The boys cheer excitedly."
        iona "[s3_name], you can go and pick another one."
    elif s3_mc.current_partner == "Camilo":
        genevieve "Or..."
        genevieve @ very_happy "They started the fire to create the warm spot..."
        miki @ awkward "OK, OK, enough cat talk."
        miki @ talk "Final clue girls. Then it's the boy's turn to do the kissing."
        "The boys cheer excitedly."
        miki "[s3_name], you can go and pick another one."
    elif s3_mc.current_partner == "Harry":
        miki "Or..."
        miki @ very_happy "They started the fire to create the warm spot..."
        iona @ awkward "OK, OK, enough cat talk."
        iona @ talk "Final clue girls. Then it's the boy's turn to do the kissing."
        "The boys cheer excitedly."
        iona "[s3_name], you can go and pick another one."

    "You run over to the suitcases and grab one."
    aj @ talk "What's the clue, [s3_name]?"

    # IF STATEMENT
    if s3_mc.current_partner == "Bill":
        s3_mc "'This boy asked a girl out by making her a plate of heart shaped sandwiches!'"
        aj @ happy "Aw, that's actually a really sweet one."
    elif s3_mc.current_partner == "Camilo":
        s3_mc "'This boy once flew a date to Rome!'"
        aj @ happy "Wow, that's so exciting!"
    elif s3_mc.current_partner == "Harry":
        s3_mc "'This boy once serenaded a girl with a ukulele wearing nothing but a tie.'"
        aj @ happy "Aw, that's actually kinda hilarious and sweet all rolled into one."

    # CHOICE
    menu:
        thought "Which boy would do that?"
        "Camilo":
            $ s3e1p2_asked_girl_out = "Camilo"
        "Bill":
            $ s3e1p2_asked_girl_out = "Bill"
        "Harry":
            $ s3e1p2_asked_girl_out = "Harry"
        "Nicky":
            $ s3e1p2_asked_girl_out = "Nicky"
        "Seb":
            $ s3e1p2_asked_girl_out = "Seb"

    s3_mc "I reckon it's [s3e1p2_asked_girl_out]."

    # IF STATEMENT
    if s3_mc.current_partner == "Bill" or s3_mc.current_partner == "Harry":
        iona @ happy "Aw, yeah."
        iona "He's a cutie."
    elif s3_mc.current_partner == "Camilo":
        miki @ happy "Aw, yeah."
        miki "He's a cutie."

    # IF STATEMENT
    if s3e1p2_asked_girl_out == "Nicky" or s3e1p2_asked_girl_out == "Seb":
        if s3_mc.current_partner == "Bill" or s3_mc.current_partner == "Harry":
            iona @ talk "I'll kiss [s3e1p2_asked_girl_out]!"
            "Iona kisses [s3e1p2_asked_girl_out] on the nose."
            iona @ happy "Such a cutie."
        elif s3_mc.current_partner == "Camilo":
            genevieve @ talk "I'll kiss [s3e1p2_asked_girl_out]!"
            "Genevieve kisses [s3e1p2_asked_girl_out] on the nose."
            genevieve @ happy "Such a cutie."
    else:
        # CHOICE
        menu:
            thought "Should I go and kiss [s3e1p2_asked_girl_out]?"
            "Why not?":
                $ s3_mc.like(s3e1p2_asked_girl_out)
                "[s3e1p2_asked_girl_out] smiles as you walk over to him."
                s3_mc "Come here, you."
                "You smooch, hands all over each other."
                "Everyone cheers."
            "Yeah, he's a cutie":
                $ s3_mc.like(s3e1p2_asked_girl_out)
                "[s3e1p2_asked_girl_out] smiles as you walk over to him."
                s3_mc "Come here, you."
                "You smooch, hands all over each other."
                "Everyone cheers."
            "Nah, [s3e1p2_asked_girl_out] isn't for me.":
                if s3_mc.current_partner == "Bill" or s3_mc.current_partner == "Harry":
                    iona @ talk "I'll kiss [s3e1p2_asked_girl_out]!"
                    "Iona kisses [s3e1p2_asked_girl_out] on the nose."
                    iona @ happy "Such a cutie."
                elif s3_mc.current_partner == "Camilo":
                    genevieve @ talk "I'll kiss [s3e1p2_asked_girl_out]!"
                    "Genevieve kisses [s3e1p2_asked_girl_out] on the nose."
                    genevieve @ happy "Such a cutie."

    # IF STATEMENT
    if s3_mc.current_partner == "Bill":
        iona @ talk "Will the hopeless romantic please step forward?"
        "Bill steps forward."
        iona @ talk "It's Bill!"
        # IF STATEMENT
        if s3e1p2_asked_girl_out == "Bill":
            thought "I guessed that right!"
        else:
            nicky @ happy "That's so sweet, man."
        bill @ flirt "You can never go wrong with a good sandwich."
        bill @ awkward "Only problem is that she hated mayo and I had put it in every one."
        bill "I had them for my lunch in the end."
        nicky @ very_happy "Nothing says love like mayo, to be fair."
    elif s3_mc.current_partner == "Camilo":
        genevieve @ talk "Will the hopeless romantic please step forward?"
        "Camilo steps forward."
        genevieve @ talk "It's Camilo!"
        # IF STATEMENT
        if s3e1p2_asked_girl_out == "Camilo":
            camilo @ flirt "[s3_name] knows me so well already."
        else:
            harry @ very_happy "That's so sweet, man."
            miki @ flirt "Yeah, you're a real cutie."
    elif s3_mc.current_partner == "Harry":
        iona @ talk "Will the hopeless romantic please step forward?"
        "Harry steps forward."
        iona @ talk "It's Harry!"
        # IF STATEMENT
        if s3e1p2_asked_girl_out == "Harry":
            thought "I knew it!"
        else:
            elladine @ very_happy "Harry! That's hilarious."
        harry @ awkward "Yeah, I really can't even play the uke very well but I thought, like, why not."
        bill @ sad "And the tie was essential?"
        seb @ sad "But the clothes weren't..."
        harry @ flirt "You've got to look smart, even in the nude."

    elladine @ talk "Right now, it's the boys' turn to find out some secrets about the girls!"
    elladine "Everyone switch sides."
    "The girls all line up. Seb runs up and grabs a suitcase."
    seb @ talk "OK..."
    seb "'This girl once cooked breakfast in bed for a guy she had just met..."
    seb @ awkward "...and set his kitchen on fire.'"
    camilo @ awkward "Oh, wow."
    seb "'...And then didn't call him back.'"

    # CHOICE
    menu:
        thought "Have I ever set fire to a boy's kitchen and not called him back?"
        "No! That's terrible":
            $ s3e1p2_set_fire = False
        "Oops, yeah, that's about me!":
            $ s3e1p2_set_fire = True

    seb @ talk "I reckon, that's..."

    # IF STATEMENT
    if s3_mc.current_partner == "Bill" or s3_mc.current_partner == "Harry":
        seb @ talk "Iona."
        "Seb jogs over and kisses her."
        seb "She seems like the fire starting type."
        "Iona crosses her arms and rolls her eyes."
        iona @ awkward "Mate, part of my job is avoiding fires."
        bill @ awkward "Is that even a type that, like, people have?"
        aj @ flirt "It wouldn't work on paper."
        iona @ talk "Can the fire starter please step forward..."
    elif s3_mc.current_partner == "Camilo":
        seb @ talk "Elladine."
        "Seb jogs over and kisses her."
        seb "She seems like the fire starting type."
        "Elladine gasps."
        camilo @ awkward "Is that even a type that, like, people have?"
        genevieve @ talk "Can the fire starter please step forward..."


    # IF STATEMENT
    if s3e1p2_set_fire:
        "You step forward."
        if s3_mc.current_partner == "Bill" or s3_mc.current_partner == "Harry":
            iona @ talk "[s3_name]!"
        elif s3_mc.current_partner == "Camilo":
            genevieve @ talk "[s3_name]!"
        aj @ talk "Woah, [s3_name]. That's intense."
        s3_mc "Yeah, it was so embarrassing. All I wanted to do was make him breakfast in bed."
        s3_mc "No one got hurt."
        s3_mc "Just my pride..."
        s3_mc "And his kitchen cupboards."
    else:
        "Elladine steps forward."
        genevieve @ talk "Elladine!"
        elladine @ sad "Yeah, it was an accident, obviously. I was trying to make him a nice fry up."
        elladine @ talk "I knocked this kitchen roll off the top shelf and it got caught in the toaster."
        elladine @ serious "No one got hurt thankfully, but yeah, I never called him back after that."
        elladine @ sad "I was way too embarrassed."

    # IF STATEMENT
    if s3_mc.current_partner == "Bill" or s3_mc.current_partner == "Harry":
        iona @ talk "OK boys, next clue."
    elif s3_mc.current_partner == "Camilo":
        genevieve @ talk "OK boys, next clue."

    "Nicky picks up a suitcase."
    nicky @ talk "Let's see what we've got here."
    "He unzips the case."
    nicky "'This girl hooked up with the chief bridesmaid at a cousin's wedding.'"
    thought "That secret's not about me, but..."

    # CHOICE
    menu:
        thought "In general would I be interested in being with girls while on Island Amore?"
        "Yeah, I'd be interested in dating girls!":
            $ s3_mc.bisexual = True
            thought "If it felt right and I met the right person, I could imagine getting with a girl in here, for sure!"
        "No, I'm going to stick with boys.":
            $ s3_mc.bisexual = False

    nicky @ happy "I've got a sneaky suspicion that this secret is about..."
    "He walks over to AJ and kisses her on the lips."
    "As he walks back, AJ grins."
    aj @ talk "What gave it away?"
    nicky @ talk "I'm not sure, but I definitely get a vibe."
    nicky "I've got a good feel for these things."
    genevieve @ talk "Surely you can't tell someone's relationship history just from looking at them."
    aj @ happy "You'd be surprised."
    
    # IF STATEMENT
    if s3_mc.bisexual == True:
        $ s3_mc.like("AJ")
        "AJ winks at you."
        if s3_mc.current_partner == "Bill":
            genevieve @ talk "Wait, what was that?"
        elif s3_mc.current_partner == "Camilo" or s3_mc.current_partner == "Harry":
            miki @ talk "Wait, what was that?"
        s3_mc "A code for girls who like girls."
        s3_mc "It's like a secret handshake that we have."
        aj @ talk "There's a secret handshake? Why wasn't I told?"
        if s3_mc.current_partner == "Bill":
            s3_mc "Ssh, don't give away that it's fake. We've got to keep Genevieve on her toes."
        elif s3_mc.current_partner == "Camilo" or s3_mc.current_partner == "Harry":
            s3_mc "Ssh, don't give away that it's fake. We've got to keep Miki on her toes."

    # IF STATEMENT
    if s3_mc.current_partner == "Bill" or s3_mc.current_partner == "Harry":
        iona @ happy "Good guess, Nicky."
    elif s3_mc.current_partner == "Camilo":
        genevieve @ happy "Good guess, Nicky."

    elladine @ talk "Next boy, grab a case!"
    "Camilo runs over and picks up a case."

    # IF STATEMENT
    if s3_mc.current_partner == "Bill":
        camilo @ happy "'This girl took a job as a waitress to escape a blind date.'"
        thought "Have I taken a job as a waitress to escape a blind date?"
    elif s3_mc.current_partner == "Camilo" or s3_mc.current_partner == "Harry":
        camilo @ flirt "'This girl did a sexy birthday striptease for a guy...'"
        camilo @ awkward "'Only to be interrupted by his family, who had flown in to surprise him!'"
        thought "Have I ever gotten interrupted during a sexy dance?"

    # CHOICE
    menu:
        thought "Is that clue about me?"
        "Yeah, that's about me":
            $ s3e1p2_camilos_clue = True
            thought "I wonder if Camilo will get it right..."
        "No, I've never done that":
            $ s3e1p2_camilos_clue = False
            thought "I wonder who did that..."

    # IF STATEMENT
    if s3_mc.current_partner == "Bill" or s3_mc.current_partner == "Harry":
        camilo "I reckon this is..."
        camilo @ happy "Elladine!"
        "He goes over to Elladine and kisses her."
    elif s3_mc.current_partner == "Camilo":
        camilo "I reckon this is..."
        camilo @ happy "[s3_name]!"
        "He runs over to you."
        camilo @ flirt "Mind if I kiss you, [s3_name]?"
        # CHOICE
        menu:
            thought "Do I mind if Camilo kisses me?"
            "Sure, go for it":
                $ s3_mc.like("Camilo")
                "He puts a hand behind your head and draws you in close."
                "He tenderly kisses the bottom of your lip."
            "Nah, I'd rather you didn't":
                camilo "That's fine! But just so everyone knows, I think this is about [s3_name]!"
                "He walks back to the others."

    elladine @ talk "Would the girl please step forward!"
    
    # IF STATEMENT
    if s3e1p2_camilos_clue:
        "You step forward."
        if s3_mc.current_partner == "Bill":
            "Genevieve also steps forward."
            genevieve @ happy "Aw! Babe, what a coincidence!"
        elif s3_mc.current_partner == "Camilo" or s3_mc.current_partner == "Harry":
            "Miki also steps forward."
            miki @ happy "Oh my god, hun! We're so similar."
        s3_mc "Ha! Yeah..."
        s3_mc "I guess it could happen to anyone."
        if s3_mc.current_partner == "Bill" or s3_mc.current_partner == "Harry":
            camilo @ awkward "I got that so wrong."
    else:
        if s3_mc.current_partner == "Bill":
            "Genevieve steps forward."
        elif s3_mc.current_partner == "Camilo" or s3_mc.current_partner == "Harry":
            "Miki steps forward."
        camilo @ awkward "Damn, I got that so wrong."

    # IF STATEMENT
    "Harry goes and picks up a suitcase."
    harry @ happy  "'This girl...'"
    # IF STATEMENT
    if s3e1p2_mc_secret == "Thunder":
        harry @ talk "'...is sexually attracted to the rumble of thunder!'"
    elif s3e1p2_mc_secret == "Rollercoaster":
        harry @ talk "'...had a naughty adventure on a rollercoaster!'"
    elif s3e1p2_mc_secret == "Dimples":
        harry @ talk "'...has a tendency to get too excited by dimples!'"
    elif s3e1p2_mc_secret == "Fan Fiction":
        harry @ talk "'...wrote fan fiction when she was younger!'"
    
    thought "Oh no! This is about me."
    thought "I wonder if Harry can guess who that's about."

    # IF STATEMENT
    if s3_mc.current_partner == "Bill" or s3_mc.current_partner == "Camilo":
        harry @ happy "I reckon it's Genevieve."
        "He strides over and kisses Genevieve, accidentally bumping against her nose."
        genevieve @ awkward "Don't worry. I didn't need my nose..."
        harry @ awkward "Did I get it right?"
        genevieve "Nope!"
    elif s3_mc.current_partner == "Harry":
        harry @ happy "I reckon it's [s3_name]."
        "He walks over to you."
        harry "I've got a hunch it was you because you kinda look guilty..."
        harry @ flirt "But I also just really want to kiss you."
        harry @ flirt "You up for that?"

        # CHOICE
        menu:
            thought "Do I mind if Harry kisses me?"
            "Yeah, sure!":
                $ s3_mc.like("Harry")
                "He closes his eyes and leans in for a kiss."
                "He leans the wrong way and bumps against your nose."
                harry @ awkward "Oops."
                harry @ flirt "Let me try that again."
                "Your lips touch and you feel him stumble forward a little. He gains his balance and draws you closer."
            "I'd rather you didn't.":
                harry @ happy "That's fine! But just so everyone knows, I think this is about [s3_name]!"
                "He walks back to the others."

        harry @ happy "Did I get it right?"

    # CHOICE
    menu:
        thought "The clue was about me! I'd better step forward..."
        "Proudly own it":
            "You leap forward with your hand on your hips."
            s3_mc "It's me!"
            # IF STATEMENT
            if s3e1p2_mc_secret == "Thunder":
                s3_mc "The thunder lover."
            elif s3e1p2_mc_secret == "Rollercoaster":
                s3_mc "The theme park exhibitionist."
            elif s3e1p2_mc_secret == "Dimples":
                s3_mc "The dimple lover."
            elif s3e1p2_mc_secret == "Fan Fiction":
                s3_mc "The smutty dirty lovely fan fiction writer."
        "Shamefully scuffle forward":
            "You step forward slowly, trying not to make any eye contact by looking at the ground."
            s3_mc "Yeah, that's about me."
        "Blame it on someone else":
            s3_mc "Um..."
            s3_mc "How do we know that clue isn't actually about you, Harry?"
            s3_mc "Whoever smelt it dealt it is a motto I live by."
            harry @ sad "Er, that's not how the game works."
            seb @ talk "Yeah, it's about one of you girls."
            "You shuffle your feet awkwardly."
            seb @ flirt "It's about you. Isn't it, [s3_name]?"
            s3_mc "Yeah... yeah it is."

    # IF STATEMENT
    if s3_mc.current_partner == "Bill" or s3_mc.current_partner == "Camilo":
        harry @ talk "[s3_name]?"
        s3_mc "Yeah."
        harry @ talk "Woah, I was well off."
        harry @ awkward "Ah, sorry, Genevieve."
        genevieve @ happy "You have got to tell us more about that later, hun."
    elif s3_mc.current_partner == "Harry":
        harry @ very_happy "Yes! I got it right."
        miki @ talk "You have got to tell us more about that later, hun."

    # IF STATEMENT
    if s3_mc.current_partner == "Bill":
        bill @ flirt "Yeah, I need details."
    elif s3_mc.current_partner == "Camilo":
        camilo @ flirt "Yeah, I need details."
    elif s3_mc.current_partner == "Harry":
        harry @ flirt "Yeah, I need details."
    
    # CHOICE
    menu:
        thought "Everyone wants to hear more about my secret..."
        "Maybe another day...":
            s3_mc "I've got an air of mystery to keep up, haven't I?"
            s3_mc "Maybe I'll reveal more another time."    
        "No way, this is enough already":
            s3_mc "You know too much already and we hardly know each other!"
            s3_mc "I've got a reputation to keep up."
        "This wasn't the half of it":
            s3_mc "I've got even more laundry that needs airing."
            s3_mc "If you want to have a rummage..."

    "Elladine coughs pointedly."

    # IF STATEMENT
    if s3_mc.current_partner == "Bill" or s3_mc.current_partner == "Harry":
        bill @ talk "Right, my turn!"
        "Bill goes up and grabs another case."
        bill "'This girl accidentally ordered sex toys to her work address.'"
        # CHOICE
        menu:
            thought "Have I ever accidentally ordered sex toys to my work?"
            "Yes, how did the suitcase know?":
                $ s3e1p2_ordered_sex_toys = True
                thought "Mysterious, all-seeing suitcase..."
            "Nah, I've never done that.":
                $ s3e1p2_ordered_sex_toys = False
                thought "How embarrassing..."
                thought "I'm glad that's not about me!"

        bill "I reckon this is..."

        # IF STATEMENT
        if s3_mc.current_partner == "Bill":
            bill @ talk "[s3_name]?"
            bill @ flirt "I think it's you, babes."
            "He walks over to you."
            bill "Mind if I kiss you?"
            # CHOICE
            menu:
                thought "Do I mind if Bill kisses me?"
                "Go for it, babes":
                    $ s3_mc.like("Bill")
                    "He kisses you softly, His hand rests on your back, drawing you in closer."
                "Nah, I'd rather you didn't":
                    bill @ happy "That's fine! But just so everyone knows, I think this is about MC!"
                    "He walks back to the others."

        elif s3_mc.current_partner == "Harry":
            bill @ talk "Iona?"
            "He walks over and kisses Iona."

        # IF STATEMENT
        if s3_mc.current_partner == "Bill":
            genevieve @ talk "Would the girl with the multiple packages please step forward?"
        elif s3_mc.current_partner == "Harry":
            miki @ talk "Would the girl with the multiple packages please step forward?"
        
        # IF STATEMENT
        if s3e1p2_ordered_sex_toys:
            "You and Iona both step forward."
            bill @ very_happy "I got it right!"
            iona @ talk "No way."
            iona @ very_happy "That's hilarious."
            iona "You've done that too?"
            s3_mc "Yeah!"
        else:
            "Iona steps forward."
            if s3_mc.current_partner == "Bill":
                bill @ sad "Damn, I got it wrong!"
                s3_mc "Can't believe you thought that was me! "
                "He winks at you."
                bill @ flirt "Maybe I just wanted an excuse to kiss you."
                s3_mc "Cheeky."
            else:
                "Iona steps forward."
                bill @ very_happy "Booyah. I got it right!"
                iona @ serious "Booyah?"
                "She winks."
                iona @ very_happy "Boo you more like."

        nicky @ awkward "Woah, girl."
        nicky "That's like, so embarrassing."
        iona @ talk "To be honest, I wasn't embarrassed at all."
        iona @ sad "It was just a faff to get all the boxes home on the train."
        harry @ talk "Boxes plural? As in more than one?"
        iona @ very_happy "Bulk order discount, babe. "
        "Bill whistles."
        bill @ talk "Wow."
        # IF STATEMENT
        if s3_mc.current_partner == "Bill":
            genevieve @ very_happy "Yeah! You go, sister."
        elif s3_mc.current_partner == "Harry":
            miki @ very_happy "Yeah! You go, sister."

    # IF STATEMENT
    if s3e1p1_cheeky_snog:
        if s3_mc.current_partner == "Bill":
            bill @ talk "Can I go again?"
            iona "Sure!"
            camilo @ happy "I'll go next."
            "He smiles at you as he walks over, hoisting a case over his toned shoulders."
            bill @ talk "OK, this girl..."
            "He looks up at you and smiles."
            bill "'This girl has already kissed a boy since we got into the Villa!'"
            iona "We'll all have by the end of this challenge."
            "He turns the piece of paper over."
            bill @ happy "'Before the challenge started!'"
            "Everyone laughs."
            genevieve "OK, I have no idea who that was."
            bill @ flirt "I think I do..."
            "He strides up to you and gently places his palm on your cheek."
            bill @ flirt "Fancy a round two?"
            # CHOICE
            menu:
                thought "Do I want [s3_mc.current_partner] to kiss me again?"
                "Yes!":
                    $ s3_mc.like(s3_mc.current_partner)
                    "He leans in and kisses you softly on the lips."
                    genevieve @ very_happy "[s3_name] is getting all the action today!"
                "Nah, you can kiss someone else":
                    bill "OK, suit yourself."
                    bill "I'll give AJ a quick kiss then."
                    "He kisses AJ on the cheek."
                "Go on then, [s3_mc.current_partner]":
                    $ s3_mc.like(s3_mc.current_partner)
                    "He leans in and kisses you softly on the lips."
                    genevieve @ very_happy "[s3_name] is getting all the action today!"
            iona @ talk "The answer was, of course..."
            "You step forward."
            iona @ happy "[s3_name]!"
            bill @ very_happy "Knew it."
            iona "Oh, you guys!"
            elladine @ happy "Such cuties."
            iona "OK..."
            iona @ talk "Next round."
            bill @ talk "Can I go again?"
            "The other boys cheer him on."
        elif s3_mc.current_partner == "Harry":
            harry @ talk "Can I go again?"
            iona "Sure!"
            camilo @ happy "I'll go next."
            "He smiles at you as he walks over, hoisting a case over his toned shoulders."
            harry @ talk "OK, this girl..."
            "He looks up at you and smiles."
            harry @ happy "'This girl has already kissed a boy since we got into the Villa!'"
            iona "We'll all have by the end of this challenge."
            "He turns the piece of paper over."
            harry @ happy "'Before the challenge started!'"
            "Everyone laughs."
            miki @ talk "OK, I have no idea who that was."
            harry @ flirt "I think I do..."
            "He strides up to you and gently places his palm on your cheek."
            harry @ flirt "Fancy a round two?"
            # CHOICE
            menu:
                thought "Do I want Harry to kiss me again?"
                "Yes!":
                    $ s3_mc.like(s3_mc.current_partner)
                    "He leans in and kisses you softly on the lips."
                    miki @ very_happy "[s3_name] is getting all the action today!"
                "Nah, you can kiss someone else":
                    harry "OK, suit yourself."
                    harry "I'll give AJ a quick kiss then."
                    "He kisses AJ on the cheek."
                "Go on then, Harry":
                    $ s3_mc.like(s3_mc.current_partner)
                    "He leans in and kisses you softly on the lips."
                    miki @ very_happy "[s3_name] is getting all the action today!"
            iona "The answer was, of course..."
            "You step forward."
            iona @ talk "[s3_name]!"
            harry @ very_happy "Knew it."
            iona "Oh, you guys!"
            elladine @ happy "Such cuties."
            iona "OK..."
            iona "Next round."

            harry @ talk "Can I go again?"
            "The other boys cheer him on."
        elif s3_mc.current_partner == "Camilo":
            camilo @ talk "I'll go next"
            "He smiles at you as he walks over, hoisting a case over his toned shoulders."
            camilo "OK, this girl..."
            "He looks up at you and smiles."
            camilo @ happy "'This girl has already kissed a boy since we got into the Villa!'"
            genevieve "We'll all have by the end of this challenge."
            "He turns the piece of paper over."
            camilo @ happy "'Before the challenge started!'"
            "Everyone laughs."
            miki "OK, I have no idea who that was."
            camilo @ flirt "I think I do..."
            "He strides up to you and gently places his palm on your cheek."
            camilo "Fancy a round two?"
            # CHOICE
            menu:
                thought "Do I want Camilo to kiss me again?"
                "Yes!":
                    $ s3_mc.like(s3_mc.current_partner)
                    "He leans in and kisses you softly on the lips."
                    miki @ very_happy "[s3_name] is getting all the action today!"
                "Nah, you can kiss someone else":
                    camilo "OK, suit yourself."
                    camilo @ happy "I'll give AJ a quick kiss then."
                    "He kisses AJ on the cheek."
                "Go on then, Camilo":
                    $ s3_mc.like(s3_mc.current_partner)
                    "He leans in and kisses you softly on the lips."
                    miki @ very_happy "[s3_name] is getting all the action today!"
            genevieve @ talk "The answer was, of course..."
            "You step forward."
            genevieve @ talk "[s3_name]!"
            camilo @ flirt "Knew it."
            genevieve @ flirt "Oh, you guys!"
            elladine @ happy "Such cuties."
            genevieve "OK..."
            genevieve "Next round."
            camilo @ very_happy "Can I go again?"
            "The other boys cheer him on."
    else:
        if s3_mc.current_partner == "Bill":
            bill @ talk "I'll go"
        elif s3_mc.current_partner == "Camilo":
            camilo @ talk "I'll go"
        elif s3_mc.current_partner == "Harry":
            harry @ talk "I'll go"
    
    "He grabs a case and looks at the clue."
    s3_mc "Just read the secret, hun."

    # IF STATEMENT
    if s3_mc.current_partner == "Bill":
        bill @ talk "'This girl has only ever had sex while on the water.'"
    elif s3_mc.current_partner == "Camilo":
        camilo @ talk "'This girl has been proposed to six times...'"
    elif s3_mc.current_partner == "Harry":
        harry @ talk "'This girl has never had sex with the lights off.'"

    "The boys go into a huddle."
    elladine flirt "Oh my gosh, which of you is this about?"
    "You look around the group. Nobody says anything."
    aj @ awkward "Come on, girls. It has to be one of us."
    "It quickly becomes clear that the clue isn't about any of you."

    # IF STATEMENT
    if s3_mc.current_partner == "Bill":
        genevieve sad "I don't get it. Who could it be?"
        iona serious "It's got to be one of us."
        "A clatter and rattle of wheels grabs everyone's attention as a large suitcase wheels out onto the platform."
        aj talk "Oh, wow."
        aj "That's one huge suitcase."
        genevieve -sad "I've never seen one that big before..."
        bill @ talk "I got a text!"
    elif s3_mc.current_partner == "Camilo":
        genevieve sad "I don't get it. Who could it be?"
        miki sad "It's got to be one of us."
        "A clatter and rattle of wheels grabs everyone's attention as a large suitcase wheels out onto the platform."
        aj talk "Oh, wow."
        aj "That's one huge suitcase."
        genevieve -sad "I've never seen one that big before..."
        camilo @ talk "I got a text!"
    elif s3_mc.current_partner == "Harry":
        miki sad "I don't get it. Who could it be?"
        iona serious "It's got to be one of us."
        "A clatter and rattle of wheels grabs everyone's attention as a large suitcase wheels out onto the platform."
        aj talk "Oh, wow."
        aj "That's one huge suitcase."
        miki -sad "I've never seen one that big before..."
        harry @ talk "I got a text!"
    
    text "Islanders, there is an unexpected item in your bagging area. [s3_mc.current_partner], please unzip the case."

    elladine @ talk "Oh my gosh, [s3_mc.current_partner]! Open up the case already!"
    "[s3_mc.current_partner] tentatively unzips the suitcase."
    "A stunning woman steps out."

    # IF STATEMENT
    if s3_mc.current_partner == "Bill":
        miki "Hey, you lot. I'm Miki."

        # Profile shot of Miki
        "Miki\n
        -21, from Cambridge\n
        -Lifestyle vlogger\n
        -Loves it when you smash the subscribe button"

        "She nods at Bill."
        miki @ very_happy "Thanks for getting me out of there, Bill."
        "Genevieve splutters in shock."
        genevieve @ talk "Wait... what? But..."
        iona @ talk "It's a new girl!"
        "Elladine and Iona run over to hug Miki."
        elladine @ very_happy"Welcome to the Villa, hun."
        nicky @ happy "Yeah, hey. I hope you weren't stuck in there for long, babe."
        miki "Nah, just a few minutes."
    elif s3_mc.current_partner == "Camilo":
        iona "Hey, you lot. I'm Iona."

        # Profile shot of Iona
        "Iona\n
        -23, from Aberdeen\n
        -Apprentice pylon rigger\n
        -Spends all day making sparks fly"

        "She nods at Camilo."
        iona @ happy "Thanks for getting me out of there, Camilo."
        "Miki splutters in shock."
        miki @ talk "Wait... what? But..."
        genevieve @ talk "It's a new girl!"
        "Elladine and Genevieve run over to hug Iona."
        elladine @ very_happy "Welcome to the Villa, hun."
        nicky @ happy "Yeah, hey. I hope you weren't stuck in there for long, babe."
        iona "Nah, just a few minutes."
    elif s3_mc.current_partner == "Harry":
        genevieve "Hey, you lot. I'm Genevieve."

        # Profile shot of Genevieve
        "Genevieve\n
        -26, from Gastonbury\n
        -Junior doctor\n
        -Wants to crowd surf into your heart"

        "She nods at Harry."
        genevieve @ happy "Thanks for getting me out of there, Harry."
        "Miki splutters in shock."
        miki @ talk "Wait... what? But..."
        iona @ talk "It's a new girl!"
        "Elladine and Iona run over to hug Genevieve."
        elladine @ very_happy "Welcome to the Villa, hun."
        nicky @ happy "Yeah, hey. I hope you weren't stuck in there for long, babe."
        genevieve "Nah, just a few minutes."

    # CHOICE
    menu:
        thought "There's a new girl in the Villa..."
        "Welcome her with a hug":
            $ s3_mc.like(s3_3rd_girl)
            if s3_mc.current_partner == "Bill":
                "You walk over and hug Miki."
                miki happy "Aw, thanks girls!"
                miki "It's so nice to be so welcomed."
            elif s3_mc.current_partner == "Camilo":
                "You walk over and hug Iona."
                iona happy "Aw, thanks girls!"
                iona "It's so nice to be so welcomed."
            elif s3_mc.current_partner == "Harry":
                "You walk over and hug Genevieve."
                genevieve happy "Aw, thanks girls!"
                genevieve "It's so nice to be so welcomed."
            
        "Try and get in the suitcase":
            "You run past Miki and attempt to clamber into the large suitcase. You fit perfectly, even standing upright."
            s3_mc "Woah, this thing is huge."
            aj @ talk "Yeah, how did they get you on the plane in that thing?"
            if s3_mc.current_partner == "Bill":
                miki @ talk "I didn't ride in it on the plane, hun. I only just got in it."
            elif s3_mc.current_partner == "Camilo":
                iona @ talk "I didn't ride in it on the plane, hun. I only just got in it."
            elif s3_mc.current_partner == "Harry":
                genevieve @ talk "I didn't ride in it on the plane, hun. I only just got in it."
            aj @ awkward "Oh right. Yeah, of course."

        "Roll your eyes and ignore her":
            $ s3_mc.dislike(s3_3rd_girl)
            "You roll your eyes. "
            thought "I totally didn't see that coming."
            "You stare at the ground as the other girls crowd around her."

    # IF STATEMENT
    if s3_mc.current_partner == "Bill":
        aj @ talk "Wait, we just had a clue, right? Miki, was it about you?"
        aj @ talk "Have you really only ever had sex on water?"
        genevieve @ talk "How does that even work?"
        "Miki smiles."
        miki @ flirt "I guess we'll have to wait for the boys to guess before we find out, won't we?"
        bill happy "Well, I think I can guess who to kiss now..."
        "He takes a step toward her."
        # CHOICE
        menu:
            thought "Miki and Bill are going to kiss"
            "Cheer them on":
                s3_mc "Woo! Get in there, [s3_mc.current_partner]."
                show bill very_happy
                "He smiles at you."
                show bill
            "Scream internally, but pretend to be fine":
                thought "..."
                thought "This is a disaster!"
                "Bill walks over to Miki."
                thought "Why me?"
                iona sad "You OK hun? You look like you're gritting your teeth a bit..."
                s3_mc "I'm fine! Totally fine."
            "Give her the stink eye":
                "You glare at Miki with menacing eyes."
                bill @ awkward "Chill out, [s3_name]."
                bill serious "It's just a kiss."

        # IF STATEMENT
        if s3e1p1_cheeky_snog:
            "Bill quickly walks over to Miki and kisses her on the lips tentatively."
            seb @ happy "How was it, mate?"
            bill @ happy "I'd say that was...maybe the third best kiss I've had today?"
            seb @ flirt "Wow. You're really cracking on, huh."
        else:
            "Bill and Miki kiss. It feels like it lasts forever."
            "They finally pull away."

        elladine @ talk "So, was he right?"
        miki happy "Yeah, it's true."
        miki "I love the water."
        miki "Oh, I got a text! That was quick."

        text "Islanders, that's the end of the challenge. Hopefully you've all learnt a little bit more about your fellow Islanders. Now all the dirt is dished, it's time for Miki to go and get to know you all."

        miki @ very_happy "Alright! Let's go, huns!"
    elif s3_mc.current_partner == "Camilo":
        aj @ talk "Wait, we just had a clue, right? Iona, was it about you?"
        aj @ talk "Did you really get proposed six times?"
        miki @ talk "Juicy!"
        "Iona smiles."
        iona @ talk "I guess we'll have to wait for the boys to guess before we find out, won't we?"
        camilo happy "Well, I think I can guess who to kiss now..."
        "He takes a step toward her."
        # CHOICE
        menu:
            thought "Iona and Camilo are going to kiss"
            "Cheer them on":
                s3_mc "Woo! Get in there, [s3_mc.current_partner]."
                show camilo very_happy
                "He smiles at you."
                show camilo
            "Scream internally, but pretend to be fine":
                thought "..."
                thought "This is a disaster!"
                "Camilo walks over to Iona."
                thought "Why me?"
                genevieve sad "You OK hun? You look like you're gritting your teeth a bit..."
                s3_mc "I'm fine! Totally fine."
            "Give her the stink eye":
                "You glare at Iona with menacing eyes."
                camilo @ awkward "Chill out, [s3_name]."
                camilo serious "It's just a kiss."
        # IF STATEMENT
        if s3e1p1_cheeky_snog:
            "Camilo quickly walks over to Iona and kisses her on the lips tentatively."
            seb @ happy "How was it, mate?"
            camilo @ flirt "I'd say that was...maybe the third best kiss I've had today?"
            seb @ flirt "Wow. You're really cracking on, huh."
        else:
            "Camilo and Iona kiss. It feels like it lasts forever."
            "They finally pull away."
        elladine @ talk "So, was he right?"
        iona happy "Yeah, it's true."
        iona "I can't help it, people just always seem to want to marry me."
        iona "Oh, I got a text! That was quick."

        text "Islanders, that's the end of the challenge. Hopefully you've all learnt a little bit more about your fellow Islanders. Now all the dirt is dished, it's time for Iona to go and get to know you all."

        iona @ very_happy "Alright! Let's go, huns!"
    elif s3_mc.current_partner == "Harry":
        aj @ talk "Wait, we just had a clue, right? Genevieve, was it about you?"
        aj @ talk "Have you really never ever had sex with the lights off?"
        aj "Do you only do it in the day or something?"
        "Genevieve smiles."
        genevieve @ flirt "I guess we'll have to wait for the boys to guess before we find out, won't we?"
        harry happy "Well, I think I can guess who to kiss now..."
        "He takes a step toward her."
        # CHOICE
        menu:
            thought "Genevieve and Harry are going to kiss"
            "Cheer them on":
                s3_mc "Woo! Get in there, [s3_mc.current_partner]."
                show harry very_happy
                "He smiles at you."
                show harry
            "Scream internally, but pretend to be fine":
                thought "..."
                thought "This is a disaster!"
                "Harry walks over to Genevieve."
                thought "Why me?"
                iona sad "You OK hun? You look like you're gritting your teeth a bit..."
                s3_mc "I'm fine! Totally fine."
            "Give her the stink eye":
                "You glare at Genevieve with menacing eyes."
                harry @ awkward "Chill out, [s3_name]."
                harry @ awkward "It's just a kiss."

        # IF STATEMENT
        if s3e1p1_cheeky_snog:
            "Harry quickly walks over to Genevieve and kisses her on the lips tentatively."
            seb happy "How was it, mate?"
            harry @ flirt "I'd say that was...maybe the third best kiss I've had today?"
            seb @ flirt "Wow. You're really cracking on, huh."
        else:
            "Harry and Genevieve kiss. It feels like it lasts forever."
            "They finally pull away."
        elladine @ talk "So, was he right?"
        genevieve happy "Yeah, it's true."
        genevieve "What can I say."
        genevieve @ flirt "I like to be able to see the action..."
        genevieve "Oh, I got a text! That was quick."
    
        text "Islanders, that's the end of the challenge. Hopefully you've all learnt a little bit more about your fellow Islanders. Now all the dirt is dished, it's time for Genevieve to go and get to know you all."
        
        genevieve @ very_happy "Alright! Let's go, huns!"

    "[s3_3rd_girl] struts off towards the Villa, and everyone else follows."
    thought "So, now this [s3_3rd_girl] person is in the mix."
    thought "I should think about how I want to play things with her."
    thought "Do I want to get in her good books early?"
    thought "Or find out her priorities?"
    thought "Maybe I should get to her before the other Islanders do, and get the gossip."
    
    # CHOICE
    menu:
        thought "Should I get [s3_3rd_girl] over for a private chat?"
        "Spend some time with the new girl":
            $ s3_mc.like(s3_3rd_girl)
            $ s3e1p2_talk_to_new_girl = True
            call s3e1p2_talk_to_new_girl from _call_s3e1p2_talk_to_new_girl
        "Don't talk to her":
            $ s3_mc.dislike(s3_3rd_girl)
            $ s3e1p2_talk_to_new_girl = False
            "You watch her walk off with the others."
            thought "Nah, I'm not bothered."
            thought "I'll just get to know her with the others."

    scene s3-poolside-day with dissolve
    $ on_screen = []

    "You and the other Islanders are lounging by the pool."
    # IF STATEMENT
    # only makes sense if you have images of MC
    # if current partner likes outfit:
    #     if s3_mc.current_partner == "Bill":
    #         bill "By the way. I never got the chance to say it earlier, but I absolutely love the swimsuit."
    #         bill "It looks so good on you."
    #     elif s3_mc.current_partner == "Camilo":
    #         camilo "By the way. I never got the chance to say it earlier, but I absolutely love the swimsuit."
    #         camilo "It looks so good on you."
    #     elif s3_mc.current_partner == "Harry":
    #         harry "By the way. I never got the chance to say it earlier, but I absolutely love the swimsuit."
    #         harry "It looks so good on you."
    # else:
    #     if s3_mc.current_partner == "Bill":
    #         bill "Call me shallow, but I love how good you look, [s3_name]."
    #         bill "Even in your lowkey getup."
    #     elif s3_mc.current_partner == "Camilo":
    #         camilo "Call me shallow, but I love how good you look, [s3_name]."
    #         camilo "Even in your lowkey getup."
    #     elif s3_mc.current_partner == "Harry":
    #         harry "Call me shallow, but I love how good you look, [s3_name]."
    #         harry "Even in your lowkey getup."

    # s3_mc "Thanks!"

    # IF STATEMENT
    if s3_mc.current_partner == "Bill" or s3_mc.current_partner == "Harry":
        iona @ talk "So, everyone's dirties are out now..."
        iona "And now [s3_3rd_girl] is here."
    elif s3_mc.current_partner == "Camilo":
        genevieve @ talk "So, everyone's dirties are out now..."
        genevieve "And now [s3_3rd_girl] is here."

    "[s3_3rd_girl] does a little wave."

    # IF STATEMENT
    if s3_mc.current_partner == "Bill":
        miki @ happy "Yeah, it's me."
    elif s3_mc.current_partner == "Camilo":
        iona @ happy "Yeah, it's me."
    elif s3_mc.current_partner == "Harry":
        genevieve @ happy "Yeah, it's me."

    harry @ talk "So much has happened, in so little time!"
    harry "I feel like we're already a solid group."

    # IF STATEMENT
    if s3_mc.current_partner == "Bill":
        iona @ talk "I know, right? It's all going down."
        iona "Pretending to be a waitress..."
        if s3e1p2_camilos_clue:
            show iona very_happy
            "She winks at you and Genevieve."
    elif s3_mc.current_partner == "Camilo" or s3_mc.current_partner == "Harry":
        genevieve @ talk "I know, right? It's all going down."
        genevieve "Embarrassing sexy dances..."
        if s3e1p2_camilos_clue:
            show genevieve very_happy
            "She winks at you and Miki."

    # IF STATEMENT
    if s3_mc.current_partner == "Bill":
        nicky @ talk "I can't believe Miki's secret."
        bill @ talk "Yeah, did you, like, live on a boat or something?"
        miki flirt "Yeah, I do actually."
        bill @ very_happy "Oh, woah. That makes more sense now."
    elif s3_mc.current_partner == "Camilo":
        nicky @ talk "I can't believe Iona's secret."
        camilo @ talk "You must have seen, like, all the cheesy proposals."
        iona "Yeah, I've seen them all."
        iona happy "One guy even flew a plane with a message on a banner."
        camilo "Oh, wow."
        "She shrugs."
        iona @ flirt "He flew the wrong way."
        iona "So my name read 'ANOI'. He was so embarrassed."
    elif s3_mc.current_partner == "Harry":
        nicky @ talk "I can't believe Genevieve's secret."
        harry @ talk "Yeah, like you've never turned off the lights?"
        genevieve happy "Nope... never."
        genevieve @ flirt "I like to be able to see what's happening."
        
    nicky "I thought it was a great clue."
    seb "Yeah, same."
    seb @ happy "Shows you've got good life experiences and all that."

    # CHOICE
    menu:
        thought "What do I think about [s3_3rd_girl]'s clue?"
        "I can't wait to get to know [s3_3rd_girl]!":
            $ s3_mc.like(s3_3rd_girl)
            s3_mc "You sound right up my street, [s3_3rd_girl]."
            s3_mc "I can't wait to get to know you!"
            if s3_mc.current_partner == "Bill":
                miki @ happy "Aw, thanks, [s3_name]."
            elif s3_mc.current_partner == "Camilo":
                iona @ happy "Aw, thanks, [s3_name]."
            elif s3_mc.current_partner == "Harry":
                genevieve @ happy "Aw, thanks, [s3_name]."
        "It doesn't say much about her":
            s3_mc "Is it, like, the best reflection of your personality?"
            if s3_mc.current_partner == "Bill":
                miki awkward "Um... no, probably not."
            elif s3_mc.current_partner == "Camilo":
                iona awkward "Um... no, probably not."
            elif s3_mc.current_partner == "Harry":
                genevieve awkward "Um... no, probably not."
            nicky @ happy "I think it's a proper funny place to start though."
        "I don't believe [s3_3rd_girl] at all":
            $ s3_mc.dislike(s3_3rd_girl)
            s3_mc "I don't believe you, [s3_3rd_girl]."
            nicky @ flirt "Why would she make that up?"
            "You shrug."
            s3_mc "It's a game."
            if s3_mc.current_partner == "Bill":
                genevieve @ awkward "Yeah you've got to stand out."
            elif s3_mc.current_partner == "Camilo" or s3_mc.current_partner == "Harry":
                miki @ awkward "Yeah you've got to stand out."
            nicky @ serious "Yeah, authentically."

            if s3_mc.current_partner == "Bill":
                miki sad "It's also a bit of a specific thing to lie about..."
            elif s3_mc.current_partner == "Camilo":
                iona sad "It's also a bit of a specific thing to lie about..."
            elif s3_mc.current_partner == "Harry":
                genevieve sad "It's also a bit of a specific thing to lie about..."
            s3_mc "Hmm..."

    # IF STATEMENT
    if s3_mc.current_partner == "Bill":
        iona happy "For real though Miki, you definitely made an entrance."
        iona @ talk "Maybe we should all arrive in suitcases next time!"
        miki happy "Yeah, I thought it was a bit out there at first but it was actually really fun."
        miki "I can't believe all this."
        "She gestures to the Villa."
        miki @ talk "It's amazing, isn't it?"
    elif s3_mc.current_partner == "Camilo":
        genevieve happy "For real though Iona, you definitely made an entrance."
        genevieve @ talk "Maybe we should all arrive in suitcases next time!"
        iona happy "Yeah, I thought it was a bit out there at first but it was actually really fun."
        iona @ talk "This place is bigger than I thought it would be!"
    elif s3_mc.current_partner == "Harry":
        iona happy "For real though Genevieve, you definitely made an entrance."
        iona @ talk "Maybe we should all arrive in suitcases next time!"
        genevieve happy "It worked really well."
        genevieve "It's so cool to be finally here."
        genevieve @ awkward "I really needed a holiday."

    aj happy "Yeah, I'm still getting used to all this."
    elladine "We'll all settle in soon enough."
    camilo happy "Once we have, like, proper meal together."
    camilo "Then it'll feel like home."
    camilo @ flirt "Food is the way to my heart..."
    aj @ very_happy "As long as I haven't cooked it, then a good meal is exactly what we need."

    if s3_mc.current_partner == "Harry":
        if s3e1p2_set_fire:
            iona @ happy "Yeah, and hopefully [s3_name] doesn't burn the kitchen down!"
        else:
            iona @ happy "Yeah, and hopefully Elladine doesn't burn the kitchen down!"
    else:
        if s3e1p2_set_fire:
            genevieve @ happy "Yeah, and hopefully [s3_name] doesn't burn the kitchen down!"
        else:
            genevieve @ happy "Yeah, and hopefully Elladine doesn't burn the kitchen down!"

    # CHOICE
    menu:
        thought "Is food the way to my heart?"
        "Of course! Food makes the heart grow fonder":
            harry @ awkward "I'm pretty sure it's absence makes the heart fonder."
            bill @ talk "Come on, [s3_name] is right."
            bill happy "Food is the real key to it."
        "Nah, I'm more of a drinks gal":
            s3_mc "Give me a good bottle and I'm happy."
            bill @ happy "Nah, you can't beat a good piece of toast."
        "As long as I'm eating it off [s3_mc.current_partner]'s body":
            $ s3_mc.like(s3_mc.current_partner)
            elladine @ talk "Woah, [s3_name]!"
            s3_mc "Did I say that out loud?"
            if s3_mc.current_partner == "Bill":
                "Bill blushes, but grins excitedly."
                bill @ flirt "You sure did..."
            elif s3_mc.current_partner == "Camilo":
                "Camilo blushes, but grins excitedly."
                camilo @ flirt "You sure did..."
            elif s3_mc.current_partner == "Harry":
                "Harry blushes, but grins excitedly."
                harry @ flirt "You sure did..."

    # IF STATEMENT
    if s3_mc.current_partner == "Bill":
        miki @ talk "Oh, that's mine."
    elif s3_mc.current_partner == "Camilo":
        iona @ talk "Oh, that's mine."
    elif s3_mc.current_partner == "Harry":
        genevieve @ talk "Oh, that's mine."
    
    text "[s3_3rd_girl], it's time for you to decide who to couple up with. All Islanders, please gather at the fire pit for the recoupling. #chooseyourmatch #dontlookback"
    
    "[s3_3rd_girl] looks around the group with a cheeky glint in her eye."
    elladine serious "Who are you going to choose?"

    "Who knows, Elladine?"
    "Who knows...?"
    if s3e1p2_talk_to_new_girl:
        "Well, I guess [s3_name] does."
    else:
        "Well, I guess [s3_3rd_girl] does."
    "Remind me not to let those lot in the kitchen."
    if s3e1p2_set_fire:
        "Especially that [s3_name] and AJ. They're fire hazards."
    else:
        "Especially that Elladine and AJ. They're fire hazards."
    "I don't know how I'd actually stop them. I can't leave this shed."
    "Maybe if I shout loud enough."

    scene sand with dissolve
    $ on_screen = []

    "Coming up..."
    "The Islanders get their graft on."
    if s3_mc.current_partner == "Bill":
        genevieve flirt "Single and ready to mingle, eh?"
        iona happy "Guess we'll need to keep a close eye on you."
        "And the power is in Miki's hands."
        miki serious "But, ultimately, I do have to make a choice and so..."
    elif s3_mc.current_partner == "Camilo":
        miki flirt "Single and ready to mingle, eh?"
        genevieve happy "Guess we'll need to keep a close eye on you."
        "And the power is in Miki's hands."
        iona serious "But, ultimately, I do have to make a choice and so..."
    elif s3_mc.current_partner == "Harry":
        miki flirt "Single and ready to mingle, eh?"
        iona happy "Guess we'll need to keep a close eye on you."
        "And the power is in Miki's hands."
        genevieve serious "But, ultimately, I do have to make a choice and so..."

    scene sand with dissolve
    $ on_screen = []

    jump s3e1p3
    
    return

label s3e1p2_talk_to_new_girl:
    scene s3-platform-excess-baggage with dissolve
    $ on_screen = []

    thought "Yeah, I'll call her over for a chat."
    s3_mc "Hey [s3_3rd_girl]."
    "She peels away from the others and walks over to you."
    if s3_mc.current_partner == "Bill":
        miki @ happy "Hey, hun."
        miki @ sad "You all right?"
        s3_mc "Yeah, I thought I'd see if you wanted to have a chat?"
        s3_mc "Girl to girl."
        miki @ happy "I'd love to."
        miki "Roof terrace? I've been dying to check it out."
        s3_mc "Great idea."
        
        scene s3-roof-day with dissolve
        $ on_screen = []

        "You and [s3_3rd_girl] sit beside each other on the roof."
        miki @ happy "Thanks for this."
        miki "Like, I was so worried coming in later."
        miki "Because everyone else has had a chance to couple up and meet each other first."
        # CHOICE
        menu:
            thought "[s3_3rd_girl] was worried about coming in late..."
            "You don't need to worry":
                s3_mc "Everyone seems pretty chill."
                s3_mc "Plus, we've only been here for a few hours!"
                miki happy "That's true, yeah."
                miki "You're so right."
            "I've got your back":
                miki @ talk "Really?"
                s3_mc "Always."
            "I would have been terrified":
                miki @ sad "I was proper worried."

        miki sad "I literally live on a boat, but when I got out of that suitcase I felt so unsteady on my legs."
        s3_mc "Yeah, it's a pretty surreal experience."
        s3_mc "But it'll be fun, you'll see."
        miki serious "For sure."
        miki @ happy "I'm so glad you called me over."
        miki "I wanted to talk to you about who I'm crushing on right now."
        s3_mc "Oh, yeah?"
        miki @ awkward "Yeah, you see..."
        "She looks down, then up again."
        miki @ awkward "I'm actually really attracted to Bill."
        
        # CHOICE
        menu:
            thought "[s3_3rd_girl] is into [s3_mc.current_partner]!"
            "I totally saw that coming":
                miki @ talk "You did?"
                s3_mc "Yeah, I had a hunch."
            "Yeah, I don't blame you! He's gorgeous":
                miki flirt "He is, isn't he?"
                miki "And a sweetheart as well."
            "But I'm with him!":
                miki sad "I know, I know."

        miki serious "That's why I wanted to talk to you."
        miki "Right now, if I had to couple up with someone, I'd for sure pick Bill."
        miki @ sad "I've got to choose someone so I wanted to be super upfront with you about it."
        miki @ awkward "I know it's early days..."
        s3_mc "It's only been a few hours."
        miki "...but feelings get so magnified in here."

        # CHOICE
        menu:
            thought "How do I feel about the idea of [s3_3rd_girl] picking [s3_mc.current_partner]?"
            "I'd be OK about it":
                miki @ talk "Really?"
                s3_mc "Yeah, like you said, early days."
            "At least you told me":
                miki @ talk "I thought it was the best thing to do."
            "I'd be annoyed":
                miki sad "Oh, really?"
                s3_mc "Yeah."
                miki @ talk "Well, I'm sorry you feel like that."
                miki "I hope we can move past, like, whatever happens."
                miki "If it happens."

        miki serious "I've got no clue whatsoever how he feels about me."
        miki "But I really wanted to talk to you about it."
        miki happy "So, thank you for taking the time to talk to me..."
        miki "It means a lot."
        miki serious "We should get back to the others."
        "You both head down from the roof terrace."
    elif s3_mc.current_partner == "Camilo":
        iona happy "Hey, hun."
        iona sad "You all right?"
        s3_mc "Yeah, I thought I'd see if you wanted to have a chat?"
        s3_mc "Girl to girl."
        iona happy "I'd love to."
        iona "Roof terrace? I've been dying to check it out."
        s3_mc "Great idea."

        scene s3-roof-day with dissolve
        $ on_screen = []

        "You and [s3_3rd_girl] sit beside each other on the roof."
        iona happy "Thanks for this."
        iona @ sad "Like, I was so worried coming in later."
        iona serious "Because everyone else has had a chance to couple up and meet each other first."
        # CHOICE
        menu:
            thought "[s3_3rd_girl] was worried about coming in late..."
            "You don't need to worry":
                s3_mc "Everyone seems pretty chill."
                s3_mc "Plus, we've only been here for a few hours!"
                iona happy "That's true, yeah."
                iona "You're so right."
            "I've got your back":
                iona @ talk "Really?"
                s3_mc "Always."
            "I would have been terrified":
                iona sad "I was proper worried."

        iona serious "I work on pylons, like, they're proper high and it can get kinda windy."
        iona "But that doesn't scare me."
        iona @ sad "But coming onto this..."
        iona @ flirt "Mate, I was terrified."
        s3_mc "Yeah, it's a pretty surreal experience."
        s3_mc "But it'll be fun, you'll see."
        iona "For sure."
        iona "I'm so glad you called me over."
        iona @ flirt "I actually really wanted to chat with you about who I'm keen on."
        s3_mc "Oh, yeah?"
        iona sad "Yeah, you see..."
        "She looks down, then up again."
        iona "When I look at the boys, the one who really makes me go 'he's my type' is Camilo."
        iona @ flirt "He's banging."
        
        # CHOICE
        menu:
            thought "[s3_3rd_girl] is into [s3_mc.current_partner]!"
            "I totally saw that coming":
                iona @ talk -sad "You did?"
                s3_mc "Yeah, I had a hunch."
            "Yeah, I don't blame you! He's gorgeous":
                iona happy "He is, isn't he?"
                iona "And a sweetheart as well."
            "But I'm with him!":
                iona @ awkward "I know, I know."

        iona serious "That's why I wanted to talk to you."
        iona @ flirt "Right now, if I had to couple up with someone, I'd for sure pick Camilo."
        iona "I've got to choose someone so I wanted to be super upfront with you about it."
        iona "I know it's early days..."
        s3_mc "It's only been a few hours."
        iona @ flirt "...but feelings get so magnified in here."

        # CHOICE
        menu:
            thought "How do I feel about the idea of [s3_3rd_girl] picking [s3_mc.current_partner]?"
            "I'd be OK about it":
                iona @ talk "Really?"
                s3_mc "Yeah, like you said, early days."
            "At least you told me":
                iona @ happy "I thought it was the best thing to do."
            "I'd be annoyed":
                iona sad "Oh, really?"
                s3_mc "Yeah."
                iona @ flirt "Well, I'm sorry you feel like that."
                iona "I hope we can move past, like, whatever happens."
                iona "If it happens."

        iona serious "And also, I don't know if he likes me the same way."
        iona "But I really wanted to talk to you about it."
        iona happy "So, thank you for taking the time to talk to me..."
        iona "It means a lot."
        iona "We should get back to the others."
        "You both head down from the roof terrace."
    elif s3_mc.current_partner == "Harry":
        genevieve happy "Hey, hun."
        genevieve sad "You all right?"
        s3_mc "Yeah, I thought I'd see if you wanted to have a chat?"
        s3_mc "Girl to girl."
        genevieve happy"I'd love to."
        genevieve "Roof terrace? I've been dying to check it out."
        s3_mc "Great idea."

        scene s3-roof-day with dissolve
        $ on_screen = []

        "You and [s3_3rd_girl] sit beside each other on the roof."
        genevieve happy "Thanks for this."
        genevieve @ awkward "Like, I was so worried coming in later."
        genevieve serious "Because everyone else has had a chance to couple up and meet each other first."
        # CHOICE
        menu:
            thought "[s3_3rd_girl] was worried about coming in late..."
            "You don't need to worry":
                s3_mc "Everyone seems pretty chill."
                s3_mc "Plus, we've only been here for a few hours!"
                genevieve happy "That's true, yeah."
                genevieve "You're so right."
            "I've got your back":
                genevieve @ talk "Really?"
                s3_mc "Always."
            "I would have been terrified":
                genevieve @ sad "I was proper worried."

        
        genevieve serious "I mean, I'm used to huge crowds and dealing with sick people and all this intense stuff, from work."
        genevieve @ talk "But this was so beyond that."
        genevieve @ awkward "Also that suitcase was kinda dark which freaked me out a bit."
        genevieve "Luckily I wasn't in there for long."
        s3_mc "Yeah, it's a pretty surreal experience."
        s3_mc "But it'll be fun, you'll see."
        genevieve "For sure."
        genevieve "I'm so glad you called me over."
        genevieve @ awkward "I wanted to say, I'm actually low-key into someone already."
        s3_mc "Oh, yeah?"
        genevieve sad "Yeah, you see..."
        "She looks down, then up again."
        genevieve @ awkward "Harry is definitely a bit of me."
    
        # CHOICE
        menu:
            thought "[s3_3rd_girl] is into [s3_mc.current_partner]!"
            "I totally saw that coming":
                genevieve @ talk "You did?"
                s3_mc "Yeah, I had a hunch."
            "Yeah, I don't blame you! He's gorgeous":
                genevieve happy "He is, isn't he?"
                genevieve "And a sweetheart as well."
            "But I'm with him!":
                genevieve sad "I know, I know."

        genevieve serious "That's why I wanted to talk to you."
        genevieve "Right now, if I had to couple up with someone, I'd for sure pick Harry."
        genevieve @ awkward "I've got to choose someone so I wanted to be super upfront with you about it."
        genevieve "I know it's early days..."
        s3_mc "It's only been a few hours."
        genevieve @ sad "...but feelings get so magnified in here."

        # CHOICE
        menu:
            thought "How do I feel about the idea of [s3_3rd_girl] picking [s3_mc.current_partner]?"
            "I'd be OK about it":
                genevieve @ talk "Really?"
                s3_mc "Yeah, like you said, early days."
            "At least you told me":
                genevieve @ happy "I thought it was the best thing to do."
            "I'd be annoyed":
                genevieve sad "Oh, really?"
                s3_mc "Yeah."
                genevieve @ awkward "Well, I'm sorry you feel like that."
                genevieve "I hope we can move past, like, whatever happens."
                genevieve "If it happens."

        genevieve serious "I've no idea how he feels, like."
        genevieve "But I really wanted to talk to you about it."
        genevieve happy "So, thank you for taking the time to talk to me..."
        genevieve "It means a lot."
        genevieve "We should get back to the others."
        "You both head down from the roof terrace."

    return

#########################################################################
## Episode 1, Part 3
#########################################################################
label s3e1p3:
    scene sand with dissolve
    $ on_screen = []

    show screen day_title(1, 3) with Pause(4)
    hide screen day_title with dissolve

    "Welcome back..."
    "To Island Amore!"
    "In an absolutely shocking twist that literally no one could have predicted..."
    "Another girl has already entered the Villa!"
    if s3_mc.current_partner == "Bill":
        miki very_happy "Hey, you lot. I'm Miki."
        miki "Thanks for getting me out of there."
        show miki at npc_exit
        pause 0.3
        $ renpy.hide("miki")
    elif s3_mc.current_partner == "Camilo":
        iona happy "Hey, you lot. I'm Iona."
        iona "Thanks for getting me out of there."
        show iona at npc_exit
        pause 0.3
        $ renpy.hide("iona")
    elif s3_mc.current_partner == "Harry":
        genevieve happy "Hey, you lot. I'm Genevieve."
        genevieve "Thanks for getting me out of there."
        show genevieve at npc_exit
        pause 0.3
        $ renpy.hide("genevieve")

    "Ladies, hide your men, this one's coming for them..."
    "Though it'll be hard to hide them in a Villa covered in cameras..."
    "Maybe if they put the sheets over their heads and pretend to be ghosts?"
    "Or stand really still and pretend to be statues?"
    "I don't know. I've never played a game of Hide and Seek in my life."
    "Coming up!"
    "Bill gets cheesy..."
    show bill at npc_center
    bill "I don't know about the rest of you, but I'm cream-crackered."
    show bill at npc_exit
    pause 0.3
    $ renpy.hide("bill")
    if s3_mc.current_partner == "Bill":
        "And Miki takes her pick..."
        show miki at npc_center
        miki serious "The guy I'd like to couple up with is..."
        show miki at npc_exit
        pause 0.3
        $ renpy.hide("miki")
    elif s3_mc.current_partner == "Camilo":
        "And Iona takes her pick..."
        show iona at npc_center
        iona serious "The guy I'd like to couple up with is..."
        show iona at npc_exit
        pause 0.3
        $ renpy.hide("iona")
    elif s3_mc.current_partner == "Harry":
        "And Genevieve takes her pick..."
        show genevieve at npc_center
        genevieve serious "The guy I'd like to couple up with is..."
        show genevieve at npc_exit
        pause 0.3
        $ renpy.hide("genevieve")

    scene s3-dressing-room with dissolve
    $ on_screen = []

    "The dressing room is a flurry of activity as the girls ready themselves for [s3_3rd_girl]'s decision."
    # IF STATEMENT
    if s3_mc.current_partner == "Bill" or s3_mc.current_partner == "Harry":
        iona sad "It's so weird knowing that [s3_3rd_girl]'s just stood by the firepit waiting for us."
    elif s3_mc.current_partner == "Camilo":
        genevieve awkward "It's so weird knowing that [s3_3rd_girl]'s just stood by the firepit waiting for us."
    
    if s3_mc.current_partner == "Bill":
        genevieve sad "Waiting for the guys more like."
        elladine sad "Yeah. It really didn't take long for the drama to start."
        genevieve "Tell me about it! I thought we'd at least have a day or something."
    elif s3_mc.current_partner == "Camilo" or s3_mc.current_partner == "Harry":
        miki sad "Waiting for the guys more like."
        elladine sad "Yeah. It really didn't take long for the drama to start."
        miki "Tell me about it! I thought we'd at least have a day or something."

    if s3_mc.current_partner == "Bill" or s3_mc.current_partner == "Harry":
        iona serious "Well, we kind of did."
    elif s3_mc.current_partner == "Camilo":
        genevieve serious "Well, we kind of did."
    
    aj "Can you pass me my lipstick, Ella, babes."
    elladine -sad "Of course hun."
    aj @ happy "Thanks! [s3_3rd_girl]'s super fit, don't you think?"

    # CHOICE
    menu:
        thought "[s3_3rd_girl] is..."
        "Almost too good looking":
            elladine serious "Yeah..."
        "Not really all that":
            elladine sad "I don't know how you can say that?"
        "Not as fit as me":
            elladine @ happy "You're both gorgeous."

    elladine serious "She's definitely some fierce competition."
    aj "That's why I want to make a special effort."
    thought "Everyone's going all out. I guess if there was a night for it, now's the time..."

    # IF STATEMENT
    if s3e1p1_grab_some_condoms:
        "You absent-mindedly undo your bra, then hear the telltale sound of plastic wrappers hitting the floor."
        s3_mc "The condoms!"
        "Different coloured wrappers indicating flavours spill across the room. Cherry red, banana yellow, and wheatgrass green."
        aj @ talk "Woah, [s3_name]!"
        s3_mc "Whoops..."
        aj @ flirt "Someone's looking to get busy."
        s3_mc "Better to be safe than sorry."
        elladine @ very_happy "Damn right."

    # Evening wear outfit selector
    # change all npcs to evening wear

    $ outfit = "evening"

    # IF STATEMENT
    # Only makes sense with MC images
    # if s3_current_outfit in s3_npc_preferred_outfits["Elladine"]:
    #     thought "Oh yeah, this is going to blow some minds."
    #     "Elladine looks over to you. Her eyes go wide."
    #     elladine "Damn! [s3_name], you're a real heart-stealer in that!"
    #     s3_mc "That's the idea."
    # else:
    #     s3_mc "Or, I could just wear this I guess..."
    #     elladine "Not going to push the boat out a bit? You must be confident."


    if s3_mc.current_partner == "Bill" or s3_mc.current_partner == "Harry":
        "Iona turns to you."
        iona serious "Are you worried about tonight, babe?"
    elif s3_mc.current_partner == "Camilo":
        "Genevieve turns to you."
        genevieve serious "Are you worried about tonight, babe?"

    # CHOICE
    menu:
        thought "Am I worried about who [s3_3rd_girl] will pick?"
        "I'd be lying if I said no":
            if s3_mc.current_partner == "Bill" or s3_mc.current_partner == "Harry":
                iona "Yeah, I know what you mean."
                iona @ awkward "Why am I so nervous?"
            elif s3_mc.current_partner == "Camilo":
                genevieve "Yeah, I know what you mean."
                genevieve @ awkward "Why am I so nervous?"
        "No, of course I'm not":
            if s3_mc.current_partner == "Bill" or s3_mc.current_partner == "Harry":
                iona "Yeah..."
                iona @ flirt "I don't know. I feel surprisingly nervous myself."
            elif s3_mc.current_partner == "Camilo":
                genevieve "Yeah..."
                genevieve @ awkward "I don't know. I feel surprisingly nervous myself."
        "How could I when I look this good?":
            elladine @ happy -serious "Wow, hun. I wish I had your confidence!"
            aj @ flirt "She's not wrong, though."
            if s3_mc.current_partner == "Bill" or s3_mc.current_partner == "Harry":
                iona @ happy -serious "Hearing that actually made me feel a little better myself."
            elif s3_mc.current_partner == "Camilo":
                genevieve @ happy -serious "Hearing that actually made me feel a little better myself."
        "Actually, I know she's going to pick [s3_mc.current_partner]." if s3e1p2_talk_to_new_girl == True:
            if s3_mc.current_partner == "Bill" or s3_mc.current_partner == "Harry":
                iona @ talk "Really? How?"
                s3_mc "She told me."
                iona "Oh..."
            elif s3_mc.current_partner == "Camilo":
                genevieve @ talk "Really? How?"
                s3_mc "She told me."
                genevieve "Oh..."
            elladine @ flirt "At least she was honest, I guess?"

    if s3_mc.current_partner == "Bill":
        "Genevieve takes a deep breath, and gives herself one last look-over in the mirror."
        genevieve serious "Well, girls, I guess this is it..."
    elif s3_mc.current_partner == "Camilo" or s3_mc.current_partner == "Harry":
        "Miki takes a deep breath, and gives herself one last look-over in the mirror."
        miki serious "Well, girls, I guess this is it..."

    scene s3-firepit-night with dissolve
    $ on_screen = []

    "[s3_3rd_girl] stands in front of the Islanders sat around the firepit."

    # CHOICE
    menu:
        thought "We only just arrived and already I might get separated from [s3_mc.current_partner]..."
        "Hold his hand":
            $ s3_mc.like(s3_mc.current_partner)
            if s3_mc.current_partner == "Bill":
                "You reach over and take a hold of [s3_mc.current_partner]'s hand. He turns and smiles at you."
                bill @ flirt "Your hands are so soft."
                "You blush"
                bill @ happy "Seriously, it's like holding a warm loaf of bread or something..."
                s3_mc "Huh?"
                bill @ awkward "...I don't know. Ignore me. My mind's all over the place."
                "He shifts in his seat."
            elif s3_mc.current_partner == "Camilo":
                "You reach over and take a hold of [s3_mc.current_partner]'s hand. He turns and smiles at you."
                camilo @ flirt "Your hands are so soft."
                "You blush"
                camilo @ happy "Seriously, it's like holding a warm loaf of bread or something..."
                s3_mc "Huh?"
                camilo @ awkward "...I don't know. Ignore me. My mind's all over the place."
                "He shifts in his seat."
            elif s3_mc.current_partner == "Harry":
                "You reach over and take a hold of [s3_mc.current_partner]'s hand. He turns and smiles at you."
                harry @ flirt "Your hands are so soft."
                "You blush"
                harry @ happy "Seriously, it's like holding a warm loaf of bread or something..."
                s3_mc "Huh?"
                harry @ awkward "...I don't know. Ignore me. My mind's all over the place."
                "He shifts in his seat."

        "Glare at [s3_3rd_girl]":
            "You frown at [s3_3rd_girl]. She doesn't look at you."
            s3_mc "Dammit, she didn't see me!"
            "You squint harder and lean in closer."
            thought "She has to notice me now."
            "Just then, you hear [s3_mc.current_partner]'s voice whispering in your ear."
            if s3_mc.current_partner == "Bill":
                bill awkward "Um, what are you doing?"
                s3_mc "Huh?"
                bill @ serious -awkward "Do you need glasses or something?"
            elif s3_mc.current_partner == "Camilo":
                camilo awkward "Um, what are you doing?"
                s3_mc "Huh?"
                camilo @ serious -awkward "Do you need glasses or something?"
            elif s3_mc.current_partner == "Harry":
                harry awkward "Um, what are you doing?"
                s3_mc "Huh?"
                harry @ serious -awkward"Do you need glasses or something?"
            s3_mc "No..."

        "Look at the other Islanders":
            "You look around to see how the others are handling [s3_3rd_girl]'s arrival."
            thought "If those girls are nervous, they're doing a banging job of hiding it."
            "The only one who seems a little off is Elladine, who occasionally glances at her hands."
            "The boys seem calm, too. But you look harder, you notice that Seb's chewing his cheek."
            if s3_mc.current_partner == "Bill":
                "Harry can't keep his eyes off of Miki."
            elif s3_mc.current_partner == "Harry":
                "Camilo's eyes are fixed on Genevieve's face. He bites his lips."
            thought "Any of these guys would probably jump at the chance to be with [s3_3rd_girl]..."

    "[s3_3rd_girl] clears her throat, then speaks."

    if s3_mc.current_partner == "Bill":
        miki @ talk "I didn't know how to feel on the way here."
        miki "I was excited, obviously, but I knew I'd be taking a guy away from another girl."
        miki @ serious "I thought I'd be OK with that as you've only been together since this morning..."
        miki @ sad "But looking at you all now, you already seem like such cute couples."
        miki "But at first glance, this boy seems like my type on paper."
        miki @ happy "He's smart, funny, and just dreamy."
        miki @ awkward "And although I don't want to break a promising couple up so early on..."
        miki @ serious "I'm here to make a choice and so..."
        "Everyone tenses."

        if s3e1p2_talk_to_new_girl:
            thought "Here she goes. About to pick [s3_mc.current_partner]..."
        else:
            thought "She better not pick [s3_mc.current_partner]."
        miki "The boy I'd like to couple up with is..."
        thought "Maybe she won't?"
        miki @ happy "[s3_mc.current_partner]."
    elif s3_mc.current_partner == "Camilo":
        iona @ talk "I didn't know how to feel on the way here."
        iona "I was excited, obviously, but I knew I'd be taking a guy away from another girl."
        iona @ serious "I thought I'd be OK with that as you've only been together since this morning..."
        iona @ sad "But looking at you all now, you already seem like such cute couples."
        iona "But at first glance, this boy seems like my type on paper."
        iona @ happy "He's smart, funny, and just dreamy."
        iona @ awkward "And although I don't want to break a promising couple up so early on..."
        iona @ serious "I'm here to make a choice and so..."
        "Everyone tenses."
        if s3e1p2_talk_to_new_girl:
            thought "Here she goes. About to pick [s3_mc.current_partner]..."
        else:
            thought "She better not pick [s3_mc.current_partner]."
        iona "The boy I'd like to couple up with is..."
        thought "Maybe she won't?"
        iona @ happy "[s3_mc.current_partner]."
    elif s3_mc.current_partner == "Harry":
        genevieve @ talk "I didn't know how to feel on the way here."
        genevieve "I was excited, obviously, but I knew I'd be taking a guy away from another girl."
        genevieve @ serious "I thought I'd be OK with that as you've only been together since this morning..."
        genevieve @ sad "But looking at you all now, you already seem like such cute couples."
        genevieve "But at first glance, this boy seems like my type on paper."
        genevieve @ happy "He's smart, funny, and just dreamy."
        genevieve @ awkward "And although I don't want to break a promising couple up so early on..."
        genevieve @ serious "I'm here to make a choice and so..."
        "Everyone tenses."
        if s3e1p2_talk_to_new_girl:
            thought "Here she goes. About to pick [s3_mc.current_partner]..."
        else:
            thought "She better not pick [s3_mc.current_partner]."
        genevieve "The boy I'd like to couple up with is..."
        thought "Maybe she won't?"
        genevieve @ happy "[s3_mc.current_partner]."

    # CHOICE
    menu:
        thought "[s3_3rd_girl] picked [s3_mc.current_partner]!"
        "I called it" if s3e1p2_talk_to_new_girl == True:
            pass
        "At least she told me" if s3e1p2_talk_to_new_girl == False:
            pass
        "No, dammit!":
            pass
        "Well, this sucks":
            pass

    if s3_mc.current_partner == "Harry":
        "Genevieve looks at you apologetically."
        genevieve @ sad "I'm so sorry, babe."
    "You hear sighs of relief and murmurs coming from the others."
    elladine sad "Oh no! Poor [s3_name]..."
    seb sad "Wow, that's brutal."
    nicky sad "Yeah, that's rough, man."

    # CHOICE
    menu:
        thought "[s3_3rd_girl]'s taken my guy..."
        "It is what it is":
            $ s3_mc.like(s3_3rd_girl)
            if s3_mc.current_partner == "Bill":
                "Miki smiles."
                miki @ happy "Thanks for understanding, [s3_name]."
            elif s3_mc.current_partner == "Camilo":
                "Iona smiles."
                iona @ happy "Thanks for understanding, [s3_name]."
            elif s3_mc.current_partner == "Harry":
                "Genevieve smiles."
                genevieve @ happy "Thanks for understanding, [s3_name]."
        "How could you?":
            $ s3_mc.dislike(s3_3rd_girl)
            if s3_mc.current_partner == "Bill":
                "Miki's face drops."
                miki sad "It was a really hard decision, babe. I didn't want to make it..."
            elif s3_mc.current_partner == "Camilo":
                "Iona's face drops."
                iona sad "It was a really hard decision, babe. I didn't want to make it..."
            elif s3_mc.current_partner == "Harry":
                "Genevieve's face drops."
                genevieve sad "It was a really hard decision, babe. I didn't want to make it..."
        "I'll be coming for him":
            if s3_mc.current_partner == "Bill":
                miki "Good."
                miki @ happy "I'm looking forward to the competition."
            elif s3_mc.current_partner == "Camilo":
                iona "Good."
                iona @ happy "I'm looking forward to the competition."
            elif s3_mc.current_partner == "Harry":
                genevieve "Good."
                genevieve @ happy "I'm looking forward to the competition."
        "At least you told me " if s3e1p2_talk_to_new_girl == True:
            $ s3_mc.like(s3_3rd_girl)
            if s3_mc.current_partner == "Bill":
                miki "I really didn't want it to be a surprise for you..."
            elif s3_mc.current_partner == "Camilo":
                iona "I really didn't want it to be a surprise for you..."
            elif s3_mc.current_partner == "Harry":
                genevieve "I really didn't want it to be a surprise for you..."

    "[s3_mc.current_partner] puts a hand on your back."

    if s3_mc.current_partner == "Bill":
        bill @ angry "I can't believe this."
        bill sad "I was blown away when you picked me. It's like I'd won the jackpot."
        bill "And now we're not a couple, less than a day after that..."
    elif s3_mc.current_partner == "Camilo":
        camilo @ angry "I can't believe this."
        camilo sad "I was blown away when you picked me. It's like I'd won the jackpot."
        camilo "And now we're not a couple, less than a day after that..."
    elif s3_mc.current_partner == "Harry":
        harry @ angry "I can't believe this."
        harry sad "I was blown away when you picked me. It's like I'd won the jackpot."
        harry "And now we're not a couple, less than a day after that..."
    "He stands to walk over to [s3_3rd_girl]."

    # CHOICE
    menu:
        thought "Bill's getting up to leave..."
        "Squeeze his hand":
            $ s3_mc.like(s3_mc.current_partner)
            if s3_mc.current_partner == "Bill":
                "You reach out, grab his hand, and give it a gentle squeeze. He stops in his tracks and turns back to you."
                bill @ flirt "Don't worry. I'll only be over there."
                s3_mc "But that's not here."
                bill "Yeah..."
                "He sighs, then continues over to [s3_3rd_girl]."
            elif s3_mc.current_partner == "Camilo":
                "You reach out, grab his hand, and give it a gentle squeeze. He stops in his tracks and turns back to you."
                camilo @ happy "Don't worry. I'll only be over there."
                s3_mc "But that's not here."
                camilo "Yeah..."
                "He sighs, then continues over to [s3_3rd_girl]."
            elif s3_mc.current_partner == "Harry":
                "You reach out, grab his hand, and give it a gentle squeeze. He stops in his tracks and turns back to you."
                harry @ flirt "Don't worry. I'll only be over there."
                s3_mc "But that's not here."
                harry "Yeah..."
                "He sighs, then continues over to [s3_3rd_girl]."
        "Drag him back":
            if s3_mc.current_partner == "Bill":
                "You reach out, wrap your fingers around his arm, and pull."
                bill @ talk "Agh!"
                "He lurches back, loses his balance and falls hard onto the seat."
                "Seb and Nicky let out a laugh. Elladine raises an eyebrow at you."
                bill @ awkward "Ow, my bum!"
                bill "These cushions are weirdly firm."
                "He looks at you with a puzzled expression."
                s3_mc "Sorry..."
                bill @ flirt -sad"Don't worry. Look, I'm only going to be over there."
                s3_mc "But that's not here."
                "He gets back up and makes his way over to [s3_3rd_girl]."
            elif s3_mc.current_partner == "Camilo":
                "You reach out, wrap your fingers around his arm, and pull."
                camilo @ talk "Agh!"
                "He lurches back, loses his balance and falls hard onto the seat."
                "Seb and Nicky let out a laugh. Elladine raises an eyebrow at you."
                camilo @ awkward "Ow, my bum!"
                camilo "These cushions are weirdly firm."
                "He looks at you with a puzzled expression."
                s3_mc "Sorry..."
                camilo @ happy -sad "Don't worry. Look, I'm only going to be over there."
                s3_mc "But that's not here."
                "He gets back up and makes his way over to [s3_3rd_girl]."
            elif s3_mc.current_partner == "Harry":
                "You reach out, wrap your fingers around his arm, and pull."
                harry @ talk "Agh!"
                "He lurches back, loses his balance and falls hard onto the seat."
                "Seb and Nicky let out a laugh. Elladine raises an eyebrow at you."
                harry @ awkward "Ow, my bum!"
                harry "These cushions are weirdly firm."
                "He looks at you with a puzzled expression."
                s3_mc "Sorry..."
                harry @ happy -sad "Don't worry. Look, I'm only going to be over there."
                s3_mc "But that's not here."
                "He gets back up and makes his way over to [s3_3rd_girl]."
        "Wave goodbye":
            "You slowly wave at [s3_mc.current_partner] as he makes his way over to [s3_3rd_girl]."
            "He turns, sees you, and does a small, reassuring wink."
            thought "There he goes..."
            "[s3_mc.current_partner] nods at [s3_3rd_girl]."

    if s3_mc.current_partner == "Bill":
        bill @ flirt "Alright, girl?"
        miki happy "I'm good, you?"
    elif s3_mc.current_partner == "Camilo":
        camilo @ flirt "Hiya, you alright?"
        iona happy "I'm good, you?"
    elif s3_mc.current_partner == "Harry":
        harry @ flirt "Hey! How are you doing?"
        genevieve happy "I'm good, you?"

    "[s3_mc.current_partner] shrugs. He and [s3_3rd_girl] share a clumsy hug."
    s3_mc "I got a text..."
    s3_mc "I swear, if this is me getting dumped already I'm gonna be livid."
    aj sad "That wouldn't happen already, right?"
    seb sad "It isn't unheard of."
    elladine sad "Read it out, hun."

    text "[s3_name], [s3_3rd_girl] has taken your partner, leaving you single..."

    s3_mc "Ugh."

    text "...so get ready to mingle. #getthatgrafton #thesinglelife"

    aj @ talk -sad "What's that all mean?"
    s3_mc "I'm...safe?"
    elladine @ talk -sad "Phew! Not gonna lie but that would have been proper cruel."

    # IF STATEMENT
    if s3_mc.bisexual == True:
        aj @ very_happy "Yay!"
        aj @ flirt "Single and ready to mingle, eh?"
        aj @ flirt "Guess we'll need to keep a close eye on you."
    else:
        aj @ happy "Ooh..."
        genevieve @ happy "Single and ready to mingle, eh?"
        genevieve @ happy "Guess we'll need to keep a close eye on you."

    "Nicky gets up and stretches."
    nicky -sad "I don't know about you lot, but my bum's gone numb."
    "He makes his way over to [s3_3rd_girl]."

    # CHOICE
    menu:
        thought "Should I go and talk to [s3_3rd_girl]?"
        "Walk over to [s3_3rd_girl]":
            scene s3-lawn-night with dissolve
            $ on_screen = []

            if s3_mc.current_partner == "Bill":
                "You make your way over to [s3_3rd_girl] along with Nicky, Genevieve and Iona."
                genevieve @ happy "Hey, girl!"
                miki @ happy "Hi!"
                nicky "Thought we'd come over and chat properly."
                "Iona gives you a sympathetic look before turning to [s3_3rd_girl]."
                iona "I hope you're alright. That was a tough decision for anyone to make."
                genevieve "Yeah, I'm so glad it wasn't me doing it."
                "[s3_3rd_girl] goes to speak, but looks at you instead."
                miki "Sorry, all. Can I have a quick word with [s3_name] first?"
            elif s3_mc.current_partner == "Camilo":
                "You make your way over to [s3_3rd_girl] along with Nicky, Miki and Genevieve."
                miki @ happy "Hey, girl!"
                iona @ happy "Hi!"
                nicky "Thought we'd come over and chat properly."
                "Genevieve gives you a sympathetic look before turning to [s3_3rd_girl]."
                genevieve "I hope you're alright. That was a tough decision for anyone to make."
                miki "Yeah, I'm so glad it wasn't me doing it."
                "[s3_3rd_girl] goes to speak, but looks at you instead."
                iona "Sorry, all. Can I have a quick word with [s3_name] first?"
            elif s3_mc.current_partner == "Harry":
                "You make your way over to [s3_3rd_girl] along with Nicky, Miki and Iona."
                miki @ happy "Hey, girl!"
                genevieve @ happy "Hi!"
                nicky "Thought we'd come over and chat properly."
                "Iona gives you a sympathetic look before turning to [s3_3rd_girl]."
                iona "I hope you're alright. That was a tough decision for anyone to make."
                miki "Yeah, I'm so glad it wasn't me doing it."
                "[s3_3rd_girl] goes to speak, but looks at you instead."
                genevieve "Sorry, all. Can I have a quick word with [s3_name] first?"
            nicky "Oh yeah, no problem."
            "Nicky winks at you as he ushers the others away... including [s3_mc.current_partner]."
        "Stay where you are":
            scene s3-firepit-night
            $ on_screen = []
            "You stay back while everyone around you gets up and goes off in their own little groups."
            "The flames of the fire flicker and twirl. You soon find yourself lost in thought."
            # CHOICE
            menu:
                thought "I can't stop thinking about..."
                "How I'm single again":
                    thought "Like, I literally came here to stop being single!"
                "All the mingling I'm going to do":
                    thought "This is a blessing. It means I'll get to do as much grafting as I want."
                "Chinstrap penguins...":
                    thought "They're just so silly! It's like they're wearing helmets all the time."
            "Just then, a voice snaps you out of your thoughts."
            # IF STATEMENT
            if s3_mc.current_partner == "Bill":
                miki serious "[s3_name]?"
                s3_mc "Huh?"
            elif s3_mc.current_partner == "Camilo":
                iona serious "[s3_name]?"
                s3_mc "Huh?"
            elif s3_mc.current_partner == "Harry":
                genevieve serious "[s3_name]?"
                s3_mc "Huh?"
        "Walk away from the others":
            scene s3-sun-loungers-night with dissolve
            $ on_screen = []
            "You get up, leaving the rest of the Islanders to form their own little groups."
            "The night is surprisingly chilly. You rub your arms for some warmth."
            "The sound of laughter drifts over from the other Islanders."
            # IF STATEMENT
            if s3_mc.current_partner == "Bill":
                miki "Cold?"
                "You turn and see Miki standing in front of you. A concerned look on her face."
                miki @ awkward "Me too. And I thought Cambridge could get chilly!"
                miki "Sometimes the boat's little heater isn't enough, you know?"
                "She rubs her arm."
            elif s3_mc.current_partner == "Camilo":
                iona "Cold?"
                "You turn and see Iona standing in front of you. A concerned look on her face."
                "She rubs her arm."
            elif s3_mc.current_partner == "Harry":
                genevieve "Cold?"
                "You turn and see Genevieve standing in front of you. A concerned look on her face."
                genevieve @ awkward "I nearly forgot to pack a cardigan for the colder evenings."
                "She rubs her arm."

    if s3_mc.current_partner == "Bill":
        miki serious "Um, I'd like to clear the air with you."
        s3_mc "Sure...let's talk."
        scene s3-poolside-night with dissolve
        $ on_screen = []
        miki @ happy "Thanks."
        miki serious "I want you to know that it wasn't anything personal. I mean, obviously, I've only just met you."
        if s3e1p2_talk_to_new_girl:
            miki "That's why I told you earlier who I was going to pick, so it wasn't a shock."
        else:
            miki "I wanted to tell you earlier, but we didn't get any time to chat."
            miki "I didn't want it to come as a shock."
        miki @ sad "At the end of the day, I had to pick someone."
        miki "But I actually think this puts you in a really strong position. You're now free to chat and flirt with whoever you want."
        miki happy "Even if that person is Bill. Like, all's fair. I won't make a fuss."
        miki "Early days and all that."
        "She pauses."
        miki "So...friends?"
    elif s3_mc.current_partner == "Camilo":
        iona serious "Um, I'd like to clear the air with you."
        s3_mc "Sure...let's talk."
        scene s3-poolside-night with dissolve
        $ on_screen = []
        iona @ happy "Thanks."
        iona serious "I want you to know that it wasn't anything personal. I mean, obviously, I've only just met you."
        if s3e1p2_talk_to_new_girl:
            iona "That's why I told you earlier who I was going to pick, so it wasn't a shock."
        else:
            iona "I wanted to tell you earlier, but we didn't get any time to chat."
            iona "I didn't want it to come as a shock."
        iona @ sad "At the end of the day, I had to pick someone."
        iona "But I actually think this puts you in a really strong position. You're now free to chat and flirt with whoever you want."
        iona happy "Even if that person is Camilo. Like, all's fair. I won't make a fuss."
        iona "Early days and all that."
        "She pauses."
        iona "So...friends?"
    elif s3_mc.current_partner == "Harry":
        genevieve serious "Um, I'd like to clear the air with you."
        s3_mc "Sure...let's talk."
        scene s3-poolside-night with dissolve
        $ on_screen = []
        genevieve @ happy "Thanks."
        genevieve serious "I want you to know that it wasn't anything personal. I mean, obviously, I've only just met you."
        if s3e1p2_talk_to_new_girl:
            genevieve "That's why I told you earlier who I was going to pick, so it wasn't a shock."
        else:
            genevieve "I wanted to tell you earlier, but we didn't get any time to chat."
            genevieve "I didn't want it to come as a shock."
        genevieve @ sad "At the end of the day, I had to pick someone."
        genevieve @ happy "But I actually think this puts you in a really strong position. You're now free to chat and flirt with whoever you want."
        genevieve -serious "Even if that person is Harry. Like, all's fair. I won't make a fuss."
        genevieve "Early days and all that."
        "She pauses."
        genevieve happy "So... friends?"

    # CHOICE
    menu:
        thought "Should I forgive [s3_3rd_girl] for choosing [s3_mc.current_partner]?"
        "Hey, it's fine. It was a tough call":
            $ s3_mc.like(s3_3rd_girl)
            "[s3_3rd_girl]'s shoulders relax with relief."
            if s3_mc.current_partner == "Bill":
                miki @ very_happy "Thanks, babe! You have no idea how awkward I was feeling."
                miki "You're so understanding."
                "She squeezes your arm lightly."
                miki "Come on, then. We should get back to the others."
            elif s3_mc.current_partner == "Camilo":
                iona "Thanks, babe! You have no idea how awkward I was feeling."
                iona -serious "You're so understanding."
                "She squeezes your arm lightly."
                iona "Come on, then. We should get back to the others."
            elif s3_mc.current_partner == "Harry":
                genevieve "Thanks, babe! You have no idea how awkward I was feeling."
                genevieve -serious "You're so understanding."
                "She squeezes your arm lightly."
                genevieve "Come on, then. We should get back to the others."
            "You walk back together."
        "I'm sorry, but I need some time":
            $ s3_mc.dislike(s3_3rd_girl)
            "[s3_3rd_girl] gaze falls to the ground. She lets out a heavy sigh."
            if s3_mc.current_partner == "Bill":
                miki @ sad "I understand..."
                miki serious "Look, I hope we can still be friends someday, you know?"
                s3_mc "Hmm."
                "She looks back at the others."
                miki -serious "Alright, I guess I should get back over there."
            elif s3_mc.current_partner == "Camilo":
                iona @ sad "I understand..."
                iona serious "Look, I hope we can still be friends someday, you know?"
                s3_mc "Hmm."
                "She looks back at the others."
                iona -serious "Alright, I guess I should get back over there."
            elif s3_mc.current_partner == "Harry":
                genevieve @ sad "I understand..."
                genevieve serious "Look, I hope we can still be friends someday, you know?"
                s3_mc "Hmm."
                "She looks back at the others."
                genevieve -serious "Alright, I guess I should get back over there."
            "[s3_3rd_girl] walks back on her own."
        "Relax, girl! I'd known him for two minutes":
            $ s3_mc.like(s3_3rd_girl)
            if s3_mc.current_partner == "Bill":
                miki @ talk "Hah!"
                "She tries to stop herself from laughing."
                miki @ awkward "Ah, I'm sorry..."
                miki "I'm just relieved."
                miki -happy "I really hate the idea of getting on the wrong side of someone in here."
                miki "Especially on the first day!"
                "A burst of laughter from the other group makes her turn her head."
                miki @ happy "Sounds like they're having fun. Come on, let's get back there."
            elif s3_mc.current_partner == "Camilo":
                iona @ talk "Hah!"
                "She tries to stop herself from laughing."
                iona @ awkward "Ah, I'm sorry..."
                iona "I'm just relieved."
                iona -happy "I really hate the idea of getting on the wrong side of someone in here."
                iona "Especially on the first day!"
                "A burst of laughter from the other group makes her turn her head."
                iona @ happy "Sounds like they're having fun. Come on, let's get back there."
            elif s3_mc.current_partner == "Harry":
                genevieve @ talk "Hah!"
                "She tries to stop herself from laughing."
                genevieve @ awkward "Ah, I'm sorry..."
                genevieve "I'm just relieved."
                genevieve -happy "I really hate the idea of getting on the wrong side of someone in here."
                genevieve "Especially on the first day!"
                "A burst of laughter from the other group makes her turn her head."
                genevieve @ happy "Sounds like they're having fun. Come on, let's get back there."
            "The two of you make your way to the others."

    scene s3-firepit-night with dissolve
    $ on_screen = []
    "Seb, Nicky, Elladine and Genevieve are sat around the firepit chatting"
    thought "I could do with someone to talk to."

    "{i}Island Amore isn't just about romance. It's also about the friendships you form along the way. One of these four Islanders is going to be a close friend for the rest of your time in the Villa.{/i}"

    thought "People can get attached pretty quickly in this Villa. I should think about who I want to be friends with..."
    thought "I don't think I've ever met anyone as positive as Elladine."
    thought "I feel like she's the kind of person that always has a funny story to share or a comfortable shoulder to cry on."
    if s3_mc.current_partner == "Harry":
        thought "Genevieve did just pick Harry, but she was in a tough position..."
        thought "And she actually seems kinda lovely... I feel like she's used to dealing with people and understands how to navigate tricky issues..."
    else:
        thought "I feel like Genevieve is used to dealing with people and understands how to navigate tricky issues..."
        thought "Plus, she just seems lovely."
    thought "I don't get romantic vibes off Seb and Nicky. I definitely see them more as friends than romantic partners."
    thought "Nicky already strikes me as a proper joker. He's got an 'older bro' vibe to him."
    thought "Seb's got this darker side to him. Like, he's got the most life experience here and will just say things how they are..."

    # CHOICE
    menu:
        thought "Who should I speak to?"
        "Elladine":
            $ s3_mc.bff = 'Elladine'
        "Genevieve":
            $ s3_mc.bff = 'Genevieve'
        "Nicky":
            $ s3_mc.bff = 'Nicky'
        "Seb":
            $ s3_mc.bff = 'Seb'

    call s3e1p3_best_friend_chat from _call_s3e1p3_best_friend_chat
    
    if s3e1p3_prank:
        call s3e1p3_prank from _call_s3e1p3_prank

    # Uncomment if MC imgs are added to game.
    # scene s3-dressing-room with dissolve
    # $ on_screen = []

    # thought "Right, first night in the Villa and I'm single. It's worth going all out tonight."
    # thought "I want the others to see who they're dealing with..."

    # # MC outfit change to sleepwear

    # $ outfit = "pjs"

    # thought "This outfit is beyond cute."

    scene s3-bathroom with dissolve
    $ on_screen = []

    "You squeeze some toothpaste onto your brush and begin to clear your teeth."
    "You hear the bathroom door open and close. You turn to see AJ standing there, towel in hand."
    aj @ awkward "Oh, sorry! I should have knocked."
    s3_mc "Thawt's oclay, garl."
    "She laughs."
    aj @ happy "What?"
    "You try to speak again but a dribble of toothpaste makes it's way down your chin instead."
    "You quickly wipe it away."
    s3_mc "Whurlps!"
    aj @ happy "Hah! Gross."
    aj "Don't mind me, hun. I'm just going to brush my teeth as well."
    "She looks you up and down quickly."
    aj @ flirt "I didn't think pyjamas could look so good. You're making me jealous."
    "She picks up her brush and begins to vigorously clean her teeth."
    thought "I've never seen someone brush their teeth so hard and fast..."
    aj @ talk "Schwo, howsh shings?"
    s3_mc "Hmm?"
    "She chuckles and leans in towards the sink."
    "The two of you go to use it at the same time and gently bump into each other."
    if s3_mc.bisexual == True:
        show aj awkward
        "AJ's face flushes red."
    else:
        show aj happy
        "AJ giggles."
    "She gestures to the sink. You quickly rinse your mouth."
    s3_mc "Thanks."
    "AJ does the same."
    aj -happy -awkward "No problem."
    "She grins at you as she wipes her mouth with her towel."
    aj "Ahh, minty fresh."
    aj "I asked how's things?"

    # CHOICE
    menu:
        s3_mc "Things are..."
        "Great!":
            aj @ happy "Glad to hear it."
        "All a bit much":
            aj @ serious "Aw, sorry, babes."
        "What they are":
            aj "That sounds like something Seb would say..."

    "AJ slowly plays with the towel in her hands."
    
    if s3_mc.bisexual == True:
        "AJ slowly plays with the towel in her hands."
        aj awkward "So, um, [s3_name]?"
        s3_mc "Yeah?"
        aj -awkward "Earlier you said you're interested in women, too..."
        s3_mc "Yeah..."
        aj  "Well, like, I was wondering if, y'know, now that you're single..."
        aj awkward "Wow, I'm usually so much more direct than this, but I'm a bag of nerves right now!"
        "She laughs and bites her lip."
        aj flirt "Look, I think you're well cute and, honestly, in a whole different league to the guys here."
        aj awkward "Could something maybe happen between us?"

        # CHOICE
        menu:
            thought "Am I interested in AJ?"
            "Um, I don't think so, sorry":
                $ s3_mc.dislike("AJ")
                aj @ serious "Aw, oh well."
                aj @ happy -awkward "Don't ask, don't get, right?"
            "One hundred percent yes":
                $ s3_mc.like("AJ")
                $ s3_like_aj = True
                $ s3_lis.append("AJ")
                aj @ very_happy "Amazing!"
                show aj awkward
                "She looks at you, her cheeks flushing again."
                show aj happy
                "AJ looks at you and laughs."
                s3_mc "What's wrong?"
                aj -happy -awkward "Oh, nothing, really."
                s3_mc "Really?"
                aj @ flirt "Yeah, you look gorgeous as usual."
                aj  "But you've just got a tiny stray lash on your face."
                aj @ flirt "Stay still, I'll get it for you."
                "She moves closer. You can feel her breath on your cheek."
                "She gently removes the eyelash from your face and blows it to one side."
                aj @ happy "I made a wish on that eyelash, by the way."
        
        # CHOICE
        menu:
            thought "AJ just made a wish on my eyelash.."
            "We can't both wish on the eyelash":
                "EMPTY"
                # NEED TO FILL
            "Maybe we wished for the same thing...":
                aj flirt "Maybe we did..."
                "She bites her lower lip, her eyes look longingly at your face."
            "What did you wish for?":
                aj @ awkward "I can't tell you because then it might not come true."
                aj flirt "But I can show you."

        # CHOICE
        menu:
            thought "I think I know what AJ wished for..."
            "Kiss her":
                $ s3_mc.like("AJ")
                "You lean in towards AJ and whisper softly in her ear."
                s3_mc "Your wish is my command."
                show aj flirt
                "She closes her eyes again. Your lips gently touch for a moment. It's soft and earnest."
                "She draws you closer with her hand on the nape of your neck."
                "You melt into one another for a few moments."
                "Your hands explore each other's bodies."
                "Your heart flutters a little as you both pull away."
                aj "You've got some powerful eyelashes, [s3_name]."
                aj @ very_happy "Because my wish just totally came true."
            "Wait and see if she kisses me":
                $ s3_mc.like("AJ")
                "You look at her shyly, your cheeks flush red."
                s3_mc "Show me then."
                show aj flirt
                "She smiles, closes her eyes, and leans towards you."
                "AJ lighty kisses your lips and you instantly move in closer, drawn to her touch."
                "You want to be as close to her as possible. She kisses you softly, her hands slowly explore your body."
                "Your heart flutters a little as you both pull away."
                aj -flirt "That was my wish, by the way."
                aj @ happy "To kiss you."
                s3_mc "I gathered."
            "Change the subject":
                "EMPTY"
                # NEED TO FILL
        aj @ talk "It is such a weird tradition, isn't it?"
        aj "I bet someone from ages ago, like, made a wish after finding an eyelash and it came true and they told all their mates."
        aj @ happy "And now we all believe in the power of the eyelash."
        "AJ smiles at you."
        aj @ flirt "I hope we get to spend more time together in the Villa."
        aj @ happy "Being alone with you is like..."
        aj @ awkward "I don't know how to describe it with, like, words and stuff..."
        aj @ flirt "But I know I want more of it."
    else:
        aj "So, you got your eye on any of the guys here?"
        # CHOICE
        menu:
            thought "Which guy do I have my eye on?"
            "Harry":
                aj @ happy "Ooh, he's well cute and a right laugh!"
                aj "He likes to swim like me, too!"
                if s3_mc.current_partner == "Harry":
                    aj "It sucks that you don't get to spend your first night here with him."
            "Camilo":
                aj @ happy "Can't fault you there!"
                aj "Strong athletic type with a heart of gold."
                "She swoons dramatically."
                if s3_mc.current_partner == "Camilo":
                    aj "It sucks that you don't get to spend your first night here with him."
            "Bill":
                aj @ talk "Hah! Really?"
                aj @ awkward "Sorry, that was well rude."
                aj "It's just, he's got an opinion on everything!"
                aj "Though, he's kinda funny, I'll give you that."
                if s3_mc.current_partner == "Bill":
                    aj "It sucks that you don't get to spend your first night here with him."
            "Nobody so far...":
                s3_mc "I definitely don't get a romantic vibe off Nicky or Seb, and none of the other three really stand out yet..."
                aj @ happy "Well, I'm sure there are more to come."

    "A knock on the door breaks you both out of your conversation."

    scene s3-bedroom-night with dissolve
    $ on_screen = []

    seb serious "Hey, you done yet?"
    seb "There's half a dozen people out here waiting to use the loo."
    seb @ awkward "Some are in more desperate need than others!"

    scene s3-bathroom with dissolve
    $ on_screen = []

    show aj at npc_center
    s3_mc "Whoops."
    "AJ chuckles again."
    aj @ happy "I guess we should go."

    scene sand with dissolve
    $ on_screen = []

    "Don't fret, [s3_name]! So, you've lost [s3_mc.current_partner], but at least you've got a bed!"
    "I don't even have a sleeping bag! All the budget's gone on biscuits for the Islanders to argue over."
    "Not that they appreciate my sacrifice!"
    "Next time on Island Amore..."
    "Seb says something appalling at breakfast..."

    show seb at npc_center
    seb "I really want some black pudding."
    show seb at npc_exit
    pause 0.3
    $ renpy.hide("seb")

    "Eww!"
    "And [s3_name] gets grafting..."
    s3_mc "Let me ride you..."
    "And we've got a whole bunch of other surprises lined up for you."
    "It's a whole new series! I can't wait to see what's going to happen."
    
    jump s3e2p1

    return

## LABELS FOR EPISODE 1 PART 3
label s3e1p3_best_friend_chat:
    "You make your way over to where [s3_mc.bff] is sitting with the others."
    elladine @ happy "Hey, [s3_name]!"
    if s3_mc.current_partner == "Harry":
        genevieve @ happy "Join us! We're staying close to the fire for warmth."
        seb "Yeah, right? I thought it'd be baking."
        seb "Didn't realise I'd need a fluffy onesie at night"
    s3_mc "Hey, [s3_mc.bff]..."

    $ pronouns(s3_mc.bff)
    $ s3_mc.like(s3_mc.bff)
    if s3_mc.bff == "Elladine":
        elladine "Yeah?"
        s3_mc "Could I speak to you in private?"
        elladine @ happy "Of course, hun!"
        elladine "Roof terrace?"
        s3_mc "Sounds good!"
        "The two of you make your way upstairs."
    elif s3_mc.bff == "Genevieve":
        genevieve "Yeah?"
        s3_mc "Could I speak to you in private?"
        genevieve @ happy "Of course, babes!"
        genevieve "Roof terrace?"
        s3_mc "Sounds good!"
        "The two of you make your way upstairs."
    elif s3_mc.bff == "Nicky":
        nicky "Yeah?"
        s3_mc "Could I speak to you in private?"
        nicky @ happy "Yeah, man. Let's go."
        nicky "Roof terrace?"
        s3_mc "Sounds good!"
        "The two of you make your way upstairs."
    elif s3_mc.bff == "Seb":
        seb "Yeah?"
        s3_mc "Could I speak to you in private?"
        seb @ happy "Yeah, man. Let's go."
        "He turns to the others."
        seb "I guess if AJ comes by, let her know I'll be back in a bit."
        seb "Where is she, anyway?"
        nicky @ awkward "I think she said something about taking a midnight splash."
        "Seb shakes his head."
        seb @ serious "Too much energy in that one..."
        seb "Roof terrace?"
        s3_mc "Sounds good!"
        "The two of you make your way upstairs."

    scene s3-roof-night with dissolve
    $ on_screen = []

    # IF STATEMENT
    if s3_mc.bff == "Genevieve" and s3_mc.current_partner == "Harry":
        "After having Harry taken from her by Genevieve, [s3_name]'s made the interesting decision to confide in her."
        "Could this be the start of a beautifully awkward friendship?"
    else:
        "After having [s3_mc.current_partner] taken from her, [s3_name] and [s3_mc.bff] have come to the terrace to talk it over."
        "I get the feeling that this could be the start of a beautiful friendship..."
    "You and [s3_mc.bff] make your way to the nearest sofa and take a seat that overlooks the rest of the Villa."
    "There's a splash, then AJ emerges from the pool. She runs around to the other side, then cannonballs in again."

    if s3_mc.bff == "Elladine":
        elladine @ talk "I bet that girl's never been tired in her life..."
    elif s3_mc.bff == "Genevieve":
        genevieve @ talk "I bet that girl's never been tired in her life..."
    elif s3_mc.bff == "Nicky":
        nicky @ talk "I bet that girl's never been tired in her life..."
    elif s3_mc.bff == "Seb":
        seb @ talk "I bet that girl's never been tired in her life..."

    # CHOICE
    menu:
        thought "AJ seems to be bursting with energy..."
        "I wish I was more like that":
            if s3_mc.bff == "Elladine":
                elladine @ talk "Right?"
                elladine "I just don't get how some people can be so active. I'm useless without two coffees in the morning."
            elif s3_mc.bff == "Genevieve":
                genevieve @ talk "Right?"
                genevieve "I just don't get how some people can be so active. I'm useless without two coffees in the morning."
            elif s3_mc.bff == "Nicky":
                nicky @ talk "Right?"
                nicky "I just don't get how some people can be so active. I'm useless without two coffees in the morning."
            elif s3_mc.bff == "Seb":
                seb @ talk "Right?"
                seb "I just don't get how some people can be so active. I'm useless without two coffees in the morning."
        "I get tired just watching her":
            if s3_mc.bff == "Elladine":
                elladine @ talk "Right?"
                elladine "I just don't get how some people can be so active. I'm useless without two coffees in the morning."
            elif s3_mc.bff == "Genevieve":
                genevieve @ talk "Right?"
                genevieve "I just don't get how some people can be so active. I'm useless without two coffees in the morning."
            elif s3_mc.bff == "Nicky":
                nicky @ talk "Right?"
                nicky "I just don't get how some people can be so active. I'm useless without two coffees in the morning."
            elif s3_mc.bff == "Seb":
                seb @ talk "Right?"
                seb "I just don't get how some people can be so active. I'm useless without two coffees in the morning."
        "Maybe she'll keep me on my toes...":
            if s3_mc.bff == "Elladine":
                if s3_mc.bisexual == True:
                    elladine "Ooh, is there a little chemistry, there?"
                elladine "She seems like a dynamo. Maybe the two of you should work out together."
                elladine "Get the old heart rate going."
            elif s3_mc.bff == "Genevieve":
                if s3_mc.bisexual == True:
                    genevieve "Ooh, is there a little chemistry, there?"
                genevieve "She seems like a dynamo. Maybe the two of you should work out together."
                genevieve "Exercise releases endorphins, which can help you feel happy."
                s3_mc "Wow, am I getting medical advice from Doctor Viv?"
                genevieve @ happy "My full title is actually Doctor Aliu, but I like Doctor Viv."
            elif s3_mc.bff == "Nicky":
                if s3_mc.bisexual == True:
                    nicky "Ooh, is there a little chemistry, there?"
                nicky "She seems like a dynamo. Maybe the two of you should work out together."
                nicky "Get the old heart rate going."
            elif s3_mc.bff == "Seb":
                if s3_mc.bisexual == True:
                    seb "Ooh, is there a little chemistry, there?"
                seb "She seems like a dynamo. Maybe the two of you should work out together."
                seb "Get the old heart rate going."
            
    if s3_mc.bff == "Genevieve" and s3_mc.current_partner == "Harry":
        genevieve "Thanks again for accepting my apology earlier."
        genevieve "I really didn't want there to be any bad feelings between us."
    "There's a moment of silence as the two of you watch the other Islanders roam around the Villa."

    if s3_mc.bff == "Elladine":
        elladine serious "So, how are you doing?"
        elladine "Tonight must have been tough..."
    elif s3_mc.bff == "Genevieve":
        genevieve sad "So, how are you doing?"
        genevieve "Tonight must have been tough..."
    elif s3_mc.bff == "Nicky":
        nicky sad "So, how are you doing?"
        nicky "Tonight must have been tough..."
    elif s3_mc.bff == "Seb":
        seb sad "So, how are you doing?"
        seb "Tonight must have been tough..."

    # CHOICE
    menu:
        s3_mc "I'm doing..."
        "Pretty good, all things considered":
            s3_mc "I'm OK. Anyway, it's only the first day, still."
            if s3_mc.bff == "Elladine":
                elladine @ happy -serious "Exactly! You're thinking smart here."
            elif s3_mc.bff == "Genevieve":
                genevieve @ happy -serious "Exactly! You're thinking smart here."
            elif s3_mc.bff == "Nicky":
                nicky @ happy -serious "Exactly! You're thinking smart here."
            elif s3_mc.bff == "Seb":
                seb @ happy -serious "Exactly! You're thinking smart here."
        "Meh, my head's all over the place":
            if s3_mc.bff == "Elladine":
                elladine "That's understandable. You've already been through a dumping and it's only the first day."
            elif s3_mc.bff == "Genevieve":
                genevieve "That's understandable. You've already been through a dumping and it's only the first day."
            elif s3_mc.bff == "Nicky":
                nicky "That's understandable. You've already been through a dumping and it's only the first day."
            elif s3_mc.bff == "Seb":
                seb "That's understandable. You've already been through a dumping and it's only the first day."
        "Great! I'm single and ready to mingle!":
            s3_mc "...again."
            s3_mc "As everyone keeps saying."
            if s3_mc.bff == "Genevieve":
                "Genevieve laughs."
                genevieve @ happy -serious "Good to see it hasn't dampened your spirit."
            elif s3_mc.bff == "Seb":
                "Seb laughs."
                seb @ happy -serious "Good to see it hasn't dampened your spirit."
            elif s3_mc.bff == "Nicky":
                "Nicky laughs."
                nicky @ happy -serious "Good to see it hasn't dampened your spirit."
            elif s3_mc.bff == "Elladine":
                "Elladine laughs."
                elladine @ happy -serious "Good to see it hasn't dampened your spirit."

    # IF STATEMENT
    if s3_mc.bff == "Elladine":
        "Elladine smiles at you."
        elladine "Want to know what I think?"
        s3_mc "Go on."
        elladine @ talk "The way I see it, you're actually in one of the best positions in the Villa."
        elladine "You can graft on whoever you want to now, and no one can really have a problem with you for it."
        elladine "You can get to know everyone before the next recoupling!"
        elladine @ happy "I'd say that's better than pairing up with a stranger straight away."
    elif s3_mc.bff == "Genevieve":
        "Genevieve smiles at you."
        genevieve "Want to know what I think?"
        s3_mc "Go on."
        genevieve @ talk "The way I see it, you're actually in one of the best positions in the Villa."
        genevieve "You can graft on whoever you want to now, and no one can really have a problem with you for it."
        genevieve "You can get to know everyone before the next recoupling!"
        genevieve @ happy "I'd say that's better than pairing up with a stranger straight away."
    elif s3_mc.bff == "Nicky":
        "Nicky stretches and lays his arm down across the top of the seat."
        nicky "Do you want to hear what I think about your situation?"
        s3_mc "Go on."
        nicky @ talk "The way I see it, you're actually in one of the best positions in the Villa."
        nicky "You can graft on whoever you want to now, and no one can really have a problem with you for it."
        nicky "You can get to know everyone before the next recoupling!"
        nicky @ happy "I'd say that's better than pairing up with a stranger straight away."
    elif s3_mc.bff == "Seb":
        "Seb coughs and tucks his hair behind his ear"
        seb "So, um, I've been thinking about your situation..."
        s3_mc "Go on."
        seb @ talk "The way I see it, you're actually in one of the best positions in the Villa."
        seb "You can graft on whoever you want to now, and no one can really have a problem with you for it."
        seb "You can get to know everyone before the next recoupling!"
        seb @ happy "I'd say that's better than pairing up with a stranger straight away."

    # CHOICE
    menu:
        thought "[s3_mc.bff] thinks that being single at the start is better..."
        "You make a good point":
            if s3_mc.bff == "Elladine":
                elladine happy "Of course I do. I'm a fountain of knowledge."
            elif s3_mc.bff == "Genevieve":
                genevieve happy "Of course I do. I'm a fountain of knowledge."
            elif s3_mc.bff == "Nicky":
                nicky happy "Of course I do. I'm a fountain of knowledge."
            elif s3_mc.bff == "Seb":
                seb happy "There's a first time for everything."
        "But what if I already like [s3_mc.current_partner]?":
            if s3_mc.bff == "Elladine":
                elladine @ talk "Then go out and get him back!"
                elladine "Tomorrow is when the real grafting starts. You've just gotta keep your eyes on the prize."
            elif s3_mc.bff == "Genevieve" and s3_mc.current_partner == "Harry":
                genevieve @ talk "Well, there's nothing wrong with a bit of healthy competition, is there?"
                genevieve "Tomorrow is when the real grafting starts. You've just gotta keep your eyes on the prize."
            elif s3_mc.bff == "Genevieve":
                genevieve @ talk "Then go out and get him back!"
                genevieve "Tomorrow is when the real grafting starts. You've just gotta keep your eyes on the prize."
            elif s3_mc.bff == "Nicky":
                nicky @ talk "Then go out and get him back!"
                nicky "Tomorrow is when the real grafting starts. You've just gotta keep your eyes on the prize."
            elif s3_mc.bff == "Seb":
                seb @ talk "Then go out and get him back!"
                seb "Tomorrow is when the real grafting starts. You've just gotta keep your eyes on the prize."
        "I'm going to graft so hard":
            if s3_mc.bff == "Elladine":
                elladine @ happy "Yeah, you are!"
                "She pokes you in the ribs."
            elif s3_mc.bff == "Genevieve":
                genevieve @ happy "That makes me happy to hear."
            elif s3_mc.bff == "Nicky":
                nicky @ happy "Yeah, you are!"
                "He pokes you in the ribs."
            elif s3_mc.bff == "Seb":
                seb @ happy "That makes me happy to hear."

    "[s3_mc.bff] looks out thoughtfully at the view."
    # IF STATEMENT
    if s3_mc.bff == "Elladine":
        "The two of you say nothing for a while, taking in the moment in silence."
        elladine @ talk "I still can't believe we're here. It doesn't feel real!"
        s3_mc "Feels pretty real to me. I've just had my man snatched."
        elladine "It's only the start, hun."
        elladine "But seriously, look at where we are. The Island Amore Villa!"
        elladine "This place is lush, don't you think?"
    elif s3_mc.bff == "Genevieve":
        genevieve "It's well dark already, isn't it?"
        s3_mc "Yeah, it is actually."
        genevieve @ talk "I can't believe we're in here looking for love."
        genevieve "Such a weird, like, concept, isn't it?"
        genevieve "We're on an Island doing some kind of treasure hunting or something..."
        genevieve "And the prize is that you might fall in love."
    elif s3_mc.bff == "Nicky":
        nicky "It's well dark already, isn't it?"
        s3_mc "Yeah, it is actually."
        nicky @ talk "I can't believe we're in here looking for love."
        nicky "Such a weird, like, concept, isn't it?"
        nicky "We're on an Island doing some kind of treasure hunting or something..."
        nicky "And the prize is that you might fall in love."
    elif s3_mc.bff == "Seb":
        seb "It's well dark already, isn't it?"
        s3_mc "Yeah, it is actually."
        seb @ talk "I can't believe we're in here looking for love."
        seb "Such a weird, like, concept, isn't it?"
        seb "We're on an Island doing some kind of treasure hunting or something..."
        seb "And the prize is that you might fall in love."

    if s3_mc.bff == "Genevieve":
        # CHOICE
        menu:
            thought "[s3_mc.bff] thinks we're on a treasure hunt for love!"
            "Yeah, and I've lost my treasure already":
                if s3_mc.current_partner == 'Harry':
                    pass
                else:
                    genevieve "Girl, you've got nothing to worry about."
                    genevieve @ happy "[s3_3rd_girl] has got nothing on you."
                    genevieve "I'm sure you're still in with a chance to win him back!"
            "Don't forget about the prize money":
                genevieve @ very_happy "Ha!"
                "She playfully nudges you in the shoulder."
                s3_mc "What? Everyone knows that's the real treasure around here."
                "[s3_mc.bff] smiles and shrugs."
                genevieve "You're not wrong."
                genevieve @ flirt "I wouldn't mind a piece of that cash either."
            "But sex marks the spot":
                "[s3_mc.bff] snorts with laughter. "
                genevieve @ very_happy "Sex marks the spot?"
                s3_mc "You bet it does on my treasure spot."
                "You stick your tongue into your cheek."
                genevieve "OK wow!"
                genevieve @ flirt "[s3_name] you're filthy and I love it."

        if s3_mc.current_partner == "Harry":
            genevieve serious "I want to apologise to you for picking Harry."
            genevieve @ awkward "But then also, I don't want to apologise, because that's how Island Amore works."
            genevieve @ sad "But then, I do want to apologise cos I, like, hurt your feelings!"
            genevieve "It's a messy one."
            # CHOICE
            menu:
                thought "Genevieve doesn't know if she should apologise for coupling up with Harry..."
                "There's nothing to forgive":
                    s3_mc "You did what you had to do, and I respect that."
                    s3_mc "Besides, I'd known him, what, 12 hours?"
                    s3_mc "Not exactly a huge loss, hun."
                    genevieve @ happy -serious "Ha. I'm glad you see it that way."
                "I'd appreciate a sorry":
                    "EMPTY"
                    # NEED TO FILL
                "That's just how it goes in here":
                    "EMPTY"
                    # NEED TO FILL
            genevieve @ happy "I'm just glad we can still be friends."
            s3_mc "Me too."
            "She gives you a big, friendly smile."
            genevieve "Wow, that brought the mood down, huh?"
            genevieve serious "I guess I just worry more when it's dark."

        "Genevieve bites her thumbnail absentmindedly."
        genevieve serious "I'm like, such a night warrior and a worrier."
        s3_mc "A worrying night warrior."
        genevieve @ happy -serious "Yeah, that should be my superhero name at work or something."
        s3_mc "What is it that you do again?"
        genevieve "Junior doctor."
        genevieve @ sad "I always get hyper sensitive when it gets dark."
        genevieve "Which means three things..."
        "She counts them off on her fingers as she goes along."
        genevieve "One, I'm good at working night shifts because I am rarely able to sleep."
        genevieve "Two, when I'm not working, I'm freaking out because work is, like, such a good distraction."
        genevieve "I'm mostly working on site for festivals at the moment."

        # CHOICE
        menu:
            s3_mc "Working as a doctor at a festival sounds..."
            "Really hard work":
                genevieve "Yeah, it can be."
                if s3_mc.job == "Model":
                    genevieve "Being a model must have its moments, though."
                elif s3_mc.job == "Scientist":
                    genevieve "Being a scientist must have its moments, though."
                elif s3_mc.job == "Musician":
                    genevieve "Being a musician must have its moments, though."
                elif s3_mc.job == "Athlete":
                    genevieve "Being an athlete must have its moments, though."
                genevieve "Every job has its bad habits."
            "Like my absolute dream job":
                genevieve "Is it!?"
                genevieve @ happy "Awh, that's so cool."
                genevieve "It's a pretty full on job, but someone's gotta do it, right?"
            "Rubbish! I thought you didn't like the dark?":
                genevieve @ very_happy "You'd think, wouldn't you?"
                genevieve @ happy "But actually it's perfect."

        genevieve "I love that I'm surrounded by people."
        genevieve @ happy "It's literally constant when you're working as a doctor at a festival."
        genevieve "Can't stand how quiet and dark hospitals can get."
        genevieve @ awkward "I bet this place will be a bit spooky, like, late at night."
        genevieve "It'd be easier if there were more people."
        s3_mc "What was the third thing?"
        "Genevieve looks puzzled."
        genevieve @ awkward "You know what?"
        genevieve @ happy "For the life of me I can't remember."
        genevieve "It's because it's getting late."
        genevieve "I'm just getting restless."

        # CHOICE
        menu:
            thought "Genevieve struggles settling down at night."
            "Don't worry, I'll look out for you!":
                genevieve @ happy "Awh, really?"
                genevieve @ happy "Means a lot, I'm not going to lie."
            "I'll be out like a log soon":
                genevieve @ talk "At least that makes one of us!"
            "I can never get to sleep either":
                "You and Genevieve high five."
                genevieve "My belief is that my body clock was set for a different timezone."
                genevieve @ talk "Maybe here it'll be okay!"

    elif s3_mc.bff == "Elladine":
        # CHOICE
        menu:
            s3_mc "The Villa's..."
            "Completely mind blowing":
                elladine "Right? Like you see it on telly and are just like, yeah, it's a big house."
                elladine "But actually being here is like..."
                elladine @ talk "It's a huge house! It has walk-in showers!"
            "Smaller than I expected":
                # NEED TO FILL
                "EMPTY"
            "Got nothing on this place I stayed at in Magaluf":
                # NEED TO FILL
                "EMPTY"

        elladine "And there's something even better here..."
        elladine @ happy "A group of fit boys all wanting to get with us!"
        
        # CHOICE 
        menu:
            s3_mc "The boys are..."
            "Definitely the highlight":
                $ s3_mc.like("Elladine")
                s3_mc "They are just all so fit!"
                elladine @ flirt "Nicky seems like my cup of tea, but that doesn't mean I'm not checking out the others."
                elladine @ awkward "I wonder how Camilo's muscles bulge when he does push ups?"
            "Too basic for me":
                # NEED TO FILL
                "EMPTY"
            "Not the only thing I'm here for":
                # NEED TO FILL
                "EMPTY"

        "She looks off into the distance for a while."
        "Elladine takes a deep breath of the cool night air."
        elladine "It's so fresh out here."
        elladine "This place really does seem perfect. Flawless, even."
        elladine "I hope it stays that way..."

    elif s3_mc.bff == "Nicky":
        # CHOICE
        menu:
            thought "Nicky says I remind him of his sisters..."
            "Because she's so beautiful?":
                nicky @ talk "Ha! No."
                nicky @ awkward "Wait, not that I'm saying my sister isn't' beautiful. She's probably watching this."
                nicky "But I wasn't talking about looks."
            "Because she's so sassy?":
                nicky @ talk "Ha! That's part of it, yeah."
                nicky @ happy "Though I reckon you could out-sass her, if it came down to it."
            "Because she's a reality TV star?":
                "He snorts."
                nicky "She wishes."

        nicky "I was mainly thinking the way drama just seems to find you."
        nicky "Not necessarily your fault."
        nicky "I know how it can be. My sister never goes looking for drama, it just.. follows her around."
        nicky "When things go right for her, they go big right."
        nicky @ flirt "When they go wrong, they go big wrong."
        nicky "And like, I know I've known you for less than a day, but that's already the vibe I'm getting around you."
        
        # CHOICE
        menu:
            thought "Nicky thinks I attract drama..."
            "No, babes, I create it":
                s3_mc "Drama does not 'follow me around', Nicky. How dare you?"
                s3_mc "I am the drama."
                show nicky very_happy
                "He laughs. You give him your best serious face, which makes him laugh more."
            "I can't help it, it just happens":
                s3_mc "I've literally never tried to be that girl, but people just..."
                s3_mc "Well, people seem to lose their common sense a bit when I'm around."
                nicky "Yup. That's what I thought."
            "I've never had drama in my life":
                # NEED TO FILL
                "EMPTY"

        nicky -very_happy "Don't get me wrong, I think it's a good thing."
        nicky "Interesting things happen to interesting people."
        nicky @ happy "You're rich in personality. It's a blessing and a curse."
        s3_mc "It sounds like you're talking from experience. Are you a drama-attractor too?"
        nicky "Nah, mate. It's fun to watch other people's, but in my own life, I keep it chill."
        nicky "If there's any chance of me getting dragged into it, well..."
        nicky @ awkward "I make myself scarce."
        nicky "House parties, family holidays, relationships... if things get hairy, I'll just grab my coat and bail."
        
        # CHOICE
        menu:
            thought "Nicky would rather run away than get dragged into drama..."
            "That's usually a good idea":
                s3_mc "If someone's making your life more complicated than it needs to be, there's no shame in just walking away."
                nicky "Yeah.."
            "You should stick things out":
                s3_mc "If someone's feelings are hurt, either yours or someone else's, you need to see it through."
                s3_mc "If you just keep running away every time, where's that going to leave you?"
                nicky @ flirt "Yeah..."
            "Don't hang out with me, then":
                # NEED TO FILL
                "EMPTY"

        nicky sad "It can make it hard to get properly close to people, sometimes. Y'know, romantically."
        nicky "I guess that's part of the reason I'm here in the first place."
    elif s3_mc.bff == "Seb":
        "Seb looks out thoughtfully at the view."
        seb "Your family's probably sat at home watching all this unfold, right?"
        # CHOICE
        menu:
            thought "Are my family watching at home?"
            "Yeah, of course!":
                s3_mc "Being in here is a huge event of my life!"
                s3_mc "They wouldn't want to miss it any more than they'd want to miss my wedding or my graduation."
                seb "That makes sense."
            "Oof, hope not":
                s3_mc "I really, really don't need anyone in my family to see this."
                seb "Oh, I hear you."
            "I don't mind either way":
                s3_mc "My family's known me my whole life. There's probably nothing I could do here that would shock them."
                s3_mc "If they wanna follow my exploits on TV, I don't care."
                seb @ happy "Hey, respect."

        s3_mc "Why'd you ask? Are you worried about embarrassing yourself in front of your own family?"
        seb "Not exactly."
        seb sad "To be honest, I'm not sure my parents even know I'm here."
        s3_mc "You didn't tell them?"
        seb @ serious "I mean, I mentioned it to them on the phone, but I don't think they were paying attention."
        seb "Or even if they were, they probably didn't really get what I was talking about. They don't watch much TV."
        seb @ awkward "We're not close. Never have been. Honestly, we all prefer it that way."

        # CHOICE
        menu:
            thought "Seb's not close to his parents..."
            "Good for you, man":
                s3_mc "If you don't get on with your parents, there's no obligation to pretend."
                seb @ happy -sad "Thanks for that. Not everybody gets it."
                seb "It's not that we hate each other or anything. We just don't have much in common."
                seb "And I don't have any brothers or sisters to keep in touch with, or anything like that."
            "Why not reach out to them?":
                s3_mc "At the end of the day, they're still your parents. I'm sure they'd really appreciate it."
                seb "Nah, I'm not sure they would."
                seb @ talk "It's not that we hate each other or anything. We just don't have much in common."
                seb "And I don't have any brothers or sisters to keep in touch with, or anything like that."
            "You can have one of mine":
                s3_mc "I've got more than I need. You'd be doing me a favour."
                seb @ happy -sad"That's very generous of you."
                seb "Plus, then we'd be brother and sister. I've always kinda wondered what that would be like."

        s3_mc "You're an only child?"
        seb -sad "Yep. It was a bit lonely growing up, but it made me an independent spirit. I've always done my best work alone."
        seb "That's why I opened my shop in the first place, you know?"
        seb "Running a small business is tough, but it suits me."
        seb "I'm not good at being part of someone else's team."
        seb @ happy "I like to do things my way."
        s3_mc "But you can't run a shop all by yourself, right? You must have employees."
        seb "Well, yeah. There's my second-in-command, Doom."
        s3_mc "Doom?"
        seb @ flirt "So...remember that story earlier, about how I rescued a cat from a burning tree?"
        seb "The rest of the story is that I adopted the cat and named her Doom."
        seb "And now she helps out around the shop."
        seb @ happy "Well, she mostly sleeps on the counter and meows at the customers."
        seb "But she's good at it."

        # CHOICE
        menu:
            thought "Seb's shop assistant is his cat..."
            "That's adorable":
                s3_mc "I would love it if I went into a shop and there was a cat asleep on the counter! I would shop there all the time!"
                seb @ very_happy "Really?"
                s3_mc "Yeah, I think it's awesome!"
                "Seb grins."
                seb @ happy "I guess it is pretty cute."
            "That's ridiculous":
                s3_mc "What if I come into your shop, trying to buy a rare and expensive record, but you're having a nap in the back room?"
                s3_mc "And I try to ask Doom about it, but she just meows at me?"
                s3_mc "You've just lost out on a sale, sir."
                seb @ flirt "That's a risk I'm willing to take."
            "I hope you pay her a living wage":
                s3_mc "Because otherwise that's just exploitative."
                seb @ talk "Of course! What do you take me for?"
                seb @ flirt "I pay her in cat food and scratches."
                seb "And sometimes catnip, if she's good."

        s3_mc "Wait, so who's watching the shop while you're here? You didn't leave Doom on her own, did you?"
        seb @ talk "Oh, no! No, don't worry."
        seb "There's an actual human employee looking after her and the shop."
        seb "I hope she's actually OK. She's actually..."
        "He looks around and lowers his voice excitedly."
        seb @ happy "She's actually expecting kittens soon."
        s3_mc "Oh my gosh, really?"
        seb @ very_happy "Yeah! It's bad timing, 'cause I might not get to be there when they're born..."
        seb "But I'm well excited."

    scene s3-lawn-night with dissolve
    $ on_screen = []

    "The sound of the other Islanders draws your attention away from [s3_mc.bff]."
    bill "Right, I don't know about the rest of you, but I'm cream-crackered."
    miki @ talk "You're a cream cracker?"
    camilo happy "Hah! He is now. That's brilliant."
    bill angry"What? No. I'm knackered."
    miki @ talk "Oh!"
    miki "You mumble too much."
    iona @ awkward "Who even likes cream crackers?"
    camilo "They're gross. Chocolate bourbons all the way, you get me?"
    bill @ talk "Wait, a cream cracker isn't a biscuit."
    camilo @ talk "Isn't it one of those square ones with custard cream in the middle?"
    bill @ angry "That's a custard cream, mate, and they're way better than bourbons."
    "The door to the Villa closes."

    scene s3-roof-night with dissolve
    $ on_screen = []

    # IF STATEMENT
    if s3_mc.bff == "Elladine":
        elladine "Sounds like everyone's going to bed."
        s3_mc "Guess I'll be sleeping alone."
        "[s3_mc.bff] rubs her chin."
        elladine @ talk "You know what?"
        elladine "I think you should find a way to show that you're totally not fazed by this."
        elladine awkward "Some way to show the Villa that you're still here to have a good time, just like everyone else."
        "She thinks about it for a moment."
        elladine @ happy -awkward "What about a prank?"
        s3_mc "Do you have anything in mind?"
        elladine "Well, if we want to do it before bed, it's got to be something simple and classic."
        elladine "What about if you hide somewhere and jump out at someone?"
        elladine "I can keep them distracted while you get ready. What do you say?"
    elif s3_mc.bff == "Genevieve":
        genevieve "Sounds like everyone's going to bed."
        s3_mc "Guess I'll be sleeping alone."
        "[s3_mc.bff] rubs her chin."
        genevieve @ talk "You know what?"
        genevieve "I think you should find a way to show that you're totally not fazed by this."
        genevieve awkward "Some way to show the Villa that you're still here to have a good time, just like everyone else."
        "She thinks about it for a moment."
        genevieve @ happy -awkward "What about a prank?"
        s3_mc "Do you have anything in mind?"
        genevieve "Well, if we want to do it before bed, it's got to be something simple and classic."
        genevieve "What about if you hide somewhere and jump out at someone?"
        genevieve "I can keep them distracted while you get ready. What do you say?"
    elif s3_mc.bff == "Nicky":
        nicky "Sounds like everyone's going to bed."
        s3_mc "Guess I'll be sleeping alone."
        "[s3_mc.bff] rubs his chin."
        nicky "You know what?"
        nicky "I think you should find a way to show that you're totally not fazed by this."
        nicky awkward "Some way to show the Villa that you're still here to have a good time, just like everyone else."
        "He thinks about it for a moment."
        nicky @ happy -awkward "What about a prank?"
        s3_mc "Do you have anything in mind?"
        nicky "Well, if we want to do it before bed, it's got to be something simple and classic."
        nicky "What about if you hide somewhere and jump out at someone?"
        nicky "I can keep them distracted while you get ready. What do you say?"
    elif s3_mc.bff == "Seb":
        seb "Sounds like everyone's going to bed."
        s3_mc "Guess I'll be sleeping alone."
        "[s3_mc.bff] rubs his chin."
        seb "You know what?"
        seb "I think you should find a way to show that you're totally not fazed by this."
        seb awkward "Some way to show the Villa that you're still here to have a good time, just like everyone else."
        "He thinks about it for a moment."
        seb @ happy -awkward "What about a prank?"
        s3_mc "Do you have anything in mind?"
        seb "Well, if we want to do it before bed, it's got to be something simple and classic."
        seb "What about if you hide somewhere and jump out at someone?"
        seb "I can keep them distracted while you get ready. What do you say?"

    thought "Do I want to make one of the other Islanders jump? It could be a cute start to my single gal mischief..."

    # CHOICE
    menu:
        thought "It might be a good chance to get some alone time with someone, too..."
        "That sounds hilarious! Let's do it":
            $ s3e1p3_prank = True
            if s3_mc.bff == "Elladine":
                elladine @ very_happy "Yes! This'll be so fun."
            elif s3_mc.bff == "Genevieve":
                genevieve @ very_happy "Yes! This'll be so fun."
            elif s3_mc.bff == "Nicky":
                nicky @ very_happy "Yes! This'll be so fun."
            elif s3_mc.bff == "Seb":
                seb @ very_happy "Yes! This'll be so fun."
        "As fun as that sounds, I don't think so":
            $ s3e1p3_prank = False
            genevieve "That's fair. It's been a big day already. Another time, maybe."

    "You both stand up."
    # IF STATEMENT
    if s3_mc.bff == "Elladine":
        elladine "Hey, before we head back in, I just want to say that I'm really glad we had this chat."
        elladine "If you ever need to talk again, just come and see me, yeah?"
        elladine "Come on, then. Let's go."
    elif s3_mc.bff == "Genevieve":
        genevieve "Hey, before we head back in, I just want to say that I'm really glad we had this chat."
        genevieve "If you ever need to talk again, just come and see me, yeah?"
        genevieve "Come on, then. Let's go."
    elif s3_mc.bff == "Nicky":
        nicky "Hey, before we head back in, I just want to say that I'm really glad we had this chat."
        nicky "If you ever need to talk again, just come and see me, yeah?"
        nicky "Come on, then. Let's go."
    elif s3_mc.bff == "Seb":
        seb "Hey, before we head back in, I just want to say that I'm really glad we had this chat."
        seb "If you ever need to talk again, just come and see me, yeah?"
        seb "Come on, then. Let's go."
    "The two of you head inside."

    if s3e1p3_prank:
        scene s3-bedroom-night with dissolve
        $ on_screen = []
        "You and [s3_mc.bff] head into the bedroom. You can hear the others approaching."
        if s3_mc.bff == "Elladine":
            elladine @ happy "Alright, go time! You hide. I'll go and keep them busy."
        elif s3_mc.bff == "Genevieve":
            genevieve @ happy "Alright, go time! You hide. I'll go and keep them busy."
        elif s3_mc.bff == "Nicky":
            nicky @ happy "Alright, go time! You hide. I'll go and keep them busy."
        elif s3_mc.bff == "Seb":
            seb @ happy "Alright, go time! You hide. I'll go and keep them busy."
        "[s3_mc.bff] dashes out of the other door. You hear her talking to the others."
    
    return

label s3e1p3_prank:
    # CHOICE
    menu:
        thought "Who do I want to scare?"
        "Harry":
            $ s3e1p3_prankee = "Harry"
        "Camilo":
            $ s3e1p3_prankee = "Camilo"
        "Bill":
            $ s3e1p3_prankee = "Bill"
        "AJ":
            $ s3e1p3_prankee = "AJ"

    $ pronouns(s3e3p3_prankee)

    if s3e1p3_prankee == "AJ":
        "AJ's bed is too far away for you to dive under in time. Instead, you quickly slip into a cupboard."
    else:
        "You dive under [s3e1p3_prankee]'s bed and wait for him to get within grabbing range."

    "Bill, Camilo, and Harry enter the room."
    bill angry "...so yeah, sorry if I don't want dust powder with fake 'cream' in the middle, but no thanks."
    harry @ talk "But they're the best!"
    bill "I've literally just explained to you why that isn't the case."
    camilo awkward "I still can't believe you dunk pink wafers in your tea, bruv."
    bill @ talk -angry "They're a biscuit! Biscuits are meant to be dunked. That's like saying you shouldn't drink  beer with a curry."
    bill @ talk "It's just common sense, yeah?"
    camilo "But don't they just get soggy?"
    bill @ flirt "Well yeah, that's why you have a dunking hierarchy, ranked from hardest to weakest."
    harry "I don't think I've ever thought about biscuits so much in my life."
    aj @ sad "And I don't think I ever want to again."
    elladine "It's been very..."
    elladine @ serious "...enlightening."
    nicky @ awkward "That's a word. Not sure the one I'd for this conversation, but definitely a word."
    "From your hiding spot, you see [s3e1p3_prankee] making [his_her] way over to you."
    
    if s3e1p3_prankee == "AJ":
        aj "Anyone seen [s3_name]?"
    elif s3e1p3_prankee == "Bill":
        bill "Anyone seen [s3_name]?"
    elif s3e1p3_prankee == "Camilo":
        camilo "Anyone seen [s3_name]?"
    elif s3e1p3_prankee == "Harry":
        harry "Anyone seen [s3_name]?"
    
    if s3_mc.bff == "Elladine":
        elladine @ flirt "No?"
    elif s3_mc.bff == "Genevieve":
        genevieve @ awkward "No?"
    elif s3_mc.bff == "Nicky":
        nicky @ talk "No?"
    elif s3_mc.bff == "Seb":
        seb @ awkward "No?"

    if s3e1p3_prankee == "AJ":
        aj "Weird. Maybe she's gone to sleep on the daybeds?"
    elif s3e1p3_prankee == "Bill":
        bill "Weird. Maybe she's gone to sleep on the daybeds?"
    elif s3e1p3_prankee == "Camilo":
        camilo "Weird. Maybe she's gone to sleep on the daybeds?"
    elif s3e1p3_prankee == "Harry":
        harry "Weird. Maybe she's gone to sleep on the daybeds?"

    "[s3_mc.bff] lowers [his_her] voice into a harsh whisper."
    if s3_mc.bff == "Elladine":
        elladine "Or maybe a ghost got her..."
        "She wiggles her fingers dramatically."
        iona @ talk "Woah! Hey, guys, look at the moon."
        miki "It looks massive."
        elladine "Come out onto the terrace with me. Let's get a proper look."
        show elladine at npc_exit
        pause(0.3)
        $ renpy.hide("elladine")
    elif s3_mc.bff == "Genevieve":
        genevieve "Or maybe a ghost got her..."
        "She wiggles her fingers dramatically."
        iona @ talk "Woah! Hey, guys, look at the moon."
        miki "It looks massive."
        genevieve "Come out onto the terrace with me. Let's get a proper look."
        show genevieve at npc_exit
        pause(0.3)
        $ renpy.hide("genevieve")
    elif s3_mc.bff == "Nicky":
        nicky "Or maybe a ghost got her..."
        "He wiggles his fingers dramatically."
        iona @ talk "Woah! Hey, guys, look at the moon."
        miki "It looks massive."
        nicky "Come out onto the terrace with me. Let's get a proper look."
        show nicky at npc_exit
        pause(0.3)
        $ renpy.hide("nicky")
    elif s3_mc.bff == "Seb":
        seb "Or maybe a ghost got her..."
        "He wiggles his fingers dramatically."
        iona @ talk "Woah! Hey, guys, look at the moon."
        miki "It looks massive."
        seb "Come out onto the terrace with me. Let's get a proper look."
        show seb at npc_exit
        pause(0.3)
        $ renpy.hide("seb")
    "You hear the others leave."

    # IF STATEMENT
    if s3e1p3_prankee == "AJ":
        aj @ talk "I'll be out there in a second!"
    elif s3e1p3_prankee == "Bill":
        bill @ talk "I'll be out there in a second!"
    elif s3e1p3_prankee == "Camilo":
        camilo @ talk "I'll be out there in a second!"
    elif s3e1p3_prankee == "Harry":
        harry @ talk "I'll be out there in a second!"
    
    "[s3e1p3_prankee] stops in front of you..."

    # CHOICE
    menu:
        thought "This is it! How should I scare [him_her]?"
        "Call out [his_her] name":
            "You start with a whisper..."
            if s3e1p3_prankee == "AJ":
                s3_mc "[s3e1p3_prankee]..."
                aj @ talk "Huh?"
                s3_mc "[s3e1p3_prankee]."
                aj serious "...Hello?"
                s3_mc "[s3e1p3_prankee]!"
                "The force from your sudden shout makes [s3e1p3_prankee] jump."
                aj @ talk "What the hell?"
                "You slide the cupboard door open and step out, cackling wildly."
                aj -serious "Nice one."
            elif s3e1p3_prankee == "Bill":
                s3_mc "[s3e1p3_prankee]..."
                bill @ talk "Huh?"
                s3_mc "[s3e1p3_prankee]."
                bill serious "...Hello?"
                s3_mc "[s3e1p3_prankee]!"
                "The force from your sudden shout makes [s3e1p3_prankee] jump."
                bill @ talk "What the hell?"
                "You crawl out from under the bed, cackling wildly."
                bill -serious "Nice one."
            elif s3e1p3_prankee == "Camilo":
                s3_mc "[s3e1p3_prankee]..."
                camilo @ talk "Huh?"
                s3_mc "[s3e1p3_prankee]."
                camilo serious "...Hello?"
                s3_mc "[s3e1p3_prankee]!"
                "The force from your sudden shout makes [s3e1p3_prankee] jump."
                camilo @ talk "What the hell?"
                "You crawl out from under the bed, cackling wildly."
                camilo -serious "Nice one."
            elif s3e1p3_prankee == "Harry":
                s3_mc "[s3e1p3_prankee]..."
                harry @ talk "Huh?"
                s3_mc "[s3e1p3_prankee]."
                harry serious "...Hello?"
                s3_mc "[s3e1p3_prankee]!"
                "The force from your sudden shout makes [s3e1p3_prankee] jump."
                harry @ talk "What the hell?"
                "You crawl out from under the bed, cackling wildly."
                harry -serious "Nice one."

        "Jump out at [him_her]":
            if s3e1p3_prankee == "AJ":
                "You go to quickly jump out of the closet, but the sliding door gets jammed, making you fall out instead."
            else:
                "You quickly try to wiggle your way out from under the bed, your arms thrashing towards [s3e1p3_prankee]."
            if s3e1p3_prankee == "AJ":
                s3_mc "Argh!"
                "[he_she!c] looks down at you in bemusement."
                aj "Um, what?"
                s3_mc "...Boo?"
                aj @ happy "Nice one."
            elif s3e1p3_prankee == "Bill":
                s3_mc "Argh!"
                "[he_she!c] looks down at you in bemusement."
                bill "Um, what?"
                s3_mc "...Boo?"
                bill @ happy "Nice one."
            elif s3e1p3_prankee == "Camilo":
                s3_mc "Argh!"
                "[he_she!c] looks down at you in bemusement."
                camilo "Um, what?"
                s3_mc "...Boo?"
                camilo @ happy "Nice one."
            elif s3e1p3_prankee == "Harry":
                s3_mc "Argh!"
                "[he_she!c] looks down at you in bemusement."
                harry "Um, what?"
                s3_mc "...Boo?"
                harry @ happy "Nice one."


        "Grab his ankle" if s3e1p3_prankee in ['Bill', 'Camilo', 'Harry']:
            "[s3e1p3_prankee]'s feet get within reach..."
            if s3e1p3_prankee == "Bill":
                bill "I feel like I could sleep for days."
                s3_mc "Boo!"
                bill @ talk "Woah!"
                "[s3e1p3_prankee] jump back and then laughs."
                bill "You got me good...."
                bill "Nice one."
            elif s3e1p3_prankee == "Camilo":
                camilo "I feel like I could sleep for days."
                s3_mc "Boo!"
                camilo @ talk "Woah!"
                "[s3e1p3_prankee] jump back and then laughs."
                camilo "You got me good...."
                camilo "Nice one."
            elif s3e1p3_prankee == "Harry":
                harry "I feel like I could sleep for days."
                s3_mc "Boo!"
                harry @ talk "Woah!"
                "[s3e1p3_prankee] jump back and then laughs."
                harry "You got me good...."
                harry "Nice one."

        "Wait for her to open the cupboard" if s3e1p3_prankee == 'AJ':
            "You sink further into the clothes as AJ gets closer and closer."
            aj "I can't wait to throw on some cosy PJs!"
            aj "It was so cold coming out of the pool..."
            aj @ awkward "...Why am I talking to myself?"
            "She slides the door open and you make your move."
            s3_mc "Boo!"
            aj @ talk "Woah!"
            "AJ jump back and then laughs."
            aj "You got me good...."
            aj @ happy "Nice one."

    # IF STATEMENT
    if s3e1p3_prankee == "AJ":
        aj @ happy "That was a good effort, but it's going to take more than that to rattle me."
        # CHOICE
        menu:
            thought "She didn't seem that scared..."
            "Come on, you jumped a little":
                aj "Just a trick of the light, hun."
            "Am I not scary enough for you?":
                $ s3_mc.like("AJ")
                aj @ flirt "You're far too cute to be scary..."
            "It was fun hiding anyway.":
                $ s3_mc.like("AJ")
                aj @ flirt "Oh yeah? Perhaps you should show me sometime..."
        aj "You realise I have to get you back for this, right?"
    elif s3e1p3_prankee == "Bill":
        bill @ happy "Maybe I'll get you back by hiding in your bed?"
        # CHOICE
        menu:
            thought "Bill hiding in my bed..."
            "Sounds more like a dream come true":
                $ s3_mc.like("Bill")
                bill @ flirt "That's what I was hoping you'd say..."
            "You in my bed would be terrifying":
                $ s3_mc.dislike("Bill")
                bill @ happy "Damn right!"
                bill awkward "Um... wait."
                "He frowns."
            "Is that an invitation?":
                bill @ flirt "It can be if you want..."
        bill -awkward "You realise I have to get you back for this, right?"
    elif s3e1p3_prankee == "Camilo":
        camilo @ happy "You're lucky my reflexes didn't kick in!"
        camilo "A mate once pulled the same thing on me, and before I knew it, I was throwing him over my head..."
        camilo "Luckily we were in someone's room so he landed on the bed, and he just kinda bounced a bit."
        # CHOICE
        menu:
            thought "Camilo once threw a friend onto a bed."
            "Oh my, you're so strong":
                camilo "It's not about strength or stamina."
                camilo @ flirt "It's all in the technique..."
                s3_mc "Maybe you can show me some day."
            "Sounds like an overreaction":
                $ s3_mc.dislike("Camilo")
                camilo "Maybe. Or maybe he deserved it."
            "I hope you throw me onto a bed one day":
                $ s3_mc.like("Camilo")
                camilo @ flirt "Maybe someday soon I will."
        camilo "You realise I have to get you back for this, right?"
    elif s3e1p3_prankee == "Harry":
        harry @ awkward "I'd rather it was you under the bed than some kind of monster."
        harry flirt "Maybe next time you should warn me, and I can just join you down there?"
        # CHOICE
        menu:
            thought "Should I warn him next time?"
            "I wouldn't hide under the bed again":
                harry "Or wherever you're hiding, then."
                harry happy "Just as long as it's cosy, you get me?"
            "There won't be a next time":
                $ s3_mc.dislike("Harry")
                harry @ awkward "Shame."
                harry -flirt "Could've been a great bonding opportunity."
            "Wouldn't it be better to be in bed?":
                $ s3_mc.like("Harry")
                harry "Hmm, true."
                harry happy "A lot more space to move around in..."         
        harry -happy "You realise I have to get you back for this, right?"

    s3_mc "I'd like to see you try..."
    "Before [he_she] can say anything else, the rest of the Islanders reappear, laughing."
    iona "[s3_mc.bff] told us what you were up to, [s3_name]."
    nicky "It sounds like it worked."
    miki @ sad "Just never spook me, yeah? I hate jump scares..."
    "They start to get ready for bed."
    thought "That's enough excitement for one night. I'm going to go and get changed."

    return



#########################################################################
## Episode 2, Part 1
#########################################################################
label s3e2p1:
    scene sand with dissolve
    $ on_screen = []

    show screen day_title(2, 1) with Pause(4)
    hide screen day_title with dissolve

    "Previously on Island Amore..."
    "[s3_3rd_girl] made an entrance and stole [s3_name]'s man."

    # IF STATEMENT
    if s3_mc.current_partner == "Bill":
        miki serious "The boy I'd like to couple up with is..."
        miki happy "[s3_mc.current_partner]."
        show miki at npc_exit
    elif s3_mc.current_partner == "Camilo":
        iona serious "The boy I'd like to couple up with is..."
        iona happy "[s3_mc.current_partner]."
        show iona at npc_exit
    elif s3_mc.current_partner == "Harry":
        genevieve serious "The boy I'd like to couple up with is..."
        genevieve happy "[s3_mc.current_partner]."
        show genevieve at npc_exit
    
    scene sand
    $ on_screen = []

    "And so [s3_name] was sent to bed alone."

    # IF STATEMENT
    if s3e1p3_prank:
        "But not before giving [s3e1p3_prankee] a proper good fright."
        if s3e1p3_prankee == "AJ":
            aj "You realise I have to get you back for this, [s3_name], right?"
            show aj at npc_exit
        elif s3e1p3_prankee == "Bill":
            bill "You realise I have to get you back for this, [s3_name], right?"
            show bill at npc_exit
        elif s3e1p3_prankee == "Camilo":
            camilo "You realise I have to get you back for this, [s3_name], right?"
            show camilo at npc_exit
        elif s3e1p3_prankee == "Harry":
            harry "You realise I have to get you back for this, [s3_name], right?"
            show harry at npc_exit
        scene sand 
        $ on_screen = []
    else:
        s3_mc "I guess I'll be sleeping alone."
    "But worry not, [s3_name]!"
    "Because on today's Island Amore..."
    "It's graft o'clock!"

    scene s3-bedroom-day with dissolve
    $ on_screen = []

    "Something soft hits your head and wakes you up with a jolt."
    thought "Huh?"
    "You sit up and wipe your eyes, still bleary from the night's sleep."
    "[s3_mc.bff] laughs."
    harry @ happy "Morning, sunshine."
    s3_mc "Who did that?"
    "Everyone points at [s3_mc.bff]."

    # CHOICE
    menu:
        thought "[s3_mc.bff] just threw a pillow at me!"
        "Dive back under the covers":
            "You grab the sheets and pull them over your head."
            if s3_mc.bff == "Elladine":
                elladine "Someone's not a morning person..."
            elif s3_mc.bff == "Genevieve":
                genevieve "Someone's not a morning person..."
            elif s3_mc.bff == "Nicky":
                nicky "Someone's not a morning person..."
            elif s3_mc.bff == "Seb":
                seb "Someone's not a morning person..."
            "You peek out from under the covers."
            s3_mc "Nope."

        "Throw it back at [s3_mc.bff]":
            "You chuck the pillow back."
            s3_mc "Take that!"
            "It lands on [s3_mc.bff]'s head with a thud."
            if s3_mc.bff == "Elladine":
                elladine @ happy "Ha! Good aim."
            elif s3_mc.bff == "Genevieve":
                genevieve @ happy "Ha! Good aim."
            elif s3_mc.bff == "Nicky":
                nicky @ happy "Ha! Good aim."
            elif s3_mc.bff == "Seb":
                seb @ happy "Ha! Good aim."

        "Spoon the pillow":
            "You cuddle up to the pillow."
            thought "This is the closest I've got to a cuddle so far."
            if s3_mc.bff == "Elladine":
                elladine "Aw, [s3_name]!"
            elif s3_mc.bff == "Genevieve":
                genevieve "Aw, [s3_name]!"
            elif s3_mc.bff == "Nicky":
                nicky "Aw, [s3_name]!"
            elif s3_mc.bff == "Seb":
                seb "Aw, [s3_name]!"

    seb "At least you're awake now!"
    "Elladine gets up from her bed."
    elladine "Finally!"
    seb "Yeah, I'm starving."
    harry "Me too!"
    s3_mc "Were you all waiting for me?"
    s3_mc "Or were you watching me while I slept?"
    harry "A bit of both."
    elladine "We all woke up but didn't want to, like, leave you on your own up here."

    if s3_like_aj:
        aj @ flirt "I said we should all get in bed with you and spoon you."
    elif s3_mc.current_partner == "Bill":
        bill @ flirt "I said we should all get in bed with you and spoon you."
    elif s3_mc.current_partner == "Camilo":
        camilo @ flirt "I said we should all get in bed with you and spoon you."
    elif s3_mc.current_partner == "Harry":
        harry @ flirt "I said we should all get in bed with you and spoon you."

    s3_mc "Really?"
    miki "Yeah, we didn't want you to have to wake up on your own."
    genevieve @ sad "That would be awful..."
    genevieve @ happy "But you don't have to because you've got us!"

    # CHOICE
    menu:
        thought "The Islanders waited for me to wake up!"
        "That's so cute, thank you!":
            if s3_mc.bff == "Elladine":
                elladine @ happy "Any time, [s3_name]!"
            elif s3_mc.bff == "Genevieve":
                genevieve @ happy "Any time, [s3_name]!"
            elif s3_mc.bff == "Nicky":
                nicky @ happy "Any time, [s3_name]!"
            elif s3_mc.bff == "Seb":
                seb @ happy "Any time, [s3_name]!"

        "What are we waiting for? Let's get up":
            harry "Yeah, we should."

        "I'd rather be spooning with [s3_mc.current_partner]" if s3_like_aj == False:
            $ s3e2p1_want_spoon = True
            $ s3_mc.like(s3_mc.current_partner)
            "[s3_mc.current_partner] catches your eye for a moment, and grins."
        
        "I'd rather be spooning with AJ" if s3_like_aj:
            $ s3e2p1_want_spoon = True
            $ s3_mc.like("AJ")
            "AJ catches your eye for a moment, and grins."

    if s3e2p1_want_spoon:
        if s3_mc.bff == "Elladine":
            elladine "Either way, I think spooning time is over. We should get up and get some brekkie."
        elif s3_mc.bff == "Genevieve":
            genevieve "Either way, I think spooning time is over. We should get up and get some brekkie."
        elif s3_mc.bff == "Nicky":
            nicky "Either way, I think spooning time is over. We should get up and get some brekkie."
        elif s3_mc.bff == "Seb":
            seb "Either way, I think spooning time is over. We should get up and get some brekkie."

    "Everyone clambers out of bed and starts getting ready for the day."
    thought "It's a new day in the Villa and I'm the only single person..."

    $ outfit = "swim"

    # Add back dialogue when and if MC images are added to game
    # thought "I'd better dress to impress."
    # thought "What should I wear?"

    # MC outfit change to swimwear
    # Change all NPC outfit to swimwear

    # thought "I don't think this has lost its charm just yet."
    # thought "Now I'm ready for the day!"
    # thought "Wow. I'm looking like a snack!"
    # thought "Now I'm ready for the day!"
    # thought "This will do. (free outfit)"

    thought "Who should I talk to?"

    call screen s3e2p1_select_who_to_talk_to

label s3e2p1_end:
    scene s3-lawn-day with dissolve
    $ on_screen = []

    "Everyone is lounging on the grass. Nicky and Seb are playing catch with a wet rolled-up sock."
    "The wet sock lands in your lap."
    thought "Gross..."
    nicky awkward "Oops."
    seb awkward "Sorry!"

    # CHOICE
    menu:
        thought "I should..."
        "Throw the sock back at them":
            "You launch the sock towards Nicky and Seb."
            "With a satisfying wet squelch, it lands on Seb's head."
            seb -awkward "I deserved that."
        "Put the sock on":
            "You slide the wet sock onto your foot."
            nicky flirt "Ew."
            "Seb pulls it off your foot."
        "Chuck it at [s3_mc.current_partner]":
            "You lob it at [s3_mc.current_partner]."
            if s3_mc.current_partner == "Bill":
                bill awkward "Hey!"
            elif s3_mc.current_partner == "Camilo":
                camilo awkward "Hey!"
            elif s3_mc.current_partner == "Harry":
                harry awkward "Hey!"
            "You point at Nicky and Seb."
            s3_mc "They started it!"

    "A phone beeps."
    iona @ talk "Oh, I got a text."
    text "Islanders, get ready for some one-on-one time! This afternoon, each of the boys will be choosing someone to take out on a date. #comedatewithme #datesormates"
    harry @ very_happy "Yes!"
    harry "We've got to date whichever girls we want!"
    harry @ happy "Right on."
    "Everyone rushes inside to get ready."

    scene sand with dissolve
    $ on_screen = []

    "Things are heating up in the Villa..."
    "And not just because Bill's left the hob on."
    "It's only the second day, and already the Islanders have got themselves a date."
    "Coming up on Island Amore..."
    "Tensions rise, when the boys pick the girl they'd like to take out..."
    genevieve serious "The boys have made their decisions."
    miki sad "What?!"
    iona flirt "Did you feel that special spark with someone?"
    
    scene sand
    $ on_screen = []

    # CHOICE
    menu:
        "Do you want to continue to next part or go back to the main menu?"
        "Next Part":
            jump s3e2p2
        "Main Menu":
            call screen main_menu

    return

# Map Chose "Elladine and Genevieve"
label s3e2p1_bean_bags:
    scene s3-bean-bags-day with dissolve
    $ on_screen = []
    $ s3e2p1_visited.append("Bean Bags")

    "Elladine and Genevieve are lounging on the beanbags."
    
    # IF STATEMENT
    if "Kitchen" in s3e2p1_visited:
        "Elladine is eating a bowl of oats and yoghurt."
        elladine @ happy "Nicky is such a sweetheart bringing me breakfast like this."
        genevieve "Yeah, he seems like a good guy."
    else:
        "Elladine is looking towards the kitchen."
        elladine "I should get some food soon, I'm hungry..."

    "Genevieve smiles at you as you sit down."
    genevieve "Hey, hun."
    genevieve "We were just chatting about Harry."

    # IF STATEMENT
    if s3_mc.current_partner == "Harry":
        genevieve sad "I hope you're OK with that after last night."
        elladine serious "Yeah, we don't want you to feel awks, hun."
        # CHOICE
        menu:
            thought "How am I feeling about Genevieve and Harry?"
            "Yeah, it's all good":
                genevieve @ happy "Good."

            "I'm feeling sad about it":
                "Genevieve looks at you sympathetically."
                genevieve "I'm sorry, hun."
                genevieve "If it makes you feel any better, I'm not so sure how long we're going to last."

            "You guys won't last":
                elladine "Woah, bit harsh."
                genevieve "Nah, it's a fair comment."

    genevieve -sad "He's cute, don't get me wrong."
    genevieve "And proper funny."
    genevieve @ sad "I don't know, maybe it's because he's younger, but I'm not sure about him."

    # CHOICE
    menu:
        thought "Genevieve isn't sure about Harry..."
        "I think he's really cool":
            if s3_mc.current_partner == "Harry":
                genevieve "I know, I know."
                genevieve "I'm sorry, I'm sure that's, like, really annoying to hear coming from me."
            else:
                genevieve "Yeah, we'll see."

        "He's not my cup of tea":
            genevieve "I think we're on the same wavelength."
        "Good, he's all mine then":
            elladine @ awkward "Woah, [s3_name]!"
            s3_mc "What? I like what I see and I want what I see."
            if s3_mc.current_partner == "Bill" or s3_mc.current_partner == "Camilo":
                genevieve @ talk "You like him?"
                s3_mc "Yeah. I do."
                genevieve "Oh, I had no idea."
                genevieve "You were with [s3_mc.current_partner] this time yesterday."
            elif s3_mc.current_partner == "Harry":
                genevieve @ awkward "Hey, I mean, yeah, fair enough. You guys were together this time yesterday."

    genevieve "I suppose I shouldn't be worried about it, anyway."
    genevieve @ awkward "It's only been a night. Not really long enough to tell if you like someone, is it?"
    elladine "Isn't it?"
    elladine "I've fallen in love overnight before, for sure."

    # CHOICE
    menu:
        thought "Is one night enough time to tell if you like someone?"
        "Yeah, that's why one night stands exist":
            s3_mc "Sometimes one night is all you need to know if it's going to work... or not."
            show genevieve very_happy
            show elladine very_happy
            "Genevieve and Elladine laugh."
            genevieve @ happy -very_happy "OK, yeah, we've all been there."
            show elladine
        "No, you need more time than that":
            genevieve @ sad "You really think so?"
            s3_mc "Absolutely. You can't get a good sense of someone's personality in just one day."
        "Why do we measure love by time passing?":
            s3_mc "It's not about how much time passes. It's about how you spend that time."
            elladine "Yeah, you could have, like loads of anniversaries with someone and still be unhappy."
            genevieve "Woah, OK, you two got deep quick."

    genevieve "But yeah, it's early days."
    genevieve "We'll see."
    elladine "What do you girls want to get out of this whole thing? Like..."
    elladine "Are you just here to have a good time?"
    elladine "Or are you looking for love?"
    "She makes a little heart out of her hands."

    # CHOICE
    menu:
        thought "Why am I here?"
        "I am looking for true love":
            s3_mc "I mean, why else would I be here?"
            elladine "Yeah, I guess you're right!"
            elladine "It's odd, isn't it? Like, searching for love?"
            elladine "You wouldn't search for any other emotion the way you search for love..."
        "I'm just here to have a laugh":
            s3_mc "I just want to have a good time, you know?"
            elladine "Of course! Who doesn't?"
        "I want to make friends for life":
            "Genevieve puts her arm around you."
            genevieve "Me too, hun. Me too."

    genevieve "Honestly, I'm here for the sunshine and the good times."
    genevieve "I'm worried I've thought too much about what it's going to be like in here."
    genevieve "Like, I hope I haven't set my expectations too high."
    elladine "Hun, imagination and desire are very close."
    elladine "What you dream about reveals what you want in life."
    elladine "And you should always be trying to fulfil it."

    # CHOICE
    menu:
        thought "Should I always be going for what I want?"
        "Yeah, I always put myself first":
            s3_mc "Yeah, for sure, I always get what I want."
            elladine "That's not really what I meant."
            elladine "Sometimes what we want isn't what we actually need."
            elladine "But your desires reveal a lot about you."
        "It's important to consider other people":
            s3_mc "You should always be respectful of others."
            genevieve "Yeah, of course. But that doesn't mean you can't respect yourself as well."
        "You shouldn't worry about the future":
            genevieve "[s3_name]'s right."
            genevieve "Just be present in the now, hun."
            genevieve "No point in worrying about what might happen."
            genevieve "Unless you're talking about climate change."
            elladine "Yeah, that's important."

    elladine "That's some good deep stuff, girls."
    elladine "Words to live by."
    elladine "Who knows what's going to happen in here?"
    genevieve "Exactly."
    "Elladine stands up."

    # Adjust if statement to work with right variables
    # IF STATEMENT
    if "Kitchen" in s3e2p1_visited:
        elladine "I can't believe I'm still hungry."
        elladine "That breakfast was delicious, but yoghurt isn't exactly filling, is it?"
    else:
        elladine "I need some breakfast after all that."
    
    if len(s3e2p1_visited) == 4:
        jump s3e2p1_end
    else:
        call screen s3e2p1_select_who_to_talk_to

    return

# Map Chose "Miki and Iona"
label s3e2p1_sun_loungers:
    scene s3-sun-loungers-day with dissolve
    $ on_screen = []
    $ s3e2p1_visited.append("Sun Loungers")

    "Miki and Iona are sunbathing on the loungers."
    miki "Hey, [s3_name]."
    miki "Come over and join us."
    "You sit down beside them, enjoying the fresh breeze and the morning sun."

    # IF STATEMENT
    if "Pool" in s3e2p1_visited:
        miki "Looks like you had some fun in the pool."
    else:
        miki "Looks like Harry and Camilo are having fun in the pool."

    miki "Is that an infinity pool?"
    iona "What's an infinity pool?"
    miki "That kind of pool over there, basically."
    miki "It looks like it goes on forever."
    iona "I didn't even know there were different kinds of swimming pools."
    miki "Oh, there's loads of types!"
    miki "Infinity pool, above ground pool, lido..."
    iona "Pool table."
    "Miki laughs, and then turns to look at you."
    miki "If you had to turn into a pool..."
    miki "What pool would you be?"
    iona "What?"
    miki "I reckon Bill would be one of those pools with a wave machine. Because he's uplifting, but his opinions often go against the crowd."
    iona "What are you on about, hun?"
    miki "Simple! If you had to be a pool, what pool would you be?"

    # CHOICE
    menu:
        thought "What pool would I be if I had to be a pool?"
        "An infinity pool":
            miki "I feel that. One hundred percent."
            miki "You're such an infinity pool."
            miki "That says you are an open person."
            miki "And that you're always happy to give your time to others."
        "A deep diving pool":
            miki "Oh yeah. If you were a pool you'd be a deep one, for sure."
            miki "You're such a deep and unfathomable person."
            miki "And you're so mysterious."
            miki "A diving pool suits you so well."
        "A freezing cold plunge pool":
            miki "Oof, really? "
            s3_mc "Why, what does that say about me?"
            miki "Oh, no. Nothing bad."
            miki "It must mean that you're cold as ice."
            miki "Like the ice queen."
            miki "But I don't see you as an ice queen..."
            miki "You are pretty cool though."
        "A paddling pool":
            miki "A paddling pool?"
            miki "Those are pretty shallow...."
            miki "But with you I think that means you're always up for a laugh."

    miki "How about you, Iona?"
    miki "What kind of pool would you be if you could be a pool?"
    iona "Is this, like, a trick question?"
    iona "Are you going to ask me for my mother's maiden anime and the name of my first pet?"
    miki "What? No. What's that got to do with pools?"
    miki "[s3_name], you're sensible. What kind of pool would Iona be?"

    # CHOICE
    menu:
        s3_mc "If Iona was a pool, she would be..."
        "Calm and sexy like a pool at a spa":
            $ s3_mc.like("Iona")
            "Iona smiles."
            iona "Thanks, hun."
        "Fun and hot bubbly like a hot tub":
            $ s3_mc.like("Iona")
            iona "No one has ever said that about me before."
            "She grins at you."
            iona "Thanks, hun."
        "An unfiltered algae covered pool":
            $ s3_mc.dislike("Iona")
            "Iona and Miki look at each other awkwardly."
            iona "Um, thanks..."
            miki "That's a bit mean, [s3_name]."
            s3_mc "I just say it like I see it."
            iona "Well, my favourite colour is green, I guess."
            iona "And I suppose I don't filter my opinions, so you're probably spot on there, hun."

    iona "Actually, you know what I love? A pool with some nice LED lights changing the colour of the water. "
    miki "Oh yeah, mood lighting is key."
    miki "Ooh, if you were a light, what kind of light would you girls be?"

    # CHOICE
    menu:
        thought "What kind of light would I be?"
        "A crystal chandelier":
            s3_mc "I'd be a crystal chandelier."
            miki "Why are you a chandelier."
            iona "Because she's grand, gorgeous, and sparkling, obviously!"
        "A small bedside lamp":
            miki "Aw babe. So cute. Why are you a night light?"
            iona "Because she's sweet and kind, obviously."
        "The sun":
            miki "The sun?!"
            s3_mc "Yeah, that is the ultimate light source."
            iona "I like your style, [s3_name]."
            iona "Go hard or go home."
        "Seriously, can we not?":
            iona "OK. You don't have to play."

    iona "I'd be a lava lamp."
    iona "Calm and chill at first glance, but come too close and I'm a hot mess."
    miki "Girl, I feel you."
    "Miki yawns, stretching out her arms."
    miki "This morning is so chill."
    iona "Yeah, it's such a lava lamp mood."
    "You all relax into your loungers, taking in the morning sun."
    thought "I should probably have a wander around the rest of the Villa or I'll fall asleep in the sun."

    if len(s3e2p1_visited) == 4:
        jump s3e2p1_end
    else:
        call screen s3e2p1_select_who_to_talk_to

    return

# Map Chose "Harry, Camilo, and AJ"
label s3e2p1_pool:
    scene s3-poolside-day with dissolve
    $ on_screen = []
    $ s3e2p1_visited.append("Pool")

    "You wander over to the pool where Harry, Camilo and AJ are getting ready to dive into the water."

    # IF STATEMENT
    if "Sun Loungers" in s3e2p1_visited:
        thought "I wonder what kind of pool these lot would be..."

    # IF STATEMENT
    if s3_mc.bisexual:
        aj "Hey, [s3_name]!"
        aj "Watch us!"
    else:
        camilo "Hey, [s3_name]!"
        harry "Watch this!"

    "They all jump in."
    "The combined splash is huge. It leaves you drenched."

    # CHOICE 
    menu:
        thought "I'm soaking!"
        "Cannonball into the pool":
            "You step back and start to run towards the pool."
            s3_mc "Cannonball!"
            harry "No!"
            "You land with a splash."
        "Get in and splash them back":
            "You get into the pool."
            aj "Uh oh..."
            camilo "Here comes trouble."
            harry "It wasn't me!"

            # SUB-CHOICE
            menu:
                thought "Who should I splash?"
                "AJ":
                    "You hold on to the side and start to kick the water frantically."
                    aj "Hey!"
                    "AJ gets soaked by your kicking."
                    aj "You've made me all wet now."
                "Camilo":
                    "You cup your hands and propel them forward."
                    "Camilo gets drenched by your mini tidal wave."
                    camilo "Agh! Not fair!"
                "Harry":
                    "With swift motion of your arms, you splash Harry."
                    harry "Woah!"
                    "He shakes his head, spraying water over you all."
                    harry "You got me good, [s3_name]."

        "Pretend to melt from the water":
            s3_mc "Water?"
            s3_mc "No...I'm melting."
            "You crumble to the floor."
            s3_mc "Melting!"
            "You reach up to the sky in desperation. Harry, AJ and Camilo all laugh at you and start to splash you some more."
            "Rolling across the grass, you slide into the pool."
            camilo "Woah. Solid kicks. You ever done martial arts?"
            harry "I love your theatrical side, [s3_name]."
            aj "Yeah, you're hilarious."

    "Harry is treading water beside you. Camilo starts to splash Harry. AJ is flicking the water across the pool."

    # IF STATEMENT
    if s3_mc.current_partner == "Bill":
        camilo "I can't believe Bill has had two girls pick him already."
        harry "Yeah, two gorgeous girls."
        aj "Alright, alright, you two."
    elif s3_mc.current_partner == "Camilo":
        camilo "I just can't believe my luck."
        camilo "Two beautiful girls have chosen me already."
        "Harry splashes Camilo."
        harry "Don't brag about it, mate."
        camilo "Honestly, it's my Latino charm."
        camilo "I can't help it."
        harry "Did you sleep OK, like, on your own and stuff, [s3_name]?"
        camilo "Yeah."
        camilo "I was annoyed I didn't get to spoon you last night."
    elif s3_mc.current_partner == "Harry":
        harry "So, just to keep you in the loop, Camilo."
        harry "Two gorgeous girls have picked me already."
        "Camilo splashes Harry."
        harry "Hey!"
        camilo "Sorry, just cooling you off."
        harry "Did you sleep OK, like, on your own and stuff, [s3_name]?"
        harry "I'm kinda gutted I didn't get to sleep next to you, not gonna lie."

    # CHOICE
    menu:
        thought "How did I sleep?"
        "The bed was actually super comfy":
            harry "Yeah?"
            camilo "It wasn't too cold?"
            s3_mc "Nope. I slept great."
            harry "Good. I'm glad!"
            harry "Nothing better than a good rest to get you ready for the day."
        "I'd have slept better if [s3_mc.current_partner] was there":
            $ s3_mc.like(s3_mc.current_partner)
            if s3_mc.current_partner == "Bill":
                # NEED TO FILL
                "EMPTY"
            elif s3_mc.current_partner == "Camilo":
                camilo "Oh, wow. That's so cute, [s3_name]."
                camilo "You know, I have been told to make a great hot water bottle."
            elif s3_mc.current_partner == "Harry":
                harry "Really?"
                harry "I've got to say, I love being the little spoon..."
        "I don't mind sleeping alone" if s3_mc.bisexual == False:
            harry "Yeah?"
            camilo "It wasn't too cold?"
            s3_mc "Nope. I slept great."
            harry "Good. I'm glad!"
            harry "Nothing better than a good rest to get you ready for the day."
        "I would have preferred to sleep next to AJ" if s3_mc.bisexual == True and s3_like_aj == True:
            aj "Aw, [s3_name]!"
            aj "I'd love to spoon you."

    harry "I actually slept really well."
    harry "I've probably been up since about five."
    harry "That's when I usually wake up."
    harry "It's the secret to success, you know?"
    aj "What?"
    harry "Getting up at five."

    # CHOICE
    menu:
        thought "Do I think early mornings are the secret to success?"
        "I agree, I usually wake up early":
            $ s3_mc.like("Harry")
            harry "Oh, yeah?"
            harry "That's so good to hear."
            harry "It's really important to start your morning on a good note."
            harry "Especially somewhere new like the Villa."
        "That sounds like a lot of effort":
            harry "It's not!"
            harry "It's free and an easy thing to do once you get in a routine."
        "What is success?":
            harry "That's a good question."
            harry "We often think of success as being, like, the best."
            harry "Getting the most money, having lots of fans, or being the boss."
            harry "But really, it's about doing something that fulfils you."

    camilo "What do you do at five in the morning?"
    camilo "Work out?"
    "Harry leans on the side of the pool and runs one hand through his wet hair."
    harry "Nah, I normally do my affirmations. Then I might have a bit of a wander."
    aj "So you're saying that's the secret to success? That's all I need to do?"
    harry "That's the wrong attitude to have, AJ."
    harry "It's not about what you do."
    harry "It's about what you believe you can do for yourself."

    # CHOICE
    menu:
        s3_mc "Harry sounds like he's..."
        "Talking a load of rubbish":
            aj "Yeah, I've got to agree with [s3_name]."
            harry "Yeah, well, you'll all see one day when I rule the world."
        "Onto something":
            $ s3_mc.like("Harry")
            harry "[s3_name] gets it."
        "Just showing off":
            aj "Yeah, I've got to agree with MC."
            harry "Yeah, well, you'll all see one day when I rule the world."

    "He laughs to himself and gets out of the pool."
    harry "I've got to go and work on my mojo."
    "He walks off towards the Villa leaving wet footprints behind him."
    harry "See you lot around."
    "Camilo shakes his head. Beads of water fly off."
    "He smiles at you."
    camilo "Any of you want a piggyback around the pool?"

    # CHOICE
    menu:
        thought "Do I want Camilo to give me a piggyback around the pool?"
        "Let me ride you, Camilo":
            camilo "I'm not going to say no to that, [s3_name]."
            "AJ and Camilo laugh."
            "You climb onto Camilo's back, wrapping your legs tightly around his hips."
            if s3_mc.current_partner == "Bill" or s3_mc.current_partner == "Harry":
                camilo "Hold on tight."
            elif s3_mc.current_partner == "Camilo":
                camilo "Hope you're ready for the ride of your life, gorgeous."
            "He gallops around the pool with you on his back."
            s3_mc "Giddy up!"
            "You tighten your grip as he speeds up. You can smell the coconut sun cream on the back of his neck."
            camilo "Here comes a jump."
            "He takes you into his arms, and then leaps into the pool. There's a huge splash as you both hit the water."
        "No thanks, he should ask AJ instead":
            aj "Nah, mate. If anyone is giving anyone a piggyback, it's me."
            "With no further warning, she lifts Camilo out of the water. He quickly clings to her back."
            camilo "Woah! OK!"
            "She charges around the pool, splashing you as she passes."
            camilo "Giddy up, AJ!"
            aj "Oh, you're in for it now."
            "She playfully launches him off her back."
            "He lands with a splash in the water next to you."
            aj "I'm not a horse, you horse."
        "I want AJ to give me a piggyback":
            aj "Go on then hun, hop on."
            "You climb on AJ's back, wrapping your legs tightly around her hips."

            # IF STATEMENT
            if s3_like_aj:
                aj "Hope you're ready for the ride of your life, gorgeous."
                "She charges around the pool with you on her back."
                "As you grip tighter you can smell her coconut scented sun cream."
            else:
                aj "Hope you're ready for a bumpy ride."
                "She charges around the pool with you on her back."

            aj "Woah, watch out, tight corner."
            "She leans to the side and you both fall into the water, splashing Camilo."

    camilo "You guys are hilarious."
    aj "Yeah, I love hanging out with people who know how to have a proper laugh."
    "You all splash about in the water for a while."
    camilo "You ever notice how your hands get all wrinkly when you stay in the water too long?"
    aj "Yeah, what's that about?"
    camilo "I don't know. It's a shame we can't stay in here all day."
    thought "Camilo's right. I'd better dry off before I end up like a raisin!"
    "You climb out of the pool."

    if len(s3e2p1_visited) == 4:
        jump s3e2p1_end
    else:
        call screen s3e2p1_select_who_to_talk_to

    return

# Map Chose"Seb and Bill"
label s3e2p1_kitchen:
    scene s3-kitchen-day with dissolve
    $ on_screen = []
    $ s3e2p1_visited.append("Kitchen")

    "You wander into the kitchen. Seb is looking into the fridge. Bill is getting out some pots and pans."

    # IF STATEMENT
    if s3_mc.bff == "Seb":
        seb "Oh, hey, [s3_name]."
        "He gives you an awkward but friendly pat on the back."
        s3_mc "Hi, mate."
    else:
        "Seb nods at you."
        seb "Alright?"
        s3_mc "Hey."

    bill "Morning, sleepy head."
    s3_mc "Morning."

    # Add back in once there are MC images in game
    # bill "There's an old roofer saying 'if it ain't broke, don't fix it.'"
    # bill "As true for tiles as it is for your outfit, [s3_name]. You're looking great."
    # seb "Pretty sure that's not a roofer's saying, Bill."
    # bill "Whatever."
    # bill "Loving the new outfit by the way, MC. It looks amazing on you."
    # bill "Sticking to the basic look today, are we? Well, it's not like you need any help turning heads in here, I guess. (free outfit)"

    if s3_mc.current_partner == "Bill":
        "Bill glances back at the pans, then smiles at you."
        bill "You sleep OK, on your own, like? I hope it wasn't weird."
        bill "It's still hard to believe we're the first couple to get split up."

        # CHOICE
        menu:
            thought "How do I feel about Bill and I getting split up."
            "Yeah, I'm pretty gutted":
                bill "Same..."
                bill "Not going to lie."
            "It is what it is":
                bill "But what does that even mean?"
                bill "What is what it is?"
                bill "I guess we'll never know..."
            "I want to be with you again!":
                bill "You'd better get your graft on then!"

    "Bill starts cracking eggs into a pan."
    seb "You making a fry-up, Bill?"
    bill "You bet. Want some?"
    seb "I could do with one right now, sure."
    bill "Nothing better than a good full English breakfast with baked beans, ten mushrooms, two tomatoes, three sausages, two fried eggs, and three hash browns."
    nicky "Mate, where's the bacon?"
    bill "There isn't any."
    nicky "I've never heard anyone be so specific."
    bill "If you're gonna do it, that's how it's done."
    bill "Want one, [s3_name]?"

    # CHOICE
    menu:
        thought "Bill's offering to cook me breakfast!"
        "I'd love a fry-up, thanks Bill":
            $ s3_mc.diet = "Meat"
            bill "One fry-up coming up!"
        "Ah, I prefer not to eat meat":
            $ s3_mc.diet = "Vegetarian"
            bill "That's OK."
            bill "One vegetarian fry-up coming up."
        "I'm vegan. No meat or eggs for me please!":
            $ s3_mc.diet = "Vegan"
            bill "That's OK."
            bill "One vegan fry-up coming up."

    "Bill starts getting busy preparing the food."
    bill "Seb, can you check the fridge for some mayo?"
    bill "You've got to have one mayo sachet per sausage."
    bill "That's the perfect ratio."
    seb "Mayo in sachets? Mate, this isn't a pub lunch."
    "Seb chucks him a bottle of mayonnaise."
    seb "Here, fill your boots."

    # CHOICE
    menu:
        thought "Bill likes his fry-ups..."
        "Mayo is crucial" if s3_mc.diet != "Vegan":
            $ s3_mc.like("Bill")
            s3_mc "Awesome. No breakfast is complete without it."
            bill "You know it."
        "Mayo is crucial as long as it's vegan" if s3_mc.diet == "Vegan":
            $ s3_mc.like("Bill")
            seb "Oh yeah, there's a bottle of egg-free mayo here too."
        "I'd eat Bill's sausage any day":
            bill "Just when I thought I'd heard it all..."
            bill "You can have a go later if you'd like."
        "What about ketchup?":
            s3_mc "You can't have eggs without ketchup."
            bill "Right you are!"
            bill "Chuck us the ketchup as well, Seb."
            seb "Sure."
            "He passes over the bottle."

    "Bill serves a dish for you both."
    bill "Bon happy eat!"
    seb "What did you just say?"
    bill "Bon happy eat."
    bill "Like, I hope this meal makes you happy."
    bill "That's what my mum used to always say to me!"
    seb "It's bon appetit, mate."
    seb "Not bon happy eat."
    "Bill shrugs."
    bill "Bon happy eat."
    "Seb rolls his eyes and walks out of the kitchen."

    show seb at npc_exit
    pause 0.3
    $ on_screen.remove("seb")
    $ renpy.hide("seb")

    bill "Suit yourself, Seb."
    "Bill grins as he slides the delicious breakfast towards you."

    # IF STATEMENT
    if s3_mc.diet == "Vegan":
        bill "A perfect vegan fry-up. Complete with baked beans, ten mushrooms, two tomatoes, three vegan sausages, scrambled tofu, and three hash browns."
    elif s3_mc.diet == "Vegetarian":
        bill "A perfect vegetarian fry-up. Complete with baked beans, ten mushrooms, two tomatoes, three vegetarian sausages, scrambled tofu, and three hash browns."
    elif s3_mc.diet == "Meat":
        bill "A perfect fry-up. Complete with baked beans, ten mushrooms, two tomatoes, three sausages, two fried eggs, and three hash browns."
    bill "And condiments!"
    "Nicky comes over to check out the dish."
    nicky "Looks good, mate."

    # IF STATEMENT
    if "Bean Bags" in s3e2p1_visited:
        nicky "I'm going to take Elladine her breakfast."
    else:
        nicky "Elladine wanted some more of these yoghurt things."

    nicky "But if you've got any leftovers I'll have some of that."
    "Nicky heads off out of the kitchen carrying a bowl of oats and yoghurt."
    
    show nicky at npc_exit
    pause 0.3
    $ renpy.hide("nicky")

    bill "We should have our first breakfast up on the roof terrace."
    s3_mc "What, you and Miki?"
    bill "Ah, I was actually thinking about you and me..."
    bill "If you'd like..."

    # CHOICE
    menu:
        thought "Bill wants to have our first breakfast together!"
        "I'd love to have breakfast with you":
            $ s3e2p1_bfast_with_bill = True
            call s3e2p1_bfast_with_bill from _call_s3e2p1_bfast_with_bill
        "Nah, I'm not actually that hungry anymore":
            s3_mc "Sorry Bill, I'm not actually that hungry anymore."
            bill "Oh, OK."
            bill "Well, I don't want it to go cold..."
            bill "Guess, it's just breakfast for one then."
            "You walk off, leaving him in the kitchen alone to eat both plates."
    
    if len(s3e2p1_visited) == 4:
        jump s3e2p1_end
    else:
        call screen s3e2p1_select_who_to_talk_to

    return

label s3e2p1_bfast_with_bill:
    bill "Great!"
    bill "Let's head up."
    "He grabs some cutlery and napkins for you both and you head over to the roof terrace together."

    scene s3-roof-day with dissolve
    $ on_screen = []

    "You and Bill settle down on the roof terrace with your fry-ups on your lap."
    bill "Let's tuck in, yeah?"
    s3_mc "Yeah."

    # CHOICE
    menu:
        thought "Time for breakfast with Bill..."
        "Bon happy eat":
            $ s3_mc.like("Bill")
            bill "Yes!"
            bill "You get me."
            bill "Food is always about making people feel happy."
        "This looks yummy":
            bill "You think?"
            bill "I hope it tastes as good as it looks."
        "Do you cook at home?":
            bill "Yeah, good food is the answer to everything."

    "There's quiet for second as you both begin to eat."
    bill "This ain't so bad!"

    # IF STATEMENT
    if s3_mc.diet == "Meat":
        "Bill grins as you take a bite of a sausage."
    else:
        "Bill grins as you take a bite of your vegan sausage."

    "You nod in agreement, mouth still full."
    bill "Oops!"
    bill "You've got a little bit of mayo on your cheek."

    # CHOICE
    menu:
        thought "I've got mayo on my cheek!"
        "Wipe it off yourself":
            "Bill passes you a napkin. You quickly wipe it off."
            bill "There you go, perfect."
        "Ask him to get it":
            s3_mc "Can you get it?"
            bill "Sure."
            "He whips out a napkin and carefully wipes it off your cheek."
            bill "There you go."
            bill "Perfect."
        "Tell him to lick it off":
            $ s3e2p1_bill_lick = True
            s3_mc "Aw, no! Can you lick it off for me, please?"
            bill "Like, with my tongue?"
            s3_mc "Yeah! Waste not want not...and you did say you loved mayo."
            "Bill shrugs, smiles, and leans over towards you."
            "You feel his breath against your cheek as he licks the mayo off you."
            bill "Got it."
            "He leans back grinning."

    bill "I do love mayo."
    bill "There's nothing better than having a fry-up for breakfast."
    bill "It's my favourite kind of date."
    bill "Especially when it's the morning after the night before."

    if s3_mc.current_partner == "Bill":
        bill "I know we didn't get to spend the night together last night, but..."
    
    bill "This is sort of like a breakfast date, isn't it?"

    # CHOICE
    menu:
        thought "Bill just said we're on a date!"
        "I'm so happy we're on a date together":
            $ s3_mc.like("Bill")
            bill "Yeah, me too."
            bill "I know it's early days, but I really feel like we've got a spark."
        "This is a pretty cheap date":
            $ s3_mc.dislike("Bill")
            bill "Aw, really?"
            bill "That's fair enough."
            bill "Everyone's entitled to their opinions."
            bill "Even if they're wrong."
        "We're just mates, this isn't a date":
            $ s3_mc.dislike("Bill")
            bill "That's fair enough."
            bill "I'd treat anyone to a good fry-up no matter if they fancy me or don't."

    # IF STATEMENT
    if s3_mc.diet == "Meat":
        "Bill dips his last sausage into some of your ketchup."
    else:
        "Bill goes to dip his non-vegan sausage in your ketchup but catches himself just in time."
        bill "Oops, sorry!"

    bill "Did you know..."
    bill "Like, two hundred years ago they thought that ketchup was going to be a medicine."

    # CHOICE
    menu:
        thought "Did I know that ketchup was thought to be a medicine in the 1800s?"
        "Yeah, I knew that":
            bill "It's weird, isn't it?"
            bill "If people back then were looking at my plate right now, they'd think I was ill or something."
        "Ketchup didn't exist then":
            bill "It did! The first published recipe of ketchup was recorded in 1812."
        "That's so cool, what else do you know?":
            bill "Every banana you eat is a clone."
            s3_mc "What?"
            bill "It's true."
            bill "We clone them nowadays."
            s3_mc "Huh?"

    "Bill finishes his food and puts his plate to the side. You finish up the last of your breakfast."
    bill "Thanks for joining me on this fry-up date."

    # IF STATEMENT
    if s3e2p1_bill_lick == True:
        bill "You know, I don't think a girl has ever asked me to lick her face on the first date before."
        s3_mc "What can I say? I'm one of a kind."
        bill "Yep. You've now set the bar for all future girls."
        bill "You're proper hilarious, [s3_name]."

    "Bill runs a hand through his hair and grins at you."
    bill "I've been dying to have a moment alone with you."

    # CHOICE
    menu:
        thought "Bill's been looking forward to this..."
        "I've been daydreaming about it myself":
            bill "Oh really?"
            "He moves closer to you. You can smell his aftershave, something heady and masculine."
            bill "Better make it something worth dreaming about, then."
        "So what are you planning to do with it?":
            bill "I've got a couple of things in mind."
            s3_mc "A couple, eh?"
            bill "Right now, I can only think of one."
        "Just a moment? Bye then":
            "He turns around and takes a step away, then turns back and moves closer to you."
            bill "Hello again."
            s3_mc "A second moment alone! What're you gonna do with it?"
            bill "I've got an idea."

    # CHOICE
    menu:
        thought "He's so close..."
        "Kiss him":
            "You reach out and run your hand along his strong, stubbled jaw, pulling his head to yours."
            "Your lips meet. For a moment, all you can feel is his mouth against yours and the touch of his hands on your waist."
        "Wait for him to kiss you":
            "He leans in and kisses you sweetly. His stubble is rough against your skin."
            "His hands on your waist are firm but gentle as he pulls your body against his."
        "Talk to him instead":
            s3_mc "Let's chat for a bit?"
            bill "Sure. I'd like that."
            s3_mc "What's that aftershave? It smells great."
            bill "It's called 'For Men'."
            s3_mc "Just 'For Men'?"
            bill "I got it off some market stall."

            # SUB-CHOICE
            menu:
                thought "Bill got his aftershave from a market stall..."
                "Well, it's smells great":
                    bill "Cheers. It's not, like, 'classy', but the smell's good, so who cares?"
                    bill "That's all that matters."
                "That's very,er... practical":
                    bill "That's me!"
                    bill "Might not be the 'classiest' place to buy it, but it's still a well expensive brand."
                "Aftershave's a scam anyway":
                    bill "Damn right. It's overpriced alcohol and smelly oil."

    "He smiles at you."
    bill "This is way better than dating on the outside."
    s3_mc "How do you mean?"
    s3_mc "Well, honestly, I'd been coming up empty, relationship-wise."
    s3_mc "The faff was getting on my nerves, you know?"

    # CHOICE
    menu:
        thought "Bill says dating is a faff..."
        "I think so too!":
            s3_mc "I've had a pretty bad run of dates myself."
            bill "Rubbish, isn't it?"
        "I actually really enjoy dating":
            s3_mc "Meeting people, going to new restaurants, learning about someone..."
            bill "Nah, you don't want to go to new restaurants. Getting to know people is hard enough."
            bill "But not knowing if the food's going to be any good either? No thanks?"
            bill "And people can be so hit and miss, you know?"
        "What do you mean by faff?":
            bill "Just all of it. It's a right pain."
            bill "So much effort spent chasing after people, not knowing what they're really like until it's too late."
            bill "But by then you're already in too deep..."

    # CHOICE
    menu:
        thought "Bill's cynical about dating..."
        "I totally agree":
            s3_mc "You're so right."
            s3_mc "I was getting sick of it all myself."
        "It's worth it, though":
            bill "Hasn't paid off yet..."
            bill "I'm in here, after all."
        "I don't think it's a faff at all":
            s3_mc "I really enjoy dating!"
            bill "Good for you."
            bill "Maybe you know something I don't."
            s3_mc "Bill admitting he might not know everything?"
            bill "Oh, shut it."

    bill "It's why I'm in here. All that hassle sorted for us? Yes please."
    bill "Plus, everyone here's guaranteed to be hot and interesting."
    s3_mc "Am I hot and interesting?"
    "He flashes you a grin and winks."
    bill "Is the Pope Catholic?"
    s3_mc "Um..what?"
    bill "I mean, like, yeah obviously you are."
    "Bill shuffles nervously and runs his hand through his hair again."
    "His cheeks flush red."
    bill "Come on, we'd better mingle with the others."
    bill "I'll take your plate to the kitchen."
    "You both head downstairs, feeling full and satisfied after a tasty breakfast."

    return 


#########################################################################
## Episode 2, Part 2
#########################################################################
label s3e2p2:
    scene sand with dissolve
    $ on_screen = []

    show screen day_title(2, 2) with Pause(4)
    hide screen day_title with dissolve

    "Welcome back to Island Amore!"
    "Last time, the Islanders got some exciting news..."

    show bill at npc_center
    bill "Bon happy eat."
    show bill at npc_exit
    pause 0.3
    $ renpy.hide("bill")

    "This wasn't the exciting news, I just had to come back to it to make sure I hadn't imagined it."
    "'Bon happy eat.' Incredible."
    "Anyway, that exciting news I was talking about..."

    show harry at npc_center
    harry "We're all going on dates!"
    show harry at npc_exit
    pause 0.3
    $ renpy.hide("harry")

    "But who will the boys choose?"
    "And will any of them leave an impression on [s3_name]?"
    " Let's find out..."

    scene s3-dressing-room with dissolve
    $ on_screen = []

    "Our brand new Villa comes equipped with all the luxury extras you might expect..."
    "Including a state-of-the-art information exchange environment the girls can use to talk about the boys."
    "Sorry, I think it's still technically called the 'dressing room.'"

    genevieve "I really hope I get picked to go on a date!"
    miki "Me too! I'd love to get some proper time alone with Bill."
    iona "It's so annoying that the boys get to choose and we're stuck waiting around to see who gets picked."
    genevieve "I'm sure we'll get our chance to do the choosing again soon."
    aj "Yeah, don't worry! I doubt we'll be waiting long."
    iona "It's easy for you two to be chill about it."
    iona "You're coupled up with the only two boys who don't have their eyes on [s3_name]."
    "There's an awkward pause as everyone looks at you."
    miki "It's true, babes. With you being single, I guess it's hard for us not to see you as a threat."

    # CHOICE
    menu:
        thought "Am I a threat to the couples?"
        "-Yeah, I'm a red alert":
            s3_mc "Wee-oo! Wee-oo!"
            s3_mc "You hear that?"
            s3_mc "That's the MC alert siren."
            s3_mc "It means I'm here, I'm dangerous, and I can't be stopped."
            "Elladine snorts with laughter."
            iona "Oh my gosh."
        "I don't have much choice...":
            $ s3_mc.like("Elladine")
            s3_mc "Look, none of this is my fault. I didn't ask to be single."
            s3_mc "And I can't help it if the boys like me, either."
            s3_mc "It's their turn to choose the dates, so there's nothing we can do about it now."
            elladine "Well said, [s3_name]."
        "Come on, let's chill out":
            $ s3_mc.like("Elladine")
            s3_mc "What happened to all that talk about how we're going to be friends, and not waste our time on petty drama?"
            s3_mc "Those boys are choosing, so it's out of our hands."
            s3_mc "Whatever happens, will happen."
            s3_mc "But you're still my girls, OK?"
            s3_mc "And we can handle our emotions like adults."
            elladine "Well said, [s3_name]."

    elladine "Let's not forget, [s3_name] was coupled up with [s3_mc.current_partner] first, until [s3_3rd_girl] came along."
    elladine "Nobody is the villain here."
    elladine "We're all just playing the cards we've been dealt."
    genevieve "That's true. Any of us could end up single at the next recoupling, so let's all just try to show a little understanding."
    "Just as Genevieve finishes talking, her phone beeps."
    genevieve "I've got a text!"
    aj "What does it say?"
    "Genevieve reads aloud."
    genevieve "'Girls, the boys have now made their decisions. Each of them chose one of you to date and their decisions were as follows...'"
    genevieve "'Nicky has chosen Elladine.'"
    elladine "Yay!"
    aj "No surprises there!"
    genevieve "'Seb has invited AJ.'"
    aj "Wait, really?"
    aj "I mean... cool, I guess."

    # IF STATEMENT
    if s3_like_aj:
        "She looks at you and bites her lips."
        aj "Maybe it is a shame that we can't choose for ourselves after all, huh, babes?"
        aj "'Cause I know who I would've picked."

    elladine "I'm sure you'll have a great time, AJ."
    miki "Read out the rest of the text!"
    iona "Yeah! Who did Camilo choose?"
    "Genevieve looks back at her phone and starts reading again."
    genevieve "'Camilo has chosen... [s3_name].'"
    iona "Oh..."
    genevieve "'Bill has also invited [s3_name].'"
    miki "What?!"
    genevieve "'And Harry has invited...'"
    "Genevieve's face falls slightly."
    genevieve "[s3_name]."
    elladine "Woah! Three dates, [s3_name]?!"
    iona "Leave some boys for the rest of us!"

    # CHOICE
    menu:
        thought "Bill, Camilo and Harry all invited me for dates!"
        "Well, this is embarrassing":
            s3_mc "Sorry, girls. I guess this is exactly what you were nervous about."
            genevieve "It's OK, [s3_name]."
            genevieve "You go have a good time."
            "Genevieve is clearly trying, but she can't hide how disappointed she is."
        "This is going to be awesome":
            s3_mc "Yes! Time for me to crack on!"
            elladine "Yeah! You go, girl!"
        "I'm going to be exhausted":
            s3_mc "Three dates?"
            s3_mc "That's way too many dates."
            genevieve "It says here you don't have to go on all three dates if you don't want to."

    aj "So, who are you going to see first?"

    # CHOICE
    menu:
        thought "Which boy do I want to date first?"
        "Bill":
            $ s3e2p2_first_date = "Bill"
        "Camilo":
            $ s3e2p2_first_date = "Camilo"
        "Harry":
            $ s3e2p2_first_date = "Harry"

    if s3_mc.current_partner == s3e2p2_first_date:
        aj "Oh, yeah. Makes sense."
        aj "Since you were coupled with him, and everything."
    else:
        if s3_mc.current_partner == "Bill":
            aj "Oh, I thought you were going to say Bill."
        elif s3_mc.current_partner == "Camilo":
            aj "Oh, I thought you were going to say Camilo"
        elif s3_mc.current_partner == "Harry":
            aj "Oh, I thought you were going to say Harry."

    elladine "Come on, then! We've been standing here chatting long enough."
    elladine "Let's go and meet our dates!"

    # ORDER OF DATES
    # FIRST DATE
    scene s3-beach-date with dissolve
    $ on_screen = []

    $ outfit = "evening"

    "A date and chairs have been set out on the sand for your date. There's a bottle of champagne and two glasses."
    "[s3e2p2_first_date] is already waiting for you."
    "His face lights up as you stride across the beach, and he stands up to greet you."

    # IF STATEMENT
    if s3e2p2_first_date == "Bill":
        bill "Hey, [s3_name]!"
        bill "You look amazing. I mean, you always do."
        bill "But especially so today."
        # Add back when adding in MC images with alternative outfit choices
        # bill "You look amazing. That outfit is really something else."
        # bill "I mean, obviously. You don't need me to tell you that. I just..."
        # bill "You look amazing. Even when you're not trying."
        # bill "Not that I'm saying you don't put effort in!"
        # bill "Just that, what you're wearing it's not like... you know..."
        bill "Sorry, I'm rambling."
        bill "I'm glad you wanted to see me first."
    elif s3e2p2_first_date == "Camilo":
        camilo "Hey, [s3_name]!"
        camilo "You look amazing. I mean, you always do."
        camilo "But especially so today."
        # Add back when adding in MC images with alternative outfit choices
        # camilo "You look amazing. That outfit is really something else."
        # camilo "I mean, obviously. You don't need me to tell you that. I just..."
        # camilo "You look amazing. Even when you're not trying."
        # camilo "Not that I'm saying you don't put effort in!"
        # camilo "Just that, what you're wearing it's not like... you know..."
        camilo "Sorry, I'm rambling."
        camilo "I'm glad you wanted to see me first."
    elif s3e2p2_first_date == "Harry":
        harry "Hey, [s3_name]!"
        harry "You look amazing. I mean, you always do."
        harry "But especially so today."
        # Add back when adding in MC images with alternative outfit choices
        # harry "You look amazing. That outfit is really something else."
        # harry "I mean, obviously. You don't need me to tell you that. I just..."
        # harry "You look amazing. Even when you're not trying."
        # harry "Not that I'm saying you don't put effort in!"
        # harry "Just that, what you're wearing it's not like... you know..."
        harry "Sorry, I'm rambling."
        harry "I'm glad you wanted to see me first."

    # CHOICE
    menu:
        thought "I chose to see [s3e2p2_first_date] first..."
        "I'm excited for us to spend some time alone together":
            $ s3_mc.like(s3e2p2_first_date)
            s3_mc "I've been really looking forward to this!"
            if s3e2p2_first_date == "Bill":
                bill "Me too."
            elif s3e2p2_first_date == "Camilo":
                camilo "Me too."
            elif s3e2p2_first_date == "Harry":
                harry "Me too."
        "It's a great honour, so try not to screw it up":
            s3_mc "You're getting me at my freshest, so I expect to be wowed, OK?"
            if s3e2p2_first_date == "Bill":
                bill "Noted."
            elif s3e2p2_first_date == "Camilo":
                camilo "Noted."
            elif s3e2p2_first_date == "Harry":
                harry "Noted."
        "I just wanted to get it out of the way":
            $ s3_mc.dislike(s3e2p2_first_date)
            s3_mc "Don't read too much into it. I had to start somewhere."
            if s3e2p2_first_date == "Bill":
                bill "Oh... OK."
            elif s3e2p2_first_date == "Camilo":
                camilo "Oh... OK."
            elif s3e2p2_first_date == "Harry":
                harry "Oh... OK."
    "He pulls your chair out for you and you both take your seats."
    
    if s3e2p2_first_date == "Bill":
        call s3e2p2_bill_date from _call_s3e2p2_bill_date
    elif s3e2p2_first_date == "Camilo":
        call s3e2p2_camilo_date from _call_s3e2p2_camilo_date
    elif s3e2p2_first_date == "Harry":
        call s3e2p2_harry_date from _call_s3e2p2_harry_date

    $ on_screen = []

    "You're left sitting alone for a minute, basking in the sun, until your phone beeps."
    thought "I've got a text."
    text "[s3_name], you need to date at least one more boy before returning to the Villa. Please decide who you would like to join you next."

    ## SECOND DATE

    # CHOICE
    menu:
        thought "For my second date, I would like..."
        "Bill" if s3e2p2_first_date != 'Bill':
            $ s3e2p2_second_date = "Bill"
        "Camilo" if s3e2p2_first_date != 'Camilo':
            $ s3e2p2_second_date = "Camilo"
        "Harry" if s3e2p2_first_date != 'Harry':
            $ s3e2p2_second_date = "Harry"

    # IF STATEMENT - Set Third Date
    if s3e2p2_first_date != "Bill" and s3e2p2_second_date != "Bill":
        $ s3e2p2_third_date = "Bill"
    elif s3e2p2_first_date != "Camilo" and s3e2p2_second_date != "Camilo":
        $ s3e2p2_third_date = "Camilo"
    elif s3e2p2_first_date != "Harry" and s3e2p2_second_date != "Harry":
        $ s3e2p2_third_date = "Harry"

    "You type [s3e2p2_second_date]'s name into your phone and hit send."
    "A second later, your phone beeps again."
    text "[s3_name], your second date will be with you very soon! #popularqueen #indemand"
    "You sit alone for a while, toying with your champagne glass and admiring the view."
    "After a minute, you see [s3e2p2_second_date] approaching across the beach."

    if s3e2p2_second_date == "Bill":
        bill "[s3_name]! Hi!"
        "He smiles as he reaches the table."
        bill "Mind if I sit down here?"

        # CHOICE
        menu:
            thought "[s3e2p2_second_date] asked if he can sit down..."
            "Be my guest":
                s3_mc "I'll get lonely otherwise, out here all by myself."
                bill "Well, we can't have that."
            "If you must":
                $ s3_mc.dislike(s3e2p2_second_date)
                s3_mc "Fine. I guess."
                bill "Um, thanks."
            "Pull out his chair for him":
                $ s3_mc.like(s3e2p2_second_date)
                s3_mc "Here."
                "You quickly get up and pull out his chair."
                bill "This is off to a good start, isn't it?"
                bill "Thanks."
    elif s3e2p2_second_date == "Camilo":
        camilo "[s3_name]! Hi!"
        "He smiles as he reaches the table."
        camilo "Mind if I sit down here?"

        # CHOICE
        menu:
            thought "[s3e2p2_second_date] asked if he can sit down..."
            "Be my guest":
                s3_mc "I'll get lonely otherwise, out here all by myself."
                camilo "Well, we can't have that."
            "If you must":
                $ s3_mc.dislike(s3e2p2_second_date)
                s3_mc "Fine. I guess."
                camilo "Um, thanks."
            "Pull out his chair for him":
                $ s3_mc.like(s3e2p2_second_date)
                s3_mc "Here."
                "You quickly get up and pull out his chair."
                camilo "This is off to a good start, isn't it?"
                camilo "Thanks."
    elif s3e2p2_second_date == "Harry":
        harry "[s3_name]! Hi!"
        "He smiles as he reaches the table."
        harry "Mind if I sit down here?"

        # CHOICE
        menu:
            thought "[s3e2p2_second_date] asked if he can sit down..."
            "Be my guest":
                s3_mc "I'll get lonely otherwise, out here all by myself."
                harry "Well, we can't have that."
            "If you must":
                $ s3_mc.dislike(s3e2p2_second_date)
                s3_mc "Fine. I guess."
                harry "Um, thanks."
            "Pull out his chair for him":
                $ s3_mc.like(s3e2p2_second_date)
                s3_mc "Here."
                "You quickly get up and pull out his chair."
                harry "This is off to a good start, isn't it?"
                harry "Thanks."

    "He takes a seat opposite you and pours himself some champagne."

    if s3e2p2_second_date == "Bill":
        call s3e2p2_bill_date from _call_s3e2p2_bill_date_1
    elif s3e2p2_second_date == "Camilo":
        call s3e2p2_camilo_date from _call_s3e2p2_camilo_date_1
    elif s3e2p2_second_date == "Harry":
        call s3e2p2_harry_date from _call_s3e2p2_harry_date_1

    $ on_screen = []

    # THIRD DATE
    "You find yourself sitting alone again. The champagne bottle is almost empty."
    thought "I've got another text..."
    text "[s3_name], you've now been on a date with [s3e2p2_first_date] and [s3e2p2_second_date]. Your third date will be with [s3e2p2_third_date]."

    # CHOICE
    menu:
        thought "My last date is with [s3e2p2_third_date]..."
        "Yes! Bring it on!":
            "A few minutes later, [s3e2p2_third_date] joins you at the table."
            if s3e2p2_third_date == "Bill":
                bill "Hi, [s3_name]. Thanks for sticking around."
            elif s3e2p2_third_date == "Camilo":
                camilo "Hi, [s3_name]. Thanks for sticking around."
            elif s3e2p2_third_date == "Harry":
                harry "Hi, [s3_name]. Thanks for sticking around."
            "He sits down opposite you and pours himself a drink."
        "Eh, may as well see him too":
            "A few minutes later, [s3e2p2_third_date] joins you at the table."
            if s3e2p2_third_date == "Bill":
                bill "Hi, [s3_name]. Thanks for sticking around."
            elif s3e2p2_third_date == "Camilo":
                camilo "Hi, [s3_name]. Thanks for sticking around."
            elif s3e2p2_third_date == "Harry":
                harry "Hi, [s3_name]. Thanks for sticking around."
            "He sits down opposite you and pours himself a drink."
        "Actually, I'm ready to go back to the villa":
            $ s3e2p2_only_two_dates = True
            thought "Two dates is enough for me."
            thought "Besides, it's starting to get a bit chilly out here."
            thought "I'm sure [s3e2p2_third_date] won't mind."
            "You finish the last of your champagne, get to your feet, and head back to the Villa."
    
    if s3e2p2_only_two_dates == False:
        if s3e2p2_third_date == "Bill":
            call s3e2p2_bill_date from _call_s3e2p2_bill_date_2
        elif s3e2p2_third_date == "Camilo":
            call s3e2p2_camilo_date from _call_s3e2p2_camilo_date_2
        elif s3e2p2_third_date == "Harry":
            call s3e2p2_harry_date from _call_s3e2p2_harry_date_2

    scene s3-lawn-day with dissolve
    $ on_screen = ["camilo"]

    show camilo at npc_center

    if s3e2p2_only_two_dates:
        "When you arrive back at the Villa, you find the lawn deserted."
        thought "Where has everyone got to?"
        thought "I'll have a look and find out..."
    else:
        "You and [s3e2p2_third_date] walk into the Villa to find it deserted."
        s3_mc "Where is everyone?"
        if s3e2p2_third_date == "Bill":
            bill "I'll see if I can find out."
        elif s3e2p2_third_date == "Camilo":
            camilo "I'll see if I can find out."
        elif s3e2p2_third_date == "Harry":
            harry "I'll see if I can find out."
        "He walks inside."

    scene s3-gym-day with dissolve
    $ on_screen = []

    "The only person around is AJ, doing pull-ups in the gym."
    aj "Hey, [s3_name]! Welcome back!"
    "She carefully lowers herself to the ground and wipes her forehead."
    aj "Sorry, I'm all sweaty."
    aj "Everyone else is inside, so I thought I'd take the chance to squeeze in a workout."
    aj "I need to burn off some energy every day or I can't sit still."
    aj "My coach says I'm like a puppy sometimes."

    # CHOICE
    menu:
        thought "AJ likes working out..."
        "I really enjoy it, too":
            s3_mc "Nothing like exercise to get the endorphins pumping."
            aj "Maybe we can be gym buddies."
        "I'd rather be sunbathing":
            s3_mc "Why would I make myself sweaty and tired when I could be sunning myself beside the pool?"
            aj "Good answer. I'm kinda glad, actually."
            aj "It's been hard enough finding time to work out with the boys all hogging the equipment."
            aj "I don't need any more competition!"
        "I prefer watching the boys...":
            s3_mc "They look so hot when they're working out."
            aj "Oh yeah, tell me about it."
            aj "I think they totally know they do, too."
            s3_mc "Oh, one hundred percent."
        "I prefer watching you..." if s3_like_aj == True:
            $ s3_mc.like("AJ")
            s3_mc "I'm not gonna lie, seeing you on that pull-up bar makes it difficult to ignore..."
            s3_mc "You're pretty hot."
            "She raises her eyebrows and grins."
            aj "Remind me to get my sweat on more often when you're around, then."

    "She takes a swig from her water bottle."
    aj "Sorry, I haven't even asked yet..."
    aj "How did your dates go?"

    # CHOICE
    menu:
        s3_mc "My dates were..."
        "Really fun":
            s3_mc "I had a great time. Turns out these boys do have good chat."
            aj "Yes! Babes, I'm so glad!"
            aj "I know you're technically single, but you're doing so much better than me right now."
        "A mixed bag":
            s3_mc "You know, some good, some bad. I'm still sorting through it all in my head."
            aj "Well, that sounds promising!"
            aj "You're doing better than me right now, anyway."
        "A waste of time":
            s3_mc "These boys have no chat."
            s3_mc "I'd have been better off staying at the Villa."
            aj "Ah, mate. I'm so sorry."
            aj "If it's any consolation, I'm kind of in the same boat."

    "She sighs."
    aj "I know it's a bit early to say, but I really don't think anything's going to happen between me and Seb."
    aj "I thought he looked all cool and interesting when I coupled up with him, but our energies just don't match at all."
    aj "And the date was a disaster."
    aj "I asked him if there were any girls in the Villa he fancied, and he changed the subject."
    aj "Started telling me a story about some gig he saw back in the day where the band all started brawling onstage."
    aj "It was a great story, to be fair."
    aj "But it was pretty obvious he doesn't see me that way."

    if s3_like_aj:
        aj "Then he asked me if there were any girls in the Villa I fancied."
        s3_mc "And what did you say?"
        aj "I said 'yes', of course."

    # CHOICE
    menu:
        thought "AJ says she doesn't feel much potential with Seb..."
        "You should give him a chance":
            s3_mc "You've only known him for a couple of days."
            s3_mc "Once you two spend a bit more time together, you might realise you've got more in common than you thought."
            aj "I guess."
        "You should crack on with someone else":
            s3_mc "Things move fast in here. Don't waste your time on a relationship that's not going anywhere."
            s3_mc "You should get grafting, girl!"
            aj "Yes! Exactly!"
            aj "Ugh, you're so wise. I'm glad I talked to you about this."
        "You should crack on with me":
            $ s3_mc.like("AJ")
            s3_mc "Things move fast in here."
            s3_mc "Don't waste your time on a relationship that's not going anywhere."
            s3_mc "Especially when I'm right here in front of you."
            "She blushes as a big smile spreads across her face."
            aj "You really mean that?"
            s3_mc "I said it, didn't I?"

    "She slurps on the water bottle again, even though it's almost empty."

    if s3_like_aj:
        aj "You know..."
        aj "I was thinking earlier, about how it's not fair."
        s3_mc "What's not fair?"
        aj "All the boys got the chance to invite you on a date, but I didn't get the option."
        s3_mc "Are you saying you would have asked me, if you could?"
        aj "In a heartbeat, babe. I'd love to spend some time alone with you."
        s3_mc "Well... you're alone with me now."
        "AJ looks at you for a moment."
        "Without saying a word, she takes a step towards you."
        "She raises one arm to lean against the weight machine behind you, bringing her face close to yours."

        # CHOICE
        menu:
            thought "I think we're having a moment."
            "Move away from her":
                $ s3_mc.dislike("AJ")
                "You nonchalantly dodge around her so you're standing under the pull-up bar."
            "Go in for a kiss":
                $ s3_mc.like("AJ")
                "You lean forward, closing the last few inches between you."
                "You let your eyes fall shut as your lips meet hers."
                "She kisses you back without hesitation, excited and tender all at once."
                "Her free hand caresses your waist, pulling you close against her toned stomach."
                "When you finally break the kiss, her eyes are round and sparkling."
                aj "Wow."
                s3_mc "Slick comeback."
                aj "Give me a break."
                aj "I'm not good with words at the best of times."
                aj "Let alone when I'm standing this close to a beautiful girl."
                s3_mc "Now, that actually was slick."
            "Say something flirty":
                # FILL IN
                "EMPTY"
        "AJ reluctantly steps away from you and waves to the group."
    else:
        "Just then, you spot some of the other Islanders coming towards you across the lawn."

    scene s3-lawn-day with dissolve
    $ on_screen = []

    nicky "Hey, [s3_name]! You're back!"
    elladine "How were your three dates, babes?"

    if s3e2p2_only_two_dates:
        s3_mc "Actually, I only saw [s3e2p2_first_date] and [s3e2p2_second_date]."
        s3_mc "I didn't feel like sticking around for [s3e2p2_third_date]."
        elladine "Oh! Why not?"

        # CHOICE
        menu:
            s3_mc "I didn't go on a date with [s3e2p2_third_date] because..."
            "I'm just not interested in him":
                s3_mc "It would have been a waste of both our time, honestly."
                elladine "Fair enough."
            "I needed a break from dating":
                s3_mc "It's really tiring. I just wanted to come back here and chill out a bit."
                elladine "Fair enough."
            "I didn't want to upset Miki" if s3e2p2_third_date == "Bill":
                $ s3_mc.like("Miki")
                "Miki smiles gratefully at you."
            "I didn't want to upset Iona" if s3e2p2_third_date == "Camilo":
                $ s3_mc.like("Iona")
                "Iona smiles gratefully at you."
            "I didn't want to upset Genevieve" if s3e2p2_third_date == "Harry":
                $ s3_mc.like("Genevieve")
                "Genevieve smiles gratefully at you."

    miki "What was the place like? Was it super romantic?"

    # CHOICE
    menu:
        s3_mc "The date location..."
        "It had a really pretty view":
            s3_mc "It was this lovely spot on the beach, right next to the ocean."
        "It wasn't for me":
            s3_mc "I mean, if you've seen one beach, you've seen them all."
            s3_mc "I'm hoping for something a bit fancier next time."
        "I'm never going to the beach in heels again":
            s3_mc "Who thought that was a good idea?"
            s3_mc "I'm not Wonder Woman."

    nicky "Me and Elladine were on the beach, too. It was nice."
    elladine "Yeah, it was really romantic!"
    iona "Ooh, did you two make a bit of a connection?"
    nicky "I think maybe we did, yeah."
    iona "What about you, [s3_name]?"
    iona "Did you feel that special spark with someone?"
    thought "This is my chance to make sure everyone knows exactly what I'm after."
    thought "I'm single, and I'm going to have to couple up soon."
    thought "I should use this chance to make it clear what I want."
    thought "Then they'll have to accept that I'm not here to mess around."

    if s3_like_aj:
        thought "I could even say AJ, even though we didn't get to go on an official date!"
        thought "Then it's like, nobody can pretend we don't have a thing going on."

    # CHOICE
    menu:
        thought "Did I feel a special spark with someone today?"
        "Yes, and I'll tell you who...":
            iona "You did?"
            elladine "Who's the lucky boy, babes?"
            miki "Go on, spill the tea!"

            # SUB-CHOICE
            menu:
                s3_mc "I really hit it off with..."
                "Bill" if s3e2p2_first_date == 'Bill' or s3e2p2_second_date == 'Bill' or (s3e2p2_third_date == 'Bill' and s3e2p2_only_two_dates == False):
                    $ s3e2p2_special_spark = "Bill"
                    s3_mc "He was really sweet and funny. I had a great time."
                    s3_mc "And I'm pretty sure he did, too."
                    s3_mc "I definitely think there's something developing there."
                    elladine "That's so exciting!"
                    seb "He's gonna be made up when we tell him you said that."
                    "Miki bites her lips and looks away."
                "Camilo" if s3e2p2_first_date == 'Camilo' or s3e2p2_second_date == 'Camilo' or (s3e2p2_third_date == 'Camilo' and s3e2p2_only_two_dates == False):
                    $ s3e2p2_special_spark = "Camilo"
                    s3_mc "He was really sweet and funny. I had a great time."
                    s3_mc "And I'm pretty sure he did, too."
                    s3_mc "I definitely think there's something developing there."
                    elladine "That's so exciting!"
                    seb "He's gonna be made up when we tell him you said that."
                    "Iona frowns, but doesn't say anything."
                "Harry" if s3e2p2_first_date == 'Harry' or s3e2p2_second_date == 'Harry' or (s3e2p2_third_date == 'Harry' and s3e2p2_only_two_dates == False):
                    $ s3e2p2_special_spark = "Harry"
                    s3_mc "He was really sweet and funny. I had a great time."
                    s3_mc "And I'm pretty sure he did, too."
                    s3_mc "I definitely think there's something developing there."
                    elladine "That's so exciting!"
                    seb "He's gonna be made up when we tell him you said that."
                    "Genevieve sighs softly, but doesn't say anything."
                "AJ" if s3_like_aj == True:
                    $ s3e2p2_special_spark = "AJ"
                    s3_mc "Not a boy at all, actually."
                    s3_mc "Me and AJ have been just hanging out here, and I had a better time with her than any of the boys."
                    s3_mc "I definitely think we've got something started between us."
                    "AJ grins sheepishly and puts an arm around your waist."
                    miki "Oh my gosh! You two are so cute together!"
                    aj "We are, aren't we?"
                    s3_mc "So you can all relax now, girls."
                    s3_mc "I'm not planning to pie anyone off in the near future."
                    s3_mc "Except Sec, I guess. Sorry about that."
                    seb "No, it's OK!"
                    seb "Me and AJ were only ever gonna be friends, anyway."
                    seb "You two would make a much better couple."
                    elladine "So, it looks like [s3_name] might not be single for very long."

        "I don't want to tell you":
            seb "You spent all afternoon dating and you don't even want to share your thoughts?"
            seb "That's a dangerous game for someone who's single, if you ask me."
        "Maybe I did, maybe I didn't":
            s3_mc "Who can say? I'm an enigma."
            s3_mc "You'll all just have to wait and find out."
            seb "Tease!"
        "Nope, not yet":
            s3_mc "There's no standout candidate yet, to be honest."
            iona "That's a shame, love."
            nicky "It's alright. It's early days."
            nicky "She's got plenty of time to find someone."

    "Just then you see the other boys making their way towards you."
    camilo "Alright? How's it going?"
    aj "We were talking about our dates."
    bill "Oh yeah, of course. What a day, huh?"

    if s3e2p2_special_spark == "Bill":
        bill "I hope [s3_name] said good things."
        seb "She certainly did..."
    elif s3e2p2_special_spark == "Camilo":
        camilo "I hope [s3_name] said good things."
        seb "She certainly did..."
    elif s3e2p2_special_spark == "Harry":
        harry "I hope [s3_name] said good things."
        seb "She certainly did..."

    harry "Do you think we could finish this conversation over dinner?"
    harry "I'm starving."
    camilo "Me too."
    camilo "How about we do the cooking tonight, lads?"
    camilo "As a treat for the girls. Since we got to choose the dates."
    seb "I'm up for that. I'm a pretty good cook."
    iona "Are you? Really?"
    seb "Not even a little bit, but I thought it might come true if I said it with enough confidence."
    nicky "That's the spirit. Come on, lads, let's get to the kitchen."
    seb "You girls go relax. The boys have got this."

    scene sand with dissolve
    $ on_screen = []

    "Coming up..."
    "The boys make dinner..."
    show nicky at npc_center
    nicky "How'd you take so long to slice a mushroom, man?"
    show nicky at npc_exit
    pause 0.3
    $ renpy.hide("nicky")

    "Nicky's claim that they've 'got this' is tested to its limits..."
    
    show aj at npc_center
    aj "Woah, that's a lot of cheese, Bill."
    show aj at npc_exit
    pause 0.3
    $ renpy.hide("aj")
    
    "And Genevieve doesn't know how to handle the results..."
    
    show genevieve at npc_center
    genevieve "It looks a bit stiff..."
    show genevieve at npc_exit
    pause 0.3
    $ renpy.hide("genevieve")

    jump s3e2p3

    return

label s3e2p2_bill_date:

    if s3e2p1_bfast_with_bill:
        bill "I know I said this morning was kinda like a date."
        bill "But this is our first proper date, like, officially."
        s3_mc "What's the difference?"
        bill "I dunno. I guess we talk about more date-type things?"
        bill "Like this..."
        "He clears his throat and puts on a serious face."

    bill "How you finding life in the Villa so far?"

    # CHOICE
    menu:
        thought "How am I finding life on Island Amore?"
        "It's everything I hoped it would be":
            s3_mc "The weather, the people, the Villa... it's all great."
            s3_mc "I hope I don't get dumped before I've had a chance to really enjoy myself properly."
            bill "You and me both!"
        "It's a mix of good and bad":
            s3_mc "It's like anything. Really fun in some ways..."
            bill "Kinda weird and overwhelming in others?"
            s3_mc "Yeah."
            s3_mc "I hope I don't get dumped before I've had a chance to really enjoy myself properly."
            bill "You and me both!"
        "I'm still waiting for the 'Love'":
            s3_mc "Things better start getting romantic around here, and quick, or I'm off."
            bill "Noted."
            bill "Give it another twenty minutes or so, and then if things haven't heated up to your expectations, I'll help you build an escape raft."
            bill "But I'm sure it won't come to that."

    bill "I'd be gutted if you left now. I've barely started getting to know you."
    s3_mc "Yeah, but I'm single now, aren't I?"
    s3_mc "So it might not be up to me."
    s3_mc "If I don't couple up with someone, I'll be done."
    bill "Something tells me coupling up isn't gonna be a problem for a girl like you."
    "You raise your glass. Bill cheerfully clinks his glass against it."
    "He takes a sip of champagne and scrunches up his nose."
    bill "I'll never understand why people pay so much for this stuff."
    bill "It's not even that nice."
    s3_mc "Let me guess, you're more of a beer guy?"
    bill "Well, yeah, obviously."

    # CHOICE
    menu:
        thought "Bill prefers beer to champagne..."
        "You're so right":
            s3_mc "Give me a nice pint over a glass of bubbly any day."
            bill "Right answer."
            s3_mc "So if I'd said the opposite... what? You would've just got up and walked away?"
            bill "No way!"
            bill "If anything, it would've been even better if you'd disagreed with me."
            s3_mc "Huh?"
            bill "Then we could've had a proper debate about it."
        "You're so wrong":
            s3_mc "Give me a glass of bubbly over a beer any day."
            bill "Ah, mate, no way. I wish I could take you for a pint at my local."
            s3_mc "I'm sure it's great, but I don't need you to try to change my mind about what drinks i like."
            bill "I didn't mean to try to change your mind!"
            bill "I meant so we could have a proper debate about it."
        "Who cares?":
            s3_mc "It's all alcohol at the end of the day, right?"
            bill "Well, yeah...but it's not really about the drink itself."
            bill "It's about the debate you have about the drink."

    bill "I absolutely love a chat like that, when you go back and forth with someone all night..."
    bill "Telling each other you're wrong about beer vs wine, or cats vs dogs, or football vs rugby, or whatever."
    bill "It doesn't matter what it is."
    bill "The point is, there's no point to it."
    bill "It's not a real fight because you both know it doesn't really matter if you're wrong."
    bill "It's just a laugh. And when you get bored of it, you can change the subject and start arguing about something else."
    bill "I think you're probably really good at it."
    bill "You, Nicky and Camilo are all high on my list of people to have pointless chats with."

    # CHOICE
    menu:
        thought "Bill enjoys having pointless arguments..."
        "Me too, I think it's fun":
            s3_mc "I love a good pointless fight about what the best movie ever made is, or something like that."
            bill "Yeah! Exactly!"
            bill "It's Rocky IV, for the record."
            s3_mc "Rocky...four? Isn't that really old?"
            bill "It's not old, it's classic."
            bill "And yeah, it has to be Rocky IV."
            bill "Why would they keep making them if they didn't get better each time?"
            s3_mc "I'm not sure about that logic..."
            bill "Well, I'd love to get into it with you properly, but I think our time's almost up."
            if s3_mc.current_partner != "Bill":
                bill "Thanks for giving me a chance today. (if you weren't coupled with him before)"
        "Nah, that makes no sense":
            bill "But we could have a really good debate about it, couldn't we?"
            s3_mc "I'd rather not."
        "Well, you're wrong about champagne!":
            s3_mc "It's good! It's fizzy and sweet!"
            s3_mc "It makes me feel fancy!"
            "Bill laughs."
            bill "But it's the fizziness and the fanciness I don't like about it!"
            bill "All the bubbles go up my nose and then I'm trying not to burp because I'm supposed to be acting fancy!"
            s3_mc "But that's all part of the fun!"

    if s3_mc.current_partner == "Bill":
        "He puts his hand on the table next to yours, as if he wants to take it but isn't sure if he should."
        bill "Hey..."
        bill "I'm really sorry about what happened last night."
        bill "I know Miki wasn't trying to hurt anyone, but I wish she hadn't broken us up."
        bill "You were the one I really wanted. You still are."

        # CHOICE
        menu:
            thought "Bill would rather be with me than Miki..."
            "Well, yeah, I'm pretty great":
                s3_mc "Sexy, funny, smart. I'm the whole package."
                bill "Yes, you are. Miki knows that as well as I do."
            "But she's so lovely":
                s3_mc "She's so pretty and cool!"
                bill "Yeah..."
            "Does she know you feel that way?":
                bill "Yeah, of course."
                bill "We had a chat about it last night. I told her the truth."

        bill "She's a great girl, and I'm not necessarily opposed to getting to know her better..."
        bill "It's just that I never expected to be in this position, and now I don't know what to do."
        bill "You were my first choice, at the end of the day."
        "His eyes rest longingly on yours for a moment, before he quickly looks down at his empty champagne glass."

    bill "I've had a proper lovely time."
    bill "I'm sorry we didn't get into any of the classic first date chat, like how many siblings we've got and all that."

    if s3e2p1_bill_lick:
        bill "Though I guess once you licked mayo off someone's face, all that stuff seems a bit low-key."

    # CHOICE
    menu:
        thought "There's a lot of things we didn't get to talk about..."
        "We've got to save something for our next date":
            $ s3_mc.like("Bill")
            $ s3_like_bill = True
            $ s3_lis.append("Bill")
            bill "Yeah?"
            s3_mc "Yeah."
            s3_mc "And we'll see if your beer opinions really stand up to scrutiny."
            bill "I'm looking forward to it."
        "It's OK, I've still had a nice time":
            s3_mc "Your chat's pretty good, honestly."
            bill "Thanks! You're not so bad yourself."
        "Yeah, let's never do this again":
            $ s3e2p2_reject_bill = True
            $ s3_mc.dislike("Bill")
            s3_mc "I don't think we really clicked, Sorry."
            bill "Oof. Sorry about that."
            bill "At least it's over now, hey."

    "He stands up."
    if s3e2p2_first_date == "Bill" or s3e2p2_second_date == "Bill":
        bill "See you back at the Villa, then, [s3_name]."

    if s3e2p2_reject_bill != True:
        "He blows you a kiss as he leaves."

    show bill at npc_exit
    pause 0.3
    $ renpy.hide("bill")

    return

label s3e2p2_camilo_date:
    camilo "This is proper swanky, isn't it?"
    "He gestures to the crystal blue waves rolling against the beach."
    camilo "I've been for beach picnics before, but nothing like this."

    # CHOICE
    menu:
        s3_mc "As date locations go, this is..."
        "Way fancier than I'm used to":
            camilo "Yeah, same!"
        "About normal for me":
            camilo "Wow, really? You must be living a pretty glamorous life."
            camilo "It doesn't surprise me. You've got that kinda vibe about you."
        "Below my usual standard":
            camilo "Wow, really? You must be living a pretty glamorous life."
            camilo "It doesn't surprise me. You've got that kinda vibe about you. "

    camilo "I'd usually take someone for a meal, and then maybe the cinema, if there's something we both want to see."
    camilo "But it's nice to get out of your comfort zone for once."
    camilo "And it's especially nice to get a bit of quiet time out here with you."
    camilo "Don't get me wrong, I like the others. They seem like a sound lot."
    camilo "But I think this table might get a bit crowded with nine more chairs."

    # CHOICE
    menu:
        s3_mc "The rest of the Islanders..."
        "They all seem so nice":
            s3_mc "They've been really sweet to me so far."
            s3_mc "I already feel like I'm going to make some good friends here."
            camilo "That's great. Same here, honestly."
        "I like them...with some exceptions":
            s3_mc "I mean... for the most part, everyone's really nice."
            s3_mc "But without naming any names..."
            camilo "Oh, I get you."
            camilo "I guess there'll always be one or two in every group."
        "We don't really know them yet":
            s3_mc "I know we had that challenge yesterday with all the embarrassing secrets, but that doesn't mean you actually know somebody."
            s3_mc "I think it's too early to say if we're going to get on with everyone here."
            camilo "Yeah, you're probably right."

    camilo "I just want us all to be friends, you know?"
    camilo "I'm used to having lots of people around me that I care about. My family, all my mates, my regulars to the shop."
    camilo "What's the saying? No one is the Isle of Man?"
    s3_mc "I think you mean 'no man is an island.'"
    camilo "Yeah, that's the one."
    camilo "What about you? What's your social life like, normally?"

    # CHOICE
    menu: 
        s3_mc "Back home..."
        "I have loads of friends":
            s3_mc "I've got a pretty wide social circle, so I'm used to hanging out in a big group like we do at the Villa."
            s3_mc "I'm totally in my element here."
            camilo "It definitely shows!"
        "I just have a few close mates":
            s3_mc "My best friends are really important to me."
            s3_mc "I'd never think about replacing them."
            s3_mc "So it's a bit new to me, hanging out in a big group like we do at the Villa."
        "I'm more focused on my career":
            s3_mc "Work is the most important thing to me at the moment."
            camilo "Respect."

    camilo "It must be proper hard, trying to balance a social life with your career."

    # IF STATEMENT
    if s3_mc.job == "Model":
        # FILL IN
        "EMPTY - Job = Model"
    elif s3_mc.job == "Scientist":
        s3_mc "Yeah, sometimes working in a lab means keeping really odd hours."
    elif s3_mc.job == "Musician":
        # FILL IN
        "EMPTY - Job = Musician"
    elif s3_mc.job == "Athlete":
        s3_mc "Yeah, training for hours almost every day can make it a bit hard to go out sometimes."

    camilo "Well, you never know. Maybe you'll make some new friends while you're in the Villa."

    if s3_mc.current_partner == "Camilo":
        "He puts his hand on the table next to yours, as if he wants to take it but isn't sure if he should."
        camilo "Hey..."
        camilo "I'm really sorry about what happened last night."
        camilo "I know Iona wasn't trying to hurt anyone, but I wish she hadn't broken us up."
        camilo "You were the one I really wanted. You still are."

        # CHOICE
        menu:
            thought "Camilo would rather be with me than Iona..."
            "Well, yeah, I'm pretty great":
                s3_mc "Sexy, funny, smart. I'm the whole package."
                camilo "Yes, you are. Iona knows that as well as I do."
            "But she's so lovely":
                s3_mc "She's so pretty and cool!"
                camilo "Yeah..."
            "Does she know you feel that way?":
                camilo "Yeah, of course."
                camilo "We had a chat about it last night. I told her the truth."

        camilo "She's a great girl, and I'm not necessarily opposed to getting to know her better..."
        camilo "It's just that I never expected to be in this position, and now I don't know what to do."
        camilo "You were my first choice, at the end of the day."

    camilo "I saw you had a chat with [s3_mc.bff] last night, after what happened at the recoupling."
    
    # IF STATEMENT
    if s3_mc.bff == "Elladine":
        # FILL IN
        "EMPTY - BFF = Elladine"
    elif s3_mc.bff == "Genevieve":
        camilo "She seems like a real chill girl. I'm glad you two are hitting it off."
    elif s3_mc.bff == "Nicky":
        # FILL IN
        "EMPTY - BFF = Nicky"
    elif s3_mc.bff == "Seb":
        camilo "That was a real relief to me, to be honest. He definitely needs a friend in here."

    "He takes a sip of champagne and smiles."
    camilo "And obviously I hope you and me are gonna be close, too."

    # CHOICE
    menu:
        thought "Camilo hopes we're going to be 'close'..."
        "Yeah, we'll be friends":
            s3_mc "You're a good laugh."
            s3_mc "I can already tell we're going to have fun together."
            camilo "Right back at you."
        "Let's be more than friends":
            $ s3_mc.like("Camilo")
            $ s3_like_camilo = True
            $ s3_lis.append("Camilo")
            s3_mc "I think we've got potential, don't you?"
            camilo "I was kind of hoping you'd say that."
        "Slow down there, buddy":
            $ s3_mc.dislike("Camilo")
            $ s3e2p2_reject_camilo = True
            s3_mc "Let's not get ahead of ourselves."
            camilo "Oh. I mean yeah, of course."
            "He leans back in his chair, putting some distance between you."
            camilo "It's just..."
    
    if s3e1p1_cheeky_snog and s3_mc.current_partner == "Camilo":
        camilo "When we had that kiss."
    elif s3_mc.current_partner == "Camilo":
        camilo "When you first walked out of the Villa..."
    else:
        camilo "Yesterday, on the lawn..."    
    
    camilo "I dunno, it felt kinda special."
    camilo "Like the rest of the world stopped mattering for a second."
    "He sighs and looks down at the table."
    camilo "But that's not the world we live in."
    camilo "We've got a whole Villa full of people to take into account."
    camilo "Speaking of which, I think our time's just about up."
    "He drains his glass, then reluctantly gets to his feet."

    if s3e2p2_first_date == "Camilo" or s3e2p2_second_date == "Camilo":
        camilo "This has been really nice, [s3_name]."
        camilo "I'll see you later, yeah?"
        s3_mc "See you later, Camilo."

    if s3e2p2_reject_camilo != True:
        if s3_mc.current_partner == "Camilo" or s3_like_camilo == True:
            "He shoots you a wink before he turns to leave."
        elif s3_like_camilo == False:
            "He smiles, but doesn't stop to say anything else before turning to leave."
    
    show camilo at npc_exit
    pause 0.3
    $ renpy.hide("camilo")

    return

label s3e2p2_harry_date:
    harry "So..."
    harry "You're a [s3_mc.job], right?"
    harry "That's pretty sick."

    # CHOICE
    menu:
        thought "Harry thinks my job is cool..."
        "That's right, it's very cool":
            s3_mc "It's my dream job."
            s3_mc "I'm really lucky that I get paid to do something I love."
            harry "That's the best. I'm really happy for you."
        "It's not all it's cracked up to be":
            s3_mc "Everyone says that, but really, it's just a job."
            harry "Yeah?"
            s3_mc "Yeah. It's not, like, my life purpose or anything."
            harry "I guess that makes sense."
        "You're just saying that":
            s3_mc "It's fine, you don't need to flatter me."
            harry "No, I'm serious!"

    # IF STATEMENT
    if s3_mc.job == "Model":
        harry "I went through a phase of wanting to do modelling, actually."
        harry "I think I just liked the idea of getting to wear lots of nice suits and standing around looking suave and serious."
        harry "But I know there's a lot more to it than that, obviously."
        harry "And I probably don't have enough patience to stand still for that long."
    elif s3_mc.job == "Scientist":
        harry "When I was at school, I briefly thought I was going to become a scientist someday."
        harry "You know, discover something that would really make a difference to the world. Go down in history."
        harry "But the only problem was..."
        harry "I wasn't very good at science."
    elif s3_mc.job == "Musician":
        harry "Every kid kinda dreams of growing up to be a rockstar, right?"
        harry "I know I did, anyway."
        harry "But my parents wouldn't let me take guitar lessons. They made me do piano and violin instead."
        harry "I tried to teach myself the guitar later, but I wasn't very good at it."
    elif s3_mc.job == "Athlete":
        harry "I liked playing football when I was younger. All kinds of sports, but mainly football."
        harry "I was pretty good at it, for a while."
        harry "But by the time I got a bit older, I realised I wasn't as good as the other lads anymore."
        harry "So I quit."

    "He sighs."
    harry "There's been loads of things like that in my life."
    harry "I'm always picking up new ideas and then putting them down again when they don't work out."
    harry "But that's alright! I'll hit on the right thing eventually."
    harry "I'm destined for great things, I know it."
    harry "I'm not sure what, exactly. But something great."

    # CHOICE
    menu:
        thought "Harry thinks he's destined for great things..."
        "I'm sure you're right":
            $ s3_mc.like("Harry")
            s3_mc "I can tell you've got the spirit."
            s3_mc "And look, you're already Island Amore!"
            s3_mc "You're definitely heading for the stars."
            harry "Exactly."
        "Only if you work for it":
            $ s3_mc.like("Harry")
            s3_mc "I like that you're ambitious, but ambition won't get you anywhere by itself."
            s3_mc "You've got to actually know what it is you want."
            s3_mc "And you've got to stick at it, not give up when it doesn't immediately go your way."
            s3_mc "If you focus all that energy, you'll be able to do something amazing."
            harry "Ah, you're right. I know you're right."
            harry "I swear I'm working on it. I don't want to spend the rest of my life just bouncing from one thing to the next."
        "Be realistic, dude":
            $ s3_mc.dislike("Harry")
            s3_mc "Look, you're never going to achieve anything if you don't have the drive to keep working at it."
            s3_mc "You don't even know what it is you want to do!"
            s3_mc "Why not just chill out and accept that it might not happen."
            harry "I've heard that one before."

    s3_mc "So..."
    s3_mc "How did you end up on Island Amore?"
    harry "Oh, I don't just dream big with my career goals."
    harry "I also want my big romance to be the biggest and best it can be."
    harry "So it just made sense to come and try to meet someone here."
    s3_mc "Not just to try and win the game?"
    harry "Well, I want to win. Of course I want to win."
    harry "I love winning."
    harry "But I'm not here to play the game."
    harry "You could couple up with someone you don't really like, and win the fifty grand... but where's that got you?"
    s3_mc "It's got you a bunch of money..."
    harry "Yeah, but wouldn't have anyone to really celebrate with."
    harry "I want to leave here with a girl who leaves an impression on the world, you know?"
    "He glances shyly up at you, then back down at his champagne glass."
    harry "How about you? What are you looking for in here?"

    # CHOICE
    menu:
        s3_mc "I'm here looking for..."
        "My soulmate":
            s3_mc "You know, my future husband."
            harry "Wow. Yes. I'm glad you've set your sights high."
            harry "Don't you leave here until you've found the one for you, alright?"
            s3_mc "I'll do my best."
        "A summer fling":
            s3_mc "I don't need anything super serious. "
            s3_mc "I just want someone I can have a great time with in the moment."
            harry "Fair enough. No harm in that."
        "I guess we'll see":
            s3_mc "If I meet someone I can settle down and spend my whole life with, great."
            s3_mc "But I'm not going to force it."
            s3_mc "Maybe I just meet someone who makes me happy in the short term, and that's cool too."
            harry "Go with the flow, huh? Good for you."
            harry "I don't think I've ever been that relaxed about anything."
            harry "Sometimes I wish I was."

    # IF STATEMENT
    if s3_mc.current_partner == "Harry":
        "He puts his hand on the table next to yours, as if he wants to take it but isn't sure if he should."
        harry "Hey..."
        harry "I'm really sorry about what happened last night."
        harry "I know Genevieve wasn't trying to hurt anyone, but I wish she hadn't broken us up."
        harry "You were the one I really wanted. You still are."

        # CHOICE
        menu:
            thought "Harry would rather be with me than Genevieve..."
            "Well, yeah, I'm pretty great":
                s3_mc "Sexy, funny, smart. I'm the whole package."
                harry "Yes, you are. Harry knows that as well as I do."
            "But she's so lovely":
                s3_mc "She's so pretty and cool!"
                harry "Yeah..."
            "Does she know you feel that way?":
                harry "Yeah, of course."
                harry "We had a chat about it last night. I told her the truth."

        harry "She's a great girl, and I'm not necessarily opposed to getting to know her better..."
        harry "It's just that I never expected to be in this position, and now I don't know what to do."
        harry "You were my first choice, at the end of the day."

    harry "Maybe this is a bit of a weird question..."

    if s3e1p1_cheeky_snog and s3_mc.current_partner == "Harry":
        harry "Especially after that kiss. (if you were coupled and chose the gem option to kiss him)"
        "He blushes at that memory."

    harry "But do you think you've already met the person since you got here?"
    harry "Or are you still waiting for them to show up?"

    # CHOICE
    menu:
        thought "Have I already found the person I'm looking for?"
        "Yeah, maybe...":
            s3_mc "It's early days, but I'm definitely aware of my options."
            harry "Oh!"
            "He looks hopeful, but uncertain."
            harry "Well, that's good. I suppose."
            harry "For you, I mean."
        "I'm looking at him":
            $ s3_mc.like("Harry")
            $ s3_like_harry = True
            $ s3_lis.append("Harry")
            s3_mc "I've got everything I want right here."
            "He chokes on his champagne."
            harry "I..."
            harry "I was hoping you'd say something like that, I didn't think about what to do if you actually said it."
            harry "Well, you just made my day."
        "No, not yet":
            $ s3_mc.dislike("Harry")
            $ s3e2p2_reject_harry = True
            "He looks a little downcast, but nods."
            harry "Fair. It's still early days, after all."
            harry "Even if you don't like anyone yet, there'll be more lads joining soon, I'm sure."

    "He looks down at his empty glass."
    harry "Well, this has been great."
    harry "But I think it's time to head back."

    if s3e2p2_first_date == "Harry" or s3e2p2_second_date == "Harry":
        s3_mc "I'll see you back in there in a bit, then."
        harry "Yep! Thanks for this, [s3_name]. It's been a real treat."
    
    "He gives you a hug goodbye."

    if s3e2p2_reject_harry:
        "Then he waves as he sets off down the beach."
    else:
        "His hands, warm and gentle, linger on your arms as he lets go."

    show harry at npc_exit
    pause 0.3
    $ renpy.hide("harry")

    return

#########################################################################
## Episode 2, Part 3
#########################################################################
label s3e2p3:
    scene sand with dissolve
    $ on_screen = []

    show screen day_title(2, 3) with Pause(4)
    hide screen day_title with dissolve

    "Welcome back..."
    "To the island of love most commonly referred to as..."
    "Island Amore!"
    "That would have been more effective if I'd done a drum roll."
    "I'm sure they'll edit one if for the replay."
    "Previously, our islanders got to know each other better during some romantic dates..."

    show elladine at npc_center
    elladine "Yeah, it was really romantic!"
    show elladine at npc_exit
    pause 0.3
    $ renpy.hide("elladine")

    "Thanks, Elladine."
    "But after three dates with nothing but champagne, everyone's a little peckish!"
    "...and probably a bit tipsy."
    "Never fear! The boys are ready to cook up a storm."

    show camilo at npc_center
    camilo "Perfection takes time, you know?"
    show camilo at npc_exit
    pause 0.3
    $ renpy.hide("camilo")

    "Looking tasty, Camilo."
    "And the food's good, too..."

    scene s3-dressing-room with dissolve
    $ on_screen = []

    "You and the other girls are getting ready for dinner."
    elladine "I wonder what they're cooking up for us?"
    iona "I'm hoping for something simple like bangers and mash."
    iona "Don't get me wrong, I wouldn't mind something posher..."
    iona "But I'm not sure that I trust those boys in the kitchen, y'know?"
    elladine "True..."
    miki "Bill told me that there's only three seasonings you ever need to use..."
    miki "Salt, pepper, and curry powder..."
    miki "I couldn't believe it!"
    aj "Seb thinks you can cook everything in a saucepan. Even when he wants to fry something."
    elladine "Great, now I'm actually scared..."
    elladine "How do you think the boys' cooking is going to be, [s3_name]?"

    # CHOICE
    menu:
        thought "I think the boys' cooking is going to be..."
        "Just wok I need":
            pass
        "A bit half-baked":
            pass
        "A recipe for disaster":
            pass

    "The girls roll their eyes, except for Miki and Iona who burst into laughter."
    miki "I love puns."
    miki "People say they're not funny, but like, why am I laughing?"
    elladine "Because you both have a terrible sense of humour?"
    "Miki pauses for a moment."
    miki "I don't think it's that."
    aj "It's definitely that, mate."
    "Genevieve grins."
    genevieve "To be fair, I bet not all of you can cook, either."
    aj "True, I once burned a poached egg."
    iona "That's pretty normal, babe."
    aj "No, I mean, burned it. Like, charred to a crisp."
    iona "...How'd you manage that?"
    aj "I have no idea!"

    # CHOICE
    menu:
        thought "AJ burned a poached egg to a crisp somehow..."
        "I'm rubbish in the kitchen, too":
            $ s3_mc.like("AJ")
            s3_mc "Like, I've never even been able to make toast right."
            miki "But you just put it in the toaster and it comes out done?"
            s3_mc "You'd think that, but that's not what happens with me."
            aj "Thanks, babe. That makes me feel better."
        "That seems kinda impossible":
            aj "You'd think that, but it totally happened."
            aj "The local paper ran a story about it and everything."
            elladine "Was it a slow news day?"
            aj "You have no idea how bad it was."
            miki "What?"
            elladine "AJ, hun, we're going to have to come back to this at some other point."
        "I'd love to see that...":
            aj "Nooo. It was so embarrassing."
            aj "Besides, I don't know how I did it."

    "The smell of food wafts up to the dressing room and you feel your stomach rumble."
    thought "I hope that means dinner is nearly ready."
    thought "Whatever it is."
    miki "Ooh, my stomach's growling too. That smells incredible."
    elladine "I'm suddenly super hungry."
    miki "Come on then, let's go see what they've made."

    ## Add back in once MC images are added and has clothes to change into
    # elladine "[s3_name] isn't even dressed yet, though."
    # "Miki grins at you and rolls her eyes."
    # miki "Babe, come on."
    # thought "Hmm, time to make myself fabulous."

    # MC outfit change to evening wear
    # Change all NPCs to evening wear

    # thought "Woah, who's that gorgeous woman staring at me?"
    # thought "Oh, it's my reflection."
    # "You wink at yourself."
    # genevieve "I'd never pull that look off so well, [s3_name]."
    # s3_mc "Thanks babe!"
    # thought "It's a chill evening tonight. No need to play all my cards at once."
    # genevieve "Ooh, [s3_name]. I never got to say before how much I love that on you."
    # s3_mc "Thanks babe!"
    # thought "Or I'll just stick with this..."
    # genevieve "Not gonna put an effort in for the boys, [s3_name]? They are making us dinner."
    # s3_mc "Let's see how good the dinner is first..."
    # genevieve "Good point! I should probably rein in my expectations a bit, huh?"

    iona "What are we waiting for? Let's get down there!"

    scene s3-kitchen-night with dissolve
    $ on_screen = []

    "You enter the kitchen. The walls are splattered with strings of spaghetti, the odd mushroom, and various sauces."
    "The sink is overflowing with dirty dishes and discarded cooking utensils."
    "Pans clatter, cutlery falls on the floor, and over the din the boys' voices cut through with the odd curse."
    "The only boy who seems calm and quiet is Camilo."
    s3_mc "Hey boys!"
    harry "Hey girls!"
    bill "Agh! Harry, you knocked my mushroom onto the floor!"
    harry "Why was it so close to the edge?"
    "Bill sighs as he rinses the mushroom off."
    bill "It was the centrepiece of the dish."
    camilo "A mushroom was the centrepiece?"
    bill "When the dish is called 'Mushroom Surprise', of course it's at the centre."
    nicky "Wouldn't it be hidden? You know, it being a surprise and all?"
    bill "That's the surprise."
    harry "I'm confused..."

    # CHOICE
    menu:
        s3_mc "In a dish called 'Mushroom Surprise' the mushroom should be..."
        "On the top and centre":
            $ s3_mc.like("Bill")
            bill "See! Glad someone gets it."
            nicky "You and [s3_name] are the only ones..."
        "Hidden in the middle":
            $ s3_mc.like("Nicky")
            nicky "[s3_name] gets where I'm coming from."
            bill "But it's hardly a surprise if mushroom is in the title..."
        "In another dish entirely...":
            $ s3_mc.like("Nicky")
            s3_mc "That's the real surprise!"
            nicky "So no mushroom at all?"
            bill "I can't actually argue with that..."

    "Iona stumbles slightly as her shoe gets caught on the floor."
    iona "Eww."
    iona "The floor is stickier than my local pub on a bank holiday weekend."
    "You look around."
    thought "This kitchen is a disaster and the boys seem to be struggling."

    # CHOICE
    menu:
        thought "What should I say?"
        "The food smells amazing, guys!":
            $ s3_mc.like("Bill")
            $ s3_mc.like("Harry")
            harry "With this many pro chefs getting our cook on? Of course it does."
            nicky "Bill's here too."
            bill "Oi!"
            nicky "Just joshing you, Mushroom man."
            bill "Not my nickname."
            nicky "You know I love you really."
        "Who's cleaning this mess?":
            harry "Those who cook don't clean. That's the rule we have in my house."
            s3_mc "So you do all the cleaning?"
            harry "Nah, I'm the oldest. My sisters and brother do the cleaning."
            s3_mc "So what do you do?"
            harry "Supervise, don't I?"
            elladine "I'm not cleaning this mess."
            miki "Yeah, where would we even start?"
            iona "Maybe a firehose and just put it on full blast..."
            nicky "How about we enjoy the food first, yeah? Then we'll work out who's doing the cleaning."
        "Do you boys need a hand?":
            $ s3_mc.like("Bill")
            $ s3_mc.like("Harry")
            bill "Does it look like we do? "
            iona "Yes."
            s3_mc "Kinda, yeah..."
            "The other girls nod in agreement."
            harry "That's a kind offer, but we've got this."
            "He steps back to his counter."

    "There's a squelching sound."
    harry "What the...?"
    bill "Did you just step on my tomato?"
    harry "Why was it on the floor?"
    bill "It's round! It rolled off the counter..."
    "Bill's standing over a tower of grated cheese."
    "He's still grating."

    # CHOICE
    menu:
        thought "Bill's grating loads of cheese..."
        "It's a good thing I love cheese":
            bill "Gotta have cheese with your pasta."
            elladine "But I'd also like some pasta with my cheese."
        "That's a lot of cheese, Bill":
            bill "Gotta have cheese with your pasta."
            elladine "But I'd also like some pasta with my cheese."
        "Can I have some pasta with my cheese?":
            elladine "That's exactly what I was thinking..."
            bill "Cheese is the best part about any pasta dish."

    "You see Seb standing over a small bag of onions. He pokes at them tentatively, as if they might bite him."
    seb "I'm so out of my element, man..."
    genevieve "Did you check the pasta before draining it, Harry?"
    "Harry pulls the colander out of the sink, steam rises off of it."
    harry "What? Nah, it's been long enough."
    genevieve "Are you sure? It looks a bit stiff..."
    harry "It's good, love. See?"
    "He takes a piece of rigid pasta out of the colander and crunches down on it."
    "His face twists and he spits it out into the bin."
    harry "Um..."
    "He fills up a new pan with fresh water."
    genevieve "Don't forget the salt."
    nicky "Alright, speaking of salt, there's enough flying around from you girls."
    nicky "Go on, take your bants elsewhere and let us get on with the grub."
    miki "But I'm fascinated by your process!"
    iona "Or lack of..."
    nicky "Out!"

    scene s3-lawn-night with dissolve
    $ on_screen = []

    "You all walk away giggling."
    elladine "So..."
    elladine "The food looked interesting."

    # CHOICE
    menu:
        thought "How are the boys doing in the kitchen?"
        "It smelled so good....":
            s3_mc "How did it look so bad?"
            genevieve "I swear something on a plate just winked at me..."
        "How did they make such a mess?":
            elladine "Right? I'm the sort of person that has to clean as they cook."
            elladine "Can't stand a messy kitchen."
        "There was no space to sit on a counter":
            genevieve "Why would you want to sit on a counter?"
            iona "I can think of a few reasons..."
            s3_mc "Iona gets me."
            "The others laugh."

    miki "I'll be honest, it was kind of hot to see them all sweating in there."
    iona "True, despite the disaster, they seemed to actually be taking it seriously."
    s3_mc "But they were just really bad at it."
    iona "So who caught your eye, Miki?"
    miki "Maybe Nicky? He seemed so in control."
    elladine "Can't argue with that."
    genevieve "I thought Seb was adorable. He looked so lost and out of place."
    s3_mc "Why was he poking the onions?"
    "The others shrug."
    iona "Seeing as we're talking about the guys..."
    iona "How's everyone feeling about their couples?"
    "There's a pause. Then Miki sighs."
    miki "Bill's a bit odd, to be honest. He keeps telling me these strange theories he has."
    elladine "You and the rest of us..."

    # CHOICE
    menu:
        thought "Miki thinks Bill is a bit odd..."
        "I actually don't mind his bants":
            s3_mc "At least, I think it's bants."
        "How does a guy have so many opinions?":
            s3_mc "It's like, we get it, you like things a certain way. Good for you?"
            iona "Thank you! He really reminds me of my granddad at times."
            iona "Just always had to say something."
        "He's well fit, though":
            s3_mc "His eyes are amazing, and that body..."
            iona "So, you're more of a looks over chat kinda gal, eh?"
            iona "I can respect that."
        "I don't have an opinion on him":
            "The others laugh."
            miki "I wonder how he'd feel about that?"
            iona "I'm sure he'd have plenty of thoughts about it..."

    genevieve "It's not the worst thing for someone to have opinions."
    genevieve "Even if he does have a lot of them..."

    "Iona smirks."
    iona "Camilo's obviously a bit of alright, but we haven't talked much."

    # CHOICE
    menu:
        "Iona says she's attracted to Camilo. How do I feel about him?"
        "Was his face sculpted or something?":
            s3_mc "It's like, unnaturally perfect..."
            s3_mc "Some people are just so lucky."
            iona "Yourself included! You're all kinds of fit."
            iona "You and Camilo would have such gorgeous babies..."
        "Am I the only one that thinks he's average?":
            "The other girls turn to look at you."
            elladine "Yeah."
            genevieve "Yep."
            aj "Sooo fit."
            iona "Seems like you are, babes."
        "The things I'd do to him...":
            s3_mc "Like, I just wouldn't be able to control myself. We'd be at it non-stop."
            s3_mc "And then we'd really spice things up when I get out of the..."
            "You stop yourself."
            s3_mc "Oh, sorry. I got carried a little away."
            iona "Don't stop! It was just getting good."
        "He seems sweet, but isn't my type":
            iona "That's fair. I want to get to know him better, but not sure how to really?"
            s3_mc "Talk to him?"
            iona "I try, but end up just staring at his face..."

    "Genevieve laughs."
    genevieve "I picked Harry because he's honestly one of the cutest boys here, but he's a bit immature."

    # CHOICE
    menu:
        thought "How do I feel about Harry?"
        "He's got a lot of confidence":
            s3_mc "I like a man who knows what he wants from life."
            genevieve "That's true. It's a rare quality."
            elladine "Does he though? He told me a bunch of different business ideas."
            iona "I call that being innovative."
        "I think he's a bit of a try-hard":
            s3_mc "I get the feeling he's always trying to impress."
            genevieve "That's just it. When I like a guy, it's because I find him interesting. His achievements are a bonus."
            elladine "I'm not like that at all. I like a man who knows what he wants and goes for it."
            iona "Yeah, some of the fellas I know want a pat on the back for putting their shirt on in the morning."
        "I want to nibble on those cute ears...":
            s3_mc "And then slowly work my way down to that toned chest."
            s3_mc "And just keep going lower and lower..."
            iona "And then start spanking."
            s3_mc "Not exactly where I was going with that, but yeah, sure."
        "He seems nice, but I'm not interested":
            iona "That's fine. Just means more cuties for us."
            s3_mc "That's if Genevieve will share him."
            genevieve "Hey, I've already said I'm not one-hundred-percent sold either."

    "Just then, Camilo's voice breaks through your chat."
    camilo "Grub's up, ladies!"
    miki "Great! I'm starving."
    iona "Same. I just hope they've made something edible..."
    "The six of you make your way over to the dining table."
    "The boys 'feast' is set out in front of you."
    "You look around. One of the boys is missing."
    s3_mc "Where's Camilo?"
    nicky "He's just finishing up in the kitchen."
    bill "Seems to think he's some kind of master chef or something."
    seb "To be fair, his food looked immense."
    harry "And ours doesn't?"
    nicky "Settle down, lads. Let the girls decide that, yeah?"

    $ done = False
    while not done:
        # CHOICE
        menu:
            thought "Let's see what's on offer..."
            "A bowl of... something?" if 'Soup' not in s3e2p3_food_seen:
                $ s3e2p3_food_seen.append("Soup")
                "The thick sludge is the same shade of brown you get after mixing a bunch of different paints together."
                "It smells earthy, almost like a garden centre."
                iona "Well, this is..."
                iona "...interesting."
                s3_mc "What is it?"
                nicky "It's soup!"
                elladine "How did you make it?"
                nicky "OK, I'm going to be the first to admit that I don't know how to make soup."
                nicky "So I guess-timated."
                nicky "I gathered a bunch of veg that was lying around, blended them with water and herbs, then heated it up."
                s3_mc "Which herbs?"
                nicky "The green ones."
                miki "This is amazing."
                nicky "Thanks!"
                miki "It's like we're seeing how Nicky's mind works!"
                nicky "Huh?"
            "A plate of mushy pasta" if 'Pasta' not in s3e2p3_food_seen:
                $ s3e2p3_food_seen.append("Pasta")
                "At least, you think it's pasta."
                "There's so much grated cheese covering it, it's hard to tell where the cheese ends and the pasta begins."
                aj "This looks great!"
                bill "It does?"
                aj "Yeah! I love cheesy pasta."
                bill "It was meant to be spag-bol, but someone kept stepping on my ingredients."
                "He glares at Harry."
                harry "Mate! I'll ask again, why was the mince on the floor?!"
                "You see AJ take a spoonful of the spaghetti, but it gets lodged in the starchy mass."
                aj "Oh..."
                genevieve "Harry, how long did you leave the pasta to simmer?"
                harry "Well, after realising it wasn't done, I left it on for another twenty minutes."
                harry "Y'know, blitz it to be safe, right?"
            "A questionable fruit salad" if 'Fruit Salad' not in s3e2p3_food_seen:
                $ s3e2p3_food_seen.append("Fruit Salad")
                "The blow is filled with watermelon slices. Each one is cut to different shapes and sizes."
                elladine "How's this a fruit salad? It's just watermelon."
                bill "Look closer..."
                "You peer closer at the collection of red, green, and black, then spot them."
                s3_mc "Are those...tomatoes?"
                bill "Bingo!"
                iona "Why?"
                bill "Because cutting up that bloody watermelon took so long, we only had time to chuck in a handful of other fruits."
                harry "The tomatoes were just sat there..."
                bill "And, you know, they're fruits and all."
                elladine "Don't think I'D have made that connection."
                bill "Why not? Both are red. I have this theory..."
                iona "Here we go..."
                bill "...that if you combine food of the same colour, it can't taste bad."
                bill "So, like, with a salad, if you only use green veg, it works. Just try and show me otherwise."
                "Iona points to the bowl of fruit."
                iona "Like, right there..."
            "That's enough food for now..." if len(s3e2p3_food_seen) > 0:
                $ done = True
                pass

    aj "Where's yours, Seb?"
    "He points to the chopping board with a single onion lying on it."
    aj "Oh, at least you tried..."
    seb "Nah, I didn't."
    nicky "Come on, girls! Dig in."
    "All the girls go quiet. The only noise any of them make is AJ's stomach as it rumbles."

    # CHOICE
    menu:
        thought "Oh boy. What should I start with?"
        "Slurp the herb soup":
            "You take a hold of the ladle and start to pull it up. There's a squelching sound as it breaks free of the 'soup'."
            thought "Oh no..."
        "Try some of the pasta gloop":
            "You stick a spoon into the cheesy pasta. When you try to pull it out it sticks fast."
            thought "It's like glue!"
        "Go safe and pick the fruit":
            "Going with what you think is the safest option, you pick up a slice of watermelon."
            "Half a tomato slides off its surface."
            thought "Maybe not..."

    miki "I don't get it. What smelled so good?"
    nicky "What do you mean?"
    "She gestures at the food."
    "Just then, you all turn to see Camilo holding a tray."
    camilo "Sorry for the wait! Perfection takes time, you know?"
    "He sets the tray down. You see everyone's eyes go wide at the sight of what looks like pastries."
    harry "You made Cornish pasties?"
    camilo "They're empanadas actually."
    camilo "Like a pasty, but filled with a very different spice mix."
    elladine "They look amazing!"
    camilo "Thanks! It's a family recipe. I've made three types. Meat, veggie with cheese, and vegan."
    aj "Hand over one, quick!"
    camilo "Help yourselves."
    
    $ food = s3_mc.diet.lower()
    s3_mc "I'll take a [food] one."

    if s3_mc.diet == "Meat":
        "Your mouth waters uncontrollably. You bite down. The meat is tender and packed with flavour."

    s3_mc "They're... incredible!"
    aj "This is better than sex."
    iona "Hell, this is sex. Like, in my mouth."
    genevieve "You realise how that sounds?"
    iona "I know exactly how that sounds."
    bill "Oh, come off it. No way are they that good."
    "The other boys grumble. Bill puts a spoonful of his pasta into his mouth."
    "He chews it slowly, then puts the spoon down."
    iona "What's this? A speechless Bill?"
    nicky "I think the pasta's glued his mouth shut."
    "Bill swallows hard, wincing slightly, then grabs an empanada and tentatively tastes it."
    "His eyes go wide and he hungrily takes another few quick bites."
    bill "They're alright, I'spose."
    "You continue to tuck in."

    # CHOICE
    menu:
        thought "Camilo's food is amazing...."
        "Don't feel bad, boys, you tried":
            harry "Oh, no. The 'don't feel bad' line."
            harry "We really messed up, lads."
            bill "Speak for yourself."
        "Can Camilo cook every night?":
            $ s3_mc.like("Iona")
            iona "Yes!"
            "She turns to him, a pleading look on her face."
            iona "Pleeease!"
            camilo "If I'd known they'd be this popular, I'd have made more. I'll make arepas next time."
        "I love a man that can cook...":
            $ s3_mc.like("Camilo")
            camilo "Oh, yeah? You know, this is just a tasty snack right."
            s3_mc "You're a tasty snack."
            camilo "Touché."
            iona "I thought the food was meant to be hot, not the conversation..."

    camilo "Oh, I almost forgot!"
    "He quickly heads back into the kitchen."
    "You hear him rummage around for a moment, before emerging carrying a tray filled with cake and brightly coloured ice cream."
    harry "Woah! Where'd you make that?"
    camilo "I didn't. They were in the freezer."
    camilo "I guess they were put there as a treat for us."
    seb "The freezer... of course. I should have looked in there from the start."
    iona "What kind of cake is it?"
    camilo "Let's find out!"
    "He slices into the cake, producing a neat, multi-coloured slice."
    s3_mc "It's a rainbow cake!"
    bill "What's rainbow taste like?"
    aj "Happiness!"
    camilo "Alright, I'm just going to set this down over here. Everyone has to eat their hot food first."
    harry "Aww..."
    iona "That means eating Camilo's food."
    harry "Ooh!"
    "You all dig in."
    nicky "Man, this grub's so good. It reminds me of a date I had at this Brazilian barbeque place."
    nicky "They just kept piling meat on our plates. At one point, I couldn't see my date's face through the meat tower!"
    bill "Sounds class."
    nicky "It was at first, but I didn't really think it through."
    nicky "By the end of the meal, we could hardly move."
    nicky "Kinda goes without saying neither of us exactly felt sexy after eating that much."
    seb "That's not that bad a date."
    s3_mc "Go on Seb, what is a bad date?"
    "Seb grunts, then laughs."
    seb "So, I once dated this girl. Ashley or something."
    seb "I can't remember her name, which is fitting seeing as she never remembered mine."
    genevieve "Ouch, what do you mean?"
    seb "The entire time we were seeing each other, she called me Mark."
    seb "It got past the point where I could correct her."
    nicky "So what'd you do, man?"
    seb "The only thing I could. I dumped her."
    seb "It was either face the discomfort of dumping her, or telling her that my name was actually Seb after three months of dating..."
    seb "I know which one I preferred. "

    # CHOICE
    menu:
        thought "Seb dumped a girl because she kept him calling Mark..."
        "I'd do the same thing":
            $ s3_mc.like("Seb")
            s3_mc "Nothing worse than having the, 'I've forgotten your name..' conversation."
            seb "Yeah. Somehow dumping someone is just easier."
            seb "What's that say about us, [s3_name]?"
            s3_mc "People better get our names right!"
            "He smiles at you."
        "Isn't that a bit shallow?":
            $ s3_mc.dislike("Seb")
            s3_mc "It's not her fault she couldn't remember. Maybe you just look more like a Mark."
            seb "But I'm not good at awkward conversations..."
        "Wait, your name isn't Mark?":
            seb "No."
            nicky "Woah! Good thing you cleared that up."
            s3_mc "I just thought Seb was a nickname. Like, short for Mark, you know?"
            seb "Ha-ha. Very funny. Knock it off."
            nicky "Sure thing..."
            nicky "...Mark"
            "Seb grumbles, but he can't help and grin at you and Nicky."

    aj "Want to hear something even more awkward than that?"
    nicky "Always."
    aj "This one time, I was meant to meet this girl at a posh restaurant in the middle of town."
    aj "I dressed up all fancy and everything for this date."
    aj "But she stood me up!"
    harry "What?"
    harry "Her loss."
    aj "Wait, it gets better."
    aj "So as I was all ready for a night out, I thought, sod it, and went with a few of my girlies."
    aj "I met a guy there and ended up going back to his flat. Turns out he lived with his sister..."
    aj "...who was the girl that stood me up!"
    miki "No way!"
    iona "AJ's the player."
    elladine "What did you do, hun?"
    aj "To say it was a mood killer is an understatement."
    aj "But, we actually laughed it off and watched some cheesy horror films."
    genevieve "That's so sweet."

    # CHOICE
    menu:
        thought "AJ got off with the brother of a girl who stood her up..."
        "I admire that so much":
            $ s3_mc.like("AJ")
            aj "Thanks, babes. It wasn't on purpose, though!"
        "You seem so chill about it":
            aj "I don't think it helps anyone to get angry over these things. It's not like we knew each other that well."
            aj "It was just an inconvenience with a happy ending..."
        "Why'd she stand you up?" if s3_like_aj == False:
            aj "You know, I didn't think to ask her."
            aj "It really doesn't matter!"
        "I'd never stand you up..." if s3_like_aj == True:
            $ s3_mc.like("AJ")
            aj "Good to know..."

    seb "Alright, I want to hear one of [s3_name]'s stories. She must have a few."
    s3_mc "Wow, thanks!"

    # CHOICE
    menu:
        thought "Do I have an embarrassing dating story?"
        "I once went home with someone else":
            camilo "What?"
            s3_mc "Yeah, we went for a meal. The guy was decent enough."
            s3_mc "But our waiter was an old fling of mine!"
            aj "The world is so tiny sometimes."
            elladine "So what happened?"
            s3_mc "Well, it became clear that me and the waiter still had the hots for each other."
            s3_mc "His little apron was so tight around his waist..."
            iona "I'm really learning a lot about you from this story, hun."
            s3_mc "So I said goodnight to my 'date'."
            s3_mc "Then waited for my fling to get off his shift, so we could go back to mine."
            s3_mc "I asked him to keep the apron on..."
        "I went out when I was sick and threw up on the date" if s3_like_aj == False:
            aj "That sounds like a nightmare!"
            s3_mc "Yeah, I had a cold, but this guy was super hot and only available that night."
            s3_mc "It was fine until he ordered oysters."
            elladine "Eww..."
            camilo "They're minging."
            s3_mc "I started feeling grim again and he kept slurping them down really loudly..."
            s3_mc "And that was it. I threw up everywhere."
            s3_mc "Mostly on him."
            bill "Sexy."
        "I got a guy back for cheating":
            iona "What?"
            s3_mc "I went out on a date with this guy I met on an app."
            s3_mc "Things were going well and heads to the bathroom."
            s3_mc "Then his phone rings and the word 'wife' flashes up on the screen."
            elladine "Wait, he just had her down as 'wife' in his phone?"
            iona "Who does that?"
            s3_mc "This guy."
            miki "What did you do?"
            s3_mc "I took her number down, forwarded her the conversation I'd had with her husband, then left."
            iona "You badass."
        "I took a girl to a circus" if s3_like_aj == True:
            aj "That sounds fun!"
            s3_mc "It should have been, but..."
            s3_mc "...the clowns were really scary."
            "Everyone shudders."
            nicky "Clowns, man. I don't get them. Like, why do they exist?"
            aj "For everyone's amusement!"
            miki "And nightmares..."
            s3_mc "But I thought it was going well until the ringmaster asked for a volunteer and my date went up. They made her disappear."
            s3_mc "And that was that."
            iona "Huh?"
            s3_mc "Yeah, I didn't see her after that. She bailed, I guess."

    "You all continue chatting while you eat Camilo's amazing food."
    "Eventually, Harry gets up to clear the table."
    "He picks up the plate of spaghetti and goes to move past you."
    "As he does so, the chunk of it slides off, landing on your head."

    # CHOICE
    menu:
        thought "The spaghetti just fell on me!"
        "What the...":
            pass
        "Eww, get this off me!":
            pass
        "It tastes better than it looks":
            pass

    "There's a well of sauce in the middle of the spaghetti. The red liquid seeps down onto you."
    bill "The sauce surprise..."
    harry "Mate!"
    bill "Hey, don't look at me like that. You'd have all found it earlier if you'd actually eaten it!"
    s3_mc "Can we get back to the fact that I'm covered in cold sauce and spaghetti?"
    thought "No-one seems to be that bothered about this."

    # CHOICE
    menu:
        thought "Maybe I should show them I mean business..."
        "Start a food fight":
            $ s3e2p3_food_fight = True
            call s3e2p3_food_fight from _call_s3e2p3_food_fight
        "Just grumble instead...":
            "No-one seems to listen."
            thought "Hey, come on..."
            s3_mc "I need to go and get this gunk out of my hair and face."
            "Camilo looks at you."
            camilo "Yeah, you're covered in it."


    "Camilo looks at you."
    camilo "Wow, [s3_name], you're covered in gunk..."
    s3_mc "Yeah... I need to clean up."
    camilo "Want me to come with you?"

    # CHOICE
    menu:
        thought "Do I want to get some alone time with Camilo?"
        "That'd be great, thanks!":
            $ s3_mc.like("Camilo")
            $ s3e2p3_clean_off_with_cam = True
            call s3e2p3_clean_off_with_cam from _call_s3e2p3_clean_off_with_cam
        "Nah, I've got this":
            camilo "Cool, cool. Don't forget the bits of spaghetti at the back of your neck."

            scene s3-bathroom with dissolve
            $ on_screen = []

            "You enter the bathroom. Bits of spaghetti drop onto the floor."
            thought "I'm covered from head to toe..."


    thought "That hot shower is going to feel so good!"
    "You run the water until it steams, then jump in."

    scene s3-shower with dissolve
    $ on_screen = []

    "As you remove the remnants of pasta and watermelon, your thoughts drift off to your time in the Villa so far..."

    # CHOICE
    menu:
        thought "It's been two days, but my highlight so far has been..."
        "Coupling up with [s3_mc.current_partner]":
            thought "And I'm pretty sure I can get him back."
        "Becoming friends with [s3_mc.bff]":
            thought "We just get each other."
        "Going on the dates earlier...":
            thought "Nice to know I've got options..."
        "Getting to know AJ" if s3_like_aj == True:
            thought "And I can't wait to get to know her better."

    thought "And we're only at the start of it all."
    thought "I can't wait to see what else is in store..."
    "You turn the shower off and towel yourself dry."
    thought "But first, I should get changed."

    # MC outfit change to sleepwear, include once there are mc images
    # thought "This is still sexy, right?"
    # iona "Looking good, [s3_name]. As always"
    # s3_mc "You're cute, Iona."
    # iona "Not as cute as you look right now."

    scene s3-bedroom-night with dissolve
    $ on_screen = []

    "You sprawl out in the large, empty bed and take a final look around the room."

    if s3e2p3_clean_off_with_cam:
        "Camilo catches your gaze and winks in response."
        "A sly smile spreads across his face."

    if s3e2p3_food_fight:
        bill "Mate, my ear is well itchy."
        "Bill stands there, scratching at it."
        bill "What the...?"
        "He pulls a watermelon seed out of it."
        miki "Eww! Gross."
        bill "How'd I not notice that before?"
        "Everyone laughs as Bill flicks it away and settles into bed."

    thought "I can't believe I've got one of the fittest guys here interested in me.."
    thought "I better get some sleep."
    thought "Got another full day of grafting to do tomorrow..."

    scene sand with dissolve
    $ on_screen = []

    "Didn't their muss ever tell our Islanders not to play with their food?"
    "Judging by the state of the kitchen, clearly not..."
    "Coming up!"
    "AJ and Genevieve do a thing..."
    aj "I'm not sure about this."
    genevieve "Scared?"
    aj "No! I just don't want to hurt you."

    show aj at npc_exit
    show genevieve at npc_exit
    pause 0.3
    $ renpy.hide("aj")
    $ renpy.hide("genevieve")

    s3_mc "Maybe next time we chat it'll be a different kind of saucy."
    "Stay tuned."

    jump s3e3p1

    return

label s3e2p3_food_fight:
    "You grab a handful of the pasta out of your hair."

    # CHOICE
    menu:
        thought "Who should I throw this at?"
        "Bill":
            $ s3e2p3_first_victim = "Bill"
            "You turn to [s3e2p3_first_victim] and grin."
            bill "Mate, why are you staring at me like that?"
        "Harry":
            $ s3e2p3_first_victim = "Harry"
            "You turn to [s3e2p3_first_victim] and grin."
            harry "Mate, why are you staring at me like that?"
        "Camilo":
            $ s3e2p3_first_victim = "Camilo"
            "You turn to [s3e2p3_first_victim] and grin."
            camilo "Mate, why are you staring at me like that?"
        "Seb":
            $ s3e2p3_first_victim = "Seb"
            "You turn to [s3e2p3_first_victim] and grin."
            seb "Mate, why are you staring at me like that?"
        "Nicky":
            $ s3e2p3_first_victim = "Nicky"
            "You turn to [s3e2p3_first_victim] and grin."
            nicky "Mate, why are you staring at me like that?"
        "AJ":
            $ s3e2p3_first_victim = "AJ"
            "You turn to [s3e2p3_first_victim] and grin."
            aj "Um, babes? That grin is a little scary."

    "You launch the food from your hand."
    "It makes a satisfying plopping sound as it lands on [s3e2p3_first_victim]'s head."

    if s3e2p3_first_victim == "Bill":
        bill "Agh!"
        "Everyone else goes quiet. [s3e2p3_first_victim] pulls a string of spaghetti from his head, then turns to face you."
        bill "Oh, it's on, [s3_name]..."
        "He picks up a handful of watermelon and hurls it at you."
    elif s3e2p3_first_victim == "Camilo":
        camilo "Agh!"
        "Everyone else goes quiet. [s3e2p3_first_victim] pulls a string of spaghetti from his head, then turns to face you."
        camilo "Oh, it's on, [s3_name]..."
        "He picks up a handful of watermelon and hurls it at you."
    elif s3e2p3_first_victim == "Harry":
        harry "Agh!"
        "Everyone else goes quiet. [s3e2p3_first_victim] pulls a string of spaghetti from his head, then turns to face you."
        harry "Oh, it's on, [s3_name]..."
        "He picks up a handful of watermelon and hurls it at you."
    elif s3e2p3_first_victim == "Nicky":
        nicky "Agh!"
        "Everyone else goes quiet. [s3e2p3_first_victim] pulls a string of spaghetti from his head, then turns to face you."
        nicky "Oh, it's on, [s3_name]..."
        "He picks up a handful of watermelon and hurls it at you."
    elif s3e2p3_first_victim == "Seb":
        seb "Agh!"
        "Everyone else goes quiet. [s3e2p3_first_victim] pulls a string of spaghetti from his head, then turns to face you."
        seb "Oh, it's on, [s3_name]..."
        "He picks up a handful of watermelon and hurls it at you."
    elif s3e2p3_first_victim == "AJ":
        aj "Agh!"
        "Everyone else goes quiet. [s3e2p3_first_victim] pulls a string of spaghetti from her head, then turns to face you."
        aj "Oh, it's on, [s3_name]..."
        "She picks up a handful of watermelon and hurls it at you."

    "You manage to duck just in time..."

    if s3e2p3_first_victim == "Nicky":
        "The juicy mess splatters across Seb's face instead."
        seb "So it's like that, [s3e2p3_first_victim]?"
    else:
        "The juicy mess splatters across Nicky's face instead."
        nicky "So it's like that, [s3e2p3_first_victim]?"

    "He picks up an empanada, takes a bite, puts it back down, then throws some of Bill's pasta back at [s3e2p3_first_victim]."

    if s3e2p3_first_victim == "Bill":
        bill "Bloody hell, that packs a wallop!"
    elif s3e2p3_first_victim == "Camilo":
        camilo "Bill! How is your pasta so thick?"
    elif s3e2p3_first_victim == "Harry":
        harry "Bill! How is your pasta so thick?"
    elif s3e2p3_first_victim == "Nicky":
        nicky "Bill! How is your pasta so thick?"
    elif s3e2p3_first_victim == "Seb":
        seb "Bill! How is your pasta so thick?"
    elif s3e2p3_first_victim == "AJ":
        aj "Bill! How is your pasta so thick?"

    harry "It's like a brick!"
    "Before you know it, food is flying all over the place. Iona chucks a chunk of watermelon at Harry, who deflects it with his plate."
    "He then grabs a bottle of mustard and squeezes it hard, letting loose a torrent of the hot, yellow liquid."
    "Through the chaos [s3e2p3_first_victim] walks up to you."

    if s3e2p3_first_victim == "Bill":
        bill "Looks like you got me good."
        s3_mc "What can I say? I'm a cracking shot."
        if s3_mc.like_mc("Bill") >= 16:
            bill "Maybe later you can show me what else you're good at..."
            "He winks at you."
        bill "But there's something you're not very good at..."
        s3_mc "Oh?"
        bill "Paying attention!"
        "He points behind you."
    elif s3e2p3_first_victim == "Camilo":
        camilo "Looks like you got me good."
        s3_mc "What can I say? I'm a cracking shot."
        if s3_mc.like_mc("Camilo") >= 16:
            camilo "Maybe later you can show me what else you're good at..."
            "He winks at you."
        camilo "But there's something you're not very good at..."
        s3_mc "Oh?"
        camilo "Paying attention!"
        "He points behind you."
    elif s3e2p3_first_victim == "Harry":
        harry "Looks like you got me good."
        s3_mc "What can I say? I'm a cracking shot."
        if s3_mc.like_mc("Harry") >= 16:
            harry "Maybe later you can show me what else you're good at..."
            "He winks at you."
        harry "But there's something you're not very good at..."
        s3_mc "Oh?"
        harry "Paying attention!"
        "He points behind you."
    elif s3e2p3_first_victim == "Nicky":
        nicky "That was a banging shot, [s3_name]."
        s3_mc "What can I say? I'm a cracking shot."
        nicky "That's plain to see..."
        nicky "But there's something you're not very good at..."
        s3_mc "Oh?"
        nicky "Paying attention!"
        "He points behind you."
    elif s3e2p3_first_victim == "Seb":
        seb "That was a banging shot, [s3_name]."
        s3_mc "What can I say? I'm a cracking shot."
        seb "That's plain to see..."
        seb "But there's something you're not very good at..."
        s3_mc "Oh?"
        seb "Paying attention!"
        "He points behind you."
    elif s3e2p3_first_victim == "AJ":
        aj "How'd you land such a good shot babes?"
        s3_mc "What can I say? I'm a cracking shot."
        aj "That's plain to see..."
        if s3_like_aj:
            aj "Maybe later you can show me what else you're good at..."
            "She winks at you."
        aj "But there's something you're not very good at..."
        s3_mc "Oh?"
        aj "Paying attention!"
        "She points behind you."

    if s3_mc.bff == "Nicky" and s3e2p3_first_vistim == "Nicky":
        "You turn just in time to see the pasta leave [s3_mc.current_partner]'s hand before it hits you in the chest."
        nicky "Hah-hah!"
    elif s3_mc.bff == "Seb" and s3e2p3_first_vistim == "Seb":
        "You turn just in time to see the pasta leave [s3_mc.current_partner]'s hand before it hits you in the chest."
        seb "Hah-hah!"
    else:
        "You turn just in time to see the pasta leave [s3_mc.bff]'s hand before it hits you in the chest."

    # CHOICE
    menu:
        thought "That's it, I'm going to get..."
        "Bill":
            $ s3e2p3_second_victim = "Bill"
        "Harry":
            $ s3e2p3_second_victim = "Harry"
        "Camilo":
            $ s3e2p3_second_victim = "Camilo"
        "Seb":
            $ s3e2p3_second_victim = "Seb"
        "AJ":
            $ s3e2p3_second_victim = "AJ"
        "Nicky":
            $ s3e2p3_second_victim = "Nicky"

    s3_mc "Oi! [s3e2p3_second_victim]!"

    if s3e2p2_second_victim == "Bill":
        bill "Huh?"
        "You grab a handful of the pasta and launch it at [s3e2p3_second_victim]."
        "It sticks pleasingly to his face."
        if s3e2p3_first_victim == s3e2p3_second_victim:
            bill "Guess, I deserved a second serving..."
        else:
            bill "Ugh! The sauce surprise is everywhere!"
        bill "OK, in hindsight, that was not a good idea."
    elif s3e2p2_second_victim == "Harry":
        harry "Huh?"
        "You grab a handful of the pasta and launch it at [s3e2p3_second_victim]."
        "It sticks pleasingly to his face."
        if s3e2p3_first_victim == s3e2p3_second_victim:
            harry "Guess, I deserved a second serving..."
        else:
            harry "Ugh! The sauce surprise is everywhere!"
    elif s3e2p2_second_victim == "Camilo":
        camilo "Huh?"
        "You grab a handful of the pasta and launch it at [s3e2p3_second_victim]."
        "It sticks pleasingly to his face."
        if s3e2p3_first_victim == s3e2p3_second_victim:
            camilo "Guess, I deserved a second serving..."
        else:
            camilo "Ugh! The sauce surprise is everywhere!"
    elif s3e2p2_second_victim == "Seb":
        seb "Huh?"
        "You grab a handful of the pasta and launch it at [s3e2p3_second_victim]."
        "It sticks pleasingly to his face."
        if s3e2p3_first_victim == s3e2p3_second_victim:
            seb "Guess, I deserved a second serving..."
        else:
            seb "Ugh! The sauce surprise is everywhere!"
        seb "This stuff's like tar!"
    elif s3e2p2_second_victim == "AJ":
        aj "Huh?"
        "You grab a handful of the pasta and launch it at [s3e2p3_second_victim]."
        "It sticks pleasingly to his face."
        if s3e2p3_first_victim == s3e2p3_second_victim:
            aj "Guess, I deserved a second serving..."
        else:
            aj "Ugh! The sauce surprise is everywhere!"
    elif s3e2p2_second_victim == "Nicky":
        nicky "Huh?"
        "You grab a handful of the pasta and launch it at [s3e2p3_second_victim]."
        "It sticks pleasingly to his face."
        if s3e2p3_first_victim == s3e2p3_second_victim:
            nicky "Guess, I deserved a second serving..."
        else:
            nicky "Ugh! The sauce surprise is everywhere!"

    "Bill swivels around with a fistful of food."
    bill "Prepare to get wrecked!"
    "Nicky, Harry and Camilo turn to face him, all bearing food in their hands."
    bill "Oh, woah, wait a minute, lads..."
    "They let loose. Pasta, watermelon, cake, ice cream, and some mystery foods fly through the air. Bill is covered in them."
    bill "Agh! I'm done, I'm done! You got me..."
    "As the last chunk of watermelon lands on an outdoor light, everyone stops and looks down at the mess on the floor, table and themselves."
    camilo "Well, that got intense."
    bill "I think I have cheese in my ear."
    nicky "Damn, that would've been a perfect set-up for some kind of cheesy one-liner joke."
    bill "Too bad I never say cheesy one-liners."
    nicky "Give it time..."

    return

label s3e2p3_clean_off_with_cam:
    camilo "Let's go, then."

    scene s3-bathroom with dissolve
    $ on_screen = []

    "You and Camilo step into the bathroom. Bits of spaghetti drop onto the floor."
    s3_mc "Ugh, it's so cold and slimy..."
    camilo "Don't worry, we'll get off."
    camilo "I mean, get it off..."
    "You start to wipe away some of the sauce on your leg. Camilo pulls strands of spaghetti off your back."

    if s3e2p3_food_fight:
        camilo "That food fight got messy. You were smart to get to the shower first."
        camilo "That wait is going to be long for everyone else."
        "The tips of his fingers brush against your neck and shoulders."
    else:
        camilo "Lucky there isn't a queue for the shower or anything."
        "You feel Camilo move his hand up to your hair, pulling away more spaghetti as gently as if your hair was made of silk."

    # CHOICE
    menu:
        thought "What should I say to Camilo?"
        "How are you and Iona getting on?":
            camilo "Hmm, that's a tough one."
            camilo "Don't get me wrong, yeah, Iona's flames, but, like, I don't think I fancy her."
            s3_mc "Oh?"
            camilo "Yeah..."
            s3_mc "Who do you fancy, then?"
            camilo "You, of course."
            camilo "Thought that was obvious."
        "You have a really gentle touch...":
            camilo "Thanks. It comes from my little sister. She asks me to stroke her head when she can't sleep."
            camilo "I quickly learned how much pressure is just right."
            s3_mc "Having my head scratched puts me to sleep so quickly..."
            camilo "Same. I almost can't think of a better sensation."
        "Enjoying the view back there?":
            camilo "I'd be lying if I said no..."

    "You turn so you're facing him..."
    camilo "Hey, [s3_name], tell me about your family."

    # CHOICE
    menu:
        thought "What's my family like?"
        "Just kind of normal really...":
            s3_mc "Just your typical family, you know?"
            "He chuckles."
            camilo "I used to wonder what it'd be like growing up in one of them."
            camilo "There's always something going on in my family. Something loud."
        "We're quite rowdy":
            s3_mc "Not exactly, what you'd call reserved."
            "He grins."
            camilo "I knew I liked you."
            camilo "My family's like that, too. Always something going on. Something loud."
        "We're pretty quiet":
            s3_mc "We like to just chill out and do our own thing most of the time."
            camilo "Wow, I can't imagine that."
            camilo "There's always something going on in my family. Something loud."

    camilo "People think we're arguing even when we're agreeing!"

    # CHOICE
    menu:
        thought "Camilo grew up in a loud family..."
        "You must have brothers":
            s3_mc "Let me guess - brothers?"
            camilo "Just one. But it's actually my sisters, Gabriela and Alejandra, who you've gotta watch out for."
            camilo "You don't wanna mess with them. And then I've got literally about fifty cousins, no bants."
        "You must have sisters":
            s3_mc "Let me guess - sisters?"
            camilo "How'd you guess?"
            camilo "Two sisters, Gabriela and Alejandra. And one brother. And literally about fifty cousins, no bants."
        "Tell me more about your family":
            s3_mc "I want to hear all about them."
            camilo "Well, there's my mum and dad, and then two sisters, Gabriela and Alejandra, and my brother. And literally about fifty cousins, no bants."

    s3_mc "What's your brother's name?"
    camilo "Tom."
    "He shrugs."
    camilo "I think my parents wanted to mix it up a bit by the time they had him."
    s3_mc "Are you the oldest?"
    camilo "Yeah. Gabriela and Alejandra are 22 and 21, then Tom's 19."
    "He smiles with such genuine warmth that for a moment you can almost feel it on your skin."
    camilo "We're family, but we're mates too, you know?"
    s3_mc "That's so nice."
    camilo "Yeah. We're tight."
    "He looks down."
    camilo "Lots of people round my end aren't so lucky. Divorce and that."


    # CHOICE
    menu:
        thought "Camilo looks a bit sad..."
        "Tell him a joke":
            s3_mc "Hey, I've got a joke for you."
            "He brightens."
            camilo "I proper love jokes. Go on, then."
            s3_mc "A ham sandwich walks into a bar. The barman looks up and says..."
            s3_mc "'Sorry, we don't serve food here.'"
            "It takes him a moment."
            camilo "Haha, classic. Food."
            camilo "Amazingly fit and funny. The whole package."
            "He grins at you, and you suddenly realise how close you are."
        "Try to distract him":
            s3_mc "Hey, look! An owl!"
            "Camilo looks round, confused."
            camilo "An... owl?"
            s3_mc "Yeah, I, er... thought I saw an owl."
            camilo "You are proper silly, you."
            camilo "But amazingly fit."
            "He grins at you, and you suddenly realise how close you are."
        "Give him a hug":
            s3_mc "Hey..."
            "You shuffle over to him and put your arm around his broad shoulder. His back is hard and muscular."
            "He immediately brightens up, and hugs you back. His warm, strong hands wrap around you. He smells like coffee, cherries and cinnamon."
            "He whispers in your ear."
            camilo "You are well fit."

    # CHOICE
    menu:
        thought "He's so hot..."
        "Give him a peck on the cheek":
            "You softly plant your lips on his tanned cheek, noting with satisfaction that the hair on his arms rise up."
            camilo "Any chance of another?"
            s3_mc "That's all for now."
            camilo "Blimey, mamacita. I'm gonna have to up my game, aren't I?"
            s3_mc "Yep."
        "Give him a proper kiss":
            "You press your lips against his. You sink into the warmth of his arms, and he kisses you back like it's all he ever wanted."
            s3_mc "Wow, you've done that before."
            camilo "It was all practice for you, mamacita."
            s3_mc "Cheesy, but I'll allow it."
            camilo "I'll up my game next time."
            s3_mc "I'll look forward to it."
        "Gently pull away":
            camilo "I really wanna kiss you right now."
            s3_mc "Not this time."
            camilo "So maybe next time?"
            s3_mc "Maybe. We'll see."
            camilo "Blimey, mamacita. I'm gonna have to up my game, aren't I?"
            s3_mc "Yup."

    s3_mc "Alright, I should get showered."
    camilo "I'd offer to join you but there wouldn't be much cleaning happening..."
    s3_mc "You're right."
    camilo "I'll leave you to it."

    show camilo at npc_exit
    pause 0.3
    $ renpy.hide("camilo")

    return

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
    show nicky at npc_exit
    pause 0.3
    $ renpy.hide("nicky")
    $ on_screen = []

    "Come to think of it, 'dinner' might be generous as well..."
    elladine "How's this a fruit salad? It's just watermelon."
    show elladine at npc_exit
    pause 0.3
    $ renpy.hide("elladine")
    $ on_screen = []

    if s3e2p3_food_fight:
        "Though in the end, most of it ended up on the Islanders..."

    "But fear not, Camilo's steaming empanadas saved the day!"
    aj "This is better than sex."
    show aj at npc_exit
    pause 0.3
    $ renpy.hide("aj")
    $ on_screen = []

    "Look out for a surge in empanada-making courses this summer."
    "Coming up!"
    "Elladine shoots for the stars!"
    elladine "Then he took me out to the balcony..."
    show elladine at npc_exit
    pause 0.3
    $ renpy.hide("elladine")

    "Wish I had a balcony."
    "...or a window, for that matter."
    "Nobody made dinner for me last night, by the way."
    "I had a microwave cheeseburger."
    "Thanks for asking."

    scene s3-bedroom-day with dissolve
    $ on_screen = []

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

    $ outfit = "swim"

    # ADD BACK ONE MC HAS IMAGES
    # thought "Hmm, let's see. What should I wear?"
    # # MC outfit change to swimwear
    # thought "What out, everyone. Here I come!"
    # thought "This outfit already has a proven track record of turning heads."
    # s3_mc "It's perf."
    # thought "I guess I'll have to rely on my sparkling personality."

    scene s3-kitchen-day with dissolve
    $ on_screen = []

    "Nicky, Seb, Genevieve and Elladine are hanging out in the kitchen."
    # ADD BACK ONCE MC HAS IMAGES
    # elladine "Wow, [s3_name], that outfit really brings out your...everything."
    elladine "Hi [s3_name]."
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
    genevieve "Oh, I love him! He's got that song, 'You Eyes and Mine'."
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
    $ on_screen = []
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
    $ on_screen = []
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
    $ on_screen = []
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

label s3e3p1_ending:
    scene s3-kitchen-day with dissolve
    $ on_screen = []

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
    show genevieve at npc_exit
    pause 0.3
    $ renpy.hide("genevieve")
    $ on_screen.remove("genevieve")

    show harry at move_center
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
                    harry "Sounds good!"
                    harry "I love French toast, but I never knew how to make it."
                "American pancakes":
                    harry "Sounds good!"
                    harry "I think I made British-style ones once."
                    harry "But I always wanted to know how to make the fluffy ones!"
                "Poached eggs on toast":
                    harry "I love poached eggs!"
                    harry "They're pretty tricky, though, right?"
                    s3_mc "Don't worry. There's a knack to it."
                "Vegan American pancakes":
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

    scene sand with dissolve
    $ on_screen = []

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
    show elladine at npc_exit
    pause 0.3
    $ renpy.hide("elladine")
    $ on_screen = []

    "And [s3_name], Genevieve, and AJ got physical..."
    "In an arm wrestling competition!"
    aj "Wanna try your luck?"
    show aj at npc_exit
    pause 0.3
    $ renpy.hide("aj")
    $ on_screen = []

    "You're on, AJ."
    "I've been single forever."
    "Which means I have a distinct advantage when it comes to arm wrestling with my right hand."
    "Coming up!"
    "The Islanders get stuck in a game of Truth and Dare."
    camilo "What are you doing down there?"
    show camilo at npc_exit
    pause 0.3
    $ renpy.hide("camilo")
    $ on_screen = []

    "And Bill is looking a little pail..."
    show bill bucket at npc_center
    bill "Help me!"
    show bill at npc_exit
    pause 0.3
    $ renpy.hide("bill")

    "Sorry Bill, can't help you there."
    "The last time I did a dare..."
    "I ended up having to be a voice over for ten people in their swimwear."
    "Here comes [s3_name], AJ, Camilo, Harry, Bill, Genevieve, Elladine, Nicky, Seb and Iona."
    "They're raring to get daring!"
    "Sigh."
    "I wonder if I'll ever escape."

    scene s3-sun-loungers-day with dissolve
    $ on_screen = []

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

label s3e3p2_lounge:
    scene s3-lounge as dissolve
    $ on_screen = []
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
    $ on_screen = []
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
    $ on_screen = []
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
    $ on_screen = []
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
    $ on_screen = []

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
    show aj at npc_exit
    pause 0.3
    $ renpy.hide("aj")

    "Excited is an understatement."
    "This is a recoupling, people!"
    
    show elladine at npc_center
    elladine "And the most exciting part of the recoupling is what comes after."
    show elladine at npc_exit
    pause 0.3
    $ renpy.hide("elladine")
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
    show bill at npc_exit
    show nicky at npc_exit
    pause 0.3
    $ renpy.hide("bill")
    $ renpy.hide("nicky")
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
    $ on_screen = []

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

    show genevieve at npc_exit
    show elladine at npc_exit
    pause .3
    $ renpy.hide("genevieve")
    $ renpy.hide("elladine")
    $ on_screen = []
    
    $ outfit = "evening"

    "Iona mists herself with one last squirt of strawberry-scented perfume."
    iona "Right, is everyone ready?"
    miki "As I'll ever be!"
    aj "Then let's go, team!"
    "The six of you head out of the dressing room and towards the firepit."

    scene s3-firepit-night with dissolve
    $ on_screen = []

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
    $ on_screen = []

    if s3e3p3_go_alone:
        $ s3_mc.like([s3e3p3_lonely_one])
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

        if s3e3p3_get_to_know == "Bill" or s3e3p3_get_to_know == "Camilo" or s3e3p3_get_to_know == "Harry" or s3e3p3_get_to_know ==  "Nicky":
            if s3e3p3_get_to_know == "Nicky":
                s3_mc "I know people see him and Elladine as a solid couple, but I think his could still be turned."
            else:
                s3_mc "I know he's with [s3_3rd_girl_options[s3e3p3_get_to_know]], but I don't think they're serious yet. His head could def still be turned."

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
                bill "I don't mind speaking what I think, but also don't give a monkeys if people don't agree."
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

    
label s3e3p3_roof_sex:
    scene s3-roof-night with dissolve
    $ on_screen = []
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

label s3e3p3_ending:
    scene s3-bedroom-night with dissolve
    $ on_screen = []

    "When you arrive in the bedroom, the other Islanders are already getting into bed."
    thought "Hmm, I should probably get into some comfier clothes..."

    scene s3-dressing-room with dissolve
    $ on_screen = []

    # Add back one MC has images in game
    # "MC outfit change to sleepwear"
    # "Hey, babe." -> always
    # "You look so great in those." -> if one of current partner fav outfits, else nothing

    "You get changed into your pjs."
    thought "That's better."

    $ outfit = "pjs"

    scene s3-bedroom-night with dissolve
    $ on_screen = []

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
        show bill at npc_exit
        pause .3
        $ renpy.hide("bill")
    elif s3_mc.current_partner == "Camilo":
        show camilo at npc_exit
        pause .3
        $ renpy.hide("camilo")
    elif s3_mc.current_partner == "Harry":
        show harry at npc_exit
        pause .3
        $ renpy.hide("harry")
    elif s3_mc.current_partner == "AJ":
        show aj at npc_exit
        pause .3
        $ renpy.hide("aj")

    $ on_screen = []

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
        show elladine at npc_exit
        pause .3
        $ renpy.hide("elladine")
        $ on_screen.remove("elladine")
    elif s3_mc.bff == "Genevieve":
        genevieve "Nothing..."
        show genevieve at npc_exit
        pause .3
        $ renpy.hide("genevieve")
        $ on_screen.remove("genevieve")
    elif s3_mc.bff == "Nicky":
        nicky "Nothing..."
        show nicky at npc_exit
        pause .3
        $ renpy.hide("nicky")
        $ on_screen.remove("nicky")
    elif s3_mc.bff == "Seb":
        seb "Nothing..."
        show seb at npc_exit
        pause .3
        $ renpy.hide("seb")
        $ on_screen.remove("seb")

    if s3_mc.current_partner == "Bill":
        show bill at move_center
    elif s3_mc.current_partner == "Camilo":
        show camilo at move_center
    elif s3_mc.current_partner == "Harry":
        show harry at move_center
    elif s3_mc.current_partner == "AJ":
        show aj at move_center

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