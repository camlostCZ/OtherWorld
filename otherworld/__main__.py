import sys
from app import CliApp

try:
    app = CliApp()
    app.run()
except KeyboardInterrupt:
    print("Interrupted by user.", file=sys.stderr)
except KeyError:
    print("Unabled to initialize the game. Invalid YAML files?", 
        file=sys.stderr)
