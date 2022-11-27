import warnings
warnings.filterwarnings("ignore", category=UserWarning)

import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt

from wordcloud import WordCloud, STOPWORDS
from io import BytesIO
import base64


def gen_wordcloud(text=None):
    try:
        if text:
            wc = WordCloud().generate_from_text(text)
            plt.figure(figsize = (10, 5), facecolor = None)
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
        else:
            return None
    except:
        return None
        