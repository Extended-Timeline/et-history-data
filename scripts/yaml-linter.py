import yaml, sys

try:
    with open(sys.argv[1], 'r', encoding='utf-8') as f:
        yaml.safe_load(f)
except yaml.YAMLError as e:
    print(e, file=sys.stderr)
    sys.exit(1)
except Exception as e:
    print(f"Unexpected error: {e}", file=sys.stderr)
    sys.exit(1)
