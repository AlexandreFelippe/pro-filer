import pytest
from pro_filer.actions.main_actions import show_disk_usage
from pro_filer.cli_helpers import _get_printable_file_path


@pytest.fixture
def empty_context_file():
    return {"all_files": []}


@pytest.fixture
def tmp_files(tmp_path):
    file1 = tmp_path / "file_1.txt"
    file2 = tmp_path / "file_2.txt"
    file3 = tmp_path / "file_3.txt"

    file1.touch()
    file1.write_text("Hello")
    file2.touch()
    file2.write_text("World")
    file3.touch()
    file3.write_text("!")

    return [str(file1), str(file2), str(file3)]


def test_show_disk_usage_empty_context(empty_context_file, capsys):
    show_disk_usage(empty_context_file)

    captured = capsys.readouterr().out

    assert captured == "Total size: 0\n"


def test_show_disk_usage(tmp_files, capsys):
    context = {"all_files": tmp_files}
    show_disk_usage(context)

    file1 = f"'{_get_printable_file_path(tmp_files[0])}':".ljust(70)
    file2 = f"'{_get_printable_file_path(tmp_files[1])}':".ljust(70)
    file3 = f"'{_get_printable_file_path(tmp_files[2])}':".ljust(70)

    captured = capsys.readouterr().out

    expected_output = (
        f"{file1} 5 (45%)\n"
        + f"{file2} 5 (45%)\n"
        + f"{file3} 1 (9%)\n"
        + "Total size: 11\n"
    )
    assert captured == expected_output
