import eel
import logging
from src import utils

logger = logging.getLogger(__name__)


@eel.expose
def click_button(data):
    tmp1 = utils.test()
    tmp = tmp1.insert_database(data)
