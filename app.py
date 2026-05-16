import os
import streamlit as st
import json
import base64
import pandas as pd
import altair as alt
from PIL import Image
import plotly.graph_objects as go

# ── Page config ────────────────────────────────────────────────────────────────
icon_path = os.path.join(os.path.dirname(__file__), "media", "ssbu-icon.png")
favicon = Image.open(icon_path) if os.path.exists(icon_path) else "🎮"
st.set_page_config(page_title="SSBU Optimizer", page_icon=favicon, layout="wide", initial_sidebar_state="expanded")

# Hide the sidebar collapse/expand buttons so the navigation is always visible
st.markdown(
    """
    <style>
        [data-testid="collapsedControl"] {display: none;}
        [data-testid="stSidebarCollapseButton"] {display: none;}
            
            /* Move sidebar content closer to the top and centered */
            [data-testid="stSidebarUserContent"] {
                padding-top: 0rem !important;
                padding-left: 1rem !important;
                padding-right: 1rem !important;
                overflow-y: hidden !important;
            }
            
            /* Remove scrolling capability from the sidebar container */
            [data-testid="stSidebar"] > div:first-child {
                overflow-y: hidden !important;
            }
            
            /* Make sidebar navigation tabs larger and full-width */
            [data-testid="stSidebar"] [data-testid="stRadio"] label[data-baseweb="radio"] {
                width: 100% !important;
                padding: 12px 16px;
                background-color: rgba(228, 128, 128, 0.2);
                border-radius: 8px;
                margin-bottom: 6px;
                cursor: pointer;
            }
            [data-testid="stSidebar"] [data-testid="stRadio"] label[data-baseweb="radio"]:hover {
                background-color: rgba(128, 128, 128, 0.2);
            }
    </style>
    """,
    unsafe_allow_html=True,
)

# ── Progress Tracking ──────────────────────────────────────────────────────────
PROGRESS_FILE = "data/progress.json"
ROSTER_FILE = "data/roster.json"

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

def load_roster():
    if os.path.exists(ROSTER_FILE):
        try:
            with open(ROSTER_FILE, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return {}
    return {}

def save_roster():
    with open(ROSTER_FILE, "w") as f:
        json.dump(st.session_state.roster, f)

if "progress" not in st.session_state:
    st.session_state.progress = load_progress()

if "roster" not in st.session_state:
    st.session_state.roster = load_roster()

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

if os.path.exists(icon_path):
    with open(icon_path, "rb") as f:
        icon_b64 = base64.b64encode(f.read()).decode()
    st.markdown(
        f"""
        <div style="display: flex; align-items: center; gap: 15px;">
            <img src="data:image/png;base64,{icon_b64}" style="width: 160px; flex-shrink: 0;" />
            <h1 style="margin: 0;">Super Smash Bros. Ultimate Optimizer</h1>
        </div>
        """,
        unsafe_allow_html=True
    )
else:
    st.markdown(
        """
        <div style="display: flex; align-items: center; gap: 15px;">
            <h1 style="margin: 0;">🎮</h1>
            <h1 style="margin: 0;">Super Smash Bros. Ultimate Optimizer</h1>
        </div>
        """,
        unsafe_allow_html=True
    )
st.caption("Matchup data sourced from pro player matchup charts. Learning paths based on competitive guides.")

# ── Sidebar Navigation ─────────────────────────────────────────────────────────
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["⚔️ Matchup Analyzer", "🛡️ Counterpicker", "📚 Learning Path", "📊 Overall Stats", "🎖️ Tier List", "👤 My Roster", "📈 My Progress"], label_visibility="collapsed")

# Add a spacer to push the "About this app" section to the bottom
st.sidebar.markdown("<div style='min-height: 12vh;'></div>", unsafe_allow_html=True)
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

    with st.container(border=True):
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
        with st.container(border=True):
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

        with st.container(border=True):
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

        with st.container(border=True):
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

        with st.container(border=True):
            st.subheader("🔍 Head-to-Head")
            opponent = st.selectbox("Pick an opponent to check:", ["-"] + [c for c in characters if c != selected], key="h2h")
            if opponent == "-":
                st.info("Select an opponent to view the head-to-head matchup.")
            elif opponent and opponent in data:
                score = data[opponent]
                badge = get_result_badge(score)
                st.markdown(f"**{selected}** vs **{opponent}**: Score `{score}` → {badge}", unsafe_allow_html=True)
            else:
                st.info("Matchup data for this pairing not available yet.")


