define narrator = Character(None)
define player = Character("[player_name]")
define coach = Character("Coach Rahman", color="#58d68d")
define scout = Character("Maya Chen", color="#79b8ff")
define captain = Character("Afiq", color="#ffd166")
define teammate = Character("Daniel", color="#a8d8ea")
define analyst = Character("Performance Analyst", color="#d7b7ff")


image bg stadium_dawn = "images/stadium_dawn.png"
image bg opening_stadium = "images/opening_stadium.png"
image bg stadium_day = "images/stadium_day.png"
image bg training_ground = "images/training_ground.png"
image bg training_ground_real = "images/training_ground_real.png"
image bg match_night = "images/match_night.png"
image bg match_stadium_night = "images/match_stadium_night.png"
image bg office = "images/office.png"
image bg coach_office_real = "images/coach_office_real.png"
image bg transfer_meeting_room = "images/transfer_meeting_room.png"
image bg finale = "images/finale.png"
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
<<<<<<< Updated upstream
=======
image top_bar = Solid("#000")
image bottom_bar = Solid("#000")
image afiq = "images/afiq.png"
image main_player_front = "images/main_player_front.png"

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
>>>>>>> Stashed changes

transform scale_up:
    zoom 0.6

transform scale_down:
    zoom 0.6

transform scout_right:
    xalign 0.84
    yalign 1.0
    zoom 0.72

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
    show main_player at center, scale_up
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
<<<<<<< Updated upstream
    with fade
=======
>>>>>>> Stashed changes

    narrator "You are [player_name], a young footballer who grew up chasing a torn ball across narrow streets, empty car parks, and one stubborn little field behind the school."
    narrator "Your boots are not new. Your family still checks the price of every away trip. But when the ball comes to you, the noise of ordinary life disappears."
    scene bg academy_gate_behind
    with fade
    show main_player_behind at center, scale_up
    narrator "Tonight, you walk through the academy gate for the first time."
    scene bg academy_gate_front
    with dissolve
    show main_player_front at center, scale_up
    narrator "Beyond it are floodlights, scouts, contracts, rival players, dressing-room politics, and the quiet fear that maybe the dream is bigger than you."
    scene bg academy_pitchside_night
    with dissolve
<<<<<<< Updated upstream
    teammate "You are the new one, right? Afiq. Do not look so shocked. Everyone gets nervous the first day."
=======
    show afiq at left, scale_down with dissolve
    captain "You are the new one, right? Do not look so shocked. Everyone gets nervous the first day."
>>>>>>> Stashed changes
    player "I thought getting here would feel like the finish line."
    coach "It is not the finish line, [player_name]. It is the first whistle."
    coach "Talent brought you to this field. Discipline decides whether you stay. Courage decides whether anyone remembers you."

    $ add_note("Target users receive a simple goal immediately: guide a player toward a professional career.")

