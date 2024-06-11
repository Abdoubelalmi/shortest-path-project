# Shortest Path Finder

This Python application allows users to find the shortest path between two locations in various cities of Algeria using OpenStreetMap data.

## Features

- Select from a list of Algerian cities to retrieve map data.
- Choose source and destination nodes from the respective list boxes.
- Calculate and visualize the shortest path between selected locations using A\* search algorithm.

## Installation

1. Ensure you have Python installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

2. Install the required Python packages using `pip`. Open a terminal and run the following command:

   ```bash
   pip install osmnx networkx matplotlib tkinter
   ```

3. Download or clone this repository to your local machine.

   ```bash
   git clone https://github.com/Abdoubelalmi/shortest-path-project.git
   cd shortest-path-finder
   ```

## Usage

1. Run the `shortest_path_finder.py` script to launch the application.

   ```bash
   python shortest_path_finder.py
   ```

2. Select a city from the dropdown menu (you may need to wait a few seconds for the map data to download).

3. Choose the source and destination places from the respective list boxes.

4. Click the "Find Shortest Path" button to calculate and display the shortest path between the selected locations.


## Screenshots

![Application Interface](screenshots/app_interface.png)
_Screenshot 1: Application interface showing the selection of a city and source/destination places._

![Shortest Path Display](screenshots/map_with_shortest_path.png)
_Screenshot 2: Application interface displaying the shortest path between two locations._
