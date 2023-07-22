# pyyt
Python script to download all videos as audio from a given YouTube playlist

-------------------
### Attribution ###

An abstraction of [youtube-dl](https://github.com/rg3/youtube-dl) for my specific use case.
Thanks to [rg3](https://github.com/rg3) and everyone that contributed.

-------------------
### Installation

* Clone the repo: `git clone https://github.com/patillacode/pyyt.git`

* Move into the repo folder: `cd pyyt`

* Create a virtual environment: `python3 -m venv venv`

* Activate the virtualenv: `source venv/bin/activate`

* Install requirements: `pip install -r requirements.txt`

---------

### Usage
* Run `python pyyt.py`

**Note:** Audio files will be downloaded into the `./downloads` folder

-----------
### Example

```bash
Welcome to pyyt - Select your option:

1 - Download an entire playlist as audio

2 - Download a single video as audio

Write your selection: 1
Please insert the YouTube playlist URL: https://www.youtube.com/playlist?list=PLOr27fEnfYc5a6p1auEgwWxGiGbe55rHR
[youtube:tab] PLOr27fEnfYc5a6p1auEgwWxGiGbe55rHR: Downloading webpage
[download] Downloading playlist: music10
...
```
