# from urllib import request, parse, error
# import json

if __name__ == "__main__":
    
    # query = parse.urlencode({'q': 'python'})

    # # httpbin은 요청 내용을 반환해 줌
    # url = f'https://httpbin.org/get?{query}'
    # try:
    #     with request.urlopen(url) as f:
    #         res = f.read().decode('utf-8')
    # except error.HTTPError as e:
    #     print(e)
    
    # print(json.loads(res))

    import requests

    # res = requests.get('https://httpbin.org/get', params={'q': 'python'})
    # print(res.json())

    res = requests.post('https://httpbin.org/post', data={'q': 'python'})
    print(res.json().keys())  
    print(res.json().values())  
    print(res.json()['form'])  