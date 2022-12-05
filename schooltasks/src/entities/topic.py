"""moduli sisältää topic eli aihe-luokan"""


class Topic:
    """luokka aiheen ominaisuuksille"""

    def __init__(self, topic):
        """alustaa Topic luokan olion
        Args:   topic: aihe"""
        self.topic = topic

    def __repr__(self):
        return f"Topic({self.topic})"

    def __str__(self):
        return f"{self.topic}"
