# MinesweeperLinuxDesktop
Minesweeper is a game originated in the 1960s. To win you have to click on the grid boxes that could contain bombs or number that shows how many bombs are in the near by. If you reveal all the cells except the bombs you win.

This version has been developed with PyQt5 GUI framework in Python.

## Getting Started
To play this game you need to know the rules:
* The boxes on the grid contain bombs or numbers that shows how many bombs are in the near by
* If you click on a bomb you lose. If you reveal all the squares except the bombs you win
* To reveal a box you have to left click it.
* You can right click a cell to mark it as a bomb. 
  * This can help you to win but you don't have to mark all the bombs to win.

### Prerequisites
You need to have installed Anaconda python enviroment and PyQt5 GUI framework

### Installing
* To play the game you have to run the `main.py`
```
$ ipython
$ run main.py
```

## Implementation details
This version was developed based on the Model View Controller pattern.
Indeed in this repository you will find:
* 'View.py' that contains all the GUI elements
* 'Model.py' that with the class Box.py compose the logic of the game with all the datas.
* 'Controller.py' enables the connection of the classes above.

* 'DataType.py' and 'Text Manager' are the files that allow the Leaderboard management

# Preview
<img src="https://github.com/EnricoCollini/MinesweeperLinuxDesktop/blob/master/video.gif" height="400">