# --- NEW DRAMA EXPANSION BEGINS HERE ---

    narrator "Coach Rahman walks away, his whistle gleaming under the floodlights. The moment he is out of earshot, the quiet evening air shatters."

    show main_player at left with dissolve
    show teammate at right with dissolve

    teammate "Don't let the old man's speeches get to your head, 'prodigy'."

    narrator "Afiq tosses a mud-stained training bib right at your chest. It lands with a heavy, wet thud."

    teammate "Look around you. Half the guys here were captain of their state teams. The other half have fathers who played in the top tier."
    teammate "Then you walk in with boots that look like they survived a war, and suddenly the scouts are whispering?"

    player "I earned my trial here just like everyone else, Afiq."

    teammate "Trial? This isn't a playground. There are only two open spots left on the registration list for the upcoming cup tournament."
    teammate "If you rise, someone else falls. I've spent three years bleeding for this academy. I'm not letting some street-baller take my spot in the showcase."

    narrator "The surrounding academy players stop their drills, turning their heads to watch the confrontation. The pressure in your chest tightens like a vice."

    menu:
        "How do you handle Afiq's open hostility?"

        "Keep your cool and let your football do the talking":
            $ teamwork += 1
            $ coach_opinion += 1
            $ pressure += 1
            player "Then don't worry about me, Afiq. Worry about keeping up with me on the pitch."
            teammate "Arrogant, aren't we? Let's see if that mouth can save you when the tackles start flying."
            narrator "You swallow your anger and look past him toward the grass. You've faced tougher critics on concrete streets."

        "Fire back and draw a line in the sand":
            $ confidence += 2
            $ pressure += 2
            $ teamwork -= 1
            player "If your three years of hard work can be threatened by 'some street-baller' in one day, maybe you aren't as good as you think you are."
            narrator "A collective 'oh' ripples through the watching players. Afiq steps up, chest to chest, his eyes burning."
            teammate "You're going to regret saying that. When we get into the match drills, I'm personally making sure you don't finish the session."

        "Defuse the situation and show humility":
            $ teamwork += 2
            $ confidence -= 1
            player "I'm not here to take anyone's place, man. I'm just trying to help my family. We can both make the squad if we play together."
            narrator "Afiq blinks, momentarily caught off guard by your lack of malice, before scowling and stepping back."
            teammate "This is professional football, not a charity. There is no 'together' when a contract is on the line."

    narrator "Before the tension can boil over into a physical fight, a sharp blast of a whistle echoes across the training ground."

    captain "Daniel! [player_name]! If you two have that much energy to waste, you can run laps until midnight!"

    narrator "The crowd scatter instantly, retrieving their footballs as Coach Rahman approaches with a clipboard, his eyes narrowing at the group."

    jump choose_position

label choose_position:
    scene bg training_ground_real
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
    scene bg training_ground_real
    with dissolve

    narrator "The first elite training session is faster than expected. Players sprint, collide, recover, shout, reset, and sprint again."
    coach "Today is not about looking talented. Today is about proving you can repeat good decisions when your lungs are burning."

    if position == "Attacker":
        narrator "Your drill is ruthless: curved runs behind the line, first-time finishing, weak-foot shots, and pressing triggers when the defender receives with a bad touch."
    elif position == "Midfielder":
        narrator "Your drill is a storm of rondos, half-turn receiving, scanning before the pass, switch-of-play timing, and resisting the urge to force every ball forward."
    elif position == "Defender":
        narrator "Your drill is built on duels: body shape, recovery runs, last-second blocks, defensive headers, and choosing when to step out or hold the line."
    else:
        narrator "Your drill is lonely and loud: reaction saves, crosses through traffic, one-on-ones, distribution under pressure, and commanding defenders who barely know you."

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
                narrator "You repeat finishes until the movement feels automatic: near post, far post, chip, driven shot, cutback."
            elif position == "Midfielder":
                narrator "You ask for extra rondo rounds and learn to receive with your body open before pressure arrives."
            elif position == "Defender":
                narrator "You practice recovery tackles until your timing stops being desperate and starts being clean."
            else:
                narrator "You face shot after shot until diving no longer feels dramatic, only necessary."

        "Train smart and ask for detailed feedback":
            $ training_focus = "smart"
            $ skill += 2
            $ coach_opinion += 2
            $ teamwork += 1
            coach "That is professional behavior. You improve faster when you understand why."
            analyst "Your clips are not perfect, but you are asking the right questions. That matters."
            narrator "You learn the system instead of just surviving the drill."

        "Do the minimum and save energy for match day":
            $ training_focus = "minimum"
            $ skill += 1
            $ confidence += 1
            $ coach_opinion -= 1
            coach "Careful. Rest is useful, but the staff must believe you are committed."
            narrator "You feel fresh, but the coach writes something short on his clipboard. Short notes are rarely comforting."

        "Skip training and hope nobody notices":
            $ training_focus = "skip"
            $ skill -= 1
            $ coach_opinion -= 3
            $ confidence -= 1
            $ reputation -= 1
            coach "[player_name], football is a team activity. When you disappear, everyone else pays for it."
            narrator "The system makes the error recoverable, but the consequence is clear."

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
    scene bg match_stadium_night
    with dissolve

    if not first_start:
        jump bench_arc

    narrator "The team sheet goes up on the wall. Your name is in the starting lineup."
    captain "First start. Do not play the occasion. Play the ball."
    narrator "By the 83rd minute, the match is tied. Rain shines under the floodlights. Every pass sounds louder than it should."

    if position == "Attacker":
        narrator "A long diagonal drops behind the full-back. You bring it down inside the box. The goalkeeper steps forward, and Afiq screams for the square pass."
        jump first_match_attacker
    elif position == "Midfielder":
        narrator "You receive between the lines with one touch to turn. Afiq is sprinting behind the centre-backs, but the opponent's midfield is tired and the game is ready to be controlled."
        jump first_match_midfielder
    elif position == "Defender":
        narrator "The opponent breaks down your side. Their winger cuts inside, their striker darts across your shoulder, and one wrong step opens the goal."
        jump first_match_defender
    else:
        narrator "A loose back pass slows in the wet grass. Their striker reaches it first. Suddenly it is just you, the attacker, and the sound of the crowd rising."
        jump first_match_goalkeeper