# ══════════════════════════════════════════════════════════════════════════════
# PAGE 2 — COUNTERPICK SUGGESTER
# ══════════════════════════════════════════════════════════════════════════════
elif page == "🛡️ Counterpicker":
    st.header("Counterpick Suggester")
    st.markdown("Find the best characters to counter an opponent you are struggling against.")

    char_list = ["-"] + sorted(char_data.keys())

    with st.container(border=True):
        col1, col2, col3, col4 = st.columns(4)
        
        difficulty_options = ["-", "Beginner", "Intermediate", "Advanced"]
        playstyle_options  = ["-", "Zoner", "Rushdown", "Grappler", "Balanced"]
        
        with col1:
            main_char = st.selectbox("Your Main (Optional):", char_list, key="cp_main")
        with col2:
            opponent_char = st.selectbox("Character Beating You:", char_list, key="cp_opponent")
        with col3:
            diff_filter = st.selectbox("Filter by Difficulty:", difficulty_options, key="cp_diff")
        with col4:
            style_filter = st.selectbox("Filter by Playstyle:", playstyle_options, key="cp_style")

    if opponent_char == "-":
        st.info("Select the character beating you to see counterpick suggestions.")
    else:
        suggestions = []
        for char in matchups:
            if char == opponent_char or char == main_char:
                continue
            
            info = char_data.get(char, {})
            if diff_filter != "-" and info.get("difficulty", "").lower() != diff_filter.lower():
                continue
            if style_filter != "-" and info.get("playstyle", "").lower() != style_filter.lower():
                continue

            if opponent_char in matchups[char]:
                score = matchups[char][opponent_char]
                suggestions.append({
                    "Character": char,
                    "Score": score,
                    "Tier": info.get("tier", "-"),
                    "Playstyle": info.get("playstyle", "-")
                })
        
        suggestions.sort(key=lambda x: x["Score"], reverse=True)
        top_3 = suggestions[:3]

        if not top_3:
            st.warning("No matchup data available against this character.")
        else:
            if main_char != "-" and main_char in matchups and opponent_char in matchups[main_char]:
                main_score = matchups[main_char][opponent_char]
                badge = get_result_badge(main_score)
                st.markdown(f"**Your Main ({main_char}) vs {opponent_char}**: Score `{main_score}` → {badge}", unsafe_allow_html=True)
                st.divider()

            st.subheader(f"Top 3 Counterpicks against {opponent_char}")
            
            cols = st.columns(3)
            for i, cp in enumerate(top_3):
                with cols[i]:
                    with st.container(border=True):
                        st.markdown(f"### #{i+1} {cp['Character']}")
                        
                        score_badge = get_result_badge(cp['Score'])
                        st.markdown(f"**Matchup Score:** `{cp['Score']}` {score_badge}", unsafe_allow_html=True)
                        
                        tier_badge = get_tier_badge(cp['Tier'])
                        st.markdown(f"**Tier:** {tier_badge}", unsafe_allow_html=True)
                        
                        style_badge = get_playstyle_badge(cp['Playstyle'])
                        st.markdown(f"**Playstyle:** {style_badge}", unsafe_allow_html=True)
                        
                        portrait_path = f"media/character-portraits/{cp['Character']}.png"
                        fallback_path = f"media/character-portraits/{cp['Character']}.jpg"
                        pyra_path = f"media/character-portraits/Pyra.png"
                        
                        if os.path.exists(portrait_path):
                            st.image(portrait_path, use_container_width=True)
                        elif os.path.exists(fallback_path):
                            st.image(fallback_path, use_container_width=True)
                        elif cp['Character'] == "Pyra/Mythra" and os.path.exists(pyra_path):
                            st.image(pyra_path, use_container_width=True)


