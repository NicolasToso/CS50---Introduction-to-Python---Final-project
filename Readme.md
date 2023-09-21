# Final Project CS50 - introduction to Pyhton:  "Place Finder"
#### Video Demo:  <https://youtu.be/HYaTR-Gu5Bk>
#### Description:
This program searches for places registered in Google Maps according to an address and a category entered by the user. It also allows you to save the records, and then display or delete them.

## What does the project folder contain?
    project.py --> Program file
    test_project.py --> Test file
    query_log.txt --> Where the records will be kept
    reguirements.txt --> Necessary libraries

In the libraries folder are all the installed packages necessary to run the program. 
For example: 
* Googlemaps
* Keyboard
* Requests
* Tabulate
* PyFiglet

## What does project.py do precisely?
The program displays a menu with 4 options on the screen. 
* Search places 
* View stored places 
* Erase log 
* Exit
  
You must choose by entering the corresponding number.

### Searching Places

To search for a place it is necessary to enter a reference address and the category.

The address can sometimes be found just by entering the street name and number. But if it was not found, you can add more details such as the district or state. The program will ask if the address it found is the one it is looking for.

The category refers to the type of place you are looking for, for example, bank, market, pet store.

Once the address is accepted and the category is entered, the program will show a table with the first 5 results according to their qualification and their respective locations.

Finally, it will ask if you want to save any of the results found.

### View Log

This option will show the results that were saved in the registry (name and address)

### Erase Log

Here, you can delete all saved queries from the registry. Don't worry, the program will ask you again to confirm your decision.


## Functions

**Project.py** is composed of 10 functions:

``main()``:
* Shows the menu with options
* Keyboard entry of the option, address and category to search is requested.
* Depending on the option entered, calls the other functions
* Print the search results in a table
* Show stored results
* Return = *__None__*

``format_address(address)``:
* Open the GoogleMaps API service with a user key
* Request the API for the coordinates that correspond to the entered address (using the `maps.reverse_geocode` method). 
* Request the API for the complete address using the coordinates obtained
* Returns the coordinates and full address
* Return = *__complete_direction, lat_len__*

``check_address(dir)``:
* Shows the complete address obtained by GoogleMaps
* Asks the user if it corresponds to their search
* Return = *__str(response)__*


``Map_requests(address , category)``:
* Initializes the GoogleMaps API with a user key
* Request nearby places (using the `maps.places` method) at the address entered by the user
* Return = *__results[ ]__*

`results(result_list)`:
* Takes as argument a list of lists, composed of the search results
* Extracts the first 5 results and saves them in a temporary table
* Return = *__table[ ]__*

`save_result(table)`:
* Takes the saved temporary table as an argument
* Ask the user if they want to save any records
* Creates a *.txt* file where it stores the saved records
* Return = *__None__*

`print_log()`:
* Open saved file
* Prints all saved records on the screen.

`erase_log()`:
* Clean the log by deleting all records.
* Return = *__None__*


`wait_and_clean()`:
* Clear the terminal after 1 second
* Return = *__None__*
  
`esc_and_clean()`:
* The program does not continue until the "Esc" key is pressed. This allows the user to view the logs for as long as they prefer without the terminal being cleaned.
* Clear the terminal
* Return = *__None__*


## The Process

### The Idea

This is where I have to give credit for this to my wife. 

Talking about what my project would be about, she was the one who gave me a similar idea, which worked as a trigger for the final idea.

### The Design

At first I wanted it to be as close to a current program as possible, that is, intuitive and visually pleasing.

That is why, in addition to the menu with options, I included cleaning the terminal once what the user wanted to do had finished executing.

As far as code is concerned, I tried to separate into functions what I could execute in a block to make it easier to develop and correct errors.

### The Challenges

The first challenge I had to face was how to manipulate the information that the GoogleMaps API would give me.

I had to read a lot of documentation and do a lot of tests to understand it. The results returned by the API are lists of lists, so I had to figure out which part of those lists is what I needed.

I also had difficulty getting the search to be accurate and not return incorrect results. That is why I created a function that would obtain the geolocation data according to what the user enters on the screen and another function that, depending on the latitude and longitude, will find the address and place and then consult with the user if it matches what they entered.

I also had to investigate how to use a timeout so that the error messages in the main menu would disappear and the clean menu would show again. Likewise, look for documentation on how to capture keyboard keys, where I found the *Keyboard* package.

With the rest of the code I had no other difficulties, other than the usability of the program, that it displays the messages correctly and that they look good visually.

## Final message

First of all, I would like to greatly thank everyone who was involved in carrying out this Python course.

I would like to especially thank and congratulate to David Malan for his teaching skills and for making this introductory course really interesting, push me to want to learn even more.
I am extremely happy with everything he has taught me and I have learned. I can't believe what I'm capable of after a month.