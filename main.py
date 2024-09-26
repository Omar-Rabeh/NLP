#import tensorflow as tf
#from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences


sentence = ['I love my dog' ,
            'I Love my cat',
            'You love my dog!',
            'Do you think my dog is amazing']


tokenizer = Tokenizer(num_words = 100, oov_token="<OOV>")
tokenizer.fit_on_texts(sentence)

word_index = tokenizer.word_index
#how the sentences containing those words can be turned into sequences of numbers

sequences = tokenizer.texts_to_sequences(sentence)

test_data = ['i really love my dog','my dog loves my manatee']
test_seq = tokenizer.texts_to_sequences(test_data)

padded = pad_sequences(sequences,padding='post',maxlen=5, truncating= 'post')


print(word_index)
print(sequences)
print(padded)
