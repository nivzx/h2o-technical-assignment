import h2o

from h2o_wave import main, app, Q, ui, on, run_on

from helpers.card_helpers import clear_cards
from helpers.app_helper import init

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


@on('#results')
async def results(q: Q):
    clear_cards(q)  # When routing, drop all the cards except of the main ones (header, sidebar, meta).
    await display_results(q)

@on('#form')
async def form(q: Q):
    clear_cards(q, ['form'])
    display_form(q)

@app('/')
async def serve(q: Q):
    # Run only once per client connection.
    if not q.client.initialized:
        q.client.cards = set()
        await init(q, home)
        q.client.initialized = True

    if(q.args.submit_button):
        await handle_interaction(q)
        pass

    # Handle routing.
    await run_on(q)
    await q.page.save()

