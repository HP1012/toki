import logging
import eel

import src.web
import src.const as CONST

logger = logging.getLogger(__name__)

def start_eel(mode='chrome'):
    '''Start Eel'''
    # def on_close(page, sockets):
    #     pass

    eel.init('web')

    options = {
        'mode': mode,
        'host': 'localhost',
        'port': CONST.PORT
    }

    logger.debug("Start app in mode %s", mode)

    try:
        # web.generate_html()
        #/home/hp1012/.local/lib/python3.8/site-packages/eel/__init__.py line 141
        eel.start('index.html', options=options,suppress_error=True,close_callback=False,disable_cache=True)

    except Exception as e:
        logger.exception(e)
        if mode == 'chrome':
            start_eel('edge')

if __name__ == "__main__":
    logger.debug("Start app in mode %s", "OK")
    start_eel()