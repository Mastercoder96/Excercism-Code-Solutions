def add_prefix_un(word):


    return "un" + word


 


def make_word_groups(vocab_words):
  
    return(" :: " + vocab_words[0]).join(vocab_words)

    


def remove_suffix_ness(word):
    
    base = word[:-4]
    
    if base[-1] == 'i':
        return base[:-1] + 'y'
    return base
    



def noun_to_verb(sentence, index):
    
    return sentence.split(' ')[index].replace('.','') + 'en'


   