define narrator = Character(None)
define player = Character("[player_name]")
define coach = Character("Coach Rahman", color="#58d68d")
define scout = Character("Maya Chen", color="#79b8ff")
define captain = Character("Afiq", color="#ffd166")
define analyst = Character("Performance Analyst", color="#d7b7ff")
define fade_to_black = Fade(0.5, 0.5, 0.5, color="#000")

image bg opening_stadium = "images/opening_stadium.png"
image bg stadium_day = "images/stadium_day.png"
image bg training_ground = "images/training_ground.png"
image bg training_ground_real = "images/training_ground_real.png"
image bg match_stadium_night = "images/match_stadium_night.png"
image bg coach_office = "images/coach_office.png"
image bg transfer_meeting_room = "images/transfer_meeting_room.png"
image bg career_outcome_celebration = "images/career_outcome_celebration.png"
image maya_chen = "images/maya_chen.png"
image bg training_ground_empty_dawn = "images/training_ground_empty_dawn.png"
image main_player = "images/main_player.png"
image bg academy_gate_behind = "images/academy_gate_night.png"
image bg academy_gate_front = "images/academy_gate_front.png"
image bg hometown_street = "images/hometown_street.png"
image main_player_hometown = "images/main_player_hometown.png"
image main_player_behind = "images/main_player_behind.png"
image bg academy_pitchside_night = "images/academy_pitchside_night.png"
image top_bar = Solid("#000")
image bottom_bar = Solid("#000")
image bg training_drills = "images/training_drills.png"
image bg dressing_room = "images/dressing_room.png"
image bg players_staring = "images/players_staring.png"
image afiq = "images/afiq.png"
image main_player_front = "images/main_player_front.png"
image coach_rahman = "images/coach_rahman.png"
image main_talking = "images/main_talking.png"
image afiq_smirk = "images/afiq_smirk.png"
image afiq_bib = "images/afiq_bib.png"
image main_normal_face = "images/main_normal_face.png"
image main_control = "images/main_control.png"

show top_bar:
    xpos 0
    ypos -100
    xsize 1280
    ysize 100
    linear 0.5 ypos 0

show bottom_bar:
    xpos 0
    ypos 720
    xsize 1280
    ysize 100
    linear 0.5 ypos 620

transform scale_up:
    zoom 0.6

transform scale_down:
    zoom 0.6

transform scout_right:
    xalign 0.84
    yalign 1.0
    zoom 0.72

transform slide_in_left:
    xpos -500 ypos 0.8        # Start off-screen to the left
    easein_cubic 0.6 xpos 0.1 # Slide in over 0.6s with ease-out cubic curve

transform slide_in_right:
    xpos 1500 ypos 0.8        # Start off-screen to the right
    easein_cubic 0.6 xpos 0.9 # Slide in from the right

transform slide_left:
    xoffset -500
    alpha 0.0
    ease 0.5 xoffset 0 alpha 1.0

default player_name = "Player"
default position = ""
default archetype = ""
default skill = 0
default coach_opinion = 0
default confidence = 0
default reputation = 0
default loyalty = 0
default teamwork = 0
default pressure = 0
default difficulty = 0
default fan_mood = 0
default first_match_result = ""
default advanced_match_result = ""
default training_focus = ""
default career_status = ""
default career_path = ""
default first_start = False
default evaluation_notes = []

init python:
    def clamp_stat(value):
        return max(-3, min(10, value))

    def stat_line(name, value):
        marker = "++" if value >= 6 else "+" if value >= 3 else "!" if value < 0 else "-"
        return "%s %s: %s" % (marker, name, value)

    def add_note(text):
        if text not in evaluation_notes:
            evaluation_notes.append(text)

screen project_main_menu():
    tag menu

    add "images/opening_stadium.png"
    add Solid("#03070899")

    frame:
        background Solid("#07100fcc")
        xalign 0.5
        yalign 0.48
        xsize 920
        padding (56, 46)

        vbox:
            spacing 18
            xalign 0.5

            text "RISE TO GLORY" size 68 bold True xalign 0.5 color "#f7f4df"
            text "A football decision simulation about discipline, pressure, loyalty, and professional ambition." size 24 xalign 0.5 color "#d4efe0"

            null height 12

            hbox:
                spacing 18
                xalign 0.5
                textbutton "Start Career" action Return("start") xsize 260
                textbutton "Design Brief" action Return("instructions") xsize 260
                textbutton "Exit" action Quit(confirm=False) xsize 180

            null height 12

            text "Prototype focus: interaction flow, feedback, emotional engagement, error recovery, and usability evaluation." size 20 xalign 0.5 color "#adc7bd"

screen project_instructions():
    tag menu

    add "images/office.png"
    add Solid("#020509aa")

    frame:
        background Solid("#08111add")
        xalign 0.5
        yalign 0.5
        xsize 1060
        padding (50, 42)

        vbox:
            spacing 20

            text "Interaction Design Brief" size 48 bold True color "#f8f4df"
            text "You guide a young footballer through training, match pressure, transfer offers, teamwork, public reputation, and career consequences." color "#e5f4ee"
            text "The prototype shows user input through choices, system output through dialogue and score feedback, interface feedback through the live performance dashboard, and recoverability through replay and clear consequence summaries." color "#e5f4ee"

            hbox:
                spacing 18
                xalign 0.5
                frame:
                    background Solid("#123028cc")
                    xsize 300
                    padding (20, 16)
                    vbox:
                        spacing 8
                        text "Cognitive Support" size 25 bold True
                        text "Short choices, visible stats, immediate feedback, and final explanation reduce memory load." size 20
                frame:
                    background Solid("#2b2236cc")
                    xsize 300
                    padding (20, 16)
                    vbox:
                        spacing 8
                        text "Social Design" size 25 bold True
                        text "Coach, teammate, scout, fans, and club loyalty create social consequences." size 20
                frame:
                    background Solid("#332515cc")
                    xsize 300
                    padding (20, 16)
                    vbox:
                        spacing 8
                        text "Evaluation" size 25 bold True
                        text "The ending report lists what users can test: clarity, feedback, decision confidence, and replay value." size 20

            textbutton "Back" action Return() xalign 0.5 xsize 220

screen chapter_card(title, subtitle):
    modal True
    zorder 90

    add Solid("#00000099")
    frame:
        background Solid("#08110fe6")
        xalign 0.5
        yalign 0.5
        xsize 860
        padding (44, 38)

        vbox:
            spacing 18
            xalign 0.5
            text title size 50 bold True xalign 0.5 color "#f5efc8"
            text subtitle size 26 xalign 0.5 color "#cceadd"
            textbutton "Continue" action Return() xalign 0.5 xsize 220

    frame:
        background Solid("#00000000")
        xalign 0.0
        yalign 0.0
        xsize 540
        ysize 90
        padding (28, 16)

        vbox:
            spacing 4
            text "— CHAPTER —" size 16 color "#7db89a" xalign 0.0
            text chapter_title size 34 bold True color "#f5efc8" xalign 0.0

screen career_hud():
    zorder 70

    frame:
        background Solid("#06100dcc")
        xpos 24
        ypos 22
        xsize 430
        padding (18, 14)

        vbox:
            spacing 5
            text "[player_name]  |  [position]" size 21 bold True color "#f9f1d0"
            text "[stat_line('Skill', skill)]   [stat_line('Confidence', confidence)]" size 17
            text "[stat_line('Coach', coach_opinion)]   [stat_line('Reputation', reputation)]" size 17
            text "[stat_line('Teamwork', teamwork)]   [stat_line('Pressure', pressure)]" size 17

screen project_end_screen(final_title, final_message, final_score):
    add "images/career_outcome_celebration.png"
    add Solid("#020304aa")

    frame:
        background Solid("#08110ee6")
        xalign 0.5
        yalign 0.5
        xsize 1040
        padding (48, 42)

        vbox:
            spacing 18

            text final_title size 46 bold True xalign 0.5 color "#fff1a8"
            text final_message color "#edf8ef"
            text "Final performance score: [final_score]" size 26 xalign 0.5 color "#9ef0bd"

            frame:
                background Solid("#10231dcc")
                xfill True
                padding (22, 18)
                vbox:
                    spacing 6
                    text "Usability and Evaluation Evidence" size 28 bold True
                    for note in evaluation_notes:
                        text "- [note]" size 20

            hbox:
                xalign 0.5
                spacing 24
                textbutton "Replay and Improve" action Return("replay") xsize 260
                textbutton "Exit" action Quit(confirm=False) xsize 160

label start:
    call screen project_main_menu

    if _return == "instructions":
        call screen project_instructions
        jump start

    jump reset_story

