"""cosmian_lib_anonymization.anonymize_dataset function"""

from typing import Any, Dict, Union

from pandas import DataFrame

import cosmian_lib_anonymization.anonymization as anonymization


def anonymize_dataset(data_frame: DataFrame, config_file: Dict[str, Any]):
    """Apply config anonymization to dataframe.

    Parameters
    ----------
    data_frame : DataFrame
    config_file : Dict[str, Any]

    """
    data_frame = data_frame.fillna("")
    config_metadata = config_file["input_dataset"]["dataset_metadata"]
    blocked_words_tokens: Dict[int, Dict[str, str]] = anonymization.get_blocked_words(
        config_metadata
    )

    # Apply technique
    def apply_technique(
        element: Union[str, float, int],
        element_type,
        technique: anonymization.TechniqueType,
        technique_options: Any,
    ):
        # None
        if technique == anonymization.TechniqueType.NoTechnique:
            return element

        # Hash
        elif technique == anonymization.TechniqueType.Hash:
            return apply_hash(element, technique_options)

        # Aggregate on number
        elif technique == anonymization.TechniqueType.Aggregate:
            return apply_aggregate(element, element_type, technique_options)

        # Noise
        elif technique == anonymization.TechniqueType.AddNoise:
            return apply_noise(element, element_type, technique_options)

        # Block word
        elif technique == anonymization.TechniqueType.BlockWords:
            return apply_block_words(element, element_type, technique_options)

        # default
        else:
            return element

    def apply_hash(element: Union[str, float, int], technique_options: Any) -> str:
        try:
            salt = technique_options["salt"]
        except KeyError:
            salt = None
        hashed = anonymization.hash_string(
            element,
            anonymization.HashType(technique_options["hash_function"]),
            salt,
        )
        return hashed

    def apply_aggregate(
        element: Union[str, float, int],
        element_type: anonymization.ElementType,
        technique_options: Any,
    ) -> str:
        # on number
        if (
            element_type == anonymization.ElementType.Integer
            or element_type == anonymization.ElementType.Float
        ):
            if element:
                aggregated = anonymization.round_num(
                    element, technique_options["precision"]
                )
                if element_type == "Integer":
                    aggregated = int(aggregated)
                return str(aggregated)
            else:
                return str(element)

        # on date
        elif element_type == anonymization.ElementType.Date:
            if element:
                agreggated_date = anonymization.round_time(
                    element,
                    anonymization.PrecisionOnDate(technique_options["precision"]),
                )
                return str(agreggated_date)
            else:
                return str(element)
        else:
            return str(element)

    def apply_noise(
        element: Union[str, float, int],
        element_type: anonymization.ElementType,
        technique_options: Any,
    ) -> str:
        # on number
        if (
            element_type == anonymization.ElementType.Integer
            or element_type == anonymization.ElementType.Float
        ):
            if element:
                noisy = anonymization.add_noise_number(
                    element,
                    anonymization.NoiseType(technique_options["noise_type"]),
                    technique_options["standard_deviation"],
                )
                if element_type == anonymization.ElementType.Integer:
                    noisy = int(noisy)
                else:
                    noisy = anonymization.round_float(element, noisy)
                return str(noisy)
            else:
                return str(element)

        # on date
        elif element_type == anonymization.ElementType.Date:
            if element:
                noisy_date = anonymization.noise_on_date(
                    element,
                    anonymization.NoiseType(technique_options["noise_type"]),
                    anonymization.PrecisionOnDate(technique_options["precision_type"]),
                    technique_options["standard_deviation"],
                )
                return str(noisy_date)
            else:
                return str(element)

    def apply_block_words(
        element: Union[str, float, int],
        element_type: anonymization.ElementType,
        technique_options: Any,
    ) -> str:
        if element_type == anonymization.ElementType.Text:
            if (
                anonymization.WordBlockType(technique_options["block_type"])
                == anonymization.WordBlockType.Mask
            ):
                masked = anonymization.mask_words(
                    element, technique_options["word_list"]
                )
                return masked
            elif (
                anonymization.WordBlockType(technique_options["block_type"])
                == anonymization.WordBlockType.Tokenize
            ):
                tokenized = anonymization.tokenize_words(
                    element, blocked_words_tokens[index]
                )
                return tokenized
            else:
                print("Error in json config > Block words technique")
                return element
        else:
            return element

    for index, config in enumerate(config_metadata):
        element_type = anonymization.ElementType(config["type"])
        technique = anonymization.TechniqueType(config["technique"])
        technique_options = {}
        if technique != anonymization.TechniqueType.NoTechnique:
            try:
                technique_options = config["technique_options"]
            except KeyError:
                technique_options = None

            data_frame.iloc[:, index] = data_frame.iloc[:, index].apply(
                apply_technique,
                args=(
                    element_type,
                    technique,
                    technique_options,
                ),
            )

    return data_frame
