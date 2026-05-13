import streamlit as st
import json
import pandas as pd

# ── Load data ──────────────────────────────────────────────────────────────────
with open("data/matchups.json") as f:
    matchups = json.load(f)

with open("data/characters.json") as f:
    char_data = json.load(f)

# ── Page config ────────────────────────────────────────────────────────────────
st.set_page_config(page_title="SSBU Optimizer", page_icon="🎮", layout="wide")

st.title("🎮 Super Smash Bros. Ultimate Optimizer")
st.caption("Matchup data sourced from pro player matchup charts. Learning paths based on competitive guides.")

# ── Tab layout ─────────────────────────────────────────────────────────────────
tab1, tab2 = st.tabs(["⚔️ Matchup Analyzer", "📚 Learning Path"])


# ══════════════════════════════════════════════════════════════════════════════
# TAB 1 — MATCHUP ANALYZER
# ══════════════════════════════════════════════════════════════════════════════
with tab1:
    st.header("Character Matchup Analyzer")
    st.markdown("Scores range from **0.0** (hard loss) to **1.0** (dominant win). **0.5 = even**.")

    characters = sorted(matchups.keys())
    selected = st.selectbox("Select your character:", characters, key="matchup_char")

    if selected:
        data = matchups[selected]
        df = pd.DataFrame(list(data.items()), columns=["Opponent", "Score"])

        def label(score):
            if score >= 0.6:
                return "✅ Advantage"
            elif score <= 0.4:
                return "❌ Disadvantage"
            else:
                return "➖ Even"

        df["Result"] = df["Score"].apply(label)
        df = df.sort_values("Score", ascending=False)

        # Summary metrics
        adv = len(df[df["Score"] >= 0.6])
        even = len(df[(df["Score"] > 0.4) & (df["Score"] < 0.6)])
        dis = len(df[df["Score"] <= 0.4])

        m1, m2, m3 = st.columns(3)
        m1.metric("✅ Advantages", adv)
        m2.metric("➖ Even", even)
        m3.metric("❌ Disadvantages", dis)

        st.divider()

        # Three columns: advantage / even / disadvantage
        col1, col2, col3 = st.columns(3)

        with col1:
            st.subheader("✅ Advantages")
            adv_df = df[df["Score"] >= 0.6][["Opponent", "Score"]].reset_index(drop=True)
            if adv_df.empty:
                st.info("No advantages in this dataset.")
            else:
                st.dataframe(adv_df, use_container_width=True, hide_index=True)

        with col2:
            st.subheader("➖ Even")
            even_df = df[(df["Score"] > 0.4) & (df["Score"] < 0.6)][["Opponent", "Score"]].reset_index(drop=True)
            if even_df.empty:
                st.info("No even matchups in this dataset.")
            else:
                st.dataframe(even_df, use_container_width=True, hide_index=True)

        with col3:
            st.subheader("❌ Disadvantages")
            dis_df = df[df["Score"] <= 0.4][["Opponent", "Score"]].reset_index(drop=True)
            if dis_df.empty:
                st.info("No disadvantages in this dataset.")
            else:
                st.dataframe(dis_df, use_container_width=True, hide_index=True)

        st.divider()

        # Bar chart
        st.subheader(f"{selected}'s Full Matchup Chart")
        chart_df = df.set_index("Opponent")[["Score"]]
        st.bar_chart(chart_df)

        # Head-to-head picker
        st.divider()
        st.subheader("🔍 Head-to-Head")
        opponent = st.selectbox("Pick an opponent to check:", [c for c in characters if c != selected], key="h2h")
        if opponent and opponent in data:
            score = data[opponent]
            result = label(score)
            st.markdown(f"**{selected}** vs **{opponent}**: Score `{score}` → {result}")
        else:
            st.info("Matchup data for this pairing not available yet.")


# ══════════════════════════════════════════════════════════════════════════════
# TAB 2 — LEARNING PATH
# ══════════════════════════════════════════════════════════════════════════════
with tab2:
    st.header("Character Learning Path")
    st.markdown("Structured skill progression from zero to competitive. Complete stages in order.")

    char_list = sorted(char_data.keys())
    char_pick = st.selectbox("Choose a character:", char_list, key="learn_char")

    if char_pick and char_pick in char_data:
        info = char_data[char_pick]

        st.markdown(f"**Difficulty:** `{info['difficulty']}`")
        st.markdown(f"**Overview:** {info['overview']}")
        st.divider()

        # Track all skills for progress bar
        all_skills = [skill for stage in info["path"] for skill in stage["skills"]]
        total = len(all_skills)
        completed = []

        # Render each stage
        for i, stage in enumerate(info["path"]):
            stage_label = f"Stage {i + 1}: {stage['stage']}"
            with st.expander(stage_label, expanded=(i == 0)):
                for skill in stage["skills"]:
                    key = f"{char_pick}_{stage['stage']}_{skill}"
                    checked = st.checkbox(skill, key=key)
                    if checked:
                        completed.append(skill)

        # Progress bar
        st.divider()
        st.subheader("Your Progress")
        pct = len(completed) / total if total > 0 else 0
        st.progress(pct)
        st.caption(f"{len(completed)} / {total} skills completed ({int(pct * 100)}%)")

        if pct == 1.0:
            st.success("🏆 You've completed all stages. You're playing at a pro level with this character.")
        elif pct >= 0.75:
            st.info("💪 Almost there — you're in advanced territory.")
        elif pct >= 0.5:
            st.info("📈 Good progress — pushing into advanced skills.")
        elif pct >= 0.25:
            st.info("🔧 Intermediate stage — keep building.")
        else:
            st.info("🟢 Just getting started. Work through Stage 1 first.")

    else:
        st.warning("No learning path data found for this character. Add them to characters.json.")