label reset_story:
    scene bg training_ground_empty_dawn        
    with fade
    show main_player at slide_left
    $ player_name = renpy.input("Enter your player's name:", length=20).strip()
    if player_name == "":
        $ player_name = "Player"

    $ position = ""
    $ archetype = ""
    $ skill = 0
    $ coach_opinion = 0
    $ confidence = 0
    $ reputation = 0
    $ loyalty = 0
    $ teamwork = 0
    $ pressure = 0
    $ difficulty = 0
    $ fan_mood = 0
    $ first_match_result = ""
    $ advanced_match_result = ""
    $ training_focus = ""
    $ career_status = ""
    $ career_path = ""
    $ first_start = False
    $ evaluation_notes = []

    show screen career_hud
    jump introduction

label introduction:
    scene bg hometown_street
    show main_player_hometown at center, scale_up
    with fade
    show main_player_hometown at center, scale_up


    narrator "{cps=60}You are [player_name], a young footballer who grew up chasing a torn ball across narrow streets, empty car parks, and one stubborn little field behind the school.{/cps}"
    narrator "{cps=60}Your boots are not new. Your family still checks the price of every away trip. But when the ball comes to you, the noise of ordinary life disappears.{/cps}"
    jump academy_gate
    
transform talking_right:
    xalign 1.3

label academy_gate:
    scene bg academy_gate_behind
    with fade
    show main_player_behind at center, scale_up
    narrator "{cps=60}Tonight, you walk through the academy gate for the first time.{/cps}"
    scene bg academy_gate_front
    with dissolve
    show main_player_front at center, scale_up with dissolve
    narrator "{cps=60}Beyond it are floodlights, scouts, contracts, rival players, dressing-room politics, and the quiet fear that maybe the dream is bigger than you.{/cps}"
    scene bg training_ground
    with dissolve
    show afiq at left, scale_down with dissolve
    show main_talking at center, scale_up, talking_right with dissolve
    captain "You are the new one, right? Do not look so shocked. Everyone gets nervous the first day."
    player "I thought getting here would feel like the finish line."
    show coach_rahman at right, scale_down with dissolve
    coach "It is not the finish line, [player_name]. It is the first whistle."
    coach "Talent brought you to this field. Discipline decides whether you stay. Courage decides whether anyone remembers you."

    $ add_note("Target users receive a simple goal immediately: guide a player toward a professional career.")

    hide coach_rahman with dissolve
    narrator "{cps=60}Coach Rahman walks away, his whistle gleaming under the floodlights. The moment he is out of earshot, the quiet evening air shatters.{/cps}"

    hide afiq with dissolve
    show afiq_smirk at left, scale_down with dissolve
    captain "Don't let the old man's speeches get to your head, 'prodigy'."

    hide afiq_smirk with dissolve
    show afiq_bib at left, scale_down with dissolve
    narrator "Afiq tosses a mud-stained training bib right at your chest. It lands with a heavy, wet thud."

    hide afiq_bib with dissolve
    show afiq_smirk at left, scale_down with dissolve
    captain "Look around you. Half the guys here were captain of their state teams. The other half have fathers who played in the top tier."
    captain "Then you walk in with boots that look like they survived a war, and suddenly the scouts are whispering?"

    player "I earned my trial here just like everyone else, Afiq."

    captain "Trial? This isn't a playground. There are only two open spots left on the registration list for the upcoming cup tournament."
    captain "If you rise, someone else falls. I've spent three years bleeding for this academy. I'm not letting some street-baller take my spot in the showcase."

    narrator "The surrounding academy players stop their drills, turning their heads to watch the confrontation. The pressure in your chest tightens like a vice."

    scene bg players_staring
    with dissolve

    show afiq_smirk at left, scale_down with dissolve
    show main_normal_face at right, scale_up with dissolve
    menu:
        "How do you handle Afiq's open hostility?"

        "Keep your cool and let your football do the talking":
            $ teamwork += 1
            $ coach_opinion += 1
            $ pressure += 1
            player "Then don't worry about me, Afiq. Worry about keeping up with me on the pitch."
            captain "Arrogant, aren't we? Let's see if that mouth can save you when the tackles start flying."
            hide main_normal_face with dissolve
            show main_control at right, scale_up with dissolve
            narrator "{cps=60}You swallow your anger and look past him toward the grass. You've faced tougher critics on concrete streets.{/cps}"

        "Fire back and draw a line in the sand":
            $ confidence += 2
            $ pressure += 2
            $ teamwork -= 1
            player "If your three years of hard work can be threatened by 'some street-baller' in one day, maybe you aren't as good as you think you are."
            narrator "{cps=60}A collective 'oh' ripples through the watching players. Afiq steps up, chest to chest, his eyes burning.{/cps}"
            captain "You're going to regret saying that. When we get into the match drills, I'm personally making sure you don't finish the session."

        "Defuse the situation and show humility":
            $ teamwork += 2
            $ confidence -= 1
            player "I'm not here to take anyone's place, man. I'm just trying to help my family. We can both make the squad if we play together."
            narrator "{cps=60}Afiq blinks, momentarily caught off guard by your lack of malice, before scowling and stepping back.{/cps}"
            captain "This is professional football, not a charity. There is no 'together' when a contract is on the line."

    narrator "{cps=60}Before the tension can boil over into a physical fight, a sharp blast of a whistle echoes across the training ground.{/cps}"

    show coach_rahman at right, scale_down with dissolve
    coach "Afiq! [player_name]! If you two have that much energy to waste, you can run laps until midnight!"

    narrator "{cps=60}The crowd scatter instantly, retrieving their footballs as Coach Rahman approaches with a clipboard, his eyes narrowing at the group.{/cps}"

    jump choose_position

label choose_position:
    scene bg training_drills
    with dissolve

    coach "Before I judge your level, I need to know your football mind. Where do you see the game from?"

    menu:
        "Choose your main position."

        "Attacker - goals, risk, and instinct":
            $ position = "Attacker"
            $ archetype = "Finisher"
            $ skill += 2
            $ confidence += 1
            $ pressure += 1
            narrator "You choose Attacker. The team will forgive quiet minutes if you can decide loud ones."

        "Midfielder - tempo, vision, and control":
            $ position = "Midfielder"
            $ archetype = "Playmaker"
            $ coach_opinion += 1
            $ teamwork += 2
            narrator "You choose Midfielder. Your job is to read the game and make others better."

        "Defender - courage, timing, and leadership":
            $ position = "Defender"
            $ archetype = "Guardian"
            $ skill += 1
            $ coach_opinion += 2
            $ teamwork += 1
            narrator "You choose Defender. You will not always be praised for danger you prevent, but the team will feel it."

        "Goalkeeper - reflexes, command, and nerve":
            $ position = "Goalkeeper"
            $ archetype = "Last Wall"
            $ skill += 1
            $ confidence += 1
            $ coach_opinion += 1
            $ pressure += 1
            narrator "You choose Goalkeeper. One mistake can become a headline, but one save can become a legend."

    $ renpy.notify("Role selected: " + position + " / " + archetype)
    $ add_note("Position selection changes the scoring model, giving users visible system response.")

    jump training_decision

