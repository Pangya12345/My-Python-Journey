import re

def main():
    print(parse(input("HTML: ")))

def parse(s):
    pattern = r'<iframe.*src=".*://.*.youtube.com/embed/(.+?)".*></iframe>'
    result = re.search(pattern, s)
    if result:
        new_result = result.group(1)
    else:
        return None

    return f"https://youtu.be/{new_result}"


if __name__ == "__main__":
    main()