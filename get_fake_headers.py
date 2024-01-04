from fake_headers import Headers

def get_headers(os="win") -> dict: 
    header = Headers(
        browser="chrome",  # Generate only Chrome UA
        os=os,  # os - str, win/mac/lin. OS of User Agent. Default: random
        headers=True  # generate misc headers
    ) 
    
    return header.generate()