label training_decision:
    scene bg training_drills
    with dissolve

    narrator "{cps=60}The first elite training session is faster than expected. Players sprint, collide, recover, shout, reset, and sprint again.{/cps}"
    coach "Today is not about looking talented. Today is about proving you can repeat good decisions when your lungs are burning."

    narrator "{cps=60}The squad splits into a heavy possession grid. You find your rhythm, tracking the ball cleanly, until a shadow cuts across your path.{/cps}"
    narrator "{cps=60}It's Afiq. He isn't looking at the ball; his eyes are locked entirely on your ankles.{/cps}"
    narrator "{cps=60}Before you can pivot, he lunges in with a fierce, borderline illegal sliding tackle that sends you crashing violently into the turf.{/cps}"

    show captain at center with dissolve
    captain "Welcome to the academy, street-boy. Get up. The game doesn't stop because you're on the floor."

    menu:
        "How do you react to Afiq's dangerous tackle?"

        "Spring up instantly and shove him back":
            $ pressure += 2
            $ coach_opinion -= 1
            $ teamwork -= 1
            player "Are you trying to break my leg before the season even starts?!"
            narrator "{cps=60}You shove Afiq square in the chest. He smiles maliciously, stepping into your space as the squad rushes to separate you.{/cps}"
            coach "[player_name]! Afiq! Keep your hands to yourselves or both of you can pack your bags right now!"
            narrator "{cps=60}The coach writes something sharp on his clipboard. Your temper just cost you points with the staff.{/cps}"

        "Dust yourself off silently and offer a mocking smirk":
            $ confidence += 2
            $ skill += 1
            $ pressure += 1
            narrator "{cps=60}You take your time getting up, slowly brushing the wet grass off your knees. You look him up and down, then flash a calm smirk.{/cps}"
            player "Nice tackle. My little brother hits harder than that, though."
            narrator "{cps=60}A few teammates choke back a laugh. Afiq's face reddens, your complete composure clearly driving him crazy.{/cps}"
            captain "Let's see if you're still laughing by the end of the drill."

        "Accept the challenge calmly and look him in the eyes":
            $ teamwork += 1
            $ coach_opinion += 1
            player "Fair challenge. But you'll have to be faster than that next time."
            narrator "{cps=60}You pull yourself up and offer a brief, professional nod. Coach Rahman watches from a distance, nodding slightly at your maturity.{/cps}"
            coach "Good tracking, Afiq. Clean recovery, [player_name]. Keep the ball moving!"

    narrator "{cps=60}The whistle blows again, forcing everyone back into their tactical roles. The air is thick with sweat, rain, and spite.{/cps}"

    if position == "Attacker":
        narrator "{cps=60}Your drill is ruthless: curved runs behind the line, first-time finishing, weak-foot shots, and pressing triggers when the defender receives with a bad touch.{/cps}"
    elif position == "Midfielder":
        narrator "{cps=60}Your drill is a storm of rondos, half-turn receiving, scanning before the pass, switch-of-play timing, and resisting the urge to force every ball forward.{/cps}"
    elif position == "Defender":
        narrator "{cps=60}Your drill is built on duels: body shape, recovery runs, last-second blocks, defensive headers, and choosing when to step out or hold the line.{/cps}"
    else:
        narrator "{cps=60}Your drill is lonely and loud: reaction saves, crosses through traffic, one-on-ones, distribution under pressure, and commanding defenders who barely know you.{/cps}"

    menu:
        "How do you handle your position drill?"

        "Stay after training for extra position work":
            $ training_focus = "extra"
            $ skill += 3
            $ coach_opinion += 2
            $ confidence += 1
            $ pressure += 1
            coach "That hunger is useful. Just understand what comes with it: once people see it, they expect it every day."
            if position == "Attacker":
                narrator "{cps=60}You repeat finishes until the movement feels automatic: near post, far post, chip, driven shot, cutback.{/cps}"
            elif position == "Midfielder":
                narrator "{cps=60}You ask for extra rondo rounds and learn to receive with your body open before pressure arrives.{/cps}"
            elif position == "Defender":
                narrator "{cps=60}You practice recovery tackles until your timing stops being desperate and starts being clean.{/cps}"
            else:
                narrator "{cps=60}You face shot after shot until diving no longer feels dramatic, only necessary.{/cps}"

        "Train smart and ask for detailed feedback":
            $ training_focus = "smart"
            $ skill += 2
            $ coach_opinion += 2
            $ teamwork += 1
            coach "That is professional behavior. You improve faster when you understand why."
            analyst "Your clips are not perfect, but you are asking the right questions. That matters."
            narrator "{cps=60}You learn the system instead of just surviving the drill.{/cps}"

        "Do the minimum and save energy for match day":
            $ training_focus = "minimum"
            $ skill += 1
            $ confidence += 1
            $ coach_opinion -= 1
            coach "Careful. Rest is useful, but the staff must believe you are committed."
            narrator "{cps=60}You feel fresh, but the coach writes something short on his clipboard. Short notes are rarely comforting.{/cps}"

        "Skip training and hope nobody notices":
            $ training_focus = "skip"
            $ skill -= 1
            $ coach_opinion -= 3
            $ confidence -= 1
            $ reputation -= 1
            coach "[player_name], football is a team activity. When you disappear, everyone else pays for it."
            narrator "{cps=60}The system makes the error recoverable, but the consequence is clear.{/cps}"

    $ skill = clamp_stat(skill)
    $ coach_opinion = clamp_stat(coach_opinion)
    $ confidence = clamp_stat(confidence)
    $ reputation = clamp_stat(reputation)
    $ add_note("Training choices demonstrate error prevention and recovery through immediate feedback.")

    if skill + coach_opinion + teamwork >= 4:
        $ first_start = True
    else:
        $ first_start = False

    jump first_match

label first_match:
    scene bg dressing_room
    with dissolve

    if not first_start:
        jump bench_arc

    narrator "{cps=60}The team sheet goes up on the wall. Your name is in the starting lineup.{/cps}"
    captain "First start. Do not play the occasion. Play the ball."

    show captain at center with dissolve
    narrator "{cps=60}Afiq stands in front of the board, staring at your name in the Starting XI. His knuckles are white as he grips his kit bag.{/cps}"
    captain "Starting? You've been here five minutes and he's handing you the shirt?"
                
    menu:
        "How do you handle your bitter rival before kickoff?"

        "Remind him of his own advice":
            $ confidence += 2
            $ pressure += 1
            player "Like you said, Afiq... don't play the occasion. Play the ball. Watch me play it tonight."
            captain "Arrogant bastard. If you drop points for us out there, I'll make sure the gaffer never forgets it."
            narrator "{cps=60}He brushes past you, slamming the dressing room door shut.{/cps}"

        "Offer a professional truce for the team's sake":
            $ teamwork += 2
            $ coach_opinion += 1
            player "The coach made the call, not me. But we need a win tonight. Let's put this aside until full-time."
            narrator "{cps=60}Afiq looks at your extended hand, scowls, and ignores it—but his posture loosens slightly.{/cps}"
            captain "Don't mistake my silence for friendship, street-boy. Just don't ruin my stats out there."
                
    hide captain with dissolve
    narrator "{cps=60}By the 83rd minute, the match is tied. Rain shines under the floodlights. Every pass sounds louder than it should.{/cps}"

    if position == "Attacker":
        narrator "{cps=60}A long diagonal drops behind the full-back. You bring it down inside the box. The goalkeeper steps forward, and Afiq screams for the square pass.{/cps}"
        jump first_match_attacker
    elif position == "Midfielder":
        narrator "{cps=60}You receive between the lines with one touch to turn. Afiq is sprinting behind the centre-backs, but the opponent's midfield is tired and the game is ready to be controlled.{/cps}"
        jump first_match_midfielder
    elif position == "Defender":
        narrator "{cps=60}The opponent breaks down your side. Their winger cuts inside, their striker darts across your shoulder, and one wrong step opens the goal.{/cps}"
        jump first_match_defender
    else:
        narrator "{cps=60}A loose back pass slows in the wet grass. Their striker reaches it first. Suddenly it is just you, the attacker, and the sound of the crowd rising.{/cps}"
        jump first_match_goalkeeper

label bench_arc:
    narrator "{cps=60}The team sheet goes up on the wall. Your eyes search once, twice, then stop.{/cps}"
    narrator "{cps=60}Your name is not in the starting eleven.{/cps}"

    show captain at center with dissolve
    narrator "{cps=60}Afiq walks up beside you, snapping a captain's band onto his arm or adjusting his shiny starting jersey. He smirks.{/cps}"
    captain "What's wrong, prodigy? Looks like the gaffer realized street tricks don't win league matches."
    captain "Enjoy the view from the bench. Make sure you keep my water bottle warm."

    menu:
        "How do you swallow your pride on the bench?"
                        
        "Channel the anger into focus":
            $ pressure += 2
            $ skill += 1
            player "Laugh now, Afiq. But when I get my minutes, you better hope you aren't the one slowing the game down."
            captain "I'll be on the pitch making history while you're counting the crowd. See ya."
            narrator "{cps=60}Your blood boils, but you channel that heat into absolute focus. You will be ready.{/cps}"

        "Stay ice-cold and observant":
            $ confidence += 1
            $ coach_opinion += 1
            narrator "{cps=60}You look him dead in the eye, saying absolutely nothing. The lack of a reaction makes his smirk falter.{/cps}"
            player "Good luck out there. You'll need it."
            narrator "{cps=60}You turn away to find your training jacket. You will use this time to study the opponent's weaknesses.{/cps}"

    hide captain with dissolve

    coach "You are on the bench today. This is not punishment. This is information."
    player "I can help the team."
    coach "Then prove it from minute one of training tomorrow. A career is not built only on match nights."
    narrator "{cps=60}For eighty minutes, you sit in a jacket, watching players in your position make the runs, tackles, passes, or saves you imagined for yourself.{/cps}"
    narrator "{cps=60}The match ends in a draw. Nobody blames you. Somehow, that hurts more.{/cps}"
    captain "Do not disappear because of one bench. Make the coach feel uncomfortable leaving you out."

    menu:
        "How do you begin the hard-work arc?"

        "Arrive early for two weeks and rebuild trust":
            $ skill += 3
            $ coach_opinion += 3
            $ confidence += 1
            $ teamwork += 1
            $ first_match_result = "bench comeback"
            narrator "{cps=60}You become the first player on the training pitch and the last one out. The staff stop talking about your absence and start talking about your response.{/cps}"
            coach "This is what I wanted to see. The bench can break a player, or it can sharpen one."

        "Ask senior players to mentor you":
            $ skill += 2
            $ coach_opinion += 2
            $ teamwork += 2
            $ first_match_result = "bench learner"
            narrator "{cps=60}You learn tiny professional habits: how to recover, when to speak, how to read a defender's hips, how to stay ready without sulking.{/cps}"
            captain "You listened. That is why you are still moving forward."

        "Complain and wait for another chance":
            $ confidence += 1
            $ coach_opinion -= 2
            $ reputation -= 1
            $ pressure += 2
            $ first_match_result = "bench frustration"
            narrator "{cps=60}Your frustration is understandable, but it leaks into your body language. Staff notice everything at this level.{/cps}"
            coach "Wanting minutes is normal. Acting entitled to them is dangerous."

    $ skill = clamp_stat(skill)
    $ coach_opinion = clamp_stat(coach_opinion)
    $ confidence = clamp_stat(confidence)
    $ reputation = clamp_stat(reputation)
    $ teamwork = clamp_stat(teamwork)
    $ pressure = clamp_stat(pressure)
    $ add_note("The bench path prevents early endings and turns poor training into a recovery arc.")

    jump coach_feedback

