def add_prefix_un(word):
    return 'un' + word

def make_word_groups(vocab_words):
    prefix = vocab_words[0]
    vocab_words = [prefix] + [prefix + word for word in vocab_words[1:]]
    return ' :: '.join(vocab_words)

def remove_suffix_ness(word):
    word = word[:-4]
    if word.endswith('i'):
        word = word[:-1] + 'y'
        return word
    else:
        return word

def adjective_to_verb(sentence, index):
    sentence = sentence.split()
    last_word = sentence[index]
    if last_word.endswith('.'):
        last_word = last_word[:-1] + 'en'
        return last_word
    return last_word + 'en'
    