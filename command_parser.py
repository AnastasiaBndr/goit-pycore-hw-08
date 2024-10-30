def parse_input(content):
    cmd, *args = content.split()
    cmd = cmd.strip().lower()
    return cmd, *args
