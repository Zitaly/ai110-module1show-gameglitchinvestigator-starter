# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|Guess of 50 | Go HIGHER! | Go LOWER! | None |
|Press New Game | Start New Game | New game is started on back end, but the player can't play. | None |
| Change difficulty | Change difficulty to the chosen difficulty. | Difficulty remains on normal. | None |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
Claude with some googling.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
When I went to fix the bug with starting a new game, the AI suggested a reset of the game's variables. This did the trick and properly reset the game.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  Claude suggested that a file be made in the root folder, but this file was not needed, as I deleted it without suffering any errors.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I tested the fixes by playing the game and testing that specific feature.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  After I used AI to fix the new game feature, I started a new game, won the game, and started another new game. The solution worked. The bugs hampered the function of the entire game, as it ran better with a few fixed.
- Did AI help you design or understand any tests? How?
The AI helped design the tests, but it frequently made mistakes until the terms were simplified.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Streamlit seems rather simple to run, but it isn't as persistent as a normal site.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
  Using AI reminds me of the PBJ sandwich early Computer Science question where you have to give instructions on how to make a PBJ sandwich. Questions that might seem reeasonable to anyone looking at them can be easily messed up, wasting tokens (money) and time. AI can work fast, but it can waste even more time and money than just doing it manually.
- What is one thing you would do differently next time you work with AI on a coding task?
I would architect my solutions more and ensure that the AI is veering off course. When the problem is simple, I'll solve it myself. Additionally, I'll try to cluster changes.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
AI-generated code can be fast and efficient, but it can change the functionality of something and cause issues down the line. AI is a tool, and a tool is only as good as the person using it.
