from wordcloud import WordCloud

# This is the function to generate the image of word cloud from the given text
def get_wordcloud(text):

    wordcloud = WordCloud(
        background_color='white',
        width=800,
        height=600,
        margin=2,
        stopwords={'feat', 'remix', 'Radio', 'Edit', 'The', 'I', 'You'}
    ).generate(text)

    return wordcloud
