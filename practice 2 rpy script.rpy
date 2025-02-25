# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character

# The game starts here.

label start:
    scene bg cafe interior
    play music "audio/soft cafe music.mp3" volume 0.5
    "A few minutes go by as you sit and stare at the hot chocolate in front of you going cold. You try to distract yourself from the fact that Elijah is late once again…"
    "Looking around you see all the yummy pastries just waiting on the side wishing they were in your belly right now, some cute little jellyfish lights which look so magical and…"
    play sound "audio/phone buzzing.mp3" volume 0.8
    "Violet" "AGH! Oh um"
    "you blush hoping no one just heard you letting out that yelp. You look down to see messages from Elijah."
    "Elijah" "Heyyyy so don't hate me but I'm not coming.Insteadddd I’ve set you up on a blind date! Ta Daaaaa! Anyways STAY WHERE YOU ARE! Love ya <3"
    play sound "audio/sigh.mp3" volume 0.6
    "Violet" "Why Eli?????"
    "As you debate whether or not to leave the cafe you hear a voice..."
    play sound "audio/footsteps.mp3" volume 0.8

    label sprites:
    "???" "So you must be the famous Violet..."
    show yami smirk
    "You look up from your phone to be met with this random stranger smirking at you"
    "Violet" "Ugh yes, sorry who are you?"
    "???" "Name’s Yami"
    show yami neutral
    "Before you can say anything more Yami sits down in front of you placing his coffee down and looking up at you..You can already feel the intensity from his gaze."
    "Violet" "Well nice to meet you Yami, sorry I was not prepared for this at all"
    "Yami" "Don’t worry about that we’re here now that’s all that matters"
    "Violet" "Yeah anyways as you know my name is Vio-"
    show yami angry
    "Yami" "I was standing alone here for 10 minutes, I was worried I was going to be stood up! Can you imagine how embarrassing that would’ve been for me?"
    "Yami" "So how are you?"
    show yami happy closed
    "Yami lets out a light chuckle"
    "Did he just interrupt me? Rude but ok maybe it’s just first date nerves."

label choices:
    "Pick one out of three options..."
menu:
    "Appeal to Yami: Good now that you’re here.":
                                                jump choices1_a
    "Neutral Response: I’m good thank you, you?":
                                                jump choices1_b
    "Irritate Yami: Well I have been better but I’m fine.":
                                                          jump choices1_c
label choices1_a:
    show yami smirk
    jump choices1_common

label choices1_b:
    show yami uninterested
    jump choices1_common

label choices1_c:
    show yami angry
    jump choices1_common

label choices1_common:
    "Yami" "I’ve had a bit of a morning, you know when you look this good you have all these agencies trying to book you."
    show yami neutral

label start_2:
    "He looks at you waiting for a response but before you can even say a word he continues"
    "Yami" "I mean you probably wouldn’t know, but that’s ok we all start somewhere"
    show yami happy closed
    "You frown annoyed by the comment. You decide to dismiss the comment and try to keep a straight face but you’ll keep this in mind when he next says anything"
    "Yami" "I’m joking pretty lady just relax"
    show yami neutral

label choices_2:
    "Pick one out of three options..."

menu:
    "Appeal to Yami: Awhh so you do think I’m pretty":
                                                     jump choices2_a
    "Neutral Response: I’m all relaxed don’t you worry":
                                                       jump choices2_b
    "Irritate Yami: Oh so now you think I’m pretty? Funny way of showing it":
                                                                            jump choices2_c
label choices2_a:
      show yami happy
      jump choices2_common

label choices2_b:
      show yami neutral
      jump choices2_common

label choices2_c:
      show yami angry 
      jump choices2_common

label choices2_common:
    "Yami" "So what do you think of me?"
    "Oh god is he really asking me this"

label choices_3:
    "Pick one out of three options..."

menu:
    "Appeal to Yami: I’m not surprised you’re a model look at you":
                                                                  jump choices3_a
    "Neutral Response: You seem very nice":
                                          jump choices3_b
    "Irritate Yami: Don’t think you need me to inflate your ego anymore":
                                                                        jump choices3_c