label first_match_attacker:
    narrator "{cps=60}The match reaches a boiling point. The stadium lights cut through the heavy rain.{/cps}"
    narrator "{cps=60}A long diagonal pass drops cleanly behind the opponent's full-back . You bring it down inside the penalty box with a sharp first touch .{/cps}"
    narrator "{cps=60}The goalkeeper rushes forward, trying to narrow your angle . Out of the corner of your eye, you see Afiq sprinting into space.{/cps}"
    captain "[player_name]! Square it! Square the damn ball!" 

    menu:
        "Attacker: Do you swallow your pride and pass, or back your own street instinct?" 

        "Pass across goal to Afiq":
            if skill + teamwork >= 4: 
                $ first_match_result = "assist" 
                $ reputation += 2 
                $ coach_opinion += 2 
                $ confidence += 1 
                $ teamwork += 1 
                narrator "{cps=60}You wait half a heartbeat, pulling the goalkeeper completely out of position, and slide the ball across the six-yard box .{/cps}"
                narrator "{cps=60}Afiq slides in, tapping it into an open net. The stadium erupts into cheers .{/cps}"
                show captain at center with dissolve
                captain "That was... perfect. You saw the move before everyone else." 
                player "We win together, Afiq. Remember?"
                narrator "{cps=60}Afiq stares at you, a mix of shock and reluctant respect crossing his face, before turning to celebrate with the fans.{/cps}"
            else:
                $ first_match_result = "blocked pass" 
                $ coach_opinion -= 1 
                $ pressure += 1 
                narrator "{cps=60}The idea is generous, but your execution is sloppy under pressure. The pass is badly underhit .{/cps}"
                narrator "{cps=60}An opposing defender slides in, cutting out the ball, and the scoring chance dies instantly .{/cps}"
                
                show captain at center with dissolve
                captain "Are you kidding me?! If you can't make a simple five-yard pass, don't play at this level!"
                narrator "{cps=60}Afiq throws his arms up in sheer fury, completely disgusted by your mistake.{/cps}"

        "Shoot before the goalkeeper sets":
            if skill + confidence >= 5: 
                $ first_match_result = "goal" 
                $ reputation += 3 
                $ coach_opinion += 2 
                $ confidence += 2 
                $ fan_mood += 2 
                narrator "{cps=60}You block out his shouting. You strike the ball early, catching the goalkeeper completely off guard .{/cps}"
                narrator "{cps=60}The ball flashes across the wet grass and kisses the inside of the far post. Goal! {/cps}"
                coach "That is the kind of courage scouts remember." 
                
                show captain at center with dissolve
                narrator "{cps=60}Afiq jogs over, his mouth slightly open in disbelief. He wanted the spotlight, but your skill silenced him.{/cps}"
                player "Told you my mouth wasn't the only thing that could save me."
                captain "Hmph. Lucky strike. Do it again next week, then we'll talk."
            else:
                $ first_match_result = "miss" 
                $ coach_opinion -= 1 
                $ pressure += 1 
                $ teamwork -= 1
                narrator "{cps=60}You shoot with your heart more than your technique, trying desperately to prove a point to Afiq .{/cps}"
                narrator "{cps=60}The shot rises wildly over the crossbar, flying into the stands alongside your pride .{/cps}"
                
                show captain at center with dissolve
                captain "Selfish! Absolute street-ball garbage! You choked because your ego is bigger than the team!"
                narrator "{cps=60}Afiq aggressively gets into your face, screaming over the sound of the rain as you look down at the grass.{/cps}"

    hide captain with dissolve

    jump first_match_wrap

label first_match_midfielder:
    narrator "{cps=60}You receive the ball between the lines, opening your body with your first touch.{/cps}"
    narrator "{cps=60}Out of the corner of your eye, you see Afiq tearing past the center-backs into open space, screaming for the ball.{/cps}"
    narrator "{cps=60}But the opponent's midfield looks exhausted, and a safe pass would let you dictate the closing minutes.{/cps}"

    menu:
        "Midfielder: Risk the high-stakes killer pass to your rival, or control the game?"

        "Thread the through ball to Afiq":
            if skill + teamwork >= 4:
                $ first_match_result = "through ball assist"
                $ reputation += 2
                $ coach_opinion += 2
                $ teamwork += 2
                narrator "{cps=60}You disguise your hips, waiting until the absolute last millisecond before sliding a precision pass through a microscopic gap.{/cps}"
                narrator "{cps=60}Afiq chases it down and smashes it home!{/cps}"
                
                show captain at center with dissolve
                captain "I only had to run... You put that on a silver platter for me."
                player "Just make sure you finish the next one too."
                narrator "{cps=60}Afiq gives you a sharp, respectful nod. The tension between you transforms into tactical chemistry.{/cps}"

            else:
                $ first_match_result = "forced pass"
                $ reputation -= 1
                $ pressure += 1
                narrator "{cps=60}You force the ball, but your execution is half a second too late. The center-back reads your eyes and cuts it out.{/cps}"

                show captain at center with dissolve
                captain "Are you blind?! If you're going to try and be a playmaker, learn how to weigh a pass!"
                narrator "{cps=60}Afiq turns back to yell at you, pointing aggressively at the grass where the ball should have landed.{/cps}"

        "Control the game and move the tired defense":
            if coach_opinion + teamwork >= 4:
                $ first_match_result = "tempo control"
                $ coach_opinion += 2
                $ teamwork += 2
                $ confidence += 1
                narrator "{cps=60}You ignore Afiq's frantic shouting. You turn back, recycle possession, and shift the opponent's block from side to side until the whistle blows.{/cps}"
                coach "That is midfield maturity. You made the match breathe at your speed."
                
                show captain at center with dissolve
                captain "You should have risked it. I was wide open."
                player "We controlled the game and kept the points, Afiq. That's what a midfielder does."
                narrator "{cps=60}He scowls and turns away, frustrated that you chose strategic safety over giving him his glory moment.{/cps}"
            else:
                $ first_match_result = "too slow"
                $ confidence -= 1
                narrator "{cps=60}You try to slow the match down, but you panic on the ball. Your touches become safe and stagnant, letting the pressure build.{/cps}"
                
                show captain at center with dissolve
                captain "Unbelievable! You completely choked our momentum because you're too scared to pass forward!"

    hide captain with dissolve

    jump first_match_wrap

