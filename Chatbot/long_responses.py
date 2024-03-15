import random

R_FOOD = "As a machine learning model created by OpenAI, I don't have a physical form, and therefore, I don't eat or consume any kind of food. "
R_COUNSEL = "Stay Positive: Maintain a positive mindset even in challenging situations. A positive outlook can help you navigate difficulties more effectively."
R_LOVE = "Love is a complex and multifaceted emotion that encompasses a range of feelings, attitudes, and behaviors.I can do is help you with your querries and doubts"

def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "Sounds about right.",
                "What does that mean?"][
        random.randrange(4)]
    return response