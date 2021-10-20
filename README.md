<img src="https://bit.ly/2VnXWr2" alt="Ironhack Logo" width="100"/>

# Title of Your Project
*[Gerard Domenech]*

*[Data Analytics - Part time SEP21]*

## Content
- [Project Description](#project-description)
- [Rules](#rules)
- [Workflow](#workflow)
- [Organization](#organization)
- [Links](#links)

## Project Description 
2-player version of "Risk" Boardgame. As a fan of boardgames I picked Risk because is a classic, although the game I wrote is loosely based on it.

## Rules
Describe briefly the rules of the game you chose.
The game duration is 10 rounds(each player will do 1 turn for round)
Turn order:

    1) Recruit Troops on regions you already control (the player 2 always recruit first)
    2) Select a region you control as a source of your attack
    3) Select the target region you will attack
    4) The attack will then happen. The winner is decided based on a 1d6 roll + the number of troops
    each have on the attacking/defending region
        4.1) If you win you conquer the region and 1 troop is deployed
        4.2) If you lose the combat you lose 1 troop on the region from where the attack come from.

At the end of 10 rounds, the player who controls more regions wins the game.
    

## Workflow
I started the project by looking videos that explain Risk rules.
Since it was kinda complex, I simplified the game ( less regions, a fixed number of rounds.. ).
Then i wrote on paper the possible classes that the program should have.
I started coding the game. Along the processes some ideas were scrapped off due to complexity or lack of time.
I then created the first stable version of the game, so it's at least functional.
I tested it and find some minor bugs and corrections.
Then i prepared the presentation

## Organization

I used Trello to organize my ideas and do not lose track of them.
My repository consist of the main jupyternotebook that contains all of the commits i have worked on, the readme file, and the current stable .py version of the game.


## Links
Include links to your repository, slides and trello/kanban board. Feel free to include any other links associated with your project. 

[Repository](https://github.com/GerardDD/Fake_Risk)  
[Slides](https://slides.com/)  
[Trello](https://trello.com/b/7h8mRIzU/fakerisk)  