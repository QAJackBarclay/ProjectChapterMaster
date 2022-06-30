from application import app
from flask import request
from random import choice

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
        1: "Unstable Psyker,
        2: "Corrupter Psyker",
    }
}


master = "Chapter Master"


@app.route('/get_rank')
def deployed():
    data_sent = request.get_json()
    the_rank = data_sent[obj]
    the_chapter = data_sent[source]
    if rank == 'scout':
        lname = random.choice(list(scout["names"].values()))
    elif rank == 'brother':
        lname = random.choice(list(brother["names"].values()))
    elif rank == 'captain':
        lname = random.choice(list(captain["names"].values()))
    elif rank == 'psyker':
        lname = random.choice(list(psyker["names"].values()))
    else rank == 'master':
        lname = master

return f"You are ${lname} of the ${chapter}, you have served them for ${service} years."