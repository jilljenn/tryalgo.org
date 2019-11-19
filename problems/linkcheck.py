import urllib.error
from urllib.request import urlopen
from urllib.parse import urlsplit
import time
import yaml


examples = {}
with open('problems.yaml') as f:
    problems = yaml.safe_load(f.read())
    for problem in problems:
        for url in problem['links']:
            domain = urlsplit(url).netloc
            if domain not in examples:
                examples[domain] = url
                print(domain, url)
                dt = time.time()
                try:
                    r = urlopen(url)
                    print('=>', r.getcode(), '{:.3f}s'.format(time.time() - dt))
                except urllib.error.HTTPError:
                    print('=> 404')
                except urllib.error.URLError as e:
                    print('=> error', e)
                except ConnectionResetError:
                    print('=> server hung up')
