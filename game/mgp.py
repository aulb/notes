from collections import Counter

FIRST_PLACE = 0
SECOND_PLACE = 1
THIRD_PLACE = 2

POINTS = {
  FIRST_PLACE: 15,
  SECOND_PLACE: 10,
  THIRD_PLACE: 5, 
}

def get_sorted_standing(score):
  standing = []
  for name in score:
    standing.append([name, score[name]])
  standing.sort(key=lambda x: -x[1])
  return standing

def get_season_score(rankings):
  total_score = Counter()
  for ranking in rankings:
    for index, name in enumerate(ranking):
      if index == FIRST_PLACE:
        total_score[name] += POINTS[FIRST_PLACE]
      elif index == SECOND_PLACE:
        total_score[name] += POINTS[SECOND_PLACE]
      elif index == THIRD_PLACE:
        total_score[name] += POINTS[THIRD_PLACE]
    print(get_sorted_standing(total_score))
  return total_score

if __name__ == "__main__":
  test = [
    ["A", "B", "C", "D", "E"],  
    ["E", "B", "D", "C", "A"],  
    ["D", "A", "C", "B", "E"],  
    ["C", "E", "D", "A", "B"],  
    ["E", "C", "D", "A", "B"],  
    ["E", "C", "B", "D", "A"],  
    ["E", "C", "B", "A", "D"],  
    ["E", "D", "A", "B", "C"],  
    ["A", "E", "D", "C", "B"],  
    ["E", "C", "B", "A", "D"],  
  ]
  print(get_season_score(test))