import requests as req
import json
import pathlib
import git
import argparse
import sys



HEADERS = {'Authorization': ""}

URL_REPOS_LIST = 'https://api.github.com/user'  #repos
PER_PAGE = 10



def paginator(url, page):
    '''paginator generator routine'''

    url_send = f"{url}?page={str(page)}&per_page={str(PER_PAGE)}"
    res_json = req.get(url_send, headers=HEADERS).json()

    yield res_json

    if len(res_json)==0: return

    page += 1

    yield from paginator(url, page)





def main():
    ''' core routine '''  

    parser = argparse.ArgumentParser("GitHub cloner")
    parser.add_argument("--token", required=True, help="You GitHub auth token", type=str)
    parser.add_argument("--user", required=False, help="GitHub username to clone from", type=str)
    parser.add_argument("--path", required=False, help="Path to save repos", type=str)
    args = parser.parse_args()


    curr_folder = pathlib.Path(__file__).parent.resolve()
    if args.path is not None:
        curr_folder = args.path.strip()

    url = URL_REPOS_LIST
    if args.user is not None:
        url += 's/' + args.user.strip() + '/'  
    else:
        url += '/'    
    url += 'repos'

      
    HEADERS['Authorization'] = f"token {args.token}"

    for res_json in paginator(url, 1):
        if isinstance(res_json, dict):
            if 'message' in res_json:
                print(res_json['message'])
                sys.exit()

        for level in res_json:
            print(f"cloning {level['clone_url']}")
            git.Git(curr_folder).clone(level['clone_url'])


if __name__ == '__main__':
    main()