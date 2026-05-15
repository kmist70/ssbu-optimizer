import os
import streamlit as st
import json
import pandas as pd
import altair as alt
from PIL import Image

# ── Page config ────────────────────────────────────────────────────────────────
icon_path = os.path.join(os.path.dirname(__file__), "media", "ssbu-icon.png")
favicon = Image.open(icon_path) if os.path.exists(icon_path) else "🎮"
st.set_page_config(page_title="SSBU Optimizer", page_icon=favicon, layout="wide")

# ── Progress Tracking ──────────────────────────────────────────────────────────
PROGRESS_FILE = "data/progress.json"

def load_progress():
    if os.path.exists(PROGRESS_FILE):
        try:
            with open(PROGRESS_FILE, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    return []

def save_progress():
    with open(PROGRESS_FILE, "w") as f:
        json.dump(st.session_state.progress, f)

if "progress" not in st.session_state:
    st.session_state.progress = load_progress()

def toggle_skill(key):
    if st.session_state[key]:
        if key not in st.session_state.progress:
            st.session_state.progress.append(key)
    else:
        if key in st.session_state.progress:
            st.session_state.progress.remove(key)
    save_progress()

# ── Load data ──────────────────────────────────────────────────────────────────
with open("data/matchups.json") as f:
    matchups = json.load(f)

with open("data/characters.json") as f:
    char_data = json.load(f)

def get_difficulty_badge(difficulty):
    colors = {
        "Beginner": "#28a745",      # Green
        "Intermediate": "#dc3545",  # Red
        "Advanced": "#6f42c1",      # Purple
    }
    bg_color = colors.get(difficulty, "#6c757d")
    return f'<span style="background-color: {bg_color}; color: white; padding: 2px 8px; border-radius: 12px; font-size: 0.85em; font-weight: 600;">{difficulty}</span>'

def get_tier_badge(tier):
    colors = {
        "S": "#dc3545", # Red
        "A": "#fd7e14", # Orange
        "B": "#ffc107", # Yellow
        "C": "#28a745", # Green
        "D": "#007bff", # Blue
        "E": "#6f42c1"  # Purple
    }
    bg_color = colors.get(tier, "#6c757d")
    text_color = "black" if tier == "B" else "white" # Keeps yellow readable
    return f'<span style="background-color: {bg_color}; color: {text_color}; padding: 2px 8px; border-radius: 12px; font-size: 0.85em; font-weight: 600;">{tier}</span>'

def get_playstyle_badge(playstyle):
    colors = {
        "Rushdown": "#dc3545",  # Red
        "Zoner": "#007bff",     # Blue
        "Grappler": "#fd7e14",  # Orange
        "Balanced": "#28a745"   # Green
    }
    bg_color = colors.get(playstyle, "#6c757d")
    return f'<span style="background-color: {bg_color}; color: white; padding: 2px 8px; border-radius: 12px; font-size: 0.85em; font-weight: 600;">{playstyle}</span>'

def get_result_badge(score):
    if score >= 0.6:
        bg_color, text_color, text = "#28a745", "white", "Advantage"
    elif score <= 0.4:
        bg_color, text_color, text = "#dc3545", "white", "Disadvantage"
    else:
        bg_color, text_color, text = "#ffc107", "black", "Even"
    return f'<span style="background-color: {bg_color}; color: {text_color}; padding: 2px 8px; border-radius: 12px; font-size: 0.85em; font-weight: 600;">{text}</span>'

t_col1, t_col2 = st.columns([1, 14])
with t_col1:
    if isinstance(favicon, str):
        st.title(favicon)
    else:
        st.image(favicon, width=160)
with t_col2:
    st.title("Super Smash Bros. Ultimate Optimizer")
st.caption("Matchup data sourced from pro player matchup charts. Learning paths based on competitive guides.")

# ── Sidebar Navigation ─────────────────────────────────────────────────────────
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["⚔️ Matchup Analyzer", "📚 Learning Path", "🎖️ Tier List"])

st.sidebar.divider()
st.sidebar.markdown(
    "**About this app:**\n\n"
    "A comprehensive tool for Super Smash Bros. Ultimate players to analyze character matchups and follow structured learning paths from beginner to pro."
)