# ══════════════════════════════════════════════════════════════════════════════
# PAGE 3 — LEARNING PATH
# ══════════════════════════════════════════════════════════════════════════════
elif page == "📚 Learning Path":
    st.header("Character Learning Path")
    st.markdown("Structured skill progression from zero to competitive. Complete stages in order.")

    col1, col2 = st.columns([3, 1])
    with col1:
        with st.container(border=True):
            only_roster = st.checkbox("Only show characters in My Roster", key="learn_filter_roster")
            if only_roster:
                roster_chars = [c for c in char_data.keys() if c in st.session_state.roster]
                char_list = ["-"] + sorted(roster_chars)
                if not roster_chars:
                    st.warning("Your roster is empty. Go to 'My Roster' to add characters.")
            else:
                char_list = ["-"] + sorted(char_data.keys())
            char_pick = st.selectbox("Choose a character:", char_list, key="learn_char")

    if char_pick == "-":
        st.info("Select a character above to view their learning path.")
    elif char_pick in char_data:
        info = char_data[char_pick]
        
        all_skills = [skill for stage in info["path"] for skill in stage["skills"]]
        total = len(all_skills)
        completed_count = sum(1 for stage in info["path"] for skill in stage["skills"] if f"{char_pick}_{stage['stage']}_{skill}" in st.session_state.progress)
        pct = completed_count / total if total > 0 else 0

        with col2:
            completed_color = "#28a745" if pct == 1.0 else "#2d9dff"
            fig = go.Figure(go.Pie(
                values=[completed_count, total - completed_count],
                labels=["Completed", "Remaining"],
                hole=0.7,
                textinfo="none",
                marker=dict(colors=[completed_color, "rgba(128, 128, 128, 0.2)"])
            ))
            fig.update_layout(
                showlegend=False,
                margin=dict(l=10, r=10, t=10, b=10),
                annotations=[dict(text=f"{int(pct * 100)}%", x=0.5, y=0.5, font_size=32, showarrow=False)],
                height=220
            )
            st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})

        with col1:
            with st.container(border=True):
                badge = get_difficulty_badge(info['difficulty'])
                st.markdown(f"**Difficulty:** {badge}", unsafe_allow_html=True)
                st.markdown(f"**Overview:** {info['overview']}")

        with st.container(border=True):
            completed = []

            st.markdown(
                """
                <style>
                [data-testid="stExpander"] details summary {
                    pointer-events: none;
                }
                [data-testid="stExpander"] details summary svg {
                    display: none;
                }
                </style>
                """,
                unsafe_allow_html=True,
            )

            for i, stage in enumerate(info["path"]):
                stage_label = f"Stage {i + 1}: {stage['stage']}"
                with st.expander(stage_label, expanded=True):
                    for skill in stage["skills"]:
                        key = f"{char_pick}_{stage['stage']}_{skill}"
                        if key not in st.session_state:
                            st.session_state[key] = key in st.session_state.progress
                        checked = st.checkbox(skill, key=key, on_change=toggle_skill, args=(key,))
                        if checked:
                            completed.append(skill)

            st.divider()
            st.subheader("Your Progress")
            if pct == 1.0:
                st.markdown(
                    """<style>
                        .stProgress > div > div > div > div {
                            background-color: #28a745 !important;
                        }
                    </style>""",
                    unsafe_allow_html=True,
                )
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
# PAGE 4 — OVERALL STATS
# ══════════════════════════════════════════════════════════════════════════════
elif page == "📊 Overall Stats":
    st.header("Overall Character Stats")
    st.markdown("A full roster overview showing every character's tier, difficulty, playstyle, and average matchup score.")

    stats_data = []
    for char, info in char_data.items():
        avg_score = 0.0
        if char in matchups and matchups[char]:
            avg_score = sum(matchups[char].values()) / len(matchups[char])
            
        stats_data.append({
            "Character": char,
            "Tier": info.get("tier", "-"),
            "Difficulty": info.get("difficulty", "-"),
            "Playstyle": info.get("playstyle", "-"),
            "Avg Matchup Score": round(avg_score, 3)
        })
        
    df_stats = pd.DataFrame(stats_data)
    
    # Convert Tier and Difficulty to categorical types for correct logical sorting
    tier_order = ["S", "A", "B", "C", "D", "E", "-"]
    diff_order = ["Beginner", "Intermediate", "Advanced", "-"]
    df_stats["Tier"] = pd.Categorical(df_stats["Tier"], categories=tier_order, ordered=True)
    df_stats["Difficulty"] = pd.Categorical(df_stats["Difficulty"], categories=diff_order, ordered=True)
    
    # Add sorting controls
    sort_col, order_col, _ = st.columns([1, 1, 2])
    with sort_col:
        sort_by = st.selectbox("Sort by:", ["Character", "Tier", "Difficulty", "Playstyle", "Avg Matchup Score"])
    with order_col:
        default_order = 1 if sort_by == "Avg Matchup Score" else 0
        sort_order = st.radio("Order:", ["Ascending", "Descending"], index=default_order, horizontal=True)

        
    df_stats = df_stats.sort_values(by=sort_by, ascending=(sort_order == "Ascending"))

    with st.container(border=True):
        st.table(df_stats.set_index("Character"))


