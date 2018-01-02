import pg_interface as pg
from wordcloud import WordCloud

stop_words = [ "a", "about", "above", "after", "again", "against", "all", "am", "an", "and", "any", "are", "as", "at", "be", "because", "been", "before", "being", "below", "between", "both", "but", "by", "could", "did", "do", "does", "doing", "down", "during", "each", "few", "for", "from", "further", "had", "has", "have", "having", "he", "he'd", "he'll", "he's", "her", "here", "here's", "hers", "herself", "him", "himself", "his", "how", "how's", "i", "i'd", "i'll", "i'm", "i've", "if", "in", "into", "is", "it", "it's", "its", "itself", "let's", "me", "more", "most", "my", "myself", "nor", "of", "on", "once", "only", "or", "other", "ought", "our", "ours", "ourselves", "out", "over", "own", "same", "she", "she'd", "she'll", "she's", "should", "so", "some", "such", "than", "that", "that's", "the", "their", "theirs", "them", "themselves", "then", "there", "there's", "these", "they", "they'd", "they'll", "they're", "they've", "this", "those", "through", "to", "too", "under", "until", "up", "very", "was", "we", "we'd", "we'll", "we're", "we've", "were", "what", "what's", "when", "when's", "where", "where's", "which", "while", "who", "who's", "whom", "why", "why's", "with", "would", "you", "you'd", "you'll", "you're", "you've", "your", "yours", "yourself", "yourselves", "rt" ]

def get_all_tweets():
    return pg.SELECT("* FROM public.tweets")

def add_words_to_dict(tweet, word_dict):
    for word in tweet['text'].lower().split():
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

def remove_stop_words(word_dict):
    for word in stop_words:
        word_dict.pop(word, None)
    return word_dict

def create_dict(tweets):
    word_dict = {}
    for tweet in tweets:
        add_words_to_dict(tweet, word_dict)
    return remove_stop_words(word_dict)

def top_words_from_list(sorted_words, word_dict):
    top_words = []
    for word in sorted_words:
        top_words += [(word, word_dict[word])]
    return top_words

def sort_words(word_dict):
    sorted_words = sorted(word_dict, key=word_dict.get)
    top_words = top_words_from_list(sorted_words, word_dict)
    return top_words

def print_word_freq(sorted_words):
    for word in sorted_words:
        print(str(word[1]) + ':', word[0])

def make_word_cloud(word_dict):
    cloud = WordCloud(background_color='white', width=1600, height=800)
    cloud.generate_from_frequencies(word_dict)
    cloud.to_file("cloud.png")

def main():
    tweets = get_all_tweets()
    freq_dict = create_dict(tweets)
    sorted_words = sort_words(freq_dict)
    # make_word_cloud(freq_dict)
    print_word_freq(sorted_words)

if __name__ == "__main__":
    main()
