import json
import os
from datetime import datetime


class ChatHistory:

    def __init__(self):

        self.directory = "history"

        os.makedirs(
            self.directory,
            exist_ok=True,
        )

    # ----------------------------------------------------
    # Save Chat
    # ----------------------------------------------------

    def save(
        self,
        repository,
        provider,
        model,
        prompt,
        response,
    ):

        timestamp = datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )

        filename = os.path.join(
            self.directory,
            f"{timestamp}.json",
        )

        data = {
            "timestamp": timestamp,
            "repository": repository,
            "provider": provider,
            "model": model,
            "prompt": prompt,
            "response": response,
        }

        with open(
            filename,
            "w",
            encoding="utf-8",
        ) as file:

            json.dump(
                data,
                file,
                indent=4,
                ensure_ascii=False,
            )

        return filename

    # ----------------------------------------------------
    # Load All Chats
    # ----------------------------------------------------

    def load_all(self):

        history = []

        files = sorted(
            os.listdir(self.directory),
            reverse=True,
        )

        for filename in files:

            if not filename.endswith(".json"):
                continue

            path = os.path.join(
                self.directory,
                filename,
            )

            with open(
                path,
                "r",
                encoding="utf-8",
            ) as file:

                history.append(
                    json.load(file)
                )

        return history

    # ----------------------------------------------------
    # Load Single Chat
    # ----------------------------------------------------

    def load(
        self,
        filename,
    ):

        path = os.path.join(
            self.directory,
            filename,
        )

        if not os.path.exists(path):

            return None

        with open(
            path,
            "r",
            encoding="utf-8",
        ) as file:

            return json.load(file)

    # ----------------------------------------------------
    # Delete Chat
    # ----------------------------------------------------

    def delete(
        self,
        filename,
    ):

        path = os.path.join(
            self.directory,
            filename,
        )

        if os.path.exists(path):

            os.remove(path)

    # ----------------------------------------------------
    # Clear History
    # ----------------------------------------------------

    def clear(self):

        files = os.listdir(
            self.directory
        )

        for filename in files:

            path = os.path.join(
                self.directory,
                filename,
            )

            if os.path.isfile(path):

                os.remove(path)

    # ----------------------------------------------------
    # Statistics
    # ----------------------------------------------------

    def count(self):

        return len(
            [
                f
                for f in os.listdir(self.directory)
                if f.endswith(".json")
            ]
        )