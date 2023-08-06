import hashlib
import uuid
from datetime import datetime, timedelta
from decimal import Decimal
from enum import Enum
from random import random
from typing import Any, Dict, List, Optional, Union

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from dateutil import parser
from numpy import log as ln


class ElementType(Enum):
    Float = "Float"
    Integer = "Integer"
    Date = "Date"
    Text = "Text"


class TechniqueType(Enum):
    NoTechnique = "None"
    Hash = "Hash"
    Aggregate = "Aggregate"
    AddNoise = "AddNoise"
    BlockWords = "BlockWords"


class HashType(Enum):
    PBKDF2 = "PBKDF2"
    SHA256 = "SHA256"


class NoiseType(Enum):
    Laplace = "Laplace"
    Gaussian = "Gaussian"


class WordBlockType(Enum):
    Mask = "Mask"
    Tokenize = "Tokenize"


class PrecisionOnDate(Enum):
    Second = "Second"
    Minute = "Minute"
    Hour = "Hour"
    Day = "Day"
    Month = "Month"
    Year = "Year"


# hash
def hash_string(
    element_to_hash: Union[str, float, int],
    hash_function: HashType,
    salt: Optional[str],
) -> str:
    if not element_to_hash:
        return ""

    # help: https://cryptography.io/en/latest/hazmat/primitives/key-derivation-functions/
    if hash_function == HashType.PBKDF2 and salt:
        byte_like_salt = salt.encode("ascii")
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=byte_like_salt,
            iterations=390000,
        )
        bytes_like_element = str(element_to_hash).encode("utf-8")
        result = kdf.derive(bytes_like_element)
        return result.hex()
    elif hash_function == HashType.SHA256 and salt:
        result_2: str = hashlib.sha256(
            salt.encode() + str(element_to_hash).encode("utf-8")
        ).hexdigest()
        return result_2
    elif hash_function == HashType.SHA256 and not salt:
        result_3: str = hashlib.sha256(str(element_to_hash).encode("utf-8")).hexdigest()
        return result_3
    else:
        # TODO: throw an error on else
        print("Error in json config > Hash technique")
        return element_to_hash


# aggregate/round number
def round_num(number_to_aggregate: str, precision: int) -> float:
    float_to_aggregate = float(number_to_aggregate)
    rounded: float = round(float_to_aggregate, -precision)
    return rounded


# add noise on numbers
def add_noise_number(
    element_to_noise: str, noise_type: NoiseType, standard_deviation: float
) -> float:
    float_to_noise = float(element_to_noise)
    if noise_type == NoiseType.Laplace:
        return laplace_noise_on_num(float_to_noise, standard_deviation)
    elif noise_type == NoiseType.Gaussian:
        return gaussian_noise_on_num(float_to_noise, standard_deviation)
    else:
        # TODO: throw an error on else
        print("Error in json config > Add noise technique")
        return float(0)


def gaussian_noise_on_num(number_to_noise: float, standard_deviation: float) -> float:
    x1 = 0.0
    x2 = 0.0
    w = 1.0
    while w >= 1.0:
        x1 = 2.0 * random() - 1.0
        x2 = 2.0 * random() - 1.0
        w = x1 * x1 + x2 * x2
    w = pow((-2.0 * ln(w)) / w, 2)
    y1 = x1 * w
    return number_to_noise + standard_deviation * y1


def laplace_noise_on_num(number_to_noise: float, standard_deviation: float):
    def sgn(x):
        return -1 if x < 0 else 1

    u = random() - 0.5
    result = number_to_noise - standard_deviation * sgn(u) * ln(1 - 2 * abs(u))
    return float(result)


# tokenize words
def tokenize_words(initial_phrase: str, word_dict_with_token: Dict[str, str]):
    if not initial_phrase:
        return ""

    def replace_words(word: str):
        return (
            word_dict_with_token[word.lower()]
            if word.lower() in word_dict_with_token
            else word
        )

    return (" ").join([replace_words(word) for word in initial_phrase.split()])


