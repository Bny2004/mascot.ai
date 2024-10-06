import sys

import pytchat

from utils.yt_chat import yt_chat


def main():

    while True:
        try:
            video_id = input("Enter YouTube Live Stream video ID: ")
            chat = yt_chat(video_id)
            break
        except pytchat.exceptions.InvalidVideoIdException:
            print(
                "Invalid video id. Please make sure you've entered correct video id.\n"
            )

    while chat.is_alive():
        for c in chat.get().sync_items():
            try:
                print(f"{c.datetime} [{c.author.name}]- {c.message}")
            except KeyboardInterrupt:
                sys.exit("\n")


if __name__ == "__main__":
    main()
