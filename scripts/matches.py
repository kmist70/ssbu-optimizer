import json

with open("data/matchups.json") as f:
    matchups = json.load(f)

# ── Pyra/Mythra ────────────────────────────────────────────────────────────────
matchups["Pyra/Mythra"] = {
    "Mario": 0.55, "Luigi": 0.55, "Donkey Kong": 0.6, "Link": 0.5,
    "Samus/Dark Samus": 0.5, "Yoshi": 0.55, "Kirby": 0.6,
    "Fox": 0.45, "Pikachu": 0.4, "Ness": 0.55, "Captain Falcon": 0.6,
    "Jigglypuff": 0.65, "Peach/Daisy": 0.45, "Bowser": 0.6,
    "Ice Climbers": 0.5, "Sheik": 0.45, "Zelda": 0.55, "Dr. Mario": 0.6,
    "Pichu": 0.45, "Falco": 0.5, "Marth": 0.5, "Lucina": 0.5,
    "Young Link": 0.5, "Ganondorf": 0.65, "Mewtwo": 0.55, "Roy": 0.5,
    "Chrom": 0.5, "Mr. Game \uff06 Watch": 0.5, "Meta Knight": 0.45,
    "Pit/Dark Pit": 0.55, "Zero Suit Samus": 0.45,
    "Wario": 0.55, "Snake": 0.45, "Ike": 0.55, "Pokemon Trainer": 0.55,
    "Diddy Kong": 0.45, "Lucas": 0.55, "Sonic": 0.4, "King Dedede": 0.65,
    "Olimar": 0.55, "Lucario": 0.5, "R.O.B.": 0.5, "Toon Link": 0.5,
    "Wolf": 0.5, "Villager": 0.5, "Mega Man": 0.45, "Wii Fit Trainer": 0.6,
    "Rosalina \uff06 Luma": 0.55, "Little Mac": 0.65, "Greninja": 0.45,
    "Mii Brawler": 0.55, "Mii Swordfighter": 0.5, "Mii Gunner": 0.5,
    "Palutena": 0.45, "Pac-Man": 0.5, "Robin": 0.55, "Shulk": 0.5,
    "Bowser Jr.": 0.6, "Duck Hunt": 0.5, "Ryu": 0.55, "Ken": 0.55,
    "Cloud": 0.5, "Corrin": 0.5, "Bayonetta": 0.6, "Inkling": 0.5,
    "Ridley": 0.6, "Simon/Richter": 0.5, "King K. Rool": 0.65,
    "Isabelle": 0.55, "Incineroar": 0.6, "Piranha Plant": 0.6,
    "Joker": 0.4, "Hero": 0.5, "Banjo \uff06 Kazooie": 0.55, "Terry": 0.5,
    "Byleth": 0.5, "Min Min": 0.4, "Steve": 0.45, "Sephiroth": 0.5,
    "Kazuya": 0.55, "Sora": 0.5
}

# ── Kazuya ─────────────────────────────────────────────────────────────────────
matchups["Kazuya"] = {
    "Mario": 0.5, "Luigi": 0.5, "Donkey Kong": 0.55, "Link": 0.4,
    "Samus/Dark Samus": 0.35, "Yoshi": 0.5, "Kirby": 0.55,
    "Fox": 0.45, "Pikachu": 0.45, "Ness": 0.5, "Captain Falcon": 0.55,
    "Jigglypuff": 0.6, "Peach/Daisy": 0.4, "Bowser": 0.5,
    "Ice Climbers": 0.55, "Sheik": 0.45, "Zelda": 0.55, "Dr. Mario": 0.55,
    "Pichu": 0.5, "Falco": 0.5, "Marth": 0.4, "Lucina": 0.4,
    "Young Link": 0.4, "Ganondorf": 0.65, "Mewtwo": 0.5, "Roy": 0.5,
    "Chrom": 0.45, "Mr. Game \uff06 Watch": 0.5, "Meta Knight": 0.45,
    "Pit/Dark Pit": 0.5, "Zero Suit Samus": 0.45,
    "Wario": 0.5, "Snake": 0.4, "Ike": 0.55, "Pokemon Trainer": 0.5,
    "Diddy Kong": 0.45, "Lucas": 0.5, "Sonic": 0.4, "King Dedede": 0.6,
    "Olimar": 0.45, "Lucario": 0.5, "R.O.B.": 0.4, "Toon Link": 0.4,
    "Wolf": 0.5, "Villager": 0.35, "Mega Man": 0.35, "Wii Fit Trainer": 0.55,
    "Rosalina \uff06 Luma": 0.45, "Little Mac": 0.6, "Greninja": 0.45,
    "Mii Brawler": 0.55, "Mii Swordfighter": 0.45, "Mii Gunner": 0.4,
    "Palutena": 0.45, "Pac-Man": 0.45, "Robin": 0.5, "Shulk": 0.4,
    "Bowser Jr.": 0.55, "Duck Hunt": 0.4, "Ryu": 0.5, "Ken": 0.5,
    "Cloud": 0.45, "Corrin": 0.45, "Bayonetta": 0.55, "Inkling": 0.5,
    "Ridley": 0.55, "Simon/Richter": 0.35, "King K. Rool": 0.6,
    "Isabelle": 0.4, "Incineroar": 0.55, "Piranha Plant": 0.5,
    "Joker": 0.45, "Hero": 0.5, "Banjo \uff06 Kazooie": 0.5, "Terry": 0.5,
    "Byleth": 0.45, "Min Min": 0.3, "Steve": 0.45, "Sephiroth": 0.4,
    "Pyra/Mythra": 0.45, "Sora": 0.5
}

