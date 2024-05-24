#########################################################################
## Episode 1, Part 1
#########################################################################
label s3e1p1:

    scene sand with dissolve

    "WHYYYY"

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

    scene s3-outside-villa-entrance with dissolve

    "Your heel click on the driveway as you stride up to the Villa."

    thought "It's gorgeous!"
    thought "I can't believe this is going to be my home for the next two weeks!"
    thought "Unless I go home early."
    thought "I wonder where everybody is?"

    "A girl peeks her head out of the entrance."

    show elladine at npc_center

    "She yells in excitement when she sees you."

    elladine @ surprised "Hey! You made it!"
    elladine @ smile "It's so nice to meet you! I'm Elladine."

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
            elladine @ smile "I know we will."

        "Wow, I love your outfit":
            $ s3_mc.like("Elladine")
            s3_mc "It's stunning!"
            elladine smile "Babes, I was about to say the same to you!"
            elladine @ surprised "Seriously. You've already set the bar super high."
            elladine "The boys are going to freak when they see us."

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

    elladine sad "I've been feeling well nervous ever since I got here."
    elladine serious "I mean it's exciting, but it's also a lot of pressure, isn't it?"

    # CHOICE
    menu:
        thought "How am I feeling?"
        "So nervous":
            s3_mc "I've never done anything like this before. It's a bit scary."
            elladine surprised "At least we're all in the same boat!"

        "Just excited":
            s3_mc "I'm really excited to meet everyone!"

        "Kinda hungry":
            $ s3e1p1_feeling_hungry = True
            elladine blush "You mean, like...hungry for love, or..?"
            s3_mc "Nope. Just hungry."
            elladine "Sounds like you need a snack."
            elladine smile "I hope there are some snacks lined up for us outside!"
            s3_mc "Why would there be snacks outside?"
            elladine @ surprised "I mean like hot guys when you see someone hot and you say 'he's a snack'."
            s3_mc "That's not what I meant, though. I'm just hungry."
            s3_mc "I wish I had a banana or something."
            "Elladine looks like she's about to make another joke, but then decides against it."

    s3_mc "Are there any other girls here yet?"
    elladine neutral"Only one. We've been waiting in the bedroom."
    elladine @ smile "Come on. I'll introduce you."

    scene s3-bedroom-day with dissolve
    $ on_screen = []

    "Elladine leads you into the bedroom, where another girl is waiting."
    "Her jaw drops when you walk in."

    aj blush "Are you the new arrival?"
    aj sad "Man, I knew everyone here was gonna be gorgeous, but I wasn't prepared..."
    elladine @ surprised "Stop staring and introduce yourself!"
    aj smile "Sorry, sorry!"
    aj neutral "My name's AJ. It's nice to meet you."

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
        elladine @ smile"We were just talking outside. She's really nice."

    aj @ surprised "I hope everyone's going to be cool. I don't want to get sucked into a load of drama."
    aj "I mean, we're all here to have fun, right?"

    # CHOICE
    menu:
        thought "AJ's here to have fun, not to get into drama..."
        "Me too! Let's keep it chill and friendly":
            $ s3_mc.like("AJ")
            s3_mc "Trust me, we're gonna have a great time."
            s3_mc "You're my girls now, and I don't let my girls turn on each other."
            aj @ smile "Yes! I'm so glad you said that."

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
    aj @ smile "I want you all to be like my new teammates while we're here."


    # CHOICE (assigns your job)
    menu:
        elladine "What do you do on the outside, [s3_name]?"
        "Model":
            $ s3_mc.job = 'Model'
            aj surprised "I knew it! As soon as you walked in, I was like, I bet she's a model."
            elladine surprised "Yeah, I can't say I'm surprised either."
        "Scientist":
            $ s3_mc.job = 'Scientist'
            aj surprised "Oh wow, that's really cool!"
            aj neutral "It's not fair that someone as pretty as you gets to be smart as well."
        "Musician":
            $ s3_mc.job = 'Musician'
            elladine @ smile "I love musicians. If I find out one of the boys is in a band, I'm going to make a beeline straight for him."
        "Athlete":
            $ s3_mc.job = 'Athlete'
            aj surprised "Snap!"
            aj smile "I knew I felt a connection with you as soon as you walked in here."


    "Suddenly, you hear a beeping noise."
    s3_mc "What was that?"
    elladine @ surprised "It sounded like a text..."
    "AJ checks her phone and gasps."
    aj @ surprised "Oh, it's me!"
    aj smile "I've got a text!"

    text "Girls, it's time to start meeting the boys. AJ, please make your way to the lawn and choose a boy to couple up with. Elladine and [s3_name], stand by in the bedroom. You'll be up next! #girlmeetsboy #getthepartystarted"

    aj neutral "What? But the other girls still haven't arrived yet!"
    elladine @ blush "I guess they'll be coming in later?"
    aj @ surprised "I'd better go, then."
    aj "I'll see you out there, guys."
    elladine neutral "Good luck!"

    "AJ races out of the bedroom. Her heels clack all the way to the lawn."

    show aj at npc_exit
    pause 0.3
    $ renpy.hide("aj")
    $ on_screen.remove("aj")
    
    elladine "She's got a lot of energy, hasn't she?"
    elladine @ blush "I guess it's hard not to be excited when you know you're picking first."
    s3_mc "I wonder what the boys will be like?"
    elladine smile "I want a guy who's been around the block a bit, you know?"
    elladine smile "Someone who knows what he's about and takes it seriously."
    elladine neutral "What about you? What's your type?"

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
            elladine @ blush "Good point."

        "I'll take one now, just in case":
            "You take a single condom and hide it in your bikini for later."
            "Elladine giggles again."
            elladine @ smile "You go, girl!"

        "Grab a whole handful":
            $ s3e1p1_grab_some_condoms = True
            "You take a fistful of condoms and stuff them down your top."
            "Elladine giggles again."
            elladine @ smile "You go, girl!"

    elladine "I'm going to hold off for now."
    elladine "I probably won't do any big bits right away..."
    elladine @ cheeky "Unless the right guy comes along, obvs."
    elladine @ surprised "Text! I think that means it's my turn!"
    "She gives you a quick hug before heading to the door."
    elladine @ smile"Good luck, [s3_name]. I'll see you down there."

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
    bill @ cheeky "Alright, beautiful? I'm Bill."

    # solo portrait shot of bill
    window hide
    show screen s3_character_profile("bill") with Pause(3)
    hide screen s3_character_profile with dissolve

    "{i}Bill\n
    -24, from Surrey\n
    -Roofer\n
    -Strong opinions about sandwiches{/i}"

    bill smile "I'm gonna come right out and say it. You look like a bit of me."

    # CHOICE
    menu:
        thought "Bill says I'm a bit of him..."
        "Smile politely":
            "You smile at Bill, trying not to give too much away."
            "I'm definitely in there."
        
        "Wink at him":
            $ s3_mc.like("Bill")
            show bill smile
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
    camilo @ blush "Hola chica. Welcome to the Villa. Amazing, isn't it?"
    s3_mc " Is it?"
    camilo smile "Well, it is now you're here."

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
    camilo smile "So I thought I should try and fancy it up a bit."

    # CHOICE
    menu:
        thought "Camilo definitely likes me..."
        "The feeling is mutual":
            $ s3_mc.like("Camilo")
            show camilo cheeky
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
    harry @ cheeky "Hey, I'm Harry."

    # solo portrait shot of harry
    window hide
    show screen s3_character_profile("harry") with Pause(3)
    hide screen s3_character_profile with dissolve

    "{i}Harry\n
    -21, from York\n
    -Business student\n
    -Usually wears a tie with his swimsuit{/i}"

    harry @ smile "For what it's worth, I'm just as gobsmacked as these other two."
    harry "But I won't try to sway you. You've got to listen to your gut."
    harry blush "Or your heart. Or, like whatever part of your body you trust to make these decisions."

    # CHOICE
    menu:
        thought "I think Harry's trying to flirt with me, too..."
        "It's working!":
            $ s3_mc.like("Harry")
            show harry blush
            "You give Harry a flirty smile. He blushes hard."
            show harry cheeky
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
            # ADJUST AFTER REFACTORING
            $ s3_li = "Bill"
            $ s3_mc.past_partners.append("Bill")
            $ s3_li = "Bill"
            $ s3_mc.like("Bill")
            $ s3_mc.like("Bill")
        "Camilo":
            # ADJUST AFTER REFACTORING
            $ s3_li = "Camilo"
            $ s3_mc.past_partners.append("Camilo")
            $ s3_li = "Camilo"
            $ s3_mc.like("Camilo")
            $ s3_mc.like("Camilo")
        "Harry":
            # ADJUST AFTER REFACTORING
            $ s3_li = "Harry"
            $ s3_mc.past_partners.append("Harry")
            $ s3_li = "Harry"
            $ s3_mc.like("Harry")
            $ s3_mc.like("Harry")

    $ s3_li_lower = s3_li.lower()
    s3_mc "The boy I want to couple up with is... [s3_li]!"
    "You stride over to [s3_li]."
    "He grins like he can't hardly believe his luck."
    s3_li smile "Nice one."

    $ s3_3rd_girl = s3_3rd_girl_options[s3_li]

    menu:
        thought "Me and [s3_li] are officially coupled up..."
        "Hug him":
            "As you reach him, you throw your arms around his shoulders."
            "He hugs you back firmly. His hands are warm on the small of your back."
        "Kiss his cheek":
            "As you reach him, you plant a kiss on his cheek, being careful not to smudge your lipstick."
        "Hands off for now":
            "You stand politely at his side, just close enough for your elbows to brush."

    s3_li smile "I'm so glad you picked me."
    s3_mc "Did I make the right decision?"
    s3_li cheeky "Definitely. But I would say that, wouldn't I?"

    "The two of you go to stand next to the other couples."

    elladine smile "Hey girl! Congratulations!"
    elladine "You really bagged yourself a hottie there."
    elladine "Um, no offence, Nicky."

    nicky "None taken."
    nicky smile "Hi, by the way."
    nicky "I'm Nicky. I'm the lucky guy who's coupled up with Elladine."

    # solo portrait shot of nicky
    window hide
    show screen s3_character_profile("nicky") with Pause(3)
    hide screen s3_character_profile with dissolve

    "{i}Nicky\n
    -24, from Newcastle\n
    -Music tutor\n
    -Oldest sibling energy{/i}"

    elladine @ smile "As soon as I found out he was a musician, I was hooked."
    elladine neutral "I've already got a really good feeling about this one."

    aj blush "Er, yeah. Me too."
    "AJ doesn't sound so convinced about her guy..."

    seb smile "Alright? My name's Seb. I'm coupled up with AJ."

    # solo portrait shot of seb
    window hide
    show screen s3_character_profile("seb") with Pause(3)
    hide screen s3_character_profile with dissolve

    "{i}Seb\n
    -28, from Liverpool\n
    -Runs a music shop\n
    -Owns 52 t-shirts and 1 shirt{/i}"

    aj surprised "I coupled up with a musician, too!"
    seb "Well, no. I'm a shopkeeper."
    aj serious "But you must know about instruments to sell them, right?"
    seb "It's not that kind of music shop. I sell records."
    seb @ surprised "You know, CDs and vinyl and stuff. There's a coffee shop, too."
    aj @ surprised "Oh! With you now, sorry."

    "{i}You can't date Nicky or Seb in this season of Island Amore The Game, but that doesn't mean you can't be friends! And don't worry - all the other boys, and some of the girls, are options.{/i}"

    aj neutral "This is so nice, you guys! We're already learning so much about each other!"

    nicky @ blush "Whoa there."
    nicky "We're still waiting on two more new girls, right?"

    elladine @ awkward"Yeah. I wonder what they'll be like?"

    # CHOICE
    menu:
        s3_mc"The last two girls..."
        "I can't wait to meet them":
            s3_mc "We're not a complete Villa crew until everyone's here."
            aj @ surprised "Right! I'm so excited for them to get here!"
            nicky @ surprised "You're not the only ones."
            "Nicky looks over at the two remaining single boys."
        "They better stay away from [s3_li]":
            $ s3_mc.like(s3_li)
            nicky @ surprised "Wow! So committed already, huh?"
            s3_li smile "I kinda like it."
            s3_li "It's nice to know [s3_name] is feeling it so strongly."
            s3_li @ surprised "I mean, if another boy came in right now and tried to couple up with her, I'd have a thing or two to say about it, as well."
        "Maybe they got lost on the way here":
            s3_mc "This place isn't exactly well signposted."
            nicky @ surprised "Bad news for the leftover boys if you're right."

    s3_li neutral "I wonder if they'd be open to coupling up with each other."
    "[s3_li] looks over at the two remaining single boys."

    # IF STATEMENT
    if s3_li == "Bill":
        "Camilo's smile is still dazzling, but it looks a little more nervous now."
        "Harry stands up straight, trying to look confident."
    elif s3_li == "Camilo":
        "Bill is masking his disappointment by concentrating on the grass between his toes."
        "Harry stands up straight, trying to look confident."
    elif s3_li == "Harry":
        "Bill is masking his disappointment by concentrating on the grass between his toes."
        "Camilo's smile is still dazzling, but it looks a little more nervous now."

    aj serious "I feel bad for them. Nobody wants to get picked last."
    elladine sad "Yeah, and it's pretty obvious they both wanted to get picked by [s3_name]..."
    aj "Well, maybe their perfect soulmates are about to walk out of that door any second."
    seb serious "Let's not kid ourselves. That kind of thing never happens in the real world."
    nicky "Alright, but this isn't exactly a normal situation, is it?"
    nicky "It's Island Amore. Where dreams come true."
    seb neutral "Wow, corny."
    nicky "Come on, mate. The magic only works if you believe in it."
    seb @ sad "Maybe that's why nothing magical ever happens to me."

    # CHOICE
    menu:
        thought "Do dreams come true in the Villa?"
        "Nicky's got it right!":
            $ s3_mc.like("Nicky")
            s3_mc "I can't wait for whatever's on the horizon!"
            nicky @ smile "That's the spirit."
        "I don't believe in magic":
            $ s3_mc.like("Seb")
            s3_mc "If we're gonna have fun in the Villa, it won't be from magic."
            s3_mc "It'll be from hard grafting."
            seb @ smile "You've got that right."
        "My dreams are too weird":
            $ s3_mc.like("Nicky")
            $ s3_mc.like("Seb")
            s3_mc "If they manage to make my dreams come true, I'll be impressed."
            s3_mc "Could they even fit a T-Rex in here?"

    "Everyone falls silent as a new girl emerges from the Villa."

    # IF STATEMENT (which women show up in villa first)
    if s3_li == "Harry":
        call s3e1p1_meet_miki from _call_s3e1p1_meet_miki
        call s3e1p1_meet_iona from _call_s3e1p1_meet_iona
    elif s3_li == "Bill":
        call s3e1p1_meet_iona from _call_s3e1p1_meet_iona_1
        call s3e1p1_meet_genevieve from _call_s3e1p1_meet_genevieve
    elif s3_li == "Camilo":
        call s3e1p1_meet_miki from _call_s3e1p1_meet_miki_1
        call s3e1p1_meet_genevieve from _call_s3e1p1_meet_genevieve_1

    # CHOICE
    menu:
        thought "They've made an impression on each other already..."
        "It's really cute":
            thought "I hope me and [s3_li] get on as well as they do!"
        "It's probably not real":
            thought "It's not like they really know each other..."
            thought "They're probably just showing off."
        "I'd be the filling in that sandwich":
            thought "They make such a hot couple!"

    elladine @ surprised "I think that's everyone."
    bill @ smile "Five great ladies, five great gents, five great couples. Makes sense to me."
    aj blush "Don't you think it's a bit early to say whether our couples are great or not?"

    # IF STATEMENT
    if s3_li == "Bill":
        bill cheeky "I dunno. I've already got a pretty great feeling about this one."
        iona @ blush "Well, it's not a competition."
    elif s3_li == "Camilo":
        camilo cheeky "I dunno. I've already got a pretty great feeling about this one."
        miki @ blush "Well, it's not a competition."
    elif s3_li == "Harry":
        harry cheeky "I dunno. I've already got a pretty great feeling about this one."
        miki @ blush "Well, it's not a competition."

    nicky @ surprised "It sort of is, though. Only the strongest couple can win the fifty grand."

    # CHOICE
    menu:
        s3_mc "Based on first impressions, I think the strongest couple here will be..."
        "Me and [s3_li]":
            $ s3e1p1_strongest_couple = "MC"
            # IF STATEMENT
            $ s3_mc.like(s3_li)
            s3_li @ cheeky "Not to bang my own drum or anything, but hard agree."
            elladine @ smile "I can't lie, you two do look super cute together."
        "Miki and Bill" if s3_li == 'Camilo' or s3_li == 'Harry':
            $ s3e1p1_strongest_couple = "Miki and Bill"
        "Iona and Camilo" if s3_li == 'Bill' or s3_li == 'Harry':
            $ s3e1p1_strongest_couple = "Iona and Camilo"
        "Genevieve and Harry" if s3_li == 'Camilo' or s3_li == 'Bill':
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
            aj blush "Wow, really?"
            seb blush "That's, um... sweet of you to say."

    # IF STATEMENT
    if s3e1p1_strongest_couple == "Miki and Bill" or s3e1p1_strongest_couple == "Iona and Camilo" or s3e1p1_strongest_couple == "Genevieve and Harry":
        $ s3_mc.dislike(s3_li)
        s3_li sad "Stronger than you and me?"
        s3_mc "I'm just being honest."

    # IF STATEMENT
    if s3_li == "Bill":
        iona @ surprised "All I meant was, it might be a competition, but it doesn't really matter who wins."
        iona "We're all just here to find love, right?"
    elif s3_li == "Camilo" or s3_li == "Harry":
        miki @ surprised "All I meant was, it might be a competition, but it doesn't really matter who wins."
        miki "We're all just here to find love, right?"

    # CHOICE
    menu:
        s3_mc "I'm here..."
        "To win the game":
            s3_mc "Don't get me wrong, we all want to find someone..."
            s3_mc "But that doesn't change the fact that this is a competition."
            s3_mc "There will be a winner."
            s3_mc "And that winner will be me."
            s3_li smile "Wow. Love that confidence."
        "To fall in love":
            s3_mc "She's right. At the end of the day, all that matters is finding the right person for you."
            s3_mc "That's the only prize worth winning, really."
            # IF STATEMENT
            if s3_li == "Bill":
                $ s3_mc.like("Iona")
                iona @ surprised "Wow, yes. [s3_name] just said it better than I ever could."
            elif s3_li == "Camilo" or s3_li == "Harry":
                $ s3_mc.like("Miki")
                miki @ surprised "Wow, yes. [s3_name] just said it better than I ever could."

        "To have fun":
            $ s3_mc.like("AJ")
            s3_mc "This is the holiday of a lifetime."
            s3_mc "Love is great and winning is fine, but why put so much pressure on it?"
            s3_mc "If all I get from this is a few cool new friends, I'll count myself a winner."
            aj @ surprised "Wow, yes. [s3_name] just said it better than I ever could."

    # IF STATEMENT
    if s3_li == "Harry":
        iona smile "Oh my days, you guys!"
        iona smile "I've got a text!"
    elif s3_li == "Camilo" or s3_li == "Bill":
        genevieve smile "Oh my days, you guys!"
        genevieve smile "I've got a text!"

    text "Islanders, it's time to get to know each other a little better. Please make your way to the challenge platform and get ready to unpack some secrets about your fellow Islanders! #excessbaggage #gettingtoknowyou"

    seb serious "We've only just got here and we're already being challenged?"
    seb sad "I was hoping we could get a nap first."

    # IF STATEMENT
    if s3e1p1_took_a_nap:
        $ s3_mc.like("Seb")
        s3_mc "I had a little nap just before I came out!"
        seb @ surprised "Oh mate, I wish I'd thought of that. Such a good move."
        seb "A little nap would be just the ticket."
    elif s3e1p1_feeling_hungry:
        $ s3_mc.like("Seb")
        seb @ surprised "I'm a little peckish too."
        s3_mc "Me too! I was saying to Elladine, I'd love some kind of snack."
        s3_li cheeky "Maybe I'm the kind of snack you're after."
        s3_mc "That's not the kind of snack I mean."

    nicky @ surprised "I hate to sound like a stuck record, but it's Island Amore."
    nicky "You have seen this show before, right? You didn't just get off at the wrong bus stop and end up here by mistake?"
    nicky "Because if that's what happened, the sooner you admit it, the less awkward it's going to be."
    elladine @ surprised "Aw, stop teasing him. He just needs a bit of time to get used to it, that's all."
    camilo smile "The challenges are just a bit of fun! It'll help us all get closer as a group."
    bill cheeky "More importantly, we'll find out everyone's saucy secrets."
    camilo blush "Well, that too, I guess..."
    bill @ surprised "Don't get me wrong. I've got nothing to hide."
    bill "But I'm excited to find out what the rest of you are holding back."
    harry @ surprised "That's true, but we're not just here to mess around and relax, or dig up gossip on each other."
    aj blush "We're not?"
    harry @ surprised "No! We're here on an important mission! To find someone we love. It's serious business."
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

    elladine @ surprised "Well, there's only one way to find out."

    # IF STATEMENT
    if s3_li == "Harry":
        iona smile "Let's go."
    elif s3_li == "Camilo" or s3_li == "Bill":
        genevieve smile "Let's go."

    if s3_li == "Bill":
        iona smile "Woo! I can't wait!"
    elif s3_li == "Camilo" or s3_li == "Harry":
        miki smile "Woo! I can't wait!"

    scene s3-lawn-day with dissolve
    $ on_screen = []

    "Chattering and laughing, the Islanders head towards the challenge platform."
    "Before you can follow, [s3_li] quietly takes you to one side."

    s3_li @ blush "Hey, [s3_name]. Sorry to hang back like this."
    s3_li @ smile "I just wanted to have a quick chat with you in private before the challenge, if that's OK."

    # CHOICE
    menu:
        thought "[s3_li] wants a chat..."
        "I thought you'd never ask":
            $ s3e1p1_li_wants_chat_response = "Positive"
            $ s3_mc.like(s3_li)
        "Sure, what's up.":
            $ s3e1p1_li_wants_chat_response = "Neutral"
        "I'd rather just get going.":
            $ s3_mc.dislike(s3_li)
            $ s3e1p1_li_wants_chat_response = "Negative"

    if s3e1p1_li_wants_chat_response == "Positive":
        s3_li cheeky "Well, I'm asking now."
    elif s3e1p1_li_wants_chat_response == "Negative":
        s3_li sad "Sorry, I'll try to make it quick."
    else:
        s3_li "Well..."

    s3_li @ smile "I just wanted to say thank you for choosing me."
    s3_li neutral "You could probably see it on my face, but you absolutely made my day."
    s3_li "You're blatantly the best-looking girl here."
    s3_li @ cheeky "And I'm no expert, but even I can see you're the best-dressed, too."

    # CHOICE
    menu:
        thought "This would be the perfect opportunity.."
        "Go in for a cheeky snog":
            $ s3e1p1_cheeky_snog = True
            $ s3_mc.like("s3_li")
            "You bet your eyelashes and tilt your face towards his."
            "His eyes go wide. His gaze flickers down to your lips, then back up to your eyes."
            "His voice is suddenly low and breathy."
            s3_li serious "Are you sure?"
            s3_mc "No time like the present."
            "He bites his lip."
            s3_li cheeky "I can't argue with that."
            if s3_li == "Bill":
                "He smiles as your lips meet."
                "His rough, calloused hands rest firmly on your hips."
                "Something about his hands seems to fit, as if the two of you have been doing this for years."
                "Finally, you both break away at the same time."
                s3_li smile "Cor."
            elif s3_li == "Camilo":
                "He draws you into a slow, sensual kiss."
                "His Hands tangle gently in your hair, stirring up goosebumps on the back of your neck."
                "Finally, you both break away at the same time."
                s3_li smile "Blimey."
            elif s3_li == "Harry":
                "He looks nervous and excited as you gently press your lips to his."
                "His hands tentatively come to rest on your lower back."
                "As the kiss goes on, he becomes more confident, pulling you close against him."
                "Finally, you both break away at the same time."
                s3_li smile "Gosh."
            s3_li "I didn't see that coming."
            s3_mc "Did you like it?"
            s3_li @ surprised "Did I like it? Did I like it? [s3_name]..."
            s3_li @ smile "I loved it."
            s3_li cheeky "Do you think we could do it again? Like, right now?"
            s3_mc "All in good time, babe."
        "Maybe later":
            $ s3e1p1_cheeky_snog = False
            "There's no rush. I only just got here."
    if s3_li == "Bill":
        s3_li @ smile "You seem like a girl who says what's on her mind, and I really admire that."
        s3_li neutral "I don't do subtlety, see. Whether I like someone or I don't like someone, I come right out and say so."
    elif s3_li == "Camilo":
        s3_li @ smile "And I don't just mean looks-wise. I think we've got that spark, you know?"
        s3_li neutral "It makes me wanna know everything there is to know about you."
    elif s3_li == "Harry":
        s3_li @ smile "I'm over here trying to act all manly and confident, and then you walk in, and it all just…melts away."
        s3_li neutral "And the weird thing is, I don't even mind."

    s3_li "So, yeah."
    s3_li "Obviously I won't try anything on if you're not interested, but I didn't want today to go any further without saying..."
    s3_li @ smile "I'm excited to start getting to know you."

    # CHOICE
    menu:
        thought "[s3_li] wants to get to know me..."
        "I'm excited to get to know you too":
            $ s3_mc.like(s3_li)
            s3_mc "I picked you for a reason. I can't wait to see where it leads us."
            s3_li smile "I'm glad you said that."
        "I'm not really interested, sorry":
            $ s3_mc.dislike(s3_li)
            s3_mc "Look, no offence..."
            s3_mc "But just because I liked you better than the other two, that doesn't mean I actually like you."
            s3_li @ sad "Oh... OK. I'm sorry."
            s3_li @ blush "I just assumed..."
            s3_li @ serious "I'll try to keep that in mind."
        "Let's wait and see how this goes":
            s3_mc "It's still early days."
            s3_li "Yeah, of course."
        "Show him the condoms" if s3e1p1_grab_some_condoms:
            $ s3_mc.like(s3_li)
            "You pull your bikini top out a bit and nod."
            s3_mc " Check this out."
            s3_li @ blush "Uh, alright...?"
            "Tentatively, he peers down inside."
            "He lets out a sharp laugh when he sees the stash of condoms there."
            s3_li @ surprised "That's certainly not what I was expecting to see."
            s3_li cheeky "Are you trying to send me a message?"
            if s3_li == "Bill":
                s3_li "Because I already told you, I don't do subtlety."
            s3_mc "I'm not trying to say anything."
            s3_mc "I'm just a girl with a top full of condoms, and I thought you ought to know."
            s3_mc "Seeing as we're being honest with each other right now."
            s3_li @ smile "Amazing."

    s3_li @ surprised "Well, I guess the others must be wondering where we've got to."
    s3_li "Let's head over for the challenge!"

    # CHOICE
    menu:
        s3_mc "We should go and meet the others at the challenge platform..."
        "Yep, let's go":
            s3_mc "I hope they haven't started without us!"
        "Race you!":
            s3_mc "Last one there has to clean the pool!"
            s3_li @ surprised "Wait, wh..."
            "You're already off and running."
            "Seconds later, you hear him laugh, then the sound of his bare feet on the grass as he gives chase."
        "Why don't you carry me?":
            s3_li @ surprised "Carry you?"
            s3_mc "That's what I said."
            s3_mc "You can do it, right? Or are these muscles just for show?"

            if s3_li == "Harry":
                harry awkward "Muscles?"
                "He looks down at his arms and gives them an optimistic flex."
            else:
                s3_li smile "He smirks and flexes his impressives arms."

            s3_li neutral "Of course I can do it. Just watch."

            if s3_li == "Harry":
                "He stretches a bit more, positions himself carefully, then scoops you up in his arms."
                "He's stronger than he looks."
            "He puts one hand on your back, scoops the other under your legs, and effortlessly sweeps you off your feet."
            s3_li cheeky "To the challenge platform, m'lady?"
            s3_mc " To the challenge platform at once!"
            "He sets off, carrying you bridal-style across the lawn."
            
    scene sand with dissolve
    $ on_screen = []

    "It's only day 1, and [s3_name] is already turning heads all over the Villa!"
    # IF STATEMENT
    if s3e1p1_cheeky_snog == True:
        "I think that snog might be one for the record books."
        "Five minutes from first sight to first kiss?"
        "The other girls will never catch up!"
    "She's coupled up with [s3_li] for now, but who knows what could happen at this afternoon's challenge?"

    elladine @ smile "We've got to kiss the boy we think the clue is about."

    show elladine at npc_exit
    pause 0.3
    $ renpy.hide("elladine")

    # IF STATEMENT
    if s3_li == "Bill":
        show genevieve at npc_center
        genevieve @ surprised "I can't believe how big that is..."
        show genevieve at npc_exit
        pause 0.3
        $ renpy.hide("genevieve")
    elif s3_li == "Camilo" or s3_li == "Harry":
        show miki at npc_center
        miki @ surprised "I can't believe how big that is..."
        show miki at npc_exit
        pause 0.3
        $ renpy.hide("miki")

    jump s3e1p2

    return

