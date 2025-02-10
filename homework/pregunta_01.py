# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
import os
import zipfile
import pandas as pd


def extract_zip(zip_path, extract_to):
    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(extract_to)


def read_text_files(base_path, data_type, sentiment):
    folder_path = os.path.join(base_path, data_type, sentiment)
    return [
        {
            "phrase": open(os.path.join(folder_path, file), "r").read(),
            "target": sentiment,
        }
        for file in os.listdir(folder_path)
    ]


def process_dataset(base_path, data_type):
    sentiments = ["negative", "positive", "neutral"]
    dataset = []
    for sentiment in sentiments:
        dataset.extend(read_text_files(base_path, data_type, sentiment))
    return dataset


def save_to_csv(data, output_path, filename):
    os.makedirs(output_path, exist_ok=True)
    pd.DataFrame(data).to_csv(os.path.join(output_path, filename), index=False)


def pregunta_01():
    """
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:

    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    * sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
      o "neutral". Este corresponde al nombre del directorio donde se
      encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```

    """

    zip_path = "files/input.zip"
    base_path = "files/input"
    output_dir = "files/output"

    extract_zip(zip_path, "files")

    train_data = process_dataset(base_path, "train")
    test_data = process_dataset(base_path, "test")

    save_to_csv(train_data, output_dir, "train_dataset.csv")
    save_to_csv(test_data, output_dir, "test_dataset.csv")

