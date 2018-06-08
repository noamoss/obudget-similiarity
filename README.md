## SimilarIt will sort entities by their textual properties similarity

Based on [Pandas](https://pandas.pydata.org/), [Gensim](https://radimrehurek.com/gensim/) with an Hebrew twist, originally developed for [OpenBudget](https://github.com/OpenBudget/BudgetKey) needs for quick entity comparison.

Notice: Currently, comparison will consider ONLY textual properties. Roadmap includes a planned step to consider quantitative variables as well.

### Installation

* `pip install -r requirements.txt`
*  verify correct settings in the [sources.json](sources.json) file
(you might prefer to create a new sources.json file, make sure to point it from [settings.py](settings.py))



### Usage

* define on [settings.py](settings.py) what kind of entity you would like to explore. Notice it must be one of the entities defined in the [sources.json](sources.json) file.
* `python3 run.py <entity_id>``

### Steps and modules (see comments in each of the modules files for further information)

0. settings.py: to define sources file path, define which entity you would like to compare, how many results (similar entities) would you like to get.
1. [data_loader](../master/data_loader): load data packages and transform into pandas Dataframe
2. [tokenization](../master/tokeniation): narrow and unify textual elements
3. [tfidf](../master/tfidf): similarity calculation based on term frequencies and cosinus similarity



* Upcoming steps are listed in the [roadmap.md](roadmap.md)
