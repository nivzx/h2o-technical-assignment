from h2o_wave import Q, ui

from helpers.card_helpers import add_card

from util.texts import hero_text


def display_home(q: Q):
    add_card(q, 'article', ui.tall_article_preview_card(
        box=ui.box('hero', height='450px', width='100%'), title='What do I do?',
        image='https://forums.living.ai/uploads/default/original/2X/a/a2565d4cf9a4d1cf125ec49251259b7bff6e9487.jpeg',
        content= hero_text
    ))

    add_card(q, f'speed', ui.tall_info_card(box='horizontal', name='', title='Speed',
                                                  caption='With the lightweight design, the app provides fast feedack', icon='SpeedHigh'))
    
    add_card(q, f'ui', ui.tall_info_card(box='horizontal', name='', title='User Interface',
                                                  caption='Simple and intuitive user interface built with H2O Wave', icon='Heart'))
    
    add_card(q, f'precision', ui.tall_info_card(box='horizontal', name='', title='Accuracy',
                                                  caption='The Neural Network is capable of providing high accurate predictions', icon='AcceptMedium'))