label bench_arc:
    narrator "The team sheet goes up on the wall. Your eyes search once, twice, then stop."
    narrator "Your name is not in the starting eleven."
    coach "You are on the bench today. This is not punishment. This is information."
    player "I can help the team."
    coach "Then prove it from minute one of training tomorrow. A career is not built only on match nights."
    narrator "For eighty minutes, you sit in a jacket, watching players in your position make the runs, tackles, passes, or saves you imagined for yourself."
    narrator "The match ends in a draw. Nobody blames you. Somehow, that hurts more."
    captain "Do not disappear because of one bench. Make the coach feel uncomfortable leaving you out."

    menu:
        "How do you begin the hard-work arc?"

        "Arrive early for two weeks and rebuild trust":
            $ skill += 3
            $ coach_opinion += 3
            $ confidence += 1
            $ teamwork += 1
            $ first_match_result = "bench comeback"
            narrator "You become the first player on the training pitch and the last one out. The staff stop talking about your absence and start talking about your response."
            coach "This is what I wanted to see. The bench can break a player, or it can sharpen one."

        "Ask senior players to mentor you":
            $ skill += 2
            $ coach_opinion += 2
            $ teamwork += 2
            $ first_match_result = "bench learner"
            narrator "You learn tiny professional habits: how to recover, when to speak, how to read a defender's hips, how to stay ready without sulking."
            captain "You listened. That is why you are still moving forward."

        "Complain and wait for another chance":
            $ confidence += 1
            $ coach_opinion -= 2
            $ reputation -= 1
            $ pressure += 2
            $ first_match_result = "bench frustration"
            narrator "Your frustration is understandable, but it leaks into your body language. Staff notice everything at this level."
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
    menu:
        "Attacker: pass or shoot?"

        "Pass across goal to Afiq":
            if skill + teamwork >= 4:
                $ first_match_result = "assist"
                $ reputation += 2
                $ coach_opinion += 2
                $ confidence += 1
                $ teamwork += 1
                narrator "You wait half a heartbeat, pull the goalkeeper toward you, and slide the ball across the six-yard box. Afiq scores into an open net."
                captain "That was perfect. You saw the move before everyone else."
            else:
                $ first_match_result = "blocked pass"
                $ coach_opinion -= 1
                $ pressure += 1
                narrator "The idea is generous, but the pass is underhit. A defender slides in and the chance dies."

        "Shoot before the goalkeeper sets":
            if skill + confidence >= 5:
                $ first_match_result = "goal"
                $ reputation += 3
                $ coach_opinion += 2
                $ confidence += 2
                $ fan_mood += 2
                narrator "You strike early. The ball flashes across the goalkeeper and kisses the inside of the far post. Goal."
                coach "That is the kind of courage scouts remember."
            else:
                $ first_match_result = "miss"
                $ coach_opinion -= 1
                $ pressure += 1
                narrator "You shoot with your heart more than your technique. It rises over the bar, and the chance follows it into the rain."

    jump first_match_wrap

