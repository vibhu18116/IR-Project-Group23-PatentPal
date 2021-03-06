# IR-Project-Group23-PatentPal
Information Retrieval Project: Group 23 - Winter 2021

![Screenshot 2021-03-25 at 12 03 22 AM](https://user-images.githubusercontent.com/43923076/112365361-90ddc680-8cfd-11eb-867e-84f87e094e4a.png)

Inventorship is an art, proving you smart\
But so many patents, where to start?

## Project Description
PatentPal - which can summarise the patents filed, create a summary for a new patent and find similar patents, given another patent or appropriate keywords.

## Exploration of Data
Data Anaysis Directory: The exploratory data analysis is in this directory.
## Baseline Models
Summary Directory: The Baselines Codes for summarisation models are in this directory.

Retrieval Directory: The Baselines Codes for retrieving patens are in this directory.

## Using the system

### Required Python Libraries
Install the following dependencies using pip3
- `pip3 install flask`
- `pip3 install transformers`
- `pip3 install pandas`
- `pip3 install nltk`
- `pip3 install pyspellchecker`
- `pip3 install pytorch torchvision -c pytorch`
- `pip3 install torch torchvision`
- `pip3 install rank_bm25`

### Steps
1. `cd Website_UI`
2. `python3 app.py`
3. Open localhost:5000 on browser.


## User Interface

### Home Page
![home](https://user-images.githubusercontent.com/43749855/117653282-d1ac7480-b1b1-11eb-80e4-dc5361a1a98e.png)

### Retrieval Page
![retrieval](https://user-images.githubusercontent.com/43749855/117653270-cce7c080-b1b1-11eb-8cce-3731c25f7e57.png)

### Summary Page
![summary](https://user-images.githubusercontent.com/43749855/117653275-cfe2b100-b1b1-11eb-948e-f4b40c06736a.png)


