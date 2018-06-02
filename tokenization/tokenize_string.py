def tokenize_text(text):
    """
    tokenize textual string and get rid of non alpha numberics, split to words in selected columns
    """
    import re

    regxlst = [re.compile(x) for x in [r'\d+',]]    # regular expressions list for clean ups:
                                                             # 1. only digits
    stringed_text = str(text)
    ignore_signs = ["\,","\:","\;","\.","\&","\$","\-","\=","\(","\)","\d+","\\n"]
    cleaned_1 = re.sub("|".join(ignore_signs),"",stringed_text) # remove non-alphanumberic characters
    cleaned_2 = re.sub("  "," ",cleaned_1)                # no more double spaces
    cleaned_3 = cleaned_2.split()                       # split into separate words list
    cleaned_4 =  [word for regex in regxlst for word in cleaned_3 if not(regex.match(word))] # filter by regular expressions
    cleaned_5 = [word for word in cleaned_4 if word is not None]
    return cleaned_5
