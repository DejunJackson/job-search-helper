import matplotlib.pyplot as plt, mpld3  
from wordcloud import WordCloud, STOPWORDS
from io import BytesIO
import base64


def gen_wordcloud(text):
    wc = WordCloud()
    wc = wc.generate_from_text(text)

   
                        
    plt.figure(figsize = (10, 10), facecolor = None)
    plt.imshow(wc)
    plt.axis("off")
    plt.tight_layout(pad = 0)
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    graphic = base64.b64encode(image_png)
    graphic = graphic.decode('utf-8')
    return graphic