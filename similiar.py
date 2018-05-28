from collections import defaultdict

import pandas as pd

# default value

word_freq = defaultdict(lambda: [0,0])

# how many times a word appears in the corpus
num_list = [200, 180, 170, 160,160]

# text
text_list = ['france', 'spain', 'spain beaches', 'france beaches', 'spain best beaches']



# loop over the text and the number
for text, num in zip(text_list, num_list):
    for word in text.split():
        word_freq[word][0] += 1
        word_freq[word][1] += num


columns = {0: 'abs_freq', 1:'wtd_freq'}

abs_wtd_df = pd.DataFrame.from_dict(word_freq,orient='index')\
            .rename(columns=columns) \
            .sort_values('wtd_freq', ascending=False) \
            .assign(rel_value=lambda df: df['wtd_freq'] / df['abs_freq'])\
            .round()


abs_wtd_df.insert(1, 'abs_perc', value=abs_wtd_df['abs_freq']/abs_wtd_df['abs_freq'].sum())
abs_wtd_df.insert(2, 'abs_perc_cum', abs_wtd_df['abs_perc'].cumsum())
abs_wtd_df.insert(4, 'wtd_freq_perc', abs_wtd_df['wtd_freq'] / abs_wtd_df['wtd_freq'].sum())
abs_wtd_df.insert(5, 'wtd_freq_perc_cum', abs_wtd_df['wtd_freq_perc'].cumsum())
abs_wtd_df.style.background_gradient(low=0, high=.8)
