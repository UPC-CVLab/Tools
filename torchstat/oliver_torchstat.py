from torchstat import stat
import torchvision.models as models
from example import Net

model1 = models.alexnet()
model2 = models.resnet18()
model3 = models.resnet34()
model4 = Net()

stat(model2, (3, 224, 224))
