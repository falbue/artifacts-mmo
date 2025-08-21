from mmo_request import mmo_request
from utils import *

def scan_maps():
    maps_file = "maps.json"
    cache_data = load_file(maps_file)
    if cache_data is not None:
        if isinstance(cache_data, dict) and 'timestamp' in cache_data and 'data' in cache_data:
            cache_time = datetime.fromisoformat(cache_data['timestamp'])
            
        if datetime.now() - cache_time < timedelta(hours=1):
            logger.debug("Данные из кеша")
            return cache_data['data']
    
    logger.debug("Cканирование карт...")
    maps = []
    data = mmo_request("/maps?size=100")
    pages = data["pages"]
    
    for i in range(pages):
        command = f"/maps?size=100&page={i+1}"
        data = mmo_request(command)
        maps.extend(data["data"])
    
    cache_data = {
        'timestamp': datetime.now().isoformat(),
        'data': maps
    }
    
    save_file(maps_file, cache_data)
    return maps
