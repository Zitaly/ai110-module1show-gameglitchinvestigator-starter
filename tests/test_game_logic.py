import sys
from pathlib import Path

# tests/ is not a package, so make the project root importable regardless of
# which directory pytest is invoked from.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from logic_utils import check_guess, parse_guess, update_score


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


def test_parse_guess_accepts_plain_and_padded_numbers():
    assert parse_guess("42") == (True, 42, None)
    assert parse_guess("  42  ") == (True, 42, None)
    assert parse_guess("-7") == (True, -7, None)


def test_parse_guess_rejects_empty_input():
    for raw in (None, "", "   "):
        ok, value, err = parse_guess(raw)
        assert not ok
        assert value is None
        assert err


def test_parse_guess_rejects_decimals():
    # Regression: "3.9" was truncated to 3, so the game scored a guess the
    # player never made instead of telling them the input was invalid.
    ok, value, err = parse_guess("3.9")
    assert not ok
    assert value is None
    assert err


def test_parse_guess_rejects_non_numbers():
    ok, value, err = parse_guess("fifty")
    assert not ok
    assert value is None
    assert err


def test_win_on_first_attempt_scores_full_points():
    # Regression: the old formula treated the first guess as the second, so a
    # perfect game paid 80 instead of 100.
    assert update_score(0, "Win", 1) == 100


def test_win_points_decay_by_attempt():
    assert update_score(0, "Win", 2) == 90
    assert update_score(0, "Win", 3) == 80


def test_win_points_floor_at_ten():
    assert update_score(0, "Win", 20) == 10


def test_wrong_guesses_cost_the_same_either_direction():
    # Regression: "Too High" awarded +5 on even attempts, so overshooting was
    # sometimes better than undershooting.
    for attempt in range(1, 6):
        assert update_score(50, "Too High", attempt) == 45
        assert update_score(50, "Too Low", attempt) == 45


def test_score_never_goes_negative():
    assert update_score(0, "Too Low", 1) == 0


def test_unknown_outcome_leaves_score_alone():
    assert update_score(37, "Sideways", 2) == 37