# LABELS FOR s3e1p1
label s3e1p1_meet_miki:

    miki happy "Hi everyone! It's so exciting to be here!"

    # solo profile shot of miki
    window hide
    show screen s3_character_profile("miki") with Pause(3)
    hide screen s3_character_profile with dissolve

    "{i}Miki\n
    -21, from Cambringe\n
    -Lifestyle vlogger\n
    -Loves it when you smash that subscribe button{/i}"

    miki "I mean, this is Island Amore, where dreams come true, right?"
    nicky @ surprised "Told you so."
    miki @ surprised "At first I was like, what happens if I totally don't like any of the boys who are left?"
    miki cheeky "But now I see the two beautiful boys you've left for me to choose from..."
    miki "I don't know why I was worried."
    "Her eyes linger on Bill."
    miki "What's your name, handsome?"
    bill cheeky "I'm Bill. Pleased to meet you, love."
    miki "You seem like a rugged, down-to-earth kind of guy, Bill."
    miki smile "And they say opposites attract."
    miki "Fancy being coupled up with an offbeat, creative type like me?"
    bill smile "I'm not exactly going to say no, am I?"
    bill @ happy "Beautiful girl asks if you want to couple up, you say yes. Basic common sense, isn't it."
    "She laughs."
    miki @ happy "I'll take that as a yes."
    "She takes his hand. Together, they walk back to you and the others."

    return

label s3e1p1_meet_iona:
    "A new girl emerges from the Villa. Everyone falls silent."
    iona happy "Good morning, Island Amore!"
    iona neutral "I don't know about the rest of you, but I'm about ready to do something wild."

    # solo profile shot of iona
    window hide
    show screen s3_character_profile("iona") with Pause(3)
    hide screen s3_character_profile with dissolve

    "{i}Iona\n
    -23, from Aberdeen\n
    -Apprentice pylon rigger\n
    -Spends all day making sparks fly{/i}"

    camilo cheeky "You don't mess around, do you?"
    iona "I certainly don't, babe."
    iona cheeky "Is that going to be a problem?"
    camilo smile "Not at all."
    camilo "In fact, I think it's going to be the opposite of a problem."
    iona @ happy "Well, now I just have to couple up with you, don't I?"
    "Iona smirks and walks over to him."
    "He gives her a little salsa-style spin and she laughs."
    "They stride over to stand beside you."

    return

