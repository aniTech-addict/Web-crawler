# Web Crawler Project Log

## Project Goal
Build a web crawler specifically for Wikipedia to extract structured data about a given topic and its related pages. The extracted data will be stored in a database for potential future use in ML model training. The scope is limited to data retrieval and storage, not the ML part.

## Current State
- Initial project structure created (`main.py`, `database_manager.py`, `README.md`).
- `database_manager.py` is set up to handle SQLite database connection and table initialization.
- `main.py` is currently empty.

## Plan Update
- Data storage method changed from JSON files to using the SQLite database via `database_manager.py`.
- We will proceed in small, digestible steps to facilitate learning.

## Next Steps (High-Level Plan)
1.  Implement user input for the topic title in `main.py`.
2.  Convert the topic title to a Wikipedia URL.
3.  Initialize the crawl queue with the starting URL.
4.  Implement the main crawling loop.
5.  Fetch and parse a page.
6.  Extract data (title, intro, headings, infobox).
7.  Store extracted data in the database.
8.  Discover and manage internal links.
9.  Add valid links to the queue.
10. Handle errors.

## Log Entries
- Initial log created reflecting project goal, current state, updated plan (database storage), and high-level next steps.
