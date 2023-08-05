"""Test modules home

"""
import os
import json
import time

from pathlib import Path as Pathlib_path
import eisenradio.lib.eisdb as eis_db
import eisenradio.eisenhome.eishome as eisen_radio
this_mod_dir = os.path.dirname(__file__)


def test_home_blueprint_val(app):
    """ test Blueprint 'eisenHOME'  """
    print('\n ... Begin: Test test_eishome')
    web = app.test_client()
    rv = web.get('/')
    assert rv.status_code == 200
    assert '<title> Your Eisen Radio! </title>' in rv.data.decode('utf-8')
    from eisenradio.eisenhome import routes as home_routes
    # read dir path from imported module
    eisen_home_dir = os.path.dirname(eisen_radio.__file__)
    assert home_routes.eisenhome_bp.template_folder == 'bp_home_templates'
    # flask returns the whole path for static
    assert home_routes.eisenhome_bp.static_folder == os.path.join(eisen_home_dir, 'bp_home_static')
    assert home_routes.eisenhome_bp.static_url_path == '/bp_home_static'
    dir_list = [
        os.path.join(eisen_home_dir, 'bp_home_templates'),
        os.path.join(eisen_home_dir, 'bp_home_static'),
    ]
    assert all([folder if Pathlib_path(folder).is_dir() else False for folder in dir_list])


def test_timer_value_set(app):
    web = app.test_client()
    timer = int(8)
    # set html timer to hours, check if value was set
    rv = web.post('/index_posts_combo',
                  data=dict(timeRecordSelectAll=timer),
                  follow_redirects=True,
                  content_type='application/x-www-form-urlencoded',
                  )
    data = json.loads(rv.get_data(as_text=True))
    assert data == timer


def test_timer_percent_value_get(app):
    """feed timer, assert returned percent status,

    simulates hours on html drop-down
    sleep to wait daemon calculates something
    return some 0.0417 percent stuff for 3 seconds, data {'result': 0.0417} type<class 'float'
    """
    web = app.test_client()
    eisen_radio.combo_master_timer = 2
    time.sleep(3)
    rv = web.get('/index_posts_percent',
                 follow_redirects=True,
                 content_type='application/x-www-form-urlencoded',
                 )
    data = json.loads(rv.get_data(as_text=True))
    assert type(data['result']) is float
    assert data['result'] > 0


def test_cookie_dark_mode(app):
    """cookie set, get, delete in one instance of app, else cookie disappears"""
    web = app.test_client()
    rv = web.get('/cookie_set_dark')
    assert 'Eisenkekse sind die besten' in rv.data.decode('utf-8')

    # json style
    rv = web.get('/cookie_get_dark')
    data = json.loads(rv.get_data(as_text=True))
    assert data['darkmode'] == 'darkmode'

    # client.cookie_jar style
    cookie = next(
        (cookie for cookie in web.cookie_jar if cookie.name == "eisen-cookie"),
        None
    )
    assert cookie is not None
    assert cookie.value == "darkmode"

    rv = app.test_client().post('/cookie_del_dark',
                                headers={"X-Requested-With": "XMLHttpRequest"},
                                follow_redirects=True, )
    cookie = rv.headers.getlist('Set-Cookie')
    cookie_val = cookie[0]  # nice one row list :(
    cookie_list = cookie_val.split(';')
    assert cookie_list[0] == 'eisen-cookie='  # cookie value is set to 0
    assert b'necesito nuevas cookies' in rv.data


def test_meta_title_info_ajax_to_html(app, db_deploy):
    """test endpoint to js output format

    feed title dict and radios_in_view_dict with know values from production ;)
    check if endpoint response has readable format for JavaScript module to write to the correct html element
    each html input text box has the database id of a radio
    """
    web = app.test_client()
    from eisenradio.api import ghettoApi

    ghettoApi.ghetto_radios_metadata_text = {'Korean_Pop': 'OVAN 오반 - I Need You 어떻게 지내',
                                             'BLUES_UK': 'Henrik Freischlader Band - Take The Blame',
                                             'japanese_pop': 'Yoko Kanno and The Seatbelts - Waltz for Zizi'}
    ghettoApi.radios_in_view_dict = {2: 'Korean_Pop', 3: 'BLUES_UK', 6: 'japanese_pop'}

    rv = web.get('/display_info',
                 follow_redirects=True,
                 content_type='application/x-www-form-urlencoded',
                 )
    data = json.loads(rv.get_data(as_text=True))
    assert data['updateDisplay'] == {'2': 'OVAN 오반 - I Need You 어떻게 지내',
                                     '3': 'Henrik Freischlader Band - Take The Blame',
                                     '6': 'Yoko Kanno and The Seatbelts - Waltz for Zizi'}


def test_page_flash_home_route(app):
    """ /page_flash """
    web = app.test_client()
    expected_flash_message = 'Count down timer ended all activities. App restart recommended!'
    rv = web.get('/page_flash')
    parsed = rv.data.decode(encoding="utf-8")
    assert expected_flash_message in parsed


def test_fail_delete_radio_active_listen(app, db_deploy):
    """ /<int:id>/delete  must FAIL, active listen """
    web = app.test_client()
    radio_to_delete = int(3)  # db id of radio
    # set listen button down for radio, no record button pressed
    eisen_radio.status_listen_btn_dict[radio_to_delete] = 1
    eisen_radio.status_record_btn_dict[radio_to_delete] = 0
    rv_db = eis_db.status_read_status_set(False, 'posts', 'title', str(radio_to_delete))
    # get no error message, radio is in db
    assert rv_db != "column not in table posts, status_read_status_set"
    rv = web.post('/' + str(radio_to_delete) + '/delete', follow_redirects=True)  # redirect to index
    parsed = rv.data.decode(encoding="utf-8")
    assert 'Radio is active. No deletion.' in parsed  # flash message


def test_fail_delete_radio_active_record(app, db_deploy):
    """ /<int:id>/delete  must FAIL, active Record """
    web = app.test_client()
    radio_to_delete = int(3)
    # set rec button down for radio, no listen button pressed
    eisen_radio.status_listen_btn_dict[radio_to_delete] = 0
    eisen_radio.status_record_btn_dict[radio_to_delete] = 1
    rv = web.post('/' + str(radio_to_delete) + '/delete', follow_redirects=True)  # redirect to index
    parsed = rv.data.decode(encoding="utf-8")
    assert 'Radio is active. No deletion.' in parsed  # flash message


def test_success_delete_radio(app, db_deploy):
    """ /<int:id>/delete  , last query must FAIL  """
    web = app.test_client()
    radio_to_delete = int(3)
    # no button is down
    eisen_radio.status_listen_btn_dict[radio_to_delete] = 0
    eisen_radio.status_record_btn_dict[radio_to_delete] = 0
    rv = web.post('/' + str(radio_to_delete) + '/delete', follow_redirects=True)  # DELETE
    parsed = rv.data.decode(encoding="utf-8")
    assert 'was successfully deleted' in parsed

    # query MUST fail, radio not in store!
    rv_db = eis_db.status_read_status_set(False, 'posts', 'title', str(radio_to_delete))
    assert rv_db == "column not in table posts, status_read_status_set"


print('--- fin ----')

# print(f'\n ,,,,,,,,,, data {data}\n')