# ══════════════════════════════════════════════════════════════════════════════
# PAGE 1 — MATCHUP ANALYZER
# ══════════════════════════════════════════════════════════════════════════════
if page == "⚔️ Matchup Analyzer":
    st.header("Character Matchup Analyzer")
    st.markdown("Scores range from **0.0** (hard loss) to **1.0** (dominant win). **0.5 = even**.")

    characters = sorted(matchups.keys())

    # ── Filter row ─────────────────────────────────────────────────────────────
    f1, f2, f3 = st.columns(3)

    difficulty_options = ["-", "Beginner", "Intermediate", "Advanced"]
    playstyle_options  = ["-", "Zoner", "Rushdown", "Grappler", "Balanced"]
    tier_options       = ["-", "S", "A", "B", "C", "D", "E"]

    with f1:
        diff_filter = st.selectbox("Filter by Difficulty:", difficulty_options)
    with f2:
        style_filter = st.selectbox("Filter by Playstyle:", playstyle_options)
    with f3:
        tier_filter = st.selectbox("Filter by Tier:", tier_options)

    # ── Apply filters ──────────────────────────────────────────────────────────
    def passes_filter(char):
        info = char_data.get(char, {})
        if diff_filter != "-" and info.get("difficulty", "").lower() != diff_filter.lower():
            return False
        if style_filter != "-" and info.get("playstyle", "").lower() != style_filter.lower():
            return False
        if tier_filter != "-" and info.get("tier", "").upper() != tier_filter.upper():
            return False
        return True

    filtered_characters = [c for c in characters if passes_filter(c)]

    if not filtered_characters:
        st.warning("No characters match the selected filters. Try removing a filter.")
        selected = "-"
    else:
        char_options = ["-"] + filtered_characters
        selected = st.selectbox("Select your character:", char_options, key="matchup_char")

    if selected == "-":
        st.info("Select a character above to view their matchup data.")
    else:
        # ── Character portrait ─────────────────────────────────────────────────
        portrait_path = f"media/character-portraits/{selected}.png"
        fallback_path = f"media/character-portraits/{selected}.jpg"
        pyra_path = f"media/character-portraits/Pyra.png"

        port_col, info_col = st.columns([1, 4])
        with port_col:
            if os.path.exists(portrait_path):
                st.image(portrait_path, width=250)
            elif os.path.exists(fallback_path):
                st.image(fallback_path, width=250)
            elif selected == "Pyra/Mythra" and os.path.exists(pyra_path):
                st.image(pyra_path, width=250)
            else:
                st.markdown("🎮")

        with info_col:
            info = char_data.get(selected, {})
            st.markdown(f"### {selected}")
            if info.get("difficulty"):
                badge = get_difficulty_badge(info['difficulty'])
                st.markdown(f"**Difficulty:** {badge}", unsafe_allow_html=True)
            if info.get("tier"):
                t_badge = get_tier_badge(info['tier'])
                st.markdown(f"**Tier:** {t_badge}", unsafe_allow_html=True)
            if info.get("playstyle"):
                p_badge = get_playstyle_badge(info['playstyle'])
                st.markdown(f"**Playstyle:** {p_badge}", unsafe_allow_html=True)
            if info.get("overview"):
                st.caption(info["overview"])

        st.divider()

        # ── Matchup data ───────────────────────────────────────────────────────
        data = matchups[selected]
        df = pd.DataFrame(list(data.items()), columns=["Opponent", "Score"])

        def label(score):
            if score >= 0.6:
                return "Advantage"
            elif score <= 0.4:
                return "Disadvantage"
            else:
                return "Even"

        def color_score(val):
            if val >= 0.6:
                return 'background-color: rgba(40, 167, 69, 0.2)'  # Green
            elif val <= 0.4:
                return 'background-color: rgba(220, 53, 69, 0.2)'  # Red
            else:
                return 'background-color: rgba(255, 193, 7, 0.2)'  # Yellow

        df["Result"] = df["Score"].apply(label)
        df = df.sort_values("Score", ascending=False)

        adv  = len(df[df["Score"] >= 0.6])
        even = len(df[(df["Score"] > 0.4) & (df["Score"] < 0.6)])
        dis  = len(df[df["Score"] <= 0.4])

        m1, m2, m3 = st.columns(3)
        m1.metric("Advantages", adv)
        m2.metric("Even", even)
        m3.metric("Disadvantages", dis)

        st.divider()

        col1, col2, col3 = st.columns(3)

        with col1:
            st.subheader("✅ Advantages")
            adv_df = df[df["Score"] >= 0.6][["Opponent", "Score"]].reset_index(drop=True)
            if adv_df.empty:
                st.info("No advantages in this dataset.")
            else:
                st.dataframe(adv_df.style.map(color_score, subset=["Score"]), use_container_width=True, hide_index=True)

        with col2:
            st.subheader("➖ Even")
            even_df = df[(df["Score"] > 0.4) & (df["Score"] < 0.6)][["Opponent", "Score"]].reset_index(drop=True)
            if even_df.empty:
                st.info("No even matchups in this dataset.")
            else:
                st.dataframe(even_df.style.map(color_score, subset=["Score"]), use_container_width=True, hide_index=True)

        with col3:
            st.subheader("❌ Disadvantages")
            dis_df = df[df["Score"] <= 0.4][["Opponent", "Score"]].reset_index(drop=True)
            if dis_df.empty:
                st.info("No disadvantages in this dataset.")
            else:
                st.dataframe(dis_df.style.map(color_score, subset=["Score"]), use_container_width=True, hide_index=True)

        st.divider()

        st.subheader(f"{selected}'s Full Matchup Chart")
        
        color_scale = alt.Scale(
            domain=["Advantage", "Even", "Disadvantage"],
            range=["#28a745", "#ffc107", "#dc3545"]
        )
        chart = alt.Chart(df).mark_bar().encode(
            x=alt.X("Opponent:N", sort="ascending"),
            y=alt.Y("Score:Q"),
            color=alt.Color("Result:N", scale=color_scale),
            tooltip=["Opponent", "Score", "Result"]
        )
        st.altair_chart(chart, use_container_width=True)

        st.divider()
        st.subheader("🔍 Head-to-Head")
        opponent = st.selectbox("Pick an opponent to check:", [c for c in characters if c != selected], key="h2h")
        if opponent and opponent in data:
            score = data[opponent]
            badge = get_result_badge(score)
            st.markdown(f"**{selected}** vs **{opponent}**: Score `{score}` → {badge}", unsafe_allow_html=True)
        else:
            st.info("Matchup data for this pairing not available yet.")


