import pandas as pd

def save_data(data: dict, output_path: str = 'result.xlsx') -> None:
    """
    Сохранение данных в Excel файл
    :param data: Входные данные {title: value}
    :param output_path: Путь сохранения
    :return:
    """
    df = pd.DataFrame([data])

    try:
        with pd.ExcelWriter(output_path, mode='a', if_sheet_exists='overlay', engine='openpyxl') as writer:
            if "Data" not in writer.sheets:
                df.to_excel(writer, index=False, sheet_name='Data')
            else:
                df.to_excel(writer, index=False, sheet_name='Data', header=False, startrow=writer.sheets['Data'].max_row)
    except FileNotFoundError:
        df.to_excel(output_path, index=False, sheet_name='Data')