#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

import tensorflow as tf


SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']


class model_from_h5(tf.keras.models.Model):
    def __init__(self, download_link, creds_file = 'credentials.json'):
        super().__init__()
        self.link = download_link
        self.creds_file = creds_file
        self.chunk_size = 32768
        self.destination = "model.h5"
        self.model = self.download()
        
    def download(self):
        session = requests.session()
        response = session.get(self.link, params = { 'id' : id }, stream = True)
        
        for key, value in response.cookies.items():
            if key.startswith('download_warning'):
                token = value
    
        if token:
            params = { 'id' : id, 'confirm' : token }
            response = session.get(self.link, params = params, stream = True)
        else:
            print("No Token Found")
            
        with open(self.destination, "wb") as f:
            for self.chunk_size in response.iter_content(self.chunk_size):
                if self.chunk: # filter out keep-alive new chunks
                    f.write(self.chunk)
                    
        return tf.keras.models.load_model(self.destination)
    