# ══════════════════════════════════════════════════════════════════════════════
# PAGE 2 — LEARNING PATH
# ══════════════════════════════════════════════════════════════════════════════
elif page == "📚 Learning Path":
    st.header("Character Learning Path")
    st.markdown("Structured skill progression from zero to competitive. Complete stages in order.")

    char_list = ["-"] + sorted(char_data.keys())
    char_pick = st.selectbox("Choose a character:", char_list, key="learn_char")

    if char_pick == "-":
        st.info("Select a character above to view their learning path.")
    elif char_pick in char_data:
        info = char_data[char_pick]

        badge = get_difficulty_badge(info['difficulty'])
        st.markdown(f"**Difficulty:** {badge}", unsafe_allow_html=True)
        st.markdown(f"**Overview:** {info['overview']}")
        st.divider()

        all_skills = [skill for stage in info["path"] for skill in stage["skills"]]
        total = len(all_skills)
        completed = []

        for i, stage in enumerate(info["path"]):
            stage_label = f"Stage {i + 1}: {stage['stage']}"
            with st.expander(stage_label, expanded=(i == 0)):
                for skill in stage["skills"]:
                    key = f"{char_pick}_{stage['stage']}_{skill}"
                    if key not in st.session_state:
                        st.session_state[key] = key in st.session_state.progress
                    checked = st.checkbox(skill, key=key, on_change=toggle_skill, args=(key,))
                    if checked:
                        completed.append(skill)

        st.divider()
        st.subheader("Your Progress")
        pct = len(completed) / total if total > 0 else 0
        st.progress(pct)
        st.caption(f"{len(completed)} / {total} skills completed ({int(pct * 100)}%)")

        if pct == 1.0:
            st.success("You've completed all stages. You're playing at a pro level with this character.")
        elif pct >= 0.75:
            st.info("Almost there — you're in advanced territory.")
        elif pct >= 0.5:
            st.info("Good progress — pushing into advanced skills.")
        elif pct >= 0.25:
            st.info("Intermediate stage — keep building.")
        else:
            st.info("Just getting started. Work through Stage 1 first.")

    else:
        st.warning("No learning path data found for this character. Add them to characters.json.")


# ══════════════════════════════════════════════════════════════════════════════
# PAGE 3 — TIER LIST
# ══════════════════════════════════════════════════════════════════════════════
elif page == "🎖️ Tier List":
    st.header("Official SSBU Tier List (4th Edition)")
    img = Image.open("media/ssbu-tier-list.png")
    st.image(img, caption="Source: Ultrank (https://medium.com/@ultrankssb/the-fourth-ultrank-tier-list-2026-9c5f6964f7e3)", width=1100)