label s3e1p1_meet_genevieve:
    "The door opens one last time, and everyone turns to look as another girl struts out onto the lawn."
    genevieve happy "Hello, darlings."
    genevieve smile "How are we all doing?"

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
    genevieve @ cheeky "What's your name, sweetie?"
    harry "Sweetie."
    harry @ blush "Er, I mean..."
    harry smile "Harry. It's Harry."
    genevieve "Lovely to meet you, Harry."
    genevieve @ cheeky "How lucky am I that nobody got to you before me?"
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

    s3_li "Obviously we've only really got a first impression to go on at the moment."
    s3_li @ cheeky "But I already feel like you're exactly my type on paper."
    show s3_li at npc_exit
    pause 0.3
    $ renpy.hide("s3_li")

    "Well, almost everyone."
    show aj at npc_center
    aj blush "Don't you think it's a bit early to say whether our couples are great or not?"
    show aj at npc_exit
    pause 0.3
    $ renpy.hide("aj")

    "It's early days, AJ, early days."
    "But you know what they say..."
    "The early bird catches the worm."

    # IF STATEMENT
    if s3e1p1_cheeky_snog:
        "Or in this case, [s3_name] and [s3_li] get smooching!"
        if s3_li == "Bill":
            show bill at npc_center
            bill smile "Cor"
            show bill at npc_exit
            pause 0.3
            $ renpy.hide("bill")
        elif s3_li == "Camilo":
            show camilo at npc_center
            camilo smile "Blimey"
            show camilo at npc_exit
            pause 0.3
            $ renpy.hide("camilo")
        elif s3_li == "Harry":
            show harry at npc_center
            harry smile "Gosh"
            show harry at npc_exit
            pause 0.3
            $ renpy.hide("harry")
        "Well said, [s3_li]."

    "Coming up..."
    "The Islander get hands-on with each other's excess baggage."
    
    show aj at npc_center
    aj surprised "What gave it away?"
    show aj at npc_exit
    pause 0.3
    $ renpy.hide("aj")

    "And one clue doesn't add up..."

    show bill at npc_center
    bill sad "I have no idea who this is about."
    show bill at npc_exit
    pause 0.3
    $ renpy.hide("bill")

    scene s3-platform-excess-baggage with dissolve
    $ on_screen = []

    "You and [s3_li] make your way over to the platform where the other Islanders have already gathered."

    elladine smile "There you are..."

    # IF STATEMENT
    if s3e1p1_cheeky_snog:
        "Elladine points at your lips."
        elladine @ blush "You've smudged your lipstick, hun. It's on your cheek."
        "You quickly wipe at your cheek. [s3_li] laughs a little."
        if s3_li == "Bill":
            bill @ cheeky "Cheeky."
        elif s3_li == "Camilo":
            camilo @ cheeky "Cheeky."
        elif s3_li == "Harry":
            harry @ cheeky "Cheeky."

    "Everyone is standing around some suitcase on a carousel."
    bill @ surprised "Those spinny things make me feel dizzy at airports."
    harry @ surprised "I always want to lie on them and just go round and round."
    harry blush "They look kinda comfy and you're always exhausted by the time you get to them."
    elladine @ surprised "I got a text."
    elladine smile "Ooh, it's the rules of the challenge!"
    elladine neutral "We're starting first."
    elladine "In each suitcase we'll find a secret clue about one of the guys..."
    elladine @ surprised "Then we kiss the guy who we think the clue's about!"
    elladine "The guy who matches the clue steps forward and we'll see if we snogged the right person."
    elladine "Then it'll be the guys' turn."
    
    # IF STATEMENT
    if s3_li == "Harry":
        miki @ surprised "So, do we actually have to kiss who we think the clue is about?"
        miki @ cheeky "Or can we just use this as a way to kiss someone we think is hot?"
        elladine @ blush "Well, you wouldn't win the game..."
        miki @ cheeky "But you'd get to snog someone you like."
    elif s3_li == "Camilo" or s3_li == "Bill":
        genevieve @ surprised "So, do we actually have to kiss who we think the clue is about?"
        genevieve @ cheeky "Or can we just use this as a way to kiss someone we think is hot?"
        elladine @ blush "Well, you wouldn't win the game..."
        genevieve @ cheeky "But you'd get to snog someone you like."
    
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
    "[s3_li] coughs, looking at you."
    # IF STATEMENT
    if s3_li == "Bill":
        bill blush "You alright, [s3_name]?"
    elif s3_li == "Camilo":
        camilo blush "You alright, [s3_name]?"
    elif s3_li == "Harry":
        harry blush "You alright, [s3_name]?"

    elladine blush "Yeah, you look a little farway."
    thought "Oops, I just got lost in thought."
    s3_mc "It's nothing."

    # CHOICE
    menu:
        s3_mc "I can't wait to..."
        "Find out the gossip about the boys":
            aj happy "Same, we've got to find out all the dirt."
        "Win this challenge!":
            elladine @ surprised "There are no losers or winners in this challenge!"
            elladine neutral "We're just getting to know each other."
            "You and Harry groan."
            harry serious "What's the point in that then?"

            # IF STATEMENT
            if s3_li == "Bill" or s3_li == "Harry":
                iona @ smile "You might get a lot of kisses."
            elif s3_li == "Camilo":
                genevieve @ smile "You might get a lot of kisses."
            harry smile "Oh, OK."
            harry @ cheeky "That doesn't sound too bad."
        "Just kiss some dudes":
            # IF STATEMENT
            if s3_li == "Bill":
                genevieve smile "I feel you hun."
                genevieve @ happy "Can't wait to get some action in here!"
            elif s3_li == "Harry" or s3_li == "Camilo":
                miki smile "I feel you hun."
                miki @ happy "Can't wait to get some action in here!"

    # IF STATEMENT
    if s3_li == "Bill":
        genevieve @ cheeky "I'm just going to kiss whoever I think is the fittest."
        elladine @ smile "Right, let's get started!"
        elladine "Iona, can you do the honours?"
        "Iona rushes to the conveyor belt and grabs a suitcase."
        "She wheels it over to the girls and quickly unzips it."
        iona "OK, the clue is..."
        iona "'This boy once woke up spooning a badger...'"
        "The boys look at each other puzzled while the girls huddle closer together."
        aj @ smile "That sounds adorable!"
        elladine @ sad "It sounds scary! Badgers will mess you up."
        iona @ sad "How do you even end up in that situation?"
        genevieve "I bet it was a prank by his mates."
    elif s3_li == "Camilo":
        genevieve @ cheeky "I'm just going to kiss whoever I think is the fittest."
        elladine @ smile "Right, let's get started!"
        elladine "Miki, can you do the honours?"
        "Miki rushes to the conveyor belt and grabs a suitcase."
        "She wheels it over to the girls and quickly unzips it."
        miki @ smile "OK, the clue is..."
        miki "'This boy once woke up spooning a badger...'"
        "The boys look at each other puzzled while the girls huddle closer together."
        aj @ smile "That sounds adorable!"
        elladine @ sad "It sounds scary! Badgers will mess you up."
        genevieve @ sad "How do you even end up in that situation?"
        miki "I bet it was a prank by his mates."
    elif s3_li == "Harry":
        miki @ cheeky "I'm just going to kiss whoever I think is the fittest."
        elladine @ smile "Right, let's get started!"
        elladine "Iona, can you do the honours?"
        "Iona rushes to the conveyor belt and grabs a suitcase."
        "She wheels it over to the girls and quickly unzips it."
        iona @ smile "OK, the clue is..."
        iona "'This boy once woke up spooning a badger...'"
        "The boys look at each other puzzled while the girls huddle closer together."
        aj @ smile "That sounds adorable!"
        elladine @ sad "It sounds scary! Badgers will mess you up."
        iona @ sad "How do you even end up in that situation?"
        miki "I bet it was a prank by his mates."

    elladine @ surprised "That's a terrible idea all round."
    aj @ surprised "But which one of these guys do you think it is?"

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
    if s3_li == "Bill" or s3_li == "Camilo":
        genevieve @ smile "I agree with [s3_name]."
        genevieve "There's something about [s3e1p2_spooned_a_badger] that makes me imagine him waking up next to a badger."
    elif s3_li == "Harry":
        miki @ smile "I agree with [s3_name]."
        miki "There's something about [s3e1p2_spooned_a_badger] that makes me imagine him waking up next to a badger."
    
    elladine @ smile "So, we've decided it's [s3e1p2_spooned_a_badger]?"
    s3_mc "I think so, yeah."
    aj @ surprised "So who wants to go kiss him?"

    # IF STATEMENT
    if s3e1p2_spooned_a_badger == "Nicky" or s3e1p2_spooned_a_badger == "Seb":
        elladine @ cheeky "Yeah, go on. I will."
        "Elladine kisses [s3e1p2_spooned_a_badger] on the lips. She leans in for a deep and romantic kiss."
    else:
        # CHOICE
        menu:
            thought "Should I volunteer to kiss [s3e1p2_spooned_a_badger]?"
            "No thanks, he's not my type":
                $ s3e1p2_challenge_kiss = False
                s3_mc "He's not for me."
                # IF STATEMENT
                if s3_li == "Bill" or s3_li == "Camilo":
                    elladine @ surprised "Genevieve, you should kiss [s3e1p2_spooned_a_badger]."
                    aj @ surprised "Yeah, you've dealt with these types before."
                    genevieve @ smile "Sure, sure."
                    "Genevieve kisses [s3e1p2_spooned_a_badger] on the lips."
                else:
                    elladine @ blush "I'll take one for the team."
                    "She kisses him."
            "Go on then, it's only a game":
                $ s3e1p2_challenge_kiss = True
                $ s3_mc.like(s3e1p2_spooned_a_badger)
                s3_mc "I'll do it."
                s3_mc "I'll kiss him."
                # IF STATEMENT
                if s3_li == "Bill" or s3_li == "Harry":
                    iona @ happy "Go on, [s3_name]!"
                elif s3_li == "Camilo":
                    genevieve @ happy "Go on, [s3_name]!"
                "You wander over to [s3e1p2_spooned_a_badger]."
                # IF STATEMENT
                if s3e1p2_spooned_a_badger == "Bill":
                    bill cheeky "Alright?"
                elif s3e1p2_spooned_a_badger == "Camilo":
                    camilo cheeky "Alright?"
                elif s3e1p2_spooned_a_badger == "Harry":
                    harry cheeky "Alright?"
                "You kiss [s3e1p2_spooned_a_badger] firmly on the lips."
                "It's tender yet urgent."
                "As you pull away he whispers in your ear."
                # IF STATEMENT
                if s3e1p2_spooned_a_badger == "Bill":
                    bill smile "You're a really good kisser."
                elif s3e1p2_spooned_a_badger == "Camilo":
                    camilo smile "You're a really good kisser."
                elif s3e1p2_spooned_a_badger == "Harry":
                    harry smile "You're a really good kisser."                
                "You blush a little and go back to the girls."
            "Do I have to stop at kissing him?":
                $ s3e1p2_challenge_kiss = True
                $ s3_mc.like(s3e1p2_spooned_a_badger)
                s3_mc "Let me at him."
                # IF STATEMENT
                if s3e1p2_spooned_a_badger == "Bill":
                    "You stride over to [s3e1p2_spooned_a_badger] and kiss him hard on his lips. You grind your body against his."
                    bill @ surprised "Woah!"
                    genevieve @ happy "Woop! Go girl."
                    "You finally pull away. He looks stunned as he wipes his brow."
                    bill cheeky "You're seriously a hot kisser."
                elif s3e1p2_spooned_a_badger == "Camilo":
                    "You stride over to [s3e1p2_spooned_a_badger] and kiss him hard on his lips. You grind your body against his."
                    camilo @ surprised "Woah!"
                    miki @ happy "Woop! Go girl."
                    "You finally pull away. He looks stunned as he wipes his brow."
                    camilo cheeky "You're seriously a hot kisser."
                elif s3e1p2_spooned_a_badger == "Harry":
                    "You stride over to [s3e1p2_spooned_a_badger] and kiss him hard on his lips. You grind your body against his."
                    harry @ surprised "Woah!"
                    miki @ happy "Woop! Go girl."
                    "You finally pull away. He looks stunned as he wipes his brow."
                    harry cheeky "You're seriously a hot kisser."
                s3_mc "Thanks, babe."
                "You stride back over to the girls."
                aj @ happy "Go [s3_name]!"
                elladine @ happy "Now that's how you go from G to D."

    elladine @ surprised "Ok, so whoever woke up to a terrifying bed companion..."
    elladine neutral "Please step forward!"
    "The boys all look at each other."
    "Nicky steps forward."
    elladine @ surprised "Nicky!"

    # IF STATEMENT
    if s3e1p2_spooned_a_badger == "Nicky":
        nicky blush "How'd you know it was me?"
    else:
        aj @ sad "Argh, Nicky? I wouldn't have known."
        nicky @ smile "I mean, there's not much of a giveaway for that."
        # IF STATEMENT
        if s3e1p2_spooned_a_badger == "Bill":
            bill @ surprised "Why'd you think it was me?"
        elif s3e1p2_spooned_a_badger == "Camilo":
            camilo @ surprised "Why'd you think it was me?"
        elif s3e1p2_spooned_a_badger == "Harry":
            harry @ surprised "Why'd you think it was me?"
        elif s3e1p2_spooned_a_badger == "Seb":
            seb @ surprised "Why'd you think it was me?"
        aj blush "I don't know! I could just see you spooning a badger is all."

    bill @ surprised "Mate, how'd you end up with a badger?"
    nicky neutral "OK, so first off, it was a baby badger that had clearly got lost."
    nicky "It had been a really cold night, so it must have somehow got into my flat and found something warm to cuddle up to."
    nicky @ smile "Me."
    aj @ surprised "So what did you do?"
    nicky @ smile "Handed it over to a local animal charity who would try to reunite it with its parents."
    nicky "Though it didn't stop clinging to me until they arrived..."
    camilo @ happy "Cute!"

    # IF STATEMENT
    if s3_li == "Bill" or s3_li == "Harry":
        iona "Adorable, but moving on..."
        iona @ cheeky "[s3_name], why don't you go and get the next suitcase?"
    elif s3_li == "Camilo":
        miki @ smile "Adorable, but moving on..."
        miki "[s3_name], why don't you go and get the next suitcase?"


    "You head over to the carousel where suitcases are going round and round, and grab one."
    aj @ happy "Bring it over, [s3_name]!"
    "You pop the case open. Inside is a label which says..."

    # IF STATEMENT
    if s3_li == "Bill":
        s3_mc "'This boy got caught having sex in his mum's wardrobe.'"
        aj @ surprised "Woah."
        genevieve @ cheeky "Filthy."
    elif s3_li == "Camilo":
        s3_mc "'This boy got caught having sex at work.'"
        aj @ surprised "Woah."
        genevieve @ cheeky "Filthy."
    elif s3_li == "Harry":
        s3_mc "'This boy got caught having sex on a roof by someone flying a drone.'"
        aj @ surprised "Woah."
        miki @ cheeky "Filthy."
    
    elladine blush "I reckon that's something Seb would do."
    aj blush "Or maybe it's [s3_li]..."

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
        if s3_li == "Bill" or s3_li == "Harry":
            iona "OK, I'll go and kiss them."
            "Iona saunters over plants a kiss on his lips."
            seb blush "Thank you for that."
            "Iona smiles."
            iona @ happy "Any day"
        elif s3_li == "Camilo":
            genevieve @ smile "OK, I'll go and kiss them."
            "Genevieve saunters over plants a kiss on his lips."
            seb blush "Thank you for that."
            "Genevieve smiles."
            genevieve @ smile "Any day"
    elif s3e1p2_caught_having_sex == "Nicky":
        if s3_li == "Bill" or s3_li == "Harry":
            iona "OK, I'll go and kiss them."
            "Iona saunters over plants a kiss on his lips."
            nicky @ smile "Thank you for that."
            "Iona smiles."
            iona @ happy "Any day"
        elif s3_li == "Camilo":
            genevieve @ smile "OK, I'll go and kiss them."
            "Genevieve saunters over plants a kiss on his lips."
            nicky @ smile "Thank you for that."
            "Genevieve smiles."
            genevieve @ smile "Any day"
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
                    if s3_li == "Bill" or s3_li == "Harry":
                        iona @ happy "Check out [s3_name] getting all the kisses..."
                        iona "You go, babe."
                    elif s3_li == "Camilo":
                        genevieve @ happy "Check out [s3_name] getting all the kisses..."
                        genevieve smile "You go, babe."
                    s3_mc "Thanks hun!"
                    "You blow all the girls a kiss. They all laugh."
            "Nah, let one of the other girls":
                # IF STATMENT
                if s3_li == "Bill":
                    genevieve @ smile "I'll kiss him!"
                    "Genevieve walks over and kisses [s3e1p2_caught_having_sex] quickly."
                    genevieve @ happy "Thank you, next!"
                elif s3_li == "Camilo" or s3_li == "Harry":
                    miki @ smile "I'll kiss him!"
                    "Miki walks over and kisses [s3e1p2_caught_having_sex] quickly."
                    miki @ happy "Thank you, next!"

    iona @ surprised "Would the guy getting sweaty and sexy in the weird places please come forward?"
    s3_mc "Did I get it right?"
    "[s3_li] steps forward."

    # IF STATEMENT
    if s3_li == "Bill" and s3e1p2_caught_having_sex == "Bill":
        bill @ smile "Yeah, you did, hun."
    elif s3_li == "Camilo" and s3e1p2_caught_having_sex == "Camilo":
        camilo @ smile "Yeah, you did, hun."
    elif s3_li == "Harry" and s3e1p2_caught_having_sex == "Harry":
        harry @ smile "Yeah, you did, hun."
    elif s3_li != s3e1p2_caught_having_sex:
        if s3_li == "Bill":
            bill blush "Nope. It was me."
        elif s3_li == "Camilo":
            camilo blush "Nope. It was me."
        elif s3_li == "Harry":
            harry blush "Nope. It was me."
        
        s3_mc "Aw, I didn't get it right!"

        if s3e1p2_caught_having_sex == "Bill":
            bill blush "I can't believe you thought it was me."
        elif s3e1p2_caught_having_sex == "Camilo":
            camilo blush "I can't believe you thought it was me."
        elif s3e1p2_caught_having_sex == "Harry":
            harry blush "I can't believe you thought it was me."
        elif s3e1p2_caught_having_sex == "Nicky":
            nicky blush "I can't believe you thought it was me."
        elif s3e1p2_caught_having_sex == "Seb":
            seb blush "I can't believe you thought it was me."

    # IF STATEMENT
    if s3_li == "Bill":
        aj @ surprised  "Why did you have sex in the wardrobe?"
        aj "Aren't there like coat hangers and stuff?"
        bill blush "I was having a house party and there was zero privacy."
        aj @ blush "Please say your mum didn't catch you."
        bill @ surprised "No, no."
        bill neutral "She actually has no idea that it happened."
        genevieve blush "Until now."
        bill "Oh yeah..."
        bill blush "Awks..."
    elif s3_li == "Camilo":
        camilo @ surprised "It was closed, OK? And like, I work at my parents' shop so it's basically my shop so it's basically my second house. It would have been fine..."
        camilo "But my dad still believes in getting milk in glass bottles, you know, to save the planet."
        camilo cheeky "And, like, after closing up me and this girl decided to get down and dirty on these boxes..."
        camilo "Heat of the moment, like..."
        camilo blush "But then the next thing I know a whole crate of these milk bottles have smashed and there is milk everywhere."
        harry @ surprised "Remind me never to buy anything from your shop, like, ever."
    elif s3_li == "Harry":
        harry @ surprised "We were up on the roof, getting into it, and then I hear this buzzing sound..."
        harry @ surprised "And there's this drone up there!"
        harry "So I threw my shoe at it."
        aj @ surprised "Wait, what about the pilot? You could have hurt someone!"
        harry "Drones don't have pilots, AJ. They're only small."
        aj blush "Oh, right..."
        harry "And besides, it was breaking the law!"
        harry serious "You shouldn't fly them around built up areas."
        elladine smile "Right, speaking of laws, what were you doing up on a roof?"
        harry cheeky "Just checking out the sights of the city from a different angle."

    # IF STATEMENT
    if s3_li == "Bill" or s3_li == "Camilo":
        genevieve "Moving swiftly on..."
        genevieve @ surprised "I'll go next."
        "Genevieve grabs another suitcase and reads out the clue."
        genevieve "'This boy rescued a cat from a burning tree.'"
    elif s3_li == "Harry":
        miki "Moving swiftly on..."
        miki @ surprised "I'll go next."
        "Miki grabs another suitcase and reads out the clue."
        miki "'This boy rescued a cat from a burning tree.'"

    aj @ surprised "Woah, how many cats get stuck up burning trees?"

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
        aj @ surprised "Yeah, me too."
        aj "I'll take this one."
        "AJ jogs over to [s3e1p2_rescue_cat] and kisses him, stroking his hair a little."
        aj @ cheeky "Meow."
    else:
        # CHOICE
        menu:
            thought "Should I go and kiss [s3e1p2_rescue_cat]?"
            "Yes! Kiss him all over":
                $ s3_mc.like(s3e1p2_rescue_cat)
                "You rush over to [s3e1p2_rescue_cat] and smother him in kisses all over his body."
                s3_mc "You're just so kissable."
                "The girls and guys all cheer."
                camilo @ cheeky "Woah."
                # IF STATEMENT
                if s3e1p2_challenge_kiss:
                    if s3_li == "Bill":
                        genevieve @ happy "[s3_name] is at it again!"
                    elif s3_li == "Camilo" or s3_li == "Harry":
                        miki @ smile "[s3_name] is at it again!"
            "Nah, I don't want to":
                if s3_li == "Bill" or s3_li == "Harry":
                    iona "I think it's Seb."
                    iona "I'm kissing him."
                    "Iona runs over to Seb and kisses him."
                    iona @ cheeky "Am I right?"
                elif s3_li == "Camilo":
                    genevieve @ surprised "I think it's Seb."
                    genevieve @ blush "I'm kissing him."
                    "Genevieve runs over to Seb and kisses him."
                    genevieve @ cheeky "Am I right?"
            "Just a quick peck will do":
                "You walk over to [s3e1p2_rescue_cat] and gently kiss him."
                if s3e1p2_challenge_kiss:
                    if s3_li == "Bill":
                        genevieve @ happy "[s3_name] is at it again!"
                    elif s3_li == "Camilo" or s3_li == "Harry":
                        miki @ cheeky "[s3_name] is at it again!"

    # IF STATEMENT
    if s3_li == "Bill" or s3_li == "Camilo":
        genevieve "OK, can the man who risked his nine lives for a cat please come forward!"
    elif s3_li == "Harry":
        iona "OK, can the man who risked his nine lives for a cat please come forward!"

    "Seb steps forward."
    seb blush "Yeah, it was me. I saved the cat."

    # IF STATEMENT
    if s3e1p2_rescue_cat == "Seb":
        seb smile "[s3_name] and AJ were right."

    elladine @ happy "That's so brave of you Seb."
    seb neutral "We were camping in the middle of nowhere and had just built our campfire."
    seb "A stray cat climbed the tree next to us."
    seb @ surprised "Then suddenly the wind picked up and the tree caught fire!"
    seb @ smile "So I climbed up and caught the cat."

    # CHOICE
    menu:
        thought "Whoa, Seb saved a cat from a burning tree!"
        "That's so brave":
            s3_mc "That's so brave, Seb!"
            seb cheeky "Thanks, [s3_name]."
        "He's foolish":
            thought "He could have gotten hurt!"
            s3_mc "He should have waited for the emergency services."
        "Seb clearly loves cats":
            s3_mc "Oh, you must love cats then to risk your life for them."
            seb @ happy "Yeah, cats are pretty awesome."

    aj @ talk "Once there was a fire in my dad's kitchen and we were all panicking and trying to find the cats to make sure they were safe..."
    aj @ blush "And we found them just stretching out on the floor in my bedroom, directly above where the fire was."
    seb @ smile "Cats are always proper dedicated to finding a warm spot."

    # IF STATEMENT
    if s3_li == "Bill":
        genevieve "Or..."
        genevieve @ happy "They started the fire to create the warm spot..."
        iona "OK, OK, enough cat talk."
        iona "Final clue girls. Then it's the boy's turn to do the kissing."
        "The boys cheer excitedly."
        iona "[s3_name], you can go and pick another one."
    elif s3_li == "Camilo":
        genevieve "Or..."
        genevieve @ happy "They started the fire to create the warm spot..."
        miki "OK, OK, enough cat talk."
        miki "Final clue girls. Then it's the boy's turn to do the kissing."
        "The boys cheer excitedly."
        miki "[s3_name], you can go and pick another one."
    elif s3_li == "Harry":
        miki "Or..."
        miki @ happy "They started the fire to create the warm spot..."
        iona "OK, OK, enough cat talk."
        iona "Final clue girls. Then it's the boy's turn to do the kissing."
        "The boys cheer excitedly."
        iona "[s3_name], you can go and pick another one."

    "You run over to the suitcases and grab one."
    aj @ talk "What's the clue, [s3_name]?"

    # IF STATEMENT
    if s3_li == "Bill":
        s3_mc "'This boy asked a girl out by making her a plate of heart shaped sandwiches!'"
        aj @ smile "Aw, that's actually a really sweet one."
    elif s3_li == "Camilo":
        s3_mc "'This boy once flew a date to Rome!'"
        aj @ smile "Wow, that's so exciting!"
    elif s3_li == "Harry":
        s3_mc "'This boy once serenaded a girl with a ukulele wearing nothing but a tie.'"
        aj @ smile "Aw, that's actually kinda hilarious and sweet all rolled into one."

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
    if s3_li == "Bill" or s3_li == "Harry":
        iona @ happy "Aw, yeah."
        iona "He's a cutie."
    elif s3_li == "Camilo":
        miki @ smile "Aw, yeah."
        miki "He's a cutie."

    # IF STATEMENT
    if s3e1p2_asked_girl_out == "Nicky" or s3e1p2_asked_girl_out == "Seb":
        if s3_li == "Bill" or s3_li == "Harry":
            iona "I'll kiss [s3e1p2_asked_girl_out]!"
            "Iona kisses [s3e1p2_asked_girl_out] on the nose."
            iona @ smile "Such a cutie."
        elif s3_li == "Camilo":
            genevieve "I'll kiss [s3e1p2_asked_girl_out]!"
            "Genevieve kisses [s3e1p2_asked_girl_out] on the nose."
            genevieve @ smile "Such a cutie."
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
                if s3_li == "Bill" or s3_li == "Harry":
                    iona "I'll kiss [s3e1p2_asked_girl_out]!"
                    "Iona kisses [s3e1p2_asked_girl_out] on the nose."
                    iona @ smile "Such a cutie."
                elif s3_li == "Camilo":
                    genevieve "I'll kiss [s3e1p2_asked_girl_out]!"
                    "Genevieve kisses [s3e1p2_asked_girl_out] on the nose."
                    genevieve @ smile "Such a cutie."

    # IF STATEMENT
    if s3_li == "Bill":
        iona "Will the hopeless romantic please step forward?"
        "Bill steps forward."
        iona @ surprised "It's Bill!"
        # IF STATEMENT
        if s3e1p2_asked_girl_out == "Bill":
            thought "I guessed that right!"
        else:
            nicky @ smile "That's so sweet, man."
        bill cheeky "You can never go wrong with a good sandwich."
        bill blush "Only problem is that she hated mayo and I had put it in every one."
        bill "I had them for my lunch in the end."
        nicky happy "Nothing says love like mayo, to be fair."
    elif s3_li == "Camilo":
        genevieve "Will the hopeless romantic please step forward?"
        "Camilo steps forward."
        genevieve @ surprised "It's Camilo!"
        # IF STATEMENT
        if s3e1p2_asked_girl_out == "Camilo":
            camilo cheeky "[s3_name] knows me so well already."
        else:
            harry smile "That's so sweet, man."
            miki @ cheeky "Yeah, you're a real cutie."
    elif s3_li == "Harry":
        iona "Will the hopeless romantic please step forward?"
        "Harry steps forward."
        iona @ surprised "It's Harry!"
        # IF STATEMENT
        if s3e1p2_asked_girl_out == "Harry":
            thought "I knew it!"
        else:
            elladine happy "Harry! That's hilarious."
        harry blush "Yeah, I really can't even play the uke very well but I thought, like, why not."
        bill sad "And the tie was essential?"
        seb cheeky "But the clothes weren't..."
        harry cheeky "You've got to look smart, even in the nude."

    elladine @ suprised "Right now, it's the boys' turn to find out some secrets about the girls!"
    elladine "Everyone switch sides."
    "The girls all line up. Seb runs up and grabs a suitcase."
    seb @ suprised "OK..."
    seb "'This girl once cooked breakfast in bed for a guy she had just met..."
    seb @ blush "...and set his kitchen on fire.'"
    camilo @ blush "Oh, wow."
    seb "'...And then didn't call him back.'"

    # CHOICE
    menu:
        thought "Have I ever set fire to a boy's kitchen and not called him back?"
        "No! That's terrible":
            $ s3e1p2_set_fire = False
        "Oops, yeah, that's about me!":
            $ s3e1p2_set_fire = True

    seb "I reckon, that's..."

    # IF STATEMENT
    if s3_li == "Bill" or s3_li == "Harry":
        seb "Iona."
        "Seb jogs over and kisses her."
        seb @ cheeky "She seems like the fire starting type."
        "Iona crosses her arms and rolls her eyes."
        iona angry "Mate, part of my job is avoiding fires."
        bill @ blush "Is that even a type that, like, people have?"
        aj "It wouldn't work on paper."
        iona neutral "Can the fire starter please step forward..."
    elif s3_li == "Camilo":
        seb "Elladine."
        "Seb jogs over and kisses her."
        seb "She seems like the fire starting type."
        "Elladine gasps."
        camilo @ blush "Is that even a type that, like, people have?"
        genevieve @ surprised "Can the fire starter please step forward..."

    # IF STATEMENT
    if s3e1p2_set_fire:
        "You step forward."
        if s3_li == "Bill" or s3_li == "Harry":
            iona @ surprised "[s3_name]!"
        elif s3_li == "Camilo":
            genevieve @ surprised "[s3_name]!"
        aj @ surprised "Woah, [s3_name]. That's intense."
        s3_mc "Yeah, it was so embarrassing. All I wanted to do was make him breakfast in bed."
        s3_mc "No one got hurt."
        s3_mc "Just my pride..."
        s3_mc "And his kitchen cupboards."
    else:
        "Elladine steps forward."
        if s3_li != "Harry":
            genevieve @ surprised "Elladine!"
        else:
            iona @ surprised "Elladine!"
        elladine sad "Yeah, it was an accident, obviously. I was trying to make him a nice fry up."
        elladine @ surprised "I knocked this kitchen roll off the top shelf and it got caught in the toaster."
        elladine serious "No one got hurt thankfully, but yeah, I never called him back after that."
        elladine sad "I was way too embarrassed."

    # IF STATEMENT
    if s3_li == "Bill" or s3_li == "Harry":
        iona "OK boys, next clue."
    elif s3_li == "Camilo":
        genevieve "OK boys, next clue."

    "Nicky picks up a suitcase."
    nicky "Let's see what we've got here."
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

    nicky smile "I've got a sneaky suspicion that this secret is about..."
    "He walks over to AJ and kisses her on the lips."
    "As he walks back, AJ grins."
    aj @ surprised "What gave it away?"
    nicky neutral "I'm not sure, but I definitely get a vibe."
    nicky @ happy "I've got a good feel for these things."

    if s3_li != "Harry":
        genevieve "Surely you can't tell someone's relationship history just from looking at them."
    else:
        miki "Surely you can't tell someone's relationship history just from looking at them."

    aj cheeky "You'd be surprised."
    
    # IF STATEMENT
    if s3_mc.bisexual == True:
        $ s3_mc.like("AJ")
        "AJ winks at you."
        if s3_li == "Bill":
            genevieve @ surprised "Wait, what was that?"
        elif s3_li == "Camilo" or s3_li == "Harry":
            miki @ surprised "Wait, what was that?"
        s3_mc "A code for girls who like girls."
        s3_mc "It's like a secret handshake that we have."
        aj surprised "There's a secret handshake? Why wasn't I told?"
        if s3_li == "Bill":
            s3_mc "Ssh, don't give away that it's fake. We've got to keep Genevieve on her toes."
        elif s3_li == "Camilo" or s3_li == "Harry":
            s3_mc "Ssh, don't give away that it's fake. We've got to keep Miki on her toes."

    # IF STATEMENT
    if s3_li == "Bill" or s3_li == "Harry":
        iona @ happy "Good guess, Nicky."
    elif s3_li == "Camilo":
        genevieve @ smile "Good guess, Nicky."

    elladine @ surprised "Next boy, grab a case!"
    "Camilo runs over and picks up a case."

    # IF STATEMENT
    if s3_li == "Bill":
        camilo @ smile "'This girl took a job as a waitress to escape a blind date.'"
        thought "Have I taken a job as a waitress to escape a blind date?"
    elif s3_li == "Camilo" or s3_li == "Harry":
        camilo @ cheeky "'This girl did a sexy birthday striptease for a guy...'"
        camilo blush "'Only to be interrupted by his family, who had flown in to surprise him!'"
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
    if s3_li == "Bill" or s3_li == "Harry":
        camilo "I reckon this is..."
        camilo neutral "Elladine!"
        "He goes over to Elladine and kisses her."
    elif s3_li == "Camilo":
        camilo "I reckon this is..."
        camilo neutral "[s3_name]!"
        "He runs over to you."
        camilo cheeky "Mind if I kiss you, [s3_name]?"
        # CHOICE
        menu:
            thought "Do I mind if Camilo kisses me?"
            "Sure, go for it":
                $ s3_mc.like("Camilo")
                "He puts a hand behind your head and draws you in close."
                "He tenderly kisses the bottom of your lip."
            "Nah, I'd rather you didn't":
                camilo neutral "That's fine! But just so everyone knows, I think this is about [s3_name]!"
                "He walks back to the others."

    elladine @ surprised "Would the girl please step forward!"
    
    # IF STATEMENT
    if s3e1p2_camilos_clue:
        "You step forward."
        if s3_li == "Bill":
            "Genevieve also steps forward."
            genevieve smile "Aw! Babe, what a coincidence!"
        elif s3_li == "Camilo" or s3_li == "Harry":
            "Miki also steps forward."
            miki smile "Oh my god, hun! We're so similar."
        s3_mc "Ha! Yeah..."
        s3_mc "I guess it could happen to anyone."
        if s3_li == "Bill" or s3_li == "Harry":
            camilo @ blush "I got that so wrong."
    else:
        if s3_li == "Bill":
            "Genevieve steps forward."
        elif s3_li == "Camilo" or s3_li == "Harry":
            "Miki steps forward."
        camilo @ blush "Damn, I got that so wrong."

    # IF STATEMENT
    "Harry goes and picks up a suitcase."
    harry "'This girl...'"
    # IF STATEMENT
    if s3e1p2_mc_secret == "Thunder":
        harry @ surprised "'...is sexually attracted to the rumble of thunder!'"
    elif s3e1p2_mc_secret == "Rollercoaster":
        harry @ surprised "'...had a naughty adventure on a rollercoaster!'"
    elif s3e1p2_mc_secret == "Dimples":
        harry @ surprised "'...has a tendency to get too excited by dimples!'"
    elif s3e1p2_mc_secret == "Fan Fiction":
        harry @ surprised "'...wrote fan fiction when she was younger!'"
    
    thought "Oh no! This is about me."
    thought "I wonder if Harry can guess who that's about."

    # IF STATEMENT
    if s3_li == "Bill" or s3_li == "Camilo":
        harry @ smile "I reckon it's Genevieve."
        "He strides over and kisses Genevieve, accidentally bumping against her nose."
        genevieve blush "Don't worry. I didn't need my nose..."
        harry blush "Did I get it right?"
        genevieve neutral "Nope!"
    elif s3_li == "Harry":
        harry @ smile "I reckon it's [s3_name]."
        "He walks over to you."
        harry "I've got a hunch it was you because you kinda look guilty..."
        harry cheeky "But I also just really want to kiss you."
        harry "You up for that?"

        # CHOICE
        menu:
            thought "Do I mind if Harry kisses me?"
            "Yeah, sure!":
                $ s3_mc.like("Harry")
                "He closes his eyes and leans in for a kiss."
                "He leans the wrong way and bumps against your nose."
                harry @ blush "Oops."
                harry "Let me try that again."
                "Your lips touch and you feel him stumble forward a little. He gains his balance and draws you closer."
            "I'd rather you didn't.":
                harry neutral "That's fine! But just so everyone knows, I think this is about [s3_name]!"
                "He walks back to the others."

        harry smile "Did I get it right?"

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
            harry sad "Er, that's not how the game works."
            seb @ surprised "Yeah, it's about one of you girls."
            "You shuffle your feet awkwardly."
            seb cheeky "It's about you. Isn't it, [s3_name]?"
            s3_mc "Yeah... yeah it is."

    # IF STATEMENT
    if s3_li == "Bill" or s3_li == "Camilo":
        harry @ surprised "[s3_name]?"
        s3_mc "Yeah."
        harry "Woah, I was well off."
        harry blush "Ah, sorry, Genevieve."
        genevieve smile "You have got to tell us more about that later, hun."
    elif s3_li == "Harry":
        harry @ happy "Yes! I got it right."
        miki @ surprised "You have got to tell us more about that later, hun."

    # IF STATEMENT
    if s3_li == "Bill":
        bill cheeky "Yeah, I need details."
    elif s3_li == "Camilo":
        camilo cheeky "Yeah, I need details."
    elif s3_li == "Harry":
        harry cheeky "Yeah, I need details."
    
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
    if s3_li == "Bill" or s3_li == "Harry":
        bill @ surprised "Right, my turn!"
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
        if s3_li == "Bill":
            bill "[s3_name]?"
            bill cheeky "I think it's you, babes."
            "He walks over to you."
            bill "Mind if I kiss you?"
            # CHOICE
            menu:
                thought "Do I mind if Bill kisses me?"
                "Go for it, babes":
                    $ s3_mc.like("Bill")
                    "He kisses you softly, His hand rests on your back, drawing you in closer."
                "Nah, I'd rather you didn't":
                    bill @ smile "That's fine! But just so everyone knows, I think this is about MC!"
                    "He walks back to the others."

        elif s3_li == "Harry":
            bill "Iona?"
            "He walks over and kisses Iona."

        # IF STATEMENT
        if s3_li == "Bill":
            genevieve "Would the girl with the multiple packages please step forward?"
        elif s3_li == "Harry":
            miki "Would the girl with the multiple packages please step forward?"
        
        # IF STATEMENT
        if s3e1p2_ordered_sex_toys:
            "You and Iona both step forward."
            bill @ happy "I got it right!"
            iona @ surprised "No way."
            iona @ happy "That's hilarious."
            iona "You've done that too?"
            s3_mc "Yeah!"
        else:
            "Iona steps forward."
            if s3_li == "Bill":
                bill sad "Damn, I got it wrong!"
                s3_mc "Can't believe you thought that was me! "
                "He winks at you."
                bill cheeky "Maybe I just wanted an excuse to kiss you."
                s3_mc "Cheeky."
            else:
                "Iona steps forward."
                bill happy "Booyah. I got it right!"
                iona serious "Booyah?"
                "She winks."
                iona happy "Boo you more like."

        nicky blush "Woah, girl."
        nicky "That's like, so embarrassing."
        iona @ surprised "To be honest, I wasn't embarrassed at all."
        iona sad "It was just a faff to get all the boxes home on the train."
        harry @ surprised "Boxes plural? As in more than one?"
        iona @ happy "Bulk order discount, babe. "
        "Bill whistles."
        bill @ surprised "Wow."
        # IF STATEMENT
        if s3_li == "Bill":
            genevieve @ happy "Yeah! You go, sister."
        elif s3_li == "Harry":
            miki @ happy "Yeah! You go, sister."

