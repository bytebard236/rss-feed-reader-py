# RSS feed reader in terminal

## Requirements

You'll build a tool for fetching and converting the feed with a given RSS feed URL.

-The user can input one or more RSS feed URLs.

-The reader will display the title, description, link, and publish date of the original content.


1. Clone the repo
  ```sh
   git clone https://github.com/uka7/terminal-rss-feed-reader.git
  ```
2. Create a virtual environment
  ```sh
   cd 
   python3 -m venv rssfeedreader
  ```
3. Activate the virtual environment
  ```sh
   source env/bin/rssfeedreader
  ```
4. Install packages
  ```sh
   pip install -r requirements.txt 
  ```
5. Run in terminal. and use interactive menu to Add / Display the Rss Feed
  ```
   python main.py 
  ```

## Example
Run in Terminal
  ```
   python main.py
  ```
### Sampe output in the command prompt
1. Add URL
2. Fetch and Display Latest news
3. Exit
Enter your choice: 1
Enter URL: https://timesofindia.indiatimes.com/rssfeedstopstories.cms
1. Add URL
2. Fetch and Display Latest news
3. Exit
Enter your choice: 2
Tile: RS polls: BJP fields Nadda from Gujarat, Chavan from Maha
Description: BJP on Wednesday released another list of seven names for upcoming Rajya Sabha polls, nominating party president JP Nadda from Gujarat and Ashok Chavan, who recently joined the saffron party after quitting Congress, from Maharashtra.In its latest list, BJP has declared four names from Gujarat and three from Maharashtra. Besides Nadda, BJP nominated Govindbhai Dholakia, Mayanbhai Nayak and Jashvantsinh Parmar from Gujarat.
Link: https://timesofindia.indiatimes.com/india/bjp-releases-list-of-nominees-for-rajya-sabha-polls-jp-nadda-and-ashok-chavan-among-candidates/articleshow/107687259.cms
