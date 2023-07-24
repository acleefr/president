# French Card Game "President" Repository

This repository contains the implementation of the French card game "President" using Python for the terminal-based version and React with TypeScript for the graphical version.

## Game Rules

**President** is a fun and strategic shedding card game typically played with a standard 52-card deck. The game is also known by various other names, such as "Asshole" or "Scum" in English.

### Objective:
The goal of the game is to be the first player to get rid of all your cards and become the President in the next round. Conversely, the last player to still have cards becomes the "Scum" or the "Asshole" and has some disadvantages in the next round.

### Number of Players:
The game can be played with 4 or more players.

### Card Ranking:
- Cards are ranked from high to low: 2, A, K, Q, J, 10, 9, 8, 7, 6, 5, 4, 3.
- Suits do not matter in this game.

### Gameplay:
1. **Dealing:** The dealer shuffles the deck and deals all the cards equally among the players.

2. **Starting Player:** The player with the 3 of Spades (3♠) starts the game. If no one has the 3 of Spades, then the player with the next lowest card starts (usually the 4 of Spades or 2 of Spades).

3. **Play:** Players take turns in a clockwise direction. Each turn, a player must play one or more cards of the same rank (e.g., single card, pair, triplet, etc.) that beats the previously played combination in rank. Players can also pass their turn if they do not wish to play any cards.

4. **Passing:** If a player cannot or does not want to play a higher combination, they must pass their turn.

5. **Clearing the Board:** Once all other players have passed, the player who played the last combination(s) successfully clears the board, and they get to start the next round.

6. **Winning a Round:** The first player to successfully play all their cards becomes the President, and the next round starts. The last player with cards becomes the "Scum" or the "Asshole."

7. **Card Ranking in the Next Round:** In subsequent rounds, the players are ranked based on their performance in the previous round, with the President getting the highest priority in playing first and the Scum getting the lowest priority.

8. **Card Trading (Optional):** In some variations of the game, the President can give their two highest-ranking cards to the Scum, who must then give their two lowest-ranking cards in return.

9. **Game End:** The game usually continues until players decide to stop or after a predetermined number of rounds. The player with the most rounds won or the highest overall score wins the game.

Remember that these rules are just a general guideline, and various regions or players might have their own variations or house rules for the game. Have fun playing "President"!

# Getting Started with Create React App

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## Available Scripts

In the project directory, you can run:

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

The page will reload if you make edits.\
You will also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can’t go back!**

If you aren’t satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you’re on your own.

You don’t have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn’t feel obligated to use this feature. However we understand that this tool wouldn’t be useful if you couldn’t customize it when you are ready for it.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).
# president
