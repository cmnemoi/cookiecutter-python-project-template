from {{ cookiecutter.project_name.lower().replace(' ', '_') }}.main import hello_world


def test_hello_world():
    assert hello_world() == "Hello, World!"
