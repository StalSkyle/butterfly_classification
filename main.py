# TODO: загнать в коллаб

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# предварительное исследование
from PIL import Image
import os
import numpy as np

path = "train_butterflies"
classes = sorted([d for d in os.listdir(path)])

total = 0
balance = dict()

for class_ in classes:
    class_path = os.path.join(path, class_)
    balance[class_] = 0
    class_images = [_ for _ in os.listdir(class_path)]

    for image in class_images:
        total += 1
        balance[class_] += 1

print(total) # 4955
print(sorted(balance.items(), key=lambda item: item[1]))