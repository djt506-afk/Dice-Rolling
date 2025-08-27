import statistics  # this is the statistics library.
# in my code it is used in the analysis function to calculate the mean, median, mode and deviation
from random import randint  # this is importing randint form the random library.
# function is crucial for my code in producing the results for the dice rolls
# as it produce a random intger based upon a given range simulating a dice roll.

import \
    matplotlib.pyplot as plt  # This import matplotlib library which is used to create ther histogram plots for my code
import seaborn as sn  # This import seaborn library which is used to create ther kde plots for my code

examples = [{"dice": [4, 6, 10], "plot type": "Histogram", "rolls": 50000},
            {"dice": [6, 8], "plot type": "KDE plot", "rolls": 10000},
            {"dice": [6, 6], "plot type": "Analysis", "rolls": 1000}
            ]


# this is a list of dictionaries which stores all the information to load examples


# for the dictionaries "dice" is a list of the number of sides each dice have. from this the number of dice can also be found
# "plot type" signifies the type of plot. this is used so the correct function for each example can be called.
# "rolls" refers to the number of times each dice is rolled in that particular example

class Dice():  # This is the dice class. For each dice inputted by the user an object based on this class is created.
    def __init__(self, sides=6):  # the class is intialised assuming the default sides of the dice is 6
        self.sides = sides  # this attribute refers to the number of sides of the dice
        self.results = []  # this attribute stores the results of the "roll" method and is appened to each time the roll method is run

    def roll(self):
        self.results.append(randint(1, self.sides))  # this method appends a random integer to the results attribute
    # it returns a random integer based on the range of values on the dice


def main():  # this is the main function which essentially runs the main menu for the program and acts as the hub between other functions
    # This is the first function called by the program and the last
    print(
        "This program is designed to analyse and simulate rolling dice and displaying the data using 3 diferent methods")

    print("\nWhen a plot has been produced in order to return to menu")
    print("the plot must be closed by pressing the exit box in the top right corner of the plot window")
    while (
            True):  # this while loop is used to keep returning back to the main menu only until the user enters 5 and the loop is broken
        # by using this it means once one of the features has been performed it brings the user back to the menu to perform anpother feature
        userinput = getint(
            "enter 1 to create histogram,\nenter 2 to create kde plot,\nenter 3 to print out analysis,\nenter 4 to run example,\n5 to exit program\n")
        # this line above calls the getint function. The user will receive the above string as a prompt to choose what option the wish to perform
        # the returned value from get int function is stored as the variable called userinput.

        if 1 <= int(userinput) <= 3:
            dice_results = rawdata()  # dice results is a list which will hold all of the data being plotted or analysed
            # this if statement above check to see if the user entered an integer between 1 and 3
            # if satified the code will create a variable called dice_results and set it to return of rawdata
            # the purpose of this if statement is so the raw data function is only called for histogram, kde plot and analysis options
            if userinput == 1:
                # this if statment check if the userinput is 1 (the user selected to make a histogram)

                plothist(dice_results,
                         input("if you wish to save jpeg of plot enter desired file name otherwise leave blank"))
                # the line above calls the plohist function in which dice_results is passed through and also a user inputted file name
                # for plothist if the filename is left blank no file is created or written to
                print("in order to return back to menu click the exit box in the top right of the plot window")
            # this print statement above lets the user know in order to return to the menu they must clost the window of the plot

            elif userinput == 2:
                # this elif statment check if the userinput is 2 (the user selected to make a kde plot)

                plotkde(dice_results,
                        input("if you wish to save jpeg of plot enter desired file name otherwise leave blank"))
                print("in order to return back to menu click the exit box in the top right of the plot window")
            # the lines above calls the plokde function in which dice_results is passed through and also a user inputted file name
            # for plotkde if the filename is left blank no file is created or written to

            elif userinput == 3:
                print(analysis(dice_results,
                               input("if you wish to save data to file enter desired file name otherwise leave blank")))
                # if the user enter 3 (print analysis of the dice rolling the code will call and print the result of the analysis function

        elif userinput == 4:

            example(examples)
            # if the user enter 4 (run examples) the if statement is staified and  it calls the example function with examples passed through
            # examples if the list of dictionaries that hold all the information for each of the 3 examples
        elif userinput == 5:
            break  # if the user enters 5 they want to exit the program. this break will force the while loop to end
        else:
            print("you have entered an invalid input make sure input between numbers 1 to 5")
            # if the user enters a charecter not listed in the menu it will print a message and will loop back to the start of the while loop


