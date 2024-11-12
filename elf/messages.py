import random

from elf.models import Guess

# 🎄 Elf Message Generator 🎄 #


def get_positive_message(answer: int | str) -> str:
    messages: list[str] = [
        f"🎉 Congratulations! {answer} is correct! The elves are dancing with joy! 🎉",
        f"🎄 Fantastic! You've unlocked the magic number {answer}! Santa is thrilled! 🎄",
        f"✨ Brilliant work! {answer} is the key! Onward to the next challenge! ✨",
        f"🎁 Well done! {answer} is spot on! You've unwrapped a new achievement! 🎁",
        f"🌟 Stellar job with {answer}! You're shining brighter than the North Star! 🌟",
        f"☃️ Amazing! {answer} has brought warmth to the winter wonderland! ☃️",
        f"🍪 Delicious success with {answer}! Mrs. Claus baked you extra cookies! 🍪",
        f"🧝 Huzzah! {answer} is right! The elves are crafting new puzzles for you! 🧝",
        f"🔔 Ring the bells! {answer} resonates perfectly! 🔔",
        f"🎊 Bravo! {answer} is a gift to the world! Your code glows like Rudolph's nose! 🎊",
        f"🎅 Ho ho ho! {answer} is absolutely correct! Santa's loading up the sleigh! 🎅",
        f"🎄 Superb! {answer} fits like the star atop the tree! 🎄",
        f"🍬 Sweet victory! {answer} is the candy cane to our hot cocoa! 🍬",
        f"🎁 The elves applaud! {answer} is the perfect present! 🎁",
        f"🎉 Hurrah! {answer} spreads joy across the coding land! 🎉",
    ]
    return random.choice(messages)


def get_negative_message(answer: int) -> str:
    messages: list[str] = [
        "🤔 Hmm, the elves are scratching their heads in confusion!",
        "🎄 Uh-oh! The Christmas lights flickered. Let's brighten up that code!",
        "🌨️ Brrr! A snowstorm of errors. Time to clear the path!",
        "🎅 Not quite the right answer. Keep trying!",
        "🦌 The reindeer suggest taking another look!",
        "🍭 Whoops! Looks like a candy cane glitch!",
        "🎁 The present didn't open as expected. Let's try unwrapping it again!",
        "✨ So close! Maybe a touch more holiday magic is needed!",
        "❄️ Frosty feels a chill. Let's warm up that answer!",
        "🌟 Keep reaching! The stars are within your grasp!",
        "🎅 Santa's checking the list twice. Give it another try!",
        "🍪 The cookie crumbled this time. Have another bite!",
        "🧝 The elves are brainstorming new ideas. Don't give up!",
        "☃️ Snow worries! Let's build a better solution!",
        "❄️ Frosty suggests re-checking your work. Snow problem! ☃️",
    ]
    return random.choice(messages)


def get_correct_answer_message(answer: int | str) -> str:
    messages: list[str] = [
        f"🎉 {answer} is Correct! The sleigh is ready to fly! 🎉",
        f"🎄 Ho ho ho! Santa approves {answer} as your answer! 🎄",
        f"✨ Sparkling success! {answer} is the right answer! ✨",
        f"🎁 {answer} is Perfect! You've unwrapped the correct solution! 🎁",
        f"🌟 Bravo! Your {answer} shines brightly on the tree! 🌟",
        f"🎅 Spot on! {answer} is just what Santa ordered! 🎅",
        f"🎉 Well done! {answer} lights up the holiday spirit! 🎉",
        f"🎄 Cheers! {answer} fits perfectly under the tree! 🎄",
        f"🌟 Excellent! {answer} is a star performer! 🌟",
        f"✨ Magic! {answer} is absolutely correct! ✨",
    ]
    return random.choice(messages)


def get_answer_too_high_message(answer: int | str) -> str:
    messages: list[str] = [
        f"🎅 Oops! {answer} is too high. Try bringing it down a notch! 🎁",
        f"🌨️ {answer} is a bit too much. Maybe think smaller! ❄️",
        f"🦌 Whoa! You overshot like a reindeer in flight. Lower {answer} a bit! 🦌",
        f"🎄 {answer} is so close, but a tad too high! Let's aim a little lower! 🎄",
        f"❄️ Frosty says {answer} is too big! Cool it down! ❄️",
        f"🎈 {answer} is floating away! Bring it down to earth! 🎈",
        f"🔥 {answer} is a bit too hot! Let's cool it off! 🔥",
        f"🎁 {answer} is a bit much! Think of trimming it down like a holiday tree. 🎄",
        f"🦌 The reindeer are nudging you to aim {answer} a bit lower! 🦌",
        f"🎄 {answer} is almost there! Drop it just a little, like soft snowfall! ❄️",
    ]
    return random.choice(messages)


