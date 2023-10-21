import json
import os
import logging
import datetime
import yaml


def read_price_list(path):
    with open(path, "r") as f:
        price_list = json.loads(f.read())
    return price_list


logger = logging.getLogger(__name__)


def setup_logging():
    try:
        os.mkdir("logs")
    except FileExistsError:
        pass
    logging_handlers = [
        logging.StreamHandler(),
        logging.FileHandler(
            f"logs/{datetime.datetime.now().strftime('%Y_%m_%d-%H_%M')}.log"
        ),
    ]
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s.%(msecs)03d | %(name)-30s | %(levelname)-8s | #%(lineno)-5d| %(message)s \n",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=logging_handlers,
    )


def calculate_price(data: dict, price_list: dict):
    total_price = (
        price_list["color"][data["add_color"]]
        + price_list["size"][data["add_size"]]
        + price_list["coverage"][data["add_coverage"]]
    )
    return total_price


def get_dialog_scenario(path):
    with open(path) as f:
        dialog_scenario = yaml.load(f, Loader=yaml.FullLoader)
    return dialog_scenario