def getint(
        prompt):  # this function essentially is used to give a prompt to the user. the prompt displayed is the argument passed through the funciton
    # the code will then accept an input from user and check that the input is valid and return the input
    while True:

        try:
            inputvalue = int(input(prompt))
            if inputvalue > 0:
                return (inputvalue)
            else:
                print("must be a positive and non zero integer")


        except ValueError:
            print("you have entered an invalid input enter an integer")
            pass


# the code above uses try and excpet to handle any invalid user inputs.
# the while loop will keep the code asking for input until the user enters a valid integer greater than 0

def rawdata():  # this function is where the raw data is collected. the user is propmted to give the number of dice and the number of rolls
    # then it calls the dice_roll function where is returns an array for the results (raw data) the user can then chose to save this data
    # to a file. the list of results is then returned.
    dicenumber = getint("enter number of dice")
    numberofrolls = getint(
        "enter number of rolls")  # to get input for the number of dice and number rolls the get int function is called twice
    dice_results = dice_roll(dicenumber, numberofrolls)
    # the line above calls the dice_roll function with the number of dice and number of rolls fed thorugh
    # the dice_roll funciton will return a list of the results from rolling and summing the dice
    filename = input("if you wish to save raw data to file enter desired file name otherwise leave blank")
    if filename:
        filename = filename.replace(' ',
                                    '_') + ".txt"  # this line will replace any spaces with a valid underscrore and will add .txt to end to make valid file name
        with open(filename, "w") as output:
            output.write(str(dice_results))
    # if the user enters a file name it will open a file of that name and write the list of dice date to it (dice_results)
    return (dice_results)


def result(dice1,
           numberofrolls):  # this function produces the result of rolling a single dice the number of times the user requires
    for i in range(numberofrolls):
        dice1.roll()  # this for loop will run the roll function for the dice object the number of rolls inputed by the user

    return (dice1.results)  # this line retursn the results attribute of the dice object


def plothist(dice_results,
             jpeg):  # this function takes in the data produced from rolling dice and produces a histogram based on the data

    plt.hist(dice_results, len(set(dice_results)), histtype='bar', facecolor='red')
    # this line uses the matplotlib method hist to create a histogram based upon dice_results list
    # the number of bins(bars) needed is calculated by finding the number of unique values produced
    # this is done  using len(set(dice_results)).
    plt.rwidth = 0
    plt.title("Dice Plot")
    plt.xlabel("Results")
    plt.ylabel("Frequency of Result")
    # these lines above set the tile and x and y labels for the histogram
    if jpeg:
        jpeg = jpeg.replace(' ', '_') + ".jpg"
        plt.savefig(jpeg)
    # if the user choses to enter a filename for jpeg in the main function it will save the histogram as a jpeg

    plt.show()  # displays the histogram


def plotkde(dice_results,
            jpeg):  # this function takes in the data produced from rolling dice and produces a KDE plot based on the data
    res = sn.kdeplot(dice_results, bw_adjust=1.3)  # this line use kdeplot from seaborn library
    # will produce what is known as a Kernel Distribution Estimation Plot
    if jpeg:
        jpeg = jpeg.replace(' ', '_') + ".jpg"
        plt.savefig(jpeg)
    plt.show()  # this line uses .show() to display a window with the kde plot


