###pose
import random

pose = []
action = ("dancing", "posing", "walking", "strolling", "sitting", "laying down", "smooching", "hugging", "looking at viewer", "looking away", "looking back", "backwiew")

maxr = 11
roll = random.randint(0,maxr)
pose.append(action[roll])
#print(' '.join(pose))