label first_match_defender:
    narrator "{cps=60}The opponent launches a dangerous counter-attack down your wing.{/cps}"
    narrator "{cps=60}Their winger cuts inside sharply, their striker darts across your blind side, and one wrong step will compromise the entire goal.{/cps}"
    narrator "{cps=60}Afiq has dropped deep to help, but he is completely out of position, leaving a massive gap behind him.{/cps}"

    menu:
        "Defender: Step out aggressively to make the tackle, or drop and yell instructions?"

        "Step out and make the tackle before the striker turns":
            if skill + confidence + coach_opinion >= 5:
                $ first_match_result = "last tackle"
                $ reputation += 2
                $ coach_opinion += 2
                $ confidence += 1
                narrator "{cps=60}You read the heavy touch perfectly, stepping in like iron to claim the ball cleanly before the striker can unleash a shot.{/cps}"
                coach "That tackle was brave because it was timed, not because it was wild."
                
                show captain at center with dissolve
                captain "Whew... Good recovery, street-boy. I thought they had us beaten there."
                player "Keep your man tracked next time, Afiq. I won't bail you out twice."
                narrator "{cps=60}Afiq looks slightly embarrassed that you had to cover his defensive error, muttering an excuse as he jogs back upfield.{/cps}"
            else:
                $ first_match_result = "mistimed tackle"
                $ reputation -= 1
                $ coach_opinion -= 1
                $ pressure += 2
                narrator "{cps=60}You lunge a fraction of a second too early. The striker easily drops his shoulder, skips right past you, and unleashes a dangerous shot.{/cps}"
                
                show captain at center with dissolve
                captain "What are you diving in for?! Stay on your feet! You just left the entire backline exposed!"
                narrator "{cps=60}Afiq throws his hands up, instantly shifting the blame entirely onto your mistake.{/cps}"

        "Drop, block the passing lane, and force a wide shot":
            if teamwork + coach_opinion >= 4:
                $ first_match_result = "defensive stand"
                $ coach_opinion += 2
                $ teamwork += 2
                narrator "{cps=60}You hold your line tightly, pointing and shouting aggressively at Afiq to drop back and plug the inner passing lane.{/cps}"
                narrator "{cps=60}He actually listens to your command. The winger gets frustrated by the lack of space and fires a wild shot wide.{/cps}"
                
                show captain at center with dissolve
                captain "Good communication. You kept us organized out there; I heard you the whole way."
                player "That's how we survive the clean sheet."
            else:
                $ first_match_result = "invited pressure"
                $ pressure += 1
                $ confidence -= 1
                narrator "{cps=60}You drop too deep into your own box, causing panic. You try shouting at Afiq, but your voice wavers and nobody coordinates.{/cps}"
                
                show captain at center with dissolve
                captain "Stop yelling and start defending! Your positioning is a total mess!"

    hide captain with dissolve

    jump first_match_wrap

label first_match_goalkeeper:
    narrator "{cps=60}A loose, lazy back-pass from Afiq stalls heavily in the wet, muddy grass.{/cps}"
    narrator "{cps=60}Their striker reads it instantly, charging forward to reach it first.{/cps}"
    narrator "{cps=60}Suddenly, it is just you, the oncoming attacker, and a catastrophic mistake caused by your rival.{/cps}"

    menu:
        "Goalkeeper: Explode forward to charge down the one-on-one, or hold your ground?"

        "Rush out, spread your body, and close the angle":
            if skill + confidence >= 4:
                $ first_match_result = "one on one save"
                $ reputation += 3
                $ coach_opinion += 2
                $ confidence += 2
                $ fan_mood += 1
                narrator "{cps=60}You explode off your line, making your body massive, and block the striker's blasted shot cleanly with your trailing leg.{/cps}"
                coach "That is goalkeeping. Decision first, reflex second."
                
                show captain at center with dissolve
                narrator "{cps=60}Afiq runs back into the box, his face pale with relief after his terrible pass nearly cost a goal.{/cps}"
                captain "Man... you completely saved me there. Massive stop. I owe you one."
                player "Watch the weight on your passes, Afiq. My heart can't take many more of those."
                narrator "{cps=60}He gives you a grateful tap on the shoulder—the bitter rivalry melting away under mutual survival.{/cps}"
            else:
                $ first_match_result = "rounded keeper"
                $ reputation -= 1
                $ pressure += 2
                narrator "{cps=60}You rush out with too much panic. The striker easily touches the ball around your diving frame.{/cps}"
                narrator "{cps=60}Thankfully, your center-back sprints back and clears it off the goal line just in time.{/cps}"

                show captain at center with dissolve
                captain "Why did you come flying out like a madman?! You made it way too easy for him to round you!"
                narrator "{cps=60}Even though it was his terrible pass that caused the crisis, Afiq immediately barks at you to cover his own skin.{/cps}"

        "Hold your ground and read the striker's finish":
            if coach_opinion + skill >= 4:
                $ first_match_result = "composed save"
                $ reputation += 2
                $ coach_opinion += 2
                $ teamwork += 1
                narrator "{cps=60}You stand your ground, refusing to bite on the striker's feints. You drop low at the perfect micro-second to smother the shot.{/cps}"
                
                show captain at center with dissolve
                captain "You saved us. Simple as that. Great composure."
                player "Just focus up. We still have a match to win."
            else:
                $ first_match_result = "late reaction"
                $ confidence -= 1
                $ coach_opinion -= 1
                narrator "{cps=60}You hesitate, caught in two minds. The striker fires early, and the ball slips beneath your hand, crashing painfully into the net.{/cps}"
                
                show captain at center with dissolve
                captain "Unbelievable! We're losing because our keeper doesn't know when to come off his line!"

    hide captain with dissolve

    jump first_match_wrap

label post_match_debrief:
    scene bg office
    with dissolve
    
    narrator "{cps=60}The steam from the showers fills the damp dressing room. The rain outside has stopped, but the atmosphere inside is still charged.{/cps}"
    
    if first_match_result in ["assist", "through ball assist", "defensive stand", "one on one save"]:
        show captain at center with dissolve
        narrator "{cps=60}Afiq sits on the bench, unstrapping his shin guards. He looks up as you walk past your locker.{/cps}"
        captain "Hey. [player_name]."
        player "Yeah?"
        captain "Out there... on that play. You didn't play like a selfish street-baller. You played for the badge."
        captain "Don't think we're best friends now. The next trial match is going to be even harder. But... you belong on this grass."
        
        menu:
            "How do you cement this shifting dynamic?"
            
            "Acknowledge the partnership":
                $ teamwork += 2
                $ coach_opinion += 1
                player "We win matches together, Afiq. Let's make sure the scouts have nothing bad to say about either of us."
                narrator "{cps=60}Afiq nods quietly, a silent understanding forming between the two top talents in the academy.{/cps}"
                    
            "Keep the competitive edge sharp":
                $ confidence += 2
                player "Just make sure you keep making those runs. I’ll keep making you look good."
                captain "Heh. Don't flatter yourself. Just don't drop your level."
        
        hide captain with dissolve

    else:
        show captain at center with dissolve
        narrator "{cps=60}The moment Coach Rahman steps out to talk to the referee, Afiq slams his boot against the floor, glaring right at you.{/cps}"
        captain "You completely compromised us out there! Your ego is going to cost half this squad their registration spots!"
        
        menu:
            "The locker room goes dead silent. How do you respond?"
                
            "Stand your ground and confront him":
                $ confidence += 2
                $ pressure += 2
                $ teamwork -= 1
                player "Stop crying, Afiq! Football is about taking risks. If you can't handle the pressure of a real game, go back to the youth team."
                narrator "{cps=60}Afiq steps up, jaw clenched, before a senior player steps between you two, pushing you both back.{/cps}"
                captain "You won't last the month here. Mark my words."
                    
            "Take accountability but refuse to back down":
                $ coach_opinion += 1
                $ pressure += 1
                player "The execution was poor, and I take responsibility for the mistake. But I'm not going to sit here and let you blame the entire match on one play."
                captain "Then fix your game before you step back onto my pitch."
        
        hide captain with dissolve

    narrator "{cps=60}Before the internal fighting can escalate any further, the heavy wooden door swings open.{/cps}"
    

label scouting_evaluation:
    show maya_chen at right with dissolve
    show coach at left with dissolve
    
    narrator "{cps=60}Coach Rahman enters, followed closely by Maya Chen, the chief scout. Maya is looking directly at her tablet, analyzing the match data.{/cps}"
    
    if first_match_result in ["assist", "through ball assist", "defensive stand", "one on one save"]:
        scout "The chemistry in the second half was fascinating, Coach. [player_name] and Afiq showed real tactical synergy under pressure."
        coach "True. Talent wins training drills, but maturity wins league cups. They adapted."
    else:
        scout "The data shows a massive tactical disconnect in the final third. The friction between [player_name] and Afiq is actively damaging our shape."
        coach "They are playing two different games on the same pitch. If they don't iron out this pride, one of them will be watching the showcase from the stands."

    scout "[player_name], I'm finalizing my report for the senior team representatives."
    scout "Individual brilliance catches our eye, but internal toxicity ruins clubs. How do you plan to handle the internal competition here?"

    menu:
        "Answer Maya Chen's evaluation question:"
            
        "I'm here to build a team, not an empire. (Focus on Teamwork)":
            $ teamwork += 2
            $ coach_opinion += 2
            $ reputation += 1
            scout "A mature answer. The clubs I represent value players who elevate those around them."
            narrator "{cps=60}Coach Rahman nods approvingly, crossing his arms with a slight smile.{/cps}"

        "I'm here to be the best. Competition makes us both sharper. (Focus on Confidence)":
            $ confidence += 3
            $ pressure += 1
            $ reputation += 2
            scout "Spoken like a true forward-thinking asset. Just ensure your ambition doesn't become a liability."
            narrator "{cps=60}Coach Rahman narrows his eyes. He respects the drive, but the warning remains unsaid.{/cps}"

    hide maya_chen
    hide coach
    with dissolve
    
    jump next_chapter_setup

