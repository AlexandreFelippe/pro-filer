import pytest
from pro_filer.actions.main_actions import find_duplicate_files


@pytest.fixture
def tmp_files(tmp_path):
    file1 = tmp_path / "file1.txt"
    file1.write_text("Hello")

    file2 = tmp_path / "file2.txt"
    file2.write_text("World")

    file3 = tmp_path / "file3.txt"
    file3.write_text("!")

    return [str(file1), str(file2), str(file3)]


@pytest.fixture
def tmp_files_duplicate(tmp_path):
    file1 = tmp_path / "file1_duplicate.txt"
    file1.write_text("Hello")

    return [str(file1)]


def test_find_duplicate_files_no_duplicates(tmp_files):
    context = {"all_files": tmp_files}
    assert find_duplicate_files(context) == []


def test_find_duplicate_files_with_duplicates(tmp_files, tmp_files_duplicate):
    tmp_files.append(tmp_files_duplicate[0])

    context = {"all_files": tmp_files}
    expected_duplicates = [(tmp_files[0], tmp_files[-1])]
    assert find_duplicate_files(context) == expected_duplicates


def test_find_duplicate_files_missing_file(tmp_files):
    tmp_files.append("non_existent_file.txt")

    context = {"all_files": tmp_files}
    with pytest.raises(ValueError):
        find_duplicate_files(context)
