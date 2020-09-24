"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, words, text):
        """Create story with words and template text."""

        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started


story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}.""",
)

test = {
    "place": "Hogwarst",
    "noun": "apple",
    "verb": "fly",
    "adjective": "bitter",
    "plural_noun": "monkeys",
}

story_options = {
    "Fairytale": Story(
        ["place1", "noun1", "verb1", "adjective1", "plural_noun1"],
        """Once upon a time in a long-ago {place1}, there lived a
       large {adjective1} {noun1}. It loved to {verb1} {plural_noun1}.""",
    ),
    "Zoo": Story(
        [
            "adjective1",
            "noun1",
            "verb(past)1",
            "adverb1",
            "adjective2",
            "noun2",
            "noun3",
            "adjective3",
            "verb1",
            "adverb2",
            "verb2",
            "adjective4",
        ],
        """Today I went to the zoo. I saw a(n) {adjective1} {noun1} jumping up and down in its tree. He {verb(past)1} {adverb1} through the large tunnel that led to its {adjective2} {noun2}. I got some peanuts and passed them through the cage to a gigantic gray {noun3} towering above my head. Feeding that animal made me hungry. I went to get a {adjective3} scoop of ice cream. It filled my stomach. Afterwards I had to {verb1} {adverb2} to catch our bus. When I got home I was too tired to {verb2} after my {adjective4} day at the zoo. """,
    ),
}