label first_match_wrap:
    $ skill = clamp_stat(skill)
    $ coach_opinion = clamp_stat(coach_opinion)
    $ confidence = clamp_stat(confidence)
    $ reputation = clamp_stat(reputation)
    $ teamwork = clamp_stat(teamwork)
    $ pressure = clamp_stat(pressure)
    $ add_note("Match interaction uses conditional outcomes, not only fixed dialogue.")

    jump coach_feedback

label coach_feedback:
    scene bg coach_office
    with dissolve
    
    coach "Sit down, [player_name]. Close the door behind you."
    narrator "Coach Rahman is sitting behind his heavy wooden desk. Next to him, the Performance Analyst is reviewing training and match telemetry data on a tablet."
    coach "The staff want to review exactly where your career is heading, because right now, your relationship with the squad—and specifically Afiq—is shifting the energy of this academy."

    if first_match_result in ["goal", "assist", "through ball assist", "tempo control", "last tackle", "defensive stand", "one on one save", "composed save", "bench comeback"]:
        $ career_status = "rise"
        $ reputation += 1
        
        coach "You are rising, [player_name]. Not because everything is perfect, but because your choices under pressure are starting to look professional."
        analyst "The telemetry tracking data says you affected the match directly in your position instead of playing like a generic player."
        
        if first_match_result == "bench comeback":
            coach "Afiq noticed it too. He told me your response to being benched showed the exact kind of hunger this academy needs."
        else:
            analyst "Your link-up play with Afiq showed real tactical maturity. You kept your head down, ignored the noise, and forced him to respect your ability."

    elif coach_opinion >= 1 or first_match_result in ["bench learner"]:
        $ career_status = "average"
        
        coach "You are not failing, but you are not separating yourself from the pack yet."
        coach "Right now you are just a part of the squad, not the reason the squad changes or wins games."
        analyst "The raw fitness and completion numbers are stable. The question is whether you can turn stable into special."
        coach "Afiq is an established player here. If you want to challenge his status, you need to provide a spark, not just pass the ball sideways."

    else:
        $ career_status = "fail"
        $ reputation -= 1
        $ pressure += 1
        
        coach "This is a serious setback. Your raw ability is not erased, but your reliability within our structure is now a major question."
        analyst "The data shows a massive tactical disconnect. You and Afiq are operating on entirely separate wavelengths out there, and it's choking our transition play."
        coach "You will get another chance here, but the next chapter has to show quiet work before it shows loud ambition."

    menu:
        "Coach Rahman waits for your response. How do you handle the criticism?"
    
        "Accept it professionally and ask for a specific performance plan":
            $ coach_opinion += 2
            $ teamwork += 1
            $ confidence += 1
            coach "Good. Specific feedback creates specific progress. That is how a professional athlete speaks."
            analyst "I'll upload your positional drill clips and tracking charts directly to your phone. Let's iron out the flaws."
            
        "Defend your decisions emotionally and claim your style is misunderstood":
            $ confidence += 1
            $ coach_opinion -= 1
            $ pressure += 1
            coach "I like confidence, kid. I do not like excuses. If your style was truly working, the scoreboard and the analyst's screen would be doing the talking for you."
            
        "Stay quiet, absorb the instructions, and reflect":
            $ coach_opinion += 1
            $ pressure -= 1
            narrator "{cps=60}You say little, keeping your face neutral. You nod slowly, letting the coach finish his assessment.{/cps}"
            coach "Good. Your next actions on the training pitch will matter infinitely more than your words right now."

    $ add_note("Feedback dialogue supports social interaction between user, coach, and team context.")
    
    jump career_decision

label career_decision:
    scene bg transfer_meeting_room
    with dissolve
    
    show maya_chen at scout_right
    with dissolve
    
    narrator "{cps=60}The heavy door of the transfer room shuts, cutting off the noise of the boots in the corridor. Maya Chen looks up from her tablet, sliding a sleek folder across the polished table.{/cps}"

    if career_status == "rise":
        scout "I represent Northbridge FC. Bigger league, bigger stadium, bigger pressure. They’ve seen your data, [player_name], and they see you as a player who can become a star."
        coach "You can go now and chase the spotlight, or stay and become the definitive face of this club."
        
        narrator "{cps=60}As the coach speaks, you look through the glass window of the meeting room. Afiq is standing by his locker outside, staring in darkly. He knows what's on that table.{/cps}"
        scout "If you sign with Northbridge, you leave this academy behind today. You leapfrog right past Afiq and step straight into the professional spotlight."

    elif career_status == "average":
        scout "Northbridge is monitoring you, but they won't promise a first-team role yet. There may be a loan, a trial, or nothing at all if your next months stay ordinary."
        coach "Stay here, [player_name]. Build your game under a system you know, and make their next offer undeniable."
        
        narrator "{cps=60}The door cracks open slightly, and Afiq walks in to drop off a tactical folder for the coach. He catches your eye, a subtle smirk playing on his lips before he leaves.{/cps}"
        scout "Afiq’s presence is a roadblock here, but moving to Northbridge right now means entering a dogfight where nobody cares about your development. You have to choose your battle."

    else:
        scout "No big club is moving yet. They know your name, [player_name], but they also know your doubts and your inconsistency."
        coach "Your best transfer right now is from unreliable to trusted. Do that here first, on our training pitch."
        
        narrator "{cps=60}The weight of the trial sits heavy in the room. You know that if you don't fight back now, Afiq will permanently cement his position as the academy's golden boy.{/cps}"
        scout "The scouts are shifting their focus entirely to Afiq for the next Showcase window. If you stay, you are entering a war to reclaim your reputation."

    menu:
        "The folder sits open on the table. Choose your career path."
     
        "Accept the transfer to a bigger club" if career_status == "rise":
            $ career_path = "transfer"
            $ reputation += 2
            $ difficulty += 3
            $ loyalty -= 1
            $ pressure += 2
            
            scout "Brave. At Northbridge, every single touch is evaluated, but every great match travels twice as far."
            narrator "{cps=60}The route becomes glamorous but unforgiving. You arrive as a pivot player—someone the new club wants to build attacks and attention around.{/cps}"
            narrator "{cps=60}As you sign the paperwork, you realize your rivalry with Afiq isn't over. You've just set up a massive future collision on a much bigger stage.{/cps}"

        "Stay loyal and become a team leader":
            $ career_path = "loyal"
            $ loyalty += 3
            $ coach_opinion += 2
            $ teamwork += 2
            
            coach "Loyalty matters in this game. Stay, lead us, and this place will remember you differently."
            narrator "{cps=60}The route becomes deeply personal. You are not just chasing trophies; you are building a bond with supporters who saw you grow from the concrete courts.{/cps}"
            narrator "{cps=60}You decide to fight Afiq on his own territory. You will take his captaincy, take his starting spot, and earn your legacy right here.{/cps}"
    
        "Stay and fight for a future transfer":
            $ career_path = "develop"
            $ reputation += 1
            $ difficulty += 1
            $ confidence += 1
            $ teamwork += 1
            
            if career_status == "average":
                scout "That may be wise. Become completely impossible to ignore, and the next transfer window changes entirely."
                coach "Good. Rise here first, then choose your next step from a position of absolute strength."
            elif career_status == "fail":
                coach "This is the correct fight. Earn training trust, earn minutes, and then you will earn the headlines."
            else:
                scout "You are gambling that waiting will make the final offer even bigger. It's a high-stakes bet on your own feet."
                
            narrator "{cps=60}You keep the dream alive without ending the story early. You refuse to flee the academy, choosing to sharpen your blade until Afiq can no longer look down on you.{/cps}"

    $ add_note("The transfer decision demonstrates feasibility and practicality: different paths reuse the same system but change difficulty.")
     
    jump advanced_match