def analysis(dice_results, filename):  # this funciton features heavy use of the statistics library
    # the function takes in the data produced from the dice rolling and returns the mean, median, mode, maximum, minimum and deviation
    mean = statistics.mean(dice_results)
    median = statistics.median(dice_results)
    mode = statistics.multimode(dice_results)
    maximum = max(dice_results)
    minimum = min(dice_results)
    deviation = statistics.stdev(dice_results)
    full_result = "Mean:" + str(round(mean, 2)) + "\n" + "Median:" + str(median) + "\n" + "Mode:" + str(
        mode) + "\n" + "Maximum:" + str(maximum) + "\n" + "Minimum:" + str(minimum) + "\n" + "Deviation:" + str(
        round(deviation,
              2)) + "\n"  # this is where the entire analysis result is store and put into the correct and readable format
    if filename:
        filename = filename.replace(' ', '_') + ".txt"
        with open(filename, "w") as output:
            output.write(
                full_result)  # if the user enters a filename and this code upbove will run creating a file based on their input

    return (full_result)  # the fucntion then retursn the entire analysis result at the end


def dice_roll(dicenumber,
              numberofrolls):  ## this function takes the in the number of dice and rolls and produces the list of data from adding the values of each dice for each roll
    dice_results = []  # this is the list used to store the data from rolling and summing the values on the dice
    for i in range(dicenumber):  # this for loop will repeat based upon the number of dice required to roll
        print("enter number of sides for dice", i + 1)  # for each dice the user can enter the desired number of sides

        die = Dice(getint(" "))  # this creates a new instance of the class and uses getint fucntion
        # this will allow the user to enter their desired number of side for the dice object
        # dice.append(die)
        if not dice_results:
            dice_results.extend(result(die, numberofrolls))
        # if the dice_results list is empty the result function is ran using the die object and the number of rolls required
        # this will add the data for rolling the first dice the number of times required by the user to the list

        else:

            dice_results2 = result(die, numberofrolls)  # temporary list used to store data to be added to dice_results

            dice_results = [x + y for x, y in zip(dice_results, dice_results2)]
        # for the data created by any subsequent dice the code uses zip to add each value of one list to each value of dice_results
        # this sums up the value of the dice for each roll

    return (dice_results)  # the dice_results list is returend at the end of the function


def example(
        examples):  # function takes in the list of dictionaries called examples and produces either histogram, kde or analysis
    # by calling thier respective funcitons
    example_results = []  # This list is used to store the example data produced
    while True:
        try:
            n = getint("enter example number 1 to 3") - 1  # this line uses getint to take in an input of an integer
            # the integer entered by the user is reduced by 1 and stored as the variable "n"

            for i in examples[n]["dice"]:
                die = Dice(int(i))
                # this for loop creates a dice object based on the dice given in examples list of dictionaries

                if not example_results:
                    example_results.extend(result(die, examples[n]["rolls"]))

                else:

                    dice_results2 = result(die, examples[n]["rolls"])

                    example_results = [x + y for x, y in zip(example_results, dice_results2)]
                # the if an else staement above add the results of roolling each dice together and form a singla

            if examples[n]["plot type"] == "Histogram":

                print("Histogram for D4 + D6 + D10 rolled 50000 times")
                plothist(example_results, "")
            elif examples[n]["plot type"] == "KDE plot":
                print("KDE plot for D6 + D8 rolled 10000 times")
                plotkde(example_results, "")
            elif examples[n]["plot type"] == "Analysis":
                print("analysis for D6 + D6 rolled 1000 times")
                print(analysis(example_results, ""))

            break
            # these if and elif statments above display which example is being run to the user and calls
            # plothist, plotkde and analysis

        except IndexError:
            print("you must enter an integer between 1 and 3")
            pass
        # if the user enters a value which is outside the number of examples avaible it will print a prompt
        # and will allow the user to enter agian until a valid input is received.


if __name__ == "__main__":
    main()