label first_match_midfielder:
    menu:
        "Midfielder: risk the killer pass or control the game?"

        "Thread the through ball to the open attacker":
            if skill + teamwork >= 4:
                $ first_match_result = "through ball assist"
                $ reputation += 2
                $ coach_opinion += 2
                $ teamwork += 2
                narrator "You disguise your hips, wait for Afiq's second run, and slide the ball through a gap that was open for less than a second."
                captain "I only had to run. You gave me the goal."
            else:
                $ first_match_result = "forced pass"
                $ reputation -= 1
                $ pressure += 1
                narrator "You see the run, but force the pass too late. The centre-back reads it and launches a counter."

        "Control the game and move the tired defense":
            if coach_opinion + teamwork >= 4:
                $ first_match_result = "tempo control"
                $ coach_opinion += 2
                $ teamwork += 2
                $ confidence += 1
                narrator "You refuse the rushed pass, recycle possession, switch play twice, and make the opponent chase until a gap opens naturally."
                coach "That is midfield maturity. You made the match breathe at your speed."
            else:
                $ first_match_result = "too slow"
                $ confidence -= 1
                narrator "You try to calm the match, but your touches become safe instead of purposeful. The crowd senses the chance fading."

    jump first_match_wrap

label first_match_defender:
    menu:
        "Defender: stop the attack now or protect the box?"

        "Step out and make the tackle before the striker turns":
            if skill + confidence + coach_opinion >= 5:
                $ first_match_result = "last tackle"
                $ reputation += 2
                $ coach_opinion += 2
                $ confidence += 1
                narrator "You read the heavy touch, step in cleanly, and take the ball before the striker can shoot. The stadium reacts like it was a goal."
                coach "That tackle was brave because it was timed, not because it was wild."
            else:
                $ first_match_result = "mistimed tackle"
                $ reputation -= 1
                $ coach_opinion -= 1
                $ pressure += 2
                narrator "You lunge half a second early. The striker skips past you, and only a desperate recovery from your teammate saves the match."

        "Drop, block the passing lane, and force a wide shot":
            if teamwork + coach_opinion >= 4:
                $ first_match_result = "defensive stand"
                $ coach_opinion += 2
                $ teamwork += 2
                narrator "You hold the line, point your full-back inside, and close the shooting angle. The opponent fires wide from frustration."
                captain "You kept us organized. I heard you the whole way."
            else:
                $ first_match_result = "invited pressure"
                $ pressure += 1
                $ confidence -= 1
                narrator "You drop too deep. The box fills with panic, and the clearance is ugly enough to make everyone shout at once."

    jump first_match_wrap

label first_match_goalkeeper:
    menu:
        "Goalkeeper: attack the one-on-one or wait him out?"

        "Rush out, spread your body, and close the angle":
            if skill + confidence >= 4:
                $ first_match_result = "one on one save"
                $ reputation += 3
                $ coach_opinion += 2
                $ confidence += 2
                $ fan_mood += 1
                narrator "You explode forward, stay big, and block the shot with your trailing leg. For a second, the whole stadium forgets how to breathe."
                coach "That is goalkeeping. Decision first, reflex second."
            else:
                $ first_match_result = "rounded keeper"
                $ reputation -= 1
                $ pressure += 2
                narrator "You rush with too much panic. The striker touches around you, and your defender clears from the line just in time."

        "Hold your ground and read the striker's finish":
            if coach_opinion + skill >= 4:
                $ first_match_result = "composed save"
                $ reputation += 2
                $ coach_opinion += 2
                $ teamwork += 1
                narrator "You wait until the striker commits, then drop low to smother the finish. The save looks calm because the decision was brave."
                captain "You saved us. Simple as that."
            else:
                $ first_match_result = "late reaction"
                $ confidence -= 1
                $ coach_opinion -= 1
                narrator "You hesitate between rushing and waiting. The shot slips under your hand and thuds into the advertising board just outside the post."

    jump first_match_wrap

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
    scene bg coach_office_real
    with dissolve

    coach "Sit down, [player_name]. The staff want to review where your career is heading."

    if first_match_result in ["goal", "assist", "through ball assist", "tempo control", "last tackle", "defensive stand", "one on one save", "composed save", "bench comeback"]:
        $ career_status = "rise"
        coach "You are rising. Not because everything is perfect, but because your choices under pressure are starting to look professional."
        $ reputation += 1
        analyst "The staff report says you affected the match in your position instead of playing like a generic player."
    elif coach_opinion >= 1 or first_match_result in ["bench learner"]:
        $ career_status = "average"
        coach "You are not failing, but you are not separating yourself yet. Right now you are part of the squad, not the reason the squad changes."
        analyst "The numbers are stable. The question is whether you can turn stable into special."
    else:
        $ career_status = "fail"
        coach "This is a setback. Your ability is not erased, but your reliability is now the main question."
        $ reputation -= 1
        $ pressure += 1
        coach "You will get another chance here, but the next chapter has to show work before it shows ambition."

    menu:
        "How do you respond to feedback?"

        "Accept it and ask for a specific improvement plan":
            $ coach_opinion += 2
            $ teamwork += 1
            $ confidence += 1
            coach "Good. Specific feedback creates specific progress."

        "Defend your decision emotionally":
            $ confidence += 1
            $ coach_opinion -= 1
            $ pressure += 1
            coach "I like confidence. I do not like excuses."

        "Stay quiet and reflect":
            $ coach_opinion += 1
            $ pressure -= 1
            narrator "You say little, but your next actions will matter more than your words."

    $ add_note("Feedback dialogue supports social interaction between user, coach, and team context.")

    jump career_decision

