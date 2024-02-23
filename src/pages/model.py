import pandas as pd
import h2o

from h2o_wave import Q, ui

from helpers.card_helpers import add_card

from util.texts import model_info
    

def display_model(q: Q):

    h2o.connect(ip='localhost', port=54321)
    
    complete_data = h2o.import_file('https://h2o-tech-assignment.s3.amazonaws.com/data/heart_failure_complete.csv')

    # Define columns for the table
    total_columns = [
        ui.table_column(name=col, label=col)
        for col in complete_data.col_names
    ]

    # Populate rows for the table
    total_rows = [
        ui.table_row(
            name=f'row_{index}',
            cells=[str(cell) for cell in row])
        for index, row in complete_data.as_data_frame(use_pandas='True').iterrows()
    ]

    add_card(q, 'complete_data', ui.form_card(
        title='Complete Dataset',
        box='vertical',
        items=[
            ui.table(
                name='complete_data',
                columns=total_columns,
                rows=total_rows,
                groupable=True,
                downloadable=True,
                height='500px',  # Set desired height
            )
        ]
    ))

    add_card(q, 'info', ui.wide_info_card(
        box='horizontal',
        name='info_card',
        title='How is it done?',
        caption=model_info,
        image='https://img.freepik.com/premium-photo/cartoon-character-doctor-with-stethoscope-his-hand_1057-22790.jpg'
        ))
    