def get_answer_too_low_message(answer: int | str) -> str:
    messages: list[str] = [
        f"🎅 Hmm, {answer} is too low. Let's raise the stakes! 🎁",
        f"🔥 {answer} is almost there! Try going a bit higher! 🎄",
        f"🦌 Your guess {answer} is under the tree! Look a little higher! 🦌",
        f"🎈 {answer} is not quite enough! Pump up that number! 🎈",
        f"🌟 Shine brighter! {answer} is a bit too low! 🌟",
        f"🎅 {answer} needs a little more cheer, a little higher, and you’ll have it! 🎉",
        f"🎁 {answer} needs to think bigger, like Santa’s toy sack! 🎁",
        f"🦌 Take {answer} up a notch! The sleigh is hovering close! 🛷",
        f"✨ Reach a bit higher for {answer}, like a star on top of the tree! 🎄",
        f"🌱 {answer} is just sprouting! Let's help it grow! 🌱",
        f"🕯️ {answer} is a flicker. Let's brighten it up! 🕯️",
        f"📈 {answer} is below the mark. Aim higher! 📈",
        f"🌤️ {answer} is peeking through. Reach for the sky! 🌤️",
    ]
    return random.choice(messages)


def get_recent_submission_message() -> str:
    messages: list[str] = [
        "🕒 Hold on! You need to wait a bit before submitting again! ⏳",
        "🎅 Patience is a virtue! Try again in a few moments! 🎄",
        "❄️ The elves are processing your last answer. Please wait! ❄️",
        "🎁 Good things come to those who wait! Give it a moment! 🎁",
        "⏰ Time is ticking! Wait a bit before your next attempt! ⏰",
        "🎅 Ho, ho, hold on! Just a few more moments. 🎄",
        "🧝 The elves need a moment to work their magic! 🧝",
        "🎉 Give it a moment; good things come to those who wait! ✨",
        "❄️ Patience! Let the snow settle before trying again. ❄️",
        "🛠️ The workshop is busy. Please wait a moment! 🛠️",
        "🌟 The stars align in a moment. Please wait! 🌟",
        "📨 Message in transit! Give it a second! 📨",
    ]
    return random.choice(messages)


def get_already_completed_message() -> str:
    messages: list[str] = [
        "🎉 You've already completed this part! Great job! 🎉",
        "🌟 Stellar! This part is already shining on your advent calendar! 🌟",
        "🎄 This puzzle piece is already in place! Well done! 🎄",
        "🎁 You've unwrapped this gift already! On to the next one! 🎁",
        "✨ This star is already on your tree! Keep climbing! ✨",
        "🎅 You've already conquered this challenge! Santa salutes you! 🎅",
        "🔥 This one's already warming the fireplace! Next puzzle awaits! 🔥",
        "☑️ Task completed! You're ahead of the sleigh! 🛷",
        "🏆 You've already earned this trophy! Keep it up! 🏆",
        "🚀 You've already launched this rocket! Time for a new adventure! 🚀",
    ]
    return random.choice(messages)


def get_incorrect_answer_message(answer: int | str) -> str:
    messages: list[str] = [
        f"🎅 {answer} is not quite the right answer. Keep trying! 🎄",
        f"❄️ {answer} is not it, but don't give up! The answer is out there! ❄️",
        f"🦌 {answer} is close, but the reindeer think you can do better! 🦌",
        f"🎁 {answer} is incorrect, but every attempt brings you closer! Try again! 🎁",
        f"🔥 The fireplace is warm, but {answer} needs a bit more heat! 🔥",
        f"🎄 {answer} missed the mark, but the holiday spirit is strong! Try again! 🎄",
        f"🕯️ {answer} flickered, but didn't light the way. Keep going! 🕯️",
        f"🍀 {answer} wasn't lucky this time. Give it another shot! 🍀",
        f"🧝 Not quite with {answer}! The elves think you’ll get it with another try! 🎄",
        f"🌟 {answer} didn't shine this time. Reach for the stars again! 🌟",
    ]
    return random.choice(messages)


def get_unexpected_response_message() -> str:
    messages: list[str] = [
        "🤔 Hmm, the elves are puzzled by this response!",
        "🎄 An unexpected twist! Check the website for details!",
        "🌟 Something magical happened! See what's up on Advent of Code!",
        "🎁 Curious! The response is unusual. Time to investigate!",
        "✨ A surprise from Santa! Head over to the website to see!",
        "🧐 The reindeer are scratching their heads. Unexpected response! 🦌",
        "🔮 Mysteries abound! Check the website for more clues! 🔮",
        "🎭 A surprise act! See what's unfolding on Advent of Code! 🎭",
        "📜 The scrolls reveal something unexpected. Take a look online! 📜",
        "🌠 A shooting star! Perhaps a new hint awaits on the website! 🌠",
    ]
    return random.choice(messages)


