import re


def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    count = 0
    pattern = r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$"
    result = re.findall(pattern, ip)
    if result == []:
        return False
    correction = result[0]
    count = 0
    for t in correction:
        if 0 <= int(t) <= 255:
            count = count + 1
        else:
            pass
    if count == 4:
        return True

    else:
        return False





if __name__ == "__main__":
    main()