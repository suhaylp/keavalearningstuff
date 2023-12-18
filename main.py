user_name = input("Enter your name: ")
print("Hi " + user_name)
print("Today you will be conducting an orchestra. This orchestra will consist of several instruments. \n"
      "When you want to  play a certain instrument, all that is required is to write the name of the instrument.\n"
      "The instruments will include a piano, harp, violin, flute, and a cello. To end the game write 'disband "
      "orchestra'\n" )

instrument_choice = input("Instrument of Choice: \n")

# We want to make this repeating next time
if instrument_choice == "piano":
    print( "You have chosen to possess a piano in your orchestra!")

elif instrument_choice == "harp":
    print("You have chosen to possess a harp in your orchestra!")
elif instrument_choice == "violin":
    print("You have chosen to possess a violin in your orchestra!")
elif instrument_choice == "flute":
    print("You have chosen to possess a flute in your orchestra!")
elif instrument_choice == "cello":
    print("You have chosen to possess a cello in your orchestra!")
else:
    print("Oopsie daisy, " + instrument_choice + " is not available in your orchestra. "
          "Please try again, and pick an instrument listed above.")