label career_decision:
    scene bg transfer_meeting_room
    with dissolve

    show maya_chen at scout_right
    with dissolve

    if career_status == "rise":
        scout "I represent Northbridge FC. Bigger league, bigger stadium, bigger pressure. They see you as a player who can become a star."
        coach "You can go now and chase the spotlight, or stay and become the face of this club."
    elif career_status == "average":
        scout "Northbridge will not promise a first-team role yet. There may be a loan, a trial, or nothing if your next months stay ordinary."
        coach "Stay, build your game, and make the offer undeniable."
    else:
        scout "No big club is moving yet. They know your name, but they also know your doubts."
        coach "Your best transfer right now is from unreliable to trusted. Do that here first."

    menu:
        "Choose your career path."

        "Accept the transfer to a bigger club" if career_status == "rise":
            $ career_path = "transfer"
            $ reputation += 2
            $ difficulty += 3
            $ loyalty -= 1
            $ pressure += 2
            scout "Brave. At Northbridge, every touch is evaluated, but every great match travels further."
            narrator "The route becomes glamorous but unforgiving. You arrive as a pivot player, someone the new club wants to build attacks and attention around."

        "Stay loyal and become a team leader":
            $ career_path = "loyal"
            $ loyalty += 3
            $ coach_opinion += 2
            $ teamwork += 2
            coach "Loyalty matters. Stay, lead us, and this place will remember you differently."
            narrator "The route becomes personal. You are not just chasing trophies; you are building a bond with supporters who saw you grow."

        "Stay and fight for a future transfer":
            $ career_path = "develop"
            $ reputation += 1
            $ difficulty += 1
            $ confidence += 1
            $ teamwork += 1
            if career_status == "average":
                scout "That may be wise. Become impossible to ignore, then the next window changes."
                coach "Good. Rise here first, then choose from strength."
            elif career_status == "fail":
                coach "This is the correct fight. Earn training trust, earn minutes, then earn headlines."
            else:
                scout "You are gambling that waiting will make the offer even bigger."
            narrator "You keep the dream alive without ending the story early."

    $ add_note("The transfer decision demonstrates feasibility and practicality: different paths reuse the same system but change difficulty.")

    jump advanced_match

label advanced_match:
    scene bg match_stadium_night
    with dissolve

    if career_path == "transfer":
        narrator "At Northbridge, you are introduced as the pivot player: not simply a signing, but a player expected to tilt the match."
        narrator "The bigger club is louder, faster, and less patient. The opponent presses like a machine because they know the cameras are watching you."
    elif career_path == "loyal":
        narrator "You stay. The captain gives you the armband for the cup night, and the supporters sing your name before kickoff."
        narrator "Your teammates know your movement. They trust your first touch before you even receive the ball."
    else:
        narrator "You are still at the club, still fighting for the next version of your career. Tonight, you start because training finally forced the coach's hand."

    if position == "Attacker":
        jump advanced_attacker
    elif position == "Midfielder":
        jump advanced_midfielder
    elif position == "Defender":
        jump advanced_defender
    else:
        jump advanced_goalkeeper

