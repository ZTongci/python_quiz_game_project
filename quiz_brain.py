class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list

    def next_question(self):
        self.question_number += 1
        option = input(
            f"Q.{self.question_number}: {self.question_list[self.question_number].text} (True"
            f"/False)?: ")

        return option

    def still_has_question(self):
        if self.question_number < len(self.question_list) - 1:
            return True
        else:
            return False
