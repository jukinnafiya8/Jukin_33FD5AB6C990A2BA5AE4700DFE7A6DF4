# Define the  base class Player
class Player:
 def Play(self):
    print("The player is playing cricket.") 
# Define the derived class batsman
class Batsman(Player):
 def play(self):
   print("The batsman is batting.")
# Define the derived class from bowler  
class Bowler(Player):
  def play(self):
   print("The bowler is bowling.")
# Create object of batsman and bowler classes
batsman = Batsman() 
bowler = Bowler() 
#call the play () method for each object
batsman.play()
bowler.play()