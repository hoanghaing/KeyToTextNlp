# pip install yake
import yake

text = "Kim Dasom (born May 6, 1993; Hangul: 김다솜), better known by her stage name Dasom (Hangul: 다솜) is a South Korean idol singer. She is best known as a vocalist of the girl group, Sistar under Starship Entertainment. Biography. Dasom was born on May 6, 1993, in Seoul, South Korea. She currently attends Anyang Arts School."


kw_extractor = yake.KeywordExtractor()
keywords = kw_extractor.extract_keywords(text)

for kw in keywords:
    print(kw)