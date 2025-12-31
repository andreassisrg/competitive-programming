import sys


def main():
    _ = int(input())
    chat = set()
    recipients = list()
    for line in sys.stdin:
        message = line.strip()
        if not message:
            break
        recipients.append(message)

    for recipient in recipients[::-1]:
        if recipient in chat:
            continue
        else:
            chat.add(recipient)
            print(recipient)


main()