# ══════════════════════════════════════════════════════════════════════════════
# PAGE 5 — TIER LIST
# ══════════════════════════════════════════════════════════════════════════════
elif page == "🎖️ Tier List":
    st.header("Official SSBU Tier List (4th Edition)")
    with st.container(border=True):
        img = Image.open("media/ssbu-tier-list.png")
        st.image(img, caption="Source: Ultrank (https://medium.com/@ultrankssb/the-fourth-ultrank-tier-list-2026-9c5f6964f7e3)", use_container_width=True)


# ══════════════════════════════════════════════════════════════════════════════
# PAGE 6 — MY ROSTER
# ══════════════════════════════════════════════════════════════════════════════
elif page == "👤 My Roster":
    st.header("My Roster")
    st.markdown("Manage the characters you play and track your aggregate progress.")

    with st.container(border=True):
        st.subheader("Manage Roster")
        char_list = ["-"] + sorted(char_data.keys())
        
        col1, col2, col3, col4 = st.columns([3, 3, 2, 2])
        with col1:
            selected_char = st.selectbox("Select Character", char_list, key="roster_char")
        with col2:
            status_options = ["Maining", "Learning", "Want to Try"]
            selected_status = st.selectbox("Status", status_options, key="roster_status")
        with col3:
            st.markdown("<br>", unsafe_allow_html=True) # padding
            if st.button("Add / Update", use_container_width=True):
                if selected_char != "-":
                    st.session_state.roster[selected_char] = selected_status
                    save_roster()
                    st.success(f"Updated {selected_char}!", icon="✅")
                else:
                    st.error("Please select a character.")
        with col4:
            st.markdown("<br>", unsafe_allow_html=True) # padding
            if st.button("Remove", use_container_width=True):
                if selected_char != "-" and selected_char in st.session_state.roster:
                    del st.session_state.roster[selected_char]
                    save_roster()
                    st.success(f"Removed {selected_char}!", icon="✅")
                elif selected_char == "-":
                    st.error("Please select a character.")
                else:
                    st.warning(f"{selected_char} is not in your roster.")

    with st.container(border=True):
        st.subheader("Current Roster")
        if not st.session_state.roster:
            st.info("Your roster is empty. Add characters above.")
        else:
            mains = [c for c, s in st.session_state.roster.items() if s == "Maining"]
            learning = [c for c, s in st.session_state.roster.items() if s == "Learning"]
            wtt = [c for c, s in st.session_state.roster.items() if s == "Want to Try"]
            
            rm1, rm2, rm3 = st.columns(3)
            with rm1:
                st.markdown("### 👑 Mains")
                if mains:
                    for c in mains:
                        st.markdown(f"- {c}")
                else:
                    st.caption("None")
            with rm2:
                st.markdown("### 📈 Learning")
                if learning:
                    for c in learning:
                        st.markdown(f"- {c}")
                else:
                    st.caption("None")
            with rm3:
                st.markdown("### 🤔 Want to Try")
                if wtt:
                    for c in wtt:
                        st.markdown(f"- {c}")
                else:
                    st.caption("None")

    with st.container(border=True):
        st.subheader("Aggregate Roster Progress")
        if not st.session_state.roster:
             st.info("Add characters to your roster to see aggregate progress.")
        else:
            total_skills = 0
            completed_skills = 0
            
            progress_data = []

            for char, status in st.session_state.roster.items():
                if char in char_data:
                    char_skills = [skill for stage in char_data[char]["path"] for skill in stage["skills"]]
                    char_total = len(char_skills)
                    char_completed = 0
                    
                    for stage in char_data[char]["path"]:
                        for skill in stage["skills"]:
                            key = f"{char}_{stage['stage']}_{skill}"
                            if key in st.session_state.progress:
                                char_completed += 1
                    
                    total_skills += char_total
                    completed_skills += char_completed
                    
                    pct = char_completed / char_total if char_total > 0 else 0
                    progress_data.append({
                        "Character": char,
                        "Status": status,
                        "Skills Completed": f"{char_completed} / {char_total}",
                        "Progress": int(pct * 100)
                    })
            
            if total_skills > 0:
                overall_pct = completed_skills / total_skills
                
                if overall_pct == 1.0:
                    st.markdown(
                        """<style>
                            .stProgress > div > div > div > div {
                                background-color: #28a745 !important;
                            }
                        </style>""",
                        unsafe_allow_html=True,
                    )
                    
                st.progress(overall_pct)
                st.caption(f"Overall Progress: **{completed_skills} / {total_skills}** skills completed (**{int(overall_pct * 100)}%**)")
                
                df_prog = pd.DataFrame(progress_data)
                df_prog["Status"] = pd.Categorical(df_prog["Status"], categories=["Maining", "Learning", "Want to Try"], ordered=True)
                df_prog = df_prog.sort_values(by=["Status", "Character"])
                
                st.divider()
                for _, row in df_prog.iterrows():
                    color = "#28a745" if row["Progress"] == 100 else "var(--primary-color, #ff4b4b)"
                    st.markdown(f"""
                        <div style="display: flex; align-items: center; margin-bottom: 12px;">
                            <div style="width: 160px; font-weight: 600;">{row['Character']}</div>
                            <div style="width: 100px; color: gray; font-size: 0.85em;">{row['Status']}</div>
                            <div style="width: 60px; text-align: right; margin-right: 15px; font-size: 0.85em; color: gray;">{row['Skills Completed']}</div>
                            <div style="flex-grow: 1; background-color: rgba(128, 128, 128, 0.2); border-radius: 4px; height: 14px; overflow: hidden;">
                                <div style="background-color: {color}; width: {row['Progress']}%; height: 100%;"></div>
                            </div>
                            <div style="width: 45px; text-align: right; font-size: 0.85em; margin-left: 10px; font-weight: 600;">{row['Progress']}%</div>
                        </div>
                    """, unsafe_allow_html=True)
            else:
                st.info("No learning paths found for characters in your roster.")


