import eel
import logging
from src import utils

logger = logging.getLogger(__name__)


@eel.expose
def click_button(name):
    tmp = 'Button on click ' + str(name)
    tmp1 = utils.test()
    tmp1.print_string(tmp)
