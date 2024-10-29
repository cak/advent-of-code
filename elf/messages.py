import random

# 🎄 Elf Message Generator 🎄 #


def get_positive_message() -> str:
    messages: list[str] = [
        "🎉 Hooray! That's the right answer! The elves are cheering! 🎉",
        "🎄 Wonderful! You've cracked it! Santa is impressed! 🎄",
        "✨ Brilliant! You've found the solution! Onward to more puzzles! ✨",
        "🎁 Fantastic! The gift of knowledge is yours! Keep it up! 🎁",
        "🌟 Excellent work! You're lighting up the advent sky! 🌟",
        "☃️ Marvelous! Your answer melts all the snowmen with joy! ☃️",
        "🍪 Sweet success! You've earned a cookie from Mrs. Claus! 🍪",
        "🧝 The elves are singing your praises! Great job! 🧝",
        "🔔 Ding dong! Your answer rings true! 🔔",
        "🎊 Jolly good! Your code is as bright as Rudolph's nose! 🎊",
        "🎅 Santa’s proud! Your answer shines brighter than a Christmas star! 🌟",
        "🎄 Splendid! You’ve solved it with holiday spirit to spare! 🎄",
        "🍬 Candy cane celebration! You’ve cracked the code! 🍬",
        "🎁 Every elf is clapping for you! A true coding gift! 🎁",
        "🎉 Superb! Your code is spreading holiday cheer everywhere! 🎉",
    ]
    return random.choice(messages)


def get_negative_message() -> str:
    messages: list[str] = [
        "🤔 Hmm, the elves are scratching their heads in confusion!",
        "🎄 Oops! The Christmas lights got tangled. Let's untangle that code!",
        "🌨️ Oh no! A blizzard of bugs! Time to shovel them out!",
        "🎅 Not quite the right answer. Keep trying!",
        "🦌 The reindeer suggest taking another look!",
        "🍭 Sticky situation! A candy cane error perhaps?",
        "🎁 The gift didn't unwrap as expected. Try again!",
        "✨ Almost there! Sprinkle some more magic dust on your code!",
        "❄️ Frosty says your answer is a bit chilly. Warm it up!",
        "🌟 Shoot for the stars! You'll get it next time!",
        "🎅 Not quite, but Santa believes you’ll get it next time! 🎄",
        "🍪 A sprinkle of holiday magic might just do the trick! Keep going! ✨",
        "🎁 It’s okay! The elves are tinkering with ideas to help! 🎁",
        "🎄 Oops, this answer needs a bit more holiday sparkle! 🎄",
        "❄️ Frosty suggests re-checking your work. Snow problem! ☃️",
    ]
    return random.choice(messages)


def get_correct_answer_message() -> str:
    messages: list[str] = [
        "🎉 Correct! The sleigh is ready to fly! 🎉",
        "🎄 Ho ho ho! Santa approves your answer! 🎄",
        "✨ Sparkling success! You've got the right answer! ✨",
        "🎁 Perfect! You've unwrapped the correct solution! 🎁",
        "🌟 Bravo! Your answer shines brightly on the tree! 🌟",
    ]
    return random.choice(messages)


def get_answer_too_high_message() -> str:
    messages: list[str] = [
        "🎅 Oops! Your answer is too high. Try bringing it down a notch! 🎁",
        "🌨️ That's a bit too much. Maybe think smaller! ❄️",
        "🦌 Whoa! You overshot like a reindeer in flight. Lower it a bit! 🦌",
        "🎄 So close, but a tad too high! Let's aim a little lower! 🎄",
        "❄️ Frosty says your number is too big! Cool it down! ❄️",
        "🎅 Whoa, that’s high! Try bringing it down like a snowflake! ❄️",
        "🎁 It’s a bit much! Think of trimming it down like a holiday tree. 🎄",
        "🦌 The reindeer are nudging you to aim a bit lower! 🦌",
        "🎄 Almost there! Drop it just a little, like soft snowfall! ❄️",
    ]
    return random.choice(messages)


def get_answer_too_low_message() -> str:
    messages: list[str] = [
        "🎅 Hmm, your answer is too low. Let's raise the stakes! 🎁",
        "🔥 Almost there! Try going a bit higher! 🎄",
        "🦌 Your guess is under the tree! Look a little higher! 🦌",
        "🎈 Not quite enough! Pump up that number! 🎈",
        "🌟 Shine brighter! Your answer is a bit too low! 🌟",
        "🎅 A little more cheer, a little higher, and you’ll have it! 🎉",
        "🎁 Think bigger, like Santa’s toy sack! 🎁",
        "🦌 Take it up a notch! The sleigh is hovering close! 🛷",
        "✨ Reach a bit higher, like a star on top of the tree! 🎄",
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
        "⏰ The elves are still wrapping your last answer. Wait a bit! 🎁",
        "🎉 Give it a moment; good things come to those who wait! ✨",
        "❄️ Patience! Let the snow settle before trying again. ❄️",
    ]
    return random.choice(messages)


def get_already_completed_message() -> str:
    messages: list[str] = [
        "🎉 You've already completed this part! Great job! 🎉",
        "🌟 Stellar! This part is already shining on your advent calendar! 🌟",
        "🎄 This puzzle piece is already in place! Well done! 🎄",
        "🎁 You've unwrapped this gift already! On to the next one! 🎁",
        "✨ This star is already on your tree! Keep climbing! ✨",
        "🎉 This one’s already in the bag! Santa’s impressed! 🎅",
        "🌟 Great job! This part’s shining on your advent calendar! 🌟",
        "🎄 You’ve already lit up this part! On to the next! 🎄",
        "🎁 Bravo! This gift’s already unwrapped! Keep going! 🎁",
    ]
    return random.choice(messages)


def get_incorrect_answer_message() -> str:
    messages: list[str] = [
        "🎅 Not quite the right answer. Keep trying! 🎄",
        "❄️ That's not it, but don't give up! The answer is out there! ❄️",
        "🦌 Close, but the reindeer think you can do better! 🦌",
        "🎁 Incorrect, but every attempt brings you closer! Try again! 🎁",
        "🔥 The fireplace is warm, but your answer needs a bit more heat! 🔥",
        "🎅 Santa’s workshop needs a bit more magic for this one! Keep trying! 🎄",
        "❄️ Frosty’s sure you’re close—keep that holiday spirit up! ☃️",
        "🧝 Not quite! The elves think you’ll get it with another try! 🎄",
        "🔥 Almost there! The holiday hearth is warming up with every try! 🔥",
    ]
    return random.choice(messages)


def get_unexpected_response_message() -> str:
    messages: list[str] = [
        "🤔 Hmm, the elves are puzzled by this response!",
        "🎄 An unexpected twist! Check the website for details!",
        "🌟 Something magical happened! See what's up on Advent of Code!",
        "🎁 Curious! The response is unusual. Time to investigate!",
        "✨ A surprise from Santa! Head over to the website to see!",
    ]
    return random.choice(messages)


def get_timer_message() -> str:
    messages: list[str] = [
        "The elves are swift! 🏃‍♂️",
        "Santa’s sleigh couldn’t be faster! 🎅💨",
        "The code is wrapped and delivered! 🎁✨",
        "The reindeer are on a roll! 🦌💨",
        "It’s snow time! ❄️⏱️",
        "A twinkling performance! 🌟",
        "Rudolph’s nose isn’t the only thing shining! 💡🎄",
        "The North Pole approves of this speed! 🧊💨",
        "Sleighing those function times! 🛷",
        "Just in time to deck the halls! 🎄",
        "That’s holiday efficiency! 🎅🎉",
    ]
    return random.choice(messages)
