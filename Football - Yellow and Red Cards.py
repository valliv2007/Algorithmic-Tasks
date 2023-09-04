"""Most football fans love it for the goals and excitement. Well, this Kata doesn't. You are to handle 
the referee's little notebook and count the players who were sent off for fouls and misbehavior.

The rules: Two teams, named "A" and "B" have 11 players each; players on each team are numbered from 1 to 11. 
Any player may be sent off the field by being given a red card. A player can also receive a yellow warning card, 
which is fine, but if he receives another yellow card, he is sent off immediately (no need for a red card in that case). 
If one of the teams has less than 7 players remaining, the game is stopped immediately by the referee, 
and the team with less than 7 players loses.

A card is a string with the team's letter ('A' or 'B'), player's number, and card's color ('Y' or 'R') - 
all concatenated and capitalized. e.g the card 'B7Y' means player #7 from team B received a yellow card.

The task: Given a list of cards (could be empty), return the number of remaining players on each team 
t the end of the game (as a tuple of 2 integers, team "A" first). If the game was terminated by the referee
 for insufficient number of players, you are to stop the game immediately, and ignore any further possible cards.

Note for the random tests: If a player that has already been sent off receives another card - ignore it."""


def men_still_standing(cards):
    # your code
    new_cards = []
    for value in cards:
        new_cards.append((value[0], value[1:-1], value[-1]))
    full_team = 11
    A = [0] * full_team
    B = [0] * full_team
    a_final = []
    b_final = []
    count_a = full_team
    count_b = full_team
    for value in new_cards:
        if value[0] == 'A':
            if A[int(value[1])-1] < 2:
                if value[2] == 'R':
                    A[int(value[1])-1] += 2
                else:
                    A[int(value[1])-1] += 1
                if A[int(value[1])-1] >= 2:
                    count_a -= 1
                if count_a == 6:
                    break

        if value[0] == 'B':
            if B[int(value[1])-1] < 2:
                if value[2] == 'R':
                    B[int(value[1])-1] += 2
                else:
                    B[int(value[1])-1] += 1
                if B[int(value[1])-1] >= 2:
                    count_b -= 1
                if count_b == 6:
                    break
    for player in A:
        if player < 2:
            a_final.append(player)
    for player in B:
        if player < 2:
            b_final.append(player)

    return (len(a_final), len(b_final))


print(men_still_standing(["A4R", "A6R", "A8R", "A10R", "A11R", "A5R", "B8R"]))