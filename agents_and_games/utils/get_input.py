def get_input(message: str, answers: list[str], message_error: str = "Try again") -> str:
    while True:
        answer = input(message)
        if answer in answers:
            print()
            return answer
        print(message_error)
        print()
