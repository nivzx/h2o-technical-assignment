import h2o

from h2o_wave import Q, ui

from helpers.card_helpers import add_card

def load_data(url):
    return 

def load_model(url):
    return h2o.import_mojo(url)

def display_model(q: Q):
    print("Hi")

    h2o.init()

    data = h2o.import_file('https://heart-failure-dataset.s3.amazonaws.com/heart_failure.csv')

    # Define columns for the table
    columns = [
        ui.table_column(name=col, label=col)
        for col in data.col_names
    ]

    # Populate rows for the table
    rows = [
        ui.table_row(
            name=f'row_{index}',
            cells=[str(cell) for cell in row])
        for index, row in enumerate(data)
    ]

    # Add the table to the UI
    q.page['example_table'] = ui.form_card(
        box='1 1 6 4',
        items=[
            ui.table(
                name='example_table',
                columns=columns,
                rows=rows,
                groupable=True,
                height='500px',  # Set desired height
            )
        ]
    )