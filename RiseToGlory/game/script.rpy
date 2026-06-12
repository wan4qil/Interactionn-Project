define narrator = Character(None)
define player = Character("[player_name]")
define coach = Character("Coach Rahman", color="#58d68d")
define scout = Character("Maya Chen", color="#79b8ff")
define teammate = Character("Afiq", color="#ffd166")
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

transform scale_up:
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
    $ evaluation_notes = []

    show screen career_hud
    jump introduction

label introduction:
    scene bg opening_stadium
    with fade

    call screen chapter_card("Act I: The Worn Field", "A small-town player begins a career shaped by every decision.")

    narrator "You are [player_name], a young football player from a small town where the evening field lights flicker before every training session."
    narrator "The dream is simple: earn a professional contract. The path is not simple at all."
    player "I do not just want to play. I want to prove I can survive pressure."
    coach "Then learn this early. Talent opens the gate, but decisions decide whether you stay inside."

    $ add_note("Target users receive a simple goal immediately: guide a player toward a professional career.")

    jump choose_position

label choose_position:
    scene bg training_ground_real
    with dissolve

    coach "First, choose the role that matches how you think under pressure."

    menu:
        "Choose your main position."

        "Striker - high risk, high reward":
            $ position = "Striker"
            $ archetype = "Finisher"
            $ skill += 2
            $ confidence += 1
            $ pressure += 1
            narrator "You choose Striker. The team expects goals, and every missed chance will be remembered."

        "Midfielder - control and creativity":
            $ position = "Midfielder"
            $ archetype = "Playmaker"
            $ coach_opinion += 1
            $ teamwork += 2
            narrator "You choose Midfielder. Your job is to read the game and make others better."

        "Defender - discipline and leadership":
            $ position = "Defender"
            $ archetype = "Guardian"
            $ skill += 1
            $ coach_opinion += 2
            $ teamwork += 1
            narrator "You choose Defender. Mistakes are costly, but discipline can make you trusted quickly."

    $ renpy.notify("Role selected: " + position + " / " + archetype)
    $ add_note("Position selection changes the scoring model, giving users visible system response.")

    jump training_decision

label training_decision:
    scene bg training_ground_real
    with dissolve

    call screen chapter_card("Act II: Training Load", "The user tests effort, recovery, and consequences.")

    narrator "The first elite training session is faster than expected. Players sprint, collide, recover, and sprint again."
    coach "A professional routine is not just effort. It is effort with control."

    menu:
        "How do you train today?"

        "Push beyond the drill":
            $ skill += 3
            $ coach_opinion += 2
            $ confidence += 1
            $ pressure += 1
            coach "Excellent. You are hungry, and the squad can see it."
            narrator "You gain sharpness, but the extra pressure of expectations rises."

        "Train smart and ask for feedback":
            $ skill += 2
            $ coach_opinion += 2
            $ teamwork += 1
            coach "That is professional behavior. You improve faster when you understand why."
            narrator "You learn the system instead of just surviving the drill."

        "Save energy for the match":
            $ skill += 1
            $ confidence += 1
            $ coach_opinion -= 1
            coach "Careful. Rest is useful, but the staff must believe you are committed."
            narrator "You feel fresh, but the coach watches you with a little doubt."

        "Skip training and hope nobody notices":
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

    jump first_match

