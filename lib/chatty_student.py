from student import Student


class ChattyStudent(Student):
    def hello(self):
        # Call the parent hello
        super().hello()
        # Add chatty part
        print(
            "How are you doing today? I'm okay, but I'm kind of tired. "
            "Did you watch The Walking Dead last night? You didn't?! Oh man, "
            "it was so crazy! What, you don't want any spoilers? "
            "Okay well let me just tell you who died..."
        )

    def raise_hand(self):
        # Call parent's raise_hand 10 times
        for _ in range(10):
            super().raise_hand()
