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


def test_difficulty_selects_matching_range():
    # Changing the difficulty has to change the guessing range with it. The app
    # used to hold every game at the Normal range no matter what was selected.
    from logic_utils import get_range_for_difficulty

    expected_ranges = {
        "Easy": (1, 20),
        "Normal": (1, 100),
        "Hard": (1, 50),
    }

    for difficulty, bounds in expected_ranges.items():
        assert get_range_for_difficulty(difficulty) == bounds

    # Each difficulty is distinct, so a stale selection cannot pass as another.
    assert len(set(expected_ranges.values())) == len(expected_ranges)

    # An unrecognized difficulty falls back to the Normal range.
    assert get_range_for_difficulty("Impossible") == (1, 100)