label first_match:
    scene bg match_stadium_night
    with dissolve

    call screen chapter_card("Act III: First Match", "A pressure choice tests the player's role and preparation.")

    narrator "Your team is tied with two minutes left. Rain shines under the floodlights. The ball rolls toward you at the edge of the penalty area."

    if position == "Defender":
        teammate "You have space, but do not lose the shape!"
    elif position == "Midfielder":
        teammate "Scan! There is a runner between the centre-backs!"
    else:
        teammate "This is yours. Finish it!"

    menu:
        "What do you do?"

        "Pass to the teammate making a run":
            if skill + teamwork >= 4 or position == "Midfielder":
                $ first_match_result = "assist"
                $ reputation += 2
                $ coach_opinion += 2
                $ confidence += 1
                $ teamwork += 1
                narrator "You disguise the pass and split the defense. Afiq scores. Assist."
                teammate "That was perfect. You saw the move before everyone else."
            else:
                $ first_match_result = "safe pass"
                $ reputation += 1
                $ coach_opinion += 1
                narrator "Your pass keeps possession, but it arrives too late to create a clear chance."

        "Shoot before the defender closes you down":
            if skill + confidence >= 5 or (position == "Striker" and skill >= 2):
                $ first_match_result = "goal"
                $ reputation += 3
                $ coach_opinion += 2
                $ confidence += 2
                $ fan_mood += 2
                narrator "You strike through the ball. It bends inside the post. Goal."
                coach "That is the kind of courage scouts remember."
            elif skill >= 2:
                $ first_match_result = "miss"
                $ coach_opinion -= 1
                $ pressure += 1
                narrator "The shot is powerful, but it misses. The choice was understandable, not optimal."
            else:
                $ first_match_result = "poor miss"
                $ reputation -= 1
                $ coach_opinion -= 2
                $ confidence -= 1
                $ pressure += 2
                narrator "You rush the shot. It flies wide, and the stadium noise suddenly feels heavier."

        "Hold possession and slow the game":
            if position == "Defender" or coach_opinion + teamwork >= 4:
                $ first_match_result = "controlled finish"
                $ coach_opinion += 2
                $ teamwork += 2
                narrator "You calm the match, draw a foul, and protect the result. It is not flashy, but it is mature."
            else:
                $ first_match_result = "lost chance"
                $ reputation -= 1
                $ confidence -= 1
                narrator "You wait too long. The defender presses, and the chance disappears."

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

    coach "Sit down, [player_name]. We need to review what happened."

    if coach_opinion >= 4:
        coach "You are progressing quickly. Your decisions are starting to match your ambition."
        $ reputation += 1
    elif coach_opinion >= 0:
        coach "There is potential, but your next step is consistency. You cannot make the user guess what you are becoming."
    else:
        coach "Your ability is not the issue. Your reliability is. You will earn your place again through better choices."
        $ reputation -= 1
        $ pressure += 1

    analyst "The dashboard helps players understand consequences without reading hidden code. That is important for usability."

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

    call screen chapter_card("Act IV: Transfer Window", "The prototype tests ambition against loyalty and difficulty.")

    show maya_chen at scout_right
    with dissolve

    scout "I represent Northbridge FC. We can put you in bigger matches quickly, but the competition will be harsh."
    coach "Or you can stay, build trust here, and grow with a staff that already knows your weaknesses."

    menu:
        "Choose your career path."

        "Accept the transfer to a bigger club":
            $ reputation += 2
            $ difficulty += 3
            $ loyalty -= 1
            $ pressure += 2
            scout "Brave. At Northbridge, every touch is evaluated."
            narrator "The route becomes glamorous but unforgiving."

        "Stay loyal and become a team leader":
            $ loyalty += 3
            $ coach_opinion += 2
            $ teamwork += 2
            coach "Loyalty matters. I will build the team around your growth."
            narrator "The route becomes steadier, with stronger relationships."

        "Negotiate a trial before deciding":
            $ reputation += 1
            $ difficulty += 1
            $ confidence += 1
            $ teamwork += 1
            scout "Smart. You want evidence before commitment."
            coach "That is a mature compromise."
            narrator "You keep options open, but now both clubs expect proof."

    $ add_note("The transfer decision demonstrates feasibility and practicality: different paths reuse the same system but change difficulty.")

    jump advanced_match

