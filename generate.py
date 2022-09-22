# from transformers import pipeline
# import time
# start_time_1 = time.time()
# generator = pipeline('text-generation', model='EleutherAI/gpt-neo-2.7B') # 10.7Gb downloaded
# end_time_1 = time.time()
# print('Generator 1: ', end_time_1 - start_time_1)
# start_time_2 = time.time()
# x = generator("SpinnerWheel has", do_sample=True, min_length=100)
# end_time_2 = time.time()
# print('Generator 2: ', end_time_2 - start_time_2)
# print(x)
# // First version: 36s step 1, 32s step 2
# [{'generated_text': 'SpinnerWheel has been used in other projects, including the game Final Fantasy IV, the mobile app Tap Tap Tapa, and most recently, in games such as Grand Theft Auto Online, for both PC 
# and mobile.\n\nBackground\n\nThe'}]

# from transformers import pipeline
# import time
# start_time_1 = time.time()
# generator = pipeline('text-generation', model='EleutherAI/gpt-neo-125M') # 526M downloaded.
# end_time_1 = time.time()
# print('Generator 1: ', end_time_1 - start_time_1)
# start_time_2 = time.time()
# x = generator("SpinnerWheel has", do_sample=True, min_length=100)
# end_time_2 = time.time()
# print('Generator 2: ', end_time_2 - start_time_2)
# print(x)

# [{'generated_text': 'SpinnerWheel has been an established feature in several recent smartphone apps for iOS and OS X. A'}]
# [{'generated_text': 'SpinnerWheel has been one of the most influential and inspiring features of this game. In the last'}]
# 1st Gen: 15s
# 2nd Gen: 0.7s



# from transformers import pipeline
# import time
# start_time_1 = time.time()
# generator = pipeline('text-generation', model='EleutherAI/gpt-neo-1.3B') # 5.31G
# end_time_1 = time.time()
# print('Generator 1: ', end_time_1 - start_time_1)
# start_time_2 = time.time()
# x = generator("SpinnerWheel has", do_sample=True, min_length=100)
# end_time_2 = time.time()
# print('Generator 2: ', end_time_2 - start_time_2)
# print(x)
# Generator 1:  24.725351095199585
# Generator 2:  15.853840112686157
# [{'generated_text': 'SpinnerWheel has the ability to create a custom slider. A Custom Slider is a slider which can be attached to a widget.\n\nA Custom Slider can be created in any of the widget classes like Slider, SpinBar and Sl'}]