label advanced_match:
    scene bg match_stadium_night
    with dissolve
    
    if career_path == "transfer":
        narrator "{cps=60}At Northbridge, you are introduced as the pivot player: not simply a casual signing, but a player expected to tilt the match instantly.{/cps}"
        narrator "{cps=60}The bigger club is louder, faster, and less patient. The opponent presses like a machine because they know the cameras are watching your debut.{/cps}"

        narrator "{cps=60}As you walk out onto the pitch, you spot a familiar face in the crowd near the tunnel. Afiq is sitting in the stands with an official academy tracking folder, taking notes.{/cps}"
        narrator "{cps=60}He catches your eye and raises his chin. He didn't come to cheer you on; he came to see if the big league is going to swallow you whole.{/cps}"

    elif career_path == "loyal":
        narrator "{cps=60}You stay. The coach honors your commitment, and the supporters sing your name loudly before kickoff.{/cps}"
        narrator "{cps=60}Your teammates know your movement. They trust your first touch before you even receive the ball.{/cps}"

        show captain at center with dissolve
        narrator "{cps=60}Afiq walks up to you in the center circle, adjusting his shinguards. The captain's armband sits tight on his sleeve.{/cps}"
        captain "The crowd is chanting for you, street-boy. Don't let it get to your head."
        captain "They trust you now, which means if you fail tonight, you aren't just letting yourself down—you're letting down everyone who turned away from a payday to stay here. Let's win this."
        hide captain with dissolve

    else:
        narrator "{cps=60}You are still at the club, still fighting for the next version of your career. Tonight, you finally start because training performance forced the coach's hand.{/cps}"
        show captain at center with dissolve
        narrator "{cps=60}Afiq looks at you as you line up in the tunnel. He is starting alongside you, but his expression is cold.{/cps}"
        captain "The coach gave you a chance because you ran yourself into the ground during drills. But running isn't the same as executing under stadium floodlights."
        captain "Don't get in my way out there. I'm chasing my own transfer window, and I won't let your redemption arc ruin my data."
        hide captain with dissolve

    if position == "Attacker":
        jump advanced_attacker
    elif position == "Midfielder":
        jump advanced_midfielder
    elif position == "Defender":
        jump advanced_defender
    else:
        jump advanced_goalkeeper

label advanced_attacker:
    narrator "{cps=60}The match becomes a fierce psychological and tactical duel between your direct movement and their defensive line. Thrive here, and the scouting story changes completely.{/cps}"
    
    menu:
        "Attacker: how do you take over?"
 
        "Attack the blindside of the centre-back all match":
            if skill + confidence + reputation - difficulty >= 7:
                $ advanced_match_result = "dominant win"
                $ reputation += 3
                $ confidence += 2
                $ fan_mood += 2
                narrator "{cps=60}You keep vanishing from the defender's shoulder, then appearing exactly where the cross lands.{/cps}"
                
                if career_path == "transfer":
                    narrator "{cps=60}From the stands, you see Afiq close his notebook and cross his arms. He looks shaken—you're dominating the tier he thought you'd freeze in.{/cps}"
                else:
                    show captain at center with dissolve
                    captain "Unbelievable movement, street-boy! They can't handle your pace. Keep driving them back!"
                    hide captain with dissolve
                    narrator "{cps=60}One goal, one won penalty, one night that feels like a career launch.{/cps}"
            else:
                $ advanced_match_result = "countered"
                $ reputation -= 1
                $ coach_opinion -= 1
                $ pressure += 2
                narrator "{cps=60}You make the runs, but impatience ruins your timing. Offside flags cut your rhythm to pieces.{/cps}"
                
                if career_path != "transfer":
                    show captain at center with dissolve
                    captain "Hold your run! You're starving us of possession by rushing into their trap!"
                    hide captain with dissolve

        "Drop between the lines and create chaos for teammates":
            if teamwork + coach_opinion + confidence >= 7:
                $ advanced_match_result = "team triumph"
                $ reputation += 2
                $ teamwork += 2
                $ loyalty += 1
                narrator "{cps=60}You drag defenders out, flick passes around corners, and create the winning goal without needing the final touch.{/cps}"
                
                if career_path != "transfer":
                    show captain at center with dissolve
                    narrator "{cps=60}Afiq screams in celebration as he latches onto your disguised flick, smashing it into the top corner.{/cps}"
                    captain "Brilliant vision! That's how we break a low block!"
                    hide captain with dissolve
            else:
                $ advanced_match_result = "isolated"
                $ reputation -= 1
                narrator "{cps=60}You drop deep, but nobody reads it. Instead of becoming unpredictable, you find yourself miles away from the goal.{/cps}"
                
                if career_path != "transfer":
                    show captain at center with dissolve
                    captain "Stop crowding my space! If you keep dropping into the midfield circle, there's no target upfront!"
                    hide captain with dissolve

    jump advanced_match_wrap

label advanced_midfielder:
    narrator "{cps=60}The match is frantic until your boots touch the ball. Your challenge is to decide whether the game needs art, order, or bite.{/cps}"
    
    menu:
        "Midfielder: how do you dominate?"
 
        "Control tempo with quick switches and calm possession":
            if coach_opinion + teamwork + loyalty + skill >= 8:
                $ advanced_match_result = "disciplined success"
                $ reputation += 2
                $ coach_opinion += 2
                $ teamwork += 1
                narrator "{cps=60}You slow the game when it panics and speed it up when space appears. By full-time, it feels like everyone played inside your rhythm.{/cps}"
                
                if career_path != "transfer":
                    show captain at center with dissolve
                    captain "Excellent maturity out there. You made the match breathe when they tried to press us."
                    hide captain with dissolve
            else:
                $ advanced_match_result = "too passive"
                $ reputation -= 1
                $ confidence -= 1
                narrator "{cps=60}You keep possession, but without enough tactical bravery. The opponent comfortably lets you have harmless sideways passes.{/cps}"
                
                if career_path != "transfer":
                    show captain at center with dissolve
                    captain "Stop passing it backward! Break the lines! We're chasing the game and you're playing it safe!"
                    hide captain with dissolve

        "Break lines with risky forward passes":
            if skill + confidence + reputation >= 7:
                $ advanced_match_result = "creative masterclass"
                $ reputation += 3
                $ confidence += 1
                $ fan_mood += 1
                narrator "{cps=60}You split the midfield three times, and each pass feels like opening a locked door. The scouts write quickly in their tablets.{/cps}"
                
                if career_path != "transfer":
                    show captain at center with dissolve
                    narrator "{cps=60}Your perfectly weighted through ball sends Afiq clear on goal. He scores cleanly and points directly back at you.{/cps}"
                    captain "Unbelievable ball! Keep feeding me those!"
                    hide captain with dissolve
            else:
                $ advanced_match_result = "forced creativity"
                $ pressure += 2
                $ reputation -= 1
                narrator "{cps=60}You chase the highlight pass too often. The constant turnovers invite heavy counter-pressure and the coach starts shouting for control.{/cps}"
                
                if career_path != "transfer":
                    show captain at center with dissolve
                    captain "The lane wasn't even open! You're throwing away possession trying to be a hero!"
                    hide captain with dissolve

    jump advanced_match_wrap

label advanced_defender:
    narrator "{cps=60}Their forward line is fast, loud, and dangerous. Your job is to make their night smaller with every single duel.{/cps}"
    
    menu:
        "Defender: how do you thrive?"
 
        "Lead a high defensive line and catch runners offside":
            if coach_opinion + teamwork + skill >= 7:
                $ advanced_match_result = "defensive command"
                $ reputation += 2
                $ coach_opinion += 2
                $ teamwork += 2
                narrator "{cps=60}You step, shout, hold, and step again. Their attackers keep running straight into your trap, and your back line moves like one single body.{/cps}"
                
                if career_path != "transfer":
                    show captain at center with dissolve
                    captain "Great leadership from the back, [player_name]! Your organization saved our midfield engine today."
                    hide captain with dissolve
            else:
                $ advanced_match_result = "line broken"
                $ pressure += 2
                $ reputation -= 1
                narrator "{cps=60}The tactical idea is brave, but the line is completely disconnected. One mistimed step gives their striker wide-open grass.{/cps}"
                
                if career_path != "transfer":
                    show captain at center with dissolve
                    captain "Wake up! If you're going to step up, you have to call it out louder! You left the whole flank exposed!"
                    hide captain with dissolve

        "Absorb pressure and win every duel in the box":
            if skill + confidence + loyalty >= 6:
                $ advanced_match_result = "wall performance"
                $ reputation += 3
                $ confidence += 1
                $ fan_mood += 1
                narrator "{cps=60}Crosses come raining in, and you meet them all: forehead, chest, boot, whatever the desperate moment demands. The crowd begins celebrating your clearances.{/cps}"
                
                if career_path != "transfer":
                    show captain at center with dissolve
                    narrator "{cps=60}After a massive goal-line block, Afiq rushes back into the box to pull you up by your jersey, slapping your shoulder.{/cps}"
                    captain "That is pure heart! Absolute wall!"
                    hide captain with dissolve
            else:
                $ advanced_match_result = "survived pressure"
                $ reputation += 1
                $ pressure += 1
                narrator "{cps=60}You survive the onslaught, but it is incredibly messy. Scrambles, deflections, and desperate clearances keep the score alive.{/cps}"

    jump advanced_match_wrap

