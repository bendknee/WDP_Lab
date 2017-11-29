import requests

DRONE_API       = 'https://www.enterkomputer.com/api/product/drone.json'
SOUNDCARD_API   = 'https://www.enterkomputer.com/api/product/soundcard.json'
OPTICAL_API     = 'https://www.enterkomputer.com/api/product/optical.json'

def get_drones():
    drones = requests.get(DRONE_API)
    return drones

# lengkapi pemanggilan utk SOUNDCARD_API dan OPTICAL_API untuk mengerjakan CHALLENGE
def get_soundcards():
    soundcards = requests.get(SOUNDCARD_API)
    return soundcards

def get_opticals():
    opticals = requests.get(OPTICAL_API)
    return opticals
