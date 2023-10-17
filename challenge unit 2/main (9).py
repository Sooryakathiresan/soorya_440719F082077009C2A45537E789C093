# Implement a class called player that represents a cricket players. The player class shoud have a method called play() which prints the player is plaing cricket. Derive two classes,Batsman and Bowler, from the player class,Override the play() method in ech derived class to print "The batsman is batting" and "The bowler is bowling", respectiely.Write a program to create a objects of both the Batsman and Bowler classes and call the play) method for each object.
#define the base class player
class player:
    def play(self):
        print("The player is playing cricket.")
#define the derived class Batsman
class Batsman(player):
    def play(self):
        print("The batsman is batting.")
#define the derived class Bowler
class Bowler(player):
    def play(self):
        print("The bowler is bowling.")
#crete objects of Batsman ad Bowler classes
batsman =Batsman()
bowler =Bowler()
#call the play() mthod for each object
batsman.play()
bowler.play()