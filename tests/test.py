import os
import json
import gdown
import unittest


class TestZoo(unittest.TestCase):

    def test_listdirs(self):
        l = [i for i in os.listdir() if i not in ['Readme.md', '.ipynb_checkpoints', '.gitignore', '.git', "tests",".github"]]
        ll = [os.path.exists(os.path.join(i, 'result.json')) for i in l]
        empty = []
        for i in range(len(ll)):
            if(ll[i] == False):
                empty.append(l[i])
                
        self.assertEqual(empty, [], "result.json missing in "+ " ".join(empty))
        
    def test_json(self):
        l = [i for i in os.listdir() if i not in ['Readme.md', '.ipynb_checkpoints', '.gitignore', '.git', "tests",".github"]]
        ll = [os.path.exists(os.path.join(i, 'result.json')) for i in l]
        all_dirs = [i for i,j in zip(l,ll) if j]
        keys = ['Title', 'Tags', 'Architecture', 'Publisher', 'Problem Domain', 'Model Format', 'Language', 'Dataset', 'Overview', 'Preprocessing', 'Link', 'Usage', 'References', 'Input Shape', 'Output Shape', 'Description']
        for i in all_dirs:
            with open(os.path.join(i, 'result.json'), 'rb') as f:
                g = json.load(f)
            for k in g.keys():
                if k not in keys:
                    self.assertEqual(k, "", "Key " + k + " in " + i + " is not one of the recommended keys")
            f.close()

    def test_paths(self):
        l = [i for i in os.listdir() if i not in ['Readme.md', '.ipynb_checkpoints', '.gitignore', '.git', "tests",".github"]]
        ll = [os.path.exists(os.path.join(i, 'result.json')) for i in l]
        all_dirs = [i for i,j in zip(l,ll) if j]
        for i in all_dirs:
            with open(os.path.join(i, 'result.json'), 'rb') as f:
                g = json.load(f)
            self.assertTrue(os.path.exists(os.path.join(i, g["Usage"])), "Usage notebook missing in " + i)
            if g["Preprocessing"] != "null" and g["Preprocessing"]:
                self.assertTrue(os.path.exists(os.path.join(i, g["Preprocessing"])), "Preprocessing notebook missing in " + i)

    def test_lang(self):
        l = [i for i in os.listdir() if i not in ['Readme.md', '.ipynb_checkpoints', '.gitignore', '.git', "tests",".github"]]
        ll = [os.path.exists(os.path.join(i, 'result.json')) for i in l]
        all_dirs = [i for i,j in zip(l,ll) if j]
        for i in all_dirs:
            with open(os.path.join(i, 'result.json'), 'rb') as f:
                g = json.load(f)
            if(g["Problem Domain"] == "Text" and not g["Language"]):
                self.fail("No Language was given for Text Model")
            if(g["Problem Domain"] != "Text" and g["Language"]):
                print(i)
                self.fail("Problem Domain was not text but Language was specified")

    """def test_model_existence(self):
        l = [i for i in os.listdir() if i not in ['Readme.md', '.ipynb_checkpoints', '.gitignore', '.git', "tests",".github"]]
        ll = [os.path.exists(os.path.join(i, 'result.json')) for i in l]
        all_dirs = [i for i,j in zip(l,ll) if j]
        base_url = 'https://drive.google.com/uc?id='
        for i in all_dirs:
            with open(os.path.join(i, 'result.json'), 'rb') as f:
                g = json.load(f)
            try:    
                gdown.download(base_url + g["Link"].split('/')[5], 'redundant', quiet = True)
            except Exception as e:
                self.fail(e)
            break"""


if __name__ == '__main__':
    unittest.main()