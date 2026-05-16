import json

with open("data/characters.json") as f:
    chars = json.load(f)

stats = {
    "Mario":             {"speed": 6, "kill_power": 5, "range": 4, "recovery": 5, "difficulty": 4},
    "Luigi":             {"speed": 5, "kill_power": 9, "range": 4, "recovery": 4, "difficulty": 6},
    "Donkey Kong":       {"speed": 7, "kill_power": 8, "range": 5, "recovery": 4, "difficulty": 3},
    "Link":              {"speed": 4, "kill_power": 7, "range": 8, "recovery": 5, "difficulty": 5},
    "Samus/Dark Samus":  {"speed": 4, "kill_power": 6, "range": 8, "recovery": 6, "difficulty": 5},
    "Yoshi":             {"speed": 7, "kill_power": 6, "range": 5, "recovery": 7, "difficulty": 4},
    "Kirby":             {"speed": 6, "kill_power": 5, "range": 3, "recovery": 8, "difficulty": 2},
    "Fox":               {"speed": 9, "kill_power": 7, "range": 4, "recovery": 4, "difficulty": 7},
    "Pikachu":           {"speed": 7, "kill_power": 5, "range": 5, "recovery": 8, "difficulty": 6},
    "Ness":              {"speed": 4, "kill_power": 7, "range": 6, "recovery": 4, "difficulty": 5},
    "Captain Falcon":    {"speed": 10, "kill_power": 8, "range": 4, "recovery": 4, "difficulty": 5},
    "Jigglypuff":        {"speed": 4, "kill_power": 9, "range": 3, "recovery": 7, "difficulty": 7},
    "Peach/Daisy":       {"speed": 4, "kill_power": 7, "range": 6, "recovery": 7, "difficulty": 8},
    "Bowser":            {"speed": 7, "kill_power": 9, "range": 5, "recovery": 5, "difficulty": 2},
    "Ice Climbers":      {"speed": 4, "kill_power": 10, "range": 5, "recovery": 3, "difficulty": 9},
    "Sheik":             {"speed": 9, "kill_power": 6, "range": 4, "recovery": 6, "difficulty": 8},
    "Zelda":             {"speed": 3, "kill_power": 8, "range": 6, "recovery": 5, "difficulty": 5},
    "Dr. Mario":         {"speed": 6, "kill_power": 7, "range": 4, "recovery": 3, "difficulty": 4},
    "Pichu":             {"speed": 7, "kill_power": 5, "range": 3, "recovery": 6, "difficulty": 6},
    "Falco":             {"speed": 5, "kill_power": 6, "range": 5, "recovery": 3, "difficulty": 6},
    "Marth":             {"speed": 7, "kill_power": 7, "range": 7, "recovery": 5, "difficulty": 6},
    "Lucina":            {"speed": 7, "kill_power": 7, "range": 7, "recovery": 5, "difficulty": 5},
    "Young Link":        {"speed": 6, "kill_power": 5, "range": 7, "recovery": 6, "difficulty": 5},
    "Ganondorf":         {"speed": 2, "kill_power": 10, "range": 5, "recovery": 3, "difficulty": 3},
    "Mewtwo":            {"speed": 8, "kill_power": 7, "range": 6, "recovery": 6, "difficulty": 6},
    "Roy":               {"speed": 8, "kill_power": 8, "range": 6, "recovery": 4, "difficulty": 5},
    "Chrom":             {"speed": 8, "kill_power": 8, "range": 6, "recovery": 3, "difficulty": 4},
    "Mr. Game \uff06 Watch": {"speed": 5, "kill_power": 7, "range": 5, "recovery": 6, "difficulty": 6},
    "Meta Knight":       {"speed": 8, "kill_power": 6, "range": 5, "recovery": 9, "difficulty": 7},
    "Pit/Dark Pit":      {"speed": 6, "kill_power": 5, "range": 5, "recovery": 9, "difficulty": 4},
    "Zero Suit Samus":   {"speed": 9, "kill_power": 6, "range": 5, "recovery": 7, "difficulty": 7},
    "Wario":             {"speed": 5, "kill_power": 9, "range": 4, "recovery": 7, "difficulty": 5},
    "Snake":             {"speed": 4, "kill_power": 7, "range": 8, "recovery": 5, "difficulty": 8},
    "Ike":               {"speed": 3, "kill_power": 9, "range": 6, "recovery": 4, "difficulty": 4},
    "Pokemon Trainer":   {"speed": 6, "kill_power": 6, "range": 6, "recovery": 6, "difficulty": 7},
    "Diddy Kong":        {"speed": 7, "kill_power": 6, "range": 5, "recovery": 6, "difficulty": 7},
    "Lucas":             {"speed": 5, "kill_power": 7, "range": 6, "recovery": 5, "difficulty": 6},
    "Sonic":             {"speed": 10, "kill_power": 5, "range": 3, "recovery": 7, "difficulty": 8},
    "King Dedede":       {"speed": 3, "kill_power": 7, "range": 5, "recovery": 8, "difficulty": 3},
    "Olimar":            {"speed": 4, "kill_power": 6, "range": 5, "recovery": 5, "difficulty": 9},
    "Lucario":           {"speed": 5, "kill_power": 8, "range": 5, "recovery": 6, "difficulty": 6},
    "R.O.B.":            {"speed": 6, "kill_power": 7, "range": 7, "recovery": 8, "difficulty": 6},
    "Toon Link":         {"speed": 6, "kill_power": 5, "range": 7, "recovery": 6, "difficulty": 5},
    "Wolf":              {"speed": 4, "kill_power": 8, "range": 6, "recovery": 5, "difficulty": 5},
    "Villager":          {"speed": 3, "kill_power": 6, "range": 7, "recovery": 7, "difficulty": 6},
    "Mega Man":          {"speed": 4, "kill_power": 5, "range": 8, "recovery": 5, "difficulty": 6},
    "Wii Fit Trainer":   {"speed": 6, "kill_power": 6, "range": 5, "recovery": 6, "difficulty": 6},
    "Rosalina \uff06 Luma":  {"speed": 6, "kill_power": 7, "range": 6, "recovery": 6, "difficulty": 7},
    "Little Mac":        {"speed": 9, "kill_power": 9, "range": 3, "recovery": 1, "difficulty": 5},
    "Greninja":          {"speed": 8, "kill_power": 7, "range": 5, "recovery": 7, "difficulty": 7},
    "Mii Brawler":       {"speed": 7, "kill_power": 7, "range": 3, "recovery": 5, "difficulty": 5},
    "Mii Swordfighter":  {"speed": 5, "kill_power": 6, "range": 6, "recovery": 6, "difficulty": 5},
    "Mii Gunner":        {"speed": 3, "kill_power": 5, "range": 8, "recovery": 5, "difficulty": 5},
    "Palutena":          {"speed": 7, "kill_power": 6, "range": 5, "recovery": 7, "difficulty": 6},
    "Pac-Man":           {"speed": 5, "kill_power": 5, "range": 7, "recovery": 7, "difficulty": 7},
    "Robin":             {"speed": 2, "kill_power": 7, "range": 7, "recovery": 4, "difficulty": 7},
    "Shulk":             {"speed": 5, "kill_power": 8, "range": 7, "recovery": 6, "difficulty": 8},
    "Bowser Jr.":        {"speed": 4, "kill_power": 6, "range": 5, "recovery": 6, "difficulty": 5},
    "Duck Hunt":         {"speed": 5, "kill_power": 4, "range": 7, "recovery": 5, "difficulty": 7},
    "Ryu":               {"speed": 4, "kill_power": 8, "range": 4, "recovery": 4, "difficulty": 8},
    "Ken":               {"speed": 6, "kill_power": 10, "range": 4, "recovery": 4, "difficulty": 8},
    "Cloud":             {"speed": 7, "kill_power": 8, "range": 7, "recovery": 4, "difficulty": 5},
    "Corrin":            {"speed": 4, "kill_power": 7, "range": 8, "recovery": 5, "difficulty": 6},
    "Bayonetta":         {"speed": 6, "kill_power": 5, "range": 5, "recovery": 7, "difficulty": 9},
    "Inkling":           {"speed": 6, "kill_power": 6, "range": 6, "recovery": 5, "difficulty": 6},
    "Ridley":            {"speed": 8, "kill_power": 8, "range": 6, "recovery": 6, "difficulty": 6},
    "Simon/Richter":     {"speed": 4, "kill_power": 6, "range": 9, "recovery": 3, "difficulty": 5},
    "King K. Rool":      {"speed": 3, "kill_power": 9, "range": 6, "recovery": 5, "difficulty": 4},
    "Isabelle":          {"speed": 3, "kill_power": 5, "range": 7, "recovery": 7, "difficulty": 6},
    "Incineroar":        {"speed": 2, "kill_power": 9, "range": 5, "recovery": 3, "difficulty": 5},
    "Piranha Plant":     {"speed": 5, "kill_power": 7, "range": 6, "recovery": 6, "difficulty": 4},
    "Joker":             {"speed": 7, "kill_power": 7, "range": 5, "recovery": 7, "difficulty": 7},
    "Hero":              {"speed": 6, "kill_power": 8, "range": 6, "recovery": 6, "difficulty": 8},
    "Banjo \uff06 Kazooie":  {"speed": 8, "kill_power": 6, "range": 6, "recovery": 6, "difficulty": 5},
    "Terry":             {"speed": 5, "kill_power": 8, "range": 5, "recovery": 4, "difficulty": 7},
    "Byleth":            {"speed": 3, "kill_power": 8, "range": 9, "recovery": 5, "difficulty": 6},
    "Min Min":           {"speed": 4, "kill_power": 7, "range": 10, "recovery": 5, "difficulty": 7},
    "Steve":             {"speed": 3, "kill_power": 7, "range": 5, "recovery": 5, "difficulty": 8},
    "Sephiroth":         {"speed": 6, "kill_power": 8, "range": 9, "recovery": 6, "difficulty": 6},
    "Pyra/Mythra":       {"speed": 7, "kill_power": 7, "range": 7, "recovery": 6, "difficulty": 7},
    "Kazuya":            {"speed": 4, "kill_power": 10, "range": 4, "recovery": 4, "difficulty": 10},
    "Sora":              {"speed": 5, "kill_power": 6, "range": 6, "recovery": 8, "difficulty": 6},
}

injected = 0
skipped = []
for char, s in stats.items():
    if char in chars:
        chars[char]["stats"] = s
        injected += 1
    else:
        skipped.append(char)

with open("data/characters.json", "w") as f:
    json.dump(chars, f, indent=2)

print(f"Injected: {injected}")
if skipped:
    print(f"Skipped (key not found): {skipped}")
else:
    print("No skips — all keys matched.")