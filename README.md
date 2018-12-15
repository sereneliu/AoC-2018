# Advent of Code 2018

## Day 1

Finished Part 1 within minutes. My first solution for Part 2 did not take long to figure out either, but incredibly slow.

    real    1m8.664s
    user    1m8.428s
    sys     0m0.032s

Moving on to Day 2 for now, but will definitely come back to optimize this second part.

After my friend [Daniel](https://github.com/ephemient) sent me [this link](https://www.reddit.com/comments/a2ajyv) a couple of minutes later...

Apparently simply changing my list to a set in Python speeds it up a lot. I learn something new everyday.

    real    0m0.116s
    user    0m0.104s
    sys     0m0.008s

## Day 2

Nothing really new here. Although, one thing I'm using this year that I didn't use last year is `break`. Never really used them before until I started playing [7 Billion Humans](https://tomorrowcorporation.com/7billionhumans).

## Day 3

3 days worth of puzzles in one day! In general, I would like to start these puzzles at midnight when they are released unless I need to sleep early or something. It's not like I think I will ever make the leaderboard, but no harm in trying to see how fast I can compete these puzzles, right? 

I'm definitely solving these much faster than last year. Before, I always came up with the solution using the example input before using my actual puzzle input. This is because I wrote print statements after every line of code I wrote just to check that my code was actually doing what I want it to. Example input is always a lot shorter so it's easier to see when I make mistakes. Now, I have a much better understanding of what my code is doing and I can skip most of this. Only need to check when I don't get the right answer at the end. Soon, I would like to get to the point where I am writing asserts instead of print statements to check my work.

## Day 4

I spent a little under 2 hours solving day 4, most of it spent on part 1. I was mostly focused on getting it done with intent to make it better the next day after more sleep. I kept thinking that my solution, while it works, was pretty terrible because I felt like I could have done it in much less code. Daniel looked at it the next morning and offered [these changes](https://github.com/ephemient/AoC-2018/blob/patch-1/day4.py), which mostly kept my structure but made more Pythonic. So much to learn from here! I vaguely remember D teaching me defaultdict last AoC but because I haven't really used it in a year, I forgot about it. What Counter can do is pretty cool. Also, looking at my code again the next day, it's not actually as much code as I remembered. I recognize that I get imposter syndrome a lot due to the fact that I never learned this stuff formally and I should stop thinking that I barely know anything (while keeping in mind that there IS a ton more to learn).

## Day 5

This day's puzzle was particularly frustrating. It didn't take me long to figure 90% of the code of each part, but took significantly longer to tweak the other 10% to actually make it work. Then my original solution took SO long. The next morning, I used inspiration from Part 2 to rewrite Part 1 so that I can get my solutions much quicker than before, but still super slow. Gotta keep thinking. D did offer me a solution, but I don't want to use his, obviously. I want to see if I can come up with one on my own that will achieve the same results.

Part 1 v1

    real    1m13.034s
    user    1m12.384s
    sys     0m0.100s

Part 2 v1 - I called it quits after waiting for over half an hour, but I assume it's around the time it takes to do Part 1 x 26.

Part 1 v2

    real    0m2.825s
    user    0m2.808s
    sys     0m0.012s

Part 2 v2

    real    1m17.145s
    user    1m16.908s
    sys     0m0.060s

## Days 6 - 10

Went on a ski trip. Will come back to these later.

## Day 11

Since I use an [online IDE](https://c9.io), I just kept it running until I got an answer to part 2. I don't know exactly how long it took, but I discovered it finished three days later...

## Day 12

Once Daniel sent me a wiki article about [elementary cellular automaton](https://en.wikipedia.org/wiki/Elementary_cellular_automaton), I assumed that my puzzle will eventually reach a stable pattern and was able to solve part 2 using this assumption. I do recognize that the pattern could stay random BUT I figured that the puzzle maker wouldn't do this. I didn't actually finish coding my solution and got my answer before midnight using a bit of math. Will come back to actually code the end.

## Day 13

## Day 14

I misread the instructions and tried to do part 2 for part 1. Took awhile before I fully understood what part 1 was actually asking for. On the other hand, that meant that it didn't take me very long to do part 2 the brute force way. I'm not very good at the "make it fast" stage. Have so much that I need to learn.
