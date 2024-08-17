#########################################################################
## Episode 5, Part 1
#########################################################################
label s3e5p1:
    scene sand with dissolve
    $ on_screen = []

    show screen day_title(5, 1) with Pause(4)
    hide screen day_title with dissolve

    "Last time on Love Island..."
    "The Islanders made a lot of puns."

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

    "That's supposed to be my job! But I'm not angry. I'm a really relaxed guy."
    "Get it? Guy? Like a guy rope?"
    "...."
    "Anyway."
    "Today..."
    "There's a big surprise in store for [s3_name]."
    "Well, three big surprises."
    "Well, one very big surprise, one slightly smaller surprise, and one rather petite surprise."
    "Think Goldilocks and the Three Bears, except instead of Goldilocks it's [s3_name], and instead of bears it's surprises."
    "Look, it'll make sense in a bit. Just trust me."

    $ pronouns(s3_mc.current_partner)

    if s3e4p2_decorate_tent:
        scene s3-inside-tent-premium-day
    else:
        scene s3-inside-tent-standard-day
    $ new_scene()

    $ outfit = "pjs"

    "When you open your eyes, [s3_mc.current_partner] is already awake."
    "[he_she!c]'s lying on his back, staring at the roof of the tent."
    s3_mc "Morning."

    if s3_mc.current_partner == "Bill":
        bill "Oh, hey! Morning, babe."
        bill "Sorry. I woke up early for some reason, and then I couldn't get back to sleep, so I've just been lying here."
    elif s3_mc.current_partner == "Camilo":
        camilo "Oh, hey! Morning, babe."
        camilo "Sorry. I woke up early for some reason, and then I couldn't get back to sleep, so I've just been lying here."
    elif s3_mc.current_partner == "Harry":
        harry "Oh, hey! Morning, babe."
        harry "Sorry. I woke up super early like I always do, to do my affirmations."
        harry "But I need a mirror to do them properly, and I didn't want to sneak off back to the Villa and leave you all alone."
        harry "So, I've kinda just been lying here."
    elif s3_mc.current_partner == "AJ":
        aj "Oh, hey! Morning, babe."
        aj "Sorry. I woke up early for some reason, and then I couldn't get back to sleep, so I've just been lying here."

    if s3_mc.current_partner == "Bill":
        if s3e4p2_decorate_tent or s3e4p2_good_tent:
            bill "I'm actually really comfy! Our tent is the best."
        else:
            bill "It's not the most comfortable, to be honest. Our tent kinda sucks."
            bill "I wanted to wake you up. But I thought you deserved a lie in, so I've been trying not to fidget too much."
    elif s3_mc.current_partner == "Camilo":
        if s3e4p2_decorate_tent or s3e4p2_good_tent:
            camilo "I'm actually really comfy! Our tent is the best."
        else:
            camilo "It's not the most comfortable, to be honest. Our tent kinda sucks."
            camilo "I wanted to wake you up. But I thought you deserved a lie in, so I've been trying not to fidget too much."
    elif s3_mc.current_partner == "Harry":
        if s3e4p2_decorate_tent or s3e4p2_good_tent:
            harry "I'm actually really comfy! Our tent is the best."
        else:
            harry "It's not the most comfortable, to be honest. Our tent kinda sucks."
            harry "I wanted to wake you up. But I thought you deserved a lie in, so I've been trying not to fidget too much."
    elif s3_mc.current_partner == "AJ":
        if s3e4p2_decorate_tent or s3e4p2_good_tent:
            aj "I'm actually really comfy! Our tent is the best."
        else:
            aj "It's not the most comfortable, to be honest. Our tent kinda sucks."
            aj "I wanted to wake you up. But I thought you deserved a lie in, so I've been trying not to fidget too much."

    # CHOICE
    menu:
        thought "[s3_mc.current_partner] was trying not to wake me up..."
        "That's so thoughtful":
            s3_mc "Thanks for letting me sleep."
            s3_mc "I hope you didn't get too bored here by yourself."
            if s3_mc.current_partner == "Bill":
                bill "It's been alright."
            elif s3_mc.current_partner == "Camilo":
                camilo "It's been alright."
            elif s3_mc.current_partner == "Harry":
                harry "It's been alright."
            elif s3_mc.current_partner == "AJ":
                aj "It's been alright."
        "Wake me up next time":
            s3_mc "If you can't sleep, I wanna keep you company!"
            s3_mc "I hope you didn't get too bored here by yourself."
            if s3_mc.current_partner == "Bill":
                bill "It's been alright."
            elif s3_mc.current_partner == "Camilo":
                camilo "It's been alright."
            elif s3_mc.current_partner == "Harry":
                harry "It's been alright."
            elif s3_mc.current_partner == "AJ":
                aj "It's been alright."
        "Viv already woke me up in the night":
            if s3_mc.current_partner == "Bill":
                bill "Really? What did she want?"
                s3_mc "I'm not really sure. It was all a bit dreamlike."
                bill "Weird. I dunno what that's about."
            elif s3_mc.current_partner == "Camilo":
                camilo "Really? What did she want?"
                s3_mc "I'm not really sure. It was all a bit dreamlike."
                camilo "Weird. I dunno what that's about."
            elif s3_mc.current_partner == "Harry":
                harry "Really? What did she want?"
                s3_mc "I'm not really sure. It was all a bit dreamlike."
                harry "Weird. I dunno what that's about."
            elif s3_mc.current_partner == "AJ":
                aj "Really? What did she want?"
                s3_mc "I'm not really sure. It was all a bit dreamlike."
                aj "Weird. I dunno what that's about."

    if s3_mc.current_partner == "Bill":
        bill "Mostly I've just been letting my mind wander."
        bill "It's actually kind of nice to have some time to think."
        bill "Everything's normally so hectic around here, you know."
    elif s3_mc.current_partner == "Camilo":
        camilo "Mostly I've just been letting my mind wander."
        camilo "It's actually kind of nice to have some time to think."
        camilo "Everything's normally so hectic around here, you know."
    elif s3_mc.current_partner == "Harry":
        harry "Mostly I've just been letting my mind wander."
        harry "It's actually kind of nice to have some time to think."
        harry "Everything's normally so hectic around here, you know."
    elif s3_mc.current_partner == "AJ":
        aj "Mostly I've just been letting my mind wander."
        aj "It's actually kind of nice to have some time to think."
        aj "Everything's normally so hectic around here, you know."

    s3_mc "What have you been thinking about?"
    "[he_she!c] rolls to face you, squishing [his_her] face into the pillow."

    if s3_mc.current_partner == "Bill":
        bill "I was just thinking about what the best colour of tent would be."
        s3_mc "Really? That's the kind of thing I expect you to have nailed down already."
        bill "I do now. But I had to think about it a bit to figure out what it was."
        s3_mc "And what did you decide, in the end?"
        bill "Green. 'Cause then if wild animals want to get in and eat your supplies, your tent will be harder to spot against the grass."
        s3_mc "What if you're not camping on grass, though?"
        bill "What else would you be camping on?"
        s3_mc "I don't know. Sand? Dirt? Grass in the summer that's gone yellow from not getting enough water?"
        "He pauses."
        bill "I might need to think about this a bit more."
        bill "Plus I've been thinking about you, and everything that happened yesterday."
    elif s3_mc.current_partner == "Camilo":
        camilo "I was thinking about this story my sisters sometimes tell."
        camilo "About this one time they went camping on a school trip together or something like that, and they had to share a tent."
        s3_mc "Is that the story?"
        camilo "No, no. The story is that one of them tried to sneak a boy into the tent for the night."
        camilo "I can't remember which sister. Probably Gabriela, to be honest."
        s3_mc "Did she get caught?"
        camilo "Of course she did. So she just tried again the next night."
        s3_mc "No way."
        camilo "She tried to smuggle this same boy into the tent every night for the whole trip. She didn't get away with it once."
        camilo "So yeah, I've just been thinking about how much they laugh when they tell that story. And I'm missing them a bit."
        camilo "Plus I've been thinking about you, and everything that happened yesterday."
    elif s3_mc.current_partner == "Harry":
        harry "I was trying to come up with apps aimed at people who go camping."
        harry "Like, maybe one called Pitchr, where you can hire someone to come and put up your tent for you."
        s3_mc "Sounds more like an app for people who want to hook up in tents, to be honest."
        harry "Yeah, I think you're right."
        harry "But maybe that's a good idea too?"
        harry "Plus I've been thinking about you, and everything that happened yesterday."
    elif s3_mc.current_partner == "AJ":
        aj "I was thinking about this time when I was a kid, and I was on the hockey team at my school."
        s3_mc "Your primary school had a hockey team?"
        aj "We weren't very good."
        aj "But we went away to this competition with some other kids' teams from around the country."
        aj "And for some reason I'd got it in my head that we would be camping? I honestly don't know why."
        s3_mc "You were disappointed about sleeping in a bed?"
        aj "I sleep in a bed every night! I wanted something different."
        aj "So yeah, me and all the other girls made a little network of tents out of our bedsheets and stuff."
        aj "We got in so much trouble. It was totally worth it."
        aj "I haven't thought about it in years, but being here reminded me."
        aj "Plus I've been thinking about you, and everything that happened yesterday."

    if s3_mc.current_partner == "Bill":
        if s3e4p2_decorate_tent or s3e4p2_good_tent:
            bill "We really smashed this tent challenge, didn't we?"
            bill "I don't know if it really is a good test of your compatibility or whatever, but... it makes you think."
            if s3e4p2_decorate_tent:
                bill "And how you went to all this effort to make the tent nice for us."
                bill "And how I never realised how much that would mean to me, until now."
                bill "Just, like, to have someone do something so nice, without being asked."
        else:
            bill "We really messed up this tent challenge, didn't we?"
            bill "I don't know if it really is a good test of your compatibility or whatever, but... it makes you think."
    elif s3_mc.current_partner == "Camilo":
        if s3e4p2_decorate_tent or s3e4p2_good_tent:
            camilo "We really smashed this tent challenge, didn't we?"
            camilo "I don't know if it really is a good test of your compatibility or whatever, but... it makes you think."
            if s3e4p2_decorate_tent:
                camilo "And how you went to all this effort to make the tent nice for us."
                camilo "And how I never realised how much that would mean to me, until now."
                camilo "Just, like, to have someone do something so nice, without being asked."
        else:
            camilo "We really messed up this tent challenge, didn't we?"
            camilo "I don't know if it really is a good test of your compatibility or whatever, but... it makes you think."
    elif s3_mc.current_partner == "Harry":
        if s3e4p2_decorate_tent or s3e4p2_good_tent:
            harry "We really smashed this tent challenge, didn't we?"
            harry "I don't know if it really is a good test of your compatibility or whatever, but... it makes you think."
            if s3e4p2_decorate_tent:
                harry "And how you went to all this effort to make the tent nice for us."
                harry "And how I never realised how much that would mean to me, until now."
                harry "Just, like, to have someone do something so nice, without being asked."
        else:
            harry "We really messed up this tent challenge, didn't we?"
            harry "I don't know if it really is a good test of your compatibility or whatever, but... it makes you think."
    elif s3_mc.current_partner == "AJ":
        if s3e4p2_decorate_tent or s3e4p2_good_tent:
            aj "We really smashed this tent challenge, didn't we?"
            aj "I don't know if it really is a good test of your compatibility or whatever, but... it makes you think."
            if s3e4p2_decorate_tent:
                aj "And how you went to all this effort to make the tent nice for us."
                aj "And how I never realised how much that would mean to me, until now."
                aj "Just, like, to have someone do something so nice, without being asked."
        else:
            aj "We really messed up this tent challenge, didn't we?"
            aj "I don't know if it really is a good test of your compatibility or whatever, but... it makes you think."
        
        "[he_she!c] pauses."

    if s3_mc.current_partner == "Bill":
        bill "Sorry. Was that a bit much? I was just thinking out loud."
    elif s3_mc.current_partner == "Camilo":
        camilo "Sorry. Was that a bit much? I was just thinking out loud."
    elif s3_mc.current_partner == "Harry":
        harry "Sorry. Was that a bit much? I was just thinking out loud."
    elif s3_mc.current_partner == "AJ":
        aj "Sorry. Was that a bit much? I was just thinking out loud."

    # CHOICE
    menu:
        thought "[s3_mc.current_partner] was thinking about me..."
        "I kinda zoned out, sorry":
            $ s3_mc.dislike(s3_mc.current_partner)
            s3_mc "Could you start over?"
            if s3_mc.current_partner == "Bill":
                bill "No, it's OK. Forget I said anything."
            elif s3_mc.current_partner == "Camilo":
                camilo "No, it's OK. Forget I said anything."
            elif s3_mc.current_partner == "Harry":
                harry "No, it's OK. Forget I said anything."
            elif s3_mc.current_partner == "AJ":
                aj "No, it's OK. Forget I said anything."
        "Save it for after breakfast":
            s3_mc "It's too early in the morning for that kind of talk, hun."
            if s3_mc.current_partner == "Bill":
                bill "Yeah, you're probably right."
            elif s3_mc.current_partner == "Camilo":
                camilo "Yeah, you're probably right."
            elif s3_mc.current_partner == "Harry":
                harry "Yeah, you're probably right."
            elif s3_mc.current_partner == "AJ":
                aj "Yeah, you're probably right."
        "It's OK, I think it's sweet":
            $ s3_mc.like(s3_mc.current_partner)
            s3_mc "Don't apologise for being honest about your feelings."
            if s3_mc.current_partner == "Bill":
                bill "Thanks, babe."
            elif s3_mc.current_partner == "Camilo":
                camilo "Thanks, babe."
            elif s3_mc.current_partner == "Harry":
                harry "Thanks, babe."
            elif s3_mc.current_partner == "AJ":
                aj "Thanks, babe."

    if s3_mc.current_partner == "Bill":
        bill "I just have to wonder..."
        bill "What's going to happen now?"
        s3_mc "What do you mean?"
        bill "I mean, it's Love Island. You don't just get together and that's it."
        bill "Relationships get tested. People get split up. New people come along and things change."
        bill "I mean..."
        bill "If you met someone else who was exactly your type on paper... what would you do?"
        bill "Do you think there's any chance your head could be turned?"
    elif s3_mc.current_partner == "Camilo":
        camilo "I just have to wonder..."
        camilo "What's going to happen now?"
        s3_mc "What do you mean?"
        camilo "I mean, it's Love Island. You don't just get together and that's it."
        camilo "Relationships get tested. People get split up. New people come along and things change."
        camilo "I mean..."
        camilo "If you met someone else who was exactly your type on paper... what would you do?"
        camilo "Do you think there's any chance your head could be turned?"
    elif s3_mc.current_partner == "Harry":
        harry "I just have to wonder..."
        harry "What's going to happen now?"
        s3_mc "What do you mean?"
        harry "I mean, it's Love Island. You don't just get together and that's it."
        harry "Relationships get tested. People get split up. New people come along and things change."
        harry "I mean..."
        harry "If you met someone else who was exactly your type on paper... what would you do?"
        harry "Do you think there's any chance your head could be turned?"
    elif s3_mc.current_partner == "AJ":
        aj "I just have to wonder..."
        aj "What's going to happen now?"
        s3_mc "What do you mean?"
        aj "I mean, it's Love Island. You don't just get together and that's it."
        aj "Relationships get tested. People get split up. New people come along and things change."
        aj "I mean..."
        aj "If you met someone else who was exactly your type on paper... what would you do?"
        aj "Do you think there's any chance your head could be turned?"

    # CHOICE
    menu:
        thought "Could my head be turned?"
        "No way, babe":
            $ s3_mc.like(s3_mc.current_partner)
            s3_mc "I'm really happy with you. I'm not about to run off."
        "It's always possible...":
            $ s3_mc.dislike(s3_mc.current_partner)
            s3_mc "I mean yeah, if someone comes along who's exactly my type on paper, of course I'm going to pay attention."
        "There's no point speculating":
            s3_mc "It's a hypothetical situation. You might as well ask me what I'd do if aliens landed on the roof terrace."
            if s3_mc.current_partner == "Bill":
                bill "What would you do if aliens landed on the roof terrace?"
                s3_mc "Couple up with one of them."
                bill "Really?"
            elif s3_mc.current_partner == "Camilo":
                camilo "What would you do if aliens landed on the roof terrace?"
                s3_mc "Couple up with one of them."
                camilo "Really?"
            elif s3_mc.current_partner == "Harry":
                harry "What would you do if aliens landed on the roof terrace?"
                s3_mc "Couple up with one of them."
                harry "Really?"
            elif s3_mc.current_partner == "AJ":
                aj "What would you do if aliens landed on the roof terrace?"
                s3_mc "Couple up with one of them."
                aj "Really?"
            s3_mc "I don't know! That's my point."

    s3_mc "Why? Have you been lying here worrying about me meeting someone else?"

    if s3_mc.current_partner == "Bill":
        bill "...At this point, I think it would make me proper sad if you met someone else."
        bill "Obviously I would never try and tell you what to do. But yeah, I would be jealous."
        bill "I think if yesterday showed me anything, it's that we make a really great team."
        bill "And even when things go wrong, we can still have fun together."
        bill "I don't wanna lose that."
        "[he_she!c] gives you a smile that turns into a stifled yawn."
        bill "Wow, sorry! I guess I'm still pretty sleepy after all."
        s3_mc "It's still early. You could probably get a nap in before breakfast."
        bill "That's not a bad idea."
        "[he_she!c] yawns again."
        bill "I think I'll just...close my eyes for a bit..."
    elif s3_mc.current_partner == "Camilo":
        camilo "...At this point, I think it would make me proper sad if you met someone else."
        camilo "Obviously I would never try and tell you what to do. But yeah, I would be jealous."
        camilo "I think if yesterday showed me anything, it's that we make a really great team."
        camilo "And even when things go wrong, we can still have fun together."
        camilo "I don't wanna lose that."
        "[he_she!c] gives you a smile that turns into a stifled yawn."
        camilo "Wow, sorry! I guess I'm still pretty sleepy after all."
        s3_mc "It's still early. You could probably get a nap in before breakfast."
        camilo "That's not a bad idea."
        "[he_she!c] yawns again."
        camilo "I think I'll just...close my eyes for a bit..."
    elif s3_mc.current_partner == "Harry":
        harry "...At this point, I think it would make me proper sad if you met someone else."
        harry "Obviously I would never try and tell you what to do. But yeah, I would be jealous."
        harry "I think if yesterday showed me anything, it's that we make a really great team."
        harry "And even when things go wrong, we can still have fun together."
        harry "I don't wanna lose that."
        "[he_she!c] gives you a smile that turns into a stifled yawn."
        harry "Wow, sorry! I guess I'm still pretty sleepy after all."
        s3_mc "It's still early. You could probably get a nap in before breakfast."
        harry "That's not a bad idea."
        "[he_she!c] yawns again."
        harry "I think I'll just...close my eyes for a bit..."
    elif s3_mc.current_partner == "AJ":
        aj "...At this point, I think it would make me proper sad if you met someone else."
        aj "Obviously I would never try and tell you what to do. But yeah, I would be jealous."
        aj "I think if yesterday showed me anything, it's that we make a really great team."
        aj "And even when things go wrong, we can still have fun together."
        aj "I don't wanna lose that."
        "[he_she!c] gives you a smile that turns into a stifled yawn."
        aj "Wow, sorry! I guess I'm still pretty sleepy after all."
        s3_mc "It's still early. You could probably get a nap in before breakfast."
        aj "That's not a bad idea."
        "[he_she!c] yawns again."
        aj "I think I'll just...close my eyes for a bit..."

    "[he_she!c] rolls over and falls straight to sleep."
    thought "I may as well go and see if any of the others are awake."

    scene s3-lawn-tents-day with dissolve
    $ new_scene()

    "You step out onto the lawn. It's cool and damp beneath your bare feet."
    "Nobody else is around. The sun is just rising over the Villa, shining down on all the Islanders' tents..."
    thought "Wait a minute."
    thought "Where did that tent come from?"
    "A new tent has appeared on the lawn overnight."
    "It's larger than the others, and made of more expensive-looking material."
    "You can hear muted voices coming from inside."
    thought "There's somebody in there!"
    thought "This explains the noise Viv was talking about last night..."

    # CHOICE
    menu: 
        thought "I should..."
        "Let them know I'm here":
            "You step up to the entrance of the mystery tent and cough loudly."
            "The voices inside go silent."
            s3_mc "Hello? Who's inside there?"
            s3_mc "Can I come in?"
            "For a moment, nothing happens."
            "Then a hand emerges from the tent and pulls you inside."
            s3_mc "Hey!"
        "Burst in announced":
            "You step up to the entrance of the mystery tent and push aside the fabric..."
        "Eavesdrop on their conversation":
            "You tip-toe closer to the mystery tent and listen closely, trying to make out the voices inside..."
            ciaran "Really? I thought he was a ride."
            show ciaran at npc_exit
            pause .3
            $ renpy.hide("ciaran")
            $ on_screen.remove("ciaran")

            tai "I wouldn't mind kissing his bucket head!"
            show tai at npc_exit
            pause .3
            $ renpy.hide("tai")
            $ on_screen.remove("tai")

            yasmin "I wouldn't kiss him if we were both wearing buckets on our heads."
            show yasmin at npc_exit
            pause .3
            $ renpy.hide("yasmin")
            $ on_screen.remove("yasmin")

            thought "Uh oh. I think I need to sneeze."
            "You do your best to stay quiet, but you can't hold it in..."
            s3_mc "Achoo!"
            "The voices inside go quiet."
            "For a moment, nothing happens."
            "Then a hand emerges from the tent and pulls you inside."
            s3_mc "Hey!"

    scene s3-inside-tent-mystery with dissolve
    $ new_scene()

    "Inside the tent is spacious and comfortable."
    "It's decorated with cushions, blankets and fairy lights, and it smells faintly of flowers."
    "Two boys and a girl are sprawled out on the floor. They all sit up straight when they see you."
    tai "Oh, look! It's [s3_name]!"
    tai "And she's looking fine as ever!"
    ciaran "Hey, well done! You're the first person to find us."
    yasmin "It must be fate."

    # CHOICE
    menu:
        thought "New Islanders! Three of them!"
        "Hey, this isn't a campsite":
            s3_mc "Do you have permits to camp here?"
            ciaran "Oh no! We left our permits at home!"
            s3_mc "Well then, I'm just going to have to take your details."
            tai "No problem, officer!"
        "Looks like it's my lucky day!":
            s3_mc "What are your names, babes?"
        "How come I've never noticed you three before?":
            "They laugh."
            tai "We were waiting for the right moment to show our faces. It's great to finally meet you!"

    tai "I'm Tai."

    window hide
    show screen s3_character_profile("tai") with Pause(3)
    hide screen s3_character_profile with dissolve

    "{i}Tai\n
    -28, from New Zealand\n
    -Rugby Coach\n
    -193cm of love{/i}"

    tai "It's so nice to finally meet you."
    "Tai holds out his arms, offering you a hug."

    # CHOICE
    menu:
        thought "Tai's going in for a hug..."
        "Not today, thank you":
            $ s3_mc.dislike("Tai")
            # NEED TO FILL
            "EMPTY"
        "Sure, I'll take a hug!":
            $ s3_mc.like("Tai")
            "Tai grins and hugs you. His arms are huge and strong, but gentle."
        "Can it come with a kiss?":
            $ s3_mc.like("Tai")
            "Tai grins and hugs you. His arms are huge and strong, but gentle."
            "He obliges you with a big kiss to the top of your head."
            tai "How was that?"
            s3_mc "It'll do for now."

    "The other boy offers you a cushion to sit on."
    ciaran "Make yourself at home!"
    ciaran "How'd you like our ten? It's so lush, I almost don't want to move into the Villa."
    ciaran "I'm Ciaran, by the way. No fada on the A."

    window hide
    show screen s3_character_profile("ciaran") with Pause(3)
    hide screen s3_character_profile with dissolve

    "{i}Ciaran\n
    -22, from Waterford, Ireland\n
    -Nightclub bouncer\n
    -No shirt, no shoes, no problem{/i}"

    # CHOICE
    menu:
        s3_mc "Hi, Ciaran..."
        "It's really nice to meet you":
            $ s3_mc.like("Ciaran")
            s3_mc "I'm sure everyone here's going to love you."
            ciaran "Thanks, [s3_name]. That really means a lot."
        "What's a fada?":
            ciaran "It's like a little mark thingy that goes on some letters in Irish."
            ciaran "'Ciaran' would usually have one on the second A."
            s3_mc "Why doesn't your name have that, then?"
            ciaran "My grandad didn't have on either, 'cause his mam forgot to write it on the form when he was born."
            ciaran "So it's kind of a family tradition now, I guess."
        "Ooh, I love your accent...":
            $ s3_mc.like("Ciaran")
            ciaran "Really?"
            s3_mc "It's gorgeous. People must say that to you all the time."
            ciaran "They really don't."
            ciaran "I've never really lived outside Ireland. Most people there speak like me."
            s3_mc "Then I'd love to go there."
            "He smiles, his face turning bright red under his freckles."

    "The third new Islander has been watching quietly while you talk to the boys."
    "When you turn to face her, she smiles. All her movements are slow and graceful."
    yasmin "[s3_name]. I've been looking forward to meeting you."
    yasmin "I'm Yasmin."

    window hide
    show screen s3_character_profile("yasmin") with Pause(3)
    hide screen s3_character_profile with dissolve

    "{i}Yasmin\n
    -23, from Kent\n
    -Singer-songwriter\n
    -Artist in need of a muse{/i}"

    "Yasmin gestures to the middle of the tent, where there's a pitcher of fruit juice and some glasses with ice."
    yasmin "Can I get you some juice? We've got loads."

    # CHOICE
    menu:
        thought "Yasmin's offering to pour me some juice..."
        "No thanks, I'm good":
            # NEED TO FILL
            "EMPTY"
        "That'd be great, thank you":
            $ s3_mc.like("Yasmin")
            "Yasmin picks up the pitcher, pours out a glass, and hands it to you."
            "The ice clinks against the glass as you take a sip. It's cold and sweet."
            s3_mc "Thanks, Yasmin."
            yasmin "No problem."
        "I hope that's flirting..." if s3_mc.bisexual:
            $ s3_mc.like("Yasmin")
            $ s3_mc.like("Yasmin")
            "Yasmin just gives you a sidelong smile as she picks up the pitcher and pours you a glass."
            "When she hands it over, her fingers brush against yours and linger for a second before pulling away."
            "The ice clinks against the glass as you take a sip. It's cold and sweet."
            s3_mc "Thanks, Yasmin."
            yasmin "No problem."
        "The boys should be pouring drinks for us":
            "You turn to Tai and Ciaran."
            s3_mc "Why didn't either of you two offer me juice?"
            tai "Oh! Right!"
            ciaran "Sorry!"
            "Both at once, the boys rush to try and pick up the pitcher."
            "They just about manage to avoid spilling any, and pour one glass each for you and Yasmin."
            "Yasmin shares a look of silent amusement with you as you both sip your drinks."

    "Tai flops down on a pile of cushions."
    tai "So, [s3_name]! I would ask you to tell us about yourself."
    tai "But we already know all about you, 'cause we've been watching everything you do on TV."
    s3_mc "Well, why don't you tell me about yourselves, instead?"
    ciaran "Oh yeah, I think [s3_name] should get to ask us some questions."
    tai "Great idea!"
    tai "Don't be offended if you can't get a straight answer out of Yasmin. That's just the way she is."
    yasmin "I like to cultivate an air of mystery when I can."
    tai "But this one here and me, we're a couple of open books, aren't we?"
    "Tai ruffles Ciaran's hair playfully, making him laugh and bat Tai's hand away."
    ciaran "We'll try to give good answers, anyway."
    s3_mc "I'll try to ask good questions."

    # CHOICE
    menu:
        thought "Who do I want to ask about first?"
        "Tai":
            $ s3_mc.like("Tai")
            s3_mc "I've got a pretty basic question for Tai."
            s3_mc "What made you want to be on Love Island?"
            tai "That's a great question!"
            tai "I'm just done with the whole 'lads on tour' thing. That's the real reason."
            tai "I don't want to be running around seeing someone different every weekend."
            tai "It used to be fun, but it's not who I am anymore."
            tai "I'm ready to find someone I can settle down with. You know, long-term."
        "Ciaran":
            $ s3_mc.like("Ciaran")
            s3_mc "I've got a pretty basic question for Ciaran."
            s3_mc "What made you want to be on Love Island?"
            ciaran "Oh, good question."
            ciaran "I wanted to... what's a good way of saying... expand my options?"
            ciaran "Waterford's grand, but it's not a big place."
            ciaran "Sometimes it feels like I know everybody there already. Especially working at the club, you know?"
            ciaran "And I know there's this whole big world of different people out here, people who think differently and feel differently."
            ciaran "I wanna meet someone who makes me feel different. If that makes sense."
        "Yasmin":
            $ s3_mc.like("Yasmin")
            s3_mc "I've got a pretty basic question for Yasmin."
            s3_mc "What made you want to be on Love Island?"
            yasmin "I think that's a perfect first question."
            yasmin "How can we ever move on to the greater mysteries of life if we don't nail down the basics first?"
            yasmin "I want to meet someone who changes my life. Even in a small way, you know."
            yasmin "Every person we meet has a chance of opening us up to some new idea of experience, some new part of ourselves."
            yasmin "It might sound pretentious, but it's my favourite thing in the world."
            yasmin "That excitement of meeting someone and just knowing you'll never be the same again."
            yasmin "And I want to do it on Love Island."
            yasmin "This way, even if I don't find someone, I'm still out here expanding my horizons."

    s3_mc "I get you."

    ciaran "Ask us another one!"

    # CHOICE
    menu:
        s3_mc "Next I've got a question for..."
        "Tai":
            $ s3_mc.like("Tai")
            s3_mc "OK, next question for Tai."
            s3_mc "What's your type on paper?"
            tai "Ooh, tricky."
            tai "I tend to go for sporty types, but that's not a hard rule."
            tai "Maybe it's just because those are the kinds of people I usually hang out with, 'cause I'm sporty myself? I'm not sure."
            tai "And I know everyone says this, but a sense of humour is so important!"
            tai "Anyone with good banter and a big laugh is my type on paper. That's the quickest way to my heart."
        "Ciaran":
            $ s3_mc.like("Ciaran")
            s3_mc "OK, next question for Ciaran."
            s3_mc "What's your type on paper?"
            ciaran "Hmm... well, I don't really have a physical type."
            ciaran "But in terms of personality, I love girls who are really affectionate and soft. 'Cause I'm kind of a big softie myself."
            ciaran "So I need someone who likes walks on the beach, and texting each other all the heart emojis, and generally being a couple of total melts."
            ciaran "Plus, if you're good with dogs, that never hurts."
        "Yasmin":
            $ s3_mc.like("Yasmin")
            s3_mc "OK, next question for Yasmin."
            s3_mc "What's your type on paper?"
            "She grins."
            yasmin "Now, this is one where I definitely can't give you a straight answer."
            yasmin "It's all in the face for me. I like a cute nose, big smile, bright eyes."
            yasmin "And when I do date men, I usually go for ones with beards."
            yasmin "But mostly I just love anyone who isn't afraid to be a little bit weird, you know? Or even a lot weird."
            yasmin "Good taste in music is always a plus, too. Especially if it's different from mine."
            yasmin "I think the best relationships are with people who can show you new things. If they can change my mind about something, even better."

    s3_mc "Good answer!"

    s3_mc "Can I ask one more question?"
    tai "Oh, go on, then."
    tai "And make it a really difficult one this time."

    # CHOICE
    menu:
        s3_mc "My last question is for..."
        "Tai":
            $ s3_mc.like("Tai")
            s3_mc "Tell me the truth, Tai. What do you think of us Islanders, based on what you've seen on TV?"
            tai "Oh, now we're getting to the spicy stuff!"
            tai "I've honestly been so excited to come and meet you all."
            tai "I don't know when I've ever seen such a beautiful bunch of people."
            s3_mc "So you don't have your eye on someone in particular?"
            tai "Well..."
            tai "Right of the bat, you and AJ are probably the two girls who caught my eye the most."
            tai "But hey, now I'm actually here, anything could happen. I guess we'll see where sparks start flying."
            yasmin "It looks a bit like they're flying already."
        "Ciaran":
            $ s3_mc.like("Ciaran")
            s3_mc "Tell me the truth, Ciaran. What do you think of us Islanders, based on what you've seen on TV?"
            ciaran "Aw, that's a harsh one!"
            ciaran "Overall, I think you all seem really nice. I can't wait to make friends with everyone here."
            s3_mc "But anyone in particular?"
            ciaran "Well..."
            ciaran "Elladine is a lovely person."
            ciaran "But I don't think there's any chance of turning her head now."
            ciaran "Otherwise you're definitely the girl I fancy the most in here."
            "Tai laughs and nudges him."
            tai "No kidding, mate. She could see that crush from space."
            ciaran "Was it that obvious?"
            yasmin "Only a lot, Ciaran. Don't worry."
        "Yasmin":
            $ s3_mc.like("Yasmin")
            s3_mc "Tell me the truth, Yasmin. What do you think of us Islanders, based on what you've seen on TV?"
            yasmin "Well, it seems like there's a lot of positive energy in the Villa right now. I can't wait to meet everyone properly."
            s3_mc "Do you have your eye on anyone in particular?"
            yasmin "Hmm."
            yasmin "In terms of boys, I'm intrigued by Seb. I think there's more to him than meets the eye."
            yasmin "I don't see anything happening with any of the girls at the moment, but I'm keeping my mind open."
            "She gives you a smile."
            tai "What'd I tell you?"
            tai "Never get a straight answer out of her!"
            yasmin "I'm just saying what I feel!"

    yasmin "But it's so hard to know how things will be just based on watching the show."
    yasmin "You can get one impression of somebody from a distance..."
    yasmin "Then when you actually get in a room with them, your energies react in a way you never saw coming."
    ciaran "Energies?"
    yasmin "You know, the way you vibe with someone, one to one."
    yasmin "It's so important, but it's difficult to predict."
    tai "I totally get it."
    tai "Like, we've only just met [s3_name] for real. We're still getting to know each other."
    tai "And yet we've already got all these ideas about, just based on everything we've seen her do on telly."
    s3_mc "Like what?"
    tai "Where to start?"

    if s3e1p1_grab_some_condoms:
        ciaran "There was that thing with the condoms on day one. "
        tai "Oh my word, that was the funniest thing I've ever seen. I was definitely cheering for you after that."

    yasmin "The way you dealt with it when [s3_3rd_girl] stole [s3_mc.past_partners[0]] from you..."

    if s3_mc.past_partners[0] == s3_mc.current_partner:
        tai "And then you won him back at the next recoupling!"
    else:
        tai "And then you switched it up and went for [s3_mc.current_partner] at the next recoupling!"

    ciaran "Classic."
    yasmin "Speaking of [s3_mc.current_partner] and recouplings..."
    yasmin "Do you think you'll stick with [him_her] again at the next one? Or maybe switch it up?"

    # CHOICE
    menu:
        thought "At the next recoupling..."
        "I'm sticking with [s3_mc.current_partner] for sure":
            yasmin "Good for you. I think you two make a good couple."
            yasmin "Just be careful not to get too set in your ways too quickly."
            yasmin "Sometimes the universe throws unexpected things at us, and the only thing we can do is just be open to it."
        "I'm planning to couple up with someone else":
            ciaran "Interesting."
            tai "Very interesting."
            yasmin "So you're not getting too comfortable just yet. That's cool."
            yasmin "Sometimes the universe throws unexpected things at us, and the only thing we can do is just be open to it."
        "I'm just keeping my options open for now":
            ciaran "Interesting."
            tai "Very interesting."
            yasmin "So you're not getting too comfortable just yet. That's cool."
            yasmin "Sometimes the universe throws unexpected things at us, and the only thing we can do is just be open to it."

    "Outside on the lawn, you can hear the other Islanders starting to wake up."
    "Someone cries out in surprise."
    ciaran "I think they've spotted our tent."
    tai "Great! Let's go out there and introduce ourselves!"
    ciaran "Yeah, and maybe get some proper breakfast. I'm starving."
    "The three of them get up to go."
    "Before they leave the tent, they pause to look back at you."
    tai "Thanks for the chat, [s3_name]. It's been great fun."
    ciaran "Yeah, I'm glad we got a chance to talk to you alone."
    ciaran "And hey, if you want to get to know us even better while we're gone..."
    ciaran "Feel free to take a peek at my luggage."
    ciaran "Wait, that sounded wrong. I mean literally..."
    "He gestures to the three suitcases in the corner of the tent."
    ciaran "That's our luggage, there. I don't mind you having a look inside if you're curious."
    tai "Yeah, mine too! I've got nothing to hide."
    yasmin "Me neither. Go for it, [s3_name]. Just remember..."
    yasmin "Curiosity killed the cat."
    "The three of them wave you a cheerful goodbye before heading out onto the lawn."

    $ leaving("ciaran")
    $ leaving("yasmin")

    "The flap falls shut, leaving you alone in the tent."
    "You can hear the other Islanders shouting and laughing as they welcome the new arrivals. Tai's voice carries over everything."
    "Before long, the tent flap is pushed aside again and [s3_mc.bff]'s face appears in the opening."

    $ pronouns(s3_mc.bff)

    if s3_mc.bff == "Elladine":
        elladine "Wow! Check this out!"
    elif s3_mc.bff == "Genevieve":
        genevieve "Wow! Check this out!"
        genevieve "This must be what was making all that noise last night."
    elif s3_mc.bff == "Nicky":
        nicky "Wow! Check this out!"
    elif s3_mc.bff == "Seb":
        seb "Wow! Check this out!"

    # CHOICE
    menu:
        s3_mc "Hey, [s3_mc.bff]..."
        "Look how fancy the new Islanders' tent is":
            s3_mc "Can you believe they got all this just for showing up five days after the rest of us?"
            if s3_mc.bff == "Elladine":
                elladine "Lucky gits. I bet they didn't even have to put it up themselves."
            elif s3_mc.bff == "Genevieve":
                genevieve "Lucky gits. I bet they didn't even have to put it up themselves."
            elif s3_mc.bff == "Nicky":
                nicky "Lucky gits. I bet they didn't even have to put it up themselves."
            elif s3_mc.bff == "Seb":
                seb "Lucky gits. I bet they didn't even have to put it up themselves."
        "Care to join me in my fancy tent?":
            s3_mc "As you can see, I've got plenty of room."
            if s3_mc.bff == "Elladine":
                elladine "That's very generous of you, your majesty."
            elif s3_mc.bff == "Genevieve":
                genevieve "That's very generous of you, your majesty."
            elif s3_mc.bff == "Nicky":
                nicky "That's very generous of you, your majesty."
            elif s3_mc.bff == "Seb":
                seb "That's very generous of you, your majesty."
        "Get out of the fancy tent! It's mine!":
            if s3_mc.bff == "Elladine":
                elladine "I don't see your name on it!"
                s3_mc "I don't need to put my name on it! I'm in it!"
                elladine "Well, I'm about to be in it too! Does that make it my tent now?"
            elif s3_mc.bff == "Genevieve":
                genevieve "I don't see your name on it!"
                s3_mc "I don't need to put my name on it! I'm in it!"
                genevieve "Well, I'm about to be in it too! Does that make it my tent now?"
            elif s3_mc.bff == "Nicky":
                nicky "I don't see your name on it!"
                s3_mc "I don't need to put my name on it! I'm in it!"
                nicky "Well, I'm about to be in it too! Does that make it my tent now?"
            elif s3_mc.bff == "Seb":
                seb "I don't see your name on it!"
                s3_mc "I don't need to put my name on it! I'm in it!"
                seb "Well, I'm about to be in it too! Does that make it my tent now?"
                s3_mc "Nooo! I was here first!"

    "Grinning, [he_she] comes inside and flops down beside you on a pile of blankets."

    if s3_mc.bff == "Elladine":
        elladine "Love the jammies, by the way. Like, they look great on you."
        elladine "This is so weird. I can't believe we got three new Islanders in one go."
        elladine "And you got to talk to them alone before any of us! What d'you make of them?"
        elladine "Tai's a hunk. Just imagine how safe you'd feel in those arms."
    elif s3_mc.bff == "Genevieve":
        genevieve "Love the jammies, by the way. Like, they look great on you."
        genevieve "This is so weird. I can't believe we got three new Islanders in one go."
        genevieve "And you got to talk to them alone before any of us! What d'you make of them?"
        genevieve "Tai's a hunk. Just imagine how safe you'd feel in those arms."
    elif s3_mc.bff == "Nicky":
        nicky "Love the jammies, by the way. Like, they look great on you."
        nicky "This is so weird. I can't believe we got three new Islanders in one go."
        nicky "And you got to talk to them alone before any of us! What d'you make of them?"
        nicky "Tai seems like a cool guy. And I think the other lads are all a bit intimidated by him, which is hilarious."
    elif s3_mc.bff == "Seb":
        seb "Love the jammies, by the way. Like, they look great on you."
        seb "This is so weird. I can't believe we got three new Islanders in one go."
        seb "And you got to talk to them alone before any of us! What d'you make of them?"
        seb "Tai seems like a cool guy, but I can't help feeling a bit... intimidated by him."
    
    # CHOICE
    menu:
        s3_mc "Tai..."
        "He's great fun":
            $ s3_mc.like("Tai")
            s3_mc "He's such a laugh. I think he's gonna be really popular in here."
            if s3_mc.bff == "Elladine":
                elladine "Oh, definitely. Great banter, all of that."
            elif s3_mc.bff == "Genevieve":
                genevieve "Oh, definitely. Great banter, all of that."
            elif s3_mc.bff == "Nicky":
                nicky "Oh, definitely. Great banter, all of that."
            elif s3_mc.bff == "Seb":
                seb "Oh, definitely. Great banter, all of that."
        "He's a bit of me":
            $ s3_mc.like("Tai")
            $ s3_mc.like("Tai")
            s3_mc "I wouldn't mind getting to know him a bit better. Or a lot better."
            if s3_mc.bff == "Elladine":
                elladine "[s3_name]!"
                elladine "You two would make such a power couple."
            elif s3_mc.bff == "Genevieve":
                genevieve "[s3_name]!"
                genevieve "You two would make such a power couple."
            elif s3_mc.bff == "Nicky":
                nicky "[s3_name]!"
                nicky "You two would make such a power couple."
            elif s3_mc.bff == "Seb":
                seb "[s3_name]!"
                seb "You two would make such a power couple."
        "We didn't click":
            $ s3_mc.dislike("Tai")
            s3_mc "He's a bit much for me."
            if s3_mc.bff == "Elladine":
                elladine "Well, then..."
            elif s3_mc.bff == "Genevieve":
                genevieve "Well, then..."
            elif s3_mc.bff == "Nicky":
                nicky "Well, then..."
            elif s3_mc.bff == "Seb":
                seb "Well, then..."

    if s3_mc.bff == "Elladine":
        elladine "What about Ciaran?"
        elladine "I think he's super cute."
        s3_mc "Puppy cute or sexy cute?"
        elladine "A bit of both!"
    elif s3_mc.bff == "Genevieve":
        genevieve "What about Ciaran?"
        genevieve "I think he's super cute."
        s3_mc "Puppy cute or sexy cute?"
        genevieve "A bit of both!"
    elif s3_mc.bff == "Nicky":
        nicky "What about Ciaran?"
        nicky "He seems like a proper sweet lad. Y'know, take-home-to-mum-material."
    elif s3_mc.bff == "Seb":
        seb "What about Ciaran?"
        seb "He seems like a proper sweet lad. Y'know, take-home-to-mum-material."

    # CHOICE
    menu:
        s3_mc "Ciaran..."
        "He is pretty fit...":
            $ s3_mc.like("Ciaran")
            $ s3_mc.like("Ciaran")
            s3_mc "Obviously."
            if s3_mc.bff == "Elladine":
                elladine "I can definitely see you two together."
            elif s3_mc.bff == "Genevieve":
                genevieve "I can definitely see you two together."
            elif s3_mc.bff == "Nicky":
                nicky "I can definitely see you two together."
            elif s3_mc.bff == "Seb":
                seb "I can definitely see you two together."
        "He's nice, but that's all":
            $ s3_mc.like("Ciaran")
            s3_mc "I think me and him could be good mates, but that's it."
            if s3_mc.bff == "Elladine":
                elladine "Fair enough."
            elif s3_mc.bff == "Genevieve":
                genevieve "Fair enough."
            elif s3_mc.bff == "Nicky":
                nicky "Fair enough."
            elif s3_mc.bff == "Seb":
                seb "Fair enough."
        "I'm not a fan":
            $ s3_mc.dislike("Ciaran")
            s3_mc "I don't see it. He's not my kind of guy at all."
            if s3_mc.bff == "Elladine":
                elladine "Fair enough."
            elif s3_mc.bff == "Genevieve":
                genevieve "Fair enough."
            elif s3_mc.bff == "Nicky":
                nicky "Fair enough."
            elif s3_mc.bff == "Seb":
                seb "Fair enough."

    if s3_mc.bff == "Elladine":
        elladine "Then there's Yasmin. I couldn't get a good read on her."
        elladine "She seemed a bit less outgoing than the other two."
        elladine "How do you feel about having a new girl in the Villa?"
    elif s3_mc.bff == "Genevieve":
        genevieve "Then there's Yasmin. I couldn't get a good read on her."
        genevieve "She seemed a bit less outgoing than the other two."
        genevieve "How do you feel about having a new girl in the Villa?"
    elif s3_mc.bff == "Nicky":
        nicky "Then there's Yasmin. I couldn't get a good read on her."
        nicky "She seemed a bit less outgoing than the other two."
        nicky "How do you feel about having a new girl in the Villa?"
    elif s3_mc.bff == "Seb":
        seb "Then there's Yasmin. I couldn't get a good read on her."
        seb "She seemed a bit less outgoing than the other two."
        seb "You know she's a musician?"
        seb "The number of times I've promised myself I'll never date another musician..."
        seb "But I might make an exception for her."
        seb "How do you feel about having a new girl in the Villa?"

    # CHOICE
    menu:
        s3_mc "Yasmin..."
        "I think we're gonna be friends":
            $ s3_mc.like("Yasmin")
            s3_mc "From meeting her just now, I think we'll get on really well."
            if s3_mc.bff == "Elladine":
                elladine "That's so great."
            elif s3_mc.bff == "Genevieve":
                genevieve "That's so great."
            elif s3_mc.bff == "Nicky":
                nicky "That's so great."
            elif s3_mc.bff == "Seb":
                seb "That's so great."
        "I don't really know her yet":
            s3_mc "It's a bit early to say. I guess we'll see if she can be cool or not."
            if s3_mc.bff == "Elladine":
                elladine "Hopefully, it'll all be chill..."
            elif s3_mc.bff == "Genevieve":
                genevieve "Hopefully, it'll all be chill..."
            elif s3_mc.bff == "Nicky":
                nicky "Hopefully, it'll all be chill..."
            elif s3_mc.bff == "Seb":
                seb "Hopefully, it'll all be chill..."
        "She'd better just stay away from [s3_mc.current_partner]":
            $ s3_mc.dislike("Yasmin")
            s3_mc "The last thing I need is a new girl coming in and breaking up my relationship. Again."
            if s3_mc.bff == "Elladine":
                elladine "Hopefully, it'll all be chill..."
            elif s3_mc.bff == "Genevieve":
                genevieve "Hopefully, it'll all be chill..."
            elif s3_mc.bff == "Nicky":
                nicky "Hopefully, it'll all be chill..."
            elif s3_mc.bff == "Seb":
                seb "Hopefully, it'll all be chill..."
        "She's totally my type" if s3_mc.bisexual:
            $ s3_mc.like("Yasmin")
            $ s3_mc.like("Yasmin")
            s3_mc "If I'm reading her right, I could be in with a shot there."
            s3_mc "It's exciting to have another girl in the Villa I could potentially crack on with."
            if s3_mc.bff == "Elladine":
                elladine "Oh, that's exciting!"
                elladine "Thanks for letting me pick your brain of the newbies."
            elif s3_mc.bff == "Genevieve":
                genevieve "Oh, that's exciting!"
                genevieve "Thanks for letting me pick your brain of the newbies."
            elif s3_mc.bff == "Nicky":
                nicky "Oh, that's exciting!"
                nicky "Thanks for letting me pick your brain of the newbies."
            elif s3_mc.bff == "Seb":
                seb "Oh, that's exciting!"
                seb "Thanks for letting me pick your brain of the newbies."

    if s3_mc.bff == "Elladine":
        elladine "You're a great judge of people. I know, 'cause you're friends with me."
        "[he_she!c] spots the suitcases in the corner."
        elladine "Is that their luggage?"
        s3_mc "Yeah. They told me it'd be OK to have a little snoop through it."
        elladine "Cool!"
        elladine "What a great chance to get to know them a bit better."
        elladine "Plus, we might find out some fun secrets about them ahead of the others."
    elif s3_mc.bff == "Genevieve":
        genevieve "You're a great judge of people. I know, 'cause you're friends with me."
        "[he_she!c] spots the suitcases in the corner."
        genevieve "Is that their luggage?"
        s3_mc "Yeah. They told me it'd be OK to have a little snoop through it."
        genevieve "Cool!"
        genevieve "What a great chance to get to know them a bit better."
        genevieve "Plus, we might find out some fun secrets about them ahead of the others."
    elif s3_mc.bff == "Nicky":
        nicky "You're a great judge of people. I know, 'cause you're friends with me."
        "[he_she!c] spots the suitcases in the corner."
        nicky "Is that their luggage?"
        s3_mc "Yeah. They told me it'd be OK to have a little snoop through it."
        nicky "Cool!"
        nicky "What a great chance to get to know them a bit better."
        nicky "Plus, we might find out some fun secrets about them ahead of the others."
    elif s3_mc.bff == "Seb":
        seb "You're a great judge of people. I know, 'cause you're friends with me."
        "[he_she!c] spots the suitcases in the corner."
        seb "Is that their luggage?"
        s3_mc "Yeah. They told me it'd be OK to have a little snoop through it."
        seb "Cool!"
        seb "What a great chance to get to know them a bit better."
        seb "Plus, we might find out some fun secrets about them ahead of the others."

    # CHOICE
    menu:
        thought "This is a really good opportunity to learn more about the new Islanders..."
        "Let's have a rummage!":
            $ s3e5p1_rummage_suitcases = True
            call s3e5p1_rummage_suitcases from _call_s3e5p1_rummage_suitcases
        "Nope, not interested ":
            if s3_mc.bff == "Elladine":
                elladine "Aw. OK."
            elif s3_mc.bff == "Genevieve":
                genevieve "Aw. OK."
            elif s3_mc.bff == "Nicky":
                nicky "Aw. OK."
            elif s3_mc.bff == "Seb":
                seb "Aw. OK."

    s3_mc "Hey, I've got a text!"
    text "[s3_name], you have been invited on a date. Please go and get ready. #datingaround #newkidontheblock"
    s3_mc "What?!"

    if s3_mc.bff == "Elladine":
        elladine "It must be one of the new Islanders! It makes sense that they get dates on their first day."
        if s3e5p1_rummage_suitcases:
            elladine "Hey, it's a good thing we had a look at their bags. That should give you something to talk about."
            s3_mc "Yeah, I'll know what to ask if there's any awkward silences."
        else:
            elladine "Bet you wish we'd had a look at their bags now. Maybe it would've given you some good stuff to talk about."
            s3_mc "I'll be fine."
            s3_mc "But it doesn't even say which one chose me!"
        elladine "It might not even be just one. You could be in for another long day of dates."
    elif s3_mc.bff == "Genevieve":
        genevieve "It must be one of the new Islanders! It makes sense that they get dates on their first day."
        if s3e5p1_rummage_suitcases:
            genevieve "Hey, it's a good thing we had a look at their bags. That should give you something to talk about."
            s3_mc "Yeah, I'll know what to ask if there's any awkward silences."
        else:
            genevieve "Bet you wish we'd had a look at their bags now. Maybe it would've given you some good stuff to talk about."
            s3_mc "I'll be fine."
            s3_mc "But it doesn't even say which one chose me!"
        genevieve "It might not even be just one. You could be in for another long day of dates."
    elif s3_mc.bff == "Nicky":
        nicky "It must be one of the new Islanders! It makes sense that they get dates on their first day."
        if s3e5p1_rummage_suitcases:
            nicky "Hey, it's a good thing we had a look at their bags. That should give you something to talk about."
            s3_mc "Yeah, I'll know what to ask if there's any awkward silences."
        else:
            nicky "Bet you wish we'd had a look at their bags now. Maybe it would've given you some good stuff to talk about."
            s3_mc "I'll be fine."
            s3_mc "But it doesn't even say which one chose me!"
        nicky "It might not even be just one. You could be in for another long day of dates."
    elif s3_mc.bff == "Seb":
        seb "It must be one of the new Islanders! It makes sense that they get dates on their first day."
        if s3e5p1_rummage_suitcases:
            seb "Hey, it's a good thing we had a look at their bags. That should give you something to talk about."
            s3_mc "Yeah, I'll know what to ask if there's any awkward silences."
        else:
            seb "Bet you wish we'd had a look at their bags now. Maybe it would've given you some good stuff to talk about."
            s3_mc "I'll be fine."
            s3_mc "But it doesn't even say which one chose me!"
        seb "It might not even be just one. You could be in for another long day of dates."

    s3_mc "Oh man..."
    s3_mc "What's [s3_mc.current_partner] going to say?"

    "Even more importantly, [s3_name]..."
    "What are you going to wear?"
    "Do you see now what I was going on about at the start? Goldilocks and the three bears of varying sizes?"
    "Forget it. This is the last time I try to do something creative with the intro."

    scene sand with dissolve
    $ on_screen = []

    "Coming up on [s3_name]'s mystery date... things and stuff."
    "Oh, alright. Here's a sneak preview."
    tai "Like I'm some kind of swimming ability mind reader."
    ciaran "I really wanted to name her Dingle but mam was having none of it."
    "Don't miss it!"

    jump s3e5p2
    
    return

label s3e5p1_rummage_suitcases:

    s3_mc "Go on, then."
    if s3_mc.bff == "Elladine":
        elladine "Yes!"
    elif s3_mc.bff == "Genevieve":
        genevieve "Yes!"
    elif s3_mc.bff == "Nicky":
        nicky "Yes!"
    elif s3_mc.bff == "Seb":
        seb "Yes!"

    "[s3_mc.bff] picks up the first suitcase and unzips it."
    "Inside are bikinis and dresses, all very neatly folded."

    if s3_mc.bff == "Elladine":
        elladine "This bag must be Yasmin's."
    elif s3_mc.bff == "Genevieve":
        genevieve "This bag must be Yasmin's."
    elif s3_mc.bff == "Nicky":
        nicky "This bag must be Yasmin's."
    elif s3_mc.bff == "Seb":
        seb "This bag must be Yasmin's."
    
    s3_mc "Well, you never know."
    "[he_she!c] holds up a little purple swimsuit."
    
    if s3_mc.bff == "Elladine":
        elladine "I'm not denying Ciaran and Tai could both pull this off, but I don't think it'd fit either of them."
        "[s3_mc.bff] moves aside the top layer of clothes."
        elladine "Oh, interesting."
        s3_mc "What?"
        elladine "There's a badge here. Like one of those button badges with a pin in the back."
        elladine "It looks homemade. That's sweet."
    elif s3_mc.bff == "Genevieve":
        genevieve "I'm not denying Ciaran and Tai could both pull this off, but I don't think it'd fit either of them."
        "[s3_mc.bff] moves aside the top layer of clothes."
        genevieve "Oh, interesting."
        s3_mc "What?"
        genevieve "There's a badge here. Like one of those button badges with a pin in the back."
        genevieve "It looks homemade. That's sweet."
    elif s3_mc.bff == "Nicky":
        nicky "I'm not denying Ciaran and Tai could both pull this off, but I don't think it'd fit either of them."
        "[s3_mc.bff] moves aside the top layer of clothes."
        nicky "Oh, interesting."
        s3_mc "What?"
        nicky "There's a badge here. Like one of those button badges with a pin in the back."
        nicky "It looks homemade. That's sweet."
    elif s3_mc.bff == "Seb":
        seb "I'm not denying Ciaran and Tai could both pull this off, but I don't think it'd fit either of them."
        "[s3_mc.bff] moves aside the top layer of clothes."
        seb "Oh, interesting."
        s3_mc "What?"
        seb "There's a badge here. Like one of those button badges with a pin in the back."
        seb "It looks homemade. That's sweet."
    
    s3_mc "Can I see?"
    "[s3_mc.bff] hands the badge over. You look closely at the logo on the front."
    s3_mc "'Enchanted Husband'? What's that?"

    if s3_mc.bff == "Elladine":
        elladine "I don't know. It sounds like the name of a band."
    elif s3_mc.bff == "Genevieve":
        genevieve "I think it's a band? I'm pretty sure I saw them on the bill for a festival I worked once."
        genevieve "I didn't catch the show, though, so I don't know if they're any good."
    elif s3_mc.bff == "Nicky":
        nicky "It's a band. They're pretty underground, though."
        nicky "They're one of those bands I only know about so I can seem cool when nobody else has heard of them."
    elif s3_mc.bff == "Seb":
        seb "I think it's a band? I'm pretty sure a kid came into the shop once to ask if we carried their stuff."
        seb "We didn't, for the record. I've never heard them, so I dunno if they're any good."

    # CHOICE
    menu:
        thought "Enchanted Husband..."
        "What bad name for a band":
            pass
        "Sounds like a band I'd listen to":
            pass
        "Why not Enchanted Wife?":
            s3_mc "Wives can be enchanted, too."
            if s3_mc.bff == "Elladine":
                elladine "Tell the band, not me."
            elif s3_mc.bff == "Genevieve":
                genevieve "Tell the band, not me."
            elif s3_mc.bff == "Nicky":
                nicky "Tell the band, not me."
            elif s3_mc.bff == "Seb":
                seb "Tell the band, not me."

    s3_mc "I wonder if Yasmin's a fan?"
    if s3_mc.bff == "Elladine":
        elladine "Either that, or she's come here to enchant herself a husband."
    elif s3_mc.bff == "Genevieve":
        genevieve "Either that, or she's come here to enchant herself a husband."
    elif s3_mc.bff == "Nicky":
        nicky "Either that, or she's come here to enchant herself a husband."
    elif s3_mc.bff == "Seb":
        seb "Either that, or she's come here to enchant herself a husband."

    s3_mc "Let's ask her later and find out."
    s3_mc "In the meantime, let's get another one of these bags open!"
    "You take the next bag and open it up."
    s3_mc "Oh, this one's not nearly as tidy. Yikes."

    if s3_mc.bff == "Elladine":
        elladine "Is it Ciaran's or Tai's?"
        s3_mc "Judging by the size of this shirt, I'd say it's got to be Tai's."
        elladine "Woah. It's the size of this tent."
        elladine "Anything interesting in there?"
    elif s3_mc.bff == "Genevieve":
        genevieve "Is it Ciaran's or Tai's?"
        s3_mc "Judging by the size of this shirt, I'd say it's got to be Tai's."
        genevieve "Woah. It's the size of this tent."
        genevieve "Anything interesting in there?"
    elif s3_mc.bff == "Nicky":
        nicky "Is it Ciaran's or Tai's?"
        s3_mc "Judging by the size of this shirt, I'd say it's got to be Tai's."
        nicky "Woah. It's the size of this tent."
        nicky "Anything interesting in there?"
    elif s3_mc.bff == "Seb":
        seb "Is it Ciaran's or Tai's?"
        s3_mc "Judging by the size of this shirt, I'd say it's got to be Tai's."
        seb "Woah. It's the size of this tent."
        seb "Anything interesting in there?"

    s3_mc "Let's see..."
    "You fish around in the bag until your hand closes over something hard and small."
    s3_mc "What's this...?"
    "You pull it out and look at it. It's a small piece of pottery that fits nicely in your palm."

    if s3_mc.bff == "Elladine":
        elladine "It's so lumpy. It looks kind of like the shape of... a person?"
        s3_mc "Or a cow. Depending on which way you hold it."
        elladine "That's so weird!"
        elladine "I wonder what it is? Why did he bring it here?"
    elif s3_mc.bff == "Genevieve":
        genevieve "It's so lumpy. It looks kind of like the shape of... a person?"
        s3_mc "Or a cow. Depending on which way you hold it."
        genevieve "That's so weird!"
        genevieve "I wonder what it is? Why did he bring it here?"
    elif s3_mc.bff == "Nicky":
        nicky "It's so lumpy. It looks kind of like the shape of... a person?"
        s3_mc "Or a cow. Depending on which way you hold it."
        nicky "That's so weird!"
        nicky "I wonder what it is? Why did he bring it here?"
    elif s3_mc.bff == "Seb":
        seb "It's so lumpy. It looks kind of like the shape of... a person?"
        s3_mc "Or a cow. Depending on which way you hold it."
        seb "That's so weird!"
        seb "I wonder what it is? Why did he bring it here?"

    # CHOICE
    menu:
        s3_mc "I think Tai's piece of pottery is..."
        "A memento of a lost love":
            s3_mc "Maybe someone gave it to him, and he's too sentimental to throw it away."
            if s3_mc.bff == "Elladine":
                elladine "Aw. I could see him being sentimental like that."
            elif s3_mc.bff == "Genevieve":
                genevieve "Aw. I could see him being sentimental like that."
            elif s3_mc.bff == "Nicky":
                nicky "Aw. I could see him being sentimental like that."
            elif s3_mc.bff == "Seb":
                seb "Aw. I could see him being sentimental like that."
        "Protection against curses":
            if s3_mc.bff == "Elladine":
                elladine "So he doesn't end up as someone's enchanted husband?"
                elladine "Makes sense."
            elif s3_mc.bff == "Genevieve":
                genevieve "So he doesn't end up as someone's enchanted husband?"
                genevieve "Makes sense."
            elif s3_mc.bff == "Nicky":
                nicky "So he doesn't end up as someone's enchanted husband?"
                nicky "Makes sense."
            elif s3_mc.bff == "Seb":
                seb "So he doesn't end up as someone's enchanted husband?"
                seb "Makes sense."
        "A snack in case he gets hungry":
            if s3_mc.bff == "Elladine":
                elladine "You think he's going to eat it?"
            elif s3_mc.bff == "Genevieve":
                genevieve "You think he's going to eat it?"
            elif s3_mc.bff == "Nicky":
                nicky "You think he's going to eat it?"
            elif s3_mc.bff == "Seb":
                seb "You think he's going to eat it?"
            s3_mc "It'd be crunchy."
            "You pretend to start putting the pottery in your mouth."
            "[s3_mc.bff] laughs and wrestles it off you."
            if s3_mc.bff == "Elladine":
                elladine "[s3_name]!"
            elif s3_mc.bff == "Genevieve":
                genevieve "[s3_name]!"
            elif s3_mc.bff == "Nicky":
                nicky "[s3_name]!"
            elif s3_mc.bff == "Seb":
                seb "[s3_name]!"

    if s3_mc.bff == "Elladine":
        elladine "I guess the last bag must be Ciaran's, then?"
        "You unzip it and open it together. The smell of fresh laundry wafts from inside."
        elladine "Ooh, I love that smell."
        "Tucked in a side pocket of Ciaran's bag you find a small, flat piece of metal."
        s3_mc "I think it's a tag for a dog collar!"
        elladine "What does the engraving say?"
        s3_mc "It says 'Kerry.'"
        elladine "I guess that's his dog?"
    elif s3_mc.bff == "Genevieve":
        genevieve "I guess the last bag must be Ciaran's, then?"
        "You unzip it and open it together. The smell of fresh laundry wafts from inside."
        genevieve "Ooh, I love that smell."
        "Tucked in a side pocket of Ciaran's bag you find a small, flat piece of metal."
        s3_mc "I think it's a tag for a dog collar!"
        genevieve "What does the engraving say?"
        s3_mc "It says 'Kerry.'"
        genevieve "I guess that's his dog?"
    elif s3_mc.bff == "Nicky":
        nicky "I guess the last bag must be Ciaran's, then?"
        "You unzip it and open it together. The smell of fresh laundry wafts from inside."
        nicky "Ooh, I love that smell."
        "Tucked in a side pocket of Ciaran's bag you find a small, flat piece of metal."
        s3_mc "I think it's a tag for a dog collar!"
        nicky "What does the engraving say?"
        s3_mc "It says 'Kerry.'"
        nicky "I guess that's his dog?"
    elif s3_mc.bff == "Seb":
        seb "I guess the last bag must be Ciaran's, then?"
        "You unzip it and open it together. The smell of fresh laundry wafts from inside."
        seb "Ooh, I love that smell."
        "Tucked in a side pocket of Ciaran's bag you find a small, flat piece of metal."
        s3_mc "I think it's a tag for a dog collar!"
        seb "What does the engraving say?"
        s3_mc "It says 'Kerry.'"
        seb "I guess that's his dog?"

    # CHOICE
    menu:
        s3_mc "Ciaran brought a dog tag to Love Island..."
        "Maybe he's hoping to adopt one":
            if s3_mc.bff == "Elladine":
                elladine "What, while he's here?"
                s3_mc "You never know."
                s3_mc "A puppy could show up in the Villa one day and follow him home. So he needs to carry a tag with him just in case."
                elladine "I love the idea that anyone would be that prepared for random puppies."
            elif s3_mc.bff == "Genevieve":
                elladine "What, while he's here?"
                s3_mc "You never know."
                s3_mc "A puppy could show up in the Villa one day and follow him home. So he needs to carry a tag with him just in case."
                elladine "I love the idea that anyone would be that prepared for random puppies."
            elif s3_mc.bff == "Nicky":
                nicky "What, while he's here?"
                s3_mc "You never know."
                s3_mc "A puppy could show up in the Villa one day and follow him home. So he needs to carry a tag with him just in case."
                nicky "I love the idea that anyone would be that prepared for random puppies."
            elif s3_mc.bff == "Seb":
                seb "What, while he's here?"
                s3_mc "You never know."
                s3_mc "A puppy could show up in the Villa one day and follow him home. So he needs to carry a tag with him just in case."
                seb "I love the idea that anyone would be that prepared for random puppies."
        "He must have a dog at home":
            if s3_mc.bff == "Elladine":
                elladine "Stands for reason."
                elladine "It's kind of adorable that he brought her tag, then. He must miss her loads."
            elif s3_mc.bff == "Genevieve":
                genevieve "Stands for reason."
                genevieve "It's kind of adorable that he brought her tag, then. He must miss her loads."
            elif s3_mc.bff == "Nicky":
                nicky "Stands for reason."
                nicky "It's kind of adorable that he brought her tag, then. He must miss her loads."
            elif s3_mc.bff == "Seb":
                seb "Stands for reason."
                seb "It's kind of adorable that he brought her tag, then. He must miss her loads."
        "Maybe Kerry is his ex":
            if s3_mc.bff == "Elladine":
                elladine "...And she wore a dog tag?"
                s3_mc "Yeah. Maybe."
                elladine "I guess it's possible."
                elladine "I'm going to keep assuming it's his dog until you can show me some proof, though."
            elif s3_mc.bff == "Genevieve":
                genevieve "...And she wore a dog tag?"
                s3_mc "Yeah. Maybe."
                genevieve "I guess it's possible."
                genevieve "I'm going to keep assuming it's his dog until you can show me some proof, though."
            elif s3_mc.bff == "Nicky":
                nicky "...And she wore a dog tag?"
                s3_mc "Yeah. Maybe."
                nicky "I guess it's possible."
                nicky "I'm going to keep assuming it's his dog until you can show me some proof, though."
            elif s3_mc.bff == "Seb":
                seb "...And she wore a dog tag?"
                s3_mc "Yeah. Maybe."
                seb "I guess it's possible."
                seb "I'm going to keep assuming it's his dog until you can show me some proof, though."

    "[s3_mc.bff] starts zipping the suitcases closed again."

    if s3_mc.bff == "Elladine":
        elladine "Well, thanks for doing this with me. It's been really fun."
        elladine "Even though it raised a lot more questions that it answered."
        elladine "Especially Tai's weird little bit of pottery. I have no idea what that was supposed to be."
    elif s3_mc.bff == "Genevieve":
        genevieve "Well, thanks for doing this with me. It's been really fun."
        genevieve "Even though it raised a lot more questions that it answered."
        genevieve "Especially Tai's weird little bit of pottery. I have no idea what that was supposed to be."
    elif s3_mc.bff == "Nicky":
        nicky "Well, thanks for doing this with me. It's been really fun."
        nicky "Even though it raised a lot more questions that it answered."
        nicky "Especially Tai's weird little bit of pottery. I have no idea what that was supposed to be."
    elif s3_mc.bff == "Seb":
        seb "Well, thanks for doing this with me. It's been really fun."
        seb "Even though it raised a lot more questions that it answered."
        seb "Especially Tai's weird little bit of pottery. I have no idea what that was supposed to be."

    return

#########################################################################
## Episode 5, Part 2
#########################################################################
label s3e5p2:
    scene sand with dissolve
    $ on_screen = []

    show screen day_title(5, 2) with Pause(4)
    hide screen day_title with dissolve

    "Previously on Love Island..."
    "Three new Islanders appeared in a tent!"
    s3_mc "Where did that tent come from?"
    "I'll huff and I'll puff and I'll blow your tent down!"
    "Said none of the Islanders."
    "Coming up on Love Island..."
    "We're going deep down into the woods today..."
    ciaran "I'm getting flustered."
    "And you can be sure of a big surprise."
    tai "I used to think waterfalls were communal showers for giants."
    "Did someone say giants?"
    "I once had a dream I was in this giant world..."
    "And this giant made me eat a giant marshmallow."
    "When I woke up, my pillow was gone..."
    "Anyway, [s3_name] better get ready for her date before those giants come and get her to eat disproportionately-sized food."

    scene s3-dressing-room with dissolve
    $ new_scene()

    "You rummage about in the dressing room looking for something to wear."
    thought "I've got a date lined up with one of the new Islanders..."
    thought "And I don't even know who it's with!"
    thought "What should I wear to this mystery date?"

    # Add back once MC has images in game and delete narration line about changing.
    # Outfit change to evening wear
    # thought "Everyone liked this before!"
    "You grab something nice from your closet and put it on quickly."
    thought "This is perfect."
    # thought "This will do."

    "There is a rush of commotion and tumble of footsteps coming up the stairs."
    "Seb barges into the dressing room."
    seb "Oh, mate! Sorry."
    seb "I didn't mean to burst in like that."
    s3_mc "No worries, Seb."
    s3_mc "I'm already dressed."
    seb "You look nice, by the way."
    s3_mc "Thanks..."

    # Add back once MC has images in game
    # seb " Really? You're going in that?"
    # s3_mc "Yes!"
    # seb "Oh. Sorry! My head's in a funny place this morning."

    s3_mc "What are you doing rushing around?"
    seb "I'm excited, I think that's the right word."

    # CHOICE
    menu:
        thought "Seb is excited!"
        "That's a first":
            seb "Yeah... I guess it is."
            seb "It's a weird cheerful feeling."
            seb "Guess I'll have to get used to it."
        "Is it the end of the world?":
            seb "Mate, if it was the end of the world I would not be hanging around."
        "Have you had too much coffee?":
            seb "Nah, I haven't had any."

    s3_mc "What's got you all excited then?"
    seb "Brace yourself."
    seb "I got picked to go on a date with one of the new Islanders!"

    # CHOICE
    menu:
        thought "Seb has got a date!"
        "Who would ask you?":
            # NEED TO FILL
            "EMPTY"
        "Congratulations, mate":
            $ s3_mc.like("Seb")
            seb "Thanks."
            seb "I'm kinda stoked."
        "I've got a date too!":
            pass

    s3_mc "I got a date as well."

    if s3_mc.bff == "Seb":
        seb "Yes, mate! Good on you."
        "He pats you on the back."
    else:
        seb "Oh, cool!"
        
    seb "Who do you think invited you?"
    seb "Or should I say, who do you want it to be?"

    # CHOICE
    menu:
        thought "Who would I rather see on my date?"
        "Yasmin" if s3_mc.bisexual:
            $ s3_mc.like("Yasmin")
            seb "Yeah, she seems alright."
        "Tai":
            $ s3_mc.like("Tai")
            seb "Yeah, he looks like he could carry me with one arm."
        "Ciaran":
            $ s3_mc.like("Ciaran")
            seb "He seems like a dog person."
            seb "Like, dogs are fine from a distance, or whatever."
            seb "But I'm more of a cat person."
        "Both of them" if s3_mc.bisexual == False:
            $ s3_mc.like("Ciaran")
            $ s3_mc.like("Tai")
            seb "Ha! Yeah, fair enough."
            seb "I'd be knackered after one."
        "All three of them" if s3_mc.bisexual:
            $ s3_mc.like("Yasmin")
            $ s3_mc.like("Ciaran")
            $ s3_mc.like("Tai")
            seb "Ha! Yeah, fair enough."
            seb "I'd be knackered after one."

    s3_mc "Who do you think picked you?"
    seb "Well, don't get me wrong, Tai and Ciaran are great, but they're not really my type."
    seb "I'm pretty sure Yasmin picked me."
    "He starts combing his hair in front of a mirror."

    if s3_mc.current_partner == "AJ":
        seb "Shit, I nearly forgot to say..."
        seb "I think AJ and Elladine also got texts as well."
        s3_mc "AJ?"
        seb "Yeah..."
        seb "Might be worth having a chat with her to, like, check in where you both are."
    elif s3_mc.bff == "Seb":
        seb "AJ and Elladine also got a text."
        s3_mc "Really?"
        seb "Yeah, they seemed pretty excited about it."

    "Seb clears his throat."
    seb "I want to get dressed, so I guess I should head back."
    s3_mc "Yeah, you don't have much time."
    s3_mc "You'd better skedaddle!"
    seb "I'm going, I'm going."

    scene s3-outside-villa-entrance with dissolve
    $ new_scene()
    $ outfit = "swim"

    "[s3_mc.current_partner] runs out to you from the Villa."

    if s3_mc.current_partner == "Bill":
        bill "There you are!"
        s3_mc "Here I am..."
        bill "Love the outfit, by the way."
        s3_mc "Thanks!"
        bill "Love the outfit, by the way. That's a new one, isn't it?"
        s3_mc "Yeah, it is. Thanks!"
        bill "So, I bet you're one of the lucky people going on a date?"
        s3_mc "Yeah."
        s3_mc "How did you know?"
        bill "You're the most gorgeous girl in the Villa and you look like you're about to leave."
        bill "Doesn't take a genius to work it out."
    elif s3_mc.current_partner == "Camilo":
        camilo "There you are!"
        s3_mc "Here I am..."
        camilo "Love the outfit, by the way."
        s3_mc "Thanks!"
        camilo "Love the outfit, by the way. That's a new one, isn't it?"
        s3_mc "Yeah, it is. Thanks!"
        camilo "So, I bet you're one of the lucky people going on a date?"
        s3_mc "Yeah."
        s3_mc "How did you know?"
        camilo "You're the most gorgeous girl in the Villa and you look like you're about to leave."
        camilo "Doesn't take a genius to work it out."
    elif s3_mc.current_partner == "Harry":
        harry "There you are!"
        s3_mc "Here I am..."
        harry "Love the outfit, by the way."
        s3_mc "Thanks!"
        harry "Love the outfit, by the way. That's a new one, isn't it?"
        s3_mc "Yeah, it is. Thanks!"
        harry "So, I bet you're one of the lucky people going on a date?"
        s3_mc "Yeah."
        s3_mc "How did you know?"
        harry "You're the most gorgeous girl in the Villa and you look like you're about to leave."
        harry "Doesn't take a genius to work it out."
    elif s3_mc.current_partner == "AJ":
        aj "There you are!"
        s3_mc "Here I am..."
        aj "Love the outfit, by the way."
        s3_mc "Thanks!"
        aj "Love the outfit, by the way. That's a new one, isn't it?"
        s3_mc "Yeah, it is. Thanks!"
        aj "So, I guess you're off on a date as well?"
        s3_mc "Yeah."
        s3_mc "How did you know?"
        aj "You're the most gorgeous girl in the Villa and you look like you're about to leave."
        aj "Doesn't take a genius to work it out."

    # CHOICE
    menu:
        thought "[s3_mc.current_partner] thinks I'm the most gorgeous girl in the Villa!"
        "Nah, that title is already taken by you!" if s3_mc.current_partner == "AJ":
            $ s3_mc.like("AJ")
            aj "Oh, stop it, you."
            s3_mc "It's so true."
            "AJ beams from cheek to cheek."
        "You're pretty hot yourself":
            $ s3_mc.like(s3_mc.current_partner)
            if s3_mc.current_partner == "Bill":
                bill "Aw, no, but for real."
                bill "You're amazing."
            elif s3_mc.current_partner == "Camilo":
                camilo "Aw, no, but for real."
                camilo "You're amazing."
            elif s3_mc.current_partner == "Harry":
                harry "Aw, no, but for real."
                harry "You're amazing."
            elif s3_mc.current_partner == "AJ":
                aj "Aw, no, but for real."
                aj "You're amazing."
        "Flattery will get you nowhere":
            $ s3_mc.dislike(s3_mc.current_partner)
            if s3_mc.current_partner == "Bill":
                bill "Oh, sorry."
                bill "I was trying to be nice."
            elif s3_mc.current_partner == "Camilo":
                camilo "Oh, sorry."
                camilo "I was trying to be nice."
            elif s3_mc.current_partner == "Harry":
                harry "Oh, sorry."
                harry "I was trying to be nice."
            elif s3_mc.current_partner == "AJ":
                aj "Oh, sorry."
                aj "I was trying to be nice."
            s3_mc "Sure."
            "[s3_mc.current_partner] kicks a piece of gravel from the drive awkwardly."
        "You're just trying to put me off my date":
            $ s3_mc.dislike(s3_mc.current_partner)
            if s3_mc.current_partner == "Bill":
                bill "Oh, sorry."
                bill "I was trying to be nice."
            elif s3_mc.current_partner == "Camilo":
                camilo "Oh, sorry."
                camilo "I was trying to be nice."
            elif s3_mc.current_partner == "Harry":
                harry "Oh, sorry."
                harry "I was trying to be nice."
            elif s3_mc.current_partner == "AJ":
                aj "Oh, sorry."
                aj "I was trying to be nice."
            s3_mc "Sure."
            "[s3_mc.current_partner] kicks a piece of gravel from the drive awkwardly."

    if s3_mc.current_partner == "Bill":
        bill "Look, before you go off on your date..."
        "[he_she!c] looks at you, a little nervously."
        bill "I just wanted to check in on how you were feeling."
        bill "I don't want to be sitting here worrying about you if I don't have anything to worry about."
    elif s3_mc.current_partner == "Camilo":
        camilo "Look, before you go off on your date..."
        "[he_she!c] looks at you, a little nervously."
        camilo "I just wanted to check in on how you were feeling."
        camilo "I don't want to be sitting here worrying about you if I don't have anything to worry about."
    elif s3_mc.current_partner == "Harry":
        harry "Look, before you go off on your date..."
        "[he_she!c] looks at you, a little nervously."
        harry "I just wanted to check in on how you were feeling."
        harry "I don't want to be sitting here worrying about you if I don't have anything to worry about."
    elif s3_mc.current_partner == "AJ":
        aj "Look, before you go off on your date..."
        "[he_she!c] looks at you, a little nervously."
        aj "I just wanted to check in on how you were feeling."
        aj "Like, I obviously really like you."
        aj "But if you're going on this date with an open mind..."
        aj "Then I guess I'll try and do the same."

    # CHOICE
    menu:
        "[s3_mc.current_partner] wants to know where we're at..."
        "My head won't turn":
            $ s3e5p2_committed = True
            $ s3_mc.like(s3_mc.current_partner)
            if s3_mc.current_partner == "Bill":
                bill "For real?"
                s3_mc "Absolutely."
                bill "That's good to know."
            elif s3_mc.current_partner == "Camilo":
                camilo "For real?"
                s3_mc "Absolutely."
                camilo "That's good to know."
            elif s3_mc.current_partner == "Harry":
                harry "For real?"
                s3_mc "Absolutely."
                harry "That's good to know."
            elif s3_mc.current_partner == "AJ":
                aj "For real?"
                s3_mc "Absolutely."
                aj "That's good to know."
        "I'm keeping my options open":
            $ s3e5p2_options_open = True
            if s3_mc.current_partner == "Bill":
                bill "OK, well."
                bill "Thanks for being honest with me."
            elif s3_mc.current_partner == "Camilo":
                camilo "OK, well."
                camilo "Thanks for being honest with me."
            elif s3_mc.current_partner == "Harry":
                harry "OK, well."
                harry "Thanks for being honest with me."
            elif s3_mc.current_partner == "AJ":
                aj "OK, well."
                aj "Thanks for being honest with me."
        "Ask me after the date":
            if s3_mc.current_partner == "Bill":
                bill "Right, yeah. I will."
            elif s3_mc.current_partner == "Camilo":
                camilo "Right, yeah. I will."
            elif s3_mc.current_partner == "Harry":
                harry "Right, yeah. I will."
            elif s3_mc.current_partner == "AJ":
                aj "Right, yeah. I will."

    if s3_mc.current_partner == "Bill":
        call s3e5p2_partner_bill from _call_s3e5p2_partner_bill
    elif s3_mc.current_partner == "Camilo":
        call s3e5p2_partner_camilo from _call_s3e5p2_partner_camilo
    elif s3_mc.current_partner == "Harry":
        call s3e5p2_partner_harry from _call_s3e5p2_partner_harry
    elif s3_mc.current_partner == "AJ":
        call s3e5p2_partner_aj from _call_s3e5p2_partner_aj

    "A few cars pull up on the driveway to take the Islanders to their dates."
    "[s3_mc.current_partner] sighs."

    if s3_mc.current_partner == "Bill":
        bill "I guess you should go on your date now."
        s3_mc "Yeah."
    elif s3_mc.current_partner == "Camilo":
        camilo "I guess you should go on your date now."
        s3_mc "Yeah."
    elif s3_mc.current_partner == "Harry":
        harry "I guess you should go on your date now."
        s3_mc "Yeah."
    elif s3_mc.current_partner == "AJ":
        aj "I guess you should go on your date now."
        s3_mc "Yeah."
        aj "I'd better go on my date as well then."

    if s3_mc.current_partner == "Bill":
        if s3e5p2_options_open:
            "[s3_mc.current_partner] nods."
            bill "I'll see you in a bit."
        elif s3e5p2_committed:
            "[s3_mc.current_partner] gives you a brief but warm hug."
            bill "Hope you have a good time."
            bill "Kinda missing you already."
            s3_mc "Aw, babes. I won't be long!"
    elif s3_mc.current_partner == "Camilo":
        if s3e5p2_options_open:
            "[s3_mc.current_partner] nods."
            camilo "I'll see you in a bit."
        elif s3e5p2_committed:
            "[s3_mc.current_partner] gives you a brief but warm hug."
            camilo "Hope you have a good time."
            camilo "Kinda missing you already."
            s3_mc "Aw, babes. I won't be long!"
    elif s3_mc.current_partner == "Harry":
        if s3e5p2_options_open:
            "[s3_mc.current_partner] nods."
            harry "I'll see you in a bit."
        elif s3e5p2_committed:
            "[s3_mc.current_partner] gives you a brief but warm hug."
            harry "Hope you have a good time."
            harry "Kinda missing you already."
            s3_mc "Aw, babes. I won't be long!"
    elif s3_mc.current_partner == "AJ":
        if s3e5p2_options_open:
            "[s3_mc.current_partner] nods."
            aj "I'll see you in a bit."
        elif s3e5p2_committed:
            "[s3_mc.current_partner] gives you a brief but warm hug."
            aj "Hope you have a good time."
            aj "Kinda missing you already."
            s3_mc "Aw, babes. I won't be long!"

    scene s3-waterfall-date with dissolve
    $ new_scene()
    $ outfit = "evening"

    "You arrive at a small wooded clearing. A beautiful waterfall flows in the distance running into a crystal clear pool."
    "A small picnic has been laid out."
    thought "This is beautiful!"
    "You settle down on the picnic blanket and wait for your first date."

    if s3_mc.bisexual:
        call s3e5p2_yasmin_date from _call_s3e5p2_yasmin_date
        thought "I wonder who's going to be my next date..."

    call s3e5p2_ciaran_date from _call_s3e5p2_ciaran_date

    "You look over to the waterfall. A text alert goes off."
    s3_mc "Another text..."
    text "[s3_name], your next date will be arriving shortly."
    thought "Oh, wow! I'm busy today!"

    call s3e5p2_tai_date from _call_s3e5p2_tai_date

    return

label s3e5p2_partner_bill:
    "Bill looks at you and smiles."
    bill "Your eyes are gorgeous..."

    # CHOICE
    menu:
        thought "Bill said my eyes are gorgeous..."
        "Compliment him back":
            s3_mc "Thanks."
            s3_mc "You have nice ears."
            bill "Ears?"
            s3_mc "Yes. Is that a weird thing to say?"
            s3_mc "They're exactly the same size and shape. I mean exactly."
            s3_mc "It's... satisfying."
            bill "Maybe I should become an ear model after all this."
            s3_mc "All the jewellery companies will wanna snap you up!"
        "Tell him how cheesy that was":
            s3_mc "Is that the best line you could come up with?"
            bill "Honest, hand on heart. I think they're stunning."
            s3_mc "Maybe I'll give you a pass, then."
        "Stare at him with wild eyes until he changes his mind":
            "You widen your eyes."
            s3_mc "How about now?"
            bill "Er, bit scary but still beautiful."
            "You widen them even more."
            s3_mc "What about now?"
            bill "Please stop."
            "You use your fingers to make your eyes as big as possible."
            s3_mc "What about now?"
            bill "I didn't need to sleep tonight anyway..."
            "You relax your eyes."

    "He laughs and gives you a squeeze."
    s3_mc "I like this vibe though."
    bill "Me showering you with compliments?"
    s3_mc "Exactly, and I'll give you extra points if you can come up with a compliment I've never heard before."
    "Bill rubs his chin."
    bill "I think you're very... no, you'll definitely have heard that one."
    bill "You have a great..."
    bill "...no."
    bill "Got it!"
    bill "You're like a mole."
    s3_mc "A mole?"
    bill "Hear me out."
    "He ticks times off on his fingers."
    bill "One, they're adorable. Find me someone who doesn't like moles. Don't bother. You can't."
    bill "Two, they are literally down to earth. Three, they have glossy beautiful hair."
    bill "Er, fur."
    bill "Same thing."
    s3_mc "Bravo.Not to mention four, they live in a dark hole and eat worms, just like me."
    bill "See? Perfect animal to compare you to."
    s3_mc "Fine, you get the points. That was definitely an original!"
    "He laughs and gives you a squeeze."
    bill "This is great. Just hanging out and being silly."
    bill "That's all you need, innit?"
    s3_mc "All you need?"
    s3_mc "I can think of plenty of other stuff I enjoy doing with people I fancy."
    "You run a finger lightly down his chest."
    bill "Well, I mean, yeah."
    "He thinks."
    bill "Honestly, yeah. That and playing video games together."

    # CHOICE
    menu:
        thought "Bill likes video games..."
        "Great, another guy who likes games":
            $ s3_mc.dislike("Bill")
            s3_mc "You roll your eyes a little."
            bill "Hey, games are fun."
            bill "Helps me unwind after work."
            s3_mc "That's good, then. They're just not for me."
            bill "I have a game I think could change your mind."
        "Awesome, what's your fave?":
            $ s3_mc.like("Bill")
            bill "Well, in general I tend to go for action games like Duty Calls, or stuff like Football Boss."
            bill "There's one exception."
            bill "The best game ever made: Captain Chicken's Galactic Command."
            s3_mc "I've never even heard of that."
            bill "Most people haven't. It's a tragedy."
            bill "Captain Chicken was this restaurant in the 90s. It's been closed for yonks, but they did this big marketing push and released a game before going belly up."
            s3_mc "What's it like?"
            bill "Hard to explain, really. You play Captain Chicken, but... in space?"
            bill "You build up your ship, which is shaped like the restaurant, and then you fight other ships."
            bill "But the fighting is kind of a golf game."
            s3_mc "A... golf game?"
            bill "Yeah, and if you mess up, it becomes a bit of a cross between Minesweeper and Pinball."
            s3_mc "..."
            bill "I said it was hard to explain! Anyway, it's brilliant."
            bill "It got really bad reviews at the time, though. People just don't know what's good."
            s3_mc "You'll have to show me someday."
            "He smiles broadly."
            bill "I'd love that."
        "I've never really played a video game":
            bill "Yeah, not everyone's into gaming."
            bill "I know which game I'd get you to try if you were interested, though."
            s3_mc "Oh?"

    return

label s3e5p2_partner_harry:
    "Harry puts his hand on your chin and tilts your head to look deeply into your eyes."
    harry "I really wanna kiss you, [s3_name]."

    # CHOICE
    menu:
        thought "Harry wants to kiss me..."
        "Let him kiss you":
            "You lean ín and whisper in his ear."
            s3_mc "What are you waiting for?"
            "Suddenly, Harry's mouth is on yours and his hands are on your body. He kisses you urgently and passionately."
        "Tease him a bit, but let him kiss you":
            "You lean and put your lips very close to his. When he moves forward, you move back slightly."
            "You do it again."
            harry "This is torture..."
            s3_mc "Yep."
            "Harry stops trying to kiss you. You wait like that for a few moments, your lips millimetres from his."
            "You can feel his warm breath."
            "Finally, you kiss him. It's urgent and passionate. You don't stop for several minutes."
        "Talk to him instead":
            "You lean and put your lips very close to his. When he moves forward, you move back slightly."
            harry "You alright?"
            s3_mc "Not today."
            harry "No problem. I don't wanna pressure you."
            s3_mc "Thanks."
            "You plant a soft kiss on his cheek."

    "Harry puts his arms around you, and you settle against him, feeling the soft thud of his heart beating."
    harry "I wanna know all about you, [s3_name]."
    s3_mc "Well, what do you wanna know?"
    harry "What do you do outside of work? Like, for fun?"

    # CHOICE
    menu:
        thought "My hobby?"
        "I play an instrument":
            harry "Oh cool, what do you play?"
            # SUB-CHOICE
            menu:
                s3_mc "I play..."
                "The trombone":
                    # NEED TO FILL
                    "EMPTY"
                "The guitar":
                    # NEED TO FILL
                    "EMPTY"
                "The violin":
                    harry "If you had it here, you could play it when someone told a sad story."
                    s3_mc "...or when Seb said literally anything."
        "I play a sport":
            harry "Oh cool, what do you like doing?"
            # SUB-CHOICE
            menu:
                s3_mc "I..."
                "Fence":
                    # NEED TO FILL
                    "EMPTY"
                "Do boxing":
                    # NEED TO FILL
                    "EMPTY"
                "Play football":
                    harry "Oh nice. So you..."
                    s3_mc "'Know how to handle balls?'"
                    harry "How did you know I was going to say that?"
                    s3_mc "Just a guess."
        "I practice art":
            harry "Oh cool, what do you do?"
            # SUB-CHOICE
            menu:
                s3_mc "I..."
                "Write":
                    # NEED TO FILL
                    "EMPTY"
                "Dance":
                    harry "Ooh, what kind of dance?"
                    # SUB-SUB-CHOICE
                    menu:
                        thought "What kind of dance do I do?(no further reactions)"
                        "Salsa":
                            pass
                        "Ballroom":
                            pass
                        "Ballet":
                            pass
                        "Modern":
                            pass
                    harry "Wow, that's so cool."
                    harry "Girls, who can dance are well sexy."
                    harry "I'm not really a good dancer, but if you act like you don't care, people think you're cool anyway."
                "Paint":
                    harry "What sort of things do you paint?"
                    # SUB-SUB-CHOICE
                    menu:
                        s3_mc "All sorts of stuff, but mostly..."
                        "Oil paintings":
                            pass
                        "Watercolours":
                            pass
                        "Comics":
                            pass
                    harry "Nice. I'm pretty bad at art and stuff. I'm more of a business guy."
                    harry "Let me know if you wanna set up a business selling your art!"
                    s3_mc "I'll bear that in mind!"

    s3_mc "What about you? What do you do for fun?"
    harry "OK, have you heard of FuryStone?"
    s3_mc "It's like a game, right?"
    harry "Yeah, it's a fantasy digital card thing. It's so much fun."

    # CHOICE
    menu:
        s3_mc "I think that fantasy stuff is..."
        "A bit weird, to be honest":
            $ s3_mc.dislike("Harry")
            # NEED TO FILL
            "EMPTY"
        "Cool, but not my thing":
            $ s3_mc.like("Harry")
            harry "Well, would you want to give it a go one day?"
            s3_mc "Yeah, maybe. I'd like that."
        "Pretty awesome":
            $ s3_mc.like("Harry")
            harry "Nice!"
            s3_mc "I love the swords, sorcery and spells! It's all right up my street."

    harry "You know, the wizards and monsters and stuff are just a cool extra."
    harry "It's actually a really deep, complex game. I'm pretty good."

    # CHOICE
    menu:
        thought "Harry says he's pretty good at FuryStone..."
        "I bet I could beat you":
            harry "Oh, a challenger approaches?"
            harry "You better watch out. I just unlocked a new wand..."
            s3_mc "I hope your wand is up to the task."
            harry "You bet it is!"
            harry "...You were talking about the replica of the Alder Wand card from FuryStone, right?"
            s3_mc "No, I mean..."
            harry "I'm kidding. I know what you mean."
        "Can you win money?":
            harry "You can at the higher levels. They fly you out to LA and stuff, it's really cool."
            harry "I'm still trying to qualify for that."
            s3_mc "Will you take me to LA if you win one?"
            harry "Sure thing... if I win."
        "Will you teach me one day?":
            $ s3_mc.like("Harry")
            harry "I'd love to!"
            harry "Though, I'm not that good a teacher, if I'm honest."
            harry "I tend to over-complicate things a bit..."
            harry "I get way too into the high-level strategy!"
            # SUB-CHOICE
            menu:
                thought "Harry gets too caught up with advanced strategy..."
                "Bring it on":
                    # NEED TO FILL
                    "EMPTY"
                "I'll try and keep up":
                    harry "They say the best way to learn is to jump into the deep end."
                    s3_mc "Do they say that?"
                    harry "Well... I say that."
                    harry "I just love that you're showing an interest."
                    harry "Nobody else I've dated ever has."
                "Go easy on me":
                    harry "I'll try!"
                    harry "I just love that you're showing an interest."
                    harry "Nobody else I've dated ever has."

    harry "My mates sometimes take the mick out of me for taking a card game so seriously."
    harry "But I don't like doing things unless I can do them properly."
    harry "I might not be the best FuryStone player in the world, but I want to keep improving."
    harry "I want to feel like I have a shot at winning every game."

    # CHOICE
    menu:
        thought "Harry is so focused on FuryStone..."
        "That's a questionable use of time":
            $ s3_mc.dislike("Harry")
            # NEED TO FILL
            "EMPTY"
        "That's cute":
            $ s3_mc.like("Harry")
            harry "Thanks."
            "He smiles at you."
        "That's a very sexy attitude":
            $ s3_mc.like("Harry")
            harry "Well, if a task is worth doing..."
            harry "I make sure I do it properly."
            "He winks at you."
    
    return

label s3e5p2_partner_camilo:
    "Camilo's muscles gleam and his eyes are like darf pools. You feel as if you could dive into them and fall forever."

    # CHOICE
    menu:
        thought "What should I do?"
        "Kiss him fast":
            pass
        "Kiss him slow":
            "You move in closer, and ever so slowly press your mouth to his. You take your time, breathing in the scent of his cologne and the heat of his body."
            "He returns the kiss with the same intensity, running his hands over every inch of your exposed skin."
            "You pull apart, pulses racing. Camilo pulls you into a hug and you spend a few minutes just listening to the sound of his heart."
        "Give him a cuddle":
            "You put your arms around him and he returns the gesture, enveloping you in sun-warmed muscle."
            "You spend a few minutes just resting there, listening to the sound of his heart."

    "Camilo strokes your hair idly."
    camilo "I've got a question for you, [s3_name]."
    camilo "It's a big one."
    s3_mc "OK, bring it on."
    camilo "I'm serious. This is gonna tell me a lot about you."
    s3_mc "I feel like we already know each other pretty well?"
    camilo "Nah, this goes above and beyond."
    s3_mc "Just ask the question!"
    camilo "Right."
    camilo "Do you think hotdogs are a sandwich?"

    # CHOICE
    menu:
        thought "Are hotdogs sandwiches?"
        "That's your big question?":
            $ s3_mc.dislike("Camilo")
            # NEED TO FILL
            "EMPTY"
        "Yes, absolutely":
            s3_mc "Yes."
            camilo "Wow, no hesitation."
            s3_mc "Well it's obvious, isn't it?"
            s3_mc "Bread, filling, boom, Sandwich."
            camilo "I don't think it's that simple."
            s3_mc "Well it's obvious, isn't it?"
            camilo "Oh boy, here we go."
            camilo "A sandwich is a beautiful thing. It's pure. A good sandwich is more than a lunch. It's... art."
            s3_mc "And a hotdog isn't?"
            camilo "No. It's just a sausage in a bun. There's no creativity there, you feel me?"
            s3_mc "What about ketchup? Relish? Onion bits?"
            camilo "All well and good, but a hotdog can never reach the lofty heights of sandwich...ness."
            s3_mc "I see."
        "No, definitely not":
            $ s3_mc.like("Camilo")
            s3_mc "No."
            camilo "Wow, no hesitation. You're a girl who knows her mind."
            s3_mc "Well it's obvious, isn't it?"
            s3_mc "A sandwich is more than just 'some bread' and 'something else'."
            s3_mc "It's got structural requirements that a hotdog just doesn't fulfil."
            "He whistles."
            camilo "You really  know your stuff. I totally agree. A good sandwich isn't just lunch. It's..."
            "You both say 'art' at the same time."
            camilo "Exactly!"

    camilo "My sandwich opinions have got me into trouble once or twice."
    camilo "I once got into a very heated argument about what sauce to put on a bacon sarnie."
    s3_mc "Oh. Wow."
    camilo "On a first date."
    s3_mc "Oh wow!"
    camilo "In my defence, she started it."
    s3_mc "I'm not sure that's as much of a defence as you think it is."
    camilo "Well, we were very young."
    camilo "You must have had bad dates that were kinda sorta your fault too?"

    # CHOICE
    menu:
        thought "Have I messed up any dates?"
        "All my dates have been good":
            # NEED TO FILL
            "EMPTY"
        "None of my bad dates were my fault":
            # NEED TO FILL
            "EMPTY"
        "Maybe once or twice":
            s3_mc "Yeah, hasn't everyone?"
            s3_mc "Especially when they're younger. Nobody's amazing at dates right off the bat."
            camilo "It's hard to imagine you mucking up a date."

    camilo "You're so hot and fun to be around!"
    s3_mc "You always say how fun I am, how good my banter is..."
    s3_mc "Is that all you've got to say about me?"
    camilo "Well, I, er..."
    s3_mc "I'm just teasing you. Mostly."
    camilo "I really like you, [s3_name]. I think you're brilliant."
    camilo "But this is all a bit new to me, plus I'm not very good at words and that."
    s3_mc "That's OK."
    "He reaches out and pulls you into a big, warm hug."

    return

label s3e5p2_partner_aj:
    "AJ smiles at you and glances at your lips."

    # CHOICE
    menu:
        thought "I should..."
        "Compliment her":
            # NEED TO FILL
            "EMPTY"
        "Whistle a tune":
            # NEED TO FILL
            "EMPTY"
        "Kiss her":
            s3_mc "Are you thinking what I'm thinking?"
            aj "Oh yeah."
            "You hurriedly lean in towards each other."
            "It's a hot fast minute of kissing."
            "As you pull away, she grins at you."
            aj "I love kissing you."

    aj "Do you think you've ever, like..."
    aj "Fallen head over heels for someone?"

    # CHOICE
    menu:
        thought "Have I fallen head over heels?"
        "Nope, never":
            # NEED TO FILL
            "EMPTY"
        "Oh yeah, definitely":
            "AJ looks a little surprised."
            aj "Was it scary?"
            s3_mc "Yeah, totally."
        "I can't walk in heels":
            aj "Yeah, me neither."

    aj "I'm not sure if I've been in a relationship long enough to know if I've fallen for someone."
    aj "I tend to get, like, bored or distracted before it could really go anywhere..."
    "She bites her skin on her thumb nervously."
    aj "But, yeah, anyway!"
    aj "Speaking of heels..."
    aj "We've got to talk about clothes."
    aj "For me, one of the best things about dating girls is borrowing each other's clothes."
    aj "That's not going to be a problem, is it?"

    # CHOICE
    menu:
        thought "AJ wants to steal my clothes!"
        "I don't share clothes":
            # NEED TO FILL
            "EMPTY"
        "What about shoes as well?":
            aj "Sure! Though I do have size 9 feet."
        "That's inevitably going to happen":
            $ s3_mc.like("AJ")
            aj "Yes!"

    aj "Not going to lie, back home I mainly just live in trainers, hockey shirts, snapbacks, plaid, and boxers."

    # CHOICE
    menu:
        thought "Hockey shirts, plaid, and boxers..."
        "That's a stereotypical look, right?...":
            $ s3_mc.dislike("AJ")
            # NEED TO FILL
            "EMPTY"
        "That's exactly what I wear too!":
            $ s3_mc.like("AJ")
            aj "Perfect! We can mix and match!"
        "My style is very different":
            $ s3_mc.like("AJ")
            aj "Well, we can have fun trying each other's styles!"

    return


label s3e5p2_yasmin_date:
    "Someone taps you on the shoulder."
    yasmin "Guess who?"
    s3_mc "Yasmin?"
    yasmin "Yeah, how did you know?"
    "She smiles and sits down on the rug, patting the place beside her."
    s3_mc "Lucky guess."
    yasmin "Are you not even a little bit surprised to see me?"

    # CHOICE
    menu:
        thought "Am I surprised to see Yasmin?"
        "Yeah! I had no idea":
            yasmin "Surprise."
        "I knew you fancied a bit of me":
            yasmin "Who wouldn't?"
        "No, my gaydar never fails":
            yasmin "Mine is usually awful."
            yasmin "But I'm glad I was right this time!"

    if s3e5p1_rummage_suitcases:
        yasmin "So, apart from rummaging around in people's luggage, what do you do for fun?"
        s3_mc "Hey!"
        s3_mc "You told me I could..."
        yasmin "I'm teasing, babe, I'm teasing."
        yasmin "You've got a curious mind. I like that."
        s3_mc "I found a pin badge in your bag."
        s3_mc "Enchanted Husband?"
        "She smiles mischievously."
        yasmin "What do you think it is?"

        # CHOICE
        menu:
            thought "What do I think Enchanted Husband is?"
            "A bespoke personal body massager":
                # NEED TO FILL
                "EMPTY"
            "A club for witches seeking revenge":
                s3_mc "Is this some kind of secret cult?"
                yasmin "Yes."
                yasmin "Never dishonor the Night Mother."
                "She burst out laughing."
                yasmin "No, it's not that."
                yasmin "It's the name of the band I used to be in!"
            "An indie band":
                yasmin "Yeah!"
                yasmin "It's a pin from the merch we had."
                s3_mc "We?"
                yasmin "Oh, yeah. It's my old band."

        s3_mc "Were you the singer?"
        yasmin "Nah, I was the bassist."
        yasmin "Though I do sing as well!"

        # CHOICE
        menu:
            thought "Yasmin played bass!"
            "What is that?":
                # NEED TO FILL
                "EMPTY"
            "Bass is so easy":
                # NEED TO FILL
                "EMPTY"
            "I can play the bass":
                $ s3_mc.like("Yasmin")
                yasmin "You can?!"
                s3_mc "Yeah!"
                yasmin "That's sick. We should jam."
                s3_mc "You're on."
            "Bass is so sexy":
                $ s3_mc.like("Yasmin")
                yasmin "Yeah, it is, isn't it?"
                s3_mc "Absolutely."
                yasmin "Means I'm good with my hands."

        yasmin "So, what kind of music do you like?"

        # CHOICE
        menu:
            s3_mc "I like..."
            "Grime":
                # NEED TO FILL
                "EMPTY"
            "Pop":
                yasmin "Yeah, everyone in my old band used to trash talk pop."
                s3_mc "People just find it really easy to hate things that are popular."
                yasmin "Yeah, totally. It makes people feel superior when they have a big opinion on something lots of people like."
                yasmin "It's not my go to genre, but I always listen to it because I think it's important as an artist to try and understand why something is super popular."
                yasmin "That's one of the reasons I left the band. We never saw eye to eye about that."
                yasmin "It's like, hello? Everyone likes pop music. That must mean there's something good there."
            "Indie stuff":
                $ s3_mc.like("Yasmin")
                yasmin "Me too!"
                yasmin "I mean, that was what our band genre sort of was so obviously I listen to it, like, all the time."
                yasmin "And if you like that stuff, you should give us a listen."
            "I'm actually in a band myself" if s3_mc.job == 'Musician':
                $ s3_mc.like("Yasmin")
                yasmin "Yeah, I heard about that!"
                yasmin "See, that just means we're sympatico."
                s3_mc "How come?"
                yasmin "I'm in a band too!"
                yasmin "Or rather, I used to be."
                yasmin "We broke up."
    else:
        s3_mc "You were in a band?"
        yasmin "Yeah, for years."

    s3_mc "So, how come you're not with the band anymore?"
    yasmin "I'm trying to find my own weird and wonderful sound."
    yasmin "I've played with all kinds of people. I've even written songs for some big-name artists, when I needed the money"
    yasmin "But I've never been able to just make my own music, exactly the way I want."
    yasmin "That's my mission, anyway."
    yasmin "To discover my voice."

    # CHOICE
    menu:
        thought "Yasmin wants to find her own voice..."
        "Yeah, whatever":
            # NEED TO FILL
            "EMPTY"
        "How inspiring!":
            thought "The way she talks is so inspiring!"
        "That's sexy af":
            "You smile at her as she chats."
            thought "Wow. I love the sound of her voice... I could listen to her talk all day."

    yasmin "Sorry, I'm not normally this much of a chatterbox."
    yasmin "I'm just trying to impress you, because, like..."
    yasmin "I feel like I've got to sell myself on this one tiny date."
    "She looks at you shyly."

    # CHOICE
    menu:
        thought "Yasmin says she's trying to impress me..."
        "Sorry, but I'm loyal to [s3_mc.current_partner]":
            yasmin "OK."
            yasmin "At least I know."
            yasmin "Damn, was that a text?"
        "You're too much for me":
            $ s3_mc.dislike("Yasmin")
            yasmin "OK."
            yasmin "At least I know."
            yasmin "Damn, was that a text?"
        "Good news, it's working":
            $ s3_like_yasmin = True
            $ s3_mc.like("Yasmin")
            $ s3e5p2_confess_attraction_yasmin = True
            yasmin "Really?"
            "She breathes a deep sigh of relief."
            yasmin "I can't tell you how awesome it is to hear you say that."
            "Yasmin fans herself with her hand."
            yasmin "This has made me more nervous than I expected."
            yasmin "I need to cool off."
            "She looks at the clear blue pool where the waterfall is running into."
            yasmin "Want to come in with me?"
            # SUB-CHOICE
            menu:
                thought "I should..."
                "Jump in holding her hand":
                    s3_mc "Mind if I hold your hand while we jump?"
                    yasmin "That would be amazing."
                    "You take her soft hand in yours, they fit perfectly together."
                    yasmin "Right, on the count of three."
                    yasmin "One.. two..."
                    s3_mc "Three!"
                    "You both leap into the air and jump into the water."
                    "You both splash about in the water together."
                    yasmin "I love the water here."
                    yasmin "Damn, was that a text?"
                    yasmin "We'd better get out and see what it says."
                    "You both clamber out of the water. Water droplets trickle down her body."
                "Cannonball!":
                    $ s3e5p2_jump_in_water = True
                    "You run and leap into the air, tucking your legs up to your chest before you plummet into the water."
                    s3_mc "Cannonball!"
                    yasmin "Hey!"
                    "She runs after you and tries to do the same."
                    yasmin "Timer!"
                    "She lands on her belly."
                    yasmin "Owch."
                    yasmin "That's going to sting in the morning."
                    "You both splash about in the water together."
                    yasmin "I love the water here."
                    yasmin "Damn, was that a text?"
                    yasmin "We'd better get out and see what it says."
                    "You both clamber out of the water. Water droplets trickle down her body."
                "Let her go in alone":
                    yasmin "Suit yourself..."
                    "Yasmin splashes some water on her face to cool down."
                    yasmin "Damn, was that a text?"

    yasmin "What does it say?"
    text "[s3_name], your next date will be arriving shortly."
    s3_mc "I've got another date!"
    yasmin "Aw, where does the time go?"
    yasmin "I hope you have fun."
    yasmin "I've got Seb next."
    s3_mc "You chose Seb?"
    yasmin "Yeah, I heard he was into music, so why not?"
    yasmin "I wanna know what he's hiding behind that hard exterior."

    if s3_like_yasmin:
        yasmin "This was great. I hope we'll be seeing a lot more of each other."
    else:
        yasmin "Anyway it was nice to get to know you!"
        yasmin "See you around!"

    $ leaving("yasmin")

    return

label s3e5p2_ciaran_date:
    "Ciaran walks over to you, waving frantically."
    ciaran "Hi!"
    ciaran "It's me."
    ciaran "Ciaran..."
    ciaran "Without a fada!"

    # CHOICE
    menu:
        thought "Ciaran picked me to have a date!"
        "Let's have a hug":
            $ s3_mc.like("Ciaran")
            "You stand up and give him a hug."
            "He smiles excitedly and hugs you tight."
            s3_mc "It's good to see you."
            ciaran "Yeah, it's good to see you!"
            "You both sit down on the picnic blanket."
        "How could I forget about the fada?":
            "He sits down beside you."
            ciaran "I know, but I find it's helpful to remind people."
            ciaran "Maybe in case you had to write me a letter or something."
            ciaran "I love the idea of getting love letters."
        "Ugh...":
            $ s3_mc.dislike("Ciaran")
            "You let out a long, loud groan."
            ciaran "Oh..."
            "Ciaran sits down awkwardly on the picnic rug."
            ciaran "Nice to see you too."

    ciaran "Um, so..."

    if s3e5p2_jump_in_water:
        ciaran "Dare I ask why you're wet?"
        s3_mc "I went for a swim with Yasmin."
        ciaran "Aw, that's cute."

    if s3e5p1_rummage_suitcases:
        s3_mc "I had a rummage in your bag earlier..."
        ciaran "I hoped you would."
        ciaran "Find anything you wanted to ask me about?"
        s3_mc "Yeah, that tag with 'Kerry' engraved on it..."
        ciaran "Ah, yeah. Kerry is my dog!"

        # CHOICE
        menu:
            thought "'Kerry' is Ciaran's dog!"
            "Aw, I totally love dogs":
                $ s3_mc.like("Ciaran")
                ciaran "You do! Great."
                ciaran "That's like all my boxes ticked then."
                s3_mc "Yeah, They're just a bundle of good vibes."
            "You look like a lost puppy":
                "He makes his eyes wide like a puppy-dog."
                ciaran "Can't shake these shiny new boy vibes."
            "I thought Kerry was your ex":
                ciaran "If I had a dog tag with my ex's name on it..."
                "He laughs out loud."
                ciaran "It'd sound the alarm bells, for sure."
                ciaran "But no, it's my dog. Kerry."
    else:
        "Ciaran smiles at you shyly and looks over to the waterfall."
        ciaran "Sorry, I'm never that good with the craic."
        s3_mc "That's alright."
        ciaran "I'm just going to head straight into my comfort zone and start talking about pets."
        ciaran "Specifically, dogs."
        s3_mc "I'm guessing you have a dog then?"
        ciaran "Yeah, she's such a good girl."

    s3_mc "What kind of dog is she?"
    "He smiles and seems to visibly relax."
    ciaran "She's an Irish Setter! All big and red and shaggy."
    ciaran "We got her from County Kerry in a place called Dingle."
    ciaran "I really wanted to name her Dingle but mam was having none of it."
    ciaran "So we settled and named her Kerry."
    ciaran "But, yeah. I love her. She's great. I hope you get to meet her one day."
    ciaran "Wait. Oops. Was that a bit too soon?"

    # CHOICE
    menu:
        thought "Ciaran wants me to meet his dog?"
        "I'd love to meet Kerry!":
            $ s3_mc.like("Ciaran")
            ciaran "Aw, grand. That's grand."
            ciaran "She'd love you, I'm sure."
            "Ciaran shuffles a little closer to you."
        "Way too soon":
            $ s3_mc.dislike("Ciaran")
            ciaran "Ah, right yeah, sorry."
            "He shifts uncomfortably on the picnic rug."
        "I'm allergic":
            ciaran "Aw, that's OK, she can be, like, not around if you ever came round or something..."

    ciaran "Right... uh, what else is a good chat on a date?"
    ciaran "Sorry."
    ciaran "I'm getting flustered."
    ciaran "Well nervous around you."
    ciaran "You're just so gorgeous and I'm not the best at this stuff."
    thought "Ciaran sounds like he's struggling..."
    thought "Maybe I should help him out!"

    # CHOICE
    menu:
        thought "What should I talk to Ciaran about? (you can only choose two)"
        "How come you're single?":
            ciaran "I'm such a rubbish romantic. Thought this would be the best place to put it to practice."
            ciaran "I've had a few flings here and there but it never quite sticks, somehow."
            ciaran "How about you?"
            # SUB-CHOICE
            menu:
                thought "Why am I single?"
                "I'm hard to pin down":
                    ciaran "I mean you're gorgeous. "
                    ciaran "I imagine people struggle to keep up sometimes."
                "I've never met the right one":
                    ciaran "I mean you're gorgeous. "
                    ciaran "I imagine people struggle to keep up sometimes."
                "I recently came out of a long term relationship":
                    ciaran "Oh, really?"
                    s3_mc "Yeah."
                    "Ciaran clears his throat to regain his composure."
                    ciaran "That must have been tough for you."
                    ciaran "I hope you're holding up OK in here?"
                    s3_mc "Thanks Ciaran."
        "Serve some cheesy chat up lines":
            $ s3_mc.like("Ciaran")
            s3_mc "You're really sweet."
            s3_mc "If you were a fruit you'd be a fineapple."
            "He grins."
            ciaran "Cheesy chat up lines! Now that's something I can work with."
            ciaran "If you were a vegetable you'd be a cutecumber!"
            s3_mc "Cute."
            ciaran "Do you like raisins?"
            s3_mc "How about a date?"
            "You both fall about laughing."
            ciaran "Was that an earthquake?"
            ciaran "Or did you just rock my world?"
            thought "I would totally rock his world."
        "Talk about your job":
            s3_mc "Well we can chat about our work."
            ciaran "Good idea. So, you're a [s3_mc.job!l], aren't you?"
            s3_mc "Yeah!"

            if s3_mc.job == "Scientist":
                ciaran "What's your, like, chosen sciency thing?"
                # CHOICE
                menu:
                    thought "What do I do in science?"
                    "Prevent bleaching of the coral reef":
                        pass
                    "Research environmentally friendly plastic":
                        pass
                    "Inventing the scientifically perfect cocktail":
                        pass
                ciaran "That's fierce."
                ciaran "I can see the headlines now."
                ciaran "[s3_name] saves the world."
                s3_mc "Fingers crossed."
            elif s3_mc.job == "Musician":
                ciaran "So, are you in like a band..."
                ciaran "Or just a one woman band?"
                # CHOICE
                menu:
                    s3_mc "I am..."
                    "In a band":
                        pass
                    "A solo artist":
                        pass
                    "Part of an orchestra":
                        pass
                ciaran "That's so cool!"
                ciaran "I'm rubbish on stage. Would probs forget my lines."
                s3_mc "We don't have lines."
                s3_mc "We have, like, musical notes and lyrics."
                ciaran "Aren't lyrics just musical lines?"
                ciaran "I don't know..."
            elif s3_mc.job == "Athlete":
                ciaran "What sport do you, like, do for work?"
                # CHOICE
                menu:
                    s3_mc "I'm a..."
                    "Footballer":
                        pass
                    "Runner":
                        pass
                    "Boxer":
                        pass
                ciaran "Wow, that sounds intense to do everyday as a job."
                s3_mc "Yeah, it can be."
            elif s3_mc.job == "Model":
                ciaran "What sort of stuff do you model?"
                # CHOICE
                menu:
                    thought "Ciaran wants to know what I model."
                    "Bikinis":
                        pass
                    "Makeup":
                        pass
                    "Furniture":
                        pass
                ciaran "Ah, yeah. That must mean you get, like, tonnes of free stuff."
                s3_mc "Yep. Loads."

    ciaran "I'm a bouncer for this club in Waterford which is near where I live. Just dealing with people on the lash."
    s3_mc "Wow! That must be hard work."
    ciaran "Yeah it can be super tough!"
    ciaran "I'm also the security guard for these bingo nights."
    ciaran "They would always be effin' and blindin' about what number got called when."
    ciaran "It can proper kick off sometimes."

    ciaran "Aw, was that a phone?"
    ciaran "Damn."
    ciaran "It's time to go to my next date."
    ciaran " We didn't even get a chance to start on the food."

    # CHOICE
    menu:
        thought "Ciaran's going to his next date."
        "Who is it with?":
            s3_mc "Who else did you pick?"
            ciaran "Elladine. Thought I might as well give it a try."
        "Just stay with me":
            $ s3_mc.like("Ciaran")
            "Ciaran smiles."
            ciaran "I wish I could."
        "Bye-bye":
            ciaran "Um, yeah, bye. I guess."

    ciaran "Before I go..."
    ciaran "I just wanted to ask, like..."
    "He points to himself."
    ciaran "I know I'm not the smoothest talker..."
    ciaran "But could you ever see yourself with a fella like me?"

    # CHOICE
    menu:
        thought "Could me and Ciaran ever be a thing?"
        "Yes! We could totally be a thing":
            $ s3_like_ciaran = True
            $ s3_mc.like("Ciaran")
            $ s3e5p2_confess_attraction_ciaran = True
            s3_mc "Totally."
            ciaran "Aw, that's proper grand."
            "He looks like he's leaning in for a hug but he stops himself."
        "No, it's [s3_mc.current_partner] for me":
            ciaran "Fair play."
            ciaran "At least you're honest."
            ciaran "I guess."
            "He sighs, looking genuinely disappointed."
        "Nah, no one says fella these days":
            ciaran "Fair play."
            ciaran "At least you're honest."
            ciaran "I guess."
            "He sighs, looking genuinely disappointed."

    ciaran "I'll be seeing you later then, [s3_name]."
    "As Ciaran walks off he turns back briefly, catching one last glimpse of you before he goes."

    $ leaving("ciaran")

    return

label s3e5p2_tai_date:
    $ on_screen = []
    "Tai comes over through the clearing in the woods. He takes a deep indulgent breath of fresh air."
    tai "Ah, now this is the life I signed up for."
    "He turns to face you and bounds down to the picnic rug."
    tai "Hey, [s3_name]."
    s3_mc "Hey Tai."
    "He opens his arms."
    tai "Fancy a hug?"

    # CHOICE
    menu:
        thought "I should..."
        "Remain seated on the rug":
            # NEED TO FILL
            "EMPTY"
        "Hug him":
            "You get up and hug him. He envelops you in his arms and squeezes you tight, almost lifting you off the ground."
        "Try and pick him up":
            "You try and pick him up."
            "He remains firmly on the ground."
            tai "Ha! Never had a girl do that before on a date."
            s3_mc "I'm just sizing you up."
            tai " Why?"
            s3_mc "You never know."
            "Tai looks at you quizzically. You both sit back down on the rug."

    if s3e5p2_jump_in_water:
        tai "You're a bit damp!"
        s3_mc "Sorry about that. I went swimming with Yasmin!"
        tai "Nice."
    else:
        tai "Bet you're knackered after all these dates."
        if s3_mc.bisexual:
            tai "I heard you've had all three of us falling for you!"

    tai "They always say that you should save the best till last, you know?"
    s3_mc "Oh, yeah?"
    "He grins cheekily."

    # CHOICE
    menu:
        thought "Tai thinks he's the best..."
        "You are pretty cool":
            $ s3_mc.like("Tai")
            "He pretends to do a hair toss."
            tai "Thanks."
            tai "I try."
        "Nah, I'm the best":
            tai "I mean, I only go for the best..."
            tai "And I picked you to date."
            tai "So, you must be pretty good."
        "[s3_mc.current_partner] is the best":
            "Tai makes a fake vomit noise."
            s3_mc "Hey!"
            tai "I joke, I joke. You're a cute pair."

    s3_mc "Oh, really?"
    tai "Yeah, everyone thinks they are the best person, or, like, the hero in their own story."
    s3_mc "Could you be the bad guy?"
    tai "No, honestly. I don't have a bad bone in my body..."

    # CHOICE
    menu:
        thought "Tai doesn't have a bad bone in his body!"
        "Me neither, I'm a sweetie":
            $ s3_mc.like("Tai")
            tai "Aw, I bet you are!"
        "I have one bad bone":
            $ s3_mc.like("Tai")
            tai "Really?"
            s3_mc "Yeah, right here."
            "You point to the end of your pinky."
            tai "You've got a naughty pinky?"
            "Tai bursts into laughter. You wiggle your pinky at him."
            tai "You've definitely got more funny bones than bad ones."
        "All of my bones are bad":
            tai "All of them?"
            s3_mc "Yeah. You better watch out."
            tai "I'm going to find the good bones in you, [s3_name]. You just wait."
            s3_mc "I'll be waiting in my grave."
            tai "You're funny. I'll give you that."

    "He sits back for a few moments. You sit and listen to the cascading roar of the thunderous waterfall."
    tai "I used to think waterfalls were communal showers for giants."
    tai "I thought about giants a lot as a kid."
    s3_mc "How come?"
    tai "Everyone used to call me 'big boned' or 'the Big Friendly Giant'."
    tai "It got me kinda down, actually."

    # CHOICE
    menu:
        thought "Tai got called big boned as a kid!"
        "I don't like talking about weight":
            tai "That's fair enough. We don't have to."
        "That's not very nice":
            tai "That's the thing, I don't think anyone really meant it in a mean way. I was always well-liked in school."
            tai "But it used to play on my mind."
            s3_mc "One tiny comment from someone about something like weight can lead to a whole bundle of insecurities."
            tai "Yeah, you're so right."
            tai "I've grown to love my size. I know I'm a big guy. And I'm happy with the space I have in the world."
            tai "And everyone used to say I give really good hugs."
            tai "Which is never a bad skill to have."
            tai "I've grown to love my size. I know I'm a big guy. And I'm happy with the space I have in the world."
            tai "And everyone used to say I give really good hugs."
            tai "Which is never a bad skill to have."
        "That means you give good hugs":
            tai "I do."
            tai "Want a hug now?"
            # SUB-CHOICE
            menu:
                thought "Do I want a hug?"
                "Yeah, give me your best hug":
                    $ s3_mc.like("Tai")
                    "He wraps his arms around you."
                    "His warm embrace instantly makes you feel safe."
                    s3_mc "Ten out of ten would hug again."
                    tai "Thanks. I try."
                "Nah, I'm OK":
                    tai "That's OK."
            tai "I've grown to love my size. I know I'm a big guy. And I'm happy with the space I have in the world."
            tai "And everyone used to say I give really good hugs."
            tai "Which is never a bad skill to have."

    tai "That's how I got into playing rugby and making pottery."
    s3_mc "Pottery and rugby?"
    tai "Yeah, weird mix, right?"
    tai "I wanted to prove to people that being bigger didn't mean I was like a bull in a china shop."
    tai "On the field I am, but in the workshop I'm careful."
    tai "It also means I'm good with my hands."

    # CHOICE
    menu:
        thought "Tai is good with his hands..."
        "I prefer feet":
            # NEED TO FILL
            "EMPTY"
        "I'd love to see some of your pots!":
            tai "Maybe one day you can."
            if s3e5p1_rummage_suitcases:
                s3_mc "Yeah, one that's not broken next time."
                tai "For sure."
        "You can put that to practise with me any day":
            tai "I'm sure we will."

    if s3e5p1_rummage_suitcases:
        s3_mc "So, that's why I found some pieces of pottery in your bag?"
        tai "Yeah. It's from the first ever pot I made."
        tai "The pot broke and my dad kept all the little bits because he wanted to put it back together again."
        tai "Then a bit fell in my bag one day when I was going to a new school."
        s3_mc "Right..."
        tai "It became this whole thing that whenever I was doing something new and I was a little nervous he'd slip one of the pieces into my bag."
        s3_mc "Sort of as a little confident boost?"
        tai "Yeah, and also as a reminder that it's okay to fail at first."

        # CHOICE
        menu:
            thought "Tai's dad puts pieces of pottery in his bag!"
            "I can't believe you make pottery!":
                # NEED TO FILL
                "EMPTY"
            "That's so lovely":
                $ s3_mc.like("Tai")
                tai "Yeah, he's great."
            "Isn't it sharp?":
                tai "No, my dad usually sands off the sharp edges."

        tai "Usually my dad is a bit of a prankster. But this was proper cute."
        tai "I carried a bit in my bag when I first moved to London."
        tai "My first big rugby game I had a piece stuck in my pants the whole time and I didn't even realise!"
        s3_mc "Ouch."
        tai "But, yeah."
        tai "That's why it was in there."
        tai "I'm really glad you found it. We wouldn't have had this chance to open up otherwise."

    if s3_mc.current_partner == "AJ":
        s3_mc "So..."
        aj "How was your date with AJ?"
        tai "It was nice!"
        tai "She's a real cutie, I can see why you like her."
        tai "She definitely has caught all the feels for you though."
        s3_mc "Good!"

    "He gestures to the waterfall."
    tai "This spot is totally lush, isn't it?"
    tai "Reminds me of something that happened when I was still living back home in New Zealand."
    tai "I set up a picnic behind a waterfall to impress some guy."
    tai "But it turned out he couldn't swim."
    tai "He got so funny about it! Kept saying how I should have known."
    tai "Like I'm some kind of swimming ability mind reader."

    # CHOICE
    menu:
        thought "Tai's date..."
        "Was a guy?":
            tai "Yeah, I've dated a few guys."
            s3_mc "So you're bi?"
            tai "Yep! Out and proud."
            tai "But yeah, this one guy - I got a really good vibe off him. He was good fun."
            tai "But he was also a massive drama."
        "Sounds like drama":
            tai "He was."
            tai "The water wasn't even deep."
        "Should have been me":
            $ s3_mc.like("Tai")
            tai "Well, now it is."

    tai "The water wasn't even deep."
    tai "It was such a waste of a good date idea."
    tai "I like a person who is up for trying new things, you know?"

    # CHOICE
    menu:
        thought "Tai likes someone who tries new things..."
        "I'm super spontaneous!":
            tai "Oh, yeah?"
            tai "In that case..."
        "Did you do it behind the waterfall?":
            tai "No, we never even made it to the waterfall."
            s3_mc "That's a shame."
        "I live in my comfort zone":
            tai "It's never too late to start trying new things."

    tai "Why don't we go and explore behind the waterfall right now?"
    tai "No one would see us behind there."
    "He winks at you."
    tai "You up for it?"

    # CHOICE
    menu:
        thought "Should me and Tai go behind the waterfall?"
        "Yeah, let's be adventurous!":
            tai "Sweet."
            $ s3e5p2_behind_waterfall = True
            call s3e5p2_behind_waterfall from _call_s3e5p2_behind_waterfall
        "Nah, you already did that on another date":
            tai "We never made it back there because he couldn't swim."
            "He smiles."
            tai "But that's OK. It's no biggie. Just an idea."
            tai "Ah! That's my phone."

    "Tai checks his phone."
    tai "Oh, it's not my phone..."
    s3_mc "It's mine!"
    text "Girls, you are all invited on a girlie sleepover in the hideaway. #girslnightin #constantcraving"
    tai "Oh, jealous!"

    # CHOICE
    menu:
        thought "A sleepover with all the girls sounds like..."
        "A good chance to flirt with some of the girls" if s3_mc.bisexual:
            "Tai winks at you."
            tai "I like where your head's at."
        "Boredom served cold, I'd rather be cracking on":
            "Tai winks at you."
            tai "I like where your head's at."
        "A lot of fun":
            tai "Yeah! I always love a good sleepover."
        "Inevitable drama":
            tai "Nah,, I'm sure it'll be chill. You've got a good group of girls here. No real drama stirrers."

    s3_mc "Maybe you should organise one for the boys."
    tai "Maybe I will."
    "Tai smiles at you as you start to walk back from the waterfall together."
    tai "Listen, before we go back there's something I wanted to ask you."
    tai "I know this has been sort of brief, but I think you're awesome, and I really like you."
    tai "I would totally be down for cracking on with you, if you want me to."
    tai "If you couldn't already tell."
    s3_mc "I had my suspicions."
    tai "I just wanted to check whether you felt the same way."
    tai "If you don't, I'll hold off."

    # CHOICE
    menu:
        thought "Do I like Tai?"
        "Yes!":
            $ s3_mc.like("Tai")
            $ s3_like_tai = True
            $ s3e5p2_confess_attraction_tai = True
            "He grins."
            tai "Good to know."
        "No, [s3_mc.current_partner] is the one for me":
            tai "Fair enough, [s3_name]. I understand."
            tai "Honestly, I'd rather know now then later on when I've already fallen too hard on my feelings."
            tai "I'll still be around if you change your mind."
        "Sorry but you're not my type":
            tai "Fair enough, [s3_name]. I understand."
            tai "Honestly, I'd rather know now then later on when I've already fallen too hard on my feelings."
            tai "I'll still be around if you change your mind."

    tai "Let's head back so you can get ready for your sleepover!"
    "You and Tai head back to the Villa."

    scene sand with dissolve
    $ on_screen = []

    "I need a tissue."
    "And some food."
    "I'm getting peckish here."
    "Can someone pack up that picnic that [s3_name] and her dates completely ignored?"
    "And if you could send it Mx. Narrator, Shed, Somewhere Behind the Villa, that would be great."
    "Just knock on the door and say you're going to blow my house down by the hairs of my chinny chin chin when you arrive."
    "I'll know what you mean."
    "Coming up while I wait for my delivery to arrive..."
    "[s3_name] and the girls have a sleepover!"
    miki "Did someone say...marshmallows?"
    "And things might get bubbly..."
    yasmin "Shall we go outside alone?"

    jump s3e5p3

label s3e5p2_behind_waterfall:
    $ s3_mc.like("Tai")
    "He holds out his hands and you start to wade over."
    "You approach the thunderous waterfall. The spray hits your face as you pass through into the cave."
    tai "Close your eyes! I'll lead us in."
    $ leaving("tai")
    "Don't worry folks."
    "We've done a very thorough health and safety check."
    "This waterfall is structurally sound enough for [s3_name] and Tai to roll about behind."
    "Um, I mean explore behind."
    "You and Tai push forward through the strong current of the waterfall's flow."

    scene s3-behind-waterfall with dissolve
    $ new_scene()

    "In seconds, you're behind the cascading wall of water."
    tai "We did it!"
    "Behind the waterfall is a small cave."
    tai "Watch your step."
    "You both sit and watch the water as it tumbles down."
    tai "Kinda magical here."
    # CHOICE
    menu:
        s3_mc "It is..."
        "Magical":
            pass
        "Romantic":
            pass
        "Damp":
            pass

    s3_mc "It really is."
    tai "It's a great place to escape for a while."
    "Tai shifts closer to you. Even though you're not quite touching, you can feel the warmth of his arm along yours."
    "When he speaks, his voice is soft and low."
    tai "I love the way you sound, [s3_name]."
    tai "Would you say something for me?"
    s3_mc "Like what?"
    tai "Anything you like."

    # CHOICE
    menu:
        thought "Tai wants me to say something because he likes my voice. I should say something..."
        "Serious":
            # NEED TO FILL
            "EMPTY"
        "Silly":
            s3_mc "She sells sea-shells on the sea shore?"
            tai "Now faster!"
            s3_mc "She-sells-sea-shells-on-the-sea-shore"
            tai "You are one skilled lady."
            s3_mc "Thank you."
        "Flirty":
            $ s3_mc.like("Tai")
            s3_mc "You're so fine, how could I say no?"
            "Tai does a dramatic shiver."
            tai "Ooh, you're giving me chills!"

    tai "The first time I heard your voice, I was in the kitchen. The telly wasn't even on very loud."
    "His dark eyes crinkle deeply as he smiles."
    tai "I had to stop washing up and turn up the volume."
    thought "It feels like such a long time ago."
    "As he draws nearer, his breath lightly tickles your cheek."

    # CHOICE
    menu:
        thought "Tai's so close!"
        "Kiss his cheek":
            "You lean close, and brush Tai's cheek lightly with a kiss."
            "His hair smells of something flowery, along with the rich scent of sandalwood."
            "His skin is soft, and you feel his cheek dimple with his smile before you draw back."
            "He bites his lips, and his gaze lingers on your mouth."
        "Kiss him on the mouth":
            "You lean close. Tai's hair smells of something flowery, along with the rich scent of sandalwood."
            "He kisses you back gently at first, and his soft lips curve in a smile."
            "As the kiss deepens, he groans in the back of his throat and draws you closer."
            "He strokes your arm, and your skin tingles all the way down."
            "When he draws back, he bites his lips and his gaze lingers on your mouth."
        "Give him a hug":
            "You wrap your arms around him, feeling just how solid he is."
            "He sighs happily, and his back muscles flex as he holds you close."
            "His hair smells of something flowery, along with the rich scent of sandalwood."
            "When he eventually draws back, he bites his lips, and his gaze lingers on your mouth."
        "Draw away":
            "As you draw back, Tai's eyes sparkle, and he gives you a broad smile."

    tai "You're pure flames, [s3_name]."
    "He pretends to fan himself."
    tai "And I could listen to your voice all day."

    # CHOICE
    menu:
        thought "Tai's really into how I sound..."
        "You have a sexy voice too":
            $ s3_mc.like("Tai")
            tai "When I talk to my friends back home, they tell me I've turned Brit."
            tai "So I tell them they sound like sheep farmers."
            tai "Course, as soon as I talk to them, I start sounding like that too!"
            "He laughs, and brushes a stray lock of hair back from his face."
        "I never thought of my voice like that":
            tai "Oh, it's like that for sure."
        "No matter what I say?":
            tai "Your voice is awesome."

    s3_mc "What if I said something unsexy? Like..."
    s3_mc "Mulch."
    tai "Even that. Still hot."
    s3_mc "That sounds like a challenge."

    # CHOICE
    menu: 
        thought "Should I try and creep Tai out with my voice?"
        "Let's keep it flirty":
            $ s3_mc.like("Tai")
            "You lean in towards Tai, your lips almost touching his ears. He shivers."
            tai "That's hot all by itself."
            # SUB-CHOICE
            menu:
                thought "I wonder what I should do now..."
                "Make a whispering noise":
                    # NEED TO FILL
                    "EMPTY"
                "Lick his ear":
                    # NEED TO FILL
                    "EMPTY"
                "Tell him what you'd like to do with him":
                    s3_mc "Another day, I could do this while you..."
                    "You carry on whispering against Tai's ear, imagining each act as you speak."
                    "Tai's breath catches, and he reaches to touch your lips when you pause."
                    tai "Oh, that sounds amazing."
                    tai "I hope I get to experience it soon."
        "Heck yes, it'll be funny":
            "You lean in towards Tai, your lips almost touching his ears. He shivers."
            tai "That's hot all by itself."
            thought "This is the perfect moment."
            # SUB-CHOICE
            menu:
                thought "What shall I do to creep Tai out?"
                "Say unsexy words":
                    "You sigh against Tai's ear, and his breath hitches."
                    s3_mc "Dental floss."
                    tai "Huh?"
                    "You give a breathy gasp."
                    s3_mc "Clammy."
                    tai "Oh, no."
                    s3_mc "Moist."
                "Screech in his ear":
                    "You sigh against Tai's ear, and his breath hitches."
                    s3_mc "You know what I think you'd like to hear?"
                    tai "Oh, I'm desperate to know."
                    "You give a breathy gasp. Tai groans a little in the back of his throat."
                    "Then you shriek like a banshee."
                "Tell a gross story":
                    "You sigh against Tai's ear, and his breath hitches."
                    s3_mc "This one time I came home after a holiday..."
                    tai "Huh?"
                    "You give a breathy gasp."
                    s3_mc "And my flatmates hadn't washed up for two weeks."
                    tai "Oh, no."
                    s3_mc "There was crusty porridge everywhere."
                    s3_mc "And dental floss floating in a frying pan."
            tai "Aaah!"
            "He pulls away, rubbing his ear and laughing."
            tai "Well played, babe. I knew we'd make a good pair."

    tai "Waterfalls are cool because they are sort of always travelling backwards."

    # CHOICE
    menu:
        thought "Tai says waterfalls travel backwards..."
        "Yeah, you're right":
            s3_mc "It's because the falling water erodes the rock that the waterfall slowly recedes upstream, right?"
            tai "Yes! Upstream, that's the word I was looking for."
        "That's totally wrong":
            tai "It's not!"
            tai "It's something about how the water from a waterfall rubs the rocks up there and eventually they'll fall away and make the waterfall move backwards."
        "I have no idea what you're on about":
            tai "It's something about how the water from a waterfall rubs the rocks up there and eventually they'll fall away and make the waterfall move backwards."

    tai "In a few years time this little cave will get bigger or be completely open because the waterfall would have moved backwards!"
    tai "I used to feel like I was never really moving forward, a bit like a waterfall."
    tai "But I've got to say, being in here with you right now has totally changed that."
    "Tai smiles and looks at you with mischievous eyes."
    thought "This could be a good private place to have some sexy alone time..."

    # CHOICE
    menu:
        thought "Do I want to do bits behind the waterfall?"
        "No, I'm staying faithful to [s3_mc.current_partner]":
            thought "I don't need to do that."
            thought "I'm happy just listening to the waterfall."
        "Nah, I don't feel like it":
            thought "I don't need to do that."
            thought "I'm happy just listening to the waterfall."
        "Bits behind the waterfall sounds like fun":
            $ s3_mc.like("Tai")
            $ s3_mc.like("Tai")
            $ s3e5p2_waterfall_bits = True
            "You smile at him with equally mischievous eyes."
            s3_mc "No pressure, but if you want to do it, I'm up for it."
            "You take out a condom out of your back pocket and wiggle it at him."
            tai "Ha, nice!"
            tai "You came prepared."

            if s3e1p1_grab_some_condoms:
                s3_mc "I got some on the first, didn't know when they would come in handy."

            "Tai grins at you as you move closer towards him."
            tai "You don't have to ask me twice."
            "He lies on the floor. You get on top of him and kiss his neck."
            tai "Wow."
            "As you nibble his ear lobe he slides his hand under your top then hesitates."
            tai "Is this ok? Can I..."
            "You whisper into his ear."
            s3_mc "Absolutely!"
            "He slowly unhooks clasps and buttons."
            "Your clothes slip off and are quickly discarded to the side of the cave."
            tai "You're beautiful."
            s3_mc "You're not so bad yourself."
            "He pulls you closer to him. You start to move your hips against his."
            "The spray of the waterfall tickles your bare skin as you explore each other's bodies."
            "You both moan. It echoes around the small cave."
            "You lie next to each other, entangled in each other's arms, staring at the cave's ceiling."
            "You're a little damp and breathing heavily."
            s3_mc "Wow."
            tai "Doing it behind a waterfall."
            "He gestures, making a tick in the air."
            tai "Check."
            s3_mc "If that doesn't put us in the Do-Bits-Society I don't know what will."
            tai "Absolutely."
            tai "Though for the sake of [s3_mc.current_partner], let's keep it on the down low."
            tai "I don't want to be rubbing in anyone's face how amazing that was."
            tai "Especially being one of the new boys on the block."
            s3_mc "Yeah, that's fair."

    "He smiles at you."
    tai "So beautiful..."
    s3_mc "The waterfall?"
    tai "No, you."
    tai "Damn."
    tai "Come on, let's head back before people wonder where we are..."
    "You both make your way out of the roaring waterfall. Tai holds your hand."

    scene s3-waterfall-date with dissolve
    $ new_scene()

    "You use the picnic blanket to dry off."

    return

#########################################################################
## Episode 5, Part 3
#########################################################################
label s3e5p3:
    scene sand with dissolve
    $ on_screen = []

    show screen day_title(5, 3) with Pause(4)
    hide screen day_title with dissolve

    "Welcome back to Love Island!"
    "Last time, [s3_name] lost herself on two romantic dates in a park."
    "Reminds me of a time I got lost at a campsite."
    "Hard to find my way back by following a trail of crisps someone had dropped."
    "Not quite the fairytale experience I was expecting."
    "Anyway, it looks like [s3_name] was spoiled for choice..."
    if s3_mc.bisexual:
        yasmin "Because, like I said, I'm really into you, so if you feel the same way that would be super cool to know."
    ciaran "But could you see yourself with a fella like me?"
    tai "You up for it?"

    $ leaving("ciaran")
    $ leaving("tai")  

    "But now..."
    "Sleepover!"

    ## ADD back once MC images are in game
    scene s3-dressing-room with dissolve
    $ new_scene()
    thought "It's sleepover time. I gotta decide what to wear."
    thought "It's only a girls' sleepover, but I still want them to see me looking fierce."
    # Outfit change to sleepwear

    $ outfit = "pjs"
    call customize_outfit from _call_customize_outfit_11

    thought "Got it. This is perfect."
    thought "Then again, it's just a chill night. No need to go overboard."

    scene s3-kitchen-night with dissolve
    $ new_scene()
    $ extra = "lamb"

    "All the girls are gathered in the kitchen, making hot chocolate for the sleepover."

    ## ADD back once MC images are in game
    # miki "[s3_name], your looks are literally hashtag-goals. I need to steal you for my insta some time. "
    # miki "Going for understated, [s3_name]? Same, to be honest. I love that we don't have to dress up for the boys tonight."

    miki "I'm so hyped for this. It's so nice of them to give us some time in the hideaway, just us girls."
    elladine "Yup, it's gonna be really great."
    elladine "I've been missing my girlies from back home."
    elladine "It'll be lovely to have a proper natter."
    "Miki starts singing a song while stirring the milk in the pan."
    miki "Everybody's lookin' forward to the girl talk, girl talk!"
    miki "It's nice just to hang out with you gal pals sometimes!"

    if s3_mc.bisexual:
        if s3_like_yasmin == False:
            "AJ waggles her eyebrows at you from across the room and flashes you a tiny, impish smile."
            # CHOICE
            menu:
                thought "How should I react to AJ"
                "Wink at her":
                    # NEED TO FILL
                    "EMPTY"
                "Pull a face":
                    "You pull a funny face and AJ giggles."
                "Blow her a kiss":
                    $ s3_mc.like("AJ")
                    "You blow her a kiss. She mimines catching it, then opens her hand and kisses her palm."
                    "Yasmin notices you flirting with AJ."
                    yasmin "Looks like these gals are already palling it up nicely."
                    aj "What do you mean?"
                    yasmin "I just think you guys are cute together, that's all."
        elif s3_like_yasmin and s3_mc.current_partner == "AJ":
            "Yasmin catches your eye."
            "She parts her mouth, and runs the tip of her tongue slowly along her top lip."
            # CHOICE
            menu:
                thought "Yasmin's flirting with! How should I react?"
                "Cross your eyes":
                    "You cross your eyes and let your tongue loll out of your mouth."
                    "A smile spreads across Yasmin's face and she snorts with laughter."
                    "AJ turns to see what the laughter is about. She giggles when she sees you."
                "Lick your lips too":
                    $ s3_mc.like("Yasmin")
                    "You follow suit, seductively tracing your lips with your tongue. You can hear Yasmin's breath catch a little."
                    "AJ sees and grins."
                    aj "Are you using that cherry chapstick? I'm always licking it off too."
                    s3_mc "Er, yeah. It's delicious."
                "Blow her a kiss":
                    $ s3_mc.like("Yasmin")
                    "You send a kiss across the room to Yasmin. She puckers up her lips and blows one back."
                    "AJ sees, and raises her eyebrows."

    "Genevieve's been hunting in the cupboards, and straightens triumphantly."

    if s3e4p3_supper == "Marshmallows" or (s3e4p2_decorate_tent == False and s3e4p2_good_tent == False):
        genevieve "We've still got marshmallows!"
        genevieve "I thought we'd used them all when we camped out."
    else:
        genevieve "Marshmallows!"
        miki "Yes girl!"
        miki "It isn't hot chocolate without some marshmallows."

    # CHOICE
    menu:
        thought "Marshmallows in hot chocolate?"
        "All the way, babe":
            $ s3_mc.like("Genevieve")
            "Genevieve points at you."
            genevieve "Knew I liked you."
        "No! It's a drink!":
            s3_mc "Toasted on a campfire? Yes."
            s3_mc "Floating in my hot chocolate. No thanks."
            "Iona gives you a thumbs-up."
            iona "I'm with [s3_name]."
        "I prefer a dash of chilli":
            $ s3_mc.like("Iona")
            iona "I do that too!"
            iona "I knew I liked you, [s3_name]."

    miki "OK, chocolate's nearly done!"
    yasmin "Great!"
    "You noticed that Yasmin's carrying a stuffed toy. It's faded purple and a bit shapeless. It doesn't look like any animal you recognise."

    # and zooming shot of lamb studffed animal
    # hide window
    # show screen s3_character_profile("lamb") with pause 4
    # hide screen s3_character_profile
    # (picture of Yasmin's toy): New Islander...?

    # CHOICE
    menu:
        thought "Is that a..."
        "Shaved bear?":
            yasmin "A shaved bear would look so wrong..."
            iona "Babe, there's nothing right about whatever that is."
        "Naked tortoise?":
            yasmin "A naked tortoise?"
            s3_mc "Yeah, you know, one without a shell."
            yasmin "Oh, I get it!"
        "Frog-manatee?":
            yasmin "Is that a real thing?"
            s3_mc "No, I just made it up."
            yasmin "I like it. Maybe that's what she is."

    yasmin "I think she was meant to be a lamb. My mum made her for me."
    iona "Has... has your mum ever seen a sheep?"
    yasmin "I haven't seen her do any crafting since."
    elladine "What's her name?"
    yasmin "...Yasmin."
    yasmin "I didn't know many names when I was three, alright?"

    # CHOICE
    menu:
        thought "Yasmin sleeps with a stuffed toy..."
        "I think it's adorable ":
            $ s3_mc.like("Yasmin")
            "She smiles."
            yasmin "It's not weird, then?"
            s3_mc "Not at all."
        "Now I'm jealous...":
            s3_mc "Wish I had a cuddle toy."
            "Yasmin laughs."
            yasmin "I might be convinced to share her."
            genevieve "Can you share her with me too?"
            yasmin "Wow, I'm glad I brought her now."
        "I don't know anyone else who does that":
            $ s3_mc.dislike("Yasmin")
            yasmin "Oh no, is it weird?"
            s3_mc "Not weird, but maybe a bit unusual!"
            s3_mc "I guess everyone's got their 'thing', haven't they?"
            yasmin "Yeah."

    "Miki serves the hot chocolate, and you make your way to the hideaway."
    iona "I have no idea how we're all gonna fit..."

    if s3_mc.current_partner == "AJ":
        "The girls head over to the hideaway but AJ holds back."
        aj "Hey..."
        "You turn and see AJ smiling nervously."
        aj "You've not said anything about the dates."

        # CHOICE
        menu:
            thought "AJ wants to know how the dates went..."
            "Um, er, yeah...":
                # NEED TO FILL
                "EMPTY"
            "I'd much rather have been on a date with you":
                $ s3_mc.like("AJ")
                aj "You're just saying that."
                s3_mc "No I'm not."
                s3_mc "I mean they were alright."
                s3_mc "But I was thinking about you the whole time."
                "You take AJ's hand. She grins and squeezes your hand back."
            "They were so much fun":
                aj "Oh. Great..."
                aj "So you liked all of them?"
                s3_mc "Yes! They were all so interesting."
                s3_mc "I think you'll really get on with Yasmin."
                aj "Like like or just... people like?"
                s3_mc "It's a bit early to say."
                aj "Yeah, of course..."

        elladine "Are you two slow coaches coming or what?"
        s3_mc "We'd better make a move"
        "You and AJ catch up with the others."

    scene s3-hideaway-night with dissolve
    $ new_scene()

    genevieve "Wow, look at this!"
    "The hideaway has been transformed into a snug den, with mattresses all over the floor and fairy lights on the walls."
    miki "Woo!"
    "Miki runs into the room and flops onto the mattresses. Elladine and AJ join her."
    iona "Right, ladies, what's the plan?"
    iona "I say we..."
    iona "Oof!"
    "A pillow hits her on the side of the head with a whumph."
    "Miki is standing there looking guilty."
    miki "Oh my gosh, did I hurt you?"
    "Iona grabs a pillow and swings for Miki."
    "She ducks, and Genevieve takes the hit."
    genevieve "I'll get you for that!"
    "Everyone scrambles to get a pillow."
    "Feathers begin to fly."

    # CHOICE
    menu:
        thought "What should I do?"
        "Ally with AJ":
            $ s3_mc.like("AJ")
            s3_mc "AJ! I've got your back!"
            "You combat roll across the mattresses and jump to your feet next to her."
            aj "That was so cool!"
        "Ally with Yasmin":
            $ s3_mc.like("Yasmin")
            s3_mc "Yasmin! Let's do this!"
            "You stand back to back like action heroes, brandishing your pillows."
            yasmin "Hey."
            s3_mc "Hi."
        "Be a lone wolf":
            "You grab a pillow and join the fray."
            s3_mc "It's every woman for herself!"
            "You start thwacking anyone in range with your pillow."
        "Ally with Genevieve" if s3_mc.bff == 'Genevieve':
            $ s3_mc.like("Genevieve")
            s3_mc "Genevieve! I've got your back!"
            "You stand back to back like action heroes, brandishing your pillows."
            genevieve "Let's do this, [s3_name]!"
        "Ally with Elladine" if s3_mc.bff == 'Elladine':
            $ s3_mc.like("Elladine")
            s3_mc "Elladine! I've got your back!"
            "You stand back to back like action heroes, brandishing your pillows."
            elladine "Let's do this, [s3_name]!"

    "The pillow fight rages on."
    "Miki and Iona form a brief alliance that's shattered when Iona launches a surprise tickle attack on Miki."

    if s3_mc.current_partner != "Camilo":
        "Iona busts out some of Camilo's jiu jitsu moves on you, but you manage to wriggle free."
        s3_mc "You need to practise more!"
        iona "Then come back here and let me!"
    else:
        "You manage to bust out some jiu jitsu moves that Camilo taught you."
        elladine "How are you so good already?"
        s3_mc "I'm a quick learner!"

    "Eventually, the pillow fight dissolves into giggles as everyone flops down onto the mattresses."
    elladine "Phew, that was a workout."
    iona "That's the mandatory pillow fight out of the way."
    iona "Well done, everyone."
    "Everyone settles in. People arrange pillows and pull blankets over themselves."
    genevieve "What were you gonna suggest, Iona?"
    genevieve "You were about to say something before it all kicked off."
    iona "Oh, yeah. We should play Snog, Marry, Pie!"
    genevieve "Isn't that kind of what we do all day anyway?"
    iona "I don't think so."
    iona "It's a classic sleepover activity!"
    iona "We've done the pillow fight. Now we should talk about who we're crushing on."
    iona "Everyone knows how the game works?"
    "Miki raises her hand."
    miki "I might need a refresher."
    iona "Basically, we go around and all say which of the boys we'd snog, who we'd marry..."
    iona "...and who we'd smush a big cream pie into the face of right now..."
    miki "Seb!"

    # CHOICE
    menu:
        thought "No hesitation from Miki there..."
        "Aw, no way Seb deserves that":
            thought "What's she got against Seb? He's lovely."
            thought "Glad I didn't suggest Seb crack on with Miki..."
        "Seb would get a pie for sure":
            thought "He'd deserve it, too."
        "I love Seb, but I don't blame her":
            thought "He does have a very pie-able face."

    iona "I guess we'll start with Miki, then."
    miki "OK, let's see."
    miki "I'd definitely snog Harry. He's just so handsome."

    if s3_mc.current_partner != "Harry":
        thought "Uh-oh. Watch out, Genevieve."
    else:
        "Miki looks at you guiltily."

        # CHOICE
        menu:
            thought "Miki would snog Harry..."
            "She better back the hell off":
                # NEED TO FILL
                "EMPTY"
            "I don't blame you":
                "You smile at her."
                s3_mc "He's super cute."
            "At least she didn't pick him to marry":
                s3_mc "Snogging is fine, but don't get any ideas about marrying him!"
                miki "Got it!"

    miki "And... like I already said, I'd pie Seb."
    s3_mc "Bad enough that you skipped over 'marry'."
    miki "Yeah. I really need to get this off my chest."
    miki "He's just so... you know..."
    s3_mc "What?"
    miki "...Miserable. He's always complaining."
    aj "He's not exactly a ray of sunshine. But he can be thoughtful sometimes."
    genevieve "He's a grumpy Gus. But that probably means he's got a good heart."
    genevieve "And I think my pie goes to Camilo."
    genevieve "That boy is too handsome for his own good!"

    # CHOICE
    menu:
        thought "Viv would pie Camilo for being handsome..."
        "Same, girl":
            if s3_mc.current_partner == "Camilo":
                s3_mc "And maybe I'll lick the cream off his face afterwards."
                "Genevieve laughs."
            else:
                iona "Pie him all you like, lads, he's not getting any less fit."
                genevieve "Unfortunately, I think you're right."
        "That's a silly reason":
            genevieve "I'm allowed to choose whatever reason I want!"
            s3_mc "I guess so. But pie isn't gonna make him any less fit."
            genevieve "Unfortunately, I think you're right."
        "Camilo would get more than a pie from me":
            iona "Oh he would, would he?"
            if s3_mc.current_partner != "Camilo":
                iona "We'll see about that."

    iona "I'm more interested in [s3_name]'s choices."
    "The girls all turn and look at you expectantly."

    # CHOICE
    menu:
        thought "I'd snog..."
        "Bill":
            $ s3e5p3_snog = "Bill"
            s3_mc "Because Bill is mega fit."
            if s3_mc.current_partner != "Bill":
                "There is silence and the girls exchange looks."
                miki "Well, babe, at least no one can fault your honesty."
                s3_mc "I mean...it's just a game, right?"
                miki "Yeah! Don't worry, I'm just teasing you."
                "You throw a pillow at Miki, who giggles at you. The other girls laugh along."
                miki "What about Girl Code?"
                s3_mc "But... we were all..."
                miki "Gotcha! Only teasing."
                "The girls laugh and you throw a pillow at Miki."
                if s3_mc.current_partner == "AJ":
                    "AJ glances at you nervously."
                    s3_mc "I mean it's just a game..."
                    "AJ smiles."
                    aj "I know. No biggie."
            else:
                miki "Aw, that's cute."
                iona "Aye, and a wee bit boring."
                "The girls laugh."
        "Camilo":
            $ s3e5p3_snog = "Camilo"
            s3_mc "Because Camilo is mega fit."
            if s3_mc.current_partner != "Camilo":
                "There is silence and the girls exchange looks."
                miki "Well, babe, at least no one can fault your honesty."
                s3_mc "I mean...it's just a game, right?"
                miki "Yeah! Don't worry, I'm just teasing you."
                "You throw a pillow at Miki, who giggles at you. The other girls laugh along."
                iona "What about Girl Code?"
                s3_mc "But... we were all..."
                iona "Gotcha! Only teasing."
                "The girls laugh and you throw a pillow at Miki."
                if s3_mc.current_partner == "AJ":
                    "AJ glances at you nervously."
                    s3_mc "I mean it's just a game..."
                    "AJ smiles."
                    aj "I know. No biggie."
            else:
                miki "Aw, that's cute."
                iona "Aye, and a wee bit boring."
                "The girls laugh."
        "Harry":
            $ s3e5p3_snog = "Harry"
            s3_mc "Because Harry is mega fit."
            if s3_mc.current_partner != "Harry":
                "There is silence and the girls exchange looks."
                miki "Well, babe, at least no one can fault your honesty."
                s3_mc "I mean...it's just a game, right?"
                miki "Yeah! Don't worry, I'm just teasing you."
                "You throw a pillow at Miki, who giggles at you. The other girls laugh along."
                genevieve "What about Girl Code?"
                s3_mc "But... we were all..."
                genevieve "Gotcha! Only teasing."
                "The girls laugh and you throw a pillow at Miki."
                if s3_mc.current_partner == "AJ":
                    "AJ glances at you nervously."
                    s3_mc "I mean it's just a game..."
                    "AJ smiles."
                    aj "I know. No biggie."
            else:
                miki "Aw, that's cute."
                iona "Aye, and a wee bit boring."
                "The girls laugh."
        "Ciaran":
            $ s3e5p3_snog = "Ciaran"
            s3_mc "Because Ciaran is mega fit."
            "There is a silence and the girls exchange looks."
            miki "Mmm, totally."
            miki "He's a babe."
            if s3_mc.current_partner == "AJ":
                "AJ glances at you nervously."
                s3_mc "I mean it's just a game..."
                "AJ smiles."
                aj "I know. No biggie."
        "Tai":
            $ s3e5p3_snog = "Tai"
            s3_mc "Because Tai is mega fit."
            "There is a silence and the girls exchange looks."
            miki "Mmm, totally."
            miki "He's a babe."
            if s3_mc.current_partner == "AJ":
                "AJ glances at you nervously."
                s3_mc "I mean it's just a game..."
                "AJ smiles."
                aj "I know. No biggie."
        "AJ" if s3_mc.bisexual:
            $ s3e5p3_snog = "Tai"
            s3_mc "Because AJ is mega fit."
            if s3_mc.current_partner != "AJ":
                "There is a silence and the girls exchange looks."
                miki "Well, babe, at least no one can fault your honesty."
                s3_mc "I mean...it's just a game, right?"
                miki "Yeah! Don't worry, I'm just teasing you."
                "You throw a pillow at Miki, who giggles at you. The other girls laugh along."
            else:
                miki "Aw, that's cute."
                iona "Aye, and a wee bit boring."
                "The girls laugh."
        "Yasmin" if s3_mc.bisexual:
            $ s3e5p3_snog = "Yasmin"
            s3_mc "Because Yasmin is mega fit."
            "There is a silence and the girls exchange looks."
            if s3_mc.current_partner != "AJ":
                miki "Well, babe, at least no one can fault your honesty."
                s3_mc "I mean...it's just a game, right?"
                miki "Yeah! Don't worry, I'm just teasing you."
                "You throw a pillow at Miki, who giggles at you. The other girls laugh along."
            else:
                "AJ glances at you nervously."
                s3_mc "I mean it's just a game..."
                "AJ smiles."
                aj "I know. No biggie."

    $ s3_mc.like(s3e5p3_snog)

    if s3_mc.current_partner == "AJ" and s3e5p3_snog != "AJ":
        $ s3_mc.dislike("AJ")

    # CHOICE
    menu:
        thought "As for marry, I'd have to say..."
        "Bill" if s3e5p3_snog != 'Bill':
            $ s3e5p3_marry = "Bill"
        "Camilo" if s3e5p3_snog != 'Camilo':
            $ s3e5p3_marry = "Camilo"
        "Harry" if s3e5p3_snog != 'Harry':
            $ s3e5p3_marry = "Harry"
        "Ciaran" if s3e5p3_snog != 'Ciaran':
            $ s3e5p3_marry = "Ciaran"
        "Tai" if s3e5p3_snog != 'Tai':
            $ s3e5p3_marry = "Tai"
        "AJ" if s3e5p3_snog != 'AJ' and s3_mc.bisexual:
            $ s3e5p3_marry = "AJ"
        "Yasmin" if s3e5p3_snog != 'Yasmin' and s3_mc.bisexual:
            $ s3e5p3_marry = "Yasmin"

    $ pronouns(s3e5p3_marry)

    # CHOICE
    menu:
        thought "Because..."
        "[he_she!c]'s got great chat":
            pass
        "[he_she!c]'s really fit":
            pass
        "I love his philosophies" if s3e5p3_marry == 'Bill':
            pass
        "He can cook" if s3e5p3_marry == 'Camilo':
            pass
        "He's really ambitious" if s3e5p3_marry == 'Harry':
            pass
        "He's got a dog" if s3e5p3_marry == 'Ciaran':
            pass
        "He's really kind" if s3e5p3_marry == 'Tai':
            pass
        "You're full of positive energy" if s3e5p3_marry == 'AJ' and s3_mc.bisexual:
            pass
        "OPTION FOR YASMIN MISSING" if s3e5p3_marry == 'Yasmin' and s3_mc.bisexual:
            pass

    $ s3_mc.like(s3e5p3_marry)

    if s3e5p3_marry == "Bill" or s3e5p3_marry == "Camilo" or s3e5p3_marry == "Harry":
        if s3_mc.current_partner == s3e5p3_marry:
            genevieve "It's so cute that you picked your partner."
            miki "It's cute that you're coupled up with someone you like that much."
        else:
            if s3e5p3_marry == "Bill":
                miki "Yeah, he's a great guy."
                miki "Fit and ?EMPTY?"
                miki "He's a great guy. Er, it doesn't mean anything, though, right?"
                s3_mc "What do you think?"
                miki "I'll pretend you said 'no, of course not!'"
            elif s3e5p3_marry == "Camilo":
                iona "Yeah, he's a great guy."
                iona "Fit and probably does breakfast in bed"
                iona "He's a great guy. Er, it doesn't mean anything, though, right?"
                s3_mc "What do you think?"
                iona "I'll pretend you said 'no, of course not!'"
            else:
                genevieve "Yeah, he's a great guy."
                genevieve "Fit and ?EMPTY?"
                genevieve "He's a great guy. Er, it doesn't mean anything, though, right?"
                s3_mc "What do you think?"
                genevieve "I'll pretend you said 'no, of course not!'"
    elif s3e5p3_marry == "Ciaran":
        elladine "Ciaran's pretty dreamy."
        iona "For sure."
    elif s3e5p3_marry == "Tai":
        aj "Tai's awesome."
        yasmin "Yeah, plus he's beautiful. Even if his farts smell like death."
    elif s3e5p3_marry == "AJ":
        if s3_mc.current_partner == "AJ":
            "You turn to AJ."
            "AJ beams at you."
            aj "I feel the same way."
            yasmin "That's nice..."
            "She bites her lips and looks down."
        else:
            # NEED TO FILL
            "EMPTY - PATH: Chose to marry AJ in game when she isn't your current partner."
    elif s3e5p3_marry == "Yasmin":
        # NEED TO FILL
        "EMPTY - PATH: Chose to marry Yasmin in game."

    # CHOICE
    menu:
        thought "And I'm gonna pie...drumroll...please..."
        "Bill" if s3e5p3_snog != 'Bill' and s3e5p3_marry != 'Bill':
            $ s3e5p3_pie = "Bill"
        "Camilo" if s3e5p3_snog != 'Camilo' and s3e5p3_marry != 'Camilo':
            $ s3e5p3_pie = "Camilo"
        "Harry" if s3e5p3_snog != 'Harry' and s3e5p3_marry != 'Harry':
            $ s3e5p3_pie = "Harry"
        "Ciaran" if s3e5p3_snog != 'Ciaran' and s3e5p3_marry != 'Ciaran':
            $ s3e5p3_pie = "Ciaran"
        "Tai" if s3e5p3_snog != 'Tai' and s3e5p3_marry != 'Tai':
            $ s3e5p3_pie = "Tai"

    # CHOICE
    menu:
        thought "Because..."
        "He's too handsome for his own good":
            genevieve "Hey! You stole my reason!"
            "You shrug."
            s3_mc "It was a good reason!"
        "He's a bit too much sometimes":
            s3_mc "You know? Sometimes I just want a bit of quiet time and it's like, here's [s3e5p3_pie]."
            miki "Totally."
        "I want to lick pie off his face":
            iona "Now I want to pie him too..."
            "There's a dazed silence."
            miki "Is everyone thinking about licking pie off [s3e5p3_pie]?"
            "Heads nod in unison and the girls erupt into giggles."

    s3_mc "Right, Iona, your go."
    iona "I would deffo snog Camilo."

    if s3_mc.current_partner == "Camilo":
        "Iona glances at you."
        # CHOICE
        menu:
            thought "Iona would snog Camilo..."
            "At least she didn't pick him to marry":
                # NEED TO FILL
                "EMPTY"
            "She better back the hell off":
                # NEED TO FILL
                "EMPTY"
            "I don't blame you":
                "You smile at her."
                s3_mc "It's just a game, babes."
                s3_mc "And he is super cute."

    iona "As for who I'd marry, I have to say... Ciaran."

    # CHOICE
    menu:
        thought "Iona would marry Ciaran..."
        "He's really lovely":
            iona "The sweetest."
            iona "I don't know him that very well yet but I can tell we're gonna get on great."
        "He's the most handsome man I've ever seen":
            iona "Tell me about it. Phew."
            "She fans herself."
        "It's a choice, I suppose":
            elladine "Not a fan?"
            "You shrug."
            s3_mc "I'm sure he's nice, but it's just too early for me to know if he's, like, husband material."
            iona "Are you sure you're not overthinking this?"

    iona "Although... on second thoughts, maybe I wouldn't marry him, exactly."
    iona "I'd definitely send him a cheeky nude or two."

    if s3_mc.current_partner != "Camilo":
        elladine "Not Camilo?"
        "Iona waves a hand."
        iona "Him too."
        miki "Would you do that? Send a nude to someone?"
        iona "Yeah."

    # CHOICE
    menu:
        thought "Would I ever send a nude?"
        "I'm not comfortable talking about this":
            $ s3e5p3_nudes = False
            miki "That's fine! This can be a really tricky subject for people."
            iona "Yeah, no need to dwell on it if you're not comfortable. That's totally cool."
            iona "Let's carry on with the game, shall we? Who's next?"
        "Definitely":
            s3_mc "As long as they asked for one."
            iona "Totally. Nothing worse than someone sending you a picture of their bits for no reason."
            s3_mc "That goes both ways. You have to make sure the person actually wants to see that before you send it."
            s3_mc "If I wanted to send a nude to someone and I knew they wanted it, then it's fine! Assuming you also know they're trustworthy."
            iona "I know right! It can be fun, but you have to know you can trust the person."
        "Only to someone I was with":
            s3_mc "I don't know if I'd trust a total stranger with it."
            genevieve "Yeah... I don't think there's anything wrong with sending them, but the trust's gotta be there."
            s3_mc "The other important thing is that you have to make sure the person you're sending it to actually wants to receive it."
            s3_mc "You shouldn't be sending nudes to try and shock or provoke people."
            s3_mc "You should only do it if there's clear consent from the person that they actually want to see that."
        "It's not my thing":
            miki "It's not mine, either. I just don't know if I could trust someone enough with that."
            miki "Like, I don't think there's anything wrong with the idea, as long as you trust the person and there's clear consent."
            miki "It's just not for me. But I think that's basically just a matter of personal taste."
            elladine "I think you're right. You have to make sure the consent is there before you do anything."
            elladine "You shouldn't just assume someone wants to see something like that, and you shouldn't be aiming to shock."
            elladine "And you have to make sure you can trust the person, of course. That's the other really important thing."


    if s3e5p3_nudes:
        iona "When I was in school, I sent a pic to a guy I was seeing, but right away I was like, 'Shit, shouldn't have done that.'"
        iona "I called him and asked him to delete it, and he was great about it."
        iona "You don't want stuff like that getting out where you have no control over it, you know?"
        miki "Plenty of guys have asked me to send them nudes."
        s3_mc "And have you?"
        miki "Nope."
        miki "They can ask but you don't owe them anything."
        iona "Yeah, even if they send you pics."
        miki "And especially if they send you pics you didn't ask for."
        miki "The number of gross DMs I get on the internet from guys who think I'll return the favour is just ridiculous."
        miki "Some days it just seems like my DMs are full of nothing but dicks. It's horrible."
        # CHOICE
        menu:
            thought "Miki gets sent a lot of dick pics..."
            "That's so skeevy":
                genevieve "Yeah, that really sucks, Miki. Sorry you have to deal with that."
                miki "Thanks. It's OK. Well, it's not OK, but you know what I mean."
            "I get loads as well":
                genevieve "That really sucks. I'm so sorry you guys have to deal with that."
                s3_mc "Thanks. It's OK. Well, it's not OK, but you know what I mean."
            "That's actually against the law":
                genevieve "Yeah, especially if they're harassing you."

        yasmin "I had a friend who had been chatting to this really nice guy and one day out of nowhere..."
        yasmin "Bam! He sends a pic of his junk."
        elladine "Why do they do that? What do they think goes through our minds when we see that?"
        iona "That's a fabulous looking willy, let me get my tripod set up and return the favour?"
        s3_mc "So wait, what did your mate do?"
        yasmin "The only thing she could do. Take a pic of her elbow crease and sent it back."
        "The girls burst out laughing."
        yasmin "He loved it. Thought it was cleavage."
        genevieve "Seriously, some people would get turned on by a ham sandwich..."
        iona "Where were we in the game, anyway? Was it someone's turn?"

    aj "Ooh, me! My turn!"
    aj "I'm gonna snog..."
    aj "Yasmin."
    aj "I just think she's really fit."
    "Yasmin blushes."

    if s3_mc.current_partner == "AJ":
        "Yasmin looks at you to see how you're going to react."
        # CHOICE
        menu:
            thought "AJ said she wants to snog Yasmin..."
            "It's a free country":
                "You shrug."
                s3_mc "I'm not the boss of AJ."
                s3_mc "Anyway, it's only a game!"
            "I wish she'd picked me":
                "You make a dramatically sad face at AJ."
                s3_mc "Where's my kiss?"
                aj "Well, I can only pick one person, and I wanted to pick you to, you know, marry..."
                s3_mc "Aw, babe..."
                s3_mc "I get to kiss you for real, anyway."
                aj "Yeah, you do!"
            "I want to snog Yasmin too":
                s3_mc "She's gorgeous."
                "Yasmin smiles at you both."
                yasmin "Aw, you guys! I feel very popular all of a sudden."

    aj "And I wanna marry..."

    if s3_mc.current_partner != "AJ":
        aj "Ciaran. I think he's really sweet and lovely."
    else:
        aj "[s3_name]."
        aj "I think she's totally stunning and an amazing person."
        # CHOICE
        menu:
            thought "AJ wants to marry me..."
            "I'd have preferred a snog":
                # NEED TO FILL
                "EMPTY"
            "That's so sweet":
                s3_mc "I'm flattered."
                aj "Just speaking the truth."
            "Let's start planning the wedding":
                s3_mc "We should have the ceremony right here in the Villa."
                s3_mc "Where we met."
                miki "How exciting!"
                elladine "Do we get to be bridesmaids?"
                aj "Er, you guys know we're only joking, right?"
                miki "Yeah, um, of course."
                s3_mc "But yes, of course you get to be bridesmaids."

    aj "Finally, I'm gonna pie... Seb."
    aj "He used my towel the other day."
    genevieve "Ew, what?"
    aj "I know. When I went to have a shower, it was all damp."
    "She shudders."
    miki "That is gross."
    iona "Right, you're up, Yasmin."

    if s3_like_yasmin:
        yasmin "I wanna snog [s3_name]."
        "You feel yourself blushing."
        # CHOICE
        menu:
            thought "Yasmin would snog me..."
            "Maybe you'll get a chance...":
                yasmin "Is that so?"
                s3_mc "You never know what might happen in the future."
            "In your dreams":
                "Yasmin smiles at you."
                yasmin "Yep. Well, last night for sure."
            "Kiss me right now, then":
                "Yasmin doesn't hesitate in leaning across the circle and placing her soft lips on yours."
                "Only you can hear the small sound of pleasure she makes."
                iona "Woo, you go girls!"
                yasmin "Just a bit of fun!"
                thought "That didn't feel like just a bit of fun..."
    else:
        yasmin "I wanna snog AJ."
        "AJ smiles."
        yasmin "I think she's so cute."
        if s3_mc.current_partner == "AJ":
            # CHOICE
            menu:
                thought "Yasmin wants to snog AJ..."
                "She should back off":
                    # NEED TO FILL
                    "EMPTY"
                "She could have picked any guy...":
                    # NEED TO FILL
                    "EMPTY"
                "No worries":
                    s3_mc "Yeah, she's very cute."
                    aj "You guys!."

    yasmin "And I'd marry..."

    if s3_mc.bisexual == False:
        yasmin "Seb."
        yasmin "I know he's with AJ, but he kind of caught my eye and I've gotta say I'm quite interested."
        iona "Interesting..."
    else:
        yasmin "[s3_name]."

        # CHOICE
        menu:
            thought "Yasmin wants to marry me!"
            "That's awesome":
                $ s3_mc.like("Yasmin")
                yasmin "I'm so glad you think so."
                yasmin "I might have a tiny crush on you."
                if s3_mc.current_partner == "AJ":
                    "AJ sighs and looks down."
            "But I'm with [s3_mc.current_partner]":
                $ s3_mc.like(s3_mc.current_partner)
                if s3_mc.current_partner == "AJ":
                    "AJ smiles at you."
                yasmin "I know. I just really fancy you. That's all. (also when MC is coupled with AJ)"
            "I don't know you very well yet":
                $ s3_mc.dislike("Yasmin")
                yasmin "I see."
                yasmin "Well I hope we can get to know each other more!"
                yasmin "I might have a tiny crush on you."
                if s3_mc.current_partner == "AJ":
                    "AJ seems really intent on fiddling with her blanket."
            "You're meant to choose different people" if s3_like_yasmin:
                yasmin "Well, it's not my fault if you're the only name that pops into my head."
                if s3_mc.current_partner == "AJ":
                    aj "Yeah but it is actually against the rules, babes."
                    aj "Pick someone else."
                    "Yasmin looks a little taken aback."
                    yasmin "OK, fine. I pick, um, Ciaran, I guess."
                    iona "What do you like about Ciaran?"
                    yasmin "I have no idea. I just needed to pick someone else apparently."
                    "AJ avoids making eye contact with anyone."

    yasmin "And my pie goes to..."
    yasmin "Tai."
    yasmin "Sorry, but it's gotta be."
    yasmin "He might be gorgeous and kind, but..."
    yasmin "He farted in the tent on the first night."
    yasmin "It was rank."
    "Everyone laughs. The game goes on for a little while longer."
    "The girls start snuggling down to go to bed, wrapping their arms around pillows and nearby women."
    "You see Yasmin make her way outside."

    scene black with dissolve
    $ new_scene()

    "You lie awake, listening to the sound of crickets outside. You feel yourself dozing off."

    scene s3-hideaway-night with dissolve
    $ new_scene()
    $ outfit = "swim"
    $ extra = "none"

    yasmin "Psst, [s3_name]."
    "Yasmin is whispering to you."
    s3_mc "What's up?"
    yasmin "Did you know there's a hot tub outside?"
    s3_mc "You mean we could have been in the hot tub this whole time?"
    yasmin "I know, right?"
    yasmin "Bet you haven't had many chances to get in the hot tub."
    s3_mc "You know what? We haven't!"
    yasmin "Well, what are you waiting for?"
    yasmin "We should just make the best of it while everyone else is crashed out."

    if s3_mc.bisexual:
        yasmin "So, I was thinking that maybe you and I could spend a little more one on one time together."
        yasmin "Alone."

    # CHOICE
    menu:
        thought "Yasmin invited me out to the hot tub..."
        "Let's go hot tubbing!":
            $ s3e5p3_hot_tubbing = True
            call s3e5p3_hot_tubbing from _call_s3e5p3_hot_tubbing
        "I need to catch up on my sleep":
            s3_mc "Sorry, babes."
            yasmin "No worries. Night!"
            "Yasmin grabs a towel and her bathing suit and makes her way outside."
            "You roll over and go to sleep."


    "Thanks a lot ladies."
    "Didn't even get a pie..."
    "You really know how to make a narrator feel special."

    scene sand with dissolve
    $ on_screen = []

    "Next time on Love Island..."
    "The lads find out what happened in the hideaway..."
    s3_mc "We gave each other oily massages..."
    "That must have happened while I was in the toilet."
    "And Tai teaches everyone a new form of exercise."

    $ outfit = "swim"

    tai "I call it... Tai Chi."
    $ leaving("tai")

    "..."
    "Do you want to tell him or should I?"
    "See you then!"

    jump s3e6p1
    return

label s3e5p3_hot_tubbing:
    $ outfit = "swim"

    "You grab your bikini and tiptoe over to her."
    yasmin "I knew you were the right person to ask."

    scene s3-hideaway-terrace-night with dissolve
    $ new_scene()

    "The night is warm. Above you, the stars are bright."
    "Yasmin slips into the hot tub and smiles at you. You get in and sit opposite her."
    s3_mc "No little Yasmin?"
    yasmin "No, she's tucked up in bed."
    yasmin "I don't think she'd enjoy getting wet."
    "Yasmin leans back and looks at the sky."
    yasmin "That was quite a game."

    if s3_mc.bisexual:
        if s3e5p3_snog != "Yasmin" and s3e5p3_marry != "Yasmin" and s3_like_yasmin:
            yasmin "Thanks for not recoiling in horror when I picked you to marry..."
            yasmin "Oh crap. I told you I had a crush on you as well, didn't I?"
            # CHOICE
            menu:
                thought "Yasmin's glad I didn't recoil when she picked me..."
                "It took me by surprise":
                    # NEED TO FILL
                    "EMPTY"
                "You don't have to say thank you":
                    s3_mc "I was really happy when you did."
                "I fancy you too":
                    "She smiles shyly."
                    yasmin "Really?"
        elif s3e5p3_snog == "Yasmin" or s3e5p3_marry == "Yasmin":
            if s3e5p3_snog == "Yasmin":
                $ fill_in = "kiss"
            else:
                $ fill_in = "marry"
            yasmin "Thanks for saying you'd [fill_in] me."
            # CHOICE
            menu:
                thought "Yasmin said thanks for picking her to [fill_in]..."
                "You don't have to say thank you":
                    s3_mc "I picked you because I wanted to."
                "It was just a bit of fun":
                    s3_mc "Don't read too much into it, yeah?"
                    yasmin "OK."
                "It meant something to me":
                    "She smiles shyly."
                    yasmin "Really?"

        "Yasmin looks down, and then up at you. Her hair falls in a dark curtain around her eyes."
        yasmin "You're very far away."

        # CHOICE
        menu:
            thought "Yasmin wants me to sit next to her..."
            "Sit next to her":
                $ s3e5p3_pursue_yasmin = True
                "You shuffle around to the other side of the tub. You don't stop until your thighs are gently touching."
                "Yasmin looks at you and smiles softly."
            "Stay on the other side of the tub":
                s3_mc "I've got more room to spread out over here."
                yasmin "OK, fair enough."
                yasmin "I've got to ask..."
                yasmin "Do you think we might have a chance? You and me?"
                yasmin "I'd love to see where things go with you."
                # CHOICE
                menu:
                    thought "Would I consider giving things a go with Yasmin?"
                    "Yes":
                        $ s3e5p3_pursue_yasmin = True
                        # NEED TO FILL
                        "EMPTY"
                    "Not right now":
                        # NEED TO FILL
                        "EMPTY"
                    "I don't see it happening":
                        $ s3_mc.dislike("Yasmin")
                        $ s3_like_yasmin = False
                        yasmin "OK."
                        yasmin "I hope we can still be friends, though."
                        s3_mc "Of course!"
            "Stay put, but rub her leg with your foot":
                s3_mc "I've got more room to spread out over here."
                yasmin "OK, fair enough."
                "You reach out your foot under the water and gently stroke Yasmin's leg."
                yasmin "I've got to ask..."
                yasmin "Do you think we might have a chance? You and me?"
                yasmin "I'd love to see where things go with you."
                # CHOICE
                menu:
                    thought "Would I consider giving things a go with Yasmin?"
                    "Yes":
                        $ s3e5p3_pursue_yasmin = True
                        # NEED TO FILL
                        "EMPTY"
                    "Not right now":
                        # NEED TO FILL
                        "EMPTY"
                    "I don't see it happening":
                        $ s3_mc.dislike("Yasmin")
                        $ s3_like_yasmin = False
                        yasmin "OK."
                        yasmin "I hope we can still be friends, though."
                        s3_mc "Of course!"

        if s3e5p3_pursue_yasmin == False:
            s3_mc "OK, my fingers are seriously wrinkly now."
            yasmin "Mine too. Let's head back in."
        else:
            yasmin "I hope this isn't a weird thing to say, but you remind me of the first person I ever kissed."
            yasmin "I only knew her for one day, when I was sixteen. We met in an airport."
            s3_mc "That's an odd place to meet girls."
            yasmin "Isn't it?"
            yasmin "I'd been visiting my mum's family in the States, and my flight home was delayed by like, eight hours."
            yasmin "She was in the same boat, except she was waiting for a flight to Australia."
            yasmin "So we knew we'd most likely never see each other again. And we never did."
            # CHOICE
            menu:
                thought "Yasmin's first kiss was with a girl she met at the airport..."
                "That's so sad":
                    # NEED TO FILL
                    "EMPTY"
                "That's romantic":
                    s3_mc "The odds of you even meeting each other in the first palace we so slim, and you still managed to have a special moment together."
                    s3_mc "That's amazing."
                    yasmin "I'm glad you get it."
                "That's hilarious":
                    yasmin "Yeah, I was sad at the time, but I smile when I look back on it now."

            yasmin "Thinking about that kiss made me realise what a strange and unpredictable world this is."
            yasmin "Most things are just beyond our control or understanding."
            yasmin "So it's no good stressing about what might have been. What happened is what happened."
            yasmin "A nice moment with a pretty girl is the greatest gift of all, if you ask me."
            "She looks at you from under her eyelashes and bites her lips."
            yasmin "So what about you? Do you remember the first time you kissed a girl?"
            yasmin "Not like the challenges in the Villa, or anything like that."
            yasmin "I mean a real kiss. A proper kiss. Just for the two of you."

            # CHOICE
            menu:
                thought "The first time I properly kissed a girl"
                "It was magical":
                    s3_mc "You never forget your first time, right?"
                    s3_mc "It was everything I'd been hoping it would be, and more."
                    yasmin "That's the best. You're so lucky."
                    s3_mc "Maybe I didn't know exactly what I was doing, but I knew I wanted to do it again."
                    yasmin "Well if you want to do it again right now..."
                    yasmin "I'm right here."
                "It was nothing special":
                    s3_mc "First times aren't always the best. You know how it is."
                    yasmin "Oh, yeah. Tell me about it."
                    s3_mc "It was pretty awkward. I needed a bit more practice before I got good at it."
                    yasmin "Well, if you want to get some more practice in right now..."
                    yasmin "I'm right here."
                "I haven't yet":
                    yasmin "Really? Never?"
                    s3_mc "Never. Not in the way you're talking about."
                    yasmin "Well, you know, [s3_name]..."
                    yasmin "It's never too late to start."

            "Without breaking eye contact, she reaches out and touches your hand."

            # CHOICE
            menu:
                thought "Yasmin wants to kiss me..."
                "Go in for the kiss":
                    $ s3_mc.like("Yasmin")
                    "She smiles and her eyes flutter closed as you lean in to kiss her."
                    "When your lips meet, she gives a little sigh of happiness."
                    "Her small hands slide into yours, tangling your fingers together."
                    "She pulls away for a moment, to plant a small kiss on your cheek and whisper in your ear."
                    yasmin "You are incredible."
                    "Then she kisses you properly again, teasing you with her tongue."
                    "For a while, nothing else in the world seems to matter at all."
                    "When you break apart, Yasmin's eyes are sparkling."
                    s3_mc "That was nice."
                    yasmin "It was better than nice."
                    "She lays her head on your shoulder. For a while, you just sit together in comfortable silence."
                "Wait for her to do it":
                    $ s3_mc.like("Yasmin")
                    s3_mc "Don't tease me."
                    "She smiles and leans in to kiss you."
                    "When your lips meet, she gives a little sigh of happiness."
                    "Her small hands slide into yours, tangling your fingers together."
                    "She pulls away for a moment, to plant a small kiss on your cheek and whisper in your ear."
                    yasmin "You are incredible."
                    "Then she kisses you properly again, teasing you with her tongue."
                    "For a while, nothing else in the world seems to matter at all."
                    "When you break apart, Yasmin's eyes are sparkling."
                    s3_mc "That was nice."
                    yasmin "It was better than nice."
                    "She lays her head on your shoulder. For a while, you just sit together in comfortable silence."
                "Change the subject":
                    pass


            s3_mc "So that girl you were talking about, the one you met at the airport..."
            s3_mc "You didn't think to swap numbers or anything?"
            yasmin "Nope. I think that would've made it  worse, don't you?"
            yasmin "I could never do that long distance relationship thing."
            yasmin "It was a fleeting, beautiful moment, and I'm okay with that."
            "She strokes the back of your hand gently with her thumb."
            yasmin "But I hope this thing between us won't be fleeting."
            yasmin "I'm getting wrinkly fingers."
            s3_mc "Me too. Let's head back in."

            if s3_mc.current_partner == "AJ":
                thought "It was cool to get some one on one time with Yasmin."
                # CHOICE
                menu:
                    thought "But it's got me thinking...How do I feel about AJ?"
                    "I don't see much of a future for us":
                        $ s3_like_aj = False
                        # NEED TO FILL
                        "EMPTY"
                    "I'm keeping my options open":
                        thought "AJ is great, but there's no harm getting to know other people."
                    "I'm happy with her":
                        $ s3_like_aj = True
                        "She's lovely and I think I make her happy too. So why mess with that?"
            else:
                # CHOICE
                menu:
                    thought "Am I interested in Yasmin?"
                    "Actually, I like AJ":
                        # NEED TO FILL
                        "EMPTY"
                    "Definitely":
                        $ s3_like_yasmin = True
                        thought "She's cute, talented and there's just something a little... mysterious about her."
                        thought "I'm not ready to rule her out just yet."
                        "AJ's cool and everything but Yasmin's got something about her."
                    "Just keeping my options open":
                        $ s3_like_yasmin = True
                        thought "I don't want to rule out where that could lead..."
                        thought "Now that I think about it, AJ's the only one for me."

        "You dry yourself off. Yasmin smiles at you and you follow her back into the hideaway."
    else:
        if s3_mc.current_partner != s3e5p3_marry:
            yasmin "You picked [s3e5p3_marry] to marry..."
            yasmin "I thought you'd pick [s3_mc.current_partner]."
            "She raises her eyebrows at you."
            yasmin "Trouble in paradise?"
            # CHOICE
            menu:
                thought "Is there 'trouble in paradise'?"
                "We're solid as a rock":
                    # NEED TO FILL
                    "EMPTY"
                "It was only a game":
                    # NEED TO FILL
                    "EMPTY"
                "[s3_mc.current_partner] and I aren't 'paradise'":
                    s3_mc "I'm having my doubts, if I'm honest."
                    yasmin "I'm sorry, babe. That's rough."
        else:
            yasmin "It's really sweet that you chose [s3e5p3_marry] to marry."
            yasmin "But you snogged [s3e5p3_snog]."
            yasmin "Are you a little bit curious?"
            $ pronouns(s3e5p3_snog)
            # CHOICE
            menu:
                thought "Am I interested in [s3e5p3_snog]?"
                "I just think [he_she!c]'s fit, that's all":
                    # NEED TO FILL
                    "EMPTY"
                "Yes, definitely":
                    # NEED TO FILL
                    "EMPTY"
                "Maybe a little bit":
                    s3_mc "Well..."
                    s3_mc "I wouldn't have picked [him_her] if I hadn't thought about it."
                    s3_mc "[s3_mc.current_partner] is great, but I can't help wondering if there's something missing."

        if s3_mc.current_partner != s3e5p3_snog and s3_mc.current_partner != s3e5p3_marry:
            yasmin "So you snogged [s3e5p3_snog] and you chose to marry [s3e5p3_marry]."
            yasmin "Are you just not feeling it with [s3_mc.current_partner]?"
            # CHOICE
            menu:
                thought "Do I still want to be with [s3_mc.current_partner]?"
                "It's only been a couple of days":
                    # NEED TO FILL
                    "EMPTY"
                "It was only a game":
                    # NEED TO FILL
                    "EMPTY"
                "My head's definitely been turned":
                    $ s3_mc.dislike(s3_mc.current_partner)
                    if s3_mc.current_partner == "Bill":
                        $ s3_like_bill = False
                    elif s3_mc.current_partner == "Camilo":
                        $ s3_like_camilo = False
                    elif s3_mc.current_partner == "Harry":
                        $ s3_like_harry = False
                    s3_mc "What can I say? I'm keeping my options open."

    thought "We should head back inside soon..."

    # CHOICE
    menu:
        thought "I probably have time to talk about a couple more things with Yasmin..."
        "So you choose to pie Tai...":
            $ s3e5p3_question = "Tai"
            # NEED TO FILL
            "EMPTY"
        "So you choose to snog AJ...":
            $ s3e5p3_question = "AJ"
            yasmin "Yeah. She's freaking adorable."
            yasmin "I always seem to go for girls who smell like summertime."
            if s3_mc.bff == "Seb":
                s3_mc "So are you considering her as well as Seb?"
                yasmin "No, I don't think so. She's cute, but that's not the be-all and end-all."
            yasmin "There's someone else I've got my eye on."
        "So you choose to marry Seb...":
            $ s3e5p3_question = "Seb"
            yasmin "Yeah. It's early days, but I think we've got a lot in common."
            yasmin "I always seem to go for boys with an air of sadness around them..."
            s3_mc "So he's who you've got your eye on, then?"
            yasmin "Yup."
            thought "Poor AJ."
            if s3_mc.bff == "Seb":
                s3_mc "Enough to maybe couple up?"
                "Yasmin blushes."
                yasmin "I'm definitely considering it."

    # CHOICE
    menu:
        thought "I probably have time for one more... (second choice; appears after the first question)"
        "So you choose to pie Tai..." if s3e5p3_question != 'Tai':
            # NEED TO FILL
            "EMPTY"
        "So you choose to snog AJ..." if s3e5p3_question != 'AJ':
            yasmin "Yeah. She's freaking adorable."
            yasmin "I always seem to go for girls who smell like summertime."
            if s3_mc.bff == "Seb":
                s3_mc "So are you considering her as well as Seb?"
                yasmin "No, I don't think so. She's cute, but that's not the be-all and end-all."
            yasmin "There's someone else I've got my eye on."
        "So you choose to marry Seb..." if s3e5p3_question != 'Seb':
            yasmin "Yeah. It's early days, but I think we've got a lot in common."
            yasmin "I always seem to go for boys with an air of sadness around them..."
            s3_mc "So he's who you've got your eye on, then?"
            yasmin "Yup."
            thought "Poor AJ."
            if s3_mc.bff == "Seb":
                s3_mc "Enough to maybe couple up?"
                "Yasmin blushes."
                yasmin "I'm definitely considering it."

    yasmin "Just so you know, I could put in a good word with Ciaran or Tai if you want."
    yasmin "We're pretty close since we all arrived together."

    # CHOICE
    menu:
        thought "Do I want Yasmin to help me get with Ciaran or Tai?"
        "No, I'm OK thanks":
            $ s3_like_ciaran = False
            $ s3_like_tai = False
            # NEED TO FILL
            "EMPTY"
        "Yes, talk to Ciaran":
            $ s3_mc.like("Ciaran")
            $ s3_like_ciaran = True
            $ s3e5p3_yasmin_help = "Ciaran"
            yasmin "You got it."
            yasmin "I'll talk to him and nudge him in your direction."
            yasmin "Though I know he already likes you."
        "Yes, talk to Tai":
            $ s3_mc.like("Tai")
            $ s3_like_tai = True
            $ s3e5p3_yasmin_help = "Tai"
            yasmin "You got it."
            yasmin "I'll talk to him and nudge him in your direction."
            yasmin "Though I know he already likes you."

    "You both sit for a while, letting the warm water bubble around you. A cicada chirps from a tree."
    yasmin "I'm getting wrinkly fingers."
    s3_mc "Me too. Let's head back in."
    "You dry yourself off. Yasmin smiles at you and you follow her back into the hideaway."

    scene s3-hideaway-night with dissolve
    $ new_scene()

    return

#########################################################################
## Episode 6, Part 1
#########################################################################
label s3e6p1:
    scene sand with dissolve
    $ on_screen = []
    $ outfit = "swim"

    show screen day_title(6, 1) with Pause(4)
    hide screen day_title with dissolve

    "Welcome back to Love Island!"
    "Yesterday, our Islanders awoke in the great outdoors that is the Villa lawn..."
    "Only to discover three new singles had pitched a tent in the night."
    ciaran "Hey, well done! You're the first person to find us."
    $ leaving("ciaran")
    "And if that wasn't wild enough, these new Islanders took a few lucky ones on a date!"

    if s3_mc.bff == "Elladine":
        elladine "It must be one of the new Islanders!"
        $ leaving("elladine")
    elif s3_mc.bff == "Genevieve":
        genevieve "It must be one of the new Islanders!"
        $ leaving("genevieve")
    elif s3_mc.bff == "Nicky":
        nicky "It must be one of the new Islanders!"
        $ leaving("nicky")
    elif s3_mc.bff == "Seb":
        seb "It must be one of the new Islanders!"
        $ leaving("seb")
    
    if s3_mc.bisexual:
        "And [s3_name] was asked out by all three..."
        yasmin "Are you not even a little surprised to see me?"
        $ leaving("yasmin")
    else:
        "And [s3_name] was asked out by both the hunky guys!"
    
    tai "It also means I'm good with my hands."
    $ leaving("tai")
    "Typical. It's just like buses. You wait all day, then three show up at once..."
    "Then the England football squad get out and ask you maths questions..."
    "But enough about my recurring dream."
    "After all those dates, our girls ended the day with a quiet sleepover."
    genevieve "I'll get you for that!"
    $ leaving("genevieve")
    "Coming up!"
    "Tai gets compliments about his wazoo..."
    miki "Tai's an incredible and passionate lover!"
    $ leaving("miki")
    "And Ciaran wants to take a tour around his hometown....."
    ciaran "Will you join me?"
    $ leaving("ciaran")
    "Don't miss it..."

    scene s3-hideaway-day with dissolve
    $ new_scene()
    $ outfit = "pjs"

    "You wake up, surrounded by the warmth of the girls. AJ lies curled in front of you."
    thought "Ow, something's poking into my back."
    "You wriggle around and discover that it's Yasmin's knee pressing into you."

    # CHOICE
    menu:
        thought "Yasmin's knee is digging into me..."
        "Gently nudge her awake":
            "You turn slightly and gently rock Yasmin's shoulder."
            s3_mc "Yasmin, babes..."
            "She blearily opens her eyes."
            yasmin "Huh?"
            s3_mc "Morning! Could you move your knee?"
            "She looks down."
            yasmin "Oh! Sorry, hun."
        "Hit her with a pillow ":
            "You grab a nearby pillow and throw it at her face."
            "She lets out a moan."
            yasmin "What's going on?"
            genevieve "Everything OK, babe?"
            yasmin "Something hit my face."
            s3_mc "Must've been a dream..."
            "She looks around confused for a moment longer, before eventually shrugging it off and rolling over."
            thought "Much better."
        "Playfully tickle her":
            "You reach over to her stomach and gently tickle it with the tips of your fingers."
            "Yasmin's face twitches. Her eyes flicker open."
            yasmin "Um, what are you doing?"
            s3_mc "Tickling you!"
            "Your fingers work faster. Yasmin seems unfazed."
            yasmin "Sorry to disappoint, but I'm not ticklish."
            s3_mc "Oh..."
            yasmin "I can pretend, if that would make you feel better?"
            "She starts to squirm."
            yasmin "Ooh aah, oh no, please stop."
            yasmin "How was that?"
            s3_mc "Much better."

    genevieve "Wow, I slept so well."
    genevieve "You know those sleeps you have maybe once a year where you actually feel completely refreshed and awake?"
    genevieve "That's me right now."

    # CHOICE
    menu:
        thought "What are my thoughts on sleep?"
        "I don't think about it till I'm desperate":
            s3_mc "And then I can't get it."
            miki "I have that all the time!"
            miki "I wish my barge rocked more. That would make me sleepier..."
            miki "Some nights I just lay there like... come on."
            miki "I find actually having someone to sleep next to is a big help..."
        "I love it":
            s3_mc "It's, like, the best!"
            genevieve "So do I!"
            genevieve "But it's so rare that I actually get, like, a perfectly restful night's sleep."
            s3_mc "Huh, I don't have that problem."
            genevieve "Lucky!"
        "I've never felt awake in my life":
            iona "Hard. Same."
            iona " I'm like a zombie in the morning until at least the second cup of coffee."
            "She wipes at her face, small bags under each eye."
            iona "Today's no different..."

    "AJ springs out of the pile."
    aj "Why are we talking so much about sleep after we just woke up?"
    aj "Come on! Let's get out there."
    aj "I want to find out what the boys got up to while we were in here."
    s3_mc "Tai said he wanted to organise his own boys' sleepover."
    miki "Do you think he did?"
    elladine "That'd be too cute."
    iona "Ugh, you morning people make me feel ill."
    "Iona pulls a sheet back over herself and curls into a small bundle."

    # CHOICE
    menu:
        thought "We should..."
        " Get up. AJ's right":
            elladine "And, no offence, but I'd like to not be squished together anymore."
            iona "More room for me."
        " Go and get some food":
            iona "Hmmm... that's not a bad shout. If there's one thing that'll get me out of bed, it's food."
            iona "Or shower sex..."
        "Spoon for a bit longer":
            iona "That's what I'm talking about!"
            iona "Come here, babes..."
            "She wraps her arms around you and pulls you into a friendly cuddle. She's surprisingly warm."
            "You feel her stomach rumble."
            iona "Oh, guess I'm hungrier than I realised."

    miki "I'm starving!"
    genevieve "Do you think the guys will have made us breakfast?"
    elladine "No chance."
    elladine "They've probably nommed the whole lot..."
    aj "More reason to get out of here, then!"
    aj "Quick, let's get ready."

    scene s3-dressing-room with dissolve
    $ new_scene()

    # Add back once there are MC images are in game.
    thought "What should I wear today?"
    # Outfit change to swimwear
    "You get changed into your bathing suit."
    $ outfit = "swim"
    thought "This is such a cute number on me."
    miki "Wow, [s3_name]! That's such a cute number on you!"
    s3_mc "I was just thinking that!"
    # thought "This caught the others' eyes before."
    # thought "I'm sure it will again..."
    # thought "This still feels a bit basic, but that's fine..."

    elladine "Alright, girls. Let's get out there and find some grub!"

    scene s3-lawn-day with dissolve
    $ new_scene()

    "You and the other girls emerge onto the lawn. The boys are sitting around with plates of food on their laps."
    camilo "Alright, ladies."
    camilo "We've got some banging food for you all in the kitchen."
    s3_mc "They did make us breakfast!"
    genevieve "That's so sweet!"

    if s3_mc.current_partner != "Camilo":
        iona "Camilo talking about banging and food? OK..."
        "He gives her a cheeky wink."
        iona "This definitely makes getting out of bed worth it."

    "[s3_mc.current_partner] walks up to you."

    if s3_mc.current_partner == "Bill":
        bill "Hey, babe!"
        "You hug each other."
        bill "It was weird not having you in bed last night. Also..."
        bill "I made you some food."
    elif s3_mc.current_partner == "Camilo":
        camilo "Hey, babe!"
        "You hug each other."
        camilo "It was weird not having you in bed last night. Also..."
        camilo "I made you some food."
    elif s3_mc.current_partner == "Harry":
        harry "Hey, babe!"
        "You hug each other."
        harry "It was weird not having you in bed last night. Also..."
        harry "I made you some food."
    elif s3_mc.current_partner == "AJ":
        "Camilo walks up to you and AJ."
        camilo "I made you two some food, seeing as you were both in the hideout."
        harry "Oi, we helped, too."
        bill "I was in charge of condiments."
        harry "Yeah, and I did the dishes..."
        s3_mc "Thanks, boys."

    # CHOICE
    menu:
        thought "That's..."
        "So sweet of you!":
            if s3_mc.current_partner == "Bill":
                bill "Glad to be of service."
            elif s3_mc.current_partner == "Camilo":
                camilo "Glad to be of service."
            elif s3_mc.current_partner == "Harry":
                harry "Glad to be of service."
            elif s3_mc.current_partner == "AJ":
                camilo "No problem!"
        "The best news I've heard all day":
            if s3_mc.current_partner == "Bill":
                bill "It's the morning."
            elif s3_mc.current_partner == "Camilo":
                camilo "It's the morning."
            elif s3_mc.current_partner == "Harry":
                harry "It's the morning."
            elif s3_mc.current_partner == "AJ":
                # NEED TO FILL
                "EMPTY - Path: Coupled with AJ"
            s3_mc "Still counts as all day."
        "So well timed! I'm starved...":
            if s3_mc.current_partner == "Bill":
                bill "Well eat up then, babe."
            elif s3_mc.current_partner == "Camilo":
                camilo "Well eat up then, babe."
            elif s3_mc.current_partner == "Harry":
                harry "Well eat up then, babe."
            elif s3_mc.current_partner == "AJ":
                camilo "Well dig in, then, you two."

    "You hear Miki laugh."
    miki "Why is there a bean bag floating in the pool?"
    seb "That's a mystery."
    miki "A mystery?!"
    seb "We have to have some secrets."
    "You all tuck into the food. It's gorgeous."
    "When you're nearly finished, Ciaran asks the big question."
    ciaran "So, what did you girls get up to at the sleepover?"

    # CHOICE
    menu:
        thought "Last night we... (you can only choose two)"
        "Had a massive pillow fight":
            s3_mc "I absolutely crushed it."
            camilo "Ooh, we did something similar..."
        "Played snog, marry, pie":
            s3_mc "I snogged [s3e5p3_snog], married [s3e5p3_marry]..."
            s3_mc "... and pied [s3e5p3_pie]."

            if s3e5p3_pie == "Bill":
                bill "It's okay. I know where I stand."
            elif s3e5p3_pie == "Camilo":
                camilo "It's okay. I know where I stand."
            elif s3e5p3_pie == "Harry":
                harry "It's okay. I know where I stand."
            elif s3e5p3_pie == "Tai":
                tai "It's okay. I know where I stand."
            elif s3e5p3_pie == "Ciaran":
                ciaran "It's okay. I know where I stand."

            if s3e5p3_snog == "Bill":
                bill "Cheer up, [s3e5p3_pie], she had to choose someone."
            elif s3e5p3_snog == "Camilo":
                camilo "Cheer up, [s3e5p3_pie], she had to choose someone."
            elif s3e5p3_snog == "Harry":
                harry "Cheer up, [s3e5p3_pie], she had to choose someone."
            elif s3e5p3_snog == "Tai":
                tai "Cheer up, [s3e5p3_pie], she had to choose someone."
            elif s3e5p3_snog == "Ciaran":
                ciaran "Cheer up, [s3e5p3_pie], she had to choose someone."
            elif s3e5p3_snog == "Yasmin":
                yasmin "Cheer up, [s3e5p3_pie], she had to choose someone."
            elif s3e5p3_snog == "AJ":
                aj "Cheer up, [s3e5p3_pie], she had to choose someone."

            if s3e5p3_pie == "Bill":
                bill "That's easy for you to say!"
            elif s3e5p3_pie == "Camilo":
                camilo "That's easy for you to say!"
            elif s3e5p3_pie == "Harry":
                harry "That's easy for you to say!"
            elif s3e5p3_pie == "Tai":
                tai "That's easy for you to say!"
            elif s3e5p3_pie == "Ciaran":
                ciaran "That's easy for you to say!"

            if s3e5p3_snog == "Bill":
                bill "True."
            elif s3e5p3_snog == "Camilo":
                camilo "True."
            elif s3e5p3_snog == "Harry":
                harry "True."
            elif s3e5p3_snog == "Tai":
                tai "True."
            elif s3e5p3_snog == "Ciaran":
                ciaran "True."
            elif s3e5p3_snog == "Yasmin":
                yasmin "True."
            elif s3e5p3_snog == "AJ":
                aj "True."

            "[s3e5p3_marry] just looks at you with a cheeky grin."
        "Gave each other oily massages...":
            ciaran "Really?!"
            harry "I can't believe we missed that."
            "You sigh."
            s3_mc "No, of course we didn't! It was a joke."
            iona "Kinda wish we had, though, now you've said it."
            iona "It sounds like a lot of fun..."
            ciaran "You know, I don't think I've ever had a massage"
            tai "What?"
            miki "Yeah, that's shocking."
            ciaran "Just never needed one, I guess?"
            tai "It's not just about needing one, my friend."
            tai "Don't worry, I've got experienced hands."
            tai "I'll give you a good kneading."
            tai "You'll feel incredible afterwards."
            ciaran "Oh, alright..."
            ciaran "Thanks!"

    elladine "But enough about what we got up to."
    iona "Yeah, tell us what you did last night..."
    miki "Why are the bean bags all over the place?"
    nicky "Simple. We jousted with them."
    genevieve "... Huh?"
    tai "One boy, the 'knight', sits on the back of another boy. The 'horse'."
    tai "They face another knight and horse team."
    tai "The knights use bean bags to knock the other knight off their horse."
    camilo "Harry got destroyed."
    harry "It's not my fault! I was against Ciaran and Tai..."
    harry "And Bill was a rubbish horse."
    bill "Oi, I was an amazing horse. I did the neighs and whinnies and everything."
    harry "You got the horse impression spot on."
    harry "Shame you didn't, like, move or anything."
    tai "Hey, to be fair, it wasn't all Bill's fault."
    tai "Me and Ciaran are just a solid team is all."
    "Tai throws a muscled arm around Ciaran's shoulders."
    "A broad smile spreads across Ciaran's face."

    # CHOICE
    menu:
        thought "Sounds like..."
        "We all had a fun night":
            genevieve "It was fab! I hadn't done a sleepover in years."
            camilo "Yeah, and I got to watch Harry get pummelled with bean bags. It was a right laugh."
        "The lads had their own sleepover":
            s3_mc "Just like you wanted, Tai!"
            tai "Yeah, jousting wasn't what I had in mind, though."
            iona "Typical guys, can't just sit still and chat for a minute"
            nicky "Didn't you have a pillow fight?"
            iona "Yeah, yeah..."
        "I could take you all at jousting...":
            tai "Ooh, tough talk from [s3_name]."
            tai "We'll see if she can back it up."
            tai "Not now, though. I'm full of breakfast..."

    $ pronouns(s3_mc.bff)
    scene s3-lawn-day with dissolve
    $ new_scene()

    "As the others continue to chat, [s3_mc.bff] comes over."

    if s3_mc.bff == "Elladine":
        elladine "Hey you!"
        s3_mc "Hey!"
        elladine "I'm glad we're all back together as one big Villa. It was weird having everyone apart."
    elif s3_mc.bff == "Genevieve":
        genevieve "Hey you!"
        s3_mc "Hey!"
        genevieve "I'm glad we're all back together as one big Villa. It was weird having everyone apart."
    elif s3_mc.bff == "Nicky":
        nicky "Hey you!"
        s3_mc "Hey!"
        nicky "I'm glad we're all back together as one big Villa. It was weird having everyone apart."
    elif s3_mc.bff == "Seb":
        seb "Hey you!"
        s3_mc "Hey!"
        seb "I'm glad we're all back together as one big Villa. It was weird having everyone apart."

    "[s3_mc.bff] smiles as [he_she] looks at you."

    if s3_mc.bff == "Elladine":
        elladine "It was great getting to just chill with you last night."
        elladine "I didn't get a chance to check in with you about your dates yet!"
        elladine "How did they go?"

        # CHOICE
        menu:
            thought "How did my dates with the new people go?"
            "I found them really awkward ":
                # NEED TO FILL
                "EMPTY"
            "I found them a bit boring ":
                # NEED TO FILL
                "EMPTY"
            "I had so much fun":
                elladine "That's great! Dates are so fun when they go well."
                elladine "And if they don't, hopefully you at least get a good story out of them."

        elladine "Dating can be such a minefield. I've had some shockers."
        elladine "And some good ones too."

        # CHOICE
        menu:
            thought "What should I ask Elladine about her dating history?"
            "About the worst date she's been on":
                # NEED TO FILL
                "EMPTY"
            "About the weirdest date she's been on":
                # NEED TO FILL
                "EMPTY"
            "About the best date she's been on ":
                elladine "My best date? I went to the National Museum in Cardiff with this guy Chris. It was kind of a blind date."
                elladine "Turned out he had an art history degree and he knew everything. It was so interesting."
                elladine "I wasn't expecting much, but by the time we got to the Chinese jades it felt like we'd known each other forever."
                elladine "He moved to Prague a couple of years ago, and we fizzled out."
                s3_mc "...but now you're here, with me! so it all worked out in the end."

                elladine "Oh well. What about you? Any particularly memorable dates in your past?"

        # CHOICE
        menu:
            thought "I should tell Elladine about that one really strange date..."
            "...at a farm":
                s3_mc "Me and this lad went to one of those farms where you can feed lambs."
                elladine "Super cute!"
                s3_mc "Yes, except three of the sheeps got out while we were there and they paid us twenty quid each to chase them down."
                s3_mc "I've never had a workout quite like it."
                elladine "Did you manage to catch the sheep?"
                s3_mc "...No."
            "...on a boat":
                s3_mc "I had champagne on a really rich guy's yacht."
                s3_mc "We didn't sail it or anything, just sat on the deck while it was moored."
                elladine "Wow, fancy."
                s3_mc "Sorry, did I say it was 'his' boat? I meant it was 'a' boat."
                elladine "No!"
                s3_mc "Yep. he'd just been hired to clean it."
                elladine "That's so brass-necked. Takes guts, I suppose."
                s3_mc "I suppose so. It was pretty scary to realise he'd been lying, though."
                elladine "Yeah, that sounds creepy. Glad you were alright!"
            "...in an escape room":
                s3_mc "I went with this guy to an escape room. It was really fun, but we got super stuck and didn't manage to solve it."
                s3_mc "A girl who worked there came in to get us..."
                s3_mc "...and the door locked behind her."
                elladine "No way! Didn't she have a key?"
                s3_mc "Nope. She had to call her friend to come let us out."
                s3_mc "But the friend wouldn't let us out until we'd solved it!"
                elladine "Wow."
                s3_mc "The really funny thing is that I only saw the guy a couple more times, but I'm still friends with Erica, the girl who got trapped in there with us."
    elif s3_mc.bff == "Nicky":
        nicky "You know, I missed having you around last night."
        s3_mc "Yeah?"
        nicky "Yeah. I just kept thinking how good you'd have been at the jousting."
        s3_mc "You know it!"
        s3_mc "Did you worry about me?"
        nicky "I wouldn't go that far. I haven't gone into full big brother mode yet."
        nicky "Besides, I know you can take care of yourself better than Rachel."
        s3_mc "Why do we always end up talking about your sister?"
        s3_mc "It seems like you're spending a lot of time worrying about her."
        nicky "Yeah... I guess I am. It's hard to break the habit!"
        nicky "Up to now, I've always been there to keep an eye on her."
        nicky "I dread to think what could've happened while I've been away."

        # CHOICE
        menu:
            thought "Nicky keeps worrying about his sister..."
            "It means you're a good brother":
                s3_mc "I think it's really sweet that you're thinking about her!"
                s3_mc "I only hope it's not getting in the way of you enjoying yourself here."
                nicky "It's not!"
                nicky "Well, maybe a little bit."
            "Your parents should be doing that":
                s3_mc "That's what they're there for, right?"
                nicky "I guess..."
                nicky "It's just always been this way since we were kids. She gets in trouble, I get her out."
                s3_mc "At this rate, it's going to stay that way forever."
            "I think she can look after herself ":
                s3_mc "Didn't you say she'd already been to uni? How old is she?"
                nicky "Twenty-two, but..."
                s3_mc "But what?"
                nicky "Well, I think of her as being younger."
                s3_mc "Come on, man. She's a grown woman. She can look out for herself."

        s3_mc "Maybe you just need to take a little step back and see what happens."
        s3_mc "I'm sure it wouldn't be the end of the world."
        nicky "Yeah... you might have a point there."
        nicky "Maybe she'd be a bit more of a grown-up if I started treating her like one."
        "He looks thoughtful, before turning back to you with a grin."
        nicky "So anyway, how was the sleepover?"
        nicky "Get up to anything scandalous?"

        # CHOICE
        menu:
            thought "The sleepover..."
            "None of your business! ":
                # NEED TO FILL
                "EMPTY"
            "It was very respectable":
                s3_mc "No spicy gossip to report, I'm afraid."
                nicky "Well, that's no fun."
                nicky "There's no point being here if you don't do something to embarrass your family just a little bit."
                s3_mc "You can't talk. You haven't done anything scandalous at all yet!"
                nicky "I'm different! I told you, I prefer watching other people's drama, not making my own."
                nicky "Being boringly settled and happy with Ella suits me just fine."
                nicky "Besides, I've got to set a good example for Rach, haven't I?"
            "I was a bit naughty ":
                s3_mc "Things may have gotten a little spicy."
                s3_mc "This is me we're talking about, remember."
                nicky "Glad to hear it."

        nicky "There's no point being here if you don't do something to embarrass your family just a little bit."
        s3_mc "You can't talk. You haven't done anything scandalous at all yet!"
        nicky "I'm different! I told you, I prefer watching other people's drama, not making my own."
        nicky "Being boringly settled and happy with Ella suits me just fine."
        nicky "Besides, I've got to set a good example for Rach, haven't I?"
    elif s3_mc.bff == "Genevieve":
        genevieve "It was great getting to just chill out with you last night."
        genevieve "How is it that we can just, like, chill out together and it doesn't have to be a big thing but it always feels amazing."
        genevieve "That's a real big deal for me."
        genevieve "It feels natural to just be around you, even when we're not talking, you know?"
        genevieve "I normally hate awkward silence."

        # CHOICE
        menu:
            thought "Awkward silences..."
            "Never happen to me":
                # NEED TO FILL
                "EMPTY"
            "Are the worst thing ever":
                genevieve "Yeah."
                genevieve "I mean, there are a bunch of other things that are, like, a lot worse than awkward silence."
                genevieve "But they are pretty bad."
            "Happen when you're with the wrong people":
                genevieve "That's so true!"
                genevieve "I can't imagine we'll ever have an awkward silence again."

        genevieve "I genuinely believe if there was ever an awkward silence it was because the other was hating me on the inside."

        # CHOICE
        menu:
            thought "Genevieve used to think people hated her!"
            "Sit there in silence":
                # NEED TO FILL
                "EMPTY"
            "I thought the same!":
                genevieve "Really? You too?"
                s3_mc "Yeah, I'd be thinking in my head that it was all my fault that it was awkward."
                genevieve "Yeah, exactly!"
            "That's silly, no one could hate you":
                "She smiles at you."
                genevieve "It was really silly and irrational of me, I know."
                genevieve "But that's how I felt."

        genevieve "I feel comfy with you, even in the silence which is like a big deal to me."
        genevieve "So, thank you for that."
    elif s3_mc.bff == "Seb":
        seb "You know, I missed having you around last night."
        s3_mc "Yeah?"
        seb "Yeah. I just kept thinking how good you'd have been at the jousting."
        s3_mc "You know it!"
        seb "I had another idea for how to name the kittens."
        seb "Not that your suggestion last time wasn't hilarious."
        seb "But, like, in case I need a backup."
        seb "What if I gave them numbers?"
        s3_mc "Numbers? Like... Kitten One, Kitten Two, Kitten Three...?"
        seb "Yeah. Don't you think that's kind of elegant?"

        # CHOICE
        menu:
            thought "Giving the kittens numbers instead of names..."
            "It's a bit harsh":
                # NEED TO FILL
                "EMPTY"
            "It makes sense":
                s3_mc "I guess it does save you coming up with names for all of them."
                seb "Exactly."
                seb "Although some of our ideas before were pretty good."
            "We should do that with people":
                seb "Like... you'd call your parents Human One and Human Two, 'cause they're the first people you ever met?"
                seb "And give a new number to every person you meet for the rest of your life?"
                s3_mc "That, or every person on earth gets their own unique number."
                seb "Tell you what, Human Twenty Billion and Twelve... that's not a bad idea."
                s3_mc "Glad you agree, Human Ten Billion, Three Thousand and One."

        seb "I guess I can't really make a decision until I get home and actually see the kittens myself."
        seb "A bit like naming a baby. Apparently."
        seb "Not that I've ever named a baby."
        seb "But my parents didn't name me until I was born and they looked at me like, oh, that's a Sebastian."
        s3_mc "Wait, do your parents still call you Sebastian?"
        seb "Yep. Which is one of the reasons I don't go round to visit them much."

        # CHOICE
        menu:
            thought "Seb's parents call him Sebastian"
            "I think it suits you better":
                # NEED TO FILL
                "EMPTY"
            "I can only see you as a Seb":
                s3_mc "You're a one-syllable-name kinda guy."
                seb "Thank you! Yes. Exactly."
                seb "I don't have anything against the name itself."
                seb "But it's not me."
            "Why not shorten it to 'Astian' instead?":
                s3_mc "You don't have to drop the middle and end of your name. Drop the first syllable instead."
                seb "I never thought of that before."
                seb "Probably because 'Astian' sounds like a name you'd give an elf in a fantasy film?"
                s3_mc "I think it sounds cool."
                seb "It has a certain charm."

        seb "Just don't call me Sebastian unless you want me to think you've suddenly turned into my mum."
        s3_mc "Well, we can't be too hard on your parents. You're having a hard time coming up with names for a bunch of baby cats."
        seb "Oof. True."
        seb "How did your parents decide to call you [s3_name], then?"

        # CHOICE
        menu:
            thought "My name..."
            "My parents just liked how it sounds":
                seb "Hey, fair enough. I think it was basically the same with mine, too."
                s3_mc "Meaningless name squad!"
            "I actually chose it myself":
                seb "Oh wow, really?"
                seb "How did you choose it?"
                # SUB-CHOICE
                menu:
                    thought "I chose my name because..."
                    "I just like how it sounds":
                        pass
                    "It's from someone I admire":
                        pass
                    "It's meaning speaks to me":
                        seb "That's badass."
                        seb "Like you just stood up and said 'actually, my name's [s3_name]'. And it was."
                        seb "I would love to do that. Just totally reinvent myself as the person I want to be."
                        seb "But I probably couldn't be bothered with the paperwork."
                    "It's got special significance":
                        seb "Oh, cool. In what way?"
                        # SUB-SUB-CHOICE
                        menu:
                            thought "The name [s3_name]..."
                            "It's an old family name":
                                pass
                            "It connects to my culture":
                                pass
                            "It's from an inspirational person":
                                pass
                        seb "That's awesome. I don't think anyone put that much thought into my name."
                        seb "It must be nice to have that connection to something outside yourself."
                        seb "So you're never really alone."
                        seb "That's deep, man."

    "[s3_mc.bff] burps loudly."

    if s3_mc.bff == "Elladine":
        elladine "Oops! Sorry. That was just a big breakfast..."
    elif s3_mc.bff == "Genevieve":
        genevieve "Oops! Sorry. That was just a big breakfast..."
    elif s3_mc.bff == "Nicky":
        nicky "Oops! Sorry. That was just a big breakfast..."
    elif s3_mc.bff == "Seb":
        seb "Oops! Sorry. That was just a big breakfast..."

    iona "Don't apologise! It's only natural."
    "Iona gives a thunderous belch."
    ciaran "Woah..."
    harry "Wait, you mean we don't have to, like, hold stuff in?"
    "He musters a small burp in response."
    harry "Ugh, that'd been trapped for ages."

    # CHOICE
    menu:
        thought "Everyone seems gassy..."
        "Maybe we should work off the food?":
            s3_mc "Something active could help?"
            tai "Hey, that's a great idea!"
        "You're all gross!":
            tai "What? You trying to say the human body is gross?"
            s3_mc "Some of it is, yeah!"
            tai "It's a wonderful, natural machine. Be proud of it!"
            "He leans back and gives a long, dramatic belch."
            iona "Embrace the gross!"
        "Burp really loudly":
            "You give an enormous burp. It's louder than all the others."
            bill "Think we've got a winner here, lads."

    tai "Let's do some post-breakfast exercise to help digest all this food."
    miki "Ooh, like yoga?"
    tai "Kinda. I call it... Tai Chi."
    aj "Tai chi? That's already a thing."
    tai "No no, Tai Chi. As in, me."
    "Elladine rolls her eyes."
    tai "It's just regular tai chi, except you also have to repeat what I say."
    tai "It'll be inspirational stuff."

    # CHOICE
    menu:
        thought "This sounds like..."
        "Such a good idea! Let's do it":
            $ s3_mc.like("Tai")
            yasmin "Yeah! I'm good to give it a go! Take us through it big guy. "
        "Something I'll regret ":
            "Iona leans over to you and whispers in your ear."
            iona "Babe, don't you see what this is really about?"
            iona "We're a bunch of sexy people in tight clothes doing intimate stretches."
            iona "What's to regret?"
        "Such a Tai thing to suggest ":
            tai "What can I say?"
            tai "It's in the name!"

    tai "Alright, everyone give each other enough space and follow my lead."
    "The Islanders play along and spread out. Tai stands in front of them, a cheeky grin on his face."
    tai "But be warned, this isn't like regular tai chi... Just copy me."
    "You all imitate Tai's pose."
    tai "Alright, we're going to start with a simple turn and repeat what I say!"
    "Tai moves fluidly and the others try to follow."
    tai "Tai's the best!"
    "Seb almost loses his balance."
    seb "Huh?"
    tai "You got to say it, friend."
    "You hear a few of the Islanders repeat it."

    # CHOICE
    menu:
        thought "Tai's the..."
        "Best!":
            $ s3_mc.like("Tai")
            tai "Aw, you're making me blush."
        "Worst ":
            $ s3_mc.dislike("Tai")
            tai "Oof, my feelings..."
        "Hottest...":
            $ s3_mc.like("Tai")
            tai "The sun's not even high in the sky, yet!"
            "He flashes a cheeky wink at you."
            thought "He knows what I mean..."
            if s3e5p2_waterfall_bits:
                $ s3_mc.dislike(s3_mc.current_partner)
                tai "Think we need another waterfall to cool down with, [s3_name]?"
                "You blush as he flashes you a wink."
                thought "That cheeky sod!"
                "You see [s3_mc.current_partner]'s smile drop."

    "Tai stands on one leg. The others follow shakily."
    "You and the other follow his lead."
    thought "Time to centre myself."
    "You focus on a spot a little way in front of you, on the ground."
    "Next to you, Miki wobbles before falling over."
    miki "Agh!"
    miki "How is balancing so hard?"
    "Ciaran's body sways."
    ciaran "I'm rubbish at it..."
    "Iona seems perfectly posed."
    iona "I'd be pretty rubbish at climbing if I couldn't balance."
    iona "Don't get why you're all struggling so much!"
    tai "Alright, next phrase..."
    tai "Tai's got the cutest bum here!"
    elladine "I thought these were meant to be inspirational?"
    tai "They are! To me, anyway."
    seb "Tai's got the cutest bum here!"
    "The others look at Seb."
    seb "What? He does. I can appreciate that."

    # CHOICE
    menu:
        thought "Does Tai have the cutest bum here?"
        "Repeat what he said":
            $ s3_mc.like("Tai")
            s3_mc "Tai has the cutest bum here!"
            tai "Just don't ask how many squats I have to do to keep it in shape..."
        "Say [s3_mc.current_partner] does":
            $ s3_mc.like(s3_mc.current_partner)
            s3_mc "[s3_mc.current_partner] has the cutest bum here!"
            if s3_mc.current_partner == "Bill":
                bill "As if there was any competition!"
            elif s3_mc.current_partner == "Camilo":
                camilo "As if there was any competition!"
            elif s3_mc.current_partner == "Harry":
                harry "As if there was any competition!"
            elif s3_mc.current_partner == "AJ":
                aj "As if there was any competition!"
        "Say that Yasmin does":
            $ s3_mc.like("Yasmin")
            s3_mc "Yasmin has the cutest bum here!"
            yasmin "As if it has anything on yours..."
            if s3_mc.bisexual:
                $ s3_mc.dislike(s3_mc.current_partner)
                "[s3_mc.current_partner] frowns at you."
        "Say Ciaran does":
            $ s3_mc.like("Ciaran")
            s3_mc "Ciaran has the cutest bum here!"
            ciaran "I was just thinking the same thing..."
            ciaran "About yours, I mean!"
            ciaran "Not about my own bum..."
            $ s3_mc.dislike(s3_mc.current_partner)
            "[s3_mc.current_partner] frowns at you."

    "Tai lunges forward. Bill and Nicky exchange a look before following suit."
    "As Bill gets low to the ground, he sits down."
    bill "Sod this. I don't go in for all this malarkey."
    bill "Just let me relax on the ground."
    tai "Bill's a big grouch!"
    "The others repeat the phrase. Bill smiles."
    tai "That wasn't the phrase."
    tai "I just wanted to say it. This is the phrase..."
    tai "Tai's an incredible and passionate lover!"

    $ pronouns(s3_mc.current_partner)

    # CHOICE
    menu:
        thought "Should I repeat what Tai said?"
        "Tai's an incredible lover!":
            $ s3_mc.like("Tai")
            tai "Don't forget passionate, too!"
            tai "I aim to please, after all."
            if s3e5p2_waterfall_bits:
                $ s3_mc.dislike(s3_mc.current_partner)
                tai "Don't you know it..."
        "Bill's a big grouch!":
            bill "Hey! That wasn't the line..."
            tai "Eh, works either way, friend."
        "I'd need to see it to believe it..." if s3e5p2_waterfall_bits == False:
            $ s3_mc.like("Tai")
            tai "It's not just something you see, [s3_name]."
            tai "It's a whole experience..."
            $ s3_mc.dislike(s3_mc.current_partner)
            "[s3_mc.current_partner] sighs. [his_her] face flushes red."
        "He sure is..." if s3e5p2_waterfall_bits:
            $ s3_mc.like("Tai")
            tai "How would you possibly know that?"
            "You shoot him a wink."
            $ s3_mc.dislike(s3_mc.current_partner)
            "[s3_mc.current_partner] sighs. [his_her] face flushes red."

    tai "That's it, everyone! Session over."
    yasmin "That wasn't like any tai chi I've done before."
    tai "I did say that at the start. It was Tai Chi."
    yasmin "Ooh..."

    $ leaving("yasmin")
    $ leaving("tai")

    "After everyone goes back to meandering around the lawn, [s3_mc.current_partner] comes up to you."

    if s3_mc.current_partner == "Bill":
        bill "Hey, babe, can we have a quick chat?"
    elif s3_mc.current_partner == "Camilo":
        camilo "Hey, babe, can we have a quick chat?"
    elif s3_mc.current_partner == "Harry":
        harry "Hey, babe, can we have a quick chat?"
    elif s3_mc.current_partner == "AJ":
        aj "Hey, babe, can we have a quick chat?"

    s3_mc "Sure!"
    "The two of you head to the loungers."

    scene s3-sun-loungers-day with dissolve
    $ new_scene()

    "You and [s3_mc.current_partner] sit on opposite loungers."
    s3_mc "So, what did you want to chat about?"
    "[s3_mc.current_partner] sighs."

    if s3_mc.current_partner == "Bill":
        bill "Well, it's just with the new Islanders coming in, a recoupling is obviously just around the corner."
        bill "What I really want to know, babe, is if you're still happy with me?"
        bill "Do you still see us as a couple?"
    elif s3_mc.current_partner == "Camilo":
        camilo "Well, it's just with the new Islanders coming in, a recoupling is obviously just around the corner."
        camilo "What I really want to know, babe, is if you're still happy with me?"
        camilo "Do you still see us as a couple?"
    elif s3_mc.current_partner == "Harry":
        harry "Well, it's just with the new Islanders coming in, a recoupling is obviously just around the corner."
        harry "What I really want to know, babe, is if you're still happy with me?"
        harry "Do you still see us as a couple?"
    elif s3_mc.current_partner == "AJ":
        aj "Well, it's just with the new Islanders coming in, a recoupling is obviously just around the corner."
        aj "What I really want to know, babe, is if you're still happy with me?"
        aj "Do you still see us as a couple?"

    # CHOICE
    menu:
        thought "Do I still see me and [s3_mc.current_partner] as a couple?"
        "Of course! We're in this together ":
            $ s3e6p1_break_up = False
            $ s3_mc.like(s3_mc.current_partner)
            "[s3_mc.current_partner] breathes a sigh of relief."
            if s3_mc.current_partner == "Bill":
                bill "That's really good to hear."
                bill "I was really nervous for a second there."
            elif s3_mc.current_partner == "Camilo":
                camilo "That's really good to hear."
                camilo "I was really nervous for a second there."
            elif s3_mc.current_partner == "Harry":
                harry "That's really good to hear."
                harry "I was really nervous for a second there."
            elif s3_mc.current_partner == "AJ":
                aj "That's really good to hear."
                aj "I was really nervous for a second there."
            s3_mc "No need, we're good!"
            "[s3_mc.current_partner] lets out a dramatic sigh of relief and breaks into a massive grin."
        "Actually, no, I don't want to be with you":
            $ s3_mc.dislike(s3_mc.current_partner)
            if s3_mc.current_partner == "Bill":
                $ s3_like_bill = False
                bill "Oh. OK."
                "[s3_mc.current_partner] looks away and bites [his_her] lip."
                bill "I'm sorry, but, I, um..."
                bill "I need to fill my water bottle up."
                bill "Thanks for the chat, [s3_name]."
                $ leaving("bill")
            elif s3_mc.current_partner == "Camilo":
                $ s3_like_camilo = False
                camilo "Oh. OK."
                "[s3_mc.current_partner] looks away and bites [his_her] lip."
                camilo "I'm sorry, but, I, um..."
                camilo "I need to fill my water bottle up."
                camilo "Thanks for the chat, [s3_name]."
                $ leaving("camilo")
            elif s3_mc.current_partner == "Harry":
                $ s3_like_harry = False
                harry "Oh. OK."
                "[s3_mc.current_partner] looks away and bites [his_her] lip."
                harry "I'm sorry, but, I, um..."
                harry "I need to fill my water bottle up."
                harry "Thanks for the chat, [s3_name]."
                $ leaving("harry")
            elif s3_mc.current_partner == "AJ":
                $ s3_like_aj = False
                aj "Oh. OK."
                "[s3_mc.current_partner] looks away and bites [his_her] lip."
                aj "I'm sorry, but, I, um..."
                aj "I need to fill my water bottle up."
                aj "Thanks for the chat, [s3_name]."
                $ leaving("aj")
            "[he_she!c] gets up and leaves you still lying on a lounger. You close your eyes."
        "It's a bit early for that...":
            $ s3_mc.dislike(s3_mc.current_partner)
            if s3_mc.current_partner == "Bill":
                bill "Oh. OK."
                "[s3_mc.current_partner] looks away and bites [his_her] lip."
                bill "I'm sorry, but, I, um..."
                bill "I need to fill my water bottle up."
                bill "Thanks for the chat, [s3_name]."
                $ leaving("bill")
            elif s3_mc.current_partner == "Camilo":
                camilo "Oh. OK."
                "[s3_mc.current_partner] looks away and bites [his_her] lip."
                camilo "I'm sorry, but, I, um..."
                camilo "I need to fill my water bottle up."
                camilo "Thanks for the chat, [s3_name]."
                $ leaving("camilo")
            elif s3_mc.current_partner == "Harry":
                harry "Oh. OK."
                "[s3_mc.current_partner] looks away and bites [his_her] lip."
                harry "I'm sorry, but, I, um..."
                harry "I need to fill my water bottle up."
                harry "Thanks for the chat, [s3_name]."
                $ leaving("harry")
            elif s3_mc.current_partner == "AJ":
                aj "Oh. OK."
                "[s3_mc.current_partner] looks away and bites [his_her] lip."
                aj "I'm sorry, but, I, um..."
                aj "I need to fill my water bottle up."
                aj "Thanks for the chat, [s3_name]."
                $ leaving("aj")
            "[he_she!c] gets up and leaves you still lying on a lounger. You close your eyes."

    if s3e6p1_break_up == False:
        if s3_mc.current_partner == "Bill":
            s3_mc "I've been thinking about what you told me the other day about your grandad."
            bill "Yeah. I love that geezer."
            s3_mc "It was so sweet. I wanna hear about the rest of your family."
            bill "Sure thing. What do you want to know?"

            # CHOICE
            menu:
                thought "What do I want to know about Bill's family? (you can ask all questions)"
                "Tell me about your siblings":
                    bill "Got two, a brother and a sister."
                    "He smiles with real warmth."
                    bill "My big sister Leanne's in construction, she's a brickie."
                    bill "And my brother Paul broke the mould a bit. He works at the council."
                    bill "In the planning department."
                "Tell me about your parents":
                    bill "Mum and dad are still together. He's a plumber, she used to work in a call centre but packed it in a few years back."
                    bill "She runs a florist's now."
                    s3_mc "Oh, that's cool!"
                    bill "Yeah. She knows exactly what she wants and she always sticks to her guns."
                    s3_mc "Reminds me of someone..."
                "Tell me about your aunts and uncles":
                    bill "I've got two aunts and two uncles. We don't see the ones on my dad's side much because they live in Australia. "
                    bill "On my mum's side, they're both electricians in Coventry."
                "Tell me about your grandparents":
                    bill "It's actually just my grandad left now."
                    s3_mc "Oh, I'm sorry to hear that."
                    "He shrugs."
                    bill "Just part of life, innit. They died before I was born."

            s3_mc "So, you're a very... buildery family."
            bill "Yup. We joke that we could build a whole house between us."
            s3_mc "And Paul can help you get planning permission!"
            "Bill chuckles."
            bill "So what's your family like?"

            # CHOICE
            menu:
                thought "My family..."
                "Is more the creative kind":
                    s3_mc "We're not the most practical bunch."
                    bill "Well, that's alright."
                    bill "Takes all sorts, doesn't it?"
                    bill "I bet there's loads of stuff your family could teach mine."
                "Are pretty average":
                    s3_mc "I don't know about a house, but they could probably manage a shed."
                    bill "Well, that's alright. My family is a bit ridiculous."
                    bill "Anyway, putting up a shed isn't that simple."
                    bill "First, you've got to decide whether your base is going to be treated wood on hardcore, concrete on sand, concrete on hardcore..."
                    bill "And then you..."
                    s3_mc "OK, OK, I get the picture!"
                "Are a lot like yours":
                    s3_mc "Oh? Maybe we should have a competition."
                    s3_mc "A house-building competition!"
                    s3_mc "Two plots of land and a year to build the best houses we can!"
                    bill "...Or I was thinking we could do a pub quiz."
                    bill "Unless you've got two spare pieces of land lying around..."
                    s3_mc "Oh... yeah. I don't."

            bill "So do you think our families will get to meet one day?"

            # CHOICE
            menu:
                thought "Do I think my family will get to meet Bill's?"
                "Maybe at the final":
                    bill "Hah, yeah, maybe they'll meet when we win!"
                    s3_mc "That'd be nice."
                "Maybe at the wedding, ha-ha-ha":
                    bill "You've been thinking about that?"
                    s3_mc "No... Just a joke..."
                    bill "Oh, yeah, I knew that."
                "Who knows?":
                    "Bill smiles."
                    bill "Yeah. There's no telling what could happen in the future."
                    bill "I like being here now, with you."

            "Bill reaches out to take your hand in his."
            "He squeezes your hand gently."
            "He looks down at his water bottle."
            bill "I need to fill my water bottle up."
            bill "Thanks for the chat, [s3_name]."
            "He gets up and leaves you still lying on a lounger. You close your eyes."

            $ leaving("bill")
        elif s3_mc.current_partner == "Harry":
            "Harry puts his arms around you. They're strong and lean. His bright, citrusy smell surrounds you."

            # CHOICE
            menu:
                thought "Harry is really close..."
                "Blow a raspberry on his neck":
                    # NEED TO FILL
                    "EMPTY"
                "Tell him to kiss your neck":
                    "He needs no encouragement. His lips softly brush your skin."
                    "A moan of pleasure escapes you, and you run your fingers through his dark hair."
                    "He keeps kissing your neck, and trails his lips across your skin to your mouth."
                    "You start kissing, slow and sweet. Your bodies press together so you can no longer tell where you end and he begins."
                    "When you pull away, you're in a daze."
                "Kiss him on the lips":
                    "Your hands find his chin and you him into you."
                    "You start kissing, slow and sweet. Your bodies press together so you can no longer tell where you end and he begins."
                    "When you pull away, you're in a daze."

            "You cuddle for a bit, and for a moment the world fades away and all you can feel is the rhythm of his breathing."
            "Harry looks around."
            harry "Isn't this place amazing? They're really spoiling us."
            harry "I'd love to own a house like the villa one day."
            s3_mc "It'd be nice, but where would you get the money?"
            harry "Oh, I'm going to be rich. For sure."

            # CHOICE
            menu:
                thought "Harry's convinced he's going to be rich..."
                "Being rich isn't everything":
                    # NEED TO FILL
                    "EMPTY"
                "Will you share it with me?":
                    harry "Yeah, course! What good is being wealthy if you can't spread it around?"
                    s3_mc "Thank you, but where are you getting this money?"
                "What makes you so sure?":
                    "He waves a hand casually."
                    harry "Becoming rich is easy. You've just got to wake up early, go with your gut and stick to your guns."
                    thought "Does he really just think that's all there is to it?"
                    harry "Oh, and you need a killer idea."
                    s3_mc "And have you got a killer idea?"

            harry "Mate, I've got loads of ideas for startups and apps."
            harry "FullFury, Talkie-Walkies, Bookrub..."

            # CHOICE
            menu:
                thought "Which idea do I want to know about?"
                "FullFury":
                    harry "Well, you know I was telling you about FuryStone?"
                    s3_mc "Yeah, the card game."
                    harry "I want to provide a coaching service for it. So the app would have articles and tutorials, but you could also hire a coach so you can improve."
                    harry "You share your screen with them and they'd walk you through plays and strategies."
                    s3_mc "Do you think people would really pay for that?"
                    harry "Definitely. I mean, I would, so I assume other people would too."
                "Talkie-Walkies":
                    harry "The idea is that it's an app for dog-walkers."
                    harry "They can communicate with you through the app, and it draws a GPS map of their route in real time."
                    harry "Also, they'd be able to upload pictures of your dog having fun."
                    harry "And there'd be a button they can press that tells you when your dog pooped."
                    s3_mc "Is the poop button really necessary?"
                    harry "The app was originally just a cartoon dog that did a poop when you pressed a button."
                    harry "The other stuff got added as we talked more about it."
                "Bookrub":
                    harry "I watch a lot of professional poker, and at big tournaments they have these people that come and give the players massages."
                    harry "I thought it'd be an amazing idea for students who have to spend all day hunched over in the library."
                    harry "So the app lets you hire a student masseur to come to the library and massage you."
                    s3_mc "I'm not sure people want to be massaged in the library."
                    harry "My market research suggested otherwise."
                    s3_mc "And who did you ask?"
                    harry "Me, and my survey said... I'd like it."

            # CHOICE
            menu:
                thought "Sounds..."
                "Like a bad idea":
                    # NEED TO FILL
                    "EMPTY"
                "Like a great idea":
                    harry "What can I say? I'm a genius."
                    harry "But being with you was definitely the best idea I've ever had."
                    harry "New app idea. I call it '[s3_name]'. But maybe with a vowel missing or something."
                    s3_mc "How does it work?"
                    harry "You push a button and all your dreams come true."
                    s3_mc "You're such a melt Harry"
                    "He laughs and draws you into his arms, squeezing you tight."

            "He looks down at his water bottle."
            harry "I need to fill my water bottle up."
            harry "Thanks for the chat, [s3_name]."
            "He gets up and leaves you still lying on a lounger. You close your eyes."

            $ leaving("harry")

        elif s3_mc.current_partner == "Camilo":
            "Camilo is looking very tickle-able all of a sudden."
            thought "I want to tickle him. Better see if he's OK with it first, though."
            s3_mc "How do you feel about tickling, babe?"
            camilo "I love it. There's one spot on my body that's proper ticklish."
            camilo "You're welcome to try and find it..."

            # CHOICE
            menu:
                thought "What's my plan of attack?"
                "Go for his armpits":
                    # NEED TO FILL
                    "EMPTY"
                "Go for the back of his legs":
                    # NEED TO FILL
                    "EMPTY"
                "Go for his sides":
                    "You dart in, pretending to aim for his legs. When he tries to stop you, you twist out of his grip and start tickling his sides mercilessly."
                    "Camilo makes a buzzer sound."
                    camilo "Sorry, that's not the right...haha...the right...hahaha!"
                    "He collapses into a fit of giggles as you keep tickling him."
                    s3_mc "Looks like you have more than one ticklish spot, mister."
                    "Camilo recovers, breathing heavily. He grins at you."
                    camilo "You've got some good moves, [s3_name]."

            camilo "Hey, you might be pretty good at BJJ."
            s3_mc "I might be good at what?"
            camilo "No no! BJJ! Two Js! Brazilian jiu jitsu."
            s3_mc "Maybe you should teach me some real moves one day."
            camilo "For sure, if you want."
            camilo "There's only one tiny thing..."
            s3_mc "What's that?"
            camilo "It's basically impossible to talk about jiu jitsu without it coming across as sexual..."

            # CHOICE
            menu:
                thought "Camilo says it's impossible to talk about BJJ without it sounding sexual..."
                "For example?":
                    # NEED TO FILL
                    "EMPTY"
                "I bet it's just you making it sexual":
                    # NEED TO FILL
                    "EMPTY"
                "Isn't that good for flirting?":
                    s3_mc "You're not gonna tell me that's a problem for you?"
                    s3_mc "I bet you'd have no trouble turning it into a bit of flirting."
                    camilo "Sometimes, yeah."

            camilo "Sometimes I'm like “here's how to mount your opponent” and they back right off!"
            s3_mc "No way that's a real move!"
            camilo "See?"
            camilo "I haven't even got to the rear naked hold yet!"
            s3_mc "OK, I get it!"
            s3_mc "But I still want you to teach me sometime."
            camilo "Well, at least you know what you're getting yourself into now, innit."
            camilo "You can't say I didn't warn you!"
            camilo "Maybe we can find a quiet spot and I'll go through some moves with you."
            s3_mc "That rear naked whatever sounds good."
            "He laughs, warm and rich."
            camilo "You're the boss!"

            "He looks down at his water bottle."
            camilo "I need to fill my water bottle up."
            camilo "Thanks for the chat, [s3_name]."
            "He gets up and leaves you still lying on a lounger. You close your eyes."

            $ leaving("camilo")
        elif s3_mc.current_partner == "AJ":
            aj "Can I be honest with you, [s3_name]?"

            # CHOICE
            menu:
                thought "AJ wants to be honest with me..."
                "No, please, lie to me, I can't handle the truth":
                    # NEED TO FILL
                    "EMPTY"
                "Sure, what's up?":
                    aj "Well..."
                    aj "I used to really struggle with getting bored when I was in relationships before, like, in real life."
                    aj "But you know what?"
                    s3_mc "What?"
                    aj "I don't think I could ever get bored of you."
                "Honesty is the best policy":
                    aj "Agreed."
                    aj "I used to really struggle with getting bored when I was in relationships before, like, in real life."
                    aj "But you know what?"
                    s3_mc "What?"
                    aj "I don't think I could ever get bored of you."

            "AJ smiles at you."
            aj "Sorry, I know that was really random, but... yeah. I don't think I'd ever, like, not want to hang out with you."

            # CHOICE
            menu:
                thought "I should..."
                "Call her out":
                    # NEED TO FILL
                    "EMPTY"
                "Kiss her":
                    s3_mc "Oh really?"
                    "You lean towards her and kiss her on the lips."
                    "She pulls you closer, savouring the moment."
                    "It feels as if time slips away from you both."
                    aj "Yep."
                    aj "Really."
                    aj "I rest my case."
                    aj "I could do that all day."
                "Tell her I'd never get bored either!":
                    aj "Good."

            "AJ clasps her hands together enthusiastically."
            aj "Ooh!"
            aj "I can't wait to introduce you to all my hockey pals."

            # CHOICE
            menu:
                thought "AJ wants me to meet her hockey team mates!"
                "I'll be a bit nervous":
                    # NEED TO FILL
                    "EMPTY"
                "Hmm... what are they like?":
                    # NEED TO FILL
                    "EMPTY"
                "That sounds like fun!":
                    aj "Yeah! It will be."

            aj "They'd, like, one hundred perfect love you."
            s3_mc "I would hope so."
            aj "Oh, for sure."
            aj "It'll be weird for them seeing me, like, actually being cool and settled in a relationship."
            aj "What were you like with dating, back at home?"

            # CHOICE
            menu:
                thought "In relationships, I'm..."
                "A slow burner":
                    # NEED TO FILL
                    "EMPTY"
                "Pure chaos":
                    # NEED TO FILL
                    "EMPTY"
                "Really loyal":
                    aj "Aw, that's so cute!"

            aj "I was always jumping from one relationship to the next."
            aj "That's actually one of the reasons I came on this show. To try and find someone to settle down with."

            "She looks down at her water bottle."
            aj "I need to fill my water bottle up."
            aj "Thanks for the chat, [s3_mc]."
            "She gets up and leaves you still lying on a lounger. You close your eyes."
            $ leaving("aj")

    "You lie there for a while, soaking in the sun."
    "Then you suddenly feel cooler."
    thought "Huh? Did the sun go in?"
    "You open your eyes to see Ciaran, whose broad frame has blocked out the sun."
    ciaran "Alright, [s3_name]?"
    s3_mc "Hey! What're you up to?"
    ciaran "Just going for a walk."
    ciaran "I usually go for two or three a day with my dog."
    ciaran "Guess I'm feeling a bit restless with all this sitting around."

    if s3e5p3_yasmin_help == "Ciaran":
        $ s3_mc.like("Ciaran")
        ciaran "I also felt like catching you on your own..."
        ciaran "Yasmin had a chat with me last night."
        s3_mc "Oh yeah?"
        ciaran "[s3_name], you must know by now that."
        ciaran "I have a crush on you. There's no need to try and win me over."
        ciaran "But I appreciate the effort!"
        s3_mc "What did Yasmin say?"
        ciaran "Oh, that she thinks we'd be a great couple... because we both have cute bums."

        # CHOICE
        menu:
            thought "Yasmin thinks Ciaran and I have cute bums..."
            "Her bum ain't bad either":
                # NEED TO FILL
                "EMPTY"
            "She's not wrong":
                ciaran "Aw, thanks!"
            "You definitely do":
                ciaran "Aw, thanks!"

        ciaran "Anyway, yeah. Thanks for asking her to do that."
        ciaran "That was really nice of you."
        ciaran "You're a really sweet girl."
        ciaran "Well, I'm off on my walk."

    "As he starts to turn away, his eyes light up, and he pauses."
    ciaran "Oh! You feel like joining me?"
    ciaran "It'd be nice to spend some time with you. I can show you some highlights of the place."
    s3_mc "Highlights of the Villa?"
    ciaran "You'll see what I mean. What do you say?"

    # CHOICE
    menu:
        thought "Should I go for a walk around the Villa with Ciaran?"
        "That sounds like fun, let's go!":
            $ s3e6p1_walk = True
            $ s3_mc.like("Ciaran")
            call s3e6p1_walk from _call_s3e6p1_walk
        "Hmm, I'm enjoying lying in the sun":
            ciaran "Aw, OK. No problem."
            ciaran "I'll have fun walking around on my own."
            ciaran "Maybe Tai would want to join me. He seems a bit restless too..."
            ciaran "Anyway, see you, [s3_name]!"
            "He walks off, and turns to wave to you for a second."
            "You settle back to the sun, but just as you're about to doze off, your phone pings loudly."
            thought "Ugh, why?"
            thought "I was so comfy..."

    text "[s3_name], please make your way to the bedroom. Don't say anything to any of the other Islanders. #mumstheword #secretservice"
    thought "What's this about?"

    "Tai... Chi..."
    "Nope. Still not getting it."
    "Oh!"
    "I get it. Chi, as in, like Tai's chi-seled abs. Of course..."

    if s3e6p1_walk:
        "I don't know about you lot, but I've now got my next holiday pegged for Waterford after that tour."
        "Going to get me some fine blaas."
        "Or at least I would if I got any holiday."

    scene sand with dissolve
    $ on_screen = []

    "Coming up!"
    "The girls are off on a secret mission..."
    aj "Oh, sweet! I'd make a cool spy."
    $ leaving("aj")
    "But will [s3_name] be up to the task?"
    s3_mc "I'll get to show off my powers of persuasion..."
    harry "Wait."
    nicky "I knew it!"
    "Stay tuned to find out..."

    jump s3e6p2

label s3e6p1_walk:
    ciaran "Great! Let me help you up."
    "He extends an arm, you use it to pull yourself off the lounger."
    "You take his hand and he easily lifts you from the lounger."

    scene s3-poolside-day with dissolve
    $ new_scene()

    "You walk around the pool."
    ciaran "Let's pretend the Villa's my hometown for a while. I'll be your tour guide."
    s3_mc "Huh?"
    ciaran "Just watch..."
    ciaran "The River Suir is looking fresh today."
    "He points to the floating bean bag."
    ciaran "Shame someone dumped another trolley in it."

    # CHOICE
    menu:
        thought "The River Suir..."
        "It really is lovely":
            s3_mc "The water's so clean. Almost as if it's chemically treated!"
            ciaran "Yeah, I've never seen it so clear."
            ciaran "Maybe the two of us should takes plunge later..."
        "What are you going on about?":
            s3_mc "This is the pool, not a river..."
            ciaran "Not in here right now."
            "He taps his head."
            ciaran "Use your imagination, too."
        "That's why I never get a shopping trolley!":
            s3_mc "Every time I have to use a basket and then my arms ache and they're never big enough!"
            ciaran "Aye, it's a real problem, for sure."
            ciaran "They once dredged the river and found 20 sunk in the mud."
            ciaran "They still had the euros in them and everything."

    "He lets out a contented sigh."
    ciaran "I love going for walks, and Waterford has got some real charm."
    "He turns to you."
    ciaran "Where'd you like to go next?"

    $ s3e6p1_walking = True

    while s3e6p1_walking: 
        # CHOICE
        menu:
            thought "I'd like to go to..."
            "Your local takeaway":
                ciaran "Great idea! You're going to love this place."
                ciaran "I go to it after every night out."
                ciaran "It has the best blaas!"
                s3_mc "The best what?"
                ciaran "Blaas! They're like a bread roll."
                ciaran "They're a local delicacy."
                call s3e6p1_walk_takeaway from _call_s3e6p1_walk_takeaway
            "Where you work":
                ciaran "I'll take you to the nightclub"
                ciaran "It's way safer than the bingo hall."
                ciaran "Some of the older fold get a bit... passionate for the game."
                ciaran "I remember one proper handbags at dawn type situation..."
                ciaran "I discovered there's more than one way to take someone down with a zimmer frame that day..."
                call s3e6p1_walk_work from _call_s3e6p1_walk_work
            "Wherever has the best view":
                ciaran "Oh, that's an easy one."
                ciaran "It's a bit of a mission to climb, but you're fit. You'll manage it fine I reckon."
                call s3e6p1_walk_view from _call_s3e6p1_walk_view
            "The Villa, I'm finished now":
                ciaran "Fair does."
                $ s3e6p1_walking = False

    scene s3-sun-loungers-day with dissolve
    $ new_scene()

    "You and Ciaran arrive back at the loungers."
    ciaran "So, how'd you find Waterford?"

    # CHOICE
    menu:
        thought "Waterford..."
        "Isn't that great ":
            # NEED TO FILL
            "EMPTY"
        "Was amazing to see":
            s3_mc "Thanks for showing me around."
            ciaran "Of course, any time."
            ciaran "Maybe one day it might even be in person..."
        "Would be better in person...":
            ciaran "It'd be grand to take you around the real place someday..."

    ciaran "Thanks for playing along with this, hey."
    ciaran "I know it's a bit silly, but it helps to keep me from getting homesick."
    ciaran "So it means a lot."
    ciaran "And I feel, like... closer to you now for sure."
    ciaran "You've seen a side of me now that no one else here has."
    "Ciaran glances down at his feet, then back at you."

    if s3_like_ciaran == False:
        ciaran "And, um, how'd you find your guide?"
        ciaran "Would you maybe try one of his other tours?"
        # CHOICE
        menu:
            thought "Am I interested in Ciaran?"
            "I am after this tour":
                $ s3_like_ciaran = True
                $ s3_mc.like("Ciaran")
                # NEED TO FILL
                "EMPTY"
            "Let's visit somewhere exotic next time":
                # NEED TO FILL
                "EMPTY"
            "I'm afraid not...":
                ciaran "Ah, that's OK. I understand."
                ciaran "Still, I hope you enjoyed this time together as a friend."
    else:
        ciaran "Would you leave your tour guide a five star review?"
        # CHOICE
        menu:
            thought "My local guide..."
            "Could work a little harder ":
                # NEED TO FILL
                "EMPTY"
            "Was fit and charming":
                s3_mc "What more could a girl ask for?"
                s3_mc "Except maybe a piggyback next time?"
                ciaran "Noted."
            "Deserves a tip. Do you accept kisses?":
                $ s3_mc.like("Ciaran")
                ciaran "Not normally, but from you... of course."
        ciaran "Hey, [s3_name]. Is it OK if I ask you a question?"
        # CHOICE
        menu:
            thought "Ciaran wants to ask me a question."
            "You just did!":
                # NEED TO FILL
                "EMPTY"
            "Sure":
                ciaran "Thanks."
            "Depends what it is":
                ciaran "Nothing bad..."
                s3_mc "Go for it."
        ciaran "Do you like me?"
        s3_mc "Sure, Ciaran. You're great."
        ciaran "I mean, do you like like me?"
        # CHOICE
        menu:
            thought "Do I like like Ciaran?"
            "Duh":
                $ s3_mc.like("Ciaran")
                ciaran "Oh good. Phew!"
            "Are we in the school playground?":
                ciaran "I didn't know how else to put it..."
            "I like like like you":
                $ s3_mc.like("Ciaran")
                ciaran "Oh, wow! That's even better!"
        ciaran "Sorry. I'm not good at this stuff. I had to ask."
        ciaran "I've... never had a girlfriend before."
        ciaran "Not that you're my girlfriend! I mean... I've misread signs before."
        # CHOICE
        menu:
            thought "Ciaran's never had a relationship..."
            "What about a fling?":
                s3_mc "Ever had one of those?"
                ciaran "I don't know. What's a fling?"
                s3_mc "Like, a little thing with a person that lasts for like a few days."
                ciaran "And then you break up?"
                s3_mc "No, then it just sort of ends at the right moment."
                "He thinks about it for a moment."
                ciaran "A thing? In an old boat?"
                s3_mc "Huh?"
                ciaran "Do old-timey boats count? For flings? If it was only three times?"
                s3_mc "Um... Yeah? I guess so."
                ciaran "Great. Then I've had flings."
                s3_mc "You need to give me more than that."
                ciaran "There's like an old boat in Waterford, like, from ancient times. Like a Viking thing."
                ciaran "I had a thing that happened there a few times in a row."
                s3_mc "A thing? In an old boat?"
                ciaran "Yeah. We got caught by security one time and then after that we never saw one another again."
                ciaran "So to answer your question..."
            "I could be your first":
                ciaran "I... don't know what to say to that..."
                ciaran "I mean, how long of a time period usually, do people usually..."
                s3_mc "Relax, Ciaran. Deep breaths."
                ciaran "OK. Sorry. You caught me off guard with that."
            "That's not a bad thing":
                s3_mc "So you've never found anyone good enough for you. That's OK."
                s3_mc "A girl would have to be pretty special to keep up with you."
                "He gives you a shy smile."
                ciaran "Yeah... really special."
        ciaran "I've been with girls before, but it's never been serious."
        ciaran "One night stands mostly."
        ciaran "I quickly realised I'm not interested in that, though."
        s3_mc "You're not?"
        ciaran "No. Each to their own, but that kind of thing is so... awkward."
        ciaran "You're kissing, you're touching, one of you burps."
        ciaran "If you don't know each other, it's weird and it kills the moment."
        ciaran "I want the kind of relationship where we'd laugh about something like that."
        ciaran "But I always mess things up before they get that far."
        ciaran "Working at the club, loads of girls try it on. Usually I ignore it because I'm just trying to work, but sometimes you just give in."
        ciaran "I had this one horrible experience where I found out this girl only hooked up with me because she thought it would get her mates free drinks in the club."
        s3_mc "That's horrible."
        ciaran "Yeah."
        "He smiles at you."
        ciaran "Thanks. I've never told anyone that before."
        "You look around you and realise it's just the two of you."
        ciaran "You know, I think this is the only time we've been alone since I got here."
        s3_mc "We should make the most of it."
        ciaran "Yeah? How so?"
        # CHOICE
        menu:
            thought "What should Ciaran and I do?"
            "Cuddle":
                # NEED TO FILL
                "EMPTY"
            "Talk some more":
                # NEED TO FILL
                "EMPTY"
            "Kiss":
                s3_mc "I have an idea."
                "You bring your hand up to his cheek, feeling the soft, fine hair there."
                "He smiles at you, his green eyes shining."
                "You pull him forwards so his lips meet yours."
                "The kiss is soft and innocent. You put your hand on his neck, and feel his pulse race under your fingertips."
                "He tastes like mind and smells like shampoo."
                "When you pull away, he's grinning at you."
                ciaran "That was incredible."
                ciaran "I've never kissed anyone like that."
                ciaran "So softly."
        ciaran "I could have spent hours there."
        s3_mc "We've got all the time in the world. Why rush?"
        ciaran "Exactly."

    "Ciaran smiles at you, his eyes bright."
    ciaran "I'm headed for the gym. See you later, OK?"
    "You smile back at him then head back to the loungers."

    scene s3-sun-loungers-day with dissolve
    $ new_scene()

    "You lie in the sun for a while, thinking of your tour of 'Waterford', when your phone suddenly goes off."

    return

label s3e6p1_walk_takeaway:
    scene s3-kitchen-day with dissolve
    $ new_scene()

    "Ciaran takes you to the kitchen. Nicky stands by the sink doing the washing up. He nods at the two of you as you enter."
    nicky "Alright, out for a little stroll?"
    ciaran "Hey, Beb, I'll take my usual."
    nicky "Eh?"
    "Ciaran turns to you."
    ciaran "This is Beb's Blaas. Best bakery from here to Cork."
    ciaran "The owner's a mate of mine."
    ciaran "She always gives me a double portion of chips."
    nicky "What's going on?"

    # CHOICE
    menu:
        thought "I'll..."
        "Take a chip blaa to go":
            $ s3_mc.like("Ciaran")
            s3_mc "And don't skimp on the ketchup"
            ciaran "Good choice!"
        "Explain all this later":
            s3_mc "Just go along with it."
            nicky "OK..."
        "Have what he's having":
            $ s3_mc.like("Ciaran")
            ciaran "The Overloaded?!"
            ciaran "You have fine taste, [s3_name]."

    "Nicky nods slowly."
    nicky "Right. Two blaas coming up."
    "He pauses."
    nicky "What the hell is a 'blaas'?"
    ciaran "It's like a bread roll."
    s3_mc "...but better."
    nicky "Oh... in that case."
    "He reaches into a cabinet and pulls out a bag of bread rolls."
    nicky "Here you go. Some blaas."
    "Ciaran takes one and gives it a gentle squeeze."
    ciaran "Hmm, a bit firm."
    nicky "Is that a problem?"
    ciaran "I prefer my blaas a little softer is all."
    "Nicky frowns."
    nicky "Nah, if they're too soft the egg will fall out."
    nicky "Don't want them to be too squishy."

    # CHOICE
    menu:
        thought "Should they be firm or squishy?"
        "It's all about firmness":
            $ s3_mc.like("Nicky")
            $ s3_mc.dislike("Ciaran")
            s3_mc "Handfeel is important..."
            s3_mc "Um, when it comes to bread."
        "You want them soft":
            $ s3_mc.like("Nicky")
            $ s3_mc.dislike("Ciaran")
            s3_mc "Handfeel is important..."
            s3_mc "Um, when it comes to bread."
        "We're still talking about bread?":
            ciaran "Of course."
            nicky "I don't know anymore. This whole thing is odd..."

    "Ciaran goes to leave."
    nicky "Wait up, man."
    ciaran "Huh?"
    nicky "Don't forget your extra portion of chips."
    "He chucks two bags of salt and vinegar crisps on the counter."
    ciaran "Oh, that's right class of you."
    nicky "Yeah, yeah... Right, I'm out of here before this gets any weirder."
    "Ciaran takes a bite of the pretend blaa."
    ciaran "As good as always."
    ciaran "Where'd you like to go next?"

    return

label s3e6p1_walk_work:
    scene s3-lounge with dissolve
    $ new_scene()

    "As you enter the lounge, Ciaran turns and stops you."
    ciaran "This is the club I do security for."

    # CHOICE
    menu:
        thought "This club is a bit..."
        "Basic for me":
            # NEED TO FILL
            "EMPTY"
        "Alternative...":
            # NEED TO FILL
            "EMPTY"
        "Homely feeling":
            ciaran "It feels that way to me sometimes, to be sure."
            ciaran "But that's just because I've worked here for so long."

    ciaran "I'm not sure where all these sofas have come from, though..."
    ciaran "Management can be a bit funny at times."
    "You go to walk past him, but he holds out his palm."
    ciaran "Sorry, miss, can I have your name?"
    s3_mc "Why'd you need my name?"
    ciaran "This is a pretty exclusive club."
    ciaran "Only the biggest names make it in."

    # CHOICE
    menu:
        thought "Ciaran says only celebrities make it into his club..."
        "I'm [s3_name]...":
            s3_mc "I should be on the list."
        "What celebrities live in Waterford?":
            ciaran "Hmm..."
            ciaran "Loads!"
            s3_mc "Name one."
            ciaran "Um, there's Bryce McFeather."
            s3_mc "Who's he?"
            ciaran "A local goose that's huge. Like, the biggest goose..."
            s3_mc "Uh-huh... Anyway, I'm [s3_name]."
        "Don't you know who I am?!":
            s3_mc "I'm [s3_name]!"
            s3_mc "Winner of Love Island."
            s3_mc "Owner of many cars and renowned A-star celeb!"
            "Ciaran's face flushes red."
            ciaran "Oh, um..."

    ciaran "[s3_name] from Love Island? The famous [s3_mc.job!l]?"
    ciaran "Step right in, ma'am!"

    # CHOICE
    menu:
        thought "Thanks, babe..."
        "Say nothing":
            # NEED TO FILL
            "EMPTY"
        "You're such a doll":
            "He winks at you."
        "Don't you need to pat me down?":
            ciaran "Oh yeah..."
            "He works his hands over your thighs, waist, and arms. His touch is gentle but firm."
            ciaran "You're clean."
            s3_mc "I can be dirty..."

    "You pretend to make a grand entrance."
    s3_mc "There's no one in here?"
    ciaran "Yeah... it's a bit early if I'm honest. We should come back later."
    ciaran "Where'd you like to go next?"

    return

label s3e6p1_walk_view:
    scene s3-roof-day with dissolve
    $ new_scene()

    "As you emerge onto the terrace, Ciaran leans against the door and lets out an exaggerated puff of air."
    ciaran "Phew, climbing Reginald's Tower is always a bit of a trek, but the view's worth it."
    "He gestures across the Villa."
    ciaran "Behold! The beauty that is Waterford."
    "You look around the Villa."

    # CHOICE
    menu:
        thought "Waterford's..."
        "Not all that":
            # NEED TO FILL
            "EMPTY"
        "Stunning ":
            ciaran "Aye, it is."
            ciaran "Some say it's too small or remote. But that's just the way I like it."
        "Really arid?":
            s3_mc "It looks more like a savannah."
            ciaran "Aye, it's true we've had an unseasonably hot summer, for sure."
            ciaran "For the first time on record, I'll add."

    s3_mc "So tell me, what's that over there?"
    "You point to a grove of trees in the distance."
    ciaran "Oh, that's County Kilkenny... we don't talk about them."
    ciaran "They always act like our rock belongs in their county."
    ciaran "Can you believe it?"
    s3_mc "What?"
    ciaran "Mount Misery. It's a rock that sits on the border."
    ciaran "People from Kilkenny always come and paint it with their colours."
    ciaran "So then we repaint it, and then they do it again!"
    "He dramatically shakes his fist at the trees."

    # CHOICE
    menu:
        thought "You really..."
        "Love your home, don't you?":
            "He smiles and his cheeks tinge red."
            ciaran "I do, and I'm not ashamed to say it."
            "He smiles at you."
        "Argue over a rock?":
            ciaran "Damn right we do. It's our rock."
            ciaran "We'll paint it whatever colours we like."
            ciaran "The only time we didn't argue over it was when we painted it rainbow for pride day after the gay marriage vote passed."
            ciaran "That was the one thing both counties agreed on."
            "He smiles at you."
        "Are a sweet lug, aren't you?":
            "His cheeks flush."

    ciaran "Come on, then. The tower will be closing soon. We should head back down."

    return

#########################################################################
## Episode 6, Part 2
#########################################################################
label s3e6p2:
    scene sand with dissolve
    $ on_screen = []

    show screen day_title(6, 2) with Pause(4)
    hide screen day_title with dissolve

    "Welcome back to Love Island, where [s3_name] is on the trail of a mystery."
    s3_mc "What's this about?"
    "She's been summoned to the bedroom, along with all the other girls."
    iona "Like we're spies or something?"
    $ leaving("iona")
    "That's exactly what it's like, Iona!"
    "But what could be so mysterious that you can't tell the boys about it...?"

    scene s3-bedroom-day with dissolve
    $ new_scene()

    "When you arrive in the bedroom, all the girls are waiting there."
    s3_mc "Did everyone get the same text?"
    genevieve "To meet here and not tell the boys?"
    yasmin "Yep."
    miki "I wonder what it all means?"
    genevieve "You don't think it's a new fella coming in?"
    s3_mc "You think so?"
    iona "No way. It's got to be a challenge. Like we're spies or something."
    aj "Oh, sweet! I'd make a cool spy."
    iona "AJ, spies have to be quiet and sneaky."
    aj "Yeah, but they also get to jump onto moving trains, and walk away from explosions and stuff."
    miki "Sounds like you're a pretty bad spy if stuff's exploding around you."
    aj "I never said I'd be a good spy. But I'd be a cool one!"

    # CHOICE
    menu:
        thought "Wait! That was my phone again..."
        "Listen to this, girls":
            elladine "Oh, yay!"
        "Everyone shut up and listen!":
            iona "Alright, alright."
        "Agents, here is your mission":
            iona "That's the spirit."

    iona "What does it say?"
    text "Girls, today you will be taking part in a top secret challenge. Between you, you must complete seven tasks, all without the boys realising that you're up to something. #pieanotherday #skyfallingforyou"
    elladine "I knew it! We are like secret agents!"
    aj "What are the challenges?"
    iona "It better not be more foot stuff."
    text "One of you must convince all the boys to jump in the pool at the same time."
    s3_mc "Me! Me!"
    aj "That's gonna be hilarious!"
    text "One of you must get Harry to rub sun cream on your back."
    iona "I can do that, no problem!"
    iona "It won't be the first time I've talked a guy into creaming me up."
    miki "Ew, what? Please don't call it that."
    text "One of you must sit in Camilo's lap and stay there for at least thirty seconds."
    miki "Is that all? That's easy!"
    elladine "Thirty seconds can be a really long time, babes."
    miki "I can do it. Just watch me."
    miki "I once took a bus from London to Edinburgh and rode on my boyfriend's lap the whole way."
    genevieve "That doesn't seem safe."
    miki "We were fine!"
    miki "He got feeling back in his legs, like, later that day. And it was super romantic."
    text "One of you must get Bill to motorboat you."
    "Elladine bursts out laughing."
    elladine "Oh, please let me do that one! That's too funny."
    "Miki leans close to you and whispers."
    miki "Would this be a bad time to ask what motorboat means?"

    # CHOICE
    menu:
        thought "Miki doesn't know what motorboating is..."
        "Honestly, neither do I":
            s3_mc "It doesn't have anything to do with actual boats, does it?"
            elladine "It's when you put your face in a girl's cleavage and go like this!"
            "She shakes her head from side to side, giggling the whole time."
        "Well, let me explain...":
            s3_mc "It's when you put your face in a girl's cleavage and go like this!"
            "You shake your head from side to side, making all the other girls collapse in giggles."
        "Me and Elladine can show you":
            elladine "Yeah, we can give you a demonstration! Come on, [s3_name]."
            "You bury your face in Elladine's cleavage and shake your head from side to side, making 'all the other girls collapse in giggles."

    miki "That's ridiculous."
    elladine "Yes. Which is why I wanna be the one who does it, just to see the look on Bill's face."
    s3_mc "Won't Nicky have something to say about that?"
    elladine "One of you will have to distract him or something."
    miki "What's the next task, then, [s3_name]?"
    text "One of you must get Nicky to say 'Enchanted Husband' out loud, without simply asking him to say it."
    aj "'Enchanted Husband'? What's that?"
    yasmin "It's my old band. So this task is basically designed by me."
    text "One of you must convince Ciaran and Tai to wrestle each other."
    aj "Mine!"
    aj "Honestly, both of those guys seem like they'd be really fun to wrestle with."
    text "One of you must convince Seb to wear your eyeliner."
    iona "Is that really a challenge? There's no way Seb hasn't already had an eyeliner phase."
    genevieve "Ooh, I want to do this one! I bet he'll look really nice."
    elladine "That's everything!"
    thought "Wow, I thought my task was good, but some of them sound even better!"
    thought "Maybe I should switch with one of the girls."
    thought "I'll get to show off my powers of persuasion..."
    thought "And maybe get a bit closer with the boys."

    # CHOICE
    menu:
        thought "Should I switch for a more exciting task?"
        "Yes please!":
            call s3e6p2_better_task from _call_s3e6p2_better_task
        "Nah":
            $ s3e6p2_task = "Pool"
            genevieve "Are you sure you're happy doing the pool one, [s3_name]?"
            s3_mc "Yeah, I'll just do the pool one."
            miki "Alright, if you're sure."

    aj "This is going to be a right laugh!"
    aj "We should all have codenames. Like... Agent Stallion. Or Agent Sparkles."
    miki "Ooh, yes! I wanna be..."
    miki "Agent Montano."
    miki "After the sneakiest telenovela villain ever."

    # CHOICE
    menu:
        thought "My condename will be..."
        "Agent Martinez":
            $ s3e6p2_agent_name = "Agent Martinez"
            "Miki gasps."
            miki "Vibing with the telenovela wavelength. Love it!"
            miki "That's perfect. So glamorous."
            iona "I love that you two have a theme going on already."
        "Agent Buckethead":
            $ s3e6p2_agent_name = "Agent Buckethead"
            miki "And your thing is you wear a bucket on your head?"
            s3_mc "I think that might make it a bit hard to do my challenge."
            s3_mc "It's more like, the boys can't read my face. I'm giving nothing away."
            iona "Ah, so it's a metaphorical bucket. Smart."
        "Agent FuryStone":
            $ s3e6p2_agent_name = "Agent FuryStone"
            s3_mc "Like that video game Harry likes?"
            s3_mc "I think it's a card game."
            iona "Either way, I like it."
        "This is silly":
            $ s3e6p2_agent_name = "Agent Serious Face"
            s3_mc "Can't we just take the challenge seriously for once? Please?"
            iona "Alright, Agent Serious Face."

    iona "Shall we head down to the daybeds? I have a feeling we'll find Harry there around about now."
    s3_mc "Good idea."
    elladine "Let's split off into groups. AJ and Miki, you're with me."
    elladine "Viv and Yasmin, you go with [s3_name] and Iona."
    yasmin "Sounds good to me."
    aj "Good luck, everyone!"
    "You lead Genevieve, Iona and Yasmin outside."

    
    call s3e6p2_nicky_task from _call_s3e6p2_nicky_task

    call s3e6p2_harry_task from _call_s3e6p2_harry_task

    call s3e6p2_seb_task from _call_s3e6p2_seb_task

    call s3e6p2_camilo_task from _call_s3e6p2_camilo_task

    call s3e6p2_ciaran_tai_task from _call_s3e6p2_ciaran_tai_task

    call s3e6p2_bill_task from _call_s3e6p2_bill_task

    call s3e6p2_pool_task from _call_s3e6p2_pool_task

    thought "Yes! We did it! We finished all our secret tasks!"
    nicky "Text!"
    "Nicky swims back over to the edge of the pool and reaches for his phone, which is lying in the grass."
    "He looks at the screen and gasps."
    nicky "I knew it!"
    camilo "What?"
    nicky "Listen!"
    text "Boys, it's time you know the truth. Earlier today, the girls were assigned a number of secret challenges involving you."
    text "Because they completed all the challenges successfully, the whole Villa will get a special reward tomorrow. #missionpossible #goteamgirls"
    harry "Is that why you've all been acting so weird today?"
    elladine "Yes!"

    if s3e6p2_task == "Pool":
        elladine "I didn't really want Bill to motorboat me!"
        bill "That... makes sense."
    elif s3e6p2_task == "Bill":
        iona "I didn't really want Harry to rub sun cream on me!"
        harry "That... makes sense."

    thought "She so did want to do that."

    if s3e6p2_switched == "Elladine":
        elladine "And there aren't any fire ants. I was just trying to get you all to jump in the pool."
    elif s3e6p2_switched == "Iona":
        iona "And there aren't any fire ants. I was just trying to get you all to jump in the pool."
    elif s3e6p2_switched == "Miki":
        miki "And there aren't any fire ants. I was just trying to get you all to jump in the pool."
    elif s3e6p2_switched == "Genevieve":
        genevieve "And there aren't any fire ants. I was just trying to get you all to jump in the pool."
    elif s3e6p2_switched == "AJ":
        aj "And there aren't any fire ants. I was just trying to get you all to jump in the pool."
    elif s3e6p2_switched == "Yasmin":
        yasmin "And there aren't any fire ants. I was just trying to get you all to jump in the pool."

    bill "Wait, so what was [s3_name]'s challenge?"

    if s3e6p2_task == "Pool":
        s3_mc "This! I had to get you all to jump in the pool."
        ciaran "So what you said just now..."
        s3_mc "Yeah, that was a trick. Sorry."
    elif s3e6p2_task == "Bill":
        s3_mc "I had to get you to motorboat me."
        s3_mc "I literally can't believe you didn't notice something was up."
        bill "I dunno. I just thought it was, like, classic [s3_name]."
        s3_mc "Motorboating is 'classic' [s3_name]? What does that even mean?"
        bill "I don't know! I didn't question it!"
        bill "You're very persuasive."
    elif s3e6p2_task == "Ciaran Tai":
        s3_mc "I had to get Ciaran and Tai to wrestle each other."
        tai "Oh, I see now."
        ciaran "Thanks for that! It was fun!"
        tai "It was the most fun."
        s3_mc "You're welcome."
    elif s3e6p2_task == "Camilo":
        s3_mc "I had to sit in Camilo's lap."
        camilo "Ohhh. Yeah, now that you say it, that does make sense."
        s3_mc "I can't believe you didn't realise something was up!"
        camilo "What can I say? You're too smooth, [s3_name], you're dangerous."
    elif s3e6p2_task == "Harry":
        s3_mc "I had to get Harry to rub sun cream on my back."
        harry "Oh! I see now."
        s3_mc "I can't believe you didn't catch on."
        harry "Hey, I was having fun! I wasn't about to question it."
        harry "Can you really blame me?"
    elif s3e6p2_task == "Seb":
        s3_mc "I had to get Seb to wear my eyeliner."
        genevieve "For the record, I think that was a good idea anyway. I really like it on him."
        seb "Thanks!"

    nicky "I totally knew it! I knew you were up to something!"
    s3_mc "Stop saying you knew it! You blatantly didn't, or you would've said something!"
    nicky "I didn't want to spoil your fun."
    elladine "Sure, babe."
    yasmin "It's academic now, 'cause we totally got away with it using our feminine wiles."
    iona "Our what?"
    aj "I thought we were using the power of friendship."

    # CHOICE
    menu:
        thought "We passed the secret challenge and..."
        "It was all down to teamwork":
            $ s3_mc.like("AJ")
            s3_mc "We all helped out in our own ways."
            aj "Yeah, exactly!"
            aj "You make a great team captain [s3e6p2_agent_name]. "
            elladine "Go team girls!"
        "I was clearly carrying the rest of you":
            $ s3_mc.dislike("AJ")
            s3_mc "I organised this whole operation. It would've been a disaster without [s3e6p2_agent_name] here."
            aj "But... the power of friendship..."
        "We owe it to the boys for being clueless":
            s3_mc "It doesn't really matter what we did."
            s3_mc "You boys were so easy to dupe, it was basically impossible for us to lose."
            iona "Ha! Well said, [s3e6p2_agent_name]."

    nicky "Another text!"
    miki "Oh, is it about our reward?"
    iona "What is it? Are we getting puppies?"
    seb "I don't think it's going to be puppies."
    ciaran "Aw."
    nicky "Just let me read it out!"
    text "Islanders, Before you find out what your reward is, it's time for another recoupling."
    text "Our newest Islanders are up first. Please get dressed and gather at the firepit. #newrules #mixitup"
    s3_mc "What?!"
    iona "A recoupling?"
    miki "But... but..."

    scene sand with dissolve
    $ on_screen = []

    "That's right, girls!"
    "Even with all your spy skills, you didn't see that coming, did you?"
    "So many questions left unanswered!"
    "Who will the new Islanders choose at tonight's recoupling?"
    "Will any of our happy couples be left intact by the time they're done?"
    "And is it just me, or did Ciaran and Tai enjoy the wrestling match a little bit more than they let on?"
    "Stay tuned to find out..."

    jump s3e6p3

    return

label s3e6p2_better_task:
    s3_mc "I fancy doing something different."
    genevieve "I was thinking we don't want to waste your talents."
    miki "Yeah, we're happy to switch if you want to!"
    thought "Great! I can pick any task I like!"

    # CHOICE
    menu:
        thought "I want to..."
        "Get Nicky to say Enchanted Husband":
            $ s3e6p2_task = "Nicky"
            $ s3e6p2_switched = "Yasmin"
            s3_mc "Hey, Yasmin..."
            s3_mc "Would you mind switching tasks with me?"
            yasmin "Oh, sure! No problem."
            yasmin "So, I'll be getting them all in the pool, then?"
            yasmin "I think I can manage that. Leave it to me."
        "Get Harry to rub sun cream on me":
            $ s3e6p2_task = "Harry"
            $ s3e6p2_switched = "Iona"
            s3_mc "Hey, Iona..."
            s3_mc "Would you mind switching tasks with me?"
            iona "Oh, sure! No problem."
            iona "So, I'll be getting them all in the pool, then?"
            iona "I think I can manage that. Leave it to me."
        "Sit in Camilo's lap":
            $ s3e6p2_task = "Camilo"
            $ s3e6p2_switched = "Miki"
            s3_mc "Hey, Miki..."
            s3_mc "Would you mind switching tasks with me?"
            miki "Oh, sure! No problem."
            miki "So, I'll be getting them all in the pool, then?"
            miki "I think I can manage that. Leave it to me."
        "Get Bill to motorboat me":
            $ s3e6p2_task = "Bill"
            $ s3e6p2_switched = "Elladine"
            s3_mc "Hey, Elladine..."
            s3_mc "Would you mind switching tasks with me?"
            elladine "Oh, sure! No problem."
            elladine "So, I'll be getting them all in the pool, then?"
            elladine "I think I can manage that. Leave it to me."
        "Get Ciaran and Tai to wrestle":
            $ s3e6p2_task = "Ciaran Tai"
            $ s3e6p2_switched = "AJ"
            s3_mc "Hey, AJ..."
            s3_mc "Would you mind switching tasks with me?"
            aj "Oh, sure! No problem."
            aj "So, I'll be getting them all in the pool, then?"
            aj "I think I can manage that. Leave it to me."
        "Put my eyeliner on Seb":
            $ s3e6p2_task = "Seb"
            $ s3e6p2_switched = "Genevieve"
            s3_mc "Hey, Genevieve..."
            s3_mc "Would you mind switching tasks with me?"
            genevieve "Oh, sure! No problem."
            genevieve "So, I'll be getting them all in the pool, then?"
            genevieve "I think I can manage that. Leave it to me."

    return

label s3e6p2_nicky_task:
    scene s3-daybeds-day with dissolve
    $ new_scene()

    "Harry, Nicky and Seb are chilling on the daybeds, minding their own business."
    "Little do they know they're about to get a visit from [s3e6p2_agent_name] and a few of her fellow operatives..."
    harry "Hey, girls."
    harry "[s3_name]. I've just had a great idea for a business. I'm gonna run my own fashion brand, and you can be my star model!"
    harry "We'd be rich..."
    s3_mc "That's sweet, Harry."
    # ADD back once MC images are in game.
    # harry "Loving the look, [s3_name]. It's really something."
    # harry "Keeping it casual today, [s3_name]? I respect that."
    nicky "What are you up to?"

    # CHOICE
    menu:
        thought "I can't let the boys know we're up to something..."
        "We're not doing anything. Back off":
            # NEED TO FILL
            "EMPTY"
        "We're just checking on the daybeds":
            nicky "Checking on the daybeds?"
            s3_mc "You know. To make sure they're still soft."
            "You test the mattress with your hands."
            s3_mc "Yep. All seems to be in order."
        "We're just checking on our fave boys!":
            s3_mc "Which is you guys!"
            harry "Aw."

    "Nicky narrows his eyes at you, but doesn't press any further."

    if s3e6p2_task == "Nicky":
        thought "I have to get Nicky to say Enchanted Husband out loud, but I can't just ask him to say it."
        thought "It could be tricky. Nicky's a pretty sharp guy."
        s3_mc "Hey, Nicky."
        nicky "Yeah?"
        s3_mc "Remind me. What was the name of that band Yasmin was in?"
        nicky "Why do you need me to tell you, Yasmin is right there?"
        yasmin "Well..."
        yasmin "Sometimes I forget the name of it..."
        
        # CHOICE
        menu:
            thought "Yasmin needs backup..."
            "It happens! Sometimes I forget my own name":
                nicky "If you say so..."
            "We can't all be as clever as you, Nicky":
                nicky "Flatterer."
            "To be fair, the band was very forgettable":
                yasmin "Um, OK."
                nicky "Well, I remember it."

        nicky "The name you're looking for is Enchanted Husband."
        yasmin "Brill. We were just testing you, babes."
        s3_mc "You passed."
        thought "Yes! First task complete."
        thought "That was a lot easier than I thought it would be."
    else:
        thought "Yasmin has to get Nicky to say Enchanted Husband out loud, but she can't just ask him to say it."
        thought "It could be tricky. Nicky's a pretty sharp guy."
        thought "I wonder how she'll play it..."
        yasmin "Hey, Nicky."
        nicky "Yeah?"
        yasmin "Remind me. What was the name of that band I was in?"
        nicky "You don't remember the name of your own band?"
        yasmin "Well..."

        # CHOICE
        menu:
            thought "Yasmin needs backup..."
            "It happens! Sometimes I forget my own name":
                nicky "If you say so..."
            "We can't all be as clever as you, Nicky":
                nicky "Flatterer."
            "To be fair, the band was very forgettable":
                yasmin "Um, OK."
                nicky "Well, I remember it."

        nicky "The name you're looking for is Enchanted Husband."
        yasmin "Brill. I was just testing you, babes."
        yasmin "You passed."
        thought "Yes! First task complete."
        thought "That was a lot easier than I thought it would be."

    return

label s3e6p2_harry_task:
    if s3e6p2_task == "Harry":
        thought "Now I've got to get Harry to rub sun cream on my back."
        thought "It's going to be tough to do it without making him suspicious."
        thought "Alright, here goes nothing."

        # CHOICE
        menu:
            thought "Hey, Harry..."
            "I'll do your sun cream if you do mine":
                # NEED TO FILL
                "EMPTY"
            "Cream me up! Now!":
                # NEED TO FILL
                "EMPTY"
            "Could you do me a favour? Pretty please?":
                harry "Sure! What is it?"
                "You hold out your sun cream bottle."
                s3_mc "It's just so hard to make sure I've got proper coverage on my back."
                s3_mc "Do you think you could rub it in for me?"
                s3_mc "I'd be really, really, grateful."
                "His face turns a little pink."
                harry "Of course, babe."

        "You sprawl out across the daybed on your stomach. The others move out of your way."
        s3_mc "Come on, Harry! Before I start burning!"
        harry "I am! Just let me..."
        "You hear him pop the cap off the bottle, then cream squirting out."
        "Seconds later you feel his hands on your back, blissfully cool and soothing."
        harry "How's this?"
        s3_mc "Ah. That's perfect."
        "He rubs the cream firmly into your skin for a few minutes before your whole back is covered."
        harry "There you go! All done."
        s3_mc "Thank you so much, Harry. I feel so much safer from the sun now."
        harry "It was my pleasure."
    else:
        iona "Harry, hun, would you mind doing me a favour?"
        harry "Sure! What is it?"
        "Iona holds out her sun cream bottle."
        iona "It's just so hard to make sure I've got proper coverage on my back."
        iona "Would you mind rubbing it in for me?"
        harry "Oh! Um..."

        if s3_mc.current_partner != "Harry":
            "He glances at Genevieve, but she just smiles sweetly at him."

        "He looks at you for guidance."

        # CHOICE
        menu:
            thought "Harry seems a bit hesitant..."
            "Stop stalling and start creaming!":
                # NEED TO FILL
                "EMPTY"
            "Go on, hun, nobody will mind":
                s3_mc "It's just sun cream. No big deal."
                harry "Yeah... yeah, you're right."
                "He takes the sun cream bottle from Iona."
            "It's OK if you use your feet":
                s3_mc "Then you know for sure there's nothing sexual about it."
                iona "Ew! [s3_name], no!"
                nicky "Thanks, [s3_name]. I'm never going to be able to un-imagine that."
                iona "It's OK, Harry. Just do it normally."
                "He's so stunned by your comment that he hardly seems to notice as Iona pushes the sun cream bottle into his hands."

        "Iona stretches out across the daybed on her stomach."
        "She gives you a cheeky thumbs up and mouths 'well done' as Harry starts to rub sun cream on her back."

    thought "Another task done!"
    thought "This is going really well so far."

    return

label s3e6p2_seb_task:
    if s3e6p2_task == "Seb":
        thought "Now, I've got to get Seb to wear my eyeliner."
        thought "There's a few different ways I could do this. I've just go to be careful not to make him suspicious."

        # CHOICE
        menu:
            thought "How should I raise the subject?"
            "Say Genevieve would like it":
                # NEED TO FILL
                "EMPTY"
            "Try flattering him":
                s3_mc "You've got the nicest eyes, Seb."
                seb "Oh! Um, thank you?"
                s3_mc "Yeah, you should do more to bring attention to them!"
                seb "How would I do that?"
                s3_mc "Hmm... maybe some eyeliner?"
                genevieve "Ooh, great idea, [s3_name]!"
                seb "You mean like make-up?"
                s3_mc "Yeah! Why not?"
            "Ask if he's tried it before":
                s3_mc "Have you ever worn eyeliner, Seb?"
                seb "What? Why?"
                s3_mc "Just your general look. You just seem like you would've tried it. Right, Viv?"
                genevieve "Yeah, I totally get that vibe from you."
                seb "Oh. Well, no. I haven't."
                s3_mc "Really? That's a bit disappointing."
                s3_mc "You should give it a try!"

        s3_mc "Come up to the dressing room and I'll put some on you."
        seb "I dunno... I didn't think you girls would be into that."
        genevieve "Of course we would! Trust me, [s3_name] knows what she's talking about."
        seb "Well... that's true."
    else:
        thought "Now, Genevieve's got to get Seb to wear her eyeliner."
        "You raise your eyebrows at Genevieve, and she nods."
        genevieve "Hey, Seb..."
        seb "Yeah, Viv?"
        genevieve "Has anyone ever told you you've got really nice eyes?"
        seb "I... really?"
        genevieve "Me and Genevieve were talking before, and we both agreed."
        genevieve "You've got the nicest eyes."
        seb "Wow. Er, cool. Thanks, Viv."
        genevieve "In fact, we think you should be doing a lot more to draw attention to them."
        seb "Huh?"
        genevieve "Make-up, babes. You'd look hot with a bit of eyeliner."
        seb "Really? Woah."
        seb "I've never worn it."
        genevieve "It would totally work with your look."
        genevieve "You should let me apply some for you. I promise I'll be gentle."
        seb "I dunno... I didn't think you girls would be into that."
        genevieve "Of course we would!"
        genevieve "Come on, [s3_name], back me up here."

        # CHOICE
        menu:
            thought "Genevieve needs my help to convince Seb..."
            "Don't do it, Seb, you're too goth already":
                # NEED TO FILL
                "EMPTY"
            "She's right, you'd look good! Give it a try":
                s3_mc "I think it'd totally complete your look"
                seb "Well, if you say so..."
            "Mate, she's clearly trying to flirt with you":
                $ s3_mc.like("Genevieve")
                $ s3_mc.like("Seb")
                s3_mc "It's a weird way to crack on, granted, but don't push her away just for that."
                "Seb looks at Genevieve and raises his eyebrows."
                "Genevieve blushes."
                genevieve "Well, uh... I mean..."

        genevieve "Both of you come up to the dressing room and I'll show you what I mean."

    "Seb shrugs."
    seb "Alright, you've convinced me."
    seb "I'll give it a try. Just this once, mind."
    genevieve "You won't regret this."
    "Together, you and Genevieve lead Seb up to the dressing room."

    scene s3-dressing-room with dissolve
    $ new_scene()

    seb "Mate, it smells like greengrocer's in here."
    s3_mc "That's what you get when you cross Iona's strawberry perfume with Yasmin's melon body spray. You get used to it."
    genevieve "Just sit here, Seb, under the light."
    seb "Alright..."

    if s3e6p2_task == "Seb":
        "He takes a seat while you retrieve your eyeliner from your make-up bag."
    else:
        "He takes a seat while Genevieve retrieves her eyeliner from her make-up bag."

    genevieve "I'm surprised you haven't tried this before, Seb. You've already got a little bit of an alternative look going on."
    seb "Yeah..."
    seb "I almost did try it, when I was a teenager."
    seb "I went through a bit of an emo phase, with the side fringe, the purple stripes and all that."
    genevieve "No way!"
    seb "Yeah! I guess most teenagers have their own way of rebelling, and that was mine."
    seb "I had to stop short of the eyeliner, just 'cause my parents would've hated it so much."
    seb "It wasn't worth the argument. Otherwise I would've tried it, to be honest."

    # CHOICE
    menu:
        thought "Seb had an emo phase as a teenager..."
        "I was a fashion rebel too!":
            s3_mc "I was totally the same. If someone told me not to wear something, that was all I wanted to wear."
            s3_mc "It wasn't about looking good. It was about showing the world I was my own person, and I wasn't going to be pushed around."
            seb "That's so cool."
        "I never had a rebellious phase":
            s3_mc "I just didn't feel the need."
            seb "Well, that's fair. It's a little difficult to explain if you've never been there yourself."
        "Babe, I'm still a fashion rebel":
            s3_mc "I'm still dressing however I want. I don't care what people think."
            genevieve "No kidding! That's probably your greatest strength, [s3_name]."
            seb "Yeah, life's too short to dress for other people."

    seb "For me, back then, it was kind of a way to distance myself from my parents. I never really felt like I belonged with them."
    "Genevieve gives him a sympathetic look."
    genevieve "Well. Whatever else, your parents seriously don't understand fashion."
    genevieve "No offence."
    seb "Ha, none taken!"
    seb "Don't worry, I don't think they're even watching the show."
    genevieve "Well, if they are, they're about to see how wrong they were."

    if s3e6p2_task == "Seb":
        s3_mc "Hold very still..."
        "You carefully start to draw along the length of Seb's eye."
    else:
        genevieve "Hold very still..."
        "She carefully starts to draw along the length of Seb's eye."

    seb "Wow, this feels weird."

    if s3e6p2_task == "Seb":
        s3_mc "Just a little longer..."
        s3_mc "And... done!"
    else:
        genevieve "Just a little longer..."
        genevieve "And... done!"
    thought "There! That's the third task finished."
    "Seb stares at himself in the mirror."
    seb "It's definitely different. I have no idea if it's good."
    seb "What do you think, [s3_name]?"

    # CHOICE
    menu:
        thought "Seb doesn't seem sure about this look..."
        "You look like a raccoon":
            # NEED TO FILL
            "EMPTY"
        "You're rocking it, babes":
            s3_mc "It really suits you!"
            seb "You're not going to tell me to slay, queen?"
            s3_mc "I can if you want me to."
            seb "No, thanks."
            seb "I'm just glad you like it. With the [s3_name] seal of approval, it can't be bad."
        "It's not an everyday thing":
            s3_mc "It's nice to change things up sometimes, but I don't think this is quite the right look for you."
            seb "Yeah, I kinda agree."
            seb "Oh, well. Doesn't hurt to try something new."

    genevieve "Why don't you keep it on for a few hours? Just to see how it goes."
    genevieve "At least give the others a chance to see."
    seb "Yeah, sure."
    seb "Worst case scenario, everyone gets a good laugh at my raccoon eyes."
    genevieve "Nobody's gonna laugh at you, Seb. We're your friends."
    genevieve "We love you. You know that, right?"
    seb "...Yeah, I know."
    "The three of you leave the dressing room and head down to the lawn."

    return

label s3e6p2_camilo_task:
    scene s3-poolside-day with dissolve
    $ new_scene()

    "The rest of the Islanders are hanging out by the pool, lounging on the grass or dangling their legs in the water."
    bill "Hey, Seb. You done something with your hair?"
    seb "Eyes, actually."
    harry "Looks great on you!"
    camilo "Yeah, it looks really nice."
    seb "Heh, thanks."
    if s3e6p2_task == "Seb":
        seb "[s3_name] did it for me."
    else:
        seb "Viv did it for me."
    tai "She did a great job!"
    tai "When are the rest of us getting makeovers?"
    genevieve "You'll have to book an appointment."
    ciaran "My ma always told me I had nice eyes."
    elladine "You do, babes! There's so much we could do to make them really pop!"
    thought "We can't get distracted. Let's go!"
    "Camilo's sitting comfortably on a beanbag in the middle of the group."

    if s3e6p2_task == "Camilo":
        # CHOICE
        menu:
            thought "Alright, I need to sit in Camilo's lap. How should I do this?"
            "Pretend to trip":
                # NEED TO FILL
                "EMPTY"
            "Just sit down":
                # NEED TO FILL
                "EMPTY"
            "Ask him nicely":
                s3_mc "Camilo, darling. There's no empty beanbags."
                s3_mc "Do you mind if I sit here?"
                camilo "Oh yeah, sure."
                "He starts to stand up, but you push him back down."
                s3_mc "No, no. I wasn't asking to take your beanbag."
                s3_mc "I was asking if I could sit here."
                "You point at his lap."
                "He looks down to where you're pointing, then back up again."
                camilo "...Oh."
                camilo "Er... yeah. Sure. Make yourself at home."

        "You wiggle around, getting comfortable."
        "Camilo's face turns bright red. The blush even spreads to his neck and ears."
        camilo "Blimey."
        "His bare skin presses against yours. His pecs are firm and smooth."
        "Instinctively, his hands come to settle on your hips."

        if s3_mc.current_partner != "Camilo":
            "He gives Iona a worried glance."
            "She just smiles, leaving Camilo relieved but confused."
        else:
            seb "You two are the worst. Get a room!"
            camilo "Hey, we're a couple. We're allowed to be cute in public."
            seb "There's a difference between being cute and... this!"
    else:
        "You look meaningfully at Miki."
        "She gives you a tiny nod and starts walking over to Camilo..."
        "Then suddenly pretends to trip and fall."
        miki "Oops!"
        camilo "Watch out!"
        "She lands sprawled across Camilo's lap."
        miki "Sorry, hun!"
        miki "Now I'm here, this is actually quite nice."
        miki "Has anyone ever told you you're really comfy?"
        "She stretches out and yawns."
        miki "I could sleep here for hours..."
        camilo "Babe, you'll make my leg go numb."
        "Miki stays there until you catch her eye, and then jumps up."
        miki "Sorry, so clumsy!"

    thought "Yes! Four down, three to go!"

    return

label s3e6p2_ciaran_tai_task:
    if s3e6p2_task == "Ciaran Tai":
        thought "Now I have to get Ciaran and Tai to wrestle each other."
        thought "This shouldn't be too hard, knowing them."

        # CHOICE
        menu:
            thought "What's the best way to get Ciaran and Tai to wrestle?"
            "Tell them it'd be hot":
                s3_mc "You know what I'd love to see more of around here?"
                s3_mc "You boys getting into fights."
                ciaran "Aw, why would we fight? We're mates."
                s3_mc "I don't mean, like, arguments."
                s3_mc "I'd just like to see you rolling around on the ground, trying to overpower each other."
                s3_mc "I think it'll be kinda hot."
                s3_mc "Like.. you and Tai, for example."
                "Grinning, Ciaran shrugs at Tai."
                ciaran "One bout? What do you say?"
                tai "Can't hurt..."
                tai "Except your pride when I totally beat you."
                ciaran "Bring it on."
            "Challenge their pride":
                s3_mc "Hey, Ciaran."
                ciaran "Yeah?"
                s3_mc "What would you do if you were at work and you had to kick a guy like Tai out of the club?"
                ciaran "Aw, why would I ever kick Tai out? Tai's a legend."
                s3_mc "Not actual Tai. I mean if there was someone as bis as Tai who was causing trouble."
                ciaran "Well... I'd just take him outside, I guess."
                s3_mc "But what if he put up a fight? Would you even be able to overpower him?"
                "Ciaran puffs his chest out a bit."
                ciaran "What are you saying? You think I couldn't take Tai in a fight?"
                tai "She's got a point, mate. I am a bit bigger than you."
                "Grinning, Ciaran shrugs at Tai."
                ciaran "One bout? What do you say?"
                tai "Can't hurt..."
                tai "Except your pride when I totally beat you."
                ciaran "Bring it on."
            "Get them both to wrestle me":
                s3_mc "I'm in the mood to wrestle. Any volunteers?"
                camilo "Sure, why not?"
                s3_mc "Thanks, but I want a real challenge."
                camilo "Aw, what?"
                s3_mc "Ciaran and Tai. Two on one."
                ciaran "Are you sure?"
                s3_mc "Totally. Bring it on."
                "Ciaran looks at Tai, who shrugs."
                "The three of you get into position on the grass while the other Islanders laugh and cheer."
                "At the last second before they both crash into you, you manage to duck out of the way, leaving them confused and grapping with each other."
                ciaran "Hey, [s3_name]! No fair!"
                s3_mc "Sorry, boys! Guess you'll just have to wrestle each other instead!"
                tai "Works for me."

        scene s3-lawn-day with dissolve
        $ new_scene()

        "Tai laughs as Ciaran tries to grapple him to the ground."
        tai "You'll have to try harder than that, mate!"
        "Ciaran ducks sideways and pulls Tai down onto the grass."
        ciaran "Gotcha!"
        "Both of them are laughing helplessly."
    else:
        thought "Now AJ has to get Ciaran and Tai to wrestle each other."
        thought "Knowing them, this one shouldn't be too hard."
        aj "Hey, Tai!"
        aj "Wanna wrestle?"
        tai "Sure!"

        scene s3-lawn-day with dissolve
        $ new_scene()

        "AJ stands up and flings herself at Tai."
        "He laughs as they go rolling to the floor."
        tai "Not fair! I wasn't ready!"
        aj "But you're bigger than me! I need some kind of advantage."
        aj "Can I have someone else on my team?"
        tai "Yeah, that seems fair."
        aj "Great."
        aj "Ciaran! You're with me!"
        ciaran "Sounds fun!"
        tai "Oh... I thought you meant one of the girls..."
        "AJ and Ciaran have already started trying to grapple Tai onto his back."
        "He gives up arguing and starts fighting back, grinning as sweet starts to shine on his forehead."
        "After a few minutes of noisy and good-natured wrestling, AJ wriggles out of the scrum, leaving Ciaran and Tai rolling around on the grass."
        "She sits down next to you, out of breath, and gives you a thumbs up."
 
    thought "Another task done! Easy!"
    "Ciaran and Tai are pretty evenly matched."
    "Tai has sheer size and strength on his side, but Ciaran is quick and never seems to run out of energy."
    yasmin "Come on, Ciaran! You can do it!"
    aj "Go Tai! Get 'im!"

    # CHOICE
    menu:
        thought "They're evenly matched..."
        "Cheer for Tai":
            $ s3_mc.like("Tai")
            s3_mc "I believe in you, Tai! Just imagine you're back on the rugby field!"
            "Tai grins, spurred on by your encouragement."
            "For a second, he gets the upper hand, before the match continues even more vigorously."
        "Cheer for Ciaran":
            $ s3_mc.like("Ciaran")
            s3_mc "I'm rooting for you, Ciaran! Just pretend you're back at the club and you have to kick him out!"
            "Ciaran grins, spurred on by your encouragement."
            "For a second, he gets the upper hand, before the match continues even more vigorously."
        "Cheer them both on":
            s3_mc "Keep going, boys! You're doing great!"
            "Tai grins."
            "Your encouragement seems to give Ciaran a new burst of energy."
            "For a second, Ciaran gets the upper hand, before the match continues even more vigorously."

    scene s3-poolside-day with dissolve
    $ new_scene()
    
    thought "Now, there's only two more tasks to go."

    return

label s3e6p2_bill_task:

    if s3e6p2_task == "Bill":
        thought "Uh oh. I have to get Bill to motorboat me."
        thought "This is probably the most ridiculous one of the lot. I just hope he doesn't suss me out."
        thought "Oh, well, here goes."

        # CHOICE
        menu:
            thought "Hey, Bill..."
            "Can you explain motorboating to me?":
                "Bill, who's just taken a sip from his water bottle, nearly spits it back out again. He starts coughing."
                bill "It's... well, it's like this."
                "He demonstrates in the air."
                bill "But you do that to, like, a girl's chest."
                s3_mc "I still don't really get it."
                s3_mc "Do you think you could show me?"
            "Have you ever motorboated a girl?":
                "Bill, who's just taken a sip from his water bottle, nearly spits it back out again. He starts coughing."
                bill "No... no, I can't say I have."
                s3_mc "Oh, that's surprising. I was just saying to the girls before, I bet Bill's done that."
                bill "What ? Why?"
                s3_mc "It's just this vibe you give off."
                s3_mc "Anyway, you should definitely give it a try."
                s3_mc "I would totally volunteer."
                bill "Really?"
            "Can you help me cross something off my bucket list?":
                bill "Sure! What is it?"
                "Bill takes a sip from his water bottle."
                s3_mc "I've never been motorboated."
                "He nearly spits his water back out again. He starts coughing."
                bill "Is that a fact?"
                s3_mc "It's been weighing on my mind. It keeps me up at night."
                s3_mc "I don't suppose you could help me out, could you?"
                bill "Well... I guess that's just part of being in a couple, right? "
                s3_mc "Sure, babe."

        bill "Alright. Here goes."
        "Grinning, Bill buries his face in your cleavage and shakes his head from side to side."
        "He comes up laughing."
        bill "You're a wild one, [s3_name]."
        bill "And I hope this isn't a weird thing to say, but you're the perfect girl to do that with."
        s3_mc "Glad you think so."
        "Elladine gives you a sneaky thumbs up."
        thought "Yes! I can't believe we got away with that!"
    else:
        thought "Uh oh. Elladine has to get Bill to motorboat her."
        "You shoot Elladine a look."
        "She looks nervously back at you, and her eyes flicker over to Nicky, who's chatting with Bill."
        thought "She's too embarrassed! There's no way she's going to do this with Nicky sitting right there!"
        thought "I have to distract him somehow."
        s3_mc "Hey, Nicky..."
        s3_mc "Could we have a chat? Just over here."
        nicky "Why?"
        s3_mc "Just come and I'll tell you."
        nicky "If you say so..."
        "He shrugs and follows you around to the other end of the pool, away from the other Islanders."
        "You make sure he's sitting with his back to the group."
        nicky "OK, so what did you want to tell me? Why do we have to be over by ourselves?"

        # CHOICE
        menu:
            thought "I just wanted to ask..."
            "Do you think [s3_mc.current_partner] likes me?":
                nicky "Are you serious?"
                nicky "Yes, [s3_mc.current_partner] likes you. [he_she!c]'s head over heels for you."
            "Are you and Elladine for real?":
                s3_mc "Like, do you really like each other? Or are you just playing the game?"
                nicky "We really like each other."
                nicky "At least, I really like her. I assume she likes me too."
            "Would you like to hear a joke?":
                s3_mc "What do you get if you cross, uh... a swimming pool..."
                s3_mc "With a piece of cake?"
                nicky "What?"
                s3_mc "Soggy cake!"

        nicky "Did you really bring me over here just to ask me that?"
        s3_mc "Well, um..."
        s3_mc "Well, I was just thinking that..."
        "You glance behind him, over his shoulder."
        "Elladine is saying something to Bill, who looks at her, confused."
        "Then he shrugs, and leans down..."
        thought "He's doing it!"
        nicky "[s3_name]? What are you looking at?"
        s3_mc "Nothing, nothing!"
        "You manage to keep him from turning around."
        "You hold his attention until you see Bill sit back away from Elladine and laughs"
        thought "Phew! It should be safe to go back now."
        nicky "Are you OK, [s3_name]? You seem kinda distracted."
        s3_mc "Yeah... yeah, just a bit. Sorry."
        s3_mc "Why don't we go back over to the others?"
        s3_mc "I'll explain all this properly later, I promise."
        "Nicky shrugs."
        nicky "Alright. If you're sure you're OK."
        "The two of you rejoin the group."
        "Elladine gives you a sneaky thumbs up."
        thought "Yes! I can't believe we got away with that!"

    thought "Only one task left to do, and then we've won the challenge!"

    return

label s3e6p2_pool_task:
    if s3e6p2_task != "Pool":
        thought "[s3e6p2_switched] has to get all the boys to jump in the pool."
        thought "I wonder how she'll play this..."
        "[s3e6p2_switched] shrieks loudly."

        if s3e6p2_switched == "Elladine":
            elladine "Fire ants! In the grass!"
        elif s3e6p2_switched == "Iona":
            iona "Fire ants! In the grass!"
        elif s3e6p2_switched == "Miki":
            miki "Fire ants! In the grass!"
        elif s3e6p2_switched == "Genevieve":
            genevieve "Fire ants! In the grass!"
        elif s3e6p2_switched == "AJ":
            aj "Fire ants! In the grass!"
        elif s3e6p2_switched == "Yasmin":
            yasmin "Fire ants! In the grass!"

        "The boys all jump to their feet."
        harry "How's a fire ant different to your regular garden variety ant?"

        if s3e6p2_switched == "Elladine":
            elladine "They sting! My feet are covered, there must be hundreds of them!"
            nicky "Where? I don't see any!"
            elladine "Hundreds of them! Quick, everyone jump in the pool!"
        elif s3e6p2_switched == "Iona":
            iona "They sting! My feet are covered, there must be hundreds of them!"
            nicky "Where? I don't see any!"
            iona "Hundreds of them! Quick, everyone jump in the pool!"
        elif s3e6p2_switched == "Miki":
            miki "They sting! My feet are covered, there must be hundreds of them!"
            nicky "Where? I don't see any!"
            miki "Hundreds of them! Quick, everyone jump in the pool!"
        elif s3e6p2_switched == "Genevieve":
            genevieve "They sting! My feet are covered, there must be hundreds of them!"
            nicky "Where? I don't see any!"
            genevieve "Hundreds of them! Quick, everyone jump in the pool!"
        elif s3e6p2_switched == "AJ":
            aj "They sting! My feet are covered, there must be hundreds of them!"
            nicky "Where? I don't see any!"
            aj "Hundreds of them! Quick, everyone jump in the pool!"
        elif s3e6p2_switched == "Yasmin":
            yasmin "They sting! My feet are covered, there must be hundreds of them!"
            nicky "Where? I don't see any!"
            yasmin "Hundreds of them! Quick, everyone jump in the pool!"

        "You and [s3e6p2_switched] sprint to the pool and jump in. The other girls all follow your lead, yelling and screaming."
        "The boys are close behind, hurling themselves into the water with a series of gigantic splashes."
        seb "Wait! Won't the water ruin the eyeliner?"
        s3_mc "It's waterproof, babes! Just jump!"
        "He takes a deep breath and jumps in."
    else:
        # CHOICE
        menu:
            thought "I have to get all the boys to jump in the pool."
            "Make it a contest between the boys":
                s3_mc "Hey, boys."
                s3_mc "Which one of you would make the biggest splash in the pool?"
                "Without even answering, Bill gets up and hurls himself straight into the water."
                "He bobs back up to the surface, shaking water out of his eyes."
                bill "Does that answer your question?"
                s3_mc "Hmm. It was a pretty good splash, but I'd have to see what the others can do before making a call."
                tai "Come on, then. I reckon I can do better than that."
                "Tai gets up and jumps in the pool, closely followed by Harry, Camilo and Ciaran."
                camilo "Who's winning so far, [s3_name]?"
                s3_mc "Ooh, it's too hard to say. I'd have to see what Nicky and Seb have to offer."
                seb "But won't it ruin the eyeliner?"
                s3_mc "Nah, babes. It's waterproof."
                seb "Oh well, in that case..."
                "Seb jumps in, leaving Nicky the only boy still out of the water."
                elladine "What's the matter, babe? Why aren't you joining in?"
                nicky "I don't have anything to prove."
                "Elladine pouts."
                elladine "Don't you want to impress me?"
                nicky "Well, when you put it like that..."
                "Nicky walks over to the edge of the pool, his eyes fixed on Elladine the whole time, and simply steps into the water."
                "She laughs and he floats back to the surface."
                nicky "How was that?"
            "Tell them there's a prize in there":
                s3_mc "I've got a text!"
                camilo "Have you? I didn't hear anything."
                "You ignore him and take out your phone."
                s3_mc "Oh my gosh! It says here that there's a special prize today for whichever boy finds it first!"
                harry "Really? Does it say what the prize is?"
                s3_mc "No. Just that it's totally awesome."
                s3_mc "And it's hidden..."
                s3_mc "At the bottom of the pool!"
                "Bill, Camilo and Harry jump to their feet and rush to be the first into the pool."
                bill "It's mine!"
                harry "Mine!"
                seb "Wait, wait! Is it safe for me to swim? Won't it ruin the eyeliner?"
                s3_mc "It's waterproof, babes."
                seb "Well, in that case..."
                "Seb takes a deep breath and jumps straight in the pool, closely followed by Camilo and Tai."
                "Nicky is the last boy left at the poolside."
                nicky "This doesn't seem right."
                nicky "Why would you tell us that if it's supposed to be hidden...?"
                s3_mc "You'll just have to jump in and find out, won't you?"
                "Nicky shrugs, sighs, and throws himself into the pool."
            "Pretend to see fire ants on the lawn":
                "You give your best scream of terror."
                harry "[s3_name]! What's the matter?"
                s3_mc "Fire ants! In the grass!"
                harry "How's a fire ant different to your regular garden variety ant?"
                s3_mc "They sting! My feet are covered, there must be hundreds of them!"
                "The boys all jump to their feet."
                nicky "Where? I don't see any!"
                s3_mc "Quick, everyone jump in the pool!"
                "You sprint to the pool and jump in. The other girls all follow your lead, yelling and screaming."
                "The boys are close behind, hurling themselves into the water with a series of gigantic splashes."
                seb "Wait! Won't the water ruin the eyeliner?"
                s3_mc "It's waterproof, babes! Just jump!"
                "He takes a deep breath and jumps in."
    return

#########################################################################
## Episode 6, Part 3
#########################################################################
label s3e6p3:
    scene sand with dissolve
    $ on_screen = []

    show screen day_title(6, 3) with Pause(4)
    hide screen day_title with dissolve

    "Last time on Love Island, we ended on a cliffhanger..."
    s3_mc "What?"
    iona "A recoupling?"
    miki "But... but..."

    $ leaving("iona")
    $ leaving("miki")

    "Sorry for leaving you in suspense like that, everyone."
    "You must be on the edge of your seats!"
    "So you probably want to just stop talking and get straight back into the action, right?"
    "Well, I will..."
    "...after telling you some of the great jokes I've written about tonight's episode."
    "..."
    "Alright, I haven't got any jokes yet."
    "But I'll be back later in the episode, and then you'll see."

    scene s3-poolside-day with dissolve
    $ new_scene()

    tai "So we get to choose first in the recoupling?"
    ciaran "Get in."
    yasmin "It's about time."

    # CHOICE
    menu:
        thought "The new Islanders get to choose before everyone else at tonight's recoupling..."
        "But I get to go first again, right?":
            tai "Huh?"
            s3_mc "I got to go first at the last recoupling."
            s3_mc "That hasn't changed, has it?"
            if s3_mc.bff == "Elladine":
                elladine "That time was because you were single. You're not single anymore."
            elif s3_mc.bff == "Genevieve":
                genevieve "That time was because you were single. You're not single anymore."
            elif s3_mc.bff == "Nicky":
                nicky "That time was because you were single. You're not single anymore."
            elif s3_mc.bff == "Seb":
                seb "That time was because you were single. You're not single anymore."
            s3_mc "Aw. Well, that's not fair."
            tai "C'mon, [s3_name], don't stress. It'll be fun."
        "Ugh, that's not fair!":
            $ s3_mc.dislike("Tai")
            s3_mc "Why should they get to go before us?"
            tai "Because we haven't even had a chance to couple up yet!"
            tai "C'mon, [s3_name], don't stress. It'll be fun."
        "This is so exciting!":
            $ s3_mc.dislike(s3_mc.current_partner)
            s3_mc "It's definitely time for another recoupling!"
            s3_mc "I can't wait to see who you three choose."
            if s3_mc.current_partner == "Bill":
                bill "Er, yeah. Me neither."
            elif s3_mc.current_partner == "Camilo":
                camilo "Er, yeah. Me neither."
            elif s3_mc.current_partner == "Harry":
                harry "Er, yeah. Me neither."
            elif s3_mc.current_partner == "AJ":
                aj "Er, yeah. Me neither."

    seb "Once you three have had your go, do the rest of us get to couple up too?"
    bill "Yeah. I guess it'll be the girl's turn, since us boys got to choose last time."
    miki "Should we go and get ready?"
    elladine "We've only just got in the pool!"
    elladine "Can't we spend a bit more time here? And just pretend for a bit that nothing's ever going to change?"

    # CHOICE
    menu:
        thought "What should we do?"
        "We need to get ready for the recoupling!":
            $ s3_mc.dislike("Elladine")
            s3_mc "It's already starting to get dark! There's no time to mess around."
            elladine "Aw, OK. I guess you're right."
            genevieve "Come on, it'll be fun!"
            genevieve "Recoupling means it's a night to really go all out."
            "You hoist yourself out of the pool. The other Islanders start to follow suit."
        "Just ten more minutes in the pool...":
            $ s3_mc.like("Elladine")
            s3_mc "Can't hurt."
            elladine "Yay!"
            nicky "Watch out! Tidal wave!"
            "Nicky sends up a huge splash of water that soaks almost everyone, including [s3_mc.current_partner], who bursts out laughing."
            "A splash fight breaks out, filling the lawn with screams and laughter."
            "You have fun with the other Islanders, until you notice the sun start to dip behind the Villa."
            if s3_mc.current_partner == "Bill":
                bill "I guess we really should go in and get ready now."
                bill "But I'm feeling a lot more ready for it after that."
            elif s3_mc.current_partner == "Camilo":
                camilo "I guess we really should go in and get ready now."
                camilo "But I'm feeling a lot more ready for it after that."
            elif s3_mc.current_partner == "Harry":
                harry "I guess we really should go in and get ready now."
                harry "But I'm feeling a lot more ready for it after that."
            elif s3_mc.current_partner == "AJ":
                aj "I guess we really should go in and get ready now."
                aj "But I'm feeling a lot more ready for it after that."
            if s3_mc.bff == "Elladine":
                elladine "Yeah, me too. This has been great."
            elif s3_mc.bff == "Genevieve":
                genevieve "Yeah, me too. This has been great."
            elif s3_mc.bff == "Nicky":
                nicky "Yeah, me too. This has been great."
            elif s3_mc.bff == "Seb":
                seb "Yeah, me too. This has been great."
            "[s3_mc.bff] gives you a grateful smile as you all start climbing out of the pool."
        "What does [s3_mc.current_partner] want to do?":
            $ s3_mc.like(s3_mc.current_partner)
            if s3_mc.current_partner == "Bill":
                bill "I want us all to spend a little bit longer out here."
            elif s3_mc.current_partner == "Camilo":
                camilo "I want us all to spend a little bit longer out here."
            elif s3_mc.current_partner == "Harry":
                harry "I want us all to spend a little bit longer out here."
            elif s3_mc.current_partner == "AJ":
                aj "I want us all to spend a little bit longer out here."
            s3_mc "Then that's what we're gonna do."
            elladine "Yay!"
            nicky "Watch out! Tidal wave!"
            "Nicky sends up a huge splash of water that soaks almost everyone, including [s3_mc.current_partner], who bursts out laughing."
            "A splash fight breaks out, filling the lawn with screams and laughter."
            "You have fun with the other Islanders, until you notice the sun start to dip behind the Villa."
            if s3_mc.current_partner == "Bill":
                bill "I guess we really should go in and get ready now."
                bill "But I'm feeling a lot more ready for it after that."
            elif s3_mc.current_partner == "Camilo":
                camilo "I guess we really should go in and get ready now."
                camilo "But I'm feeling a lot more ready for it after that."
            elif s3_mc.current_partner == "Harry":
                harry "I guess we really should go in and get ready now."
                harry "But I'm feeling a lot more ready for it after that."
            elif s3_mc.current_partner == "AJ":
                aj "I guess we really should go in and get ready now."
                aj "But I'm feeling a lot more ready for it after that."
            if s3_mc.bff == "Elladine":
                elladine "Yeah, me too. This has been great."
            elif s3_mc.bff == "Genevieve":
                genevieve "Yeah, me too. This has been great."
            elif s3_mc.bff == "Nicky":
                nicky "Yeah, me too. This has been great."
            elif s3_mc.bff == "Seb":
                seb "Yeah, me too. This has been great."
            "[s3_mc.bff] gives you a grateful smile as you all start climbing out of the pool."

    iona "Bagsy using the shower first!"
    miki "Aw, man."
    miki "Wait! Bagsy using the shower second!"
    s3_mc "Come on, girls. Let's get ready."

    scene s3-dressing-room with dissolve
    $ new_scene()
    $ outfit = "evening"

    "There's a nervous atmosphere in the dressing room."
    "Only Yasmin seems relaxed as she calmly changes into her evening clothes."
    thought "I guess it's easy for her, knowing she's choosing first."
    yasmin "Sorry, [s3_name]... could I ask you a favour?"
    yasmin "This has a zip at the back and it's a bit stubborn. Would you mind?"

    # CHOICE
    menu:
        thought "Yasmin needs help zipping up her skirt..."
        "Sorry, I'm too busy getting dressed":
            $ s3_mc.dislike("Yasmin")
            s3_mc "I've got to focus on my own look."
            yasmin "Oh... OK."
            miki "Let me get it, babes."
            yasmin "Thanks, hun."
            "Miki tugs the zip into place."
            miki "There, all done."
            yasmin "You're a star."
        "Sure, I'll give you a hand":
            $ s3_mc.like("Yasmin")
            yasmin "Thanks, hun."
            "Yasmin turns around and you tug the zip into place."
            s3_mc "There, all done."
            yasmin "You're a star."
        "If you want me to touch you, you can just ask" if s3_mc.bisexual:
            $ s3_mc.like("Yasmin")
            s3_mc "I'm not going to say no."
            "Yasmin smirks."
            yasmin "Come on, then."
            "You stand behind her, not quite touching."
            "She waits patiently as you tug the zip into place."
            "You let your hand linger at the small of her back for a moment before pulling away."
            s3_mc "There, all done."
            yasmin "Thanks, hun. You're a star."
            s3_mc "Any time, babes."

    thought "I better sort out my own outfit."
    thought "Got to make sure it's on point. This recoupling could change everything..."
    ## Add back once MC images are in game
    # Outfit change to evening wear
    # thought "Tried and true."
    ## REMOVE BELOW once MC images are added into game.
    "You get changed into your favourite evening clothes."
    iona "I love that one, babe. It's classic [s3_name]."
    # iona "Wow, MC! You're making the rest of us look bad."
    # thought "No need to get fancy."
    # thought "What's done is done. An outfit won't change the outcome of tonight."
    "There's a knock at the door, and Seb peeks into the room."
    seb "Are you girls decent?"
    aj "Yeah, come on in."
    seb "Wow, [s3_name]! You look amazing!"
    s3_mc "Thanks!"
    seb "I just came to ask about this eyeliner. It's been fun, but I kinda wanna take it off for the recoupling."
    seb "Only I'm not sure how. Wiping it just makes it smudged."
    genevieve "Oh yeah, sorry. That stuff lasts a really long time."
    genevieve "It only comes off with remover. Let me help."
    "Genevieve takes some wipes and carefully cleans the liner form around Seb's eyes."
    "When she's finished, they just look at each other for a moment, then quickly look away."
    seb "So, uh... how are you girls feeling about the recoupling?"
    seb "I've just been talking to Tai about it, and he wouldn't tell me who he was planning to choose."

    $ pronouns(s3_mc.current_partner)

    # CHOICE
    menu:
        thought "Who will Tai choose at the recoupling?"
        "I hope it's not me":
            $ s3_like_tai = False
            s3_mc "That's the last thing I want from tonight."
        "I wouldn't say no...":
            $ s3_like_tai = True
            s3_mc "He can choose me if he wants. I won't complain."
            iona "What about [s3_mc.current_partner]?"
            s3_mc "What about [him_her]?"
            iona "Well... fair play."
        "Probably Ciaran, right?":
            s3_mc "Tell me it's not just me who sees something between them."
            aj "Oh, yeah, I totally get it."
            yasmin "They'd make a cute couple."

    iona "How about you, Yasmin? Or would it go against your whole 'air of mystery' thing to tell us?"
    yasmin "I've got some ideas."

    if s3_like_yasmin:
        "She glances at you, a tiny smile on her lips."
    else:
        "She glances at Seb, a tiny smile on her lips."

    yasmin "But we'll just have to wait and see, won't we?"
    seb "Classic Yas."
    s3_mc "Shall we head down to the firepit, then?"
    genevieve "Yeah, I think we're ready!"
    elladine "Let's go, girls!"
    elladine "... And Seb!"

    scene s3-firepit-night with dissolve
    $ new_scene()

    "Outside, you and the other girls line up opposite the firepit."
    "Beside you, Elladine twirls her hair between her fingers."
    elladine "How are you feeling, babes? Nervous?"

    # CHOICE
    menu:
        thought "How am I feeling about the recoupling?"
        "I've got a good feeling about this":
            s3_mc "I think things are going my way."
            elladine "That's good. I need some of that positivity."
        "I've got a bad feeling about this":
            s3_mc "Nothing's ever straightforward around here."
            elladine "Yeah..."
        "I'm going to take things as they come":
            s3_mc "It's out of our hands now."
            elladine "Very wise."

    elladine "I'm just trying not to think about it too much."
    "Yasmin joins the boys sitting on the bench, waiting for their turn to choose."

    # Yasmin's Choice
    yasmin "Text!"
    yasmin "I'm choosing first. Sweet."
    "Yasmin stands up and looks around at all the Islanders."
    yasmin "Well, I came to Love Island looking for that special feeling."
    yasmin "When you meet someone for the first time and you just know, somehow, you'll never be the same again."

    if s3_like_yasmin:
        yasmin "And I found that feeling in the very first person I met here."
        "Her eyes light on you, and she smiles."
        yasmin "Meeting her was like finding that one song you just want to listen to on repeat. Again and again and again."
        yasmin "And every time you hear it, you find something new to love about it."
        yasmin "Which is why the girl I want to couple up with is..."
        yasmin "[s3_name]."
        
        $ s3e6p3_li = "Yasmin"
        call s3e6p3_choice from _call_s3e6p3_choice

        # ADJUST AFTER REFACTORING
        $ s3_ex = s3_mc.current_partner
        $ s3_li = "Yasmin"
        $ s3_li_lower = s3_li.lower()
        $ s3_mc.current_partner = "Yasmin"
        $ s3_mc.past_partners.append("Yasmin")

    else:
        yasmin "I don't know if I've found that with this boy, but I do know I want to get to him better."
        yasmin "I think there's more to him than meets the eye, and I hope I can be the girl to finally get past his defences."
        yasmin "So the boy I want to couple up with is..."
        yasmin "Seb."
        "Seb does a silent fist pump before going over to hug Yasmin."
        "AJ nudges you and whispers."
        aj "Looks like his mopey days might be over at last!"
        # CHOICE
        menu:
            thought "Seb and Yasmin..."
            "Who cares about them?":
                $ s3_mc.dislike("AJ")
                aj "I do. They're my friends."
                s3_mc "Yeah, yeah. Let's just keep this recoupling moving along."
            "Seems like a quality match":
                s3_mc "I think he's finally found a girl who gets him. I'm happy for them."
                aj "I know, right?"
            "It probably won't last":
                s3_mc "Seb hasn't had a good day since about 2002. There's no way that's about to change now."
                s3_mc "I don't think he'd know what to do with a happy relationship even if he found one."
                aj "Aw, but I wanna be optimistic about it. It's never too late for him to turn his life around!"
        "Yasmin and Seb sit down together, clasping one another's hands."

    # Tai's Choice
    "The sound of another text cuts through the quiet."
    tai "That was me!"
    tai "It's my turn to choose."
    "Tai stands up and looks down the line of the girls."
    tai "Well, this girl has got great banter, which is the number one thing I look for."
    tai "And she's proper fit, too, which doesn't hurt."

    if s3_like_tai and s3_like_yasmin == False:
        if s3e5p3_yasmin_help == "Tai":
            tai "When Yasmin came to me last night and told me I should couple up with her, my response was, 'I couldn't agree more'."
            tai "I find it very cute that she thought I needed persuasion."
            tai "I was, in fact, already falling for her."
        tai "Basically, I like everything about her, and I want to spend more time with her."
        tai "I can't put it any simpler than that."
        tai "[s3_name]."

        $ s3e6p3_li = "Tai"
        call s3e6p3_choice from _call_s3e6p3_choice_1

        # ADJUST AFTER REFACTORING
        $ s3_ex = s3_mc.current_partner
        $ s3_li = "Tai"
        $ s3_li_lower = s3_li.lower()
        $ s3_mc.current_partner = "Tai"
        $ s3_mc.past_partners.append("Tai")

    else:
        tai "Knowing we can talk sport together is just the icing on the cake."
        tai "I can't wait to get to know her better and see if there could be something special between us."
        tai "So the girl I want to couple up with is..."
        tai "AJ."
        "AJ's beaming as she goes to sit next to Tai."
        aj "Thanks, big guy!"
        if s3_mc.current_partner == "AJ":
            thought "What?!"
            # CHOICE
            menu:
                thought "Tai coupled with AJ!"
                "Call him out":
                    # NEED TO FILL
                    "EMPTY"
                "Give her a hug":
                    $ s3_mc.like("AJ")
                    "You wrap your arms around AJ's waist and press your face into her shoulder."
                    "Her hair is as soft as silk against your cheek."
                    s3_mc "I didn't think it would be us."
                    aj "To be honest, babe, neither did I."
                    aj "We'll find our way back to each other. If that's what you want."
                    "She squeezes you back and kisses your ear, which is the only part of you she can reach in this position."
                    "She gives you a sad look as she takes a seat. Tai looks awkwardly down at his shoes."
                "Play it cool":
                    "You watch calmly as AJ and Tai go to sit down together."
                    "They both look at you for a reaction, but you just shrug, keeping your face neutral."
    
    # Ciaran's Choice
    ciaran "So.. I guess it's me to go next, then?"
    ciaran "Oops, there's the text."
    "Ciaran stands up and looks at the remaining girls."
    ciaran "So... the one thing I had in my head when I came here was, 'I wanna find a girl who makes me feel something different.'"
    ciaran "Like, my love life up to now has been fine, but it's just been fine. It's not been exciting, it's not been special."
    ciaran "Well, this girl is both exciting and special for sure."

    if s3_like_yasmin:
        ciaran "She's got a really kind heart, and I feel like I can be myself around her."
    elif s3_like_tai:
        ciaran "She's so full of joy and positive energy, she's like a golden retriever in human form."
    else:
        ciaran "She's beautiful, but even beyond that..."
        ciaran "I've come to really admire her over the past couple of days."
        ciaran "She's funny, and adorable, and tough. More than she realises, I think."
        ciaran "I like her. A lot."
        ciaran "I dunno if she likes me back at all, so I might be making a massive mistake here."
        ciaran "But I'll be kicking myself for the rest of my life if I don't at least take a gamble."

    ciaran "Which is why the girl I want to couple up with is..."

    if s3_like_yasmin:
        ciaran "Genevieve."
        if s3_mc.past_partners[1] == "Harry":
            genevieve "Yes, babe!"
        else:
            "Genevieve looks at Harry and bites her lip before going over to Ciaran."
            "They sit down together."
    elif s3_like_tai:
        ciaran "AJ."
        aj "Oh! Wow, I did not see that coming."
        aj "But I'm not complaining."
        "They take their seats."
    else:
        ciaran "[s3_name]."
        $ s3e6p3_li = "Ciaran"
        call s3e6p3_choice from _call_s3e6p3_choice_2

        # ADJUST AFTER REFACTORING
        $ s3_ex = s3_mc.current_partner
        $ s3_li = "Ciaran"
        $ s3_li_lower = s3_li.lower()
        $ s3_mc.current_partner = "Ciaran"
        $ s3_mc.past_partners.append("Ciaran") 

    if s3_mc.past_partners[1] == "Bill":
        $ s3e6p3_other = "Miki"
    elif s3_mc.past_partners[1] == "Camilo":
        $ s3e6p3_other = "Iona"
    elif s3_mc.past_partners[1] == "Harry":
        if s3_mc.current_partner == "Yasmin":
            $ s3e6p3_other = "Seb"
        else:
            $ s3e6p3_other = "Genevieve"
    elif s3_mc.past_partners[1] == "AJ":
        if s3_mc.current_partner == "Tai":
            $ s3e6p3_other = "Ciaran"
        else:
            $ s3e6p3_other = "Tai"

    iona "So, all the new guys have chosen..."
    iona "That means it's our turn now, right?"
    miki "Ooh, it is! And it's my turn first!"
    "Miki faces the surviving Islanders and puts her hands on her hips."

    if s3_mc.past_partners[1] == "Bill":
        miki "Well, I don't want to step on anyone's toes."
        miki "But seeing as this boy is now single again, and he's still majorly a bit of me..."
        "She glances apologetically at you."
        miki "I may as well give it another shot."
        miki "So the boy I want to couple up with is Bill."
        "Bill looks at you and sighs."
    else:
        miki "Well, I've been coupled up with this boy since day one, and I'm not about to change course now."
        miki "His chat's a bit ridiculous, but in the best way."
        miki "And underneath it all, I think he's got the heart of a true romantic."
        bill "Don't expose me like this, babe."
        miki "The boy I want to couple up with is Bill."

    # CHOICE
    menu:
        thought "Bill and Miki..."
        "What a great match":
            thought "Maybe they'll start a vlog together where they review biscuits."
        "I don't see it":
            thought "Lust goblins, the pair of them."
        "She nabbed my ex!" if s3_mc.past_partners[1] == 'Bill':
            thought "I'm gonna find my way back to him."
        "Yawn" if s3_mc.past_partners[1] != 'Bill':
            thought "Talk about predictable."

    "They hug and sit down with the other couples."
    iona "My turn!"
    "Iona rakes her eyes over the remaining boys."

    if s3_mc.past_partners[1] == "Camilo":
        iona "Well, I don't want to step on anyone's toes."
        iona "But seeing as this boy is now single again, and he's still majorly a bit of me..."
        "She glances apologetically at you."
        iona "I may as well give it another shot."
        iona "So the boy I want to couple up with is Camilo."
        "Camilo looks at you and sighs."
    else:
        iona "Sorry to disappoint, lads, but I'm sticking to my guns."
        iona "I've already found a boy in here who makes me go all tingly, and I don't wanna give that up yet."
        iona "He's a proper nice guy. Not to mention proper sexy."
        "Camilo smiles modestly."
        iona "Which is why the boy I want to couple with is..."
        iona "Camilo."
        camilo "Come here, you."  
        "He takes her hand and gives her a kiss."

    "They sit down side by side."

    # CHOICE
    menu:
        thought "Camilo and Iona..."
        "So fire":
            thought "They're a really awesome pair."
        "Not as hot as they think they are":
            thought "They're cute, but I'm cuter."
        "She nabbed my ex!" if s3_mc.past_partners[1] == 'Camilo':
            thought "I'm gonna find my way back to him."
        "Next" if s3_mc.past_partners[1] != 'Camilo':
            thought "Blah, whatever."

    if s3_like_yasmin == False:
        genevieve "My turn!"
        "Genevieve stands, facing the boys. She fidgets with her hair."
        genevieve "This boy..."
        "She bites her lip, and her gaze drifts over to Harry."
        genevieve "This boy... has been a real sweetheart to me ever since we got here."
        genevieve "He's super cute, and I just know he's going to achieve his dreams one day."
        genevieve "So the boy I want to couple up with is Harry."
        harry "Thanks, Viv."
        if s3_mc.past_partners[1] == "Harry":
            "He gives you a wink as he walks over to her."
        "Genevieve and Harry sit down next to Yasmin and Seb."
        "Seb shuffles awkwardly when Genevieve's shoulder brushes against his. They don't make eye contact."

        # CHOICE
        menu:
            thought "Harry and Viv..."
            "I really like them as a couple":
                thought "They're lovely, the both of them."
            "When are they gonna wake up?":
                thought "Just so not right for each other."
            "She nabbed my ex!" if s3_mc.past_partners[1] == 'Harry':
                thought "I'm gonna find my way back to him."
            "Is it dinner time yet?" if s3_mc.past_partners[1] != 'Harry':
                thought "I'm not interested in them."

    "There's the sound of a phone beeping for the last time."
    elladine "It's me! Surprise."

    if s3_like_yasmin == False:
        # CHOICE
        menu:
            thought "Elladine's choosing, and Nicky's the only boy left..."
            "Just get on with it":
                # NEED TO FILL
                "EMPTY"
            "That worked out nicely":
                s3_mc "One girl, one boy, and they both want to be coupled up with each other."
                s3_mc "Right?"
                elladine "Well, I'm not sure..."
                "Elladine laughs."
                elladine "Just kidding, I'm sure."
                nicky "You had me going there. For about a quarter of a second."
            "You should still give a speech!":
                elladine "Aw, do you think so?"
                s3_mc "Yeah, it's romantic!"
                elladine "Alright. You're right."
                elladine "I'll try to keep it short."
    else:
        # CHOICE
        menu:
            thought "Elladine's got to choose between Nicky, Harry and Seb..."
            "Just get on with it ":
                # NEED TO FILL
                "EMPTY"
            "Go on, surprise us!":
                s3_mc "Switch things up, hun! Keep them on their toes!"
                seb "Yeah, time to be adventurous!"
                harry "Don't rush into any hasty decisions!"
            "Bad luck, Harry and Seb":
                harry "It's fine."
                seb "I'm used to it..."

        "Elladine laughs."
        elladine "Sorry, to be predictable, boys."
        elladine "I do love you both, but I've got to go with my heart."
        elladine "Well, there was never any question in my mind."
        elladine "This boy already means the world to me."
        elladine "He's loyal, he's funny... he's everything I've been looking for."
        elladine "The boy I want to couple up with is Nicky."
        nicky "Thanks, love."
        "Harry and Seb turn to face each other."
        seb "I guess this means we're both single."
        harry "Bummer."

        # CHOICE
        menu:
            thought "Harry and Seb are both single..."
            "Get packing, then":
                # NEED TO FILL
                "EMPTY"
            "I'm sorry, boys":
                $ s3_mc.like("Harry")
                s3_mc "You don't deserve to be single."
                harry "Thanks, [s3_name]."
                seb "I'm sure we'll be OK."
            "Couple up with each other":
                s3_mc "Why not?"
                ciaran "Yeah, I'm sure that'd be cool!"
                "Harry and Seb share a glance."
                seb "Thanks for the encouragement, but I think we're good."

        harry "We can be a friendship couple, how about that?"
        seb "Works for me. Wouldn't be my first time."

    miki "So, is that everyone?"
    s3_mc "Yep."
    thought "Man, I'm tired."
    thought "I need to go get ready for bed."

    if s3e6p3_good_couple:
        thought "I can't believe [s3_mc.current_partner] and I are coupled up!"
        thought "This is so exciting."
    else:
        thought "And figure out what on earth just happened..."

    "Hello, me again."
    "I know I said I'd be back with jokes, but I can't joke at a time like this. Ask me again at the end of the episode."
    "If I were [s3_name], after all the drama, I'd need a minute to get my head straight!"

    scene s3-dressing-room with dissolve
    $ new_scene()
    $ outfit = "pjs"

    thought "I need a minute to get my head straight."
    thought "Good thing I've got the dressing room to myself. Today has been a lot to take in."
    thought "And I haven't even had a proper chance to talk to [s3_mc.past_partners[1]] or [s3_mc.current_partner] about what happened..."
    thought "Well, maybe we could have a chat if they're still awake when I get into the bedroom."
    thought "I'd better hurry up and get ready for bed!"

    # Add back once MC images are added to game
    # Outfit change to sleepwear
    # thought "Oh, yeah. Super sexy."
    # thought "I guess this'll do."

    "You're wiping off the last of your make-up when you hear muffled voices through the wall."
    "It sounds like two people arguing."
    thought "There's a row going on in the bedroom!"
    thought "It sounds like [s3_mc.current_partner]..."
    thought "...And [s3_mc.past_partners[1]]?!"

    # CHOICE
    menu:
        thought "[s3_mc.current_partner] and [s3_mc.past_partners[1]] are arguing!"
        "Listen in":
            $ s3e6p3_listen = True
            call s3e6p3_listen from _call_s3e6p3_listen
        "Don't":
            thought "I'd better just leave them to it."
            "You turn back to the mirror and try to tune the voices out."
            "Seconds later, you clearly hear [s3_mc.past_partners[1]]'s voice say '[s3_name]'."
            thought "Wait... [s3_mc.past_partners[1]] definitely just said my name!"
            # SUB-CHOICE
            menu:
                thought "They're arguing about me!"
                "Listen in":
                    $ s3e6p3_listen = True
                    call s3e6p3_listen from _call_s3e6p3_listen_1
                "Don't":
                    "Eventually the argument dies down."
                    thought "I wonder what that was all about."
                    thought "Well, I'd better finish getting ready for bed, and then go through."

    scene s3-bedroom-night with dissolve
    $ new_scene()

    $ pronouns(s3_mc.past_partners[1])
    "You step into the bedroom and look around."
    "[s3_mc.past_partners[1]] is already in bed with the pillow pulled over [his_her] head."
    "[s3_mc.current_partner] gives you a wave."
    s3_mc "Hey."

    if s3_mc.current_partner == "Yasmin":
        yasmin "Hey."
        yasmin "You look incredible, by the way."
        s3_mc "Thank you."
    elif s3_mc.current_partner == "Tai":
        tai "Hey."
        tai "You look incredible, by the way."
        s3_mc "Thank you."
    elif s3_mc.current_partner == "Ciaran":
        ciaran "Hey."
        ciaran "You look incredible, by the way."
        s3_mc "Thank you."

    $ pronouns(s3_mc.current_partner)
    # CHOICE
    menu:
        thought "I'm sharing a bed with [s3_mc.current_partner]..."
        "Keep to my own side":
            "You climb into bed on your side, and [s3_mc.current_partner] lies down on the other side."
            thought "Let's just pretend there's an invisible line down the middle of the bed."
        "Cuddle up to [him_her]":
            $ s3_mc.like(s3_mc.current_partner)
            "You snuggle down under the covers and extend a hand to [s3_mc.current_partner]."
            "[he_she!c] smiles and climbs in next to you, wrapping an arm around your waist."
            "You rest your head on [his_her] chest."
        "Steal all the covers":
            $ s3_mc.dislike(s3_mc.current_partner)
            "You jump into bed and roll over, wrapping all the covers around your body like a sausage roll."
            if s3_mc.current_partner == "Yasmin":
                yasmin "Hey! It's cold!"
            elif s3_mc.current_partner == "Tai":
                tai "Hey! It's cold!"
            elif s3_mc.current_partner == "Ciaran":
                ciaran "Hey! It's cold!"
            s3_mc "Then you should've packed warmer pyjamas."

    "The bedroom starts to quiet down as one by one, the other Islanders go to sleep."

    if s3e6p3_listen:
        thought "[s3_mc.current_partner] doesn't know I overheard him arguing with [s3_mc.past_partners[1]]..."
        # CHOICE
        menu:
            thought "Should I say something?"
            "Ask [him_her] if [he_she]'s okay after the argument":
                $ s3_mc.like(s3_mc.current_partner)
                s3_mc "So... I couldn't help overhearing you and [s3_mc.past_partners[1]]..."
                if s3_mc.current_partner == "Yasmin":
                    yasmin "Oh, boy. You heard that, did you?"
                    yasmin "I'm sorry."
                elif s3_mc.current_partner == "Tai":
                    tai "Oh, boy. You heard that, did you?"
                    tai "I'm sorry."
                elif s3_mc.current_partner == "Ciaran":
                    ciaran "Oh, boy. You heard that, did you?"
                    ciaran "I'm sorry."
                s3_mc "Hey, it's okay."
                s3_mc "Are you feeling alright?"
                if s3_mc.current_partner == "Yasmin":
                    yasmin "Yeah. Yeah, I'm fine."
                    yasmin "Thanks for asking."
                    yasmin "All the emotion just kind of reached boiling point, for both of us."
                    yasmin "For what it's worth..."
                    yasmin "I stand by everything I said. I meant every word."
                elif s3_mc.current_partner == "Tai":
                    tai "Yeah. Yeah, I'm fine."
                    tai "Thanks for asking."
                    tai "All the emotion just kind of reached boiling point, for both of us."
                    tai "For what it's worth..."
                    tai "I stand by everything I said. I meant every word."
                elif s3_mc.current_partner == "Ciaran":
                    ciaran "Yeah. Yeah, I'm fine."
                    ciaran "Thanks for asking."
                    ciaran "All the emotion just kind of reached boiling point, for both of us."
                    ciaran "For what it's worth..."
                    ciaran "I stand by everything I said. I meant every word."
                s3_mc "I could tell."
            "Tell [him_her] not to fight with [s3_mc.past_partners[1]] again":
                s3_mc "So, I heard you and [s3_mc.past_partners[1]] fighting."
                if s3_mc.current_partner == "Yasmin":
                    yasmin "Oh... you did?"
                elif s3_mc.current_partner == "Tai":
                    tai "Oh... you did?"
                elif s3_mc.current_partner == "Ciaran":
                    ciaran "Oh... you did?"
                s3_mc "Yeah. And I don't want to hear it again, please."
                if s3_mc.current_partner == "Yasmin":
                    yasmin "I'm sorry."
                    yasmin "All the emotion just kind of reached boiling point, for both of us."
                    yasmin "For what it's worth..."
                    yasmin "I stand by everything I said. I meant every word."
                elif s3_mc.current_partner == "Tai":
                    tai "I'm sorry."
                    tai "All the emotion just kind of reached boiling point, for both of us."
                    tai "For what it's worth..."
                    tai "I stand by everything I said. I meant every word."
                elif s3_mc.current_partner == "Ciaran":
                    ciaran "I'm sorry."
                    ciaran "All the emotion just kind of reached boiling point, for both of us."
                    ciaran "For what it's worth..."
                    ciaran "I stand by everything I said. I meant every word."
                s3_mc "I could tell."
            "Keep quiet":
                "You bite your tongue."
                if s3_mc.current_partner == "Yasmin":
                    yasmin "Were you about to say something?"
                elif s3_mc.current_partner == "Tai":
                    tai "Were you about to say something?"
                elif s3_mc.current_partner == "Ciaran":
                    ciaran "Were you about to say something?"
                s3_mc "No, it's nothing."
    else:
        "In the dark [s3_mc.current_partner] speaks to you, [his_her] voice barely above a whisper."

    if s3_mc.current_partner == "Yasmin":
        yasmin "So... about the recoupling..."
    elif s3_mc.current_partner == "Tai":
        tai "So... about the recoupling..."
    elif s3_mc.current_partner == "Ciaran":
        ciaran "So... about the recoupling..."
    
    # CHOICE
    menu:
        thought "Listen, [s3_mc.current_partner]..."
        "I wish you hadn't chosen me":
            $ s3_mc.dislike(s3_mc.current_partner)
            s3_mc "Look, I know you had to choose someone, but why did it have to be me?"
            s3_mc "I just don't see anything happening between us."
            if s3_mc.current_partner == "Yasmin":
                yasmin "...I'm sorry."
            elif s3_mc.current_partner == "Tai":
                tai "...I'm sorry."
            elif s3_mc.current_partner == "Ciaran":
                ciaran "...I'm sorry."
        "I'm glad you chose me":
            $ s3_mc.like(s3_mc.current_partner)
            s3_mc "I'm really excited to see how things go between us."
            s3_mc "I like you, [s3_mc.current_partner]."
            if s3_mc.current_partner == "Yasmin":
                yasmin "I like you too, [s3_name]."
            elif s3_mc.current_partner == "Tai":
                tai "I like you too, [s3_name]."
            elif s3_mc.current_partner == "Ciaran":
                ciaran "I like you too, [s3_name]."
        "Let's see how this goes":
            $ s3_mc.like(s3_mc.current_partner)
            s3_mc "No promises. But I'm open to seeing what happens between us."
            if s3_mc.current_partner == "Yasmin":
                yasmin "Thanks for giving me a chance."
            elif s3_mc.current_partner == "Tai":
                tai "Thanks for giving me a chance."
            elif s3_mc.current_partner == "Ciaran":
                ciaran "Thanks for giving me a chance."

    if s3_mc.current_partner == "Yasmin":
        yasmin "And about [s3_mc.past_partners[1]]...?"
    elif s3_mc.current_partner == "Tai":
        tai "And about [s3_mc.past_partners[1]]...?"
    elif s3_mc.current_partner == "Ciaran":
        ciaran "And about [s3_mc.past_partners[1]]...?"
        
    $ pronouns(s3_mc.past_partners[1])
    # CHOICE
    menu:
        thought "Here's the thing about [s3_mc.past_partners[1]]..."
        "I do still fancy [him_her]...":
            $ s3_mc.dislike(s3_mc.current_partner)
            $ s3_mc.like(s3_mc.past_partners[1])
            s3_mc "Just because I'm coupled up with you doesn't mean my feelings for [him_her] just go away."
            if s3_mc.current_partner == "Yasmin":
                yasmin "Of course. I get it."
                yasmin "It's cool if you want to keep chatting to [him_her]. It's not like you have to choose between us right now or anything."
            elif s3_mc.current_partner == "Tai":
                tai "Of course. I get it."
                tai "It's cool if you want to keep chatting to [him_her]. It's not like you have to choose between us right now or anything."
            elif s3_mc.current_partner == "Ciaran":
                ciaran "Of course. I get it."
                ciaran "It's cool if you want to keep chatting to [him_her]. It's not like you have to choose between us right now or anything."
        "That's all in the past":
            s3_mc "I'm with you now. Maybe [s3_mc.past_partners[1]] will connect with [s3e6p3_other]"
            if s3_mc.current_partner == "Yasmin":
                yasmin "Yeah, you're probably right."
                yasmin "I'm glad you're so chill about it."
            elif s3_mc.current_partner == "Tai":
                tai "Yeah, you're probably right."
                tai "I'm glad you're so chill about it."
            elif s3_mc.current_partner == "Ciaran":
                ciaran "Yeah, you're probably right."
                ciaran "I'm glad you're so chill about it."
        "[he_she!c]'s the only one for me":
            $ s3e6p3_loyal = True
            $ s3_mc.dislike(s3_mc.current_partner)
            $ s3_mc.like(s3_mc.past_partners[1])
            s3_mc "We're totally endgame."
            "[s3_mc.current_partner] sighs."
            if s3_mc.current_partner == "Yasmin":
                yasmin "Understood. Well, I feel bad for splitting you up, then."
                yasmin "I won't try to be all coupley with you if you still have feelings for [s3_mc.past_partners[1]]."
            elif s3_mc.current_partner == "Tai":
                tai "Understood. Well, I feel bad for splitting you up, then."
                tai "I won't try to be all coupley with you if you still have feelings for [s3_mc.past_partners[1]]."
            elif s3_mc.current_partner == "Ciaran":
                ciaran "Understood. Well, I feel bad for splitting you up, then."
                ciaran "I won't try to be all coupley with you if you still have feelings for [s3_mc.past_partners[1]]."

    $ pronouns(s3_mc.current_partner)
    "You can hear [him_her] fidgeting, trying to get comfortable."

    if s3e6p3_loyal:
        $ pronouns(s3_mc.past_partner[1])
        thought "Maybe I should go and say goodnight to [s3_mc.past_partner[1]]."
        thought "[he_she!c] might be asleep already... but it's worth a try..."

        # CHOICE
        menu:
            thought "Should I go and say goodnight to [s3_mc.past_partner[1]]"
            "Yell 'goodnight' to [him_her]":
                # NEED TO FILL
                "EMPTY"
            "Just go to sleep":
                thought "Today's already been long enough."
                "You snuggle down under the covers."
            "Sneak over to [his_her] bed":
                "You quietly roll out of bed and tiptoe across the room to where [s3_mc.past_partner[1]] is lying."
                "You give [him_her] a prod, trying not to disturb [s3e6p3_other], who's asleep beside [him_her]."
                s3_mc "[s3_mc.past_partners[1]]..."
                s3_mc "Are you awake?"
                "[he_she!c] whispers back."
                if s3_mc.past_partners[1] == "Bill":
                    bill "[s3_name], isn't that you? What's the matter?"
                elif s3_mc.past_partners[1] == "Camilo":
                    camilo "[s3_name], isn't that you? What's the matter?"
                elif s3_mc.past_partners[1] == "Harry":
                    harry "[s3_name], isn't that you? What's the matter?"
                elif s3_mc.past_partners[1] == "AJ":
                    aj "[s3_name], isn't that you? What's the matter?"
                s3_mc "Nothing, babe."
        # CHOICE
        menu:
            thought "I just came over to..."
            "Say goodnight":
                $ s3_mc.like(s3_mc.past_partners[1])
                if s3_mc.past_partners[1] == "Bill":
                    bill "Aw."
                    bill "Well, goodnight to you too."
                elif s3_mc.past_partners[1] == "Camilo":
                    camilo "Aw."
                    camilo "Well, goodnight to you too."
                elif s3_mc.past_partners[1] == "Harry":
                    harry "Aw."
                    harry "Well, goodnight to you too."
                elif s3_mc.past_partners[1] == "AJ":
                    aj "Aw."
                    aj "Well, goodnight to you too."
            "Steal a kiss":
                $ s3_mc.like(s3_mc.past_partners[1])
                "[s3_mc.past_partners[1]] grins in the dark."
                if s3_mc.past_partners[1] == "Bill":
                    bill "Go on, then."
                elif s3_mc.past_partners[1] == "Camilo":
                    camilo "Go on, then."
                elif s3_mc.past_partners[1] == "Harry":
                    harry "Go on, then."
                elif s3_mc.past_partners[1] == "AJ":
                    aj "Go on, then."
                "You lean in and press your lips to [his_her]."
                "[he_she!c] draws a shaky breath when you pull away."
            "Check if you and [s3e6p3_other] were doing bits" if s3_mc.current_partner != "Yasmin":
                if s3_mc.past_partners[1] == "Bill":
                    bill "What? No!"
                    s3_mc "Cool. Just thought I'd check."
                    bill "Well, it's nice to hear your voice anyway, whatever the reason."
                elif s3_mc.past_partners[1] == "Camilo":
                    camilo "What? No!"
                    s3_mc "Cool. Just thought I'd check."
                    camilo "Well, it's nice to hear your voice anyway, whatever the reason."
                elif s3_mc.past_partners[1] == "Harry":
                    harry "What? No!"
                    s3_mc "Cool. Just thought I'd check."
                    harry "Well, it's nice to hear your voice anyway, whatever the reason."
                elif s3_mc.past_partners[1] == "AJ":
                    aj "What? No!"
                    s3_mc "Cool. Just thought I'd check."
                    aj "Well, it's nice to hear your voice anyway, whatever the reason."

        if s3_mc.past_partners[1] == "Bill":
            bill "How are things over there with you and [s3_mc.current_partner]?"
            s3_mc "We talked. I explained how I feel about the whole situation."
            bill "Well, that's good. It's important to let people know where you stand."
        elif s3_mc.past_partners[1] == "Camilo":
            camilo "How are things over there with you and [s3_mc.current_partner]?"
            s3_mc "We talked. I explained how I feel about the whole situation."
            camilo "Well, that's good. It's important to let people know where you stand."
        elif s3_mc.past_partners[1] == "Harry":
            harry "How are things over there with you and [s3_mc.current_partner]?"
            s3_mc "We talked. I explained how I feel about the whole situation."
            harry "Well, that's good. It's important to let people know where you stand."
        elif s3_mc.past_partners[1] == "AJ":
            aj "How are things over there with you and [s3_mc.current_partner]?"
            s3_mc "We talked. I explained how I feel about the whole situation."
            aj "Well, that's good. It's important to let people know where you stand."
        
        s3_mc "Yeah..."

        if s3e6p3_listen:
            s3_mc "I overheard you and [s3_mc.current_partner] making it pretty clear where you both stood earlier."
            if s3_mc.past_partners[1] == "Bill":
                bill "Oh... I'm sorry you heard that."
                bill "I just couldn't let you go without saying how I felt."
            elif s3_mc.past_partners[1] == "Camilo":
                camilo "Oh... I'm sorry you heard that."
                camilo "I just couldn't let you go without saying how I felt."
            elif s3_mc.past_partners[1] == "Harry":
                harry "Oh... I'm sorry you heard that."
                harry "I just couldn't let you go without saying how I felt."
            elif s3_mc.past_partners[1] == "AJ":
                aj "Oh... I'm sorry you heard that."
                aj "I just couldn't let you go without saying how I felt."
            s3_mc "I know."

        if s3_mc.past_partners[1] == "Bill":
            bill "Thanks for coming over, [s3_name]. It's always nice to see you."
            s3_mc "Even in the dark?"
            bill "Even in the dark."
            bill "Sleep well, babe."
        elif s3_mc.past_partners[1] == "Camilo":
            camilo "Thanks for coming over, [s3_name]. It's always nice to see you."
            s3_mc "Even in the dark?"
            camilo "Even in the dark."
            camilo "Sleep well, babe."
        elif s3_mc.past_partners[1] == "Harry":
            harry "Thanks for coming over, [s3_name]. It's always nice to see you."
            s3_mc "Even in the dark?"
            harry "Even in the dark."
            harry "Sleep well, babe."
        elif s3_mc.past_partners[1] == "AJ":
            aj "Thanks for coming over, [s3_name]. It's always nice to see you."
            s3_mc "Even in the dark?"
            aj "Even in the dark."
            aj "Sleep well, babe."
            
        s3_mc "You too, [s3_mc.past_partners[1]]."
        "You tiptoe back and slip under the covers."
    else:
        $ pronouns(s3_mc.current_partner)
        if s3_mc.current_partner == "Yasmin":
            yasmin "So.. tell me to get lost if this is too much right now, but..."
            yasmin "Can I kiss you?"
        elif s3_mc.current_partner == "Tai":
            tai "So.. tell me to get lost if this is too much right now, but..."
            tai "Can I kiss you?"
        elif s3_mc.current_partner == "Ciaran":
            ciaran "So.. tell me to get lost if this is too much right now, but..."
            ciaran "Can I kiss you?"

        # CHOICE
        menu:
            thought "[s3_mc.current_partner] wants to kiss me..."
            "I'd prefer a hug":
                $ s3_mc.like(s3_mc.current_partner)
                if s3_mc.current_partner == "Yasmin":
                    yasmin "Coming right up."
                elif s3_mc.current_partner == "Tai":
                    tai "Coming right up."
                elif s3_mc.current_partner == "Ciaran":
                    ciaran "Coming right up."
                call s3e6p3_cuddle from _call_s3e6p3_cuddle
            "Don't push your luck":
                s3_mc "Have a little patience, babe!"
                if s3_mc.current_partner == "Yasmin":
                    yasmin "Fair enough!"
                    yasmin "Just thought I'd give you the option."
                elif s3_mc.current_partner == "Tai":
                    tai "Fair enough!"
                    tai "Just thought I'd give you the option."
                elif s3_mc.current_partner == "Ciaran":
                    ciaran "Fair enough!"
                    ciaran "Just thought I'd give you the option."
            "A kiss would be lovely":
                $ s3e6p3_kiss = True
                s3_mc "I mean, if you want to..."
                if s3_mc.current_partner == "Yasmin":
                    "She gently traces a finger down your cheek."
                    yasmin "You already know I do, you mystically powerful pegasus."
                elif s3_mc.current_partner == "Tai":
                    "In the dark, all you can see are his teeth as he breaks into his huge grin."
                    tai "That can be arranged."
                elif s3_mc.current_partner == "Ciaran":
                    "You hear his breath catch in his throat."
                    ciaran "I wanted to be the one to ask."
                    ciaran "But I was worried you might say no."
                    s3_mc "Then stop worrying, babe."
                "[s3_mc.current_partner] dips [his_her] head and presses a kiss to your shoulder."
                "Slowly, [he_she] moves upwards, [his_her] lips grazing the length of your throat and up to your jaw."
                "You shiver as you finally feel [his_her] breath behind your ear."

                if s3_mc.current_partner == "Yasmin":
                    yasmin "Do you want me to keep going?"
                elif s3_mc.current_partner == "Tai":
                    tai "Do you want me to keep going?"
                elif s3_mc.current_partner == "Ciaran":
                    ciaran "Do you want me to keep going?"

                # SUB-CHOICE
                menu:
                    thought "What shall we do now..."
                    "Let's make out":
                        # NEED TO FILL
                        "EMPTY"
                    "Let's just cuddle":
                        $ s3_mc.like(s3_mc.current_partner)
                        if s3_mc.current_partner == "Yasmin":
                            yasmin "What a good idea."
                        elif s3_mc.current_partner == "Tai":
                            tai "What a good idea."
                        elif s3_mc.current_partner == "Ciaran":
                            ciaran "What a good idea."
                        call s3e6p3_cuddle from _call_s3e6p3_cuddle_1
                    "Let's do some bits":
                        $ s3e6p3_bits = True
                        $ s3_mc.like(s3_mc.current_partner)
                        s3_mc "[s3_mc.current_partner], I want you. Right now."
                        "Without another word, [s3_mc.current_partner] pulls your body against [his_her]s."
                        "You can feel [him_her] smiling as [he_she] kisses you, softly at first, then harder and deeper."
                        "You give a shiver of pleasure as [his_her] hands slip under your pyjamas, roaming across your skin."
                        "Your hands tangle in [his_her] hair as [he_she] slides under the covers..."

                        if s3_mc.current_partner == "Yasmin":
                            "Yasmin seems to know what you need, even without words."
                            "When you open your mouth to tell her how good it feels, no sound comes out, but you know she understands by the grip of her hands on your thighs."
                        elif s3_mc.current_partner == "Tai":
                            "Tai is cocky, and he has the stamina to match."
                            "One second he has you giggling, then the next, you're moaning."
                        elif s3_mc.current_partner == "Ciaran":
                            "Ciaran is eager to please."
                            "He pays attention to every sound you make and the tiny details that make your back arch with excitement."
                        
                        "When it's over you lie in the dark, your chest heaving, and watch the stars slowly clear from your vision."
                        call s3e6p3_cuddle from _call_s3e6p3_cuddle_2

                        if s3_mc.current_partner == "Yasmin":
                            yasmin "That, just now..."
                            yasmin "That was cosmic."
                            s3_mc "What does that actually mean?"
                            yasmin "Good. But like, really really good."
                        elif s3_mc.current_partner == "Tai":
                            tai "That, just now..."
                            tai "That was legendary."
                            if s3e5p2_waterfall_bits:
                                tai "I know it's not exactly 'behind a waterfall' levels of cinematic romance, but..."
                            tai "I won't be forgetting it in a hurry."
                        elif s3_mc.current_partner == "Ciaran":
                            ciaran "That, just now..."
                            ciaran "That was amazing."
                            ciaran "I thought I had it bad for you before, but now I don't think there's any coming back for me."
    
                        # SUB-CHOICE
                        menu:
                            thought "[s3_mc.current_partner] had a good time..."
                            "Shh, let's just be here":
                                # NEED TO FILL
                                "EMPTY"
                            "You were great, babe":
                                $ s3_mc.like(s3_mc.current_partner)
                                s3_mc "It was exactly what I needed after today."
                                s3_mc "I think we made a real connection, you know?"
                                if s3_mc.current_partner == "Yasmin":
                                    yasmin "I'm glad you felt it too."
                                elif s3_mc.current_partner == "Tai":
                                    tai "I'm glad you felt it too."
                                elif s3_mc.current_partner == "Ciaran":
                                    ciaran "I'm glad you felt it too."
                            "Let's not make a habit of it, yeah?":
                                $ s3_mc.dislike(s3_mc.current_partner)
                                s3_mc "There's no guarantee it'll ever happen again."
                                "[he_she!c] sighs."
                                if s3_mc.current_partner == "Yasmin":
                                    yasmin "I know."
                                elif s3_mc.current_partner == "Tai":
                                    tai "I know."
                                elif s3_mc.current_partner == "Ciaran":
                                    ciaran "I know."
    
                        "You lie wrapped up in each other for a while."

    "Your eyes start to grow heavy as sleep takes over your brain."
    "[s3_mc.current_partner] murmurs."

    if s3_mc.current_partner == "Yasmin":
        yasmin "Goodnight, then, [s3_name]."
        yasmin "Sleep well."
    elif s3_mc.current_partner == "Tai":
        tai "Goodnight, then, [s3_name]."
        tai "Sleep well."
    elif s3_mc.current_partner == "Ciaran":
        ciaran "Goodnight, then, [s3_name]."
        ciaran "Sleep well."

    scene sand with dissolve
    $ new_scene()
    $ outfit = "evening"

    "Well, here we are at the part where I give you a tantalising glimpse of the drama and romance that's in store for our Islanders tomorrow."
    "But first, I did promise you a joke."
    "Are you ready?"
    "Ahem..."
    "What would you call a knock-off version of the Villa's resident Brazilian jiu-jitsu expert?"
    "..."
    "Shamilo."
    "Get it? Like 'sham' sounds like 'Cam'?"
    "Fine, here's your teaser."
    iona "I can't watch!"
    $ leaving("iona")
    "Happy now?"
    "I'm wasted on you people..."

    # jump s3e7p1

    "Thanks that is all that is completed up til now."
    "Hope you enjoyed it and please send any errors or bugs you found to soupdad on discord :))"
    return

label s3e6p3_listen:
    "You tiptoe over to the wall and put your ear up against it."
    "You can hear the two of them arguing back and forth..."

    scene s3-bedroom-night with dissolve
    $ new_scene()

    if s3_mc.past_partners[1] == "Bill":
        bill "Look. I'm not trying to start anything."
        bill "I'm just telling you straight how I feel."
    elif s3_mc.past_partners[1] == "Camilo":
        camilo "Look. I'm not trying to start anything."
        camilo "I'm just telling you straight how I feel."
    elif s3_mc.past_partners[1] == "Harry":
        harry "Look. I'm not trying to start anything."
        harry "I'm just telling you straight how I feel."
    elif s3_mc.past_partners[1] == "AJ":
        aj "Look. I'm not trying to start anything."
        aj "I'm just telling you straight how I feel."

    if s3_mc.current_partner == "Yasmin":
        yasmin "Well, it feels like you're making me out to be the villain in this situation."
        yasmin "Why are you being so possessive? It's not my fault I had to make a decision."
    elif s3_mc.current_partner == "Tai":
        tai "Well, it feels like you're making me out to be the villain in this situation."
        tai "Why are you being so possessive? It's not my fault I had to make a decision."
    elif s3_mc.current_partner == "Ciaran":
        ciaran "Well, it feels like you're making me out to be the villain in this situation."
        ciaran "Why are you being so possessive? It's not my fault I had to make a decision."

    if s3_mc.past_partners[1] == "Bill":
        bill "But why did it have to be her?"
    elif s3_mc.past_partners[1] == "Camilo":
        camilo "But why did it have to be her?"
    elif s3_mc.past_partners[1] == "Harry":
        harry "But why did it have to be her?"
    elif s3_mc.past_partners[1] == "AJ":
        aj "But why did it have to be her?"

    if s3e6p1_break_up:
        if s3_mc.past_partners[1] == "Bill":
            bill "I already kinda had the feeling I was losing [s3_name]. I don't think she likes me as much as I like her."
            bill "I just wanted one more chance to make things work!"
        elif s3_mc.past_partners[1] == "Camilo":
            camilo "I already kinda had the feeling I was losing [s3_name]. I don't think she likes me as much as I like her."
            camilo "I just wanted one more chance to make things work!"
        elif s3_mc.past_partners[1] == "Harry":
            harry "I already kinda had the feeling I was losing [s3_name]. I don't think she likes me as much as I like her."
            harry "I just wanted one more chance to make things work!"
        elif s3_mc.past_partners[1] == "AJ":
            aj "I already kinda had the feeling I was losing [s3_name]. I don't think she likes me as much as I like her."
            aj "I just wanted one more chance to make things work!"
    else:
        if s3_mc.past_partners[1] == "Bill":
            bill "We've got something special."
            bill "That girl means the world to me, and I know I mean something to her, too."
            bill "I can't believe you would get in the middle of that right when we're about to..."
            "[s3_mc.past_partners[1]]'s voice cuts off suddenly."
            "When you hear it again, it's a little more controlled."
            bill "It's just wrong, mate. It's wrong."
        elif s3_mc.past_partners[1] == "Camilo":
            camilo "We've got something special."
            camilo "That girl means the world to me, and I know I mean something to her, too."
            camilo "I can't believe you would get in the middle of that right when we're about to..."
            "[s3_mc.past_partners[1]]'s voice cuts off suddenly."
            "When you hear it again, it's a little more controlled."
            camilo "It's just wrong, mate. It's wrong."
        elif s3_mc.past_partners[1] == "Harry":
            harry "We've got something special."
            harry "That girl means the world to me, and I know I mean something to her, too."
            harry "I can't believe you would get in the middle of that right when we're about to..."
            "[s3_mc.past_partners[1]]'s voice cuts off suddenly."
            "When you hear it again, it's a little more controlled."
            harry "It's just wrong, mate. It's wrong."
        elif s3_mc.past_partners[1] == "AJ":
            aj "We've got something special."
            aj "That girl means the world to me, and I know I mean something to her, too."
            aj "I can't believe you would get in the middle of that right when we're about to..."
            "[s3_mc.past_partners[1]]'s voice cuts off suddenly."
            "When you hear it again, it's a little more controlled."
            aj "It's just wrong, mate. It's wrong."

    $ pronouns(s3_mc.past_partners[1])
    # CHOICE
    menu:
        thought "Wow, [s3_mc.past_partners[1]] is really into me..."
        "Obviously, I'm the whole package":
            thought "It's nice to be this amazing."
        "It's sad we're not together now...":
            thought "But would I want to get back with [him_her]?"
        "We'll get back together soon":
            thought "Next chance I get, I'm grabbing [him_her] and never letting [him_her] go."

    if s3_mc.current_partner == "Yasmin":
        yasmin "I do get it."
        yasmin "But mate..."
        yasmin "I had to follow my heart. And all my heart keeps telling me is '[s3_name].'"
    elif s3_mc.current_partner == "Tai":
        tai "I do get it."
        tai "But mate..."
        tai "I had to follow my heart. And all my heart keeps telling me is '[s3_name].'"
    elif s3_mc.current_partner == "Ciaran":
        ciaran "I do get it."
        ciaran "But mate..."
        ciaran "I had to follow my heart. And all my heart keeps telling me is '[s3_name].'"

    if s3_mc.current_partner == "Yasmin" and s3e5p2_confess_attraction_yasmin:
        yasmin "We have a real spark. I like her, and I think she likes me too."
        yasmin "If you'd been paying more attention, you might have noticed."
        if s3_mc.past_partners[1] == "Bill":
            bill "What's that supposed to mean?"
        elif s3_mc.past_partners[1] == "Camilo":
            camilo "What's that supposed to mean?"
        elif s3_mc.past_partners[1] == "Harry":
            harry "What's that supposed to mean?"
        elif s3_mc.past_partners[1] == "AJ":
            aj "What's that supposed to mean?"
        yasmin "Nothing, nothing!"
        yasmin "There's been chemistry. Let's leave it at that."
    elif s3_mc.current_partner == "Tai" and s3e5p2_confess_attraction_tai:
        tai "We have a real spark. I like her, and I think she likes me too."
        tai "If you'd been paying more attention, you might have noticed."
        if s3_mc.past_partners[1] == "Bill":
            bill "What's that supposed to mean?"
        elif s3_mc.past_partners[1] == "Camilo":
            camilo "What's that supposed to mean?"
        elif s3_mc.past_partners[1] == "Harry":
            harry "What's that supposed to mean?"
        elif s3_mc.past_partners[1] == "AJ":
            aj "What's that supposed to mean?"
        tai "Nothing, nothing!"
        tai "There's been chemistry. Let's leave it at that."
    elif s3_mc.current_partner == "Ciaran" and s3e5p2_confess_attraction_ciaran:
        ciaran "We have a real spark. I like her, and I think she likes me too."
        ciaran "If you'd been paying more attention, you might have noticed."
        if s3_mc.past_partners[1] == "Bill":
            bill "What's that supposed to mean?"
        elif s3_mc.past_partners[1] == "Camilo":
            camilo "What's that supposed to mean?"
        elif s3_mc.past_partners[1] == "Harry":
            harry "What's that supposed to mean?"
        elif s3_mc.past_partners[1] == "AJ":
            aj "What's that supposed to mean?"
        ciaran "Nothing, nothing!"
        ciaran "There's been chemistry. Let's leave it at that."

    if s3_mc.current_partner == "Yasmin" and s3e5p2_confess_attraction_yasmin == False:
        yasmin "I don't know if she likes me back in the same way. In fact, I'm worried she doesn't."
        "You hear [s3_mc.past_partners[1]] scoff."
        yasmin "But I just couldn't walk out of here without doing something. I would've been kicking myself for the rest of my life."
    elif s3_mc.current_partner == "Tai" and s3e5p2_confess_attraction_tai == False:
        tai "I don't know if she likes me back in the same way. In fact, I'm worried she doesn't."
        "You hear [s3_mc.past_partners[1]] scoff."
        tai "But I just couldn't walk out of here without doing something. I would've been kicking myself for the rest of my life."
    elif s3_mc.current_partner == "Ciaran" and s3e5p2_confess_attraction_ciaran == False:
        ciaran "I don't know if she likes me back in the same way. In fact, I'm worried she doesn't."
        "You hear [s3_mc.past_partners[1]] scoff."
        ciaran "But I just couldn't walk out of here without doing something. I would've been kicking myself for the rest of my life."

    if s3_mc.current_partner == "Yasmin":
        yasmin "Besides..."
        if s3_mc.past_partners[1] == "Bill":
            yasmin "I thought you and Miki were a better match."
            bill "I mean, don't get me wrong, I like her."
            bill "But she's not [s3_name]."
            yasmin "Well, I guess it'll be up to her in the end, won't it?"
            bill "I guess it will."
            yasmin "Fine."
            bill "Fine."
        elif s3_mc.past_partners[1] == "Camilo":
            yasmin "I thought you and Iona were a better match."
            camilo "I mean, don't get me wrong, I like her."
            camilo "But she's not [s3_name]."
            yasmin "Well, I guess it'll be up to her in the end, won't it?"
            camilo "I guess it will."
            yasmin "Fine."
            camilo "Fine."
        elif s3_mc.past_partners[1] == "Harry":
            yasmin "I thought you and Genevieve were a better match."
            harry "I mean, don't get me wrong, I like her."
            harry "But she's not [s3_name]."
            yasmin "Well, I guess it'll be up to her in the end, won't it?"
            harry "I guess it will."
            yasmin "Fine."
            harry "Fine."
        elif s3_mc.past_partners[1] == "AJ":
            yasmin "I thought something was happening between you and Seb."
            aj "What? How could you possibly think that?"
            yasmin "I don't know. When you were coupled up with him, it seemed a bit like you were both in denial about liking each other."
            aj "Well, we're not. He supported me coupling up with [s3_name]."
            yasmin "Well, I guess it'll be up to her in the end, won't it?"
            aj "I guess it will."
            yasmin "Fine."
            aj "Fine."
    elif s3_mc.current_partner == "Tai":
        tai "Besides..."
        if s3_mc.past_partners[1] == "Bill":
            tai "I thought you and Miki were a better match."
            bill "I mean, don't get me wrong, I like her."
            bill "But she's not [s3_name]."
            tai "Well, I guess it'll be up to her in the end, won't it?"
            bill "I guess it will."
            tai "Fine."
            bill "Fine."
        elif s3_mc.past_partners[1] == "Camilo":
            tai "I thought you and Iona were a better match."
            camilo "I mean, don't get me wrong, I like her."
            camilo "But she's not [s3_name]."
            tai "Well, I guess it'll be up to her in the end, won't it?"
            camilo "I guess it will."
            tai "Fine."
            camilo "Fine."
        elif s3_mc.past_partners[1] == "Harry":
            tai "I thought you and Genevieve were a better match."
            harry "I mean, don't get me wrong, I like her."
            harry "But she's not [s3_name]."
            tai "Well, I guess it'll be up to her in the end, won't it?"
            harry "I guess it will."
            tai "Fine."
            harry "Fine."
        elif s3_mc.past_partners[1] == "AJ":
            tai "I thought something was happening between you and Seb."
            aj "What? How could you possibly think that?"
            tai "I don't know. When you were coupled up with him, it seemed a bit like you were both in denial about liking each other."
            aj "Well, we're not. He supported me coupling up with [s3_name]."
            tai "Well, I guess it'll be up to her in the end, won't it?"
            aj "I guess it will."
            tai "Fine."
            aj "Fine."
    elif s3_mc.current_partner == "Ciaran":
        ciaran "Besides..."
        if s3_mc.past_partners[1] == "Bill":
            ciaran "I thought you and Miki were a better match."
            bill "I mean, don't get me wrong, I like her."
            bill "But she's not [s3_name]."
            ciaran "Well, I guess it'll be up to her in the end, won't it?"
            bill "I guess it will."
            ciaran "Fine."
            bill "Fine."
        elif s3_mc.past_partners[1] == "Camilo":
            ciaran "I thought you and Iona were a better match."
            camilo "I mean, don't get me wrong, I like her."
            camilo "But she's not [s3_name]."
            ciaran "Well, I guess it'll be up to her in the end, won't it?"
            camilo "I guess it will."
            ciaran "Fine."
            camilo "Fine."
        elif s3_mc.past_partners[1] == "Harry":
            ciaran "I thought you and Genevieve were a better match."
            harry "I mean, don't get me wrong, I like her."
            harry "But she's not [s3_name]."
            ciaran "Well, I guess it'll be up to her in the end, won't it?"
            harry "I guess it will."
            ciaran "Fine."
            harry "Fine."
        elif s3_mc.past_partners[1] == "AJ":
            ciaran "I thought something was happening between you and Seb."
            aj "What? How could you possibly think that?"
            ciaran "I don't know. When you were coupled up with him, it seemed a bit like you were both in denial about liking each other."
            aj "Well, we're not. He supported me coupling up with [s3_name]."
            ciaran "Well, I guess it'll be up to her in the end, won't it?"
            aj "I guess it will."
            ciaran "Fine."
            aj "Fine."

    "You hear them both fall silent, then the sound of someone crawling into bed."

    scene s3-dressing-room with dissolve
    $ new_scene()

    thought "Wow. I can't believe I just heard that."

    # CHOICE
    menu:
        thought "[s3_mc.current_partner] and [s3_mc.past_partners[1]] fighting over me..."
        "Aw, I feel bad for them":
            thought "I never meant for this to happen."
        "Ugh, they're being childish":
            thought "If they can't handle their feelings like adults, that's their problem."
        "Hey, this is awesome":
            if s3_mc.past_partners[1] == "AJ":
                if s3_mc.current_partner == "Yasmin":
                    thought "I've got two beautiful girls fighting for my attention. I'm living the dream."
                else:
                    thought "I've got a beautiful girl and a handsome guy fighting for my attention. I'm living the bisexual dream."
            else:
                if s3_mc.current_partner == "Yasmin":
                    thought "I've got a beautiful girl and a handsome guy fighting for my attention. I'm living the bisexual dream."
                else:
                    thought "I've got two handsome guys fighting for my attention. I'm living the dream."

    thought "I wonder if I should tell them I heard everything..."
    thought "Well, I'd better finish getting ready for bed, and then go through."
    "Wow. Harsh words there from [s3_mc.past_partners[1]] and [s3_mc.current_partner]."
    "I'm sure they'll both have calmed down by the morning..."
    "Won't they..."

    return

label s3e6p3_choice:
    $ pronouns(s3e6p3_li)

    # CHOICE
    menu:
        thought "[s3e6p3_li] chose me!"
        "Hug [him_her]":
            $ s3_mc.like(s3e6p3_li)
            $ s3_mc.dislike(s3_mc.current_partner)
            $ s3e6p3_good_couple = True
            "You throw your arms around [him_her] neck, and [he_she] hugs you back, laughing."
            "[he_she!c] takes your hand and leads you to the bench, where you sit down together."
            "[s3_mc.current_partner] stares into the firepit and frowns."
        "Hug [s3_mc.current_partner]":
            $ s3_mc.like(s3_mc.current_partner)
            $ s3_mc.dislike(s3e6p3_li)
            $ s3e6p3_hug_old_li = True
            "You throw your arms around [s3_mc.current_partner], who hugs you back sadly. After a few seconds, you have to pull away."
            s3_mc "I'm sorry, babe."
            "[s3e6p3_li] looks awkwardly at the ground as you take your seat next to [him_her]."
        "Stand still in shock":
            thought "I don't know what to do!"
            "You look over at [s3_mc.current_partner], who's staring into the firepit and frowning."
            "Elladine gives you a nudge."
            elladine "Go and sit down, babes."
            "Still stunned, you take a seat next to [s3e6p3_li], who looks awkwardly at [his_her] feet."

    return

label s3e6p3_cuddle:
    "[s3_mc.current_partner] wraps both arms around you and holds you close."
    if s3_mc.current_partner == "Yasmin":
        "Her hair falls across your skin in loose, gentle curls."
        s3_mc "That tickles!"
        yasmin "Sorry..."
        "She starts to brush her away, but you stop her."
        s3_mc "No... it's nice."
    elif s3_mc.current_partner == "Tai":
        "Cradled between his strong arms and broad chest, you feel perfectly safe."
        s3_mc "Your hugs are the best."
        tai "Hey, they're all yours. Whenever you need them."
    elif s3_mc.current_partner == "Ciaran":
        "In the darkness, his pale skin almost looks like it's glowing."
        s3_mc "You're like a nightlight."
        ciaran "Because I make you feel safe?"
        s3_mc "That too."

    return