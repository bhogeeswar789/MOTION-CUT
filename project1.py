def emoji_mood_responder():

    mood_dict = {
        'happy': ('😊', 'Great to see you happy! Keep smiling!'),
        'sad': ('😢', 'It’s okay to feel sad. Things will get better.'),
        'angry': ('😡', 'Take a deep breath. Let it go.'),
        'excited': ('🤩', 'Yay! That’s the spirit!'),
        'nervous': ('😬', 'You got this! Stay strong!'),
        'tired': ('😴', 'Rest up and recharge. You deserve it.'),
        'confused': ('😕', 'It’s okay to be confused. Take your time to figure it out.'),
        'bored': ('😐', 'Find something fun to do and brighten your day!'),
        'grateful': ('🙏', 'Gratitude is a beautiful feeling. Stay thankful!'),
        'loved': ('❤️', 'You are loved and appreciated!'),
        'stressed': ('😥', 'Take a moment to breathe and relax. You got this!'),
        'proud': ('😌', 'You should be proud! Keep up the good work!'),
        'surprised': ('😲', 'Whoa! That’s surprising!'),
        'determined': ('💪', 'Stay focused and keep pushing forward!'),
        'relaxed': ('😌', 'Take a moment to enjoy the calmness.'),
        'scared': ('😨', 'Fear is just a feeling. You can overcome it!'),
        'hopeful': ('🤞', 'Keep that hope alive! Good things are coming.'),
        'curious': ('🤔', 'Curiosity is the key to learning new things!'),
        'jealous': ('😒', 'Remember, you are unique and valuable.'),
        'ashamed': ('😳', 'We all make mistakes. Learn and move forward.'),
        'anxious': ('😰', 'Take deep breaths. It will be okay.'),
        'optimistic': ('😄', 'Positive vibes only! Stay optimistic!'),
        'lonely': ('🥺', 'You are not alone. Reach out to someone.'),
        'embarrassed': ('😅', 'It’s okay! We all have those moments.'),
        'hungry': ('🍔', 'Grab a bite and fuel up!'),
        'sleepy': ('😴', 'Get some rest and recharge your energy.'),
        'frustrated': ('😤', 'Take a deep breath and let it go.')
    }

    
    mood = input("How are you feeling right now? (e.g., happy, sad, angry, etc.): ").strip().lower()

    
    if mood in mood_dict:
        emoji, message = mood_dict[mood]
        print(f"{emoji} {message}")
    else:
        
        print("🤔 Hmm, I don't quite understand that mood. Stay positive!")


if __name__ == "__main__":
    emoji_mood_responder()