label choices3_a:
      show yami happy closed
      jump choices3_common

label choices3_b:
      show yami happy
      jump choices3_common

label choices3_c:
      show yami angry
      jump choices3_common

label choices3_common:
"You take a closer look at Yami, his long, sweeping eyelashes complimenting his androgynous features.There's a subtle elegance in each flick of his lashes framing his slender eyes, yet a glint of undying certitude emanates."

label start_3:
    "The dappled light filters through the seashell-peppered drapes, casting a soft glow on his golden brown stylishly cut layers."
    "You take a quick glance at his attire and notice that he's decked out in designer brands, each piece adding to his powerful presence."
    "It's like you're living two completely different worlds. His looks are other worldly, almost mesmerising. It’s no wonder he’s a model, but there's one thing that you can't get over-"
    "Yami" "Like what you see? I don't blame you, if I could make money off my looks, I would- oh wait, I do!"
    show yami smirk
    "He's totally full of himself!"
    "All of sudden the waiter brings over the yummiest cake and places it down in front of you. You look at Yami wondering if he had ordered as a little gift, but he looks at you just as confused.The waiter catches onto the confused expressions."
    show yami neutral
    "Waiter" "Sorry I think there’s been a mix up"
    "The waiter picks up the cake and takes it off"
    "Violet" "That was odd aha"
    "Yami" "You should have said it was yours"
    show yami smirk
    "Violet" "I could never, that was someone else’s ord-"
    "Yami" "I would have"
    show yami happy
    "It goes silent for a second as this is the SECOND time he’s interrupted you"
    play sound "audio/sigh.mp3" volume 0.6
    show yami neutral
    "Yami" "Have I done something?"
    "Violet" "No no don’t worry.."
    show yami uninterested
    "Yami" " Hm ok, I didn’t think so"
    show yami neutral
    "Wow I didn’t think he could get anymore ignorant but wait he just did. The urge to want to roll my eyes is unbearable right now."
    show yami happy
    "Yami" "You’ll never guess what I got asked to do this week"
    "Violet" "Um wha-"
    "Yami" "I got asked to model for IMG models, pretty impressive am I right?"
    show yami happy closed
    "Ugh is he only going to talk about himself on this date"

label choices_4:
    "Pick one out of three options..."

menu:
    "Appeal to Yami: That’s amazing, clearly you’re a hot shot":
                                                                jump choices4_a
    "Neutral response: Oh that’s cool! Well done":
                                                  jump choices4_b

    "Irritate Yami: I guess so":
                                jump choices4_a
     
label choices4_a:
    show yami smirk
    jump choices4_common

label choices4_b:
    show yami happy
    jump choices4_common

label choices4_c:
    show yami angry
    jump choices4_common

   

label choices4_common:
    "Violet" ": I actually really like fashion, maybe you could give me some tips?"
    show yami happy closed

label start_4:
    "Yami" "I thought you’d never ask"
    show yami uninterested
    "Yami" "To be honest though some people just get fashion and well others just don't…"
    show yami neutral
    "Yami" "But I guess if I had to give you some tips it would be to figure out your own colour palette whether you're cold, warm or neutral tones always helps."
    "Yami" " And then there’s a whole other route of finding out what season you are in colour terms of course."
    "Hmm so he can actually be helpful..If only he was like this the whole time.."
    "Violet" "Well thank you very much mister top model"
    show yami smirk
    "Yami" "What can I say I’m an all rounder"
    show yami neutral
    play sound "audio/sigh.mp3" volume 0.6
    "Violet" "I feel like I’ve gotten to know about you, soo how about I tell you a little about me?"
    "Yami" "I guess..."
    "Violet" "Well I loveeee and I mean love watching classic romance films"
    show yami uninterested
    "Yami" "Oh yeah?"
    "Wow ok last time I ever talk about myself geez"
    "Violet" "Anywayy..what do you like to watch?"
    show yami neutral
    "Yami" "Oh I don’t like to waste my time watching films, I’d much rather be starring in them you know because I’m a model I could easily land myself an acting role"
    show yami smirk





label sfx:






    return