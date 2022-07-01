from application import app
from flask import request, Response
import random

scout = {
    "names": {
        0: "Sniper",
        1: "Tunnel Rat",
        2: "Neophyte",
        3: "Scout",
    }
}


brother = {
    "names": {
        0: "Devastator",
        1: "Assault Marine",
        2: "Relic Guard",
        3: "Primaris",
        4: "Battle Brother"
    }
}


captain = {
    "names": {
        0: "Primaris Captain",
        1: "Sword Brethren",
        2: "Squad Leader",
        3: "Veteran hero",
    }
}

psyker = {
    "names": {
        0: "Stable Psyker",
        1: "Unstable Psyker",
        2: "Corrupter Psyker",
    }
}


master = "Chapter Master"


@app.route('/get_rank')
def lname():
    rank = ["scout", "brother", "captain", "psyker", "master"]
    selection = random.choice(rank)
    if selection == 'scout':
        lname = random.choice(list(scout["names"].values()))
    elif selection == 'brother':
        lname = random.choice(list(brother["names"].values()))
    elif selection == 'captain':
        lname = random.choice(list(captain["names"].values()))
    elif selection == 'psyker':
        lname = random.choice(list(psyker["names"].values()))
    elif selection == 'master':
        lname = 'Chapter Master'

    return Response(selection, mimetype='text/plain')