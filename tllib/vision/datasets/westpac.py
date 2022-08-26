"""
@author: Hanxian He
@contact: hanxian.he@monash.edu
"""
from typing import Optional
import os
from .imagelist import ImageList
from ._util import download as download_data, check_exits


class Westpac(ImageList):
    """Westpac Dataset.

    Args:
        root (str): Root directory of dataset
        task (str): The task (domain) to create dataset. Choices include ``'M'``: MIAP, \
        and ``'P'``: P2datasetfull.
        download (bool, optional): If true, downloads the dataset from the internet and puts it \
            in root directory. If dataset is already downloaded, it is not downloaded again.
        transform (callable, optional): A function/transform that  takes in an PIL image and returns a \
            transformed version. E.g, :class:`torchvision.transforms.RandomCrop`.
        target_transform (callable, optional): A function/transform that takes in the target and transforms it.

    .. note:: In `root`, there will exist following files after downloading.
        ::
            MIAP/
                images/
                    clean/
                        *.jpg
                        ...
            P2datasetfull/
       
            image_list/
                MIAP.txt
                P2datasetfull.txt
                Ptest.txt
                
    """
    #Dataset is not public available currently 
    download_list = [
        ("image_list", "image_list.zip", ""),
        ("MIAP", "MIAP.tgz", ""),
        ("P2datasetfull", "p2datasetfull.tgz", "")
    ]
    image_list = {
        "M": "image_list/MIAP.txt",
        "P": "image_list/P2datasetfull.txt",
        "T": "image_list/Ptest.txt"
    }
    CLASSES = ['clean','porn_indicative','porn']

    def __init__(self, root: str, task: str, download: Optional[bool] = True, **kwargs):
        assert task in self.image_list
        data_list_file = os.path.join(root, self.image_list[task])

        if download:
            list(map(lambda args: download_data(root, *args), self.download_list))
        else:
            list(map(lambda file_name, _: check_exits(root, file_name), self.download_list))

        super(Westpac, self).__init__(root, Westpac.CLASSES, data_list_file=data_list_file, **kwargs)

    @classmethod
    def domains(cls):
        return list(cls.image_list.keys())