label advanced_attacker:
    narrator "The match becomes a duel between your movement and their defensive line. Thrive here, and the story changes."

    menu:
        "Attacker: how do you take over?"

        "Attack the blindside of the centre-back all match":
            if skill + confidence + reputation - difficulty >= 7:
                $ advanced_match_result = "dominant win"
                $ reputation += 3
                $ confidence += 2
                $ fan_mood += 2
                narrator "You keep vanishing from the defender's shoulder, then appearing where the cross lands. One goal, one won penalty, one night that feels like a launch."
            else:
                $ advanced_match_result = "countered"
                $ reputation -= 1
                $ coach_opinion -= 1
                $ pressure += 2
                narrator "You make the runs, but impatience ruins the timing. Offside flags cut your rhythm to pieces."

        "Drop between the lines and create chaos for teammates":
            if teamwork + coach_opinion + confidence >= 7:
                $ advanced_match_result = "team triumph"
                $ reputation += 2
                $ teamwork += 2
                $ loyalty += 1
                narrator "You drag defenders out, flick passes around corners, and create the winning goal without needing the final touch."
            else:
                $ advanced_match_result = "isolated"
                $ reputation -= 1
                narrator "You drop deep, but nobody reads it. Instead of becoming unpredictable, you become far from goal."

    jump advanced_match_wrap

label advanced_midfielder:
    narrator "The match is frantic until you touch the ball. Your challenge is to decide whether the game needs art, order, or bite."

    menu:
        "Midfielder: how do you dominate?"

        "Control tempo with quick switches and calm possession":
            if coach_opinion + teamwork + loyalty + skill >= 8:
                $ advanced_match_result = "disciplined success"
                $ reputation += 2
                $ coach_opinion += 2
                $ teamwork += 1
                narrator "You slow the game when it panics and speed it up when space appears. By full-time, it feels like everyone played inside your rhythm."
            else:
                $ advanced_match_result = "too passive"
                $ reputation -= 1
                $ confidence -= 1
                narrator "You keep possession, but without enough bravery. The opponent lets you have harmless passes."

        "Break lines with risky forward passes":
            if skill + confidence + reputation >= 7:
                $ advanced_match_result = "creative masterclass"
                $ reputation += 3
                $ confidence += 1
                $ fan_mood += 1
                narrator "You split the midfield three times, and each pass feels like opening a locked door. Scouts write quickly."
            else:
                $ advanced_match_result = "forced creativity"
                $ pressure += 2
                $ reputation -= 1
                narrator "You chase the highlight pass too often. The turnovers invite pressure and the coach starts shouting for control."

    jump advanced_match_wrap

label advanced_defender:
    narrator "Their forward is fast, loud, and confident. Your job is to make his night smaller with every duel."

    menu:
        "Defender: how do you thrive?"

        "Lead a high defensive line and catch runners offside":
            if coach_opinion + teamwork + skill >= 7:
                $ advanced_match_result = "defensive command"
                $ reputation += 2
                $ coach_opinion += 2
                $ teamwork += 2
                narrator "You step, shout, hold, and step again. Their attackers keep running into your trap, and your back line starts moving like one body."
            else:
                $ advanced_match_result = "line broken"
                $ pressure += 2
                $ reputation -= 1
                narrator "The idea is brave, but the line is not connected. One mistimed step gives the striker open grass."

        "Absorb pressure and win every duel in the box":
            if skill + confidence + loyalty >= 6:
                $ advanced_match_result = "wall performance"
                $ reputation += 3
                $ confidence += 1
                $ fan_mood += 1
                narrator "Crosses come in, and you meet them all: forehead, chest, boot, whatever the moment demands. The crowd begins celebrating clearances."
            else:
                $ advanced_match_result = "survived pressure"
                $ reputation += 1
                $ pressure += 1
                narrator "You survive, but it is messy. Blocks, scrambles, and desperate clearances keep the score alive."

    jump advanced_match_wrap

