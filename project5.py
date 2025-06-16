def recommend_color_and_outfit(mood):
    mood_dict = {
        "happy": ("yellow", "yellow t-shirt"),
        "sad": ("green", "green hoodie"),
        "angry": ("black", "black jacket"),
        "stressed": ("blue", "blue jeans"),
        "relaxed": ("green", "green sundress"),
        "energetic": ("red", "red sportswear"),
        "confident": ("red", "red blazer"),
        "calm": ("blue", "blue shirt"),
        "serious": ("black", "black suit"),
        "caring": ("pink", "pink sweater"),
        "excited": ("orange", "orange hoodie"),
        "bored": ("gray", "gray sweatshirt"),
        "motivated": ("purple", "purple t-shirt"),
        "romantic": ("pink", "pink dress"),
        "anxious": ("light blue", "light blue top")
    }

    mood = mood.lower()

    if mood in mood_dict:
        color, outfit = mood_dict[mood]
        print(f"Based on your mood ({mood}), we recommend you wear {color}.\nHow about a {outfit}?")
    else:
        print("Mood not recognized. Try using a common mood like 'happy', 'stressed', or 'relaxed'.")


def main():
    print("Welcome to the Color Psychology Outfit Recommender System based on our mood.")
    mood = input("How are you feeling today? (e.g., happy, sad, stressed, etc): ")
    recommend_color_and_outfit(mood)


if __name__ == "__main__":
    main()