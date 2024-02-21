import h2o

from h2o_wave import main, app, Q, ui, on, run_on, data

from helpers.card_helpers import clear_cards, add_card
from pages.home import display_home
from pages.model import display_model
from pages.results import display_results
from pages.form import display_form, handle_interaction

# Initialize H2O once when the app starts
h2o.init()


@on('#home')
async def home(q: Q):
    clear_cards(q)  # When routing, drop all the cards except of the main ones (header, sidebar, meta).
    display_home(q)

@on('#dataset')
async def dataset(q: Q):
    clear_cards(q)  # When routing, drop all the cards except of the main ones (header, sidebar, meta).

    display_model(q)
    
    # add_card(q, 'table', ui.form_card(box='vertical', items=[ui.table(
    #     name='table',
    #     downloadable=True,
    #     resettable=True,
    #     groupable=True,
    #     columns=[
    #         ui.table_column(name='text', label='Process', searchable=True),
    #         ui.table_column(name='tag', label='Status', filterable=True, cell_type=ui.tag_table_cell_type(
    #             name='tags',
    #             tags=[
    #                 ui.tag(label='FAIL', color='$red'),
    #                 ui.tag(label='DONE', color='#D2E3F8', label_color='#053975'),
    #                 ui.tag(label='SUCCESS', color='$mint'),
    #             ]
    #         ))
    #     ],
    #     rows=[
    #         ui.table_row(name='row1', cells=['Process 1', 'FAIL']),
    #         ui.table_row(name='row2', cells=['Process 2', 'SUCCESS,DONE']),
    #         ui.table_row(name='row3', cells=['Process 3', 'DONE']),
    #         ui.table_row(name='row4', cells=['Process 4', 'FAIL']),
    #         ui.table_row(name='row5', cells=['Process 5', 'SUCCESS,DONE']),
    #         ui.table_row(name='row6', cells=['Process 6', 'DONE']),
    #     ])
    # ]))


@on('#results')
async def results(q: Q):
    clear_cards(q)  # When routing, drop all the cards except of the main ones (header, sidebar, meta).

    await display_results(q)

    # for i in range(12):
    #     add_card(q, f'item{i}', ui.wide_info_card(box=ui.box('grid', width='400px'), name='', title='Tile',
    #                                               caption='Lorem ipsum dolor sit amet'))


@on('#form')
async def form(q: Q):
    q.page['sidebar'].value = '#form'
    # When routing, drop all the cards except of the main ones (header, sidebar, meta).
    # Since this page is interactive, we want to update its card
    # instead of recreating it every time, so ignore 'form' card on drop.
    clear_cards(q, ['form'])

    display_form(q)

async def init(q: Q) -> None:
    q.page['meta'] = ui.meta_card(box='', layouts=[ui.layout(breakpoint='xs', min_height='100vh', zones=[
        ui.zone('header'),
        ui.zone('content', zones=[
            # Specify various zones and use the one that is currently needed. Empty zones are ignored.
            ui.zone('hero', direction=ui.ZoneDirection.ROW),
            ui.zone('horizontal', direction=ui.ZoneDirection.ROW),
            ui.zone('vertical'),
            ui.zone('form', direction=ui.ZoneDirection.ROW, wrap='around', justify='center'),
            ui.zone('grid', direction=ui.ZoneDirection.ROW, wrap='stretch', justify='center')
        ]),
    ])])
    q.page['header'] = ui.header_card(
        box='header', title='My app', subtitle="Let's conquer the world",
        image='https://cdn.dribbble.com/userupload/2798815/file/original-d8b75e59492e979ad996c39eac216499.png?resize=752x',
        secondary_items=[
            ui.tabs(name='tabs', value=f'#{q.args["#"]}' if q.args['#'] else '#home', link=True, items=[
                ui.tab(name='#home', label='Home'),
                ui.tab(name='#dataset', label='Data'),
                ui.tab(name='#results', label='Results'),
                ui.tab(name='#form', label='Form'),
            ]),
        ],
        items=[
            ui.persona(title='Sheldon Cooper', subtitle='AI Freak | Nerd', size='xs',
                       image='https://img.freepik.com/premium-photo/sheldon-cooper-big-bang-theory-cartoon-character-generative-ai_934475-11474.jpg'),
        ]
    )
    # If no active hash present, render home.
    if q.args['#'] is None:
        await home(q)

@app('/')
async def serve(q: Q):
    # Run only once per client connection.
    if not q.client.initialized:
        q.client.cards = set()
        await init(q)
        q.client.initialized = True

    if(q.args.submit_button):
        print(q.args)
        handle_interaction(q)
        pass

    # Handle routing.
    await run_on(q)
    await q.page.save()

