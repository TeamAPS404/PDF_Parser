import json

def test_get_tag():
    from parse import get_tag
    assert get_tag('<h2>Test H2') == ('h2', 'Test H2')
    assert get_tag('<h3>Test H3') == ('h3', 'Test H3')
    assert get_tag('<p>Test P') == ('p', 'Test P')

def test_make_folder_one_layer_json():
    from parse import make_nested_json
    elements = ['<h2>FIR Copy', '<h3>Complaint Information', '<p>So start by doing...']
    folders = make_nested_json(elements)
    assert len(folders) == 1
    assert folders[0]['value'] == 'FIR Copy'
    assert len(folders[0].children) == 1
    assert folders[0].children[0]['value'] == 'Complaint Information'


def test_make_folder_two_layer_json():
    from parse import make_nested_json
    elements = ['<h2>FIR Copy', '<h3>Complaint Information', '<h3>Status', '<p>So start by doing...', '<h2>State', '<h3>Rewards', '<p>GOLD']
    folders = make_nested_json(elements)
    assert len(folders) == 2
    assert folders[0]['value'] == 'FIR Copy'
    assert len(folders[0].children) == 2
    assert folders[1]['value'] == 'State'


def test_make_folder_ignored_tags():
    from parse import make_nested_json
    elements = ['<h2>FIR Copy', '<s1>small text','<h3>Complaint Information', '<s2>Other text','<p>So start by doing...']
    folders = make_nested_json(elements)
    assert len(folders) == 1
    assert folders[0]['value'] == 'FIR Copy'
    assert len(folders[0].children) == 1
    assert folders[0].children[0]['value'] == 'Complaint Information'

def test_element_ordering():
    from parse import make_nested_json
    elements = ['<h2>FIR Copy', '<h6>some sub section', '<h3>Complaint Information', '<h6>another sub section', '<h3>Status']
    folders = make_nested_json(elements)
    assert len(folders) == 1
    assert folders[0]['value'] == 'FIR Copy'
    assert len(folders[0].children) == 3
    assert folders[0].children[1]['value'] == 'Complaint Information'
    assert folders[0].children[2]['value'] == 'Status'
