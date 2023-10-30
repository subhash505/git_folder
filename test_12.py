import spacy
nlp = spacy.load('en_core_web_sm') # dowloading the package
# # from polyglot.detect import Detector

# import nltk
# nlp =nltk.download('punkt')
# nlp=nltk.download('averaged_perceptron_tagger')

# from nltk import word_tokenize, pos_tag


text = "INCOMING WIRE - CHACCT#3805439512   THE 1/GORIS FAMILY, TRUST U/T/A DATE GORIS FAMILY TRUST CAPITAL CALL Subhash Sharma"

# text = "Machine learning (ML) is a field of inquiry devoted to understanding and building methods that learn, \
# that is, methods that leverage data to improve performance on some set of tasks. It is seen as a part of artificial \
# intelligence. Machine learning algorithms build a model based on sample data, known as training data, in order to make \
# predictions or decisions without being explicitly programmed to do so. Machine learning algorithms are used in a wide \
# variety of applications, such as in medicine, email filtering, speech recognition, and computer vision, where it is \
# difficult or unfeasible to develop conventional algorithms to perform the needed tasks."


# tokens = word_tokenize(text)
# print(tokens)
doc = nlp(text)
# print(doc)

nouns = [token.text for token in doc if token.pos_ == "NOUN"]

# for np in doc.noun_chunks:
#       print(np)
# names = [ent.text for ent in doc.ents if ent.label_ == "PERSON"]

# print(names)

# parts_of_speech = nltk.pos_tag(tokens)

# nouns = list(filter(lambda x: x[1] == "NN", parts_of_speech))
print(nouns)

print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])

list1 = [chunk.text for chunk in doc.noun_chunks]
# nouns = [token.text for token in list if token.pos_ == "NOUN"]
print(list1)

print("Noun tokens ", [ent.text for ent in nlp(list1[0]).ents if ent.label_ == "PERSON"])

for token in nlp(list1[0]):
    # if token.pos_ == "PROPN":
    #     print(token.text)
    # print(token.text,"||", token.lemma_,"||", token.pos_,"||", token.tag_,"||", token.dep_,"||",
    #         token.shape_,"||", token.is_alpha,"||", token.is_stop)
    print(token.text, token.dep_, token.head.text, token.head.pos_,
            [child for child in token.children])

# [ent.text for ent in doc.ents if ent.label_ == "PERSON"]
# from spacy import spacy.en
# from spacy.en import English

# nlp = English()
# doc = nlp(u'INCOMING WIRE - CHACCT#3805439512   THE GORIS FAMILY TRUST U/T/A DATE GORIS FAMILY TRUST CAPITAL CALL Subhash Sharma')
# for np in doc.noun_chunks:
#     np.text
# import spacy

# nlp = spacy.load("en_core_web_sm")
# doc = nlp("Apple is looking at buying U.K. startup for $1 billion")

# for token in doc:
#     print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
#             token.shape_, token.is_alpha, token.is_stop)