label advanced_match:
    scene bg match_stadium_night
    with dissolve

    call screen chapter_card("Act V: The Decisive Match", "The final challenge combines skill, confidence, teamwork, and pressure.")

    if difficulty >= 3:
        narrator "The bigger club is louder, faster, and less patient. The opponent presses like a machine."
    elif loyalty >= 3:
        narrator "Your teammates know your movement. They trust your first touch before you even receive the ball."
    else:
        narrator "The trial gives you opportunity, but also uncertainty. Everyone is watching."

    menu:
        "Choose the final match strategy."

        "Lead an aggressive attack":
            if skill + confidence + reputation - difficulty >= 7:
                $ advanced_match_result = "dominant win"
                $ reputation += 3
                $ confidence += 2
                $ fan_mood += 2
                narrator "You attack with timing, not panic. Your team wins, and your name is chanted after full-time."
            elif skill + confidence + reputation >= 7:
                $ advanced_match_result = "narrow win"
                $ reputation += 2
                $ pressure += 1
                narrator "It is messy, but your courage pays off. The team wins narrowly."
            else:
                $ advanced_match_result = "countered"
                $ reputation -= 1
                $ coach_opinion -= 1
                $ pressure += 2
                narrator "You force the attack too early. The opponent counters into the space behind you."

        "Play with tactical discipline":
            if coach_opinion + teamwork + loyalty + skill >= 8:
                $ advanced_match_result = "disciplined success"
                $ reputation += 2
                $ coach_opinion += 2
                $ teamwork += 1
                narrator "You organize the team, control dangerous spaces, and turn discipline into victory."
            elif position == "Defender" and skill >= 2:
                $ advanced_match_result = "solid draw"
                $ reputation += 1
                $ coach_opinion += 1
                narrator "You absorb pressure and earn a result. Not spectacular, but deeply useful."
            else:
                $ advanced_match_result = "too passive"
                $ reputation -= 1
                $ confidence -= 1
                narrator "You become too cautious. The opponent slowly takes control."

        "Trust the team and create for others":
            if teamwork + coach_opinion + confidence >= 7:
                $ advanced_match_result = "team triumph"
                $ reputation += 2
                $ teamwork += 2
                $ loyalty += 1
                narrator "You pull defenders out of position and create the winning chance. The team celebrates together."
            else:
                $ advanced_match_result = "miscommunication"
                $ pressure += 1
                $ reputation -= 1
                narrator "The idea is right, but the timing is not. A pass goes behind the runner at the worst moment."

    $ add_note("The final challenge combines several earlier variables, rewarding learnability and replay.")

    jump final_outcome

label final_outcome:
    scene bg career_outcome_celebration
    with fade

    hide screen career_hud

    narrator "The season ends. Your career file is reviewed by coaches, analysts, scouts, and teammates."

    $ final_score = skill + coach_opinion + confidence + reputation + loyalty + teamwork + fan_mood - difficulty - pressure

    if final_score >= 13:
        $ final_title = "Elite Professional Breakthrough"
        $ final_message = "Your decisions build skill, trust, confidence, and public reputation. You earn a professional contract and become the player young fans point to when they talk about discipline."
        $ add_note("Excellent ending shows strong output correctness: positive choices produce a believable reward.")
    elif final_score >= 7:
        $ final_title = "Professional Squad Player"
        $ final_message = "You earn a place in the professional environment. You are not yet a star, but your career is alive because your choices created enough trust and performance."
        $ add_note("Middle ending supports realistic outcomes instead of only win-or-lose feedback.")
    elif final_score >= 2:
        $ final_title = "Development Contract"
        $ final_message = "Your dream survives, but only barely. Coaches see potential, yet your pressure management and consistency still need work."
        $ add_note("Recovery remains possible, which supports good interaction design after user mistakes.")
    else:
        $ final_title = "Career Reset"
        $ final_message = "The season exposes poor preparation, weak relationships, or risky decisions. The dream is not erased, but the route must restart with better habits."
        $ add_note("Failed ending explains why the user failed instead of giving a vague result.")

    $ add_note("Future improvements: add sound, more character art, and a short questionnaire after playtesting.")
    $ add_note("Suggested evaluation: ask users to complete one successful career path and rate clarity, feedback, engagement, and ease of recovery.")

    narrator "[final_title]"
    narrator "[final_message]"

    jump end_screen_label

label end_screen_label:
    call screen project_end_screen(final_title, final_message, final_score)

    if _return == "replay":
        jump reset_story

    return
