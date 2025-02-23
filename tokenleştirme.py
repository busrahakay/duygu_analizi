# NLTK için durdurma kelimeleri ve lemmatizer'i indir
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Durdurma kelimeleri ve lemmatizer
stop_words = set(stopwords.words('turkish'))
lemmatizer = WordNetLemmatizer()

# CSV dosyasını yükleyin ve verileri ayırın
data = pd.read_csv("e-ticaret_urun_yorumlari.csv", encoding="utf-8-sig", sep=";", engine="python", on_bad_lines="skip")

# DataFrame'in ilk birkaç satırını görüntüleme
print(data.head())

# Eğer veriler tek bir sütunda ise, 'Metin' ve 'Durum' sütunlarını ayırın
if 'Metin;Durum' in data.columns:
    data[['Metin', 'Durum']] = data['Metin;Durum'].str.split(';', expand=True)

# Sütun isimlerini düzeltme
data.columns = ['Metin', 'Durum']

# Metinleri ön işleme
data['Metin'] = data['Metin'].fillna('')  # Boş olanları boş string ile doldur

# Etiketleri sayısal hale getirme
label_encoder = LabelEncoder()
data['durum_encoded'] = label_encoder.fit_transform(data['Durum'])
y = data['durum_encoded'].values

# Veri ön işleme
preprocessed_data = []
for text in data['Metin']:
    text = text.lower()
    words = word_tokenize(text)  # Tokenize işlemi
    filtered_words = [lemmatizer.lemmatize(word) for word in words if word not in stop_words and word.isalpha()]  # Stopwords ve özel karakterleri çıkar
    preprocessed_data.append(filtered_words)

# Word2Vec modelini eğitme
embedding_dim = 300  # Daha yüksek bir boyut veriye göre daha iyi olabilir
word2vec_model = Word2Vec(sentences=preprocessed_data, vector_size=embedding_dim, window=5, min_count=1, workers=4)

# Kelime sıraları ve dizinleri oluşturma
word_index = {word: index + 1 for index, word in enumerate(word2vec_model.wv.index_to_key)}

# Veriyi sayısal diziye çevirme ve hizalama
max_length = 100  # Daha yüksek max_length metinlerin daha kapsamlı temsilini sağlar
train_sequences_word2vec = [[word_index[word] for word in text if word in word_index] for text in preprocessed_data]
X = pad_sequences(train_sequences_word2vec, maxlen=max_length, padding='post', truncating='post')

# Word2Vec gömme matrisi oluşturma
embedding_matrix = np.zeros((len(word_index) + 1, embedding_dim))
for word, i in word_index.items():
    embedding_vector = word2vec_model.wv[word]
    if embedding_vector is not None:
        embedding_matrix[i] = embedding_vector

# Tokenizer'ı pickle ile kaydetme
with open('tokenizer.pickle', 'wb') as handle:
    pickle.dump(word_index, handle, protocol=pickle.HIGHEST_PROTOCOL)