# HERE HERE HERE HERE

    # IF STATEMENT
    if s3e1p1_cheeky_snog:
        if s3_li == "Bill":
            bill @ surprised "Can I go again?"
            iona "Sure!"
            camilo @ smile "I'll go next."
            "He smiles at you as he walks over, hoisting a case over his toned shoulders."
            bill @ surprised "OK, this girl..."
            "He looks up at you and smiles."
            bill "'This girl has already kissed a boy since we got into the Villa!'"
            iona "We'll all have by the end of this challenge."
            "He turns the piece of paper over."
            bill @ smile "'Before the challenge started!'"
            "Everyone laughs."
            genevieve "OK, I have no idea who that was."
            bill @ flirt "I think I do..."
            "He strides up to you and gently places his palm on your cheek."
            bill @ flirt "Fancy a round two?"
            # CHOICE
            menu:
                thought "Do I want [s3_li] to kiss me again?"
                "Yes!":
                    $ s3_mc.like(s3_li)
                    "He leans in and kisses you softly on the lips."
                    genevieve @ happy "[s3_name] is getting all the action today!"
                "Nah, you can kiss someone else":
                    bill "OK, suit yourself."
                    bill "I'll give AJ a quick kiss then."
                    "He kisses AJ on the cheek."
                "Go on then, [s3_li]":
                    $ s3_mc.like(s3_li)
                    "He leans in and kisses you softly on the lips."
                    genevieve @ happy "[s3_name] is getting all the action today!"
            iona @ talk "The answer was, of course..."
            "You step forward."
            iona @ smile "[s3_name]!"
            bill @ happy "Knew it."
            iona "Oh, you guys!"
            elladine @ smile "Such cuties."
            iona "OK..."
            iona @ talk "Next round."
            bill @ talk "Can I go again?"
            "The other boys cheer him on."
        elif s3_li == "Harry":
            harry @ talk "Can I go again?"
            iona "Sure!"
            camilo @ smile "I'll go next."
            "He smiles at you as he walks over, hoisting a case over his toned shoulders."
            harry @ talk "OK, this girl..."
            "He looks up at you and smiles."
            harry @ smile "'This girl has already kissed a boy since we got into the Villa!'"
            iona "We'll all have by the end of this challenge."
            "He turns the piece of paper over."
            harry @ smile "'Before the challenge started!'"
            "Everyone laughs."
            miki @ talk "OK, I have no idea who that was."
            harry @ flirt "I think I do..."
            "He strides up to you and gently places his palm on your cheek."
            harry @ flirt "Fancy a round two?"
            # CHOICE
            menu:
                thought "Do I want Harry to kiss me again?"
                "Yes!":
                    $ s3_mc.like(s3_li)
                    "He leans in and kisses you softly on the lips."
                    miki @ happy "[s3_name] is getting all the action today!"
                "Nah, you can kiss someone else":
                    harry "OK, suit yourself."
                    harry "I'll give AJ a quick kiss then."
                    "He kisses AJ on the cheek."
                "Go on then, Harry":
                    $ s3_mc.like(s3_li)
                    "He leans in and kisses you softly on the lips."
                    miki @ happy "[s3_name] is getting all the action today!"
            iona "The answer was, of course..."
            "You step forward."
            iona @ talk "[s3_name]!"
            harry @ happy "Knew it."
            iona "Oh, you guys!"
            elladine @ smile "Such cuties."
            iona "OK..."
            iona "Next round."

            harry @ talk "Can I go again?"
            "The other boys cheer him on."
        elif s3_li == "Camilo":
            camilo @ talk "I'll go next"
            "He smiles at you as he walks over, hoisting a case over his toned shoulders."
            camilo "OK, this girl..."
            "He looks up at you and smiles."
            camilo @ smile "'This girl has already kissed a boy since we got into the Villa!'"
            genevieve "We'll all have by the end of this challenge."
            "He turns the piece of paper over."
            camilo @ smile "'Before the challenge started!'"
            "Everyone laughs."
            miki "OK, I have no idea who that was."
            camilo @ flirt "I think I do..."
            "He strides up to you and gently places his palm on your cheek."
            camilo "Fancy a round two?"
            # CHOICE
            menu:
                thought "Do I want Camilo to kiss me again?"
                "Yes!":
                    $ s3_mc.like(s3_li)
                    "He leans in and kisses you softly on the lips."
                    miki @ happy "[s3_name] is getting all the action today!"
                "Nah, you can kiss someone else":
                    camilo "OK, suit yourself."
                    camilo @ smile "I'll give AJ a quick kiss then."
                    "He kisses AJ on the cheek."
                "Go on then, Camilo":
                    $ s3_mc.like(s3_li)
                    "He leans in and kisses you softly on the lips."
                    miki @ happy "[s3_name] is getting all the action today!"
            genevieve @ talk "The answer was, of course..."
            "You step forward."
            genevieve @ talk "[s3_name]!"
            camilo @ flirt "Knew it."
            genevieve @ flirt "Oh, you guys!"
            elladine @ smile "Such cuties."
            genevieve "OK..."
            genevieve "Next round."
            camilo @ happy "Can I go again?"
            "The other boys cheer him on."
    else:
        if s3_li == "Bill":
            bill @ talk "I'll go"
        elif s3_li == "Camilo":
            camilo @ talk "I'll go"
        elif s3_li == "Harry":
            harry @ talk "I'll go"
    
    "He grabs a case and looks at the clue."
    s3_mc "Just read the secret, hun."

    # IF STATEMENT
    if s3_li == "Bill":
        bill @ talk "'This girl has only ever had sex while on the water.'"
    elif s3_li == "Camilo":
        camilo @ talk "'This girl has been proposed to six times...'"
    elif s3_li == "Harry":
        harry @ talk "'This girl has never had sex with the lights off.'"

    "The boys go into a huddle."
    elladine flirt "Oh my gosh, which of you is this about?"
    "You look around the group. Nobody says anything."
    aj @ awkward "Come on, girls. It has to be one of us."
    "It quickly becomes clear that the clue isn't about any of you."

    # IF STATEMENT
    if s3_li == "Bill":
        genevieve sad "I don't get it. Who could it be?"
        iona serious "It's got to be one of us."
        "A clatter and rattle of wheels grabs everyone's attention as a large suitcase wheels out onto the platform."
        aj talk "Oh, wow."
        aj "That's one huge suitcase."
        genevieve -sad "I've never seen one that big before..."
        bill @ talk "I got a text!"
    elif s3_li == "Camilo":
        genevieve sad "I don't get it. Who could it be?"
        miki sad "It's got to be one of us."
        "A clatter and rattle of wheels grabs everyone's attention as a large suitcase wheels out onto the platform."
        aj talk "Oh, wow."
        aj "That's one huge suitcase."
        genevieve -sad "I've never seen one that big before..."
        camilo @ talk "I got a text!"
    elif s3_li == "Harry":
        miki sad "I don't get it. Who could it be?"
        iona serious "It's got to be one of us."
        "A clatter and rattle of wheels grabs everyone's attention as a large suitcase wheels out onto the platform."
        aj talk "Oh, wow."
        aj "That's one huge suitcase."
        miki -sad "I've never seen one that big before..."
        harry @ talk "I got a text!"
    
    text "Islanders, there is an unexpected item in your bagging area. [s3_li], please unzip the case."

    elladine @ talk "Oh my gosh, [s3_li]! Open up the case already!"
    "[s3_li] tentatively unzips the suitcase."
    "A stunning woman steps out."

    # IF STATEMENT
    if s3_li == "Bill":
        miki "Hey, you lot. I'm Miki."

        # Profile shot of Miki
        "Miki\n
        -21, from Cambridge\n
        -Lifestyle vlogger\n
        -Loves it when you smash the subscribe button"

        "She nods at Bill."
        miki @ happy "Thanks for getting me out of there, Bill."
        "Genevieve splutters in shock."
        genevieve @ talk "Wait... what? But..."
        iona @ talk "It's a new girl!"
        "Elladine and Iona run over to hug Miki."
        elladine @ happy"Welcome to the Villa, hun."
        nicky @ smile "Yeah, hey. I hope you weren't stuck in there for long, babe."
        miki "Nah, just a few minutes."
    elif s3_li == "Camilo":
        iona "Hey, you lot. I'm Iona."

        # Profile shot of Iona
        "Iona\n
        -23, from Aberdeen\n
        -Apprentice pylon rigger\n
        -Spends all day making sparks fly"

        "She nods at Camilo."
        iona @ smile "Thanks for getting me out of there, Camilo."
        "Miki splutters in shock."
        miki @ talk "Wait... what? But..."
        genevieve @ talk "It's a new girl!"
        "Elladine and Genevieve run over to hug Iona."
        elladine @ happy "Welcome to the Villa, hun."
        nicky @ smile "Yeah, hey. I hope you weren't stuck in there for long, babe."
        iona "Nah, just a few minutes."
    elif s3_li == "Harry":
        genevieve "Hey, you lot. I'm Genevieve."

        # Profile shot of Genevieve
        "Genevieve\n
        -26, from Gastonbury\n
        -Junior doctor\n
        -Wants to crowd surf into your heart"

        "She nods at Harry."
        genevieve @ smile "Thanks for getting me out of there, Harry."
        "Miki splutters in shock."
        miki @ talk "Wait... what? But..."
        iona @ talk "It's a new girl!"
        "Elladine and Iona run over to hug Genevieve."
        elladine @ happy "Welcome to the Villa, hun."
        nicky @ smile "Yeah, hey. I hope you weren't stuck in there for long, babe."
        genevieve "Nah, just a few minutes."

    # CHOICE
    menu:
        thought "There's a new girl in the Villa..."
        "Welcome her with a hug":
            $ s3_mc.like(s3_3rd_girl)
            if s3_li == "Bill":
                "You walk over and hug Miki."
                miki smile "Aw, thanks girls!"
                miki "It's so nice to be so welcomed."
            elif s3_li == "Camilo":
                "You walk over and hug Iona."
                iona smile "Aw, thanks girls!"
                iona "It's so nice to be so welcomed."
            elif s3_li == "Harry":
                "You walk over and hug Genevieve."
                genevieve smile "Aw, thanks girls!"
                genevieve "It's so nice to be so welcomed."
            
        "Try and get in the suitcase":
            "You run past Miki and attempt to clamber into the large suitcase. You fit perfectly, even standing upright."
            s3_mc "Woah, this thing is huge."
            aj @ talk "Yeah, how did they get you on the plane in that thing?"
            if s3_li == "Bill":
                miki @ talk "I didn't ride in it on the plane, hun. I only just got in it."
            elif s3_li == "Camilo":
                iona @ talk "I didn't ride in it on the plane, hun. I only just got in it."
            elif s3_li == "Harry":
                genevieve @ talk "I didn't ride in it on the plane, hun. I only just got in it."
            aj @ awkward "Oh right. Yeah, of course."

        "Roll your eyes and ignore her":
            $ s3_mc.dislike(s3_3rd_girl)
            "You roll your eyes. "
            thought "I totally didn't see that coming."
            "You stare at the ground as the other girls crowd around her."

    # IF STATEMENT
    if s3_li == "Bill":
        aj @ talk "Wait, we just had a clue, right? Miki, was it about you?"
        aj @ talk "Have you really only ever had sex on water?"
        genevieve @ talk "How does that even work?"
        "Miki smiles."
        miki @ flirt "I guess we'll have to wait for the boys to guess before we find out, won't we?"
        bill smile "Well, I think I can guess who to kiss now..."
        "He takes a step toward her."
        # CHOICE
        menu:
            thought "Miki and Bill are going to kiss"
            "Cheer them on":
                s3_mc "Woo! Get in there, [s3_li]."
                show bill happy
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
            seb @ smile "How was it, mate?"
            bill @ smile "I'd say that was...maybe the third best kiss I've had today?"
            seb @ flirt "Wow. You're really cracking on, huh."
        else:
            "Bill and Miki kiss. It feels like it lasts forever."
            "They finally pull away."

        elladine @ talk "So, was he right?"
        miki smile "Yeah, it's true."
        miki "I love the water."
        miki "Oh, I got a text! That was quick."

        text "Islanders, that's the end of the challenge. Hopefully you've all learnt a little bit more about your fellow Islanders. Now all the dirt is dished, it's time for Miki to go and get to know you all."

        miki @ happy "Alright! Let's go, huns!"
    elif s3_li == "Camilo":
        aj @ talk "Wait, we just had a clue, right? Iona, was it about you?"
        aj @ talk "Did you really get proposed six times?"
        miki @ talk "Juicy!"
        "Iona smiles."
        iona @ talk "I guess we'll have to wait for the boys to guess before we find out, won't we?"
        camilo smile "Well, I think I can guess who to kiss now..."
        "He takes a step toward her."
        # CHOICE
        menu:
            thought "Iona and Camilo are going to kiss"
            "Cheer them on":
                s3_mc "Woo! Get in there, [s3_li]."
                show camilo happy
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
            seb @ smile "How was it, mate?"
            camilo @ flirt "I'd say that was...maybe the third best kiss I've had today?"
            seb @ flirt "Wow. You're really cracking on, huh."
        else:
            "Camilo and Iona kiss. It feels like it lasts forever."
            "They finally pull away."
        elladine @ talk "So, was he right?"
        iona smile "Yeah, it's true."
        iona "I can't help it, people just always seem to want to marry me."
        iona "Oh, I got a text! That was quick."

        text "Islanders, that's the end of the challenge. Hopefully you've all learnt a little bit more about your fellow Islanders. Now all the dirt is dished, it's time for Iona to go and get to know you all."

        iona @ happy "Alright! Let's go, huns!"
    elif s3_li == "Harry":
        aj @ talk "Wait, we just had a clue, right? Genevieve, was it about you?"
        aj @ talk "Have you really never ever had sex with the lights off?"
        aj "Do you only do it in the day or something?"
        "Genevieve smiles."
        genevieve @ flirt "I guess we'll have to wait for the boys to guess before we find out, won't we?"
        harry smile "Well, I think I can guess who to kiss now..."
        "He takes a step toward her."
        # CHOICE
        menu:
            thought "Genevieve and Harry are going to kiss"
            "Cheer them on":
                s3_mc "Woo! Get in there, [s3_li]."
                show harry happy
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
            seb smile "How was it, mate?"
            harry @ flirt "I'd say that was...maybe the third best kiss I've had today?"
            seb @ flirt "Wow. You're really cracking on, huh."
        else:
            "Harry and Genevieve kiss. It feels like it lasts forever."
            "They finally pull away."
        elladine @ talk "So, was he right?"
        genevieve smile "Yeah, it's true."
        genevieve "What can I say."
        genevieve @ flirt "I like to be able to see the action..."
        genevieve "Oh, I got a text! That was quick."
    
        text "Islanders, that's the end of the challenge. Hopefully you've all learnt a little bit more about your fellow Islanders. Now all the dirt is dished, it's time for Genevieve to go and get to know you all."
        
        genevieve @ happy "Alright! Let's go, huns!"

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
    #     if s3_li == "Bill":
    #         bill "By the way. I never got the chance to say it earlier, but I absolutely love the swimsuit."
    #         bill "It looks so good on you."
    #     elif s3_li == "Camilo":
    #         camilo "By the way. I never got the chance to say it earlier, but I absolutely love the swimsuit."
    #         camilo "It looks so good on you."
    #     elif s3_li == "Harry":
    #         harry "By the way. I never got the chance to say it earlier, but I absolutely love the swimsuit."
    #         harry "It looks so good on you."
    # else:
    #     if s3_li == "Bill":
    #         bill "Call me shallow, but I love how good you look, [s3_name]."
    #         bill "Even in your lowkey getup."
    #     elif s3_li == "Camilo":
    #         camilo "Call me shallow, but I love how good you look, [s3_name]."
    #         camilo "Even in your lowkey getup."
    #     elif s3_li == "Harry":
    #         harry "Call me shallow, but I love how good you look, [s3_name]."
    #         harry "Even in your lowkey getup."

    # s3_mc "Thanks!"

    # IF STATEMENT
    if s3_li == "Bill" or s3_li == "Harry":
        iona @ talk "So, everyone's dirties are out now..."
        iona "And now [s3_3rd_girl] is here."
    elif s3_li == "Camilo":
        genevieve @ talk "So, everyone's dirties are out now..."
        genevieve "And now [s3_3rd_girl] is here."

    "[s3_3rd_girl] does a little wave."

    # IF STATEMENT
    if s3_li == "Bill":
        miki @ smile "Yeah, it's me."
    elif s3_li == "Camilo":
        iona @ smile "Yeah, it's me."
    elif s3_li == "Harry":
        genevieve @ smile "Yeah, it's me."

    harry @ talk "So much has happened, in so little time!"
    harry "I feel like we're already a solid group."

    # IF STATEMENT
    if s3_li == "Bill":
        iona @ talk "I know, right? It's all going down."
        iona "Pretending to be a waitress..."
        if s3e1p2_camilos_clue:
            show iona happy
            "She winks at you and Genevieve."
    elif s3_li == "Camilo" or s3_li == "Harry":
        genevieve @ talk "I know, right? It's all going down."
        genevieve "Embarrassing sexy dances..."
        if s3e1p2_camilos_clue:
            show genevieve happy
            "She winks at you and Miki."

    # IF STATEMENT
    if s3_li == "Bill":
        nicky @ talk "I can't believe Miki's secret."
        bill @ talk "Yeah, did you, like, live on a boat or something?"
        miki flirt "Yeah, I do actually."
        bill @ happy "Oh, woah. That makes more sense now."
    elif s3_li == "Camilo":
        nicky @ talk "I can't believe Iona's secret."
        camilo @ talk "You must have seen, like, all the cheesy proposals."
        iona "Yeah, I've seen them all."
        iona smile "One guy even flew a plane with a message on a banner."
        camilo "Oh, wow."
        "She shrugs."
        iona @ flirt "He flew the wrong way."
        iona "So my name read 'ANOI'. He was so embarrassed."
    elif s3_li == "Harry":
        nicky @ talk "I can't believe Genevieve's secret."
        harry @ talk "Yeah, like you've never turned off the lights?"
        genevieve smile "Nope... never."
        genevieve @ flirt "I like to be able to see what's happening."
        
    nicky "I thought it was a great clue."
    seb "Yeah, same."
    seb @ smile "Shows you've got good life experiences and all that."

    # CHOICE
    menu:
        thought "What do I think about [s3_3rd_girl]'s clue?"
        "I can't wait to get to know [s3_3rd_girl]!":
            $ s3_mc.like(s3_3rd_girl)
            s3_mc "You sound right up my street, [s3_3rd_girl]."
            s3_mc "I can't wait to get to know you!"
            if s3_li == "Bill":
                miki @ smile "Aw, thanks, [s3_name]."
            elif s3_li == "Camilo":
                iona @ smile "Aw, thanks, [s3_name]."
            elif s3_li == "Harry":
                genevieve @ smile "Aw, thanks, [s3_name]."
        "It doesn't say much about her":
            s3_mc "Is it, like, the best reflection of your personality?"
            if s3_li == "Bill":
                miki awkward "Um... no, probably not."
            elif s3_li == "Camilo":
                iona awkward "Um... no, probably not."
            elif s3_li == "Harry":
                genevieve awkward "Um... no, probably not."
            nicky @ smile "I think it's a proper funny place to start though."
        "I don't believe [s3_3rd_girl] at all":
            $ s3_mc.dislike(s3_3rd_girl)
            s3_mc "I don't believe you, [s3_3rd_girl]."
            nicky @ flirt "Why would she make that up?"
            "You shrug."
            s3_mc "It's a game."
            if s3_li == "Bill":
                genevieve @ awkward "Yeah you've got to stand out."
            elif s3_li == "Camilo" or s3_li == "Harry":
                miki @ awkward "Yeah you've got to stand out."
            nicky @ serious "Yeah, authentically."

            if s3_li == "Bill":
                miki sad "It's also a bit of a specific thing to lie about..."
            elif s3_li == "Camilo":
                iona sad "It's also a bit of a specific thing to lie about..."
            elif s3_li == "Harry":
                genevieve sad "It's also a bit of a specific thing to lie about..."
            s3_mc "Hmm..."

    # IF STATEMENT
    if s3_li == "Bill":
        iona smile "For real though Miki, you definitely made an entrance."
        iona @ talk "Maybe we should all arrive in suitcases next time!"
        miki smile "Yeah, I thought it was a bit out there at first but it was actually really fun."
        miki "I can't believe all this."
        "She gestures to the Villa."
        miki @ talk "It's amazing, isn't it?"
    elif s3_li == "Camilo":
        genevieve smile "For real though Iona, you definitely made an entrance."
        genevieve @ talk "Maybe we should all arrive in suitcases next time!"
        iona smile "Yeah, I thought it was a bit out there at first but it was actually really fun."
        iona @ talk "This place is bigger than I thought it would be!"
    elif s3_li == "Harry":
        iona smile "For real though Genevieve, you definitely made an entrance."
        iona @ talk "Maybe we should all arrive in suitcases next time!"
        genevieve smile "It worked really well."
        genevieve "It's so cool to be finally here."
        genevieve @ awkward "I really needed a holiday."

    aj smile "Yeah, I'm still getting used to all this."
    elladine "We'll all settle in soon enough."
    camilo smile "Once we have, like, proper meal together."
    camilo "Then it'll feel like home."
    camilo @ flirt "Food is the way to my heart..."
    aj @ happy "As long as I haven't cooked it, then a good meal is exactly what we need."

    if s3_li == "Harry":
        if s3e1p2_set_fire:
            iona @ smile "Yeah, and hopefully [s3_name] doesn't burn the kitchen down!"
        else:
            iona @ smile "Yeah, and hopefully Elladine doesn't burn the kitchen down!"
    else:
        if s3e1p2_set_fire:
            genevieve @ smile "Yeah, and hopefully [s3_name] doesn't burn the kitchen down!"
        else:
            genevieve @ smile "Yeah, and hopefully Elladine doesn't burn the kitchen down!"

    # CHOICE
    menu:
        thought "Is food the way to my heart?"
        "Of course! Food makes the heart grow fonder":
            harry @ awkward "I'm pretty sure it's absence makes the heart fonder."
            bill @ talk "Come on, [s3_name] is right."
            bill smile "Food is the real key to it."
        "Nah, I'm more of a drinks gal":
            s3_mc "Give me a good bottle and I'm happy."
            bill @ smile "Nah, you can't beat a good piece of toast."
        "As long as I'm eating it off [s3_li]'s body":
            $ s3_mc.like(s3_li)
            elladine @ talk "Woah, [s3_name]!"
            s3_mc "Did I say that out loud?"
            if s3_li == "Bill":
                "Bill blushes, but grins excitedly."
                bill @ flirt "You sure did..."
            elif s3_li == "Camilo":
                "Camilo blushes, but grins excitedly."
                camilo @ flirt "You sure did..."
            elif s3_li == "Harry":
                "Harry blushes, but grins excitedly."
                harry @ flirt "You sure did..."

    # IF STATEMENT
    if s3_li == "Bill":
        miki @ talk "Oh, that's mine."
    elif s3_li == "Camilo":
        iona @ talk "Oh, that's mine."
    elif s3_li == "Harry":
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
    if s3_li == "Bill":
        genevieve flirt "Single and ready to mingle, eh?"
        iona smile "Guess we'll need to keep a close eye on you."
        "And the power is in Miki's hands."
        miki serious "But, ultimately, I do have to make a choice and so..."
    elif s3_li == "Camilo":
        miki flirt "Single and ready to mingle, eh?"
        genevieve smile "Guess we'll need to keep a close eye on you."
        "And the power is in Miki's hands."
        iona serious "But, ultimately, I do have to make a choice and so..."
    elif s3_li == "Harry":
        miki flirt "Single and ready to mingle, eh?"
        iona smile "Guess we'll need to keep a close eye on you."
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
    if s3_li == "Bill":
        miki @ smile "Hey, hun."
        miki @ sad "You all right?"
        s3_mc "Yeah, I thought I'd see if you wanted to have a chat?"
        s3_mc "Girl to girl."
        miki @ smile "I'd love to."
        miki "Roof terrace? I've been dying to check it out."
        s3_mc "Great idea."
        
        scene s3-roof-day with dissolve
        $ on_screen = []

        "You and [s3_3rd_girl] sit beside each other on the roof."
        miki @ smile "Thanks for this."
        miki "Like, I was so worried coming in later."
        miki "Because everyone else has had a chance to couple up and meet each other first."
        # CHOICE
        menu:
            thought "[s3_3rd_girl] was worried about coming in late..."
            "You don't need to worry":
                s3_mc "Everyone seems pretty chill."
                s3_mc "Plus, we've only been here for a few hours!"
                miki smile "That's true, yeah."
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
        miki @ smile "I'm so glad you called me over."
        miki "I wanted to talk to you about who I'm crushing on right now."
        s3_mc "Oh, yeah?"
        miki @ awkward "Yeah, you see..."
        "She looks down, then up again."
        miki @ awkward "I'm actually really attracted to Bill."
        
        # CHOICE
        menu:
            thought "[s3_3rd_girl] is into [s3_li]!"
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
            thought "How do I feel about the idea of [s3_3rd_girl] picking [s3_li]?"
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
        miki smile "So, thank you for taking the time to talk to me..."
        miki "It means a lot."
        miki serious "We should get back to the others."
        "You both head down from the roof terrace."
    elif s3_li == "Camilo":
        iona smile "Hey, hun."
        iona sad "You all right?"
        s3_mc "Yeah, I thought I'd see if you wanted to have a chat?"
        s3_mc "Girl to girl."
        iona smile "I'd love to."
        iona "Roof terrace? I've been dying to check it out."
        s3_mc "Great idea."

        scene s3-roof-day with dissolve
        $ on_screen = []

        "You and [s3_3rd_girl] sit beside each other on the roof."
        iona smile "Thanks for this."
        iona @ sad "Like, I was so worried coming in later."
        iona serious "Because everyone else has had a chance to couple up and meet each other first."
        # CHOICE
        menu:
            thought "[s3_3rd_girl] was worried about coming in late..."
            "You don't need to worry":
                s3_mc "Everyone seems pretty chill."
                s3_mc "Plus, we've only been here for a few hours!"
                iona smile "That's true, yeah."
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
            thought "[s3_3rd_girl] is into [s3_li]!"
            "I totally saw that coming":
                iona @ talk -sad "You did?"
                s3_mc "Yeah, I had a hunch."
            "Yeah, I don't blame you! He's gorgeous":
                iona smile "He is, isn't he?"
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
            thought "How do I feel about the idea of [s3_3rd_girl] picking [s3_li]?"
            "I'd be OK about it":
                iona @ talk "Really?"
                s3_mc "Yeah, like you said, early days."
            "At least you told me":
                iona @ smile "I thought it was the best thing to do."
            "I'd be annoyed":
                iona sad "Oh, really?"
                s3_mc "Yeah."
                iona @ flirt "Well, I'm sorry you feel like that."
                iona "I hope we can move past, like, whatever happens."
                iona "If it happens."

        iona serious "And also, I don't know if he likes me the same way."
        iona "But I really wanted to talk to you about it."
        iona smile "So, thank you for taking the time to talk to me..."
        iona "It means a lot."
        iona "We should get back to the others."
        "You both head down from the roof terrace."
    elif s3_li == "Harry":
        genevieve smile "Hey, hun."
        genevieve sad "You all right?"
        s3_mc "Yeah, I thought I'd see if you wanted to have a chat?"
        s3_mc "Girl to girl."
        genevieve smile"I'd love to."
        genevieve "Roof terrace? I've been dying to check it out."
        s3_mc "Great idea."

        scene s3-roof-day with dissolve
        $ on_screen = []

        "You and [s3_3rd_girl] sit beside each other on the roof."
        genevieve smile "Thanks for this."
        genevieve @ awkward "Like, I was so worried coming in later."
        genevieve serious "Because everyone else has had a chance to couple up and meet each other first."
        # CHOICE
        menu:
            thought "[s3_3rd_girl] was worried about coming in late..."
            "You don't need to worry":
                s3_mc "Everyone seems pretty chill."
                s3_mc "Plus, we've only been here for a few hours!"
                genevieve smile "That's true, yeah."
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
            thought "[s3_3rd_girl] is into [s3_li]!"
            "I totally saw that coming":
                genevieve @ talk "You did?"
                s3_mc "Yeah, I had a hunch."
            "Yeah, I don't blame you! He's gorgeous":
                genevieve smile "He is, isn't he?"
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
            thought "How do I feel about the idea of [s3_3rd_girl] picking [s3_li]?"
            "I'd be OK about it":
                genevieve @ talk "Really?"
                s3_mc "Yeah, like you said, early days."
            "At least you told me":
                genevieve @ smile "I thought it was the best thing to do."
            "I'd be annoyed":
                genevieve sad "Oh, really?"
                s3_mc "Yeah."
                genevieve @ awkward "Well, I'm sorry you feel like that."
                genevieve "I hope we can move past, like, whatever happens."
                genevieve "If it happens."

        genevieve serious "I've no idea how he feels, like."
        genevieve "But I really wanted to talk to you about it."
        genevieve smile "So, thank you for taking the time to talk to me..."
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
    if s3_li == "Bill":
        miki happy "Hey, you lot. I'm Miki."
        miki "Thanks for getting me out of there."
        show miki at npc_exit
        pause 0.3
        $ renpy.hide("miki")
    elif s3_li == "Camilo":
        iona smile "Hey, you lot. I'm Iona."
        iona "Thanks for getting me out of there."
        show iona at npc_exit
        pause 0.3
        $ renpy.hide("iona")
    elif s3_li == "Harry":
        genevieve smile "Hey, you lot. I'm Genevieve."
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
    if s3_li == "Bill":
        "And Miki takes her pick..."
        show miki at npc_center
        miki serious "The guy I'd like to couple up with is..."
        show miki at npc_exit
        pause 0.3
        $ renpy.hide("miki")
    elif s3_li == "Camilo":
        "And Iona takes her pick..."
        show iona at npc_center
        iona serious "The guy I'd like to couple up with is..."
        show iona at npc_exit
        pause 0.3
        $ renpy.hide("iona")
    elif s3_li == "Harry":
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
    if s3_li == "Bill" or s3_li == "Harry":
        iona sad "It's so weird knowing that [s3_3rd_girl]'s just stood by the firepit waiting for us."
    elif s3_li == "Camilo":
        genevieve awkward "It's so weird knowing that [s3_3rd_girl]'s just stood by the firepit waiting for us."
    
    if s3_li == "Bill":
        genevieve sad "Waiting for the guys more like."
        elladine sad "Yeah. It really didn't take long for the drama to start."
        genevieve "Tell me about it! I thought we'd at least have a day or something."
    elif s3_li == "Camilo" or s3_li == "Harry":
        miki sad "Waiting for the guys more like."
        elladine sad "Yeah. It really didn't take long for the drama to start."
        miki "Tell me about it! I thought we'd at least have a day or something."

    if s3_li == "Bill" or s3_li == "Harry":
        iona serious "Well, we kind of did."
    elif s3_li == "Camilo":
        genevieve serious "Well, we kind of did."
    
    aj "Can you pass me my lipstick, Ella, babes."
    elladine -sad "Of course hun."
    aj @ smile "Thanks! [s3_3rd_girl]'s super fit, don't you think?"

    # CHOICE
    menu:
        thought "[s3_3rd_girl] is..."
        "Almost too good looking":
            elladine serious "Yeah..."
        "Not really all that":
            elladine sad "I don't know how you can say that?"
        "Not as fit as me":
            elladine @ smile "You're both gorgeous."

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
        elladine @ happy "Damn right."

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


    if s3_li == "Bill" or s3_li == "Harry":
        "Iona turns to you."
        iona serious "Are you worried about tonight, babe?"
    elif s3_li == "Camilo":
        "Genevieve turns to you."
        genevieve serious "Are you worried about tonight, babe?"

    # CHOICE
    menu:
        thought "Am I worried about who [s3_3rd_girl] will pick?"
        "I'd be lying if I said no":
            if s3_li == "Bill" or s3_li == "Harry":
                iona "Yeah, I know what you mean."
                iona @ awkward "Why am I so nervous?"
            elif s3_li == "Camilo":
                genevieve "Yeah, I know what you mean."
                genevieve @ awkward "Why am I so nervous?"
        "No, of course I'm not":
            if s3_li == "Bill" or s3_li == "Harry":
                iona "Yeah..."
                iona @ flirt "I don't know. I feel surprisingly nervous myself."
            elif s3_li == "Camilo":
                genevieve "Yeah..."
                genevieve @ awkward "I don't know. I feel surprisingly nervous myself."
        "How could I when I look this good?":
            elladine @ smile -serious "Wow, hun. I wish I had your confidence!"
            aj @ flirt "She's not wrong, though."
            if s3_li == "Bill" or s3_li == "Harry":
                iona @ smile -serious "Hearing that actually made me feel a little better myself."
            elif s3_li == "Camilo":
                genevieve @ smile -serious "Hearing that actually made me feel a little better myself."
        "Actually, I know she's going to pick [s3_li]." if s3e1p2_talk_to_new_girl == True:
            if s3_li == "Bill" or s3_li == "Harry":
                iona @ talk "Really? How?"
                s3_mc "She told me."
                iona "Oh..."
            elif s3_li == "Camilo":
                genevieve @ talk "Really? How?"
                s3_mc "She told me."
                genevieve "Oh..."
            elladine @ flirt "At least she was honest, I guess?"

    if s3_li == "Bill":
        "Genevieve takes a deep breath, and gives herself one last look-over in the mirror."
        genevieve serious "Well, girls, I guess this is it..."
    elif s3_li == "Camilo" or s3_li == "Harry":
        "Miki takes a deep breath, and gives herself one last look-over in the mirror."
        miki serious "Well, girls, I guess this is it..."

    scene s3-firepit-night with dissolve
    $ on_screen = []

    "[s3_3rd_girl] stands in front of the Islanders sat around the firepit."

    # CHOICE
    menu:
        thought "We only just arrived and already I might get separated from [s3_li]..."
        "Hold his hand":
            $ s3_mc.like(s3_li)
            if s3_li == "Bill":
                "You reach over and take a hold of [s3_li]'s hand. He turns and smiles at you."
                bill @ flirt "Your hands are so soft."
                "You blush"
                bill @ smile "Seriously, it's like holding a warm loaf of bread or something..."
                s3_mc "Huh?"
                bill @ awkward "...I don't know. Ignore me. My mind's all over the place."
                "He shifts in his seat."
            elif s3_li == "Camilo":
                "You reach over and take a hold of [s3_li]'s hand. He turns and smiles at you."
                camilo @ flirt "Your hands are so soft."
                "You blush"
                camilo @ smile "Seriously, it's like holding a warm loaf of bread or something..."
                s3_mc "Huh?"
                camilo @ awkward "...I don't know. Ignore me. My mind's all over the place."
                "He shifts in his seat."
            elif s3_li == "Harry":
                "You reach over and take a hold of [s3_li]'s hand. He turns and smiles at you."
                harry @ flirt "Your hands are so soft."
                "You blush"
                harry @ smile "Seriously, it's like holding a warm loaf of bread or something..."
                s3_mc "Huh?"
                harry @ awkward "...I don't know. Ignore me. My mind's all over the place."
                "He shifts in his seat."

        "Glare at [s3_3rd_girl]":
            "You frown at [s3_3rd_girl]. She doesn't look at you."
            s3_mc "Dammit, she didn't see me!"
            "You squint harder and lean in closer."
            thought "She has to notice me now."
            "Just then, you hear [s3_li]'s voice whispering in your ear."
            if s3_li == "Bill":
                bill awkward "Um, what are you doing?"
                s3_mc "Huh?"
                bill @ serious -awkward "Do you need glasses or something?"
            elif s3_li == "Camilo":
                camilo awkward "Um, what are you doing?"
                s3_mc "Huh?"
                camilo @ serious -awkward "Do you need glasses or something?"
            elif s3_li == "Harry":
                harry awkward "Um, what are you doing?"
                s3_mc "Huh?"
                harry @ serious -awkward"Do you need glasses or something?"
            s3_mc "No..."

        "Look at the other Islanders":
            "You look around to see how the others are handling [s3_3rd_girl]'s arrival."
            thought "If those girls are nervous, they're doing a banging job of hiding it."
            "The only one who seems a little off is Elladine, who occasionally glances at her hands."
            "The boys seem calm, too. But you look harder, you notice that Seb's chewing his cheek."
            if s3_li == "Bill":
                "Harry can't keep his eyes off of Miki."
            elif s3_li == "Harry":
                "Camilo's eyes are fixed on Genevieve's face. He bites his lips."
            thought "Any of these guys would probably jump at the chance to be with [s3_3rd_girl]..."

    "[s3_3rd_girl] clears her throat, then speaks."

    if s3_li == "Bill":
        miki @ talk "I didn't know how to feel on the way here."
        miki "I was excited, obviously, but I knew I'd be taking a guy away from another girl."
        miki @ serious "I thought I'd be OK with that as you've only been together since this morning..."
        miki @ sad "But looking at you all now, you already seem like such cute couples."
        miki "But at first glance, this boy seems like my type on paper."
        miki @ smile "He's smart, funny, and just dreamy."
        miki @ awkward "And although I don't want to break a promising couple up so early on..."
        miki @ serious "I'm here to make a choice and so..."
        "Everyone tenses."

        if s3e1p2_talk_to_new_girl:
            thought "Here she goes. About to pick [s3_li]..."
        else:
            thought "She better not pick [s3_li]."
        miki "The boy I'd like to couple up with is..."
        thought "Maybe she won't?"
        miki @ smile "[s3_li]."
    elif s3_li == "Camilo":
        iona @ talk "I didn't know how to feel on the way here."
        iona "I was excited, obviously, but I knew I'd be taking a guy away from another girl."
        iona @ serious "I thought I'd be OK with that as you've only been together since this morning..."
        iona @ sad "But looking at you all now, you already seem like such cute couples."
        iona "But at first glance, this boy seems like my type on paper."
        iona @ smile "He's smart, funny, and just dreamy."
        iona @ awkward "And although I don't want to break a promising couple up so early on..."
        iona @ serious "I'm here to make a choice and so..."
        "Everyone tenses."
        if s3e1p2_talk_to_new_girl:
            thought "Here she goes. About to pick [s3_li]..."
        else:
            thought "She better not pick [s3_li]."
        iona "The boy I'd like to couple up with is..."
        thought "Maybe she won't?"
        iona @ smile "[s3_li]."
    elif s3_li == "Harry":
        genevieve @ talk "I didn't know how to feel on the way here."
        genevieve "I was excited, obviously, but I knew I'd be taking a guy away from another girl."
        genevieve @ serious "I thought I'd be OK with that as you've only been together since this morning..."
        genevieve @ sad "But looking at you all now, you already seem like such cute couples."
        genevieve "But at first glance, this boy seems like my type on paper."
        genevieve @ smile "He's smart, funny, and just dreamy."
        genevieve @ awkward "And although I don't want to break a promising couple up so early on..."
        genevieve @ serious "I'm here to make a choice and so..."
        "Everyone tenses."
        if s3e1p2_talk_to_new_girl:
            thought "Here she goes. About to pick [s3_li]..."
        else:
            thought "She better not pick [s3_li]."
        genevieve "The boy I'd like to couple up with is..."
        thought "Maybe she won't?"
        genevieve @ smile "[s3_li]."

    # CHOICE
    menu:
        thought "[s3_3rd_girl] picked [s3_li]!"
        "I called it" if s3e1p2_talk_to_new_girl == True:
            pass
        "At least she told me" if s3e1p2_talk_to_new_girl == False:
            pass
        "No, dammit!":
            pass
        "Well, this sucks":
            pass

    if s3_li == "Harry":
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
            if s3_li == "Bill":
                "Miki smiles."
                miki @ smile "Thanks for understanding, [s3_name]."
            elif s3_li == "Camilo":
                "Iona smiles."
                iona @ smile "Thanks for understanding, [s3_name]."
            elif s3_li == "Harry":
                "Genevieve smiles."
                genevieve @ smile "Thanks for understanding, [s3_name]."
        "How could you?":
            $ s3_mc.dislike(s3_3rd_girl)
            if s3_li == "Bill":
                "Miki's face drops."
                miki sad "It was a really hard decision, babe. I didn't want to make it..."
            elif s3_li == "Camilo":
                "Iona's face drops."
                iona sad "It was a really hard decision, babe. I didn't want to make it..."
            elif s3_li == "Harry":
                "Genevieve's face drops."
                genevieve sad "It was a really hard decision, babe. I didn't want to make it..."
        "I'll be coming for him":
            if s3_li == "Bill":
                miki "Good."
                miki @ smile "I'm looking forward to the competition."
            elif s3_li == "Camilo":
                iona "Good."
                iona @ smile "I'm looking forward to the competition."
            elif s3_li == "Harry":
                genevieve "Good."
                genevieve @ smile "I'm looking forward to the competition."
        "At least you told me " if s3e1p2_talk_to_new_girl == True:
            $ s3_mc.like(s3_3rd_girl)
            if s3_li == "Bill":
                miki "I really didn't want it to be a surprise for you..."
            elif s3_li == "Camilo":
                iona "I really didn't want it to be a surprise for you..."
            elif s3_li == "Harry":
                genevieve "I really didn't want it to be a surprise for you..."

    "[s3_li] puts a hand on your back."

    if s3_li == "Bill":
        bill @ angry "I can't believe this."
        bill sad "I was blown away when you picked me. It's like I'd won the jackpot."
        bill "And now we're not a couple, less than a day after that..."
    elif s3_li == "Camilo":
        camilo @ angry "I can't believe this."
        camilo sad "I was blown away when you picked me. It's like I'd won the jackpot."
        camilo "And now we're not a couple, less than a day after that..."
    elif s3_li == "Harry":
        harry @ angry "I can't believe this."
        harry sad "I was blown away when you picked me. It's like I'd won the jackpot."
        harry "And now we're not a couple, less than a day after that..."
    "He stands to walk over to [s3_3rd_girl]."

    # CHOICE
    menu:
        thought "Bill's getting up to leave..."
        "Squeeze his hand":
            $ s3_mc.like(s3_li)
            if s3_li == "Bill":
                "You reach out, grab his hand, and give it a gentle squeeze. He stops in his tracks and turns back to you."
                bill @ flirt "Don't worry. I'll only be over there."
                s3_mc "But that's not here."
                bill "Yeah..."
                "He sighs, then continues over to [s3_3rd_girl]."
            elif s3_li == "Camilo":
                "You reach out, grab his hand, and give it a gentle squeeze. He stops in his tracks and turns back to you."
                camilo @ smile "Don't worry. I'll only be over there."
                s3_mc "But that's not here."
                camilo "Yeah..."
                "He sighs, then continues over to [s3_3rd_girl]."
            elif s3_li == "Harry":
                "You reach out, grab his hand, and give it a gentle squeeze. He stops in his tracks and turns back to you."
                harry @ flirt "Don't worry. I'll only be over there."
                s3_mc "But that's not here."
                harry "Yeah..."
                "He sighs, then continues over to [s3_3rd_girl]."
        "Drag him back":
            if s3_li == "Bill":
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
            elif s3_li == "Camilo":
                "You reach out, wrap your fingers around his arm, and pull."
                camilo @ talk "Agh!"
                "He lurches back, loses his balance and falls hard onto the seat."
                "Seb and Nicky let out a laugh. Elladine raises an eyebrow at you."
                camilo @ awkward "Ow, my bum!"
                camilo "These cushions are weirdly firm."
                "He looks at you with a puzzled expression."
                s3_mc "Sorry..."
                camilo @ smile -sad "Don't worry. Look, I'm only going to be over there."
                s3_mc "But that's not here."
                "He gets back up and makes his way over to [s3_3rd_girl]."
            elif s3_li == "Harry":
                "You reach out, wrap your fingers around his arm, and pull."
                harry @ talk "Agh!"
                "He lurches back, loses his balance and falls hard onto the seat."
                "Seb and Nicky let out a laugh. Elladine raises an eyebrow at you."
                harry @ awkward "Ow, my bum!"
                harry "These cushions are weirdly firm."
                "He looks at you with a puzzled expression."
                s3_mc "Sorry..."
                harry @ smile -sad "Don't worry. Look, I'm only going to be over there."
                s3_mc "But that's not here."
                "He gets back up and makes his way over to [s3_3rd_girl]."
        "Wave goodbye":
            "You slowly wave at [s3_li] as he makes his way over to [s3_3rd_girl]."
            "He turns, sees you, and does a small, reassuring wink."
            thought "There he goes..."
            "[s3_li] nods at [s3_3rd_girl]."

    if s3_li == "Bill":
        bill @ flirt "Alright, girl?"
        miki smile "I'm good, you?"
    elif s3_li == "Camilo":
        camilo @ flirt "Hiya, you alright?"
        iona smile "I'm good, you?"
    elif s3_li == "Harry":
        harry @ flirt "Hey! How are you doing?"
        genevieve smile "I'm good, you?"

    "[s3_li] shrugs. He and [s3_3rd_girl] share a clumsy hug."
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
        aj @ happy "Yay!"
        aj @ flirt "Single and ready to mingle, eh?"
        aj @ flirt "Guess we'll need to keep a close eye on you."
    else:
        aj @ smile "Ooh..."
        genevieve @ smile "Single and ready to mingle, eh?"
        genevieve @ smile "Guess we'll need to keep a close eye on you."

    "Nicky gets up and stretches."
    nicky -sad "I don't know about you lot, but my bum's gone numb."
    "He makes his way over to [s3_3rd_girl]."

    # CHOICE
    menu:
        thought "Should I go and talk to [s3_3rd_girl]?"
        "Walk over to [s3_3rd_girl]":
            scene s3-lawn-night with dissolve
            $ on_screen = []

            if s3_li == "Bill":
                "You make your way over to [s3_3rd_girl] along with Nicky, Genevieve and Iona."
                genevieve @ smile "Hey, girl!"
                miki @ smile "Hi!"
                nicky "Thought we'd come over and chat properly."
                "Iona gives you a sympathetic look before turning to [s3_3rd_girl]."
                iona "I hope you're alright. That was a tough decision for anyone to make."
                genevieve "Yeah, I'm so glad it wasn't me doing it."
                "[s3_3rd_girl] goes to speak, but looks at you instead."
                miki "Sorry, all. Can I have a quick word with [s3_name] first?"
            elif s3_li == "Camilo":
                "You make your way over to [s3_3rd_girl] along with Nicky, Miki and Genevieve."
                miki @ smile "Hey, girl!"
                iona @ smile "Hi!"
                nicky "Thought we'd come over and chat properly."
                "Genevieve gives you a sympathetic look before turning to [s3_3rd_girl]."
                genevieve "I hope you're alright. That was a tough decision for anyone to make."
                miki "Yeah, I'm so glad it wasn't me doing it."
                "[s3_3rd_girl] goes to speak, but looks at you instead."
                iona "Sorry, all. Can I have a quick word with [s3_name] first?"
            elif s3_li == "Harry":
                "You make your way over to [s3_3rd_girl] along with Nicky, Miki and Iona."
                miki @ smile "Hey, girl!"
                genevieve @ smile "Hi!"
                nicky "Thought we'd come over and chat properly."
                "Iona gives you a sympathetic look before turning to [s3_3rd_girl]."
                iona "I hope you're alright. That was a tough decision for anyone to make."
                miki "Yeah, I'm so glad it wasn't me doing it."
                "[s3_3rd_girl] goes to speak, but looks at you instead."
                genevieve "Sorry, all. Can I have a quick word with [s3_name] first?"
            nicky "Oh yeah, no problem."
            "Nicky winks at you as he ushers the others away... including [s3_li]."
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
            if s3_li == "Bill":
                miki serious "[s3_name]?"
                s3_mc "Huh?"
            elif s3_li == "Camilo":
                iona serious "[s3_name]?"
                s3_mc "Huh?"
            elif s3_li == "Harry":
                genevieve serious "[s3_name]?"
                s3_mc "Huh?"
        "Walk away from the others":
            scene s3-sun-loungers-night with dissolve
            $ on_screen = []
            "You get up, leaving the rest of the Islanders to form their own little groups."
            "The night is surprisingly chilly. You rub your arms for some warmth."
            "The sound of laughter drifts over from the other Islanders."
            # IF STATEMENT
            if s3_li == "Bill":
                miki "Cold?"
                "You turn and see Miki standing in front of you. A concerned look on her face."
                miki @ awkward "Me too. And I thought Cambridge could get chilly!"
                miki "Sometimes the boat's little heater isn't enough, you know?"
                "She rubs her arm."
            elif s3_li == "Camilo":
                iona "Cold?"
                "You turn and see Iona standing in front of you. A concerned look on her face."
                "She rubs her arm."
            elif s3_li == "Harry":
                genevieve "Cold?"
                "You turn and see Genevieve standing in front of you. A concerned look on her face."
                genevieve @ awkward "I nearly forgot to pack a cardigan for the colder evenings."
                "She rubs her arm."

    if s3_li == "Bill":
        miki serious "Um, I'd like to clear the air with you."
        s3_mc "Sure...let's talk."
        scene s3-poolside-night with dissolve
        $ on_screen = []
        miki @ smile "Thanks."
        miki serious "I want you to know that it wasn't anything personal. I mean, obviously, I've only just met you."
        if s3e1p2_talk_to_new_girl:
            miki "That's why I told you earlier who I was going to pick, so it wasn't a shock."
        else:
            miki "I wanted to tell you earlier, but we didn't get any time to chat."
            miki "I didn't want it to come as a shock."
        miki @ sad "At the end of the day, I had to pick someone."
        miki "But I actually think this puts you in a really strong position. You're now free to chat and flirt with whoever you want."
        miki smile "Even if that person is Bill. Like, all's fair. I won't make a fuss."
        miki "Early days and all that."
        "She pauses."
        miki "So...friends?"
    elif s3_li == "Camilo":
        iona serious "Um, I'd like to clear the air with you."
        s3_mc "Sure...let's talk."
        scene s3-poolside-night with dissolve
        $ on_screen = []
        iona @ smile "Thanks."
        iona serious "I want you to know that it wasn't anything personal. I mean, obviously, I've only just met you."
        if s3e1p2_talk_to_new_girl:
            iona "That's why I told you earlier who I was going to pick, so it wasn't a shock."
        else:
            iona "I wanted to tell you earlier, but we didn't get any time to chat."
            iona "I didn't want it to come as a shock."
        iona @ sad "At the end of the day, I had to pick someone."
        iona "But I actually think this puts you in a really strong position. You're now free to chat and flirt with whoever you want."
        iona smile "Even if that person is Camilo. Like, all's fair. I won't make a fuss."
        iona "Early days and all that."
        "She pauses."
        iona "So...friends?"
    elif s3_li == "Harry":
        genevieve serious "Um, I'd like to clear the air with you."
        s3_mc "Sure...let's talk."
        scene s3-poolside-night with dissolve
        $ on_screen = []
        genevieve @ smile "Thanks."
        genevieve serious "I want you to know that it wasn't anything personal. I mean, obviously, I've only just met you."
        if s3e1p2_talk_to_new_girl:
            genevieve "That's why I told you earlier who I was going to pick, so it wasn't a shock."
        else:
            genevieve "I wanted to tell you earlier, but we didn't get any time to chat."
            genevieve "I didn't want it to come as a shock."
        genevieve @ sad "At the end of the day, I had to pick someone."
        genevieve @ smile "But I actually think this puts you in a really strong position. You're now free to chat and flirt with whoever you want."
        genevieve -serious "Even if that person is Harry. Like, all's fair. I won't make a fuss."
        genevieve "Early days and all that."
        "She pauses."
        genevieve smile "So... friends?"

    # CHOICE
    menu:
        thought "Should I forgive [s3_3rd_girl] for choosing [s3_li]?"
        "Hey, it's fine. It was a tough call":
            $ s3_mc.like(s3_3rd_girl)
            "[s3_3rd_girl]'s shoulders relax with relief."
            if s3_li == "Bill":
                miki @ happy "Thanks, babe! You have no idea how awkward I was feeling."
                miki "You're so understanding."
                "She squeezes your arm lightly."
                miki "Come on, then. We should get back to the others."
            elif s3_li == "Camilo":
                iona "Thanks, babe! You have no idea how awkward I was feeling."
                iona -serious "You're so understanding."
                "She squeezes your arm lightly."
                iona "Come on, then. We should get back to the others."
            elif s3_li == "Harry":
                genevieve "Thanks, babe! You have no idea how awkward I was feeling."
                genevieve -serious "You're so understanding."
                "She squeezes your arm lightly."
                genevieve "Come on, then. We should get back to the others."
            "You walk back together."
        "I'm sorry, but I need some time":
            $ s3_mc.dislike(s3_3rd_girl)
            "[s3_3rd_girl] gaze falls to the ground. She lets out a heavy sigh."
            if s3_li == "Bill":
                miki @ sad "I understand..."
                miki serious "Look, I hope we can still be friends someday, you know?"
                s3_mc "Hmm."
                "She looks back at the others."
                miki -serious "Alright, I guess I should get back over there."
            elif s3_li == "Camilo":
                iona @ sad "I understand..."
                iona serious "Look, I hope we can still be friends someday, you know?"
                s3_mc "Hmm."
                "She looks back at the others."
                iona -serious "Alright, I guess I should get back over there."
            elif s3_li == "Harry":
                genevieve @ sad "I understand..."
                genevieve serious "Look, I hope we can still be friends someday, you know?"
                s3_mc "Hmm."
                "She looks back at the others."
                genevieve -serious "Alright, I guess I should get back over there."
            "[s3_3rd_girl] walks back on her own."
        "Relax, girl! I'd known him for two minutes":
            $ s3_mc.like(s3_3rd_girl)
            if s3_li == "Bill":
                miki @ talk "Hah!"
                "She tries to stop herself from laughing."
                miki @ awkward "Ah, I'm sorry..."
                miki "I'm just relieved."
                miki -smile "I really hate the idea of getting on the wrong side of someone in here."
                miki "Especially on the first day!"
                "A burst of laughter from the other group makes her turn her head."
                miki @ smile "Sounds like they're having fun. Come on, let's get back there."
            elif s3_li == "Camilo":
                iona @ talk "Hah!"
                "She tries to stop herself from laughing."
                iona @ awkward "Ah, I'm sorry..."
                iona "I'm just relieved."
                iona -smile "I really hate the idea of getting on the wrong side of someone in here."
                iona "Especially on the first day!"
                "A burst of laughter from the other group makes her turn her head."
                iona @ smile "Sounds like they're having fun. Come on, let's get back there."
            elif s3_li == "Harry":
                genevieve @ talk "Hah!"
                "She tries to stop herself from laughing."
                genevieve @ awkward "Ah, I'm sorry..."
                genevieve "I'm just relieved."
                genevieve -smile "I really hate the idea of getting on the wrong side of someone in here."
                genevieve "Especially on the first day!"
                "A burst of laughter from the other group makes her turn her head."
                genevieve @ smile "Sounds like they're having fun. Come on, let's get back there."
            "The two of you make your way to the others."

    scene s3-firepit-night with dissolve
    $ on_screen = []
    "Seb, Nicky, Elladine and Genevieve are sat around the firepit chatting"
    thought "I could do with someone to talk to."

    "{i}Island Amore isn't just about romance. It's also about the friendships you form along the way. One of these four Islanders is going to be a close friend for the rest of your time in the Villa.{/i}"

    thought "People can get attached pretty quickly in this Villa. I should think about who I want to be friends with..."
    thought "I don't think I've ever met anyone as positive as Elladine."
    thought "I feel like she's the kind of person that always has a funny story to share or a comfortable shoulder to cry on."
    if s3_li == "Harry":
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
            # ADJUST AFTER REFACTORING
            $ s3_bff = "Elladine"
            $ s3_mc.bff = 'Elladine'
        "Genevieve":
            # ADJUST AFTER REFACTORING
            $ s3_bff = "Genevieve"
            $ s3_mc.bff = 'Genevieve'
        "Nicky":
            # ADJUST AFTER REFACTORING
            $ s3_bff = "Nicky"
            $ s3_mc.bff = 'Nicky'
        "Seb":
            # ADJUST AFTER REFACTORING
            $ s3_bff = "Seb"
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
    aj @ smile "What?"
    "You try to speak again but a dribble of toothpaste makes it's way down your chin instead."
    "You quickly wipe it away."
    s3_mc "Whurlps!"
    aj @ smile "Hah! Gross."
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
        show aj smile
        "AJ giggles."
    "She gestures to the sink. You quickly rinse your mouth."
    s3_mc "Thanks."
    "AJ does the same."
    aj -smile -awkward "No problem."
    "She grins at you as she wipes her mouth with her towel."
    aj "Ahh, minty fresh."
    aj "I asked how's things?"

    # CHOICE
    menu:
        s3_mc "Things are..."
        "Great!":
            aj @ smile "Glad to hear it."
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
                aj @ smile -awkward "Don't ask, don't get, right?"
            "One hundred percent yes":
                $ s3_mc.like("AJ")
                $ s3_like_aj = True
                $ s3_lis.append("AJ")
                aj @ happy "Amazing!"
                show aj awkward
                "She looks at you, her cheeks flushing again."
                show aj smile
                "AJ looks at you and laughs."
                s3_mc "What's wrong?"
                aj -smile -awkward "Oh, nothing, really."
                s3_mc "Really?"
                aj @ flirt "Yeah, you look gorgeous as usual."
                aj  "But you've just got a tiny stray lash on your face."
                aj @ flirt "Stay still, I'll get it for you."
                "She moves closer. You can feel her breath on your cheek."
                "She gently removes the eyelash from your face and blows it to one side."
                aj @ smile "I made a wish on that eyelash, by the way."
        
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
                aj @ happy "Because my wish just totally came true."
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
                aj @ smile "To kiss you."
                s3_mc "I gathered."
            "Change the subject":
                "EMPTY"
                # NEED TO FILL
        aj @ talk "It is such a weird tradition, isn't it?"
        aj "I bet someone from ages ago, like, made a wish after finding an eyelash and it came true and they told all their mates."
        aj @ smile "And now we all believe in the power of the eyelash."
        "AJ smiles at you."
        aj @ flirt "I hope we get to spend more time together in the Villa."
        aj @ smile "Being alone with you is like..."
        aj @ awkward "I don't know how to describe it with, like, words and stuff..."
        aj @ flirt "But I know I want more of it."
    else:
        aj "So, you got your eye on any of the guys here?"
        # CHOICE
        menu:
            thought "Which guy do I have my eye on?"
            "Harry":
                $ s3_mc.like("AJ")
                $ s3_mc.like("Harry")
                aj @ smile "Ooh, he's well cute and a right laugh!"
                aj "He likes to swim like me, too!"
                if s3_li == "Harry":
                    aj "It sucks that you don't get to spend your first night here with him."
            "Camilo":
                $ s3_mc.like("AJ")
                $ s3_mc.like("Camilo")
                aj @ smile "Can't fault you there!"
                aj "Strong athletic type with a heart of gold."
                "She swoons dramatically."
                if s3_li == "Camilo":
                    aj "It sucks that you don't get to spend your first night here with him."
            "Bill":
                $ s3_mc.dislike("AJ")
                $ s3_mc.like("Bill")
                aj @ talk "Hah! Really?"
                aj @ awkward "Sorry, that was well rude."
                aj "It's just, he's got an opinion on everything!"
                aj "Though, he's kinda funny, I'll give you that."
                if s3_li == "Bill":
                    aj "It sucks that you don't get to spend your first night here with him."
            "Nobody so far...":
                s3_mc "I definitely don't get a romantic vibe off Nicky or Seb, and none of the other three really stand out yet..."
                aj @ smile "Well, I'm sure there are more to come."

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
    aj @ smile "I guess we should go."

    scene sand with dissolve
    $ on_screen = []

    "Don't fret, [s3_name]! So, you've lost [s3_li], but at least you've got a bed!"
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
    elladine @ smile "Hey, [s3_name]!"
    if s3_li == "Harry":
        genevieve @ smile "Join us! We're staying close to the fire for warmth."
        seb "Yeah, right? I thought it'd be baking."
        seb "Didn't realise I'd need a fluffy onesie at night"
    s3_mc "Hey, [s3_mc.bff]..."

    $ pronouns(s3_mc.bff)
    $ s3_mc.like(s3_mc.bff)
    if s3_mc.bff == "Elladine":
        elladine "Yeah?"
        s3_mc "Could I speak to you in private?"
        elladine @ smile "Of course, hun!"
        elladine "Roof terrace?"
        s3_mc "Sounds good!"
        "The two of you make your way upstairs."
    elif s3_mc.bff == "Genevieve":
        genevieve "Yeah?"
        s3_mc "Could I speak to you in private?"
        genevieve @ smile "Of course, babes!"
        genevieve "Roof terrace?"
        s3_mc "Sounds good!"
        "The two of you make your way upstairs."
    elif s3_mc.bff == "Nicky":
        nicky "Yeah?"
        s3_mc "Could I speak to you in private?"
        nicky @ smile "Yeah, man. Let's go."
        nicky "Roof terrace?"
        s3_mc "Sounds good!"
        "The two of you make your way upstairs."
    elif s3_mc.bff == "Seb":
        seb "Yeah?"
        s3_mc "Could I speak to you in private?"
        seb @ smile "Yeah, man. Let's go."
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
    if s3_mc.bff == "Genevieve" and s3_li == "Harry":
        "After having Harry taken from her by Genevieve, [s3_name]'s made the interesting decision to confide in her."
        "Could this be the start of a beautifully awkward friendship?"
    else:
        "After having [s3_li] taken from her, [s3_name] and [s3_mc.bff] have come to the terrace to talk it over."
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
                genevieve @ smile "My full title is actually Doctor Aliu, but I like Doctor Viv."
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
            
    if s3_mc.bff == "Genevieve" and s3_li == "Harry":
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
                elladine @ smile -serious "Exactly! You're thinking smart here."
            elif s3_mc.bff == "Genevieve":
                genevieve @ smile -serious "Exactly! You're thinking smart here."
            elif s3_mc.bff == "Nicky":
                nicky @ smile -serious "Exactly! You're thinking smart here."
            elif s3_mc.bff == "Seb":
                seb @ smile -serious "Exactly! You're thinking smart here."
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
                genevieve @ smile -serious "Good to see it hasn't dampened your spirit."
            elif s3_mc.bff == "Seb":
                "Seb laughs."
                seb @ smile -serious "Good to see it hasn't dampened your spirit."
            elif s3_mc.bff == "Nicky":
                "Nicky laughs."
                nicky @ smile -serious "Good to see it hasn't dampened your spirit."
            elif s3_mc.bff == "Elladine":
                "Elladine laughs."
                elladine @ smile -serious "Good to see it hasn't dampened your spirit."

    # IF STATEMENT
    if s3_mc.bff == "Elladine":
        "Elladine smiles at you."
        elladine "Want to know what I think?"
        s3_mc "Go on."
        elladine @ talk "The way I see it, you're actually in one of the best positions in the Villa."
        elladine "You can graft on whoever you want to now, and no one can really have a problem with you for it."
        elladine "You can get to know everyone before the next recoupling!"
        elladine @ smile "I'd say that's better than pairing up with a stranger straight away."
    elif s3_mc.bff == "Genevieve":
        "Genevieve smiles at you."
        genevieve "Want to know what I think?"
        s3_mc "Go on."
        genevieve @ talk "The way I see it, you're actually in one of the best positions in the Villa."
        genevieve "You can graft on whoever you want to now, and no one can really have a problem with you for it."
        genevieve "You can get to know everyone before the next recoupling!"
        genevieve @ smile "I'd say that's better than pairing up with a stranger straight away."
    elif s3_mc.bff == "Nicky":
        "Nicky stretches and lays his arm down across the top of the seat."
        nicky "Do you want to hear what I think about your situation?"
        s3_mc "Go on."
        nicky @ talk "The way I see it, you're actually in one of the best positions in the Villa."
        nicky "You can graft on whoever you want to now, and no one can really have a problem with you for it."
        nicky "You can get to know everyone before the next recoupling!"
        nicky @ smile "I'd say that's better than pairing up with a stranger straight away."
    elif s3_mc.bff == "Seb":
        "Seb coughs and tucks his hair behind his ear"
        seb "So, um, I've been thinking about your situation..."
        s3_mc "Go on."
        seb @ talk "The way I see it, you're actually in one of the best positions in the Villa."
        seb "You can graft on whoever you want to now, and no one can really have a problem with you for it."
        seb "You can get to know everyone before the next recoupling!"
        seb @ smile "I'd say that's better than pairing up with a stranger straight away."

    # CHOICE
    menu:
        thought "[s3_mc.bff] thinks that being single at the start is better..."
        "You make a good point":
            if s3_mc.bff == "Elladine":
                elladine smile "Of course I do. I'm a fountain of knowledge."
            elif s3_mc.bff == "Genevieve":
                genevieve smile "Of course I do. I'm a fountain of knowledge."
            elif s3_mc.bff == "Nicky":
                nicky smile "Of course I do. I'm a fountain of knowledge."
            elif s3_mc.bff == "Seb":
                seb smile "There's a first time for everything."
        "But what if I already like [s3_li]?":
            if s3_mc.bff == "Elladine":
                elladine @ talk "Then go out and get him back!"
                elladine "Tomorrow is when the real grafting starts. You've just gotta keep your eyes on the prize."
            elif s3_mc.bff == "Genevieve" and s3_li == "Harry":
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
                elladine @ smile "Yeah, you are!"
                "She pokes you in the ribs."
            elif s3_mc.bff == "Genevieve":
                genevieve @ smile "That makes me happy to hear."
            elif s3_mc.bff == "Nicky":
                nicky @ smile "Yeah, you are!"
                "He pokes you in the ribs."
            elif s3_mc.bff == "Seb":
                seb @ smile "That makes me happy to hear."

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
                if s3_li == 'Harry':
                    pass
                else:
                    genevieve "Girl, you've got nothing to worry about."
                    genevieve @ smile "[s3_3rd_girl] has got nothing on you."
                    genevieve "I'm sure you're still in with a chance to win him back!"
            "Don't forget about the prize money":
                genevieve @ happy "Ha!"
                "She playfully nudges you in the shoulder."
                s3_mc "What? Everyone knows that's the real treasure around here."
                "[s3_mc.bff] smiles and shrugs."
                genevieve "You're not wrong."
                genevieve @ flirt "I wouldn't mind a piece of that cash either."
            "But sex marks the spot":
                "[s3_mc.bff] snorts with laughter. "
                genevieve @ happy "Sex marks the spot?"
                s3_mc "You bet it does on my treasure spot."
                "You stick your tongue into your cheek."
                genevieve "OK wow!"
                genevieve @ flirt "[s3_name] you're filthy and I love it."

        if s3_li == "Harry":
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
                    genevieve @ smile -serious "Ha. I'm glad you see it that way."
                "I'd appreciate a sorry":
                    "EMPTY"
                    # NEED TO FILL
                "That's just how it goes in here":
                    "EMPTY"
                    # NEED TO FILL
            genevieve @ smile "I'm just glad we can still be friends."
            s3_mc "Me too."
            "She gives you a big, friendly smile."
            genevieve "Wow, that brought the mood down, huh?"
            genevieve serious "I guess I just worry more when it's dark."

        "Genevieve bites her thumbnail absentmindedly."
        genevieve serious "I'm like, such a night warrior and a worrier."
        s3_mc "A worrying night warrior."
        genevieve @ smile -serious "Yeah, that should be my superhero name at work or something."
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
                genevieve @ smile "Awh, that's so cool."
                genevieve "It's a pretty full on job, but someone's gotta do it, right?"
            "Rubbish! I thought you didn't like the dark?":
                genevieve @ happy "You'd think, wouldn't you?"
                genevieve @ smile "But actually it's perfect."

        genevieve "I love that I'm surrounded by people."
        genevieve @ smile "It's literally constant when you're working as a doctor at a festival."
        genevieve "Can't stand how quiet and dark hospitals can get."
        genevieve @ awkward "I bet this place will be a bit spooky, like, late at night."
        genevieve "It'd be easier if there were more people."
        s3_mc "What was the third thing?"
        "Genevieve looks puzzled."
        genevieve @ awkward "You know what?"
        genevieve @ smile "For the life of me I can't remember."
        genevieve "It's because it's getting late."
        genevieve "I'm just getting restless."

        # CHOICE
        menu:
            thought "Genevieve struggles settling down at night."
            "Don't worry, I'll look out for you!":
                $ s3_mc.like("Genevieve")
                genevieve @ smile "Awh, really?"
                genevieve @ smile "Means a lot, I'm not going to lie."
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
        elladine @ smile "A group of fit boys all wanting to get with us!"
        
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
                nicky @ smile "Though I reckon you could out-sass her, if it came down to it."
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
                show nicky happy
                "He laughs. You give him your best serious face, which makes him laugh more."
            "I can't help it, it just happens":
                s3_mc "I've literally never tried to be that girl, but people just..."
                s3_mc "Well, people seem to lose their common sense a bit when I'm around."
                nicky "Yup. That's what I thought."
            "I've never had drama in my life":
                # NEED TO FILL
                "EMPTY"

        nicky -happy "Don't get me wrong, I think it's a good thing."
        nicky "Interesting things happen to interesting people."
        nicky @ smile "You're rich in personality. It's a blessing and a curse."
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
                seb @ smile "Hey, respect."

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
                $ s3_mc.like("Seb")
                s3_mc "If you don't get on with your parents, there's no obligation to pretend."
                seb @ smile -sad "Thanks for that. Not everybody gets it."
                seb "It's not that we hate each other or anything. We just don't have much in common."
                seb "And I don't have any brothers or sisters to keep in touch with, or anything like that."
            "Why not reach out to them?":
                $ s3_mc.dislike("Seb")
                s3_mc "At the end of the day, they're still your parents. I'm sure they'd really appreciate it."
                seb "Nah, I'm not sure they would."
                seb @ talk "It's not that we hate each other or anything. We just don't have much in common."
                seb "And I don't have any brothers or sisters to keep in touch with, or anything like that."
            "You can have one of mine":
                s3_mc "I've got more than I need. You'd be doing me a favour."
                seb @ smile -sad"That's very generous of you."
                seb "Plus, then we'd be brother and sister. I've always kinda wondered what that would be like."

        s3_mc "You're an only child?"
        seb -sad "Yep. It was a bit lonely growing up, but it made me an independent spirit. I've always done my best work alone."
        seb "That's why I opened my shop in the first place, you know?"
        seb "Running a small business is tough, but it suits me."
        seb "I'm not good at being part of someone else's team."
        seb @ smile "I like to do things my way."
        s3_mc "But you can't run a shop all by yourself, right? You must have employees."
        seb "Well, yeah. There's my second-in-command, Doom."
        s3_mc "Doom?"
        seb @ flirt "So...remember that story earlier, about how I rescued a cat from a burning tree?"
        seb "The rest of the story is that I adopted the cat and named her Doom."
        seb "And now she helps out around the shop."
        seb @ smile "Well, she mostly sleeps on the counter and meows at the customers."
        seb "But she's good at it."

        # CHOICE
        menu:
            thought "Seb's shop assistant is his cat..."
            "That's adorable":
                s3_mc "I would love it if I went into a shop and there was a cat asleep on the counter! I would shop there all the time!"
                seb @ happy "Really?"
                s3_mc "Yeah, I think it's awesome!"
                "Seb grins."
                seb @ smile "I guess it is pretty cute."
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
        seb @ smile "She's actually expecting kittens soon."
        s3_mc "Oh my gosh, really?"
        seb @ happy "Yeah! It's bad timing, 'cause I might not get to be there when they're born..."
        seb "But I'm well excited."

    scene s3-lawn-night with dissolve
    $ on_screen = []

    "The sound of the other Islanders draws your attention away from [s3_mc.bff]."
    bill "Right, I don't know about the rest of you, but I'm cream-crackered."
    miki @ talk "You're a cream cracker?"
    camilo smile "Hah! He is now. That's brilliant."
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
        elladine @ smile -awkward "What about a prank?"
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
        genevieve @ smile -awkward "What about a prank?"
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
        nicky @ smile -awkward "What about a prank?"
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
        seb @ smile -awkward "What about a prank?"
        s3_mc "Do you have anything in mind?"
        seb "Well, if we want to do it before bed, it's got to be something simple and classic."
        seb "What about if you hide somewhere and jump out at someone?"
        seb "I can keep them distracted while you get ready. What do you say?"

    thought "Do I want to make one of the other Islanders jump? It could be a cute start to my single gal mischief..."

    # CHOICE
    menu:
        thought "It might be a good chance to get some alone time with someone, too..."
        "That sounds hilarious! Let's do it":
            $ s3_mc.like(s3_mc.bff)
            $ s3e1p3_prank = True
            if s3_mc.bff == "Elladine":
                elladine @ happy "Yes! This'll be so fun."
            elif s3_mc.bff == "Genevieve":
                genevieve @ happy "Yes! This'll be so fun."
            elif s3_mc.bff == "Nicky":
                nicky @ happy "Yes! This'll be so fun."
            elif s3_mc.bff == "Seb":
                seb @ happy "Yes! This'll be so fun."
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
            elladine @ smile "Alright, go time! You hide. I'll go and keep them busy."
        elif s3_mc.bff == "Genevieve":
            genevieve @ smile "Alright, go time! You hide. I'll go and keep them busy."
        elif s3_mc.bff == "Nicky":
            nicky @ smile "Alright, go time! You hide. I'll go and keep them busy."
        elif s3_mc.bff == "Seb":
            seb @ smile "Alright, go time! You hide. I'll go and keep them busy."
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

    $ pronouns(s3e1p3_prankee)

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
                aj @ smile "Nice one."
            elif s3e1p3_prankee == "Bill":
                s3_mc "Argh!"
                "[he_she!c] looks down at you in bemusement."
                bill "Um, what?"
                s3_mc "...Boo?"
                bill @ smile "Nice one."
            elif s3e1p3_prankee == "Camilo":
                s3_mc "Argh!"
                "[he_she!c] looks down at you in bemusement."
                camilo "Um, what?"
                s3_mc "...Boo?"
                camilo @ smile "Nice one."
            elif s3e1p3_prankee == "Harry":
                s3_mc "Argh!"
                "[he_she!c] looks down at you in bemusement."
                harry "Um, what?"
                s3_mc "...Boo?"
                harry @ smile "Nice one."


        "Grab [his_her] ankle" if s3e1p3_prankee in ['Bill', 'Camilo', 'Harry']:
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

        "Wait for [him_her] to open the cupboard" if s3e1p3_prankee == 'AJ':
            "You sink further into the clothes as AJ gets closer and closer."
            aj "I can't wait to throw on some cosy PJs!"
            aj "It was so cold coming out of the pool..."
            aj @ awkward "...Why am I talking to myself?"
            "She slides the door open and you make your move."
            s3_mc "Boo!"
            aj @ talk "Woah!"
            "AJ jumps back and then laughs."
            aj "You got me good...."
            aj @ smile "Nice one."

    # IF STATEMENT
    if s3e1p3_prankee == "AJ":
        aj @ smile "That was a good effort, but it's going to take more than that to rattle me."
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
        bill @ smile "Maybe I'll get you back by hiding in your bed?"
        # CHOICE
        menu:
            thought "Bill hiding in my bed..."
            "Sounds more like a dream come true":
                $ s3_mc.like("Bill")
                bill @ flirt "That's what I was hoping you'd say..."
            "You in my bed would be terrifying":
                $ s3_mc.dislike("Bill")
                bill @ smile "Damn right!"
                bill awkward "Um... wait."
                "He frowns."
            "Is that an invitation?":
                bill @ flirt "It can be if you want..."
        bill -awkward "You realise I have to get you back for this, right?"
    elif s3e1p3_prankee == "Camilo":
        camilo @ smile "You're lucky my reflexes didn't kick in!"
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
                harry smile "Just as long as it's cosy, you get me?"
            "There won't be a next time":
                $ s3_mc.dislike("Harry")
                harry @ awkward "Shame."
                harry -flirt "Could've been a great bonding opportunity."
            "Wouldn't it be better to be in bed?":
                $ s3_mc.like("Harry")
                harry "Hmm, true."
                harry smile "A lot more space to move around in..."         
        harry -smile "You realise I have to get you back for this, right?"

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
    if s3_li == "Bill":
        miki serious "The boy I'd like to couple up with is..."
        miki smile "[s3_li]."
        show miki at npc_exit
    elif s3_li == "Camilo":
        iona serious "The boy I'd like to couple up with is..."
        iona smile "[s3_li]."
        show iona at npc_exit
    elif s3_li == "Harry":
        genevieve serious "The boy I'd like to couple up with is..."
        genevieve smile "[s3_li]."
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
    harry @ smile "Morning, sunshine."
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
                elladine @ smile "Ha! Good aim."
            elif s3_mc.bff == "Genevieve":
                genevieve @ smile "Ha! Good aim."
            elif s3_mc.bff == "Nicky":
                nicky @ smile "Ha! Good aim."
            elif s3_mc.bff == "Seb":
                seb @ smile "Ha! Good aim."

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
    elif s3_li == "Bill":
        bill @ flirt "I said we should all get in bed with you and spoon you."
    elif s3_li == "Camilo":
        camilo @ flirt "I said we should all get in bed with you and spoon you."
    elif s3_li == "Harry":
        harry @ flirt "I said we should all get in bed with you and spoon you."

    s3_mc "Really?"
    miki "Yeah, we didn't want you to have to wake up on your own."
    genevieve @ sad "That would be awful..."
    genevieve @ smile "But you don't have to because you've got us!"

    # CHOICE
    menu:
        thought "The Islanders waited for me to wake up!"
        "That's so cute, thank you!":
            if s3_mc.bff == "Elladine":
                elladine @ smile "Any time, [s3_name]!"
            elif s3_mc.bff == "Genevieve":
                genevieve @ smile "Any time, [s3_name]!"
            elif s3_mc.bff == "Nicky":
                nicky @ smile "Any time, [s3_name]!"
            elif s3_mc.bff == "Seb":
                seb @ smile "Any time, [s3_name]!"

        "What are we waiting for? Let's get up":
            harry "Yeah, we should."

        "I'd rather be spooning with [s3_li]" if s3_like_aj == False:
            $ s3e2p1_want_spoon = True
            $ s3_mc.like(s3_li)
            "[s3_li] catches your eye for a moment, and grins."
        
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

    return

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
        "Chuck it at [s3_li]":
            "You lob it at [s3_li]."
            if s3_li == "Bill":
                bill awkward "Hey!"
            elif s3_li == "Camilo":
                camilo awkward "Hey!"
            elif s3_li == "Harry":
                harry awkward "Hey!"
            "You point at Nicky and Seb."
            s3_mc "They started it!"

    "A phone beeps."
    iona @ talk "Oh, I got a text."
    text "Islanders, get ready for some one-on-one time! This afternoon, each of the boys will be choosing someone to take out on a date. #comedatewithme #datesormates"
    harry @ happy "Yes!"
    harry "We've got to date whichever girls we want!"
    harry @ smile "Right on."
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

    jump s3e2p2
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
        elladine @ smile "Nicky is such a sweetheart bringing me breakfast like this."
        genevieve "Yeah, he seems like a good guy."
    else:
        "Elladine is looking towards the kitchen."
        elladine "I should get some food soon, I'm hungry..."

    "Genevieve smiles at you as you sit down."
    genevieve "Hey, hun."
    genevieve "We were just chatting about Harry."

    # IF STATEMENT
    if s3_li == "Harry":
        genevieve sad "I hope you're OK with that after last night."
        elladine serious "Yeah, we don't want you to feel awks, hun."
        # CHOICE
        menu:
            thought "How am I feeling about Genevieve and Harry?"
            "Yeah, it's all good":
                genevieve @ smile "Good."

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
            if s3_li == "Harry":
                genevieve "I know, I know."
                genevieve "I'm sorry, I'm sure that's, like, really annoying to hear coming from me."
            else:
                genevieve "Yeah, we'll see."

        "He's not my cup of tea":
            genevieve "I think we're on the same wavelength."
        "Good, he's all mine then":
            elladine @ awkward "Woah, [s3_name]!"
            s3_mc "What? I like what I see and I want what I see."
            if s3_li == "Bill" or s3_li == "Camilo":
                genevieve @ talk "You like him?"
                s3_mc "Yeah. I do."
                genevieve "Oh, I had no idea."
                genevieve "You were with [s3_li] this time yesterday."
            elif s3_li == "Harry":
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
            show genevieve happy
            show elladine happy
            "Genevieve and Elladine laugh."
            genevieve @ smile -happy "OK, yeah, we've all been there."
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
    if s3_li == "Bill":
        camilo "I can't believe Bill has had two girls pick him already."
        harry "Yeah, two gorgeous girls."
        aj "Alright, alright, you two."
        if s3_like_aj:
            aj "Did you sleep OK, like, on your own and stuff, [s3_name]?"
        else:
            harry "Did you sleep OK, like, on your own and stuff, [s3_name]?"
    elif s3_li == "Camilo":
        camilo "I just can't believe my luck."
        camilo "Two beautiful girls have chosen me already."
        "Harry splashes Camilo."
        harry "Don't brag about it, mate."
        camilo "Honestly, it's my Latino charm."
        camilo "I can't help it."
        if s3_like_aj:
            aj "Did you sleep OK, like, on your own and stuff, [s3_name]?"
        else:
            harry "Did you sleep OK, like, on your own and stuff, [s3_name]?"
        camilo "Yeah."
        camilo "I was annoyed I didn't get to spoon you last night."
    elif s3_li == "Harry":
        harry "So, just to keep you in the loop, Camilo."
        harry "Two gorgeous girls have picked me already."
        "Camilo splashes Harry."
        harry "Hey!"
        camilo "Sorry, just cooling you off."
        if s3_like_aj:
            aj "Did you sleep OK, like, on your own and stuff, [s3_name]?"
        else:
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
        "I'd have slept better if [s3_li] was there":
            $ s3_mc.like(s3_li)
            if s3_li == "Bill":
                # NEED TO FILL
                "EMPTY"
            elif s3_li == "Camilo":
                camilo "Oh, wow. That's so cute, [s3_name]."
                camilo "You know, I have been told to make a great hot water bottle."
            elif s3_li == "Harry":
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
            if s3_li == "Bill" or s3_li == "Harry":
                camilo "Hold on tight."
            elif s3_li == "Camilo":
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

    if s3_li == "Bill":
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
            $ s3_mc.like("Bill")
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

    if s3_li == "Bill":
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
            $ s3_like_bill = False
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

    elladine "Let's not forget, [s3_name] was coupled up with [s3_li] first, until [s3_3rd_girl] came along."
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

    if s3_li == s3e2p2_first_date:
        aj "Oh, yeah. Makes sense."
        aj "Since you were coupled with him, and everything."
    else:
        if s3_li == "Bill":
            aj "Oh, I thought you were going to say Bill."
        elif s3_li == "Camilo":
            aj "Oh, I thought you were going to say Camilo"
        elif s3_li == "Harry":
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

    $ s3_mc.like(s3e2p2_first_date)

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
                    $ s3_mc.like("Bill")
                    s3_mc "He was really sweet and funny. I had a great time."
                    s3_mc "And I'm pretty sure he did, too."
                    s3_mc "I definitely think there's something developing there."
                    elladine "That's so exciting!"
                    seb "He's gonna be made up when we tell him you said that."
                    "Miki bites her lips and looks away."
                "Camilo" if s3e2p2_first_date == 'Camilo' or s3e2p2_second_date == 'Camilo' or (s3e2p2_third_date == 'Camilo' and s3e2p2_only_two_dates == False):
                    $ s3e2p2_special_spark = "Camilo"
                    $ s3_mc.like("Camilo")
                    s3_mc "He was really sweet and funny. I had a great time."
                    s3_mc "And I'm pretty sure he did, too."
                    s3_mc "I definitely think there's something developing there."
                    elladine "That's so exciting!"
                    seb "He's gonna be made up when we tell him you said that."
                    "Iona frowns, but doesn't say anything."
                "Harry" if s3e2p2_first_date == 'Harry' or s3e2p2_second_date == 'Harry' or (s3e2p2_third_date == 'Harry' and s3e2p2_only_two_dates == False):
                    $ s3e2p2_special_spark = "Harry"
                    $ s3_mc.like("Harry")
                    s3_mc "He was really sweet and funny. I had a great time."
                    s3_mc "And I'm pretty sure he did, too."
                    s3_mc "I definitely think there's something developing there."
                    elladine "That's so exciting!"
                    seb "He's gonna be made up when we tell him you said that."
                    "Genevieve sighs softly, but doesn't say anything."
                "AJ" if s3_like_aj == True:
                    $ s3e2p2_special_spark = "AJ"
                    $ s3_mc.like("AJ")
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

    if s3_li != "Bill":
        s3_mc "I'll drink to that."

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
            if s3_li != "Bill":
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

    if s3_li == "Bill":
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

    if s3e2p2_reject_bill:
        "He gives you a friendly nod as he leaves."
    else:
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
        s3_mc "Yeah, rehearsing for hours almost every day can make it a bit hard to go out sometimes."
    elif s3_mc.job == "Athlete":
        s3_mc "Yeah, training for hours almost every day can make it a bit hard to go out sometimes."

    camilo "Well, you never know. Maybe you'll make some new friends while you're in the Villa."

    if s3_li == "Camilo":
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
        camilo "She seems like a real chill girl. I'm glad you two are hitting it off."
    elif s3_mc.bff == "Genevieve":
        camilo "She seems like a real chill girl. I'm glad you two are hitting it off."
    elif s3_mc.bff == "Nicky":
        camilo "He seems like a real chill guy. I'm glad you two are hitting it off."
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
    
    if s3e1p1_cheeky_snog and s3_li == "Camilo":
        camilo "When we had that kiss."
    elif s3_li == "Camilo":
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
        if s3_li == "Camilo" or s3_like_camilo == True:
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
    if s3_li == "Harry":
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

    if s3e1p1_cheeky_snog and s3_li == "Harry":
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
            if s3_like_aj:
                aj "Well, if you're ever in my flat, maybe I'll show you."
                aj "Just make sure you eat before you come round."
            else:
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
            $ s3_mc.dislike("Seb")
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
            aj "It was just an inconvenience with a smile ending..."
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
        "Coupling up with [s3_li]":
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
        "You turn just in time to see the pasta leave [s3_li]'s hand before it hits you in the chest."
        nicky "Hah-hah!"
    elif s3_mc.bff == "Seb" and s3e2p3_first_vistim == "Seb":
        "You turn just in time to see the pasta leave [s3_li]'s hand before it hits you in the chest."
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