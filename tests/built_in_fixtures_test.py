import pytest

from src.hex_converter import (  # noqa: F401
    main,
    print_hexadecimal_to_decimal,
    write_hexadecimal_to_decimal,
)

# aplica o marcador de dependency para todos os testes do arquivo
pytestmark = pytest.mark.dependency  # NÃO REMOVA ESSA LINHA


@pytest.fixture
def test_monkeypatch(monkeypatch):
    def mock_input(_):
        return "a"

    monkeypatch.setattr("builtins.input", mock_input)
    assert main() == 10


def test_capsys(capsys):
    print_hexadecimal_to_decimal("a")
    captured = capsys.readouterr()
    assert captured.out == "10\n"
    assert captured.err == ""


def test_tmp_path(tmp_path):
    output_file = tmp_path / "output.txt"
    write_hexadecimal_to_decimal("a", output_file)
    assert output_file.read_text() == "10"
