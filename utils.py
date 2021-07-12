def check_file(filepath):
    try:
        f = open(filepath)
        f.close()
    except FileNotFoundError:
        print(f"file {filepath} not accessible")
        exit()