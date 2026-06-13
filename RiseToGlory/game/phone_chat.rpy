default phone_chat_messages = []

init python:
    def phone_chat_reset():
        store.phone_chat_messages = []

    def phone_chat_add(sender, message):
        store.phone_chat_messages = store.phone_chat_messages + [(sender, message)]
        renpy.restart_interaction()


transform phone_chat_backdrop:
    on show:
        alpha 0.0
        linear 0.30 alpha 1.0
    on hide:
        linear 0.25 alpha 0.0


transform phone_chat_phone_motion:
    on show:
        xoffset 180
        yoffset 24
        zoom 0.94
        alpha 0.0
        parallel:
            easeout_cubic 0.55 xoffset 0 yoffset 0
        parallel:
            easeout_cubic 0.55 zoom 1.0
        parallel:
            linear 0.22 alpha 1.0
    on hide:
        parallel:
            easein_cubic 0.30 xoffset 140 yoffset 18
        parallel:
            easein_cubic 0.30 zoom 0.97
        parallel:
            linear 0.20 alpha 0.0


transform phone_chat_message_motion(sender):
    alpha 0.0
    xoffset (42 if sender == "me" else -42)
    yoffset 14
    zoom 0.97
    parallel:
        easeout_cubic 0.34 xoffset 0 yoffset 0
    parallel:
        easeout_cubic 0.34 zoom 1.0
    parallel:
        linear 0.18 alpha 1.0


screen phone_chat(contact_name, status="online"):
    zorder 90

    add Solid("#02060888") at phone_chat_backdrop

    fixed at phone_chat_phone_motion:
        xalign 0.84
        yalign 0.5
        xsize 780
        ysize 967

        add "gui/phone_chat/phone_background_2.png":
            xsize 780
            ysize 967

        viewport:
            xpos 48
            ypos 170
            xsize 684
            ysize 640
            mousewheel True
            draggable True
            yinitial 1.0

            vbox:
                xfill True
                spacing 14

                null height 18

                for message_id, (sender, message) in enumerate(phone_chat_messages):
                    fixed at phone_chat_message_motion(sender):
                        id "phone_chat_message_[message_id]"
                        xfill True
                        yfit True

                        frame:
                            background Solid("#d8aeb7ee" if sender == "me" else "#ffffffee")
                            xalign (1.0 if sender == "me" else 0.0)
                            xmaximum 520
                            padding (20, 15)

                            text message:
                                size 25
                                color "#4a3d40"

                null height 18

        add "gui/phone_chat/phone_foreground.png":
            xsize 780
            ysize 967

        add "gui/phone_chat/avatar_unknown.png":
            xpos 300
            ypos 72
            xsize 62
            ysize 62

        vbox:
            xpos 375
            ypos 76
            spacing 0

            text contact_name size 28 bold True color "#4a3d40"
            text status size 17 color "#a89297"

        text "Tap to continue":
            xpos 260
            ypos 892
            size 19
            color "#b7a5a9"


# Example:
# $ phone_chat_reset()
# show screen phone_chat("Afiq")
# $ phone_chat_add("them", "Incoming message.")
# pause
# $ phone_chat_add("me", "Your reply.")
# pause
# hide screen phone_chat
