## Welcome to SmokeTrees Forest
Our own model-zoo, formatless, indigenous and ease of utility models made by yours truly.

SmokeTrees Forest has a unique structure, it includes all models as seperate entities, so that we can avoid enviorment collapses in python.

## Usage:
- Please download the json file when you want to use it's corresponding model as it contains necessary information to get you started and for ease of access to Forest Utility Classes and Methods.
- Refer to documentation for usage and preprocessing modules that you may need to use once putting the models to work.
- We'll be releasing the Forest utility package as seperate modules, for ex. forest-utils-tf for Tensorflow, for now the package is still in alpha testing.

## Contribute:
You can also contribute to our model-zoo, please follow these instructions:
- All models should be self-contained in a folder inside the repo when you make a PR.
- The PR must contain an jupyter notebook converted to html showing how to use the models, if you want, you can show usage using the forest_utils to load models.
- A preprocessing notebook as html can also be added, but it's utility can also be shown inside the aforementioned usage file.
- The PR must also contain a json file, containing the following information as types mentioned, for example
```
{
    "Title": "Heartbeat Classification", (Title of the model (type:str))
    "Tags": ["Sequence Task","Disease Classification"], (ML tags you want to add it to (type:list(str)), must be one of the tags already created, check forest website to see available tags)
    "Architecture": "CNN-1D", (Architecture of the model followed, (type:str))
    "Publisher": [["Tanmay Thakur","https://github.com/lordtt13"], ["Smoketrees","https://github.com/smoke-trees"]], (The people and/or organisations involved in the commit (type:list(list)) list elements are lists containing two elements, one being the name to be shown, the other a link to the profile or null)
    "Problem Domain": "Sequence", (ML problem domains you want to add it to (type:list(str)), must be one of the domains already created, check forest website to see available domains)
    "Model Format": "Tensorflow2", (Mention what framework was used in making the model (type:str))
    "Language": "null", (If an NLP model, what language does the model take into consideration (type:str))
    "Dataset": [["MIT-BIH","https://physionet.org/content/mitdb/1.0.0/"]], (The dataset the model was trained on (type:list(list)) list elements are lists containing two elements, one being the name to be shown, the other a link to the dataset or null)
    "Overview": "A classification task done on the MIT-BIH dataset, split into 5 labels.", (A simple discription of your model (type:str))
    "Preprocessing": "null", (Path to the preprocessing.html file (type:str))
    "Link": "https://drive.google.com/file/d/1H5pB5kYTmga7xsytxGVAH07KPK00tHwJ/view?usp=sharing", (Link where your model is saved (type:str), save it in your own google drives with permissions for everyone to view)
    "Usage": "usage.html", (Path to the usage.html file (type:str)) 
    "References": "[http://ecg.mit.edu/george/publications/mitdb-embs-2001.pdf]", (Links to any research papers you followed or want to reference (type:list(str)))
    "Input Shape": "[[1,187,1]]", (Input shapes of the model (type:list(list)))
    "Output Shape": "[[1,5]]" (Output shapes of the model (type:list(list))),
    "Description": ""The MIT-BIH dataset has been used research into cardiac dynamics at more than 500 sites worldwide.\nThis model uses the Convolutional Neural Net Architecture on image data of shape [1,187,1]\nand then classifies the image into one of the five labels the dataset has been divided into."
}
```
Before contributing please ensure that you pass all tests, just run python tests/test.py

## Issues:
- If you run into any issues in using the model or the utility package please create the appropriate issue on our repo and label them.
- Please note that any kind of models that have weights loaded from elsewhere will not be accepted into the model-zoo.


