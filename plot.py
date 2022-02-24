# Generate wordcloud
import matplotlib.pyplot as plt
from wordcloud import WordCloud


class Plotter:

    def plotWordCloud(self, keyword_dict):
        text=''
        for word,freq in keyword_dict.items():
            for i in range(freq):
                text=text+word+" "

        # Generate wordcloud
        wordcloud = WordCloud(width = 800, height = 800,
                        background_color ='black',
                        min_font_size = 8,collocations=False).generate(text)
        # Plot
        #plot_cloud(wordcloud)
        plt.figure(figsize = (8, 8), facecolor = None)
        plt.imshow(wordcloud)
        plt.axis("off")
        plt.tight_layout(pad = 0)
        plt.show()
