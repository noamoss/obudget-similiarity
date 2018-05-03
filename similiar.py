from collections import defaultdict

import pandas as pd

text_list = ['france','spain','spain beaches', 'france beaches','spain best beaches']

word_freq = defaultdict(int)

for text in text_list:
    for word in text.split():
        word_freq[word] += 1

pd.DataFrame.from_dict(word_freq, orient='index').sort_values(0, ascending=False).rename(columns={0: 'abs_freq'})