# ── Sora ───────────────────────────────────────────────────────────────────────
matchups["Sora"] = {
    "Mario": 0.5, "Luigi": 0.5, "Donkey Kong": 0.6, "Link": 0.5,
    "Samus/Dark Samus": 0.5, "Yoshi": 0.55, "Kirby": 0.6,
    "Fox": 0.45, "Pikachu": 0.4, "Ness": 0.55, "Captain Falcon": 0.55,
    "Jigglypuff": 0.6, "Peach/Daisy": 0.5, "Bowser": 0.6,
    "Ice Climbers": 0.5, "Sheik": 0.45, "Zelda": 0.55, "Dr. Mario": 0.55,
    "Pichu": 0.45, "Falco": 0.5, "Marth": 0.5, "Lucina": 0.5,
    "Young Link": 0.5, "Ganondorf": 0.65, "Mewtwo": 0.55, "Roy": 0.5,
    "Chrom": 0.5, "Mr. Game \uff06 Watch": 0.5, "Meta Knight": 0.5,
    "Pit/Dark Pit": 0.55, "Zero Suit Samus": 0.45,
    "Wario": 0.55, "Snake": 0.5, "Ike": 0.55, "Pokemon Trainer": 0.55,
    "Diddy Kong": 0.45, "Lucas": 0.55, "Sonic": 0.4, "King Dedede": 0.65,
    "Olimar": 0.55, "Lucario": 0.5, "R.O.B.": 0.5, "Toon Link": 0.5,
    "Wolf": 0.5, "Villager": 0.5, "Mega Man": 0.5, "Wii Fit Trainer": 0.6,
    "Rosalina \uff06 Luma": 0.5, "Little Mac": 0.65, "Greninja": 0.45,
    "Mii Brawler": 0.55, "Mii Swordfighter": 0.5, "Mii Gunner": 0.5,
    "Palutena": 0.5, "Pac-Man": 0.5, "Robin": 0.55, "Shulk": 0.5,
    "Bowser Jr.": 0.6, "Duck Hunt": 0.5, "Ryu": 0.5, "Ken": 0.5,
    "Cloud": 0.5, "Corrin": 0.5, "Bayonetta": 0.55, "Inkling": 0.5,
    "Ridley": 0.6, "Simon/Richter": 0.5, "King K. Rool": 0.65,
    "Isabelle": 0.55, "Incineroar": 0.6, "Piranha Plant": 0.6,
    "Joker": 0.45, "Hero": 0.5, "Banjo \uff06 Kazooie": 0.55, "Terry": 0.5,
    "Byleth": 0.5, "Min Min": 0.45, "Steve": 0.5, "Sephiroth": 0.5,
    "Pyra/Mythra": 0.5, "Kazuya": 0.5
}

# ── Reverse entries ────────────────────────────────────────────────────────────
new_chars = ["Pyra/Mythra", "Kazuya", "Sora"]
for char in list(matchups.keys()):
    if char in new_chars:
        continue
    for new_char in new_chars:
        if new_char in matchups and char in matchups[new_char]:
            score = matchups[new_char][char]
            reverse = round(1.0 - score, 2)
            matchups[char][new_char] = reverse

with open("data/matchups.json", "w") as f:
    json.dump(matchups, f, indent=2)

print("Done.")