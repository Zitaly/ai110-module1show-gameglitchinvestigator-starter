"""Makes the project root importable so tests can do `from logic_utils import ...`."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
