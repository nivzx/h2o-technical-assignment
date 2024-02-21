import h2o

from h2o_wave import Q, ui

async def init(q: Q, home) -> None:
    h2o.init()

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
        box='header', title='iHeal', subtitle="An AI Powered Cardiovascular Health Predictor",
        image='https://media.istockphoto.com/id/949119664/vector/cute-white-doctor-robot-modern-health-care-flat-editable-vector-illustration-clip-art.jpg?s=612x612&w=0&k=20&c=Tp7_la5mgePZ2mkOk_17jX0f-vorLZmbT9JOTDyG4gw=',
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
