import os
import json
import unittest


class TestZoo(unittest.TestCase):

    def test_listdirs(self):
        l = [i for i in os.listdir() if i not in ['Readme.md', '.ipynb_checkpoints', '.gitignore', '.git', "tests"]]
        ll = [os.path.exists(os.path.join(i, 'result.json')) for i in l]
        empty = []
        for i in range(len(ll)):
            if(ll[i] == False):
                empty.append(l[i])
                
        self.assertEqual(empty, [], "result.json missing in "+ " ".join(empty))
        
    def test_json(self):
        l = [i for i in os.listdir() if i not in ['Readme.md', '.ipynb_checkpoints', '.gitignore', '.git', "tests"]]
        ll = [os.path.exists(os.path.join(i, 'result.json')) for i in l]
        all_dirs = [i for i,j in zip(l,ll) if j]
        keys = ['Title', 'Tags', 'Architecture', 'Publisher', 'Problem Domain', 'Model Format', 'Language', 'Dataset', 'Overview', 'Preprocessing', 'Link', 'Usage', 'References', 'Input Shape', 'Output Shape', 'Description']
        for i in all_dirs:
            f = json.load(open(os.path.join(i, 'result.json'), 'rb'))
            for k in f.keys():
                if k not in keys:
                    self.assertEqual(k, "", "Key " + k + " in " + i + " is not one of the recommended keys")
            f.close()
        

if __name__ == '__main__':
    unittest.main()