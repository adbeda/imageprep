from imageprep.utils import *


image_path = '../data/images/'
label_path = '../data/labels/'

# one bbox in a single file
image_file0 = 'data/images/79_38.jpg'
label_file0 = '../data/images/79_38.txt'

# multiple bboxes in a single file
image_file1 = '../data/images/145_28.jpg'
label_file1 = '../data/labels/145_28.txt'


def _test_image_names():
    list_of_names = image_names(image_path)
    print("List of Images", list_of_names)


def test_read_label_as_dict():
    dict_label = read_label_as_dict(label_file0)
    print("Label file as a pythondictionary: ", dict_label)


def test_read_labels():
    folder_labels = read_labels(label_path)
    print("Label files in a folder: ", folder_labels)


def test_list_path_to_files():
    output= list_path_to_files(image_path)
    print("List of images", output)