# block words
def mask_words(initial_phrase: str, word_list: List[str]) -> str:
    if not initial_phrase:
        return ""

    replacers: Dict[str, str] = {}
    for value in word_list:
        replacers[value.lower()] = "XXXX"

    def replace_words(word):
        if word.lower() in replacers:
            return replacers[word.lower()]
        else:
            return word

    string_arr = initial_phrase.split()
    result = map(replace_words, string_arr)
    return (" ").join(result)


# round datetime
def round_time(string_date: str, precision: PrecisionOnDate) -> datetime:
    # round function for minute, hour and day
    def round_min_hour_day(date: datetime, round_to: int):
        seconds = (date - date.min).seconds
        rounding = (seconds + round_to / 2) // round_to * round_to
        return date + timedelta(0, rounding - seconds, -date.microsecond)

    parsed_date = parser.parse(string_date)

    if precision == PrecisionOnDate.Minute:
        round_to = 60
        return round_min_hour_day(parsed_date, round_to)
    elif precision == PrecisionOnDate.Hour:
        round_to = 60 * 60
        return round_min_hour_day(parsed_date, round_to)
    elif precision == PrecisionOnDate.Day:
        round_to = 60 * 60 * 24
        return round_min_hour_day(parsed_date, round_to)
    elif precision == PrecisionOnDate.Month:
        d = datetime(parsed_date.year, parsed_date.month, 1)
        return d
    elif precision == PrecisionOnDate.Year:
        d = datetime(parsed_date.year, 1, 1)
        return d
    else:
        # TODO: throw an error on else
        print("Error in json config > Aggregate date technique")
        return parsed_date


# noise on date
def noise_on_date(
    utc_date: str,
    noise_type: NoiseType,
    precision_type: PrecisionOnDate,
    deviation: Union[float, int],
) -> datetime:
    date_object = parser.parse(utc_date)
    my_unix = datetime.timestamp(date_object)

    if precision_type == PrecisionOnDate.Second:
        deviation = deviation
    if precision_type == PrecisionOnDate.Minute:
        deviation = deviation * 60
    if precision_type == PrecisionOnDate.Hour:
        deviation = deviation * 60 * 60
    if precision_type == PrecisionOnDate.Day:
        deviation = deviation * 60 * 60 * 24
    if precision_type == PrecisionOnDate.Month:
        deviation = deviation * 60 * 60 * 24 * 30.5
    if precision_type == PrecisionOnDate.Year:
        deviation = deviation * 60 * 60 * 24 * 30.5 * 365

    my_unix = (
        gaussian_noise_on_num(my_unix, deviation)
        if noise_type == NoiseType.Gaussian
        else laplace_noise_on_num(my_unix, deviation)
    )

    # prevent my_unix for going out of range
    if my_unix < 0:
        my_unix = -my_unix
    if my_unix > 99999999999:
        return datetime.max
    if my_unix < -9999999999:
        return datetime.min
    else:
        return datetime.fromtimestamp(int(my_unix))


# get time
def get_time_now() -> str:
    return str(datetime.now())


# format date
def format_date(date_to_format: str) -> datetime:
    return parser.parse(date_to_format)


# round float with same digits number as input
def round_float(original: str, num_to_round: float) -> float:
    return round(num_to_round, abs(Decimal(original).as_tuple().exponent))


# get word_list
def get_blocked_words(config_metadata: Any) -> Dict[int, Dict[str, str]]:
    dataset_word_list: Dict[int, Dict[str, str]] = {}
    for colum in config_metadata:
        if (
            TechniqueType(colum["technique"]) == TechniqueType.BlockWords
            and WordBlockType(colum["technique_options"]["block_type"])
            == WordBlockType.Tokenize
        ):
            word_list = colum["technique_options"]["word_list"]
            key = colum["key"]
            dataset_word_list[key] = {}
            for word in word_list:
                dataset_word_list[key][word] = str(uuid.uuid4())
    return dataset_word_list