label advanced_goalkeeper:
    narrator "{cps=60}The game keeps dragging you into massive, decisive moments. Goalkeepers do not get many touches, but every single touch feels like a final verdict.{/cps}"
    
    menu:
        "Goalkeeper: how do you command the match?"
 
        "Play as a sweeper keeper and start attacks early":
            if skill + confidence + coach_opinion >= 7:
                $ advanced_match_result = "sweeper star"
                $ reputation += 3
                $ confidence += 2
                narrator "{cps=60}You clear danger way outside your box, clip accurate passes straight into midfield, and turn saves into instant counterattacks. The team plays ten meters higher because of you.{/cps}"
                
                if career_path != "transfer":
                    show captain at center with dissolve
                    captain "Your distribution is clinical today! It completely bypassed their initial press!"
                    hide captain with dissolve
            else:
                $ advanced_match_result = "risky keeper"
                $ pressure += 2
                $ coach_opinion -= 1
                narrator "{cps=60}You try to play high, but one loose touch nearly gifts an open goal. The stadium gasps before your defender slides in to rescue you.{/cps}"
                
                if career_path != "transfer":
                    show captain at center with dissolve
                    captain "Stop playing with fire back there! Clear the ball if you're under pressure!"
                    hide captain with dissolve

        "Command the box and make the late save":
            if teamwork + skill + reputation >= 6:
                $ advanced_match_result = "captain save"
                $ reputation += 2
                $ coach_opinion += 2
                $ teamwork += 1
                $ fan_mood += 1
                narrator "{cps=60}You claim heavy crosses through traffic, shout your defense into defensive shape, then fly completely across goal in stoppage time to push a header wide.{/cps}"
                
                if career_path != "transfer":
                    show captain at center with dissolve
                    captain "You won us the points tonight, simple as that. World-class save!"
                    hide captain with dissolve
            else:
                $ advanced_match_result = "quiet keeper"
                $ reputation += 1
                $ confidence -= 1
                narrator "{cps=60}You avoid total disaster, but absolute command never fully arrives. The clean sheet survives more than it truly shines.{/cps}"

    jump advanced_match_wrap

label advanced_match_wrap:
    $ skill = clamp_stat(skill)
    $ coach_opinion = clamp_stat(coach_opinion)
    $ confidence = clamp_stat(confidence)
    $ reputation = clamp_stat(reputation)
    $ loyalty = clamp_stat(loyalty)
    $ teamwork = clamp_stat(teamwork)
    $ pressure = clamp_stat(pressure)
    $ fan_mood = clamp_stat(fan_mood)
    $ add_note("The final challenge combines several earlier variables, rewarding learnability and replay.")

    jump final_outcome

label final_outcome:
    scene bg career_outcome_celebration
    with fade
 
    hide screen career_hud
 
    narrator "{cps=60}The long, grueling season finally reaches its curtain call. The final whistles have blown, the stands are empty, and your career data has been definitively analyzed by the coaching staff and international scouts.{/cps}"
    
    $ final_score = skill + coach_opinion + confidence + reputation + loyalty + teamwork + fan_mood - difficulty - pressure
 
    if final_score >= 13 and career_path == "loyal":
        $ final_title = "Club Legend: The Passing of the Armband"
        $ final_message = "You stayed loyal, shouldered the immense local pressure, and became the iconic leader the supporters will sing about for generations. You didn't just survive the academy—you conquered it."
        
        show captain at center with dissolve
        narrator "{cps=60}At the year-end awards ceremony, the room falls silent as Afiq approaches your table. The bitter glare he carried all season is completely gone, replaced by a profound, heavy respect.{/cps}"
        captain "I spent three years guarding my legacy here, [player_name]. I hated you because I knew the concrete courts gave you something I could never match."
        captain "But watching you bleed for this badge... you didn't just take my starting shirt. You earned it."
        narrator "{cps=60}Afiq unclips the captain's armband from his suit jacket and presses it firmly into your hand.{/cps}"
        captain "Lead them well next season, Captain."
        hide captain with dissolve

    elif final_score >= 13 and career_path == "transfer":
        $ final_title = "Superstar Arrival: Shockwaves Back Home"
        $ final_message = "The massive transfer to Northbridge didn't swallow you whole. You successfully transformed into their definitive pivot player, dominating the top-tier league under global spotlight."
        
        narrator "{cps=60}As flashing cameras surround you at the Northbridge press conference, your phone buzzes violently in your pocket with an unexpected text message from back home.{/cps}"
        narrator "{cps=60}It's from Afiq: 'I watched your debut goal on the national sports networks tonight. The academy boys are completely losing their minds.'{/cps}"
        narrator "{cps=60}The text continues: 'You actually leapfrogged past me and made it to the big stage. Don't dare look back now, street-boy. Make sure the world never forgets how hard we had to fight each other to get here.'{/cps}"

    elif final_score >= 13:
        $ final_title = "Breakthrough Prospect: The Cold Truce"
        $ final_message = "You delayed the early transfer, using targeted development to build unstoppable momentum. Now, you hold all the leverage for the upcoming international window."
        
        show captain at center with dissolve
        narrator "{cps=60}Late at night, as the stadium floodlights click off one by one, you find Afiq standing alone by the touchline, looking out at the dark pitch.{/cps}"
        captain "Every single European scout who booked a flight to watch me this month ended up writing your name down in bold ink instead. You completely disrupted my life's plan, kid."
        narrator "{cps=60}He turns to you, a cold, competitive smirk cutting through the shadows.{/cps}"
        captain "But honestly? It's the most pushed and alive I've felt since joining this academy. Enjoy the praise for now. Next season, the war starts all over again."
        hide captain with dissolve

    elif final_score >= 7:
        $ final_title = "Professional Squad Player: The Locker Room Warning"
        $ final_message = "You aren't a runaway breakout superstar yet, but your professional career is firmly alive. You log the training miles, survive criticism, and remain a highly reliable asset."
        
        show captain at center with dissolve
        narrator "{cps=60}As you pack your gear into your duffel bag to head home for the off-season break, Afiq leans heavily against your locker door, blocking your path.{/cps}"
        captain "You survived the first year, street-boy. I'll give you credit for that—most trialists fade away by October."
        captain "But stable, ordinary numbers won't get you a contract in the top tier. Rest up, because if you don't find an extra gear during pre-season, I'm taking your minutes back."
        hide captain with dissolve

    elif final_score >= 2:
        $ final_title = "Second Chance Season: Under the Captain's Heel"
        $ final_message = "You stumbled through critical fixtures, but the manager is throwing you a final structural lifeline. Your path forward requires a desperate, genuine fight to reclaim trust."
        
        show captain at center with dissolve
        narrator "{cps=60}You step out of Coach Rahman's office after a brutal, exhausting contract review. Afiq is waiting in the corridor, his arms crossed, shaking his head with utter disdain.{/cps}"
        captain "The gaffer is being incredibly soft on you because of your raw background. But luck runs out fast on this grass."
        captain "You dragged our tactical shape down this year, and you're lucky you weren't completely released. If I catch you slacking off on your positioning drills ever again, I will personally see to it that you're buried on the bench forever."
        hide captain with dissolve

    else:
        $ final_title = "Hard Reset: Expelled from the Gates"
        $ final_message = "The harsh reality of professional football completely exposed your poor preparation, fractured relationships, and reckless choices. The academy has terminated your registration."
        
        show captain at center with dissolve
        narrator "{cps=60}As you carry your cardboard box of personal belongings out past the iron academy gates, you look up one last time.{/cps}"
        narrator "{cps=60}Afiq is standing high up on the clubhouse balcony, adjusting his captain's armband in the morning sun, looking down at you like a distant memory.{/cps}"
        captain "I warned you from the very first dawn, kid. This isn't the concrete playgrounds. You thought your ego could replace structural discipline, and now you're heading back exactly where you started."
        narrator "{cps=60}He turns his back on you, walking back into the facility as the gate locks shut.{/cps}"
        captain "It's a genuine shame... you actually had the feet for it."
        hide captain with dissolve

    $ add_note("Rival storyline reaches its definitive dramatic resolution, ensuring high narrative closure.")
    $ add_note("System output correctness verified: score directly correlates to Afiq's final behavioral shift.")
 
    narrator "{cps=60}[final_title]{/cps}"
    narrator "{cps=60}[final_message]{/cps}"
 
    jump end_screen_label
 
label end_screen_label:
    call screen project_end_screen(final_title, final_message, final_score)
 
    if _return == "replay":
        jump reset_story
 
    return