label advanced_goalkeeper:
    narrator "The game keeps dragging you into big moments. Goalkeepers do not get many touches, but every touch can feel like a verdict."

    menu:
        "Goalkeeper: how do you command the match?"

        "Play as a sweeper keeper and start attacks early":
            if skill + confidence + coach_opinion >= 7:
                $ advanced_match_result = "sweeper star"
                $ reputation += 3
                $ confidence += 2
                narrator "You clear danger outside the box, clip passes into midfield, and turn saves into counterattacks. The team plays ten meters higher because of you."
            else:
                $ advanced_match_result = "risky keeper"
                $ pressure += 2
                $ coach_opinion -= 1
                narrator "You try to play high, but one loose touch nearly gifts a goal. The stadium gasps before your defender rescues you."

        "Command the box and make the late save":
            if teamwork + skill + reputation >= 6:
                $ advanced_match_result = "captain save"
                $ reputation += 2
                $ coach_opinion += 2
                $ teamwork += 1
                $ fan_mood += 1
                narrator "You claim crosses through traffic, shout your defense into shape, then fly across goal in stoppage time to push a header wide."
            else:
                $ advanced_match_result = "quiet keeper"
                $ reputation += 1
                $ confidence -= 1
                narrator "You avoid disaster, but command never fully arrives. The clean sheet survives more than it shines."

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

    narrator "The season ends. Your career file is reviewed by coaches, analysts, scouts, and teammates."

    $ final_score = skill + coach_opinion + confidence + reputation + loyalty + teamwork + fan_mood - difficulty - pressure

    if final_score >= 13 and career_path == "loyal":
        $ final_title = "Club Legend"
        $ final_message = "You stay loyal, lead the club through pressure, and become the player supporters tell their children about. Your career is not only measured in trophies, but in belonging."
        $ add_note("Excellent loyal ending rewards relationship-building and long-term identity.")
    elif final_score >= 13 and career_path == "transfer":
        $ final_title = "Superstar Arrival"
        $ final_message = "The big transfer does not swallow you. You become a pivot player at a larger club, the kind of footballer teammates search for when the match becomes difficult."
        $ add_note("Excellent ending shows strong output correctness: positive choices produce a believable reward.")
    elif final_score >= 13:
        $ final_title = "Breakthrough at Home"
        $ final_message = "You delay the glamour move and turn development into momentum. By the next transfer window, the question is no longer whether you belong, but how high you want to climb."
        $ add_note("Development ending keeps the story open for a longer player-career structure.")
    elif final_score >= 7:
        $ final_title = "Professional Squad Player"
        $ final_message = "You are not yet a star, but the career is alive. You train, start important matches, survive criticism, and keep building toward the next transfer window."
        $ add_note("Middle ending supports realistic outcomes instead of only win-or-lose feedback.")
    elif final_score >= 2:
        $ final_title = "Second Chance Season"
        $ final_message = "You stumble, but the club gives you another chance. The next arc is clear: better habits, stronger trust, and a real fight to rise instead of fading."
        $ add_note("Recovery remains possible, which supports good interaction design after user mistakes.")
    else:
        $ final_title = "Hard Reset"
        $ final_message = "The season exposes poor preparation, weak relationships, or risky decisions. The dream is not erased, but the next chapter must begin with humility and work."
        $ add_note("Failed ending explains why the user failed instead of giving a vague result.")

    $ add_note("Future improvements: add rival storylines, injuries, media interviews, contract talks, national team call-ups, mentor relationships, and multi-season progression.")
    $ add_note("Suggested evaluation: ask users to complete one successful career path and rate clarity, feedback, engagement, and ease of recovery.")

    narrator "[final_title]"
    narrator "[final_message]"

    jump end_screen_label

label end_screen_label:
    call screen project_end_screen(final_title, final_message, final_score)

    if _return == "replay":
        jump reset_story

    return
