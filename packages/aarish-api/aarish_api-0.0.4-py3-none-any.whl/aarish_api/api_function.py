import base64
import json                    

import requests

def aarish_api(image_file1,image_file2,token):
    api = 'http://143.198.39.70/facerec'

    with open(image_file1, "rb") as f:
        im1_bytes = f.read()        
    im1_b64 = base64.b64encode(im1_bytes).decode("utf8")

    with open(image_file2, "rb") as f:
        im2_bytes = f.read()        
    im2_b64 = base64.b64encode(im2_bytes).decode("utf8")

    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    
    payload = json.dumps({"image1": im1_b64, "image2":im2_b64, 'token':token, "other_key": "value"})
    response = requests.post(api, data=payload, headers=headers)


    try:
        data = response.json()     
        return data                
    except requests.exceptions.RequestException:
        return response.text