def get_cached_low_message(answer: int | str, highest_low_guess: Guess) -> str:
    # Format the timestamp to a readable string, e.g., "December 1 at 10:15 AM"
    time_str = highest_low_guess.timestamp.strftime("%B %d at %I:%M %p")
    messages: list[str] = [
        f"🎅 Your guess of {answer} is too low! Previously, you guessed {highest_low_guess.guess} on {time_str}. Let's reach for the stars! 🌟",
        f"🔥 {answer} is still below your highest low of {highest_low_guess.guess} made on {time_str}. Warm it up a bit! 🔥",
        f"🎈 {answer} hasn't lifted past your previous guess of {highest_low_guess.guess} from {time_str}. Aim higher! 🎈",
        f"🌤️ {answer} is under the holiday horizon! Your top low guess was {highest_low_guess.guess} on {time_str}. Keep climbing! 🌤️",
        f"🛷 {answer} is sledding along but hasn't surpassed your earlier {highest_low_guess.guess} (guessed on {time_str}). Push onward! 🛷",
        f"🌱 {answer} is sprouting but hasn't grown past your previous {highest_low_guess.guess} from {time_str}. Reach up! 🌱",
        f"🎁 {answer} is wrapped below {highest_low_guess.guess} (guessed on {time_str}). Unwrap a higher number! 🎁",
        f"🧝‍♂️ The elves note {answer} is still too low compared to your guess of {highest_low_guess.guess} on {time_str}. Elevate your guess! 🧝‍♂️",
        f"✨ {answer} glimmers, but your highest low was {highest_low_guess.guess} (submitted on {time_str}). Shine brighter! ✨",
        f"🚀 {answer} hasn't launched past your earlier guess of {highest_low_guess.guess} from {time_str}. Boost it up! 🚀",
    ]
    return random.choice(messages)


def get_cached_high_message(answer: int | str, lowest_high_guess: Guess) -> str:
    # Format the timestamp to a readable string
    time_str = lowest_high_guess.timestamp.strftime("%B %d at %I:%M %p")
    messages: list[str] = [
        f"🎅 Oops! {answer} is too high! Previously, you guessed {lowest_high_guess.guess} on {time_str}. Let's bring it down! 🎁",
        f"❄️ {answer} is above your lowest high of {lowest_high_guess.guess} made on {time_str}. Cool it off a bit! ❄️",
        f"🦌 {answer} is soaring higher than before! Your lowest high was {lowest_high_guess.guess} on {time_str}. Descend slightly! 🦌",
        f"🎄 {answer} climbs above the treetop! Remember, your smallest high guess was {lowest_high_guess.guess} (guessed on {time_str}). Try lower! 🎄",
        f"🌙 {answer} reaches the moon, but your lowest high was {lowest_high_guess.guess} on {time_str}. Bring it back down! 🌙",
        f"🎈 {answer} floats above your previous high of {lowest_high_guess.guess} from {time_str}. Let some air out! 🎈",
        f"🏔️ {answer} peaks higher than {lowest_high_guess.guess} (submitted on {time_str}). Let's hike down a bit! 🏔️",
        f"🔔 {answer} rings higher than the bells! Your lowest high was {lowest_high_guess.guess} on {time_str}. Tone it down! 🔔",
        f"🌟 {answer} shines above your lowest high of {lowest_high_guess.guess} (from {time_str}). Dim it slightly! 🌟",
        f"🕊️ {answer} flies over your prior high guess of {lowest_high_guess.guess} made on {time_str}. Glide lower! 🕊️",
    ]
    return random.choice(messages)


def get_cached_duplicate_message(answer: int | str, previous_guess: Guess) -> str:
    # Format the timestamp to a readable string
    time_str = previous_guess.timestamp.strftime("%B %d at %I:%M %p")
    messages: list[str] = [
        f"🎅 You've already tried {answer} on {time_str}! Let's think of a new number! 🎁",
        f"🔄 {answer} again? You guessed this before on {time_str}! Try a different number! 🔄",
        f"🎄 Déjà vu! {answer} was submitted on {time_str}. Let's pick another! 🎄",
        f"🧝 The elves remind you that {answer} was already guessed on {time_str}. Think anew! 🧝",
        f"✨ You've already sprinkled {answer} into the mix on {time_str}! Try another magic number! ✨",
        f"📜 {answer} is on the scroll of previous guesses (from {time_str})! Choose a new one! 📜",
        f"🔔 {answer}? That bell rang on {time_str}! Select a new tone! 🔔",
        f"🕹️ {answer} was played before on {time_str}! Insert a new coin and try again! 🕹️",
        f"🌟 {answer} has already shined on {time_str}! Find a new star! 🌟",
        f"🎁 Oops! {answer} is a repeat gift from {time_str}! Unwrap a different one! 🎁",
    ]
    return random.choice(messages)
