from PIL import Image
from xml.etree import ElementTree
import copy


class PhoenixData(object):
    """
        Class to represent phoenix data consisting of image name, image, mask and its annotations
    """

    def __init__(self, ):
        self.name: str = None
        self.image: Image.Image = None
        self.mask: Image.Image = None
        self.annotation_mask: Image.Image = None
        self.annotation: ElementTree = None

    def copy(self):
        return copy.deepcopy(self)
