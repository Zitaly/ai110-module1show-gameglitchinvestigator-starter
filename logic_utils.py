#FIX: Refactored into logic_utils.py
def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20

    if difficulty == "Normal":
        return 1, 100

    if difficulty == "Hard":
        return 1, 50

    return 1, 100


#FIX: Refactored into logic_utils.py
def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."

    # Surrounding whitespace is a typo, not input. A field holding only spaces
    # is still an empty field.
    text = raw.strip()

    if text == "":
        return False, None, "Enter a guess."

    try:
        value = int(text)
    except ValueError:
        # A decimal used to be silently truncated, so a guess of "3.9" was
        # scored as 3 and the player was told they had guessed something they
        # never typed. Whole numbers only.
        return False, None, "That is not a whole number."

    return True, value, None

#FIX: Refactored into logic_utils.py
def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    guess = int(guess)
    secret = int(secret)

    if guess == secret:
        return "Win", "🎉 Correct!"

    if guess > secret:
        return "Too High", "📉 Go LOWER!"

    return "Too Low", "📈 Go HIGHER!"


#FIX: Refactored into logic_utils.py
def update_score(current_score: int, outcome: str, attempt_number: int):
    """
    Update score based on outcome and attempt number.

    attempt_number is 1 for the first guess of a game.
    """
    if outcome == "Win":
        # attempt_number already counts the guess being scored, so winning on
        # the first try is worth the full 100. The old formula added one more
        # and quietly charged the player for a guess they never made.
        points = 100 - 10 * (attempt_number - 1)
        if points < 10:
            points = 10
        return current_score + points

    # Every wrong guess costs the same. "Too High" used to award +5 on
    # even-numbered attempts, so overshooting was sometimes worth more than
    # undershooting the same distance.
    if outcome in ("Too High", "Too Low"):
        return max(0, current_score - 5)

    return current_score
