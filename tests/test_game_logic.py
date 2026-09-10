import sys
from pathlib import Path

# tests/ is not a package, so make the project root importable regardless of
# which directory pytest is invoked from.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from logic_utils import check_guess


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"


def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


def test_guess_below_secret_hints_higher():
    # Regression: guessing 50 when the secret is higher used to say "Go LOWER"
    # because the hint messages were swapped relative to the outcomes.
    outcome, message = check_guess(50, 73)
    assert outcome == "Too Low"
    assert "HIGHER" in message


def test_guess_above_secret_hints_lower():
    # The mirror image of the bug above.
    outcome, message = check_guess(50, 20)
    assert outcome == "Too High"
    assert "LOWER" in message
