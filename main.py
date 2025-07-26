
import streamlit as st
import time

st.set_page_config(page_title="Accessing Secure Node", layout="centered")

COMMANDS = [
    "> connect --node 42.7.16.89",
    "> override --auth-level root",
    "> decrypt --keygen access_vault_07",
    "> inject --protocol ghost_ai --stealth-mode",
    "> execute --init-consciousness --lockout-human-safeguards"
]

st.markdown("""
<style>
.terminal {
    background-color: black;
    color: #00FF00;
    font-family: monospace;
    font-size: 20px;
    padding: 30px;
    border-radius: 10px;
    box-shadow: 0 0 20px #00FF00;
    height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
}
</style>
""", unsafe_allow_html=True)

terminal = st.empty()
output = ""

# Durée totale de l'effet (en secondes)
total_duration = 30
command_count = len(COMMANDS)
typing_time = 22  # secondes
pause_between = typing_time / command_count

for cmd in COMMANDS:
    line = ""
    for char in cmd:
        line += char
        terminal.markdown(f'<div class="terminal">{output}{line}</div>', unsafe_allow_html=True)
        time.sleep(0.04)
    output += line + "<br>"
    terminal.markdown(f'<div class="terminal">{output}</div>', unsafe_allow_html=True)
    time.sleep(pause_between - len(cmd) * 0.04)

# Curseur clignotant final pendant le reste du temps
cursor_duration = total_duration - typing_time
blink_count = int(cursor_duration / 0.8)

for _ in range(blink_count):
    terminal.markdown(f'<div class="terminal">{output}_</div>', unsafe_allow_html=True)
    time.sleep(0.4)
    terminal.markdown(f'<div class="terminal">{output}</div>', unsafe_allow_html=True)
    time.sleep(0.4)
