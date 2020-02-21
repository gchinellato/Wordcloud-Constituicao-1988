import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

with open('data/ConstituicaoTextoAtualizado_EC.txt', 'r') as fo:
    text = fo.read().lower()

words = text.split()
print('Number of words in text file :', len(words))

with open('utility/stopwords-pt-br.txt', 'r', encoding='utf-8') as fo:
    stopwords_file = fo.read().splitlines()

stopwords = set(STOPWORDS)
stopwords.update(stopwords_file)
stopwords.update(["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII", "XIII", "IV", "V"])
stopwords.update(["i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix", "x", "xi", "xii", "xiii", "iv", "v"])
stopwords.update(["seção", "título", "capítulo", "parágrafo", "inciso", "caput", "artigo", "art", "ato", "nº", "1º", "2º", "3º", "4º", "5º"])
stopwords.update(["seguinte", "seguintes", "podendo", "poderão", "prevista", "único", "redação", "acrescido",
                  "dada", "atividade", "serviço", "recurso", "emenda", "publicada", "respectiva", "respectivas", "respectivo", "respectivos"
                  "acrescida", "exercício", "salvo", "seguintes", "respectiva", "alínea","josé"])
 
wordcloud = WordCloud(stopwords=stopwords, 
                      max_words=100,
                      #max_font_size=40,
                      width=1600,
                      height=800,
                      background_color="black").generate(text)
 
fig, ax = plt.subplots(figsize=(10,6))
ax.imshow(wordcloud, interpolation='bilinear')
ax.set_axis_off()
 
plt.imshow(wordcloud)
wordcloud.to_file("wordcloud-constituicao-1988.png")
