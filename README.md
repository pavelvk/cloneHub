# Batch clone GitHub repositories


Clone all you own repositories or github user open repositories.


## Install script

1. [Clone this repository](https://github.com/pavelvk/cloneHub.git)
    ```sh
    $ git clone https://github.com/pavelvk/cloneHub.git
    ```

2. Create python VENV
     ```sh
    $ python3 -m venv myvenv
    ```

3. Activate new VENV
     ```sh
    $ source myvenv/bin/activate
    ```

4. Install requirements
     ```sh
    (myvenv)$ pip install -r requirements.txt
    ```

5. Ready!


## Usage

### Command-line arguments
```
    -h, --help     help message
    --token TOKEN  You GitHub auth token (required)
    --user USER    GitHub username to clone from (not required)
    --path PATH    Path to save repos (required)
```    

### Examples

#### Clone all you repository in current folder
```sh
(myvenv)$ python clone.py --token=ghp_AAAAAAAAAAAAAAAAAAAAAAAAAAA
```

#### Clone all you repository in folder '/media/back/myrepos'
```sh
(myvenv)$ python clone.py --token=ghp_AAAAAAAAAAAAAAAAAAAAAAAAAAA --path=/media/back/myrepos
```

#### Clone all open repository of user QWERTYYTREWQQWERTY42 in current folder
```sh
(myvenv)$ python clone.py --token=ghp_AAAAAAAAAAAAAAAAAAAAAAAAAAA --user=QWERTYYTREWQQWERTY42
```

#### Clone all open repository of user QWERTYYTREWQQWERTY42 in folder '/media/back/myrepos'
```sh
(myvenv)$ python clone.py --token=ghp_AAAAAAAAAAAAAAAAAAAAAAAAAAA --user=QWERTYYTREWQQWERTY42 --path=/media/back/myrepos
```