# ══════════════════════════════════════════════════════════════════════════════
# PAGE 7 — MY PROGRESS
# ══════════════════════════════════════════════════════════════════════════════
elif page == "📈 My Progress":
    st.header("My Progress")
    st.markdown("Track your learning path progress across all characters.")

    f1, f2, _ = st.columns([1, 1, 2])
    with f1:
        show_started_only = st.checkbox("Only show started characters")
    with f2:
        show_roster_only = st.checkbox("Only show roster characters")

    with st.container(border=True):
        st.subheader("Character Progress")
        
        total_skills = 0
        completed_skills = 0
        
        progress_data = []

        for char, info in char_data.items():
            if "path" in info:
                char_skills = [skill for stage in info["path"] for skill in stage["skills"]]
                char_total = len(char_skills)
                char_completed = 0
                
                for stage in info["path"]:
                    for skill in stage["skills"]:
                        key = f"{char}_{stage['stage']}_{skill}"
                        if key in st.session_state.progress:
                            char_completed += 1
                
                pct = char_completed / char_total if char_total > 0 else 0
                status = st.session_state.roster.get(char, "-")
                
                if show_started_only and char_completed == 0:
                    continue
                if show_roster_only and status == "-":
                    continue
                
                total_skills += char_total
                completed_skills += char_completed
                
                progress_data.append({
                    "Character": char,
                    "Status": status,
                    "Skills Completed": f"{char_completed} / {char_total}",
                    "Progress": int(pct * 100)
                })
        
        if total_skills > 0:
            overall_pct = completed_skills / total_skills
            
            if overall_pct == 1.0:
                st.markdown(
                    """<style>
                        .stProgress > div > div > div > div {
                            background-color: #28a745 !important;
                        }
                    </style>""",
                    unsafe_allow_html=True,
                )
                
            st.progress(overall_pct)
            st.caption(f"Overall Progress: **{completed_skills} / {total_skills}** skills completed (**{int(overall_pct * 100)}%**)")
            
            df_prog = pd.DataFrame(progress_data)
            df_prog["Status"] = pd.Categorical(df_prog["Status"], categories=["Maining", "Learning", "Want to Try", "-"], ordered=True)
            df_prog = df_prog.sort_values(by=["Progress", "Character"], ascending=[False, True])
            
            st.divider()
            for _, row in df_prog.iterrows():
                color = "#28a745" if row["Progress"] == 100 else "var(--primary-color, #ff4b4b)"
                st.markdown(f"""
                    <div style="display: flex; align-items: center; margin-bottom: 12px;">
                        <div style="width: 160px; font-weight: 600;">{row['Character']}</div>
                        <div style="width: 100px; color: gray; font-size: 0.85em;">{row['Status']}</div>
                        <div style="width: 60px; text-align: right; margin-right: 15px; font-size: 0.85em; color: gray;">{row['Skills Completed']}</div>
                        <div style="flex-grow: 1; background-color: rgba(128, 128, 128, 0.2); border-radius: 4px; height: 14px; overflow: hidden;">
                            <div style="background-color: {color}; width: {row['Progress']}%; height: 100%;"></div>
                        </div>
                        <div style="width: 45px; text-align: right; font-size: 0.85em; margin-left: 10px; font-weight: 600;">{row['Progress']}%</div>
                    </div>
                """, unsafe_allow_html=True)
        else:
            st.info("No characters match the selected filters.")