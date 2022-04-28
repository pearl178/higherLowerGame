
import random
import game_data
import art
src = game_data.data
end_game = False
a_dic = random.choice(src)
score = 0
print(art.logo)
while not end_game:
  b_dic = random.choice(src)
  # make sure the 2 choices are different
  while a_dic == b_dic:
    b_dic = random.choice(src)
  print(f"Compare A: {a_dic['name']}, a {a_dic['description']}, from {a_dic['country']} ")
  print(art.vs)
  print(f"Against B:{b_dic['name']}, a {b_dic['description']}, from {b_dic['country']}")
  answer = input("Who has more followers? Type 'A' or 'B': ").lower()
  #replit.clear()
  a_follower = a_dic['follower_count']
  b_follower = b_dic['follower_count']
  
  if a_follower>b_follower:
    if answer == 'a':
      correct = True
    else:
      correct = False
  if a_follower<b_follower:
    if answer == 'b':
      correct = True
      a_dic = b_dic
    else:
      correct = False
  if correct:
    score += 1
    print(f"You're right! Current score:{score}")
  else:
    print(f"Sorry,that's wrong. Final score:{score}")
    end_game = True
