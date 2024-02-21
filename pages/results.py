import h2o
import pandas as pd

from h2o_wave import Q, ui

from helpers.card_helpers import add_card



async def display_results(q: Q):
    h2o.connect(ip='localhost', port=54321)
    
    model = h2o.import_mojo('https://h2o-tech-assignment.s3.amazonaws.com/model/heart_failure_dl_model.zip')

    valid_data = h2o.import_file('https://h2o-tech-assignment.s3.amazonaws.com/data/heart_failure_complete.csv')

    predictions = model.predict(valid_data)

    # Convert predictions to a pandas DataFrame
    predictions_df = predictions.as_data_frame()

    # Extract predicted values
    predicted_values = predictions_df['predict'].values

    # Define columns for the table
    valid_columns = [
        ui.table_column(name=col, label=col)
        for col in valid_data.col_names
    ]

    # Create a new column in valid_data to store the result of comparison
    valid_data['Prediction'] = h2o.H2OFrame(['Success' if a == b else 'Fail' for a, b in zip(valid_data['HeartDisease'].as_data_frame().values.flatten(), predicted_values)])


    valid_columns.append(
        ui.table_column(name='tag', label='Prediction', filterable=True, cell_type=ui.tag_table_cell_type(
            name='tags',
            tags=[
                ui.tag(label='Fail', color='$red'),
                ui.tag(label='Success', color='$mint'),
            ]
        ))
    )

    valid_rows = [
        ui.table_row(
            name=f'row_{index}',
            cells=[str(cell) for cell in row])
        for index, row in valid_data.as_data_frame(use_pandas='True').iterrows()
    ]

    
    
    add_card(q, 'result_data', ui.form_card(
        title='Complete Dataset',
        box='vertical',
        items=[
            ui.table(
                name='result_data',
                columns=valid_columns,
                rows=valid_rows,
                groupable=True,
                downloadable=True,
                height='500px',  # Set desired height
            )
        ]
    ))

    add_card(q, 'form', ui.form_card(box='from-row1', items=[
        ui.textbox(name='textbox1', label='Textbox 1'),
        ui.textbox(name='textbox2', label='Textbox 1'),
        ui.textbox(name='textbox3', label='Textbox 1'),
        ui.buttons(justify='end', items=[
            ui.button(name='page4_step2', label='Next', primary=True),
        ]),
    ]))
